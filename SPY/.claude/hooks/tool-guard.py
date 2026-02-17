"""
ツールガード ── スパイ家族チーム 検知班用
PreToolUse フックとして signal-scout / risk-hound に適用
Edit/Write/Bash の使用を二重ブロックする（fail-closed設計）
チーム特徴: 検知班（娘と犬）は提案・警告のみ。実装権限なし
"""
import json
import os
import sys


def read_payload() -> dict:
    raw = sys.stdin.read().strip()
    if not raw:
        return {}
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        return {}


try:
    payload = read_payload()
    tool_name = str(payload.get("tool_name", "")).lower() or os.environ.get("TOOL_NAME", "").lower()
    blocked = {"edit", "write", "bash"}

    if tool_name in blocked:
        print(f"[家族ツールガード] {tool_name} の使用はブロックされました。検知班は提案・警告のみです。", file=sys.stderr)
        sys.exit(2)

    sys.exit(0)
except Exception as exc:
    print(f"[家族ツールガード] 例外発生: {exc}", file=sys.stderr)
    sys.exit(2)
