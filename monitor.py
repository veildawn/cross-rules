#!/usr/bin/env python3
"""
Surge traffic monitor - identifies FINAL,DIRECT hits that may need rules.
Usage: python3 monitor.py [--watch]
"""
import json, sys, time, subprocess
from collections import defaultdict
from datetime import datetime
import urllib.request

API_KEY = "codex"
API_BASE = "http://127.0.0.1:6171"

KNOWN_CN = {
    "weixin", "wechat", "qq.com", "qpic.cn", "qlogo.cn", "weixinbridge",
    "feishu.cn", "lark", "bytedance", "douyin", "toutiao", "baidu",
    "alibaba", "aliyun", "taobao", "alipay", "jd.com", "tmall",
    "meituan", "dianping", "bilibili", "163.com", "126.com", "sina",
    "weibo", "zhihu", "iqiyi", "youku", "kuaishou", "xiaohongshu",
}

PROXY_HINTS = {
    "intercom.io": ("claude.list", "Claude.app 支持聊天 (被墙)"),
    "expo.dev": ("developer.list", "Expo 开发工具"),
    "anthropic.com": ("claude.list", "Anthropic/Claude"),
    "openai.com": ("ai.list", "OpenAI"),
    "cloudflare.com": ("cloudflare.list", "Cloudflare"),
}

def fetch(path):
    req = urllib.request.Request(
        f"{API_BASE}{path}",
        headers={"X-Key": API_KEY}
    )
    with urllib.request.urlopen(req, timeout=5) as r:
        return json.loads(r.read())

def is_cn_domain(host):
    host = host.lower()
    return any(kw in host for kw in KNOWN_CN)

def domain_suffix(host):
    parts = host.rstrip(".").split(".")
    if len(parts) >= 2:
        return ".".join(parts[-2:])
    return host

def analyze(reqs, verbose=False):
    by_rule = defaultdict(list)
    for r in reqs:
        rule = r.get("rule", "UNKNOWN")
        host = r.get("URL", "").split(":")[0]
        policy = r.get("policyName", "UNKNOWN")
        proc = r.get("pathForStatistics", "")
        app = proc.split("/")[-1].replace(".app", "") if proc else "?"
        by_rule[rule].append({
            "host": host, "policy": policy,
            "proc": proc, "app": app,
            "id": r.get("id"), "failed": r.get("failed"),
            "status": r.get("status"),
        })

    print(f"\n{'='*60}")
    print(f"  Surge 流量分析  {datetime.now().strftime('%H:%M:%S')}")
    print(f"{'='*60}")
    print(f"  总请求数: {len(reqs)}")
    print()
    print("  规则命中分布:")
    for rule, items in sorted(by_rule.items(), key=lambda x: -len(x[1])):
        print(f"    {rule:<40s} {len(items):4d} 次")

    print()
    final = by_rule.get("FINAL", [])
    if not final:
        print("  无 FINAL 命中，所有流量均已匹配规则。")
        return

    print(f"  FINAL 命中 ({len(final)} 次) - 可能需要添加规则:")
    print()

    host_info = defaultdict(lambda: {"count": 0, "apps": set(), "policy": "", "failed": 0})
    for item in final:
        h = item["host"]
        host_info[h]["count"] += 1
        host_info[h]["apps"].add(item["app"])
        host_info[h]["policy"] = item["policy"]
        if item.get("failed"):
            host_info[h]["failed"] += 1

    suggestions = []
    for host, info in sorted(host_info.items(), key=lambda x: -x[1]["count"]):
        suffix = domain_suffix(host)
        apps = ", ".join(sorted(info["apps"]))
        cn = is_cn_domain(host)
        hint = None
        for kw, (lst, desc) in PROXY_HINTS.items():
            if kw in host:
                hint = (lst, desc)
                break

        status = ""
        if info["failed"] > 0:
            status = f" [!{info['failed']}次失败]"
        if cn:
            status += " [CN直连正常]"

        print(f"    {host:<50s} x{info['count']:3d}  via {info['policy']:<8s}  [{apps}]{status}")
        if hint and not cn:
            print(f"      -> 建议加入 {hint[0]}: {hint[1]}")
            suggestions.append((host, suffix, hint[0], hint[1]))

    if suggestions:
        print()
        print("  建议新增规则:")
        for host, suffix, lst, desc in suggestions:
            print(f"    文件: mihomo/{lst}")
            print(f"    规则: DOMAIN-SUFFIX,{suffix}")
            print(f"    说明: {desc}")
            print()

watch_mode = "--watch" in sys.argv
seen_ids = set()

try:
    if watch_mode:
        print("监听模式 (Ctrl+C 退出)...")
        while True:
            d = fetch("/v1/requests/recent")
            reqs = d.get("requests", [])
            new = [r for r in reqs if r["id"] not in seen_ids]
            seen_ids.update(r["id"] for r in reqs)
            if new:
                analyze(new, verbose=True)
            time.sleep(3)
    else:
        d = fetch("/v1/requests/recent")
        analyze(d.get("requests", []))
except KeyboardInterrupt:
    print("\n停止监听。")
except Exception as e:
    print(f"错误: {e}")
    print("请确认 Surge HTTP API 已启用 (http-api = codex@127.0.0.1:6171)")
