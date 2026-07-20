# CN Smart Routing intro assets

This folder contains the bilingual GitHub introduction system for CN Smart Routing.

## Language pairing

- English README: `cn-smart-routing-hero-en.png` and `cn-smart-routing-workflow-en.png`
- Chinese README: `cn-smart-routing-hero-zh-CN.png` and `cn-smart-routing-workflow-zh-CN.png`

The SVG files are editable sources. PNG files are exact 1600 × 900 README exports.

GitHub social preview:

- `shadowrocket-cn-smart-routing-social-preview.svg`
- `shadowrocket-cn-smart-routing-social-preview.png`

The social preview is an exact 1280 × 640 export for the repository Settings page. It is not embedded in the README.

## Visual roles

- Hero: the consumer value proposition—keep the proxy on, keep mainland traffic direct, and keep node choice manual.
- Workflow: the only process explanation—import, choose a node, and enable Configuration mode.
- The hero avoids a mini settings screen, provider logos, fake speed claims and fake network measurements.
- Internal panels use hairline outlines only. Decorative shadow is limited to the outer facade card.

## Consumer contract

- Terminal user: a mainland-China Shadowrocket user who already has a subscription.
- Use scenario: first visit to the GitHub repository before importing a public configuration.
- Desired belief: the rules are transparent, mainland-first and independent of the user's nodes.
- Next action: read the three-step setup, inspect the configuration, and import only after understanding the boundary.
- Prohibited claim: no promise of zero latency, bank-app acceptance, account-risk avoidance, Apple TV support or automatic iCloud sync.

## Generation order

1. Lock the consumer contract in `docs/PUBLIC-SURFACE-REVIEW.json`.
2. Apply `lucas-deepwheel-brand-apply`: precise, restrained, credible and ordered.
3. Use code-based SVG composition because the copy must remain exact and editable.
4. Render PNG derivatives with `python3 scripts/render-intro-assets.py --write`.
5. Run the renderer check, configuration validator, privacy scan and full-size visual inspection.

The embedded mark and tokens come from the current DeepWheel brand application Skill. Do not replace them with historical colours or a hand-drawn monogram.
