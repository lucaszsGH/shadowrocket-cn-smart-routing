#!/usr/bin/env python3
"""Validate repository-level collaboration and privacy guardrails."""

from __future__ import annotations

from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_CONTENT = {
    ".github/pull_request_template.md": [
        "## 测试证据",
        "## 风险与回退",
        "## 隐私与公开安全确认",
        "python3 scripts/validate_shadowrocket.py",
        "FINAL,PROXY",
        "订阅 URL",
        "完整日志",
    ],
    ".github/CODEOWNERS": ["* @lucaszsGH"],
    "CONTRIBUTING.md": [
        "python3 scripts/validate_repository.py",
        "一个 Pull Request 只解决一个问题",
        "SECURITY.md",
    ],
    "SECURITY.md": [
        "Report a vulnerability",
        "不会因为合并本文件而自动开启",
    ],
    "docs/maintainer-community-safety.md": [
        "protect-main",
        "Require a pull request before merging",
        "Private vulnerability reporting",
        "CI job `validate`",
    ],
}


def main() -> int:
    errors: list[str] = []

    for relative, needles in REQUIRED_CONTENT.items():
        path = ROOT / relative
        if not path.is_file():
            errors.append(f"missing required repository guardrail: {relative}")
            continue

        text = path.read_text(encoding="utf-8")
        for needle in needles:
            if needle not in text:
                errors.append(f"missing required text in {relative}: {needle}")

    workflow = ROOT / ".github" / "workflows" / "validate.yml"
    if not workflow.is_file():
        errors.append("missing validation workflow")
    else:
        workflow_text = workflow.read_text(encoding="utf-8")
        if "  validate:" not in workflow_text:
            errors.append("validation job must remain named validate")
        if "python3 scripts/validate_repository.py" not in workflow_text:
            errors.append("validation workflow does not run repository guardrails")

    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        return 1

    print("PASS: repository collaboration guardrails are present")
    print("PASS: PR template includes privacy, evidence and rollback checks")
    return 0


if __name__ == "__main__":
    sys.exit(main())
