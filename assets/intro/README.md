# CN Direct by DeepWheel intro assets

This folder contains the bilingual GitHub introduction system for CN Direct by DeepWheel.

## Language pairing

- English README: `cn-smart-routing-hero-en.png` and `cn-smart-routing-workflow-en.png`
- Chinese README: `cn-smart-routing-hero-zh-CN.png` and `cn-smart-routing-workflow-zh-CN.png`
- Update guide: `cn-direct-update-en.png` and `cn-direct-update-zh-CN.png`
- Chinese contribution guide: `cn-direct-contribute-zh-CN.png`

The SVG files are editable sources. PNG files are exact 1600 × 900 README exports.

GitHub social preview:

- `shadowrocket-cn-smart-routing-social-preview.svg`
- `shadowrocket-cn-smart-routing-social-preview.png`

The social preview is an exact 1280 × 640 export for the repository Settings page. It is not embedded in the README. Filenames stay unchanged to avoid breaking existing links and search history.

## Visual roles

- Hero: the consumer promise—mainland traffic stays direct while overseas traffic follows the selected node.
- Workflow: the observed Shadowrocket path—remote URL import, tap the configuration filename, choose Use Config, then keep node choice on the home screen.
- Update guide: enable background updates once; for a manual check, tap the configuration filename, choose Update, then verify with Preview.
- Contribution guide: report a public service and the observed problem; automated checks and maintainer review handle the remaining safety gates.
- The UI guidance is redrawn with public labels and contains no screenshots, local IPs, subscriptions, nodes or device data.
- The hero avoids provider logos, fake speed claims and fake network measurements.
- Internal panels use hairline outlines only. Decorative shadow is limited to the outer facade card.

## Consumer contract

- Terminal user: a mainland-China Shadowrocket user who already has a subscription, or a user reporting a routing problem.
- Use scenario: first visit to the GitHub repository before importing a public configuration.
- Desired belief: install once through the remote URL, keep node control, receive future stable config updates through Shadowrocket, and report problems without exposing private network data.
- Next action: import the stable Raw URL, enable Configuration mode and background config updates, then select a node.
- Prohibited claim: no promise of zero latency, bank-app acceptance, account-risk avoidance, Apple TV support, automatic iCloud sync or guaranteed background execution.

## Generation order

1. Lock the consumer contract in `docs/PUBLIC-SURFACE-REVIEW.json`.
2. Apply `lucas-deepwheel-brand-apply`: precise, restrained, credible and ordered.
3. Use code-based SVG composition because the copy must remain exact and editable.
4. Render PNG derivatives with `python3 scripts/render-intro-assets.py --write`.
5. Run the renderer check, configuration validator, privacy scan and full-size visual inspection.

The embedded mark and tokens come from the current DeepWheel brand application Skill. Do not replace them with historical colours or a hand-drawn monogram.
