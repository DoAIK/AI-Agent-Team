"""
品質ゲート ── スパイ家族チーム フィクサー用
TaskCompleted フックとして iron-fixer に適用
実装報告フォーマットの準拠を検証する（不足時はブロック）
チーム特徴: 天然混じりの判断基準ズレを補正する安全網
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

    required_keywords = ["変更", "手順", "差分"]
    missing = [kw for kw in required_keywords if kw not in content]

    if missing:
        print(
            f"[家族品質ゲート] フォーマット不備: {', '.join(missing)} が不足しています。No-Go。",
            file=sys.stderr,
        )
        sys.exit(2)

    sys.exit(0)
except Exception as exc:
    print(f"[家族品質ゲート] 例外発生: {exc}", file=sys.stderr)
    sys.exit(2)
