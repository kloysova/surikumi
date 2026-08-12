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
- `\sum` の字形に自作フォント `SugakuFourier-Math-Extension` を既定で使用
- TeX で生成する12種類の独自見出しパターン

## 必要な環境

- LuaLaTeX
- `jlreq`
- `luatexja-fontspec`
- `tikz`，`tcolorbox`，`amsmath`，`enumitem` など

TeX Live の標準的なフルインストールを想定している．Noto CJK と
TeX Gyre が利用可能な場合は既定書体として使用する．

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

`\sum` の字形は既定で自作フォントから取る．差し替わるのは Σ だけで，
積分や括弧などは文書側の数式書体のまま変わらない．文書側の Σ に
戻す場合は次のように指定する．

```latex
\usepackage[sigma=document]{surikumi}
```

自作フォントはプロジェクト内の `texmf/` にあり，`config/.latexmkrc` と
`Makefile` が検索パスへ加える．独自のビルド手順を使う場合は，
`config/.latexmkrc` と同じ環境変数を設定する．

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
