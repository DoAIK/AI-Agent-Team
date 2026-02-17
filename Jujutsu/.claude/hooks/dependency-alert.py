"""
依存警告 ── 呪術チーム エース用
PreToolUse フックとして apex-closer に適用
エースが直接 Edit/Write する際に警告を出す（ブロックしない）
チーム特徴: 規格外のエースへの依存を防ぎ、再現性のある仕組みを促す
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
    impl_tools = {"edit", "write"}

    if tool_name in impl_tools:
        print("[呪術依存警告] エースが直接実装しています。推進役(frontline-driver)への委譲を検討してください。")
        print("[呪術依存警告] エースがいなくても回る仕組みを作れ。それが本当の強さだ。")

    sys.exit(0)
except Exception:
    sys.exit(0)
