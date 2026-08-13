# 数理組版（surikumi）

`surikumi` は，日本語の数学教材を読みやすく高密度に組むための
LuaLaTeX パッケージである．JIS B5 判・2段組を基本に，講義，演習，
要点確認の紙面部品を提供する．

特定の商業誌，出版社，ロゴ，図案とは関係のない独立したプロジェクトである．

## 主な機能

- 本文 8 pt／行送り 10.8 pt を既定とするコンパクトな垂直リズム
- 明朝体の本文とゴシック体の見出し
- 例題，問題，解答，別解，注記のための部品
- 確認記事向けの節見出し，コメント，注釈，証明表示
- 行内式と別行数式で大きさをそろえ，上下限を上下に置く `\sum`
- TeX で生成する31種類の独自見出しパターン（幾何 12・和柄 10・数学的モチーフ 9）
- 背景パターンの濃度・色味・寸法の制御（`pattern-tone` / `pattern-accent` / `pattern-scale`）
- 狭い段のための行分割・改ページ制御（泣き別れ抑制，長い別行数式の段またぎ）
- 圏点，用語のゴシック，ルビ，リード文，公式囲み，まとめ，図表キャプション
- 1 段に収まらない式を逃がす，一時的な全段幅ブロック `mmwideblock`
- 柱，段の内容の高さに合わせて伸縮する段間罫，和欧間アキ，第三の密度
  `density=airy`（いずれもオプトイン）

## 必要な環境

- LuaLaTeX
- `jlreq`
- `luatexja-fontspec`
- `unicode-math` と TeX Gyre Termes Math
- `tikz`，`tcolorbox`，`amsmath`，`enumitem` など

TeX Live の標準的なフルインストールを想定している．和文は Noto CJK JP を
優先し，同じ設計を別名で提供する Noto Serif JP／Noto Sans JP の可変フォント
しか無い環境では，ウェイト軸を指定して同等の太さを得る．どちらも無ければ
jlreq の既定書体になる．欧文は TeX Gyre を使用する．数式は欧文本文と
そろえて TeX Gyre Termes Math で組む．`unicode-math` を使うため，
原稿側で `amssymb` や `bm` を読み込まない（`\bm` は `\symbf` の別名として
使える）．数式書体は `mathfontname` で差し替え，`mathfont=false` で
無効にできる．

## 使い方

`surikumi.sty` を原稿と同じディレクトリまたは TeX の検索パスへ置く．

```latex
\documentclass[lualatex,paper=b5j,fontsize=10pt,twoside]{jlreq}
\usepackage{surikumi}

\MathMagazineSetup{
  series={講義／数学},
  title={数列の基礎},
  author={数学編集部},
  deck={例題を通して基本事項を確認する．}
}

\begin{document}
\MakeMathMagazineTitle

\begin{mmexample}[1.1]{等差数列}
初項 $a$，公差 $d$ の等差数列の一般項を求めよ．
\end{mmexample}

一般項は
\[
  a_n=a+(n-1)d
\]
である．
\end{document}
```

既定は `density=compact` である．従来よりゆとりのある行間にする場合は，
次のように指定する．

```latex
\usepackage[density=standard,bodyleading=12pt]{surikumi}
```

## サンプルのビルド

```console
make
```

PDF は `build/public/` に生成される．各部品の使い分けは
[`docs/surikumi-style-guide.md`](docs/surikumi-style-guide.md) を参照する．
数式・記号の推奨表記は
[`docs/notation-style-guide.md`](docs/notation-style-guide.md) にまとめている．

## ライセンス

MIT License．詳しくは [`LICENSE`](LICENSE) を参照する．
