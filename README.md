# AgentTeam: Multi-Agent Team Design Benchmark

3種類の4人エージェントチーム（`Ninja` / `SPY` / `Jujutsu`）に同一課題を与え、
**性格・役割分担・統治ルール**が成果物品質へ与える影響を比較する実験リポジトリです。

## 1. Research Goal

### 問い
同じモデル能力・同じ課題でも、チーム運用設計の違いで成果物はどこまで変わるか。

### 仮説
- 役割分離 + 品質ゲートがあるチームは、総合品質が安定する
- 個性が強いチームは、特定軸（演出、UX、速度）に尖る
- 実装権限とレビュー権限の分離は、欠陥流入を下げる

## 2. Experimental Design

### 対象チーム
- `Ninja`
- `SPY`
- `Jujutsu`

### 共通タスク
- LP作成（エンジニア向け、かっこよさ重視）
- UFOフライトシミュレーター作成（HTML/CSS/JS単一ファイル）

### 評価軸（100点）
- 要件達成度（20）
- LP実装品質（30）
- UFO実装品質（35）
- 運用・拡張性（15）

## 3. Repository Layout

```text
AgentTeam/
├── README.md
├── .gitignore
├── Ninja/
│   ├── CLAUDE.md
│   ├── .claude/
│   │   ├── agents/
│   │   └── hooks/
│   ├── lp/index.html
│   └── ufo/index.html
├── SPY/
│   ├── CLAUDE.md
│   ├── .claude/
│   │   ├── agents/
│   │   └── hooks/
│   ├── lp/index.html
│   └── ufo/index.html
└── Jujutsu/
    ├── CLAUDE.md
    ├── .claude/
    │   ├── agents/
    │   └── hooks/
    ├── index.html
    ├── lp-design.md
    └── ufo.html
```

## 4. Usage Guide

### 4.1 Run Artifacts

1. Ninja LP: `Ninja/lp/index.html`
2. Ninja UFO: `Ninja/ufo/index.html`
3. SPY LP: `SPY/lp/index.html`
4. SPY UFO: `SPY/ufo/index.html`
5. Jujutsu LP: `Jujutsu/index.html`
6. Jujutsu UFO: `Jujutsu/ufo.html`

### 4.2 Agent Teams を有効化する（必須）

Agent Teams は実験的機能でデフォルト無効なので、まず有効化します。

A. `settings.json` に入れる（推奨）

`CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS` を `1` にします。

docs例:

```json
{
  "env": {
    "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1"
  }
}
```

### 4.3 Use as Claude Code Team Config

1. 使うチームを1つ選ぶ（`Ninja` / `SPY` / `Jujutsu`）
2. そのチームの `CLAUDE.md` を対象プロジェクトのルートに配置
3. そのチームの `.claude/agents` と `.claude/hooks` を対象プロジェクトの `.claude/` に配置し、.claude/settings.json に hooks 設定も配置（または追記）**する
4. 自然言語で指示して、Teamを起動する

## 5. License

MIT License. See `LICENSE` for details.

- Copyright (c) 2026 DoAIK
