# 解説記事の組版

## 1. 目的

`surikumi-kaisetsu.sty` は，月刊の学術解説誌の体裁で記事を組むための
`surikumi.sty` の追加パッケージである．号の扉，特集の見出し，
罫を伴う節見出し，節ごとの数式番号，段下の注，年表，参考文献，署名など，
この種の誌面に共通する部品をまとめている．

学術誌一般に共通する体裁を独自に実装したものであり，特定の商業誌の
題字，ロゴ，飾り，図案を写したものではない．既定値はすべて中立の
仮置きであり，実際の号の情報は文書側で与える．

数式・記号・句読点は，先に
[`notation-style-guide.md`](notation-style-guide.md) に従う．
本書は，その内容を解説記事の紙面へどう配置するかを定める．
`surikumi.sty` 本体の部品については
[`surikumi-style-guide.md`](surikumi-style-guide.md) を見る．
全部品の索引と短縮名の対応表は [`catalog.md`](catalog.md) にある．
本書では正式名で書くが，`\MathKaisetsuSetup` を `\MKSetup`，
`\MKMakeTitle` を `\MKTitle` のように短く書いてもよい．

## 2. 読み込み

```latex
\documentclass[lualatex,paper=b5j,fontsize=10pt,twoside]{jlreq}
\usepackage{surikumi-kaisetsu}
```

`surikumi.sty` は自動的に読み込まれる．`surikumi` 側のオプションを
変えるときは，先に本体を読み込む．

```latex
\usepackage[sigma=document]{surikumi}
\usepackage{surikumi-kaisetsu}
```

### 2.1 パッケージオプション

| オプション | 既定 | 内容 |
|---|---|---|
| `bodysize` | `9pt` | 本文の文字サイズ |
| `leading` | `14.2pt` | 本文の行送り |
| `lines` | `45` | 1 段あたりの行数．版面の高さはこの値から決まる |
| `gutter` | `8mm` | 段間 |
| `sectionstyle` | `bar` | 節見出しの既定の型 |
| `eqnumbering` | `section` | 数式番号の付け方（`section`／`continuous`／`none`） |
| `layout` | `true` | 判型と版面を設定する |
| `footer` | `true` | 柱（ノンブルと号表示）を出す |
| `footnotes` | `true` | 注を `*1)` 形式にする |
| `captions` | `true` | 図表見出しをこの形式にする |
| `flushbottom` | `false` | 段の下端をそろえる |

版面は，本文の行送りに `lines` を掛けた高さに設定する．`\topskip` も
行送りと等しくするため，本文だけの段は行数がそろい，`raggedbottom` の
ままでも左右の段が同じ行で終わる．別行数式や見出しを含む段の下端まで
そろえたいときは `flushbottom` を指定する．このとき別行数式の前後に
伸びしろが入る．

```latex
\usepackage[bodysize=8.6pt,leading=13.6pt,lines=47]{surikumi-kaisetsu}
```

## 3. 号と記事の情報

`\MathKaisetsuSetup` に鍵と値で与える．次の記事の扉を組むまで有効である．

```latex
\MathKaisetsuSetup{
  journal-name={数理組版},
  masthead-first={SURIKUMI},
  masthead-second={REVIEW},
  issue-date={January 2026},
  issue-number={Number 1},
  masthead=true,
  align=center,
  feature={特集／変分原理},
  title={変分原理の考え方},
  author={\MKName{数理}{太郎}},
  author-reading={すうり・たろう},
  affiliation={数理組版編集部}
}
```

| 鍵 | 内容 |
|---|---|
| `journal-name` | 柱に出す誌名 |
| `masthead-first`，`masthead-second` | 号の扉の欧文題字（2 行） |
| `issue-date`，`issue-number` | 題字の左右に置く発行月と号数 |
| `footer-line` | 柱の文字列を直接指定する．未指定なら誌名と号から組む |
| `feature` | 特集名．空にすると特集の表示を省く |
| `title`，`subtitle` | 表題と副題 |
| `author` | 署名 |
| `author-reading`，`affiliation` | 記事末の `\MKByline` に使う読みと所属 |
| `ornament`，`ornament-width` | 扉に置く飾りとその幅 |
| `align` | `center`（号の巻頭）または `left`（特集記事の扉） |
| `title-font` | `mincho`（既定）または `gothic` |
| `masthead` | 題字を出すか |
| `feature-bar` | 特集名を罫で挟むか |
| `feature-rule-width` | 特集の罫の長さ |
| `section-style` | 節見出しの型 |
| `footer-placement` | `odd`（既定）／`both`／`none` |

値に読点 `,` を含む鍵は，値全体をもう一重の中括弧で囲む．

```latex
footer-line={{\MKHeadingFace 数理組版}\hspace{.7em}NO. 2, FEBRUARY 2026},
```

## 4. 記事の扉

`\MKMakeTitle` が全段抜きの扉を組み，2 段組の本文に入る．
直前に `\clearpage` を置く必要はない．続けて `\MKArticleReset` を書くと，
節，数式，図表，注の番号が 1 に戻る．

```latex
\MKMakeTitle
\MKArticleReset
```

扉には二つの型がある．

- `align=center`：号の巻頭記事．題字，中央の特集名，中央の表題，
  中央の署名を縦に積む．`masthead=true` と組にして使う．
- `align=left`：特集の中の記事．細罫と太罫で挟んだ特集名，左寄せの表題，
  副題，署名を置き，外側に飾りを入れられる．

飾りは文書側で用意する．参考紙面の図案を写さず，`\includegraphics` か，
TeX で生成した独自の図形を渡す．

```latex
\newcommand{\MyOrnament}{\begin{tikzpicture}...\end{tikzpicture}}
\MathKaisetsuSetup{ornament={\MyOrnament},ornament-width={34mm}}
```

題字だけを別に置くときは `\MKMasthead`，特集の罫だけを置くときは
`\MKFeatureBar[長さ]{特集名}` を使う．

## 5. 見出し

### 5.1 節

`\MKSection{...}` は番号付きの節見出しである．型は 4 種類あり，
`section-style` で紙面全体の既定を決め，`\MKSection[型]{...}` で
一つの見出しだけを別の型にできる．星付き形式は番号を進めない．

| 型 | 体裁 | 用途 |
|---|---|---|
| `bar` | 段幅の罫の下に柱と見出し | 通常の節見出し |
| `pillars` | 両端の柱の間に中央寄せ | 特集記事の節見出し |
| `band` | 上下の罫と両端の柱 | 章が切り替わる位置 |
| `plain` | 罫も柱もなし | 短い記事，囲みの中 |

```latex
\MKSection{停留値としての運動}
\MKSection[band]{二つの積分の関係}
\MKSection*{付録}
```

### 5.2 小見出し

`\MKSubsection{...}` は `1.1` の形の番号を付け，1 字下げの位置から始める．
星付き形式は番号を進めない．小見出しの直後の段落も 1 字下げで始める．

### 5.3 行頭の見出し

`\MKRunIn{注意}` は行頭にゴシック体の語を置き，本文をそのまま続ける．
`\MKRemark{...}` と `mkremark` 環境は，この形の段落をまとめて扱う．

```latex
\MKRemark{「最小」という言い方は歴史的なものである．}

\begin{mkremark}[定義]
本文を置く．
\end{mkremark}
```

## 6. 数式番号

既定では節ごとに `(1.1)`，`(1.2)`，… と番号を付け，節が変わると
`(2.1)` に戻る．通し番号にするときは次のようにする．

```latex
\MKEquationNumbering{continuous}
```

番号を付けるのは本文中で参照する式だけであり，
参照しない式は `\[...\]` で組む．この方針は
[`notation-style-guide.md`](notation-style-guide.md) と同じである．

## 7. 注と参考文献

段の下に置く注は `*1)`，`*2)` の形で番号を付ける．本文中の参考文献番号
`1)`，`2)` と形が違うため，同じ段に並んでも取り違えない．

```latex
本文である\footnote{注の本文を置く．}．
```

注の折り返しは番号の右にそろう．番号は記事ごとに 1 から数え直す
（`\MKArticleReset`）．本文に印を出さない注には `\MKUnmarkedNote{...}` を使う．

参考文献は記事の末尾に置く．

```latex
\begin{mkreferences}
  \item 文献を並べる． \label{ref:first}
  \item 次の文献．
\end{mkreferences}
```

本文からは肩付きの番号で参照する．`\MKCite{1}` は `1)`，
`\MKCite{1,2}` は `1,2)` を肩付きで出す．`\label` を併用すれば
番号の変更に追随する．

```latex
詳しくは文献\MKCite{\ref{ref:first}} を見る．
```

## 8. 図と表

図の見出しは図の下，表の見出しは表の上に置く．番号はゴシック体，
本文は明朝体で，段の幅いっぱいに組む．図の中身は `mkfigurebody` で
段の中央にそろえる．

```latex
\begin{figure}[t]
  \begin{mkfigurebody}
    \begin{tikzpicture}...\end{tikzpicture}
  \end{mkfigurebody}
  \caption{見出しの本文を置く．}
  \label{fig:example}
\end{figure}
```

## 9. 年表，囲み，引用

年表は，年と事項を並べ，上下を罫で挟む．

```latex
\begin{mkchronology}{変分法の歩み}
  \MKChronoItem{1744}{Euler が変分法の一般的な手続きをまとめる}
  \MKChronoItem{1788}{『解析力学』が刊行される}
\end{mkchronology}
```

囲みは 2 種類ある．`mkinsert` は段の中に置く囲み，`mkfullinsert` は
段抜きの囲みで，既定では紙面の下に置く．

```latex
\begin{mkinsert}
\MKRunIn{要点}本文を置く．
\end{mkinsert}

\begin{mkfullinsert}[b]
段抜きの囲みの本文を置く．
\end{mkfullinsert}
```

引用は `mkquote` で左を 1 字下げる．

## 10. 柱

奇数ページの内側に誌名と号，外側にノンブルを置く．偶数ページは
外側のノンブルだけを出す．両方のページに誌名を出すときは
`footer-placement=both`，柱を消すときは `footer-placement=none` とする．

## 11. 1 冊に複数の記事を置く

記事ごとに `\MathKaisetsuSetup` で扉の内容を組み直し，`\MKMakeTitle` と
`\MKArticleReset` を続けて書く．`\MKMakeTitle` が前の記事を締めるので，
その直前に `\clearpage` は置かない．

```latex
\MathKaisetsuSetup{align=left,masthead=false,title={二本目の記事},...}
\MKMakeTitle
\MKArticleReset
```

## 12. 部品の一覧

| 用途 | 部品 |
|---|---|
| 号と記事の情報 | `\MathKaisetsuSetup` |
| 記事の扉 | `\MKMakeTitle` |
| 番号の初期化 | `\MKArticleReset` |
| 題字 | `\MKMasthead` |
| 特集名 | `\MKFeatureLabel`，`\MKFeatureBar` |
| 姓名の間の空き | `\MKName` |
| 節見出し | `\MKSection` |
| 小見出し | `\MKSubsection` |
| 行頭の見出し | `\MKRunIn` |
| 注意などの段落 | `\MKRemark`，`mkremark` |
| 数式番号の方式 | `\MKEquationNumbering` |
| 参考文献番号の参照 | `\MKCite` |
| 参考文献 | `mkreferences` |
| 記事末の署名 | `\MKByline`，`\MKBylineText` |
| 図の中身 | `mkfigurebody` |
| 年表 | `mkchronology`，`\MKChronoItem` |
| 段の中の囲み | `mkinsert` |
| 段抜きの囲み | `mkfullinsert` |
| 引用 | `mkquote` |
| 印のない注 | `\MKUnmarkedNote` |

## 13. 避けること

- 特定の商業誌の題字，ロゴ，飾り，図案を写さない．
- 扉の飾りに参考紙面の図をそのまま使わない．
- 高密度化のために原稿へ負の `\vspace` や局所的な `\linespread` を書かない．
  紙面の密度は `bodysize`，`leading`，`lines` で変える．
- 節見出しの型を段落ごとの気分で変えない．紙面全体で一つの型を既定にし，
  例外だけを `\MKSection[型]` で指定する．
- 注と参考文献番号の形を入れ替えない．段下の注は `*1)`，
  文献参照は `1)` である．
- 別行数式の末尾に句読点を置かない．
- 解説の文体は「だ・である調」で統一する．

## 14. 用例

| 原稿 | 内容 |
|---|---|
| [`examples/kaisetsu/kaisetsu-opening.tex`](../examples/kaisetsu/kaisetsu-opening.tex) | 号の巻頭記事．題字と中央揃えの扉 |
| [`examples/kaisetsu/kaisetsu-feature.tex`](../examples/kaisetsu/kaisetsu-feature.tex) | 特集記事の扉．副題，飾り，段抜きの囲み |
| [`examples/kaisetsu/kaisetsu-components.tex`](../examples/kaisetsu/kaisetsu-components.tex) | 部品見本．見出しの 4 型と 2 本目の記事 |

```console
make kaisetsu
```

PDF は `build/public/kaisetsu/` に生成される．
