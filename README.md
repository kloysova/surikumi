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
- TeX で生成する31種類の独自見出しパターン（幾何 12・和柄 10・数学的モチーフ 9）
- 背景パターンの濃度・色味・寸法の制御（`pattern-tone` / `pattern-accent` / `pattern-scale`）
- 狭い段のための行分割・改ページ制御（泣き別れ抑制，長い別行数式の段またぎ）
- 圏点，用語のゴシック，ルビ，リード文，公式囲み，まとめ，図表キャプション
- 1 段に収まらない式を逃がす，一時的な全段幅ブロック `mmwideblock`
- 柱，段の内容の高さに合わせて伸縮する段間罫，和欧間アキ，第三の密度
  `density=airy`（いずれもオプトイン）
- 追加パッケージ `surikumi-kaisetsu.sty` による月刊解説誌の体裁
  （号の題字，特集の扉，罫を伴う節見出し，節ごとの数式番号，
  段下の注，年表，参考文献，署名，段抜きの囲み）

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

`\sum` の字形は既定で自作フォントから取る．差し替わるのは Σ だけで，
積分や括弧などは文書側の数式書体のまま変わらない．文書側の Σ に
戻す場合は次のように指定する．

```latex
\usepackage[sigma=document]{surikumi}
```

自作フォントはプロジェクト内の `texmf/` にあり，`config/.latexmkrc` と
`Makefile` が検索パスへ加える．独自のビルド手順を使う場合は，
`config/.latexmkrc` と同じ環境変数を設定する．

## 解説記事の体裁

月刊の学術解説誌の体裁で記事を組むときは，追加パッケージ
`surikumi-kaisetsu.sty` を読み込む．本文 9 pt・行送り 14.2 pt，
1 段 45 行の版面に，号の題字，特集の扉，罫を伴う節見出し，
`(1.1)` 形式の数式番号，`*1)` 形式の段下の注，年表，参考文献，
署名，段抜きの囲みを提供する．

```latex
\documentclass[lualatex,paper=b5j,fontsize=10pt,twoside]{jlreq}
\usepackage{surikumi-kaisetsu}

\MathKaisetsuSetup{
  journal-name={数理組版},
  masthead-first={SURIKUMI},
  masthead-second={REVIEW},
  issue-date={January 2026},
  issue-number={Number 1},
  masthead=true,
  feature={特集／変分原理},
  title={変分原理の考え方},
  author={\MKName{数理}{太郎}},
  author-reading={すうり・たろう},
  affiliation={数理組版編集部}
}

\begin{document}
\MKMakeTitle
\MKArticleReset

\MKSection{停留値としての運動}

作用積分は
\begin{equation}
  S[x]=\int_{t_a}^{t_b}L\bigl(\dot{x}(t),x(t)\bigr)\,\mathrm{d}t
\end{equation}
である\footnote{注は段の下に置く．}．

\begin{mkreferences}
  \item 文献を並べる．
\end{mkreferences}

\MKByline
\end{document}
```

部品の使い分けと鍵の一覧は
[`docs/kaisetsu-format.md`](docs/kaisetsu-format.md) にまとめている．

## サンプルのビルド

```console
make
```

PDF は `build/public/` に，解説記事の用例は `build/public/kaisetsu/` に
生成される．解説記事だけを組むときは次のようにする．

```console
make kaisetsu
```

各部品の使い分けは
[`docs/surikumi-style-guide.md`](docs/surikumi-style-guide.md)，
解説記事の体裁は [`docs/kaisetsu-format.md`](docs/kaisetsu-format.md) を
参照する．数式・記号の推奨表記は
[`docs/notation-style-guide.md`](docs/notation-style-guide.md) にまとめている．

## 総目録

書体，記号，見出しの記法，紙面部品を一箇所に集めた索引が
[`docs/catalog.md`](docs/catalog.md) である．どの部品をどの記事で使うか
迷ったときは，まずここを引く．

紙の見本は次で組む．PDF は `build/public/catalog/` に生成される．

```console
make catalog
```

| 見本 | 内容 |
|---|---|
| `surikumi-catalog.pdf` | 書体，Σ，色，記号，見出し，講義・演習・確認の部品，種類を選ばない部品，問題集の追加部品 |
| `pattern-catalog.pdf` | 背景パターン31種と濃度・色味・寸法の効き方 |
| `kaisetsu-catalog.pdf` | 解説記事の版面で組んだ扉，見出しの4型，注，年表，囲み，参考文献，署名 |

いずれも各項目に命令名を添えてある．

## 短縮名

すべての長い命令に短い別名がある．長い名前が正式名で，短い名前は別名である．
どちらで書いても同じものが組まれるので，既存の原稿は書き換えなくてよい．

```latex
\MMSetup{...}          % = \MathMagazineSetup
\MMTitle               % = \MakeMathMagazineTitle
\MMSec{基本的な数列}    % = \MMConfirmationSection
\MMCom{...}            % = \MMConfirmationGeneralComment
\MMComA{...}           % = \MMConfirmationAdvancedComment（意欲的な読者向け）
\MMAnn{...}            % = \MMConfirmationGeneralNote
\MKSetup{...}          % = \MathKaisetsuSetup
```

`Com` はコメント（正方形），`Ann` は注釈（矢印），接尾の `A` は
意欲的な読者向けを表す．全対応表は
[`docs/catalog.md`](docs/catalog.md) の第13章にある．

## ライセンス

パッケージ本体（`surikumi.sty`，`surikumi-kaisetsu.sty`，
`examples/problem-sets/surikumi-mondaishu.sty`，用例，文書）は
MIT License である．詳しくは [`LICENSE`](LICENSE) を参照する．

`texmf/` に同梱する Σ のフォント `SugakuFourier-Math-Extension` だけは
別である．これは LPPL で配布される Fourier-GUTenberg の
`Fourier-Math-Extension` を基礎にした派生フォントなので，LPPL 1.3c に従う．
派生ファイルは原ファイルと異なる名称を持つ．ライセンス本文は
[`font-development/sugaku-fourier/LICENSE-LPPL-1.3c.txt`](font-development/sugaku-fourier/LICENSE-LPPL-1.3c.txt)
に収録し，設計と生成手順は
[`font-development/sugaku-fourier/README.md`](font-development/sugaku-fourier/README.md)
にまとめている．フォントを使わない場合は `sigma=document` を指定すれば，
MIT の部分だけで組める．
