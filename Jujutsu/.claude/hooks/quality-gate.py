"""
品質ゲート ── 呪術チーム 毒舌の品質番人用
TaskCompleted フックとして venom-critic に適用
品質判定フォーマットの準拠を検証する（不足時はブロック）
チーム特徴: 容赦ない品質番人の判定にもフォーマットは必要
"""
import json
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
    content = json.dumps(payload, ensure_ascii=False).lower()

    required_keywords = ["品質判定", "欠陥", "go"]
    missing = [kw for kw in required_keywords if kw not in content]

    if missing:
        print(
            f"[呪術品質ゲート] フォーマット不備: {', '.join(missing)} が不足しています。No-Go。",
            file=sys.stderr,
        )
        sys.exit(2)

    sys.exit(0)
except Exception as exc:
    print(f"[呪術品質ゲート] 例外発生: {exc}", file=sys.stderr)
    sys.exit(2)
