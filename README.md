# Cross Rules

规则集合仓库，用于存放和管理各类规则配置。

## Conflux 商店目录

从 `v0.0.15` 起，Conflux 自动收录 `main` 分支 [mihomo 目录](mihomo/)及其子目录内的 `.list` 文件。添加文件后，商店在目录缓存到期后的下一次访问时刷新，正常缓存 5 分钟。

在 [catalog.json](catalog.json) 中按规则文件的仓库相对路径维护 `title_zh`、`title_en`、`description_zh` 和 `description_en`。可以另填 `category` 和 `tags` 供商店筛选与搜索。中英文名称都未填写时，商店显示文件名。只填写一种语言时，两种界面语言都显示已填写的内容。

可用分类为 `ai`、`streaming`、`social`、`dev`、`cn_direct`、`privacy`、`gaming` 和 `other`。省略分类时，`mihomo/streaming/` 下的规则归入 `streaming`，其余规则归入 `other`。

## 目录示例

```
cross-rules/
├── README.md
└── mihomo/
    ├── ai.list
    ├── claude.list
    ├── developer.list
    ├── intl-dns.list
    ├── lan.list
    ├── media.list           # 媒体与资源站点
    ├── entertainment.list   # 娱乐与内容平台
    ├── social.list          # 社交媒体规则
    ├── web3.list            # Web3 与加密货币平台
    └── streaming/           # 流媒体规则 (分服务配置)
        ├── netflix.list
        ├── disney.list
        ├── youtube.list
        ├── spotify.list
        ├── tiktok.list
        ├── hbomax.list
        ├── primevideo.list
        ├── appletv.list
        ├── twitch.list
        └── bilibili-intl.list
```

## 常用规则

### 通用规则

| 文件 | 说明 |
|------|------|
| `mihomo/ai.list` | AI 网站与工具（不含 Claude，含 Meta Muse） |
| `mihomo/claude.list` | Claude / Anthropic 独立规则 |
| `mihomo/developer.list` | 程序员常用网站 |
| `mihomo/intl-dns.list` | 国际 DNS 服务 |
| `mihomo/lan.list` | 局域网 IPv4/IPv6 |
| `mihomo/media.list` | 媒体与资源站点 |
| `mihomo/entertainment.list` | 娱乐与内容平台 |
| `mihomo/social.list` | 社交媒体 |
| `mihomo/web3.list` | Web3 与加密货币平台 |

### 流媒体规则

| 文件 | 说明 | 解锁难度 |
|------|------|----------|
| `streaming/netflix.list` | Netflix | ⭐⭐⭐⭐ 较难 |
| `streaming/disney.list` | Disney+ / Hulu / ESPN+ | ⭐⭐⭐⭐ 较难 |
| `streaming/hbomax.list` | HBO Max / Max | ⭐⭐⭐⭐⭐ 很难 |
| `streaming/primevideo.list` | Amazon Prime Video | ⭐⭐⭐ 中等 |
| `streaming/youtube.list` | YouTube / YouTube Music | ⭐ 简单 |
| `streaming/spotify.list` | Spotify | ⭐⭐ 简单 |
| `streaming/appletv.list` | Apple TV+ | ⭐ 简单 |
| `streaming/twitch.list` | Twitch | ⭐ 简单 |
| `streaming/tiktok.list` | TikTok 国际版 | ⭐⭐ 简单 |
| `streaming/bilibili-intl.list` | Bilibili 国际版 | ⭐⭐ 简单 |

## 使用方式

```yaml
rule-providers:
  claude:
    type: http
    behavior: classical
    url: "https://raw.githubusercontent.com/Ashbaer/cross-rules/main/mihomo/claude.list"
    path: ./ruleset/claude.list
    interval: 86400
  netflix:
    type: http
    behavior: classical
    url: "https://raw.githubusercontent.com/Ashbaer/cross-rules/main/mihomo/streaming/netflix.list"
    path: ./ruleset/netflix.list
    interval: 86400
  youtube:
    type: http
    behavior: classical
    url: "https://raw.githubusercontent.com/Ashbaer/cross-rules/main/mihomo/streaming/youtube.list"
    path: ./ruleset/youtube.list
    interval: 86400

rules:
  - RULE-SET,claude,🤖 Claude
  - RULE-SET,netflix,🎬 Netflix
  - RULE-SET,youtube,📺 YouTube
```

## 许可证

MIT License
