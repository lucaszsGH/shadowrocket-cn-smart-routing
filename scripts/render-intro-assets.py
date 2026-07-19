#!/usr/bin/env python3
"""Render or validate the bilingual 1600x900 GitHub introduction assets."""

from __future__ import annotations

import argparse
import re
import shutil
import struct
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INTRO = ROOT / "assets" / "intro"
EXPECTED = (1600, 900)
STEMS = (
    "cn-smart-routing-hero-en",
    "cn-smart-routing-hero-zh-CN",
    "cn-smart-routing-workflow-en",
    "cn-smart-routing-workflow-zh-CN",
)


def find_chromium() -> str | None:
    candidates = (
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "chromium",
        "chromium-browser",
        "google-chrome",
    )
    for candidate in candidates:
        if candidate.startswith("/") and Path(candidate).exists():
            return candidate
        resolved = shutil.which(candidate)
        if resolved:
            return resolved
    return None


def check_svg(path: Path) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    if not re.search(r'<svg[^>]+width="1600"[^>]+height="900"', text):
        errors.append(f"{path.relative_to(ROOT)}: SVG canvas is not 1600x900")
    if "#1D1D1F" in text or "#1E6FE8" in text or "#111720" in text or "#F8FAFC" in text:
        errors.append(f"{path.relative_to(ROOT)}: deprecated DeepWheel colour found")
    if "aria-labelledby=" not in text or "<title" not in text or "<desc" not in text:
        errors.append(f"{path.relative_to(ROOT)}: missing accessible title or description")
    return errors


def render(svg: Path, png: Path, chromium: str) -> None:
    command = [
        chromium,
        "--headless=new",
        "--disable-gpu",
        "--hide-scrollbars",
        "--force-device-scale-factor=1",
        f"--window-size={EXPECTED[0]},{EXPECTED[1]}",
        f"--screenshot={png}",
        svg.as_uri(),
    ]
    completed = subprocess.run(command, cwd=ROOT, capture_output=True, text=True)
    if completed.returncode != 0:
        message = completed.stderr.strip().splitlines()[-1] if completed.stderr.strip() else "unknown Chromium error"
        raise RuntimeError(f"render failed for {svg.name}: {message}")


def check_png(path: Path) -> list[str]:
    if not path.exists():
        return [f"{path.relative_to(ROOT)}: rendered PNG is missing"]
    with path.open("rb") as handle:
        header = handle.read(24)
    if len(header) < 24 or header[:8] != b"\x89PNG\r\n\x1a\n" or header[12:16] != b"IHDR":
        return [f"{path.relative_to(ROOT)}: invalid PNG header"]
    size = struct.unpack(">II", header[16:24])
    if size != EXPECTED:
        return [f"{path.relative_to(ROOT)}: expected {EXPECTED}, got {size}"]
    return []


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true", help="render SVG sources to PNG with local Chromium")
    args = parser.parse_args()

    errors: list[str] = []
    for stem in STEMS:
        errors.extend(check_svg(INTRO / f"{stem}.svg"))

    if args.write:
        chromium = find_chromium()
        if not chromium:
            print("BLOCK: local Chromium was not found; no renderer is installed automatically", file=sys.stderr)
            return 2
        for stem in STEMS:
            render(INTRO / f"{stem}.svg", INTRO / f"{stem}.png", chromium)

    for stem in STEMS:
        errors.extend(check_png(INTRO / f"{stem}.png"))

    if errors:
        for error in errors:
            print(f"BLOCK: {error}")
        return 2

    action = "rendered and validated" if args.write else "validated"
    print(f"PASS: four bilingual introduction assets {action} at 1600x900")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
