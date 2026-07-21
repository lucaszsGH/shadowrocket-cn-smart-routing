# Project comparison

Last reviewed: 2026-07-21.

This is a neutral comparison of project intent, not a quality ranking. Every project below solves a different job. Check each repository's current README, license and recent changes before importing anything.

| Project | Primary job | Where it is stronger | How CN Direct differs |
|---|---|---|---|
| [Johnshall/Shadowrocket-ADBlock-Rules-Forever](https://github.com/Johnshall/Shadowrocket-ADBlock-Rules-Forever) | Multiple Shadowrocket profiles, routing modes and ad-blocking variants | Broad choice, generated rule variants and advertising filters | CN Direct ships one mainland-first profile, leaves ad blocking off by default and keeps node selection manual |
| [GMOogway/shadowrocket-rules](https://github.com/GMOogway/shadowrocket-rules) | Large modular `DIRECT`, `PROXY` and `REJECT` rule sets | Advanced composition, modular overrides and broad rule volume | CN Direct is a smaller end-user configuration with fewer daily decisions and an explicit consumer safety boundary |
| [blackmatrix7/ios_rule_script](https://github.com/blackmatrix7/ios_rule_script) | Cross-client upstream rules, rewrites and scripts | Very broad service coverage across multiple proxy clients | CN Direct is not a replacement; it consumes selected Shadowrocket rule lists and provides a focused mainland-China configuration and validation layer |
| [misha-tgshv/shadowrocket-configuration-file](https://github.com/misha-tgshv/shadowrocket-configuration-file) | Region-specific Shadowrocket configurations and lists for Russian-speaking users | Localized regional routing and configuration variants | CN Direct applies the same region-first idea to mainland-China office, payment, media, gaming, LAN, AI and developer workflows |

## Choose CN Direct when

- you already have your own subscription or nodes;
- you want a single Shadowrocket configuration instead of a rule-building toolkit;
- mainland office, banking, payment, video, games and LAN should stay direct;
- overseas AI, GitHub and unmatched overseas traffic should follow one manually selected home-screen node;
- you do not want bundled nodes, automatic country selection, scripts, MITM or default ad blocking.

## Choose another project when

- your main goal is strong ad blocking;
- you want many black-list, white-list, return-to-China or streaming variants;
- you prefer composing and maintaining modular rules yourself;
- you need one upstream rule ecosystem for many different proxy clients;
- you need optimization for a country other than mainland China.

## Important trade-offs

CN Direct uses a pinned ChinaMax snapshot for broad mainland coverage while keeping the daily workflow to one finished configuration, one remote update path and one manually selected node. It still depends on upstream public rule lists, cannot guarantee that every bank app accepts an active system VPN, and requires real-device testing for each network and node.
