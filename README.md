# Cross Rules

规则集合仓库，用于存放和管理各类规则配置。

## 目录结构

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

## 规则列表

### 通用规则

| 文件 | 说明 |
|------|------|
| `mihomo/ai.list` | AI 网站与工具（不含 Claude） |
| `mihomo/claude.list` | Claude / Anthropic 独立规则 |
| `mihomo/developer.list` | 程序员常用网站 |
| `mihomo/intl-dns.list` | 国际 DNS 服务 |
| `mihomo/lan.list` | 局域网 IPv4/IPv6 |
| `mihomo/media.list` | 媒体与资源站点 |
| `mihomo/entertainment.list` | 娱乐与内容平台 |
| `mihomo/social.list` | 社交媒体 |

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
