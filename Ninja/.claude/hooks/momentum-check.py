"""
勢いチェック ── 任務班「影走り」烈火の突撃手用
TaskCompleted フックとして blazing-driver に適用
テスト記述の有無を確認し、勢い任せの実装を防ぐ（警告のみ、ブロックしない）
チーム特徴: 熱血の推進役は根拠より勢いが先行しがち
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

    test_keywords = ["テスト", "test", "検証", "テスト結果"]
    has_test = any(kw in content for kw in test_keywords)
    if not has_test:
        print("[影走り勢いチェック] テスト記述が見つかりません。テストなき実装は実装ではない。落ち着け。")

    change_keywords = ["変更点", "差分"]
    has_change = any(kw in content for kw in change_keywords)
    if not has_change:
        print("[影走り勢いチェック] 変更点サマリが見つかりません。何を変えたか報告しろ。")

    sys.exit(0)
except Exception:
    sys.exit(0)
