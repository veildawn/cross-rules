# Cross Rules

规则集合仓库，用于存放和管理各类规则配置。

## 目录结构

```
cross-rules/
├── README.md              # 项目说明文档
└── mihomo/                # mihomo 规则集
    ├── ai.list            # AI 网站与工具规则
    ├── developer.list     # 程序员常用网站规则
    ├── dns.list           # 国外 DNS 服务规则
    └── lan.list           # 局域网 / 私有网络规则
```

## 规则列表

| 文件 | 说明 |
|------|------|
| `mihomo/ai.list` | AI 网站与工具 |
| `mihomo/developer.list` | 程序员常用网站 |
| `mihomo/dns.list` | 国外 DNS 服务 |
| `mihomo/lan.list` | 局域网 IPv4/IPv6 |

## 使用方式

```yaml
rule-providers:
  ai:
    type: http
    behavior: classical
    url: "https://raw.githubusercontent.com/Ashbaer/cross-rules/main/mihomo/ai.list"
    path: ./ruleset/ai.list
    interval: 86400
  developer:
    type: http
    behavior: classical
    url: "https://raw.githubusercontent.com/Ashbaer/cross-rules/main/mihomo/developer.list"
    path: ./ruleset/developer.list
    interval: 86400
```

## 许可证

MIT License
