# 総目録

このプロジェクトが持つ書体，記号，見出しの記法，紙面の型を
一箇所に集めた目録である．「何があるか」を引くための索引であり，
「なぜそう組むか」は [`surikumi-style-guide.md`](surikumi-style-guide.md)，
[`kaisetsu-format.md`](kaisetsu-format.md)，
[`notation-style-guide.md`](notation-style-guide.md) に書いてある．

**短い名前で打ちたいときは [13 章](#13-短縮名)を見る．**
すべての長い命令に短い別名がある．

紙の見本は次で組む．PDF は `build/public/catalog/` に出る．

```bash
make catalog
```

| 見本 | 内容 |
|---|---|
| `surikumi-catalog.pdf` | 書体，Σ，色，記号，見出し，講義・演習・確認の部品，種類を選ばない部品，問題集の追加部品，短縮名 |
| `pattern-catalog.pdf` | 背景パターン31種と濃度・色味・寸法の効き方 |
| `kaisetsu-catalog.pdf` | 解説記事の版面で組んだ扉，見出しの4型，注，年表，囲み，参考文献，署名 |

---

## 0. 迷ったときの入口

**まず「記事の種類」を決める．書体や記号はそのあとで自動的に決まる．**
種類をまたいで見出し・注・数式番号を混ぜないことが，この目録の
唯一の重要な規則である．

| 作りたいもの | 読み込む | 版面 | 見出し | 目次の節 |
|---|---|---|---|---|
| 例題で進める講義 | `surikumi` | 8pt / 2段 | `\MMHeading`，`\MMSubheading` | [7.1](#71-講義と演習の見出し) |
| 問題一覧＋後掲解説 | `surikumi` | 8pt / 2段 | `\MMHeading` | [7.1](#71-講義と演習の見出し) |
| 公式・要点の確認 | `surikumi` | 8pt / 2段 | `\MMConfirmationSection` | [7.2](#72-確認の見出し) |
| 読み物としての解説記事 | `surikumi-kaisetsu` | 9pt / 2段 / 45行 | `\MKSection` | [7.3](#73-解説記事の見出し) |
| 問題集（10型から選ぶ） | `surikumi-mondaishu` | 8pt / 2段※ | 型ごと | [17](#17-問題集の型10案) |
| 模試・コンテスト | `surikumi` | 8pt / 2段 | `\MakeMathMockTitle` ほか | [8.5](#85-模試) |
| 表紙 | `surikumi` | 全面 | `\MakeMathMagazineCover` | [8.7](#87-表紙) |

※ 問題集の型3（見開き対応）と型10（模試）は 1 段組である．原稿の先頭で
`\PassOptionsToPackage{twocolumn=false}{surikumi}` を書く．

**種類を選ばない部品もある．** 強調（圏点・用語・ルビ），リード文，
公式囲み，まとめ，図表キャプション，全段幅ブロックは，どの記事でも
同じ意味で使う（[9 章](#9-記事の種類を選ばない部品)）．

判断が割れる二つの境目．

- **確認 か 講義 か**：十進見出しと `(i)` 列挙と正方形コメントが要るなら確認．
  例題から入るなら講義．講義に確認の部品を持ち込まない．
- **解説記事 か それ以外 か**：`\MKSection` などの `MK` 系と，
  `\MMHeading` などの `MM` 系は別系統である．同じ記事に混ぜない．

---

## 1. パッケージの地図

| パッケージ | 位置 | 役割 | 依存 |
|---|---|---|---|
| `surikumi` | プロジェクト直下 | 本体．版面，書体，色，Σ，パターン，可読性，講義・演習・確認・模試・表紙の部品 | LuaLaTeX，`jlreq` |
| `surikumi-kaisetsu` | プロジェクト直下 | 月刊解説誌の体裁．版面を上書きする | `surikumi` を自動で読む |
| `surikumi-mondaishu` | `examples/problem-sets/` | 問題集10型のための追加部品のみ | `surikumi` を自動で読む |
| `sugaku-sigma` | `texmf/tex/latex/sugaku-fourier/` | Σ の字形だけを自作フォントから取る | 自動で読まれる |
| `sugaku-fouriernc` | 同上 | 数式全体を Fourier 系にそろえる（任意） | `fouriernc` |

読み込みの原則．

```latex
% 本体だけ
\usepackage{surikumi}

% 解説記事．本体のオプションを変えるときは先に本体を読む
\usepackage[sigma=document]{surikumi}
\usepackage{surikumi-kaisetsu}

% 問題集
\usepackage{surikumi-mondaishu}

% 問題集で本体のオプションも変えるとき．順序が逆だと拒否される
\usepackage[runninghead,columnrule]{surikumi}
\usepackage{surikumi-mondaishu}
```

`surikumi-kaisetsu` と `surikumi-mondaishu` は自分のオプションを持たない．
本体のオプションを変えるときは，**必ず本体を先に読み込む**．
追加パッケージへ渡すと未知のオプションとして拒否される．

`surikumi` と `surikumi-kaisetsu` は版面を取り合う．後から読む
`surikumi-kaisetsu` が勝つ．一冊に両方の版面は入らない．

**原稿側で `amssymb` と `bm` を読み込まない．** `surikumi` は
`unicode-math` を使う．どちらかを重ねると，行内式の `\sum` の上下限が
Σ の右肩・右下へ戻ってしまう．読み込まれた場合は警告が出る．
`\bm` は `\symbf` の別名として最初から使える．

### 1.1 必須の外部パッケージ

`surikumi` が必ず読み込む．原稿側で書く必要はない．

`iftex` `kvoptions` `luatexja-fontspec`（`fontspec`）`xcolor` `graphicx`
`tikz`（`calc` `patterns` `patterns.meta`）`amsmath` `enumitem`
`tcolorbox`[most] `fancyhdr` `etoolbox` `contour` `pgfkeys`

`surikumi-kaisetsu` はこれに `geometry`（`layout=true` のとき）と
`stfloats` を加える．`surikumi-mondaishu` は `array` と `booktabs` を加える．

### 1.2 任意の外部パッケージ

見つからなければ機能を落として動く．エラーにはならない．

| パッケージ | 無いとどうなるか |
|---|---|
| `unicode-math` | 数式書体を設定せず，警告を出す |
| `luatexja-ruby` | `\MMKenten` はゴシック，`\MMRuby` は素通しになる |
| `cuted` | `mmwideblock` が段の中に収まる |
| `stfloats` | `mkfullinsert` を紙面の下に置けなくなる |

---

## 2. パッケージオプション

### 2.1 `surikumi`

| オプション | 既定 | 内容 |
|---|---|---|
| `layout` | `true` | 判型と版面（182×257mm，天14/地15/内外14mm）を設定する |
| `fonts` | `true` | 既定の和文・欧文**本文**書体を設定する |
| `mathfont` | `true` | 数式書体を設定する．`fonts` とは独立 |
| `mathfontname` | `TeX Gyre Termes Math` | 使う OpenType 数式書体 |
| `twocolumn` | `true` | 2段組にする |
| `footer` | `true` | 柱を出す |
| `bodyfontsize` | `8pt` | 本文の文字サイズ |
| `bodyleading` | `10.8pt` | 本文の行送り |
| `density` | `compact` | 垂直リズム（`compact`／`standard`／`airy`） |
| `sigma` | `custom` | Σ の出どころ（`custom`／`document`） |
| `penalties` | `true` | 行分割・改ページの調整（[10.1](#101-既定で効いている調整)） |
| `runninghead` | `false` | 2ページ目以降に柱を出す |
| `columnrule` | `false` | 段間に細い罫を引く |
| `interspacing` | `false` | 和欧間・和文間のアキを調整する |

```latex
% 従来相当のゆとり
\usepackage[density=standard,bodyleading=12pt]{surikumi}

% 読者が疲れにくい版
\usepackage[density=airy,interspacing]{surikumi}
```

`density` は行送りだけでなく，別行数式の前後，`align` の行間，
最低行間をまとめて制御する．原稿側で負の `\vspace` や局所的な
`\linespread` を足さない．

| `density` | `\lineskip` | 別行数式前後 | 短い別行数式 | `\jot` | 行送り |
|---|---|---|---|---|---|
| `compact`（既定） | .7pt | .42\*行送り | .18／.26\*行送り | .16\*行送り | 10.8pt |
| `standard` | 1pt | .55\*行送り | .25／.35\*行送り | 3pt | 10.8pt |
| `airy` | 1.3pt | .7\*行送り | .33／.45\*行送り | .22\*行送り | 12.2pt※ |

※ `airy` が行送りを 12.2pt へ広げるのは，`bodyleading` を明示していない
場合だけである．明示したときはその値をそのまま使う．

### 2.2 `surikumi-kaisetsu`

| オプション | 既定 | 内容 |
|---|---|---|
| `bodysize` | `9pt` | 本文の文字サイズ |
| `leading` | `14.2pt` | 本文の行送り |
| `lines` | `45` | 1段あたりの行数．版面の高さがこれで決まる |
| `gutter` | `8mm` | 段間 |
| `sectionstyle` | `bar` | 節見出しの既定の型 |
| `eqnumbering` | `section` | 数式番号（`section`／`continuous`／`none`） |
| `layout` | `true` | 判型と版面（天12/地20/内外18mm）を設定する |
| `footer` | `true` | 柱を出す |
| `footnotes` | `true` | 注を `*1)` 形式にする |
| `captions` | `true` | 図表見出しをこの形式にする |
| `flushbottom` | `false` | 段の下端をそろえる |

---

## 3. 書体

### 3.1 既定の書体

| 用途 | 書体 | 呼び出し |
|---|---|---|
| 和文本文 | Noto Serif CJK JP | `\normalfont\mcfamily` |
| 和文見出し | Noto Sans CJK JP | `\sffamily\gtfamily\bfseries` |
| 欧文本文 | TeX Gyre Termes | `\rmfamily` |
| 欧文見出し | TeX Gyre Heros | `\sffamily` |
| 数式 | TeX Gyre Termes Math | 自動 |
| `\sum` | SugakuFourier-Math-Extension（自作） | 自動 |

和文は Noto CJK JP を優先する．ウェイト別の名前を持たない可変フォント
（Noto Serif JP／Noto Sans JP）しか無い環境では，ウェイト軸で
本文 400，太字 700，題字 900，著者名 600 を指定して同等の太さを得る．
どちらも無ければ jlreq の既定書体になる．

数式書体を欧文本文と同じ Termes 系にそろえるのは，そうしないと
欧文本文が Termes なのに数式だけ Latin Modern になり，同じ行の中で
字面と太さが食い違うためである．

```latex
\usepackage[fonts=false]{surikumi}                    % 本文書体だけ止める
\usepackage[mathfontname={STIX Two Math}]{surikumi}   % 別の数式書体
\usepackage[mathfont=false]{surikumi}                 % 数式書体を設定しない
```

`unicode-math` が定義しない `\square` と `\blacksquare` は
パッケージ側で補っている．

### 3.2 表示用の書体マクロ

| マクロ | 実体 | 使うところ |
|---|---|---|
| `\SMTitleFont` | Noto Sans CJK JP Black（12%斜体） | 記事の表題 |
| `\SMSeriesFont` | Noto Sans CJK JP Black | シリーズ名 |
| `\SMAuthorMinchoFont` | Noto Serif CJK JP SemiBold | 署名（明朝） |
| `\SMAuthorGothicFont` | Noto Sans CJK JP Bold | 署名（ゴシック） |
| `\MKBodyFace` | 本文明朝 | 解説記事の本文 |
| `\MKHeadingFace` | ゴシック太 | 解説記事の見出し |
| `\MKTitleFace` | `\SMAuthorMinchoFont` | 解説記事の表題 |
| `\MKGothicTitleFace` | `\SMAuthorGothicFont` | 同上（ゴシック） |
| `\MKMastheadFace` | TeX Gyre Termes（字間 7.0） | 号の題字 |
| `\MKPageNumberFace` | `\rmfamily\bfseries` | ノンブル |

**本文・答案・場合分け・注記の書体を変えてよい理由は存在しない．**
書体を変えるのは見出しとラベルだけである．強調が必要なときは
[9.1](#91-強調)の圏点かゴシックを使う．

### 3.3 解説記事の文字サイズ

`surikumi-kaisetsu.sty` の第3節にマクロとして置いてある．
一箇所を書き換えれば紙面全体に及ぶ．

あわせて `\normalsize` から `\Huge` までのサイズ命令が本文比で定義し直される．
フロートの中でクラス既定のサイズへ戻ってしまうのを防ぐためである．

| 命令 | 本文比 | | 命令 | 本文比 |
|---|---|---|---|---|
| `\small` | .92 | | `\large` | 1.16 |
| `\footnotesize` | .84 | | `\Large` | 1.4 |
| `\scriptsize` | .76 | | `\LARGE` | 1.7 |
| `\tiny` | .66 | | `\huge` | 2 |
| | | | `\Huge` | 2.4 |

| 要素 | サイズ / 行送り |
|---|---|
| 題字 | 17 / 20 |
| 題字の左右 | 9.6 / 11 |
| 特集名 | 8.6 / 10.5 |
| 表題 | 21.5 / 26 |
| 副題 | 10.5 / 13 |
| 署名 | 14 / 16.5 |
| 節見出し | 9.8 / 12 |
| 小見出し | 9.2 / 11.5 |
| 図表見出し | 7.6 / 10.2 |
| 注 | 6.9 / 8.8 |
| 柱 | 7.6 / 9 |
| ノンブル | 9.5 / 11 |
| 参考文献・年表・署名 | 7.3 / 9.6 |

---

## 4. 記号

### 4.1 Σ

`surikumi` は `\sum` を再定義し，行内式でも別行数式でも同じ
`textstyle` の小型 Σ を使い，上下限を必ず真上と真下に置く．
原稿側で `\textstyle` や `\limits` を書く必要はない．

```latex
和 $S_n=\sum_{k=1}^{n}a_k$ を考える．     % 行内
\[ S_n=\sum_{k=1}^{n}a_k \]               % 別行．Σ の大きさは同じ
```

| コマンド | 内容 |
|---|---|
| `\sum` | 小型 Σ ＋ 上下配置．通常はこれだけを使う |
| `\SugakuSumText` | 自作フォントの text 用 Σ（`sugaku-sigma` が提供） |
| `\SugakuSumDisplay` | 同じく display 用の大型 Σ |
| `\MMCompactSum{下限}{上限}` | 旧ソース互換．新規原稿では使わない |

`\sum\nolimits` は使わない．別行数式の Σ だけを大型字形へ切り替えない．
文書側の Σ に戻すときは `\usepackage[sigma=document]{surikumi}`．

### 4.2 確認記事の正方形と矢印

**四つの記号は，見た目ではなく「用途 × 対象読者」で選ぶ．**

| 記号 | 意味 | 対象読者 | 短い形 | 長い形（環境） |
|---|---|---|---|---|
| 斜線入り正方形 | コメント | すべての読者 | `\MMConfirmationGeneralComment` | `mmconfirmationgeneralcomment` |
| 黒塗り正方形 | コメント | 意欲的な読者 | `\MMConfirmationAdvancedComment` | `mmconfirmationadvancedcomment` |
| 斜線入り矢印 | 注釈 | すべての読者 | `\MMConfirmationGeneralNote` | `mmconfirmationgeneralnote` |
| 黒塗り矢印 | 注釈 | 意欲的な読者 | `\MMConfirmationAdvancedNote` | `mmconfirmationadvancednote` |

短縮名では `\MMCom`／`\MMComA`／`\MMAnn`／`\MMAnnA` となる
（[13 章](#13-短縮名)）．

記号だけを置く命令もある．

| 命令 | 短縮名 | 出るもの |
|---|---|---|
| `\MMConfirmationStripedMark` | `\MMComMark` | 斜線入り正方形 |
| `\MMConfirmationFilledMark` | `\MMComAMark` | 黒塗り正方形 |
| `\MMConfirmationStripedNoteMark` | `\MMAnnMark` | 斜線入り矢印 |
| `\MMConfirmationFilledNoteMark` | `\MMAnnAMark` | 黒塗り矢印 |

互換名（新規原稿では使わない）．

| 互換名 | 実体 |
|---|---|
| `\MMConfirmationNote`，`mmconfirmationnote` | 斜線入り矢印＝全読者向け注釈 |
| `mmconfirmationcomment` | 斜線入り正方形＝全読者向けコメント |

斜線の角度・間隔・線幅・開始位置は記号自身のローカル座標に固定してある．
原稿側で TikZ や Unicode で似た記号を作り足さない．

### 4.3 そのほかの記号

| 記号 | 命令 | 意味 |
|---|---|---|
| ▶ | `\MMNote{...}` | 講義の短い注記．三角も本文も本文と同じ大きさ |
| `1°`，`2°` | `\MMCaseHeading{1}{条件}` | 答案中の場合分け．黒四角を付けない |
| `*` | `\MMTimeMarks{10}` | 目標時間 10 分 |
| `°` | `\MMFiveMinuteMark` | 目標時間 5 分．`\MMTimeMarks{25}` は `**°` |
| 圏点 | `\MMKenten{...}` | 本文の強調．記号は `\MMKentenMark` |
| 白枠 | `\MMBlank[12mm]` | 記入欄 |
| □ | `\MSCheckbox` | 自己確認欄のチェックボックス |
| 黒角丸ラベル | `\MMBlackLabel{文字}` | 小さな黒ラベル |
| 丸みの強い黒ラベル | `\MMSolutionLabel{解}` | 解答ラベル |
| 黒丸数字 | `\MMMockNumber{1}` | 模試の大問番号 |
| ★ | `\MMAlternative[★]{見出し}` | 別解 |

答・最終結果・途中の主要結果を四角い枠で囲まない．
`\boxed`，`\fbox`，`\framebox` を強調に使わない．
公式を示す `\MMFormulaBox` は別物である（[9.2](#92-リード文公式まとめ)）．

### 4.4 数式表記の要点

全文は [`notation-style-guide.md`](notation-style-guide.md)．よく引くものだけ．

| 対象 | 使う | 使わない |
|---|---|---|
| 組合せ | `{}_n\mathrm{C}_r` | `\binom{n}{r}` |
| ベクトル | `\bm{v}`（＝`\symbf`） | `\vec{v}` |
| 大きさ | `\lVert\bm{v}\rVert` | `|\bm{v}|` |
| 微分記号 | `\mathrm{d}x` | `dx` |
| 分数 | `\dfrac` | `\frac`（高さが過剰な場合のみ許容） |
| 定数 | `\mathrm{e}`，`\mathrm{i}` | `e`，`i` |
| 不等号 | `\leq`，`\geq` | `\leqq`，`\geqq` |
| 近似 | `\simeq` | `\approx` |
| 積 | `ma`，`2\pi r` | `m \times a` |
| 句読点 | `，．` | `、。` |

別行数式の末尾に句読点を入れない．

---

## 5. 色

| 名前 | 値 | 用途 |
|---|---|---|
| `SMink` | gray 0.12 | 本文・罫・ラベルの黒 |
| `SMrule` | gray 0.38 | 細い罫 |
| `SMpale` | gray 0.92 | 淡い地 |
| `SMband` | gray 0.84 | 帯の地 |
| `SMpatternA` | gray 0.70 | 扉パターンの明部 |
| `SMpatternB` | gray 0.56 | 扉パターンの暗部 |
| `SMcoverBlue` | `#0757B5` | 表紙 |
| `SMcoverDeepBlue` | `#003F91` | 表紙 |
| `SMcoverOrange` | `#F06A21` | 表紙 |
| `SMcoverCyan` | `#65C5E8` | 表紙 |
| `SMcoverViolet` | `#5657A6` | 表紙 |
| `SMcoverLime` | `#EAF3B0` | 表紙 |
| `SMcoverWarm` | `#FFF4C7` | 表紙 |
| `SMpatternInk` | 計算値 | 背景パターンのインク．`pattern-tone` と `pattern-accent` の結果が入る．直接指定しない |

本文の紙面はグレースケール，表紙だけが色を持つ．
背景パターンへ色味を足すときは `pattern-accent`（[6.2](#62-濃度色味寸法)）を使い，
本文の色には使わない．

---

## 6. 背景パターン

### 6.1 31種と三つの系統

`\MathMagazineSetup{pattern=...}` で選ぶ．名前はすべて小文字である．
すべて公有の意匠を pgf のパスで独自に作図したものであり，
参考紙面の図案の複製ではない．

| 系統 | 数 | 名前 |
|---|---|---|
| 幾何 | 12 | `scales`（既定） `triangles` `diamonds` `chevrons` `weave` `hexagons` `pinwheels` `zigzags` `checker` `parquet` `origami` `ribbons` |
| 和柄 | 10 | `asanoha` `seigaiha` `shippou` `kikkou` `sayagata` `kagome` `yagasuri` `tatewaku` `mitsukuzushi` `ajiro` |
| 数学的モチーフ | 9 | `truchet` `isocubes` `sierpinski` `lattice` `moire` `envelopes` `girih` `packing` `spirals` |

濃さの目安．白抜きの題字（`title-fill=white`）を載せるときは，
薄い側を選ぶか `pattern-tone` を落とす．

- 数学的モチーフ（薄→濃）：`lattice` ＜ `sierpinski` ＜ `envelopes` ＜
  `truchet` ＜ `spirals` ＜ `packing` ＜ `girih` ＜ `moire` ＜ `isocubes`
- 和柄：線画の6種（`asanoha` `seigaiha` `shippou` `kikkou` `sayagata`
  `kagome`）が薄く，面塗りの4種（`yagasuri` `tatewaku` `mitsukuzushi`
  `ajiro`）が濃い

### 6.2 濃度・色味・寸法

| キー | 既定 | 内容 |
|---|---|---|
| `pattern-tone` | `normal` | `pale` / `light` / `normal` / `strong` |
| `pattern-accent` | `none` | 任意の色名．`none` で無彩色 |
| `pattern-scale` | `1` | タイルの倍率 |

```latex
\MathMagazineSetup{
  pattern=girih,
  pattern-tone=light,
  pattern-accent=SMcoverBlue,
  pattern-scale=1.2
}
```

**効き方に例外が二つある．**

- `pattern-scale` は数学的モチーフの9種にだけ効く．幾何12種と和柄10種は
  タイル寸法が宣言時に固定されるため，指定しても黙って無視される．
- 和柄10種は inherently coloured pattern として宣言してあり，タイル内部の
  階調をそのまま出力へ残す．したがって `pattern-accent` と
  `pattern-tone` のうちインク色の指定は効かず，白ベールだけが効く．

`pattern-tone=normal` は従来の見え方をそのまま再現する．
`strong` は白ベールを外すので，題字を載せない帯にだけ使う．

### 6.3 バナー以外の部品

| 命令 | 短縮名 | 用途 |
|---|---|---|
| `\MMPatternRule[高さ]` | `\MMPRule` | 節の区切りに使う細い帯（既定 3.2mm） |
| `\MMPatternSwatch[高さ]{幅}` | `\MMSwatch` | 行中に置く見本（既定の高さ 3.4mm） |

どちらも `\MathMagazineSetup` で選んだパターンと濃度をそのまま使う．
小さな見本では `pattern-scale` を 1 未満にして，図柄が1単位分収まるようにする．

---

## 7. 見出しの記法

**三系統ある．ここが最も混乱しやすい．同じ記事に混ぜない．**

### 7.1 講義と演習の見出し

| 命令 | 短縮名 | 体裁 |
|---|---|---|
| `\MMHeading{解説}` | — | 段幅の枠に中央寄せ・大きめのゴシック |
| `\MMSubheading{...}` | `\MMSubhead` | 行頭のゴシック太 |
| `\MMCaseHeading{1}{$x\geq0$ のとき}` | `\MMCase` | `1°　条件`，本文と同じ明朝 |

### 7.2 確認の見出し

十進番号を持つ．`\MMConfirmationReset`（`\MMReset`）が両方のカウンタを 0 に戻すので，
次の見出しが `1.` から始まる．
星付きは番号を進めない．

| 命令 | 短縮名 | 体裁 |
|---|---|---|
| `\MMConfirmationSection{...}` | `\MMSec` | `1.　見出し`（10.5pt ゴシック） |
| `\MMConfirmationSubsection{...}` | `\MMSub` | `1.1　見出し`（9.2pt ゴシック） |
| `\MMConfirmationRunInHeading{等比型}` | `\MMRun` | 行頭の型名．本文がそのまま続く |

途中番号から始めるときは，最初の見出しより前で
`\setcounter{mmconfirmationsection}{2}` とする．

### 7.3 解説記事の見出し

`\MKSection` は 4 型を持つ．紙面全体の既定を `section-style` で決め，
例外だけ `\MKSection[型]{...}` にする．段落ごとに気分で変えない．

| 型 | 体裁 | 用途 |
|---|---|---|
| `bar`（既定） | 段幅の罫の下に柱と見出し | 通常の節見出し |
| `pillars` | 両端の柱の間に中央寄せ | 特集記事の節見出し |
| `band` | 上下の罫と両端の柱 | 章が切り替わる位置 |
| `plain` | 罫も柱もなし | 短い記事，囲みの中 |

| 命令 | 体裁 |
|---|---|
| `\MKSection{...}` | 番号付きの節．星付きは番号を進めない |
| `\MKSubsection{...}` | `1.1` 形式．1字下げから始まる |
| `\MKRunIn{注意}` | 行頭のゴシック．本文がそのまま続く |

### 7.4 三系統の対照

| 役割 | 講義・演習 | 確認 | 解説記事 |
|---|---|---|---|
| 大きな区切り | `\MMHeading` | `\MMConfirmationSection` | `\MKSection` |
| その下 | `\MMSubheading` | `\MMConfirmationSubsection` | `\MKSubsection` |
| 行頭の語 | — | `\MMConfirmationRunInHeading` | `\MKRunIn` |
| 番号 | なし | `1.` / `1.1` | `1` / `1.1` |
| 数式番号 | `\begin{equation}` | 同左 | `(1.1)` 節ごと |
| 注 | `\MMNote`（▶） | 正方形・矢印 | `\footnote`（`*1)`） |
| 図表見出し | `\MMCaption` | 同左 | `\caption` |

---

## 8. 部品一覧（`surikumi`）

### 8.1 扉と設定

| 部品 | 短縮名 | 引数 | 内容 |
|---|---|---|---|
| `\MathMagazineSetup` | `\MMSetup` | 鍵と値 | 次の扉の内容を決める |
| `\MakeMathMagazineTitle` | `\MMTitle` | — | 全段抜きの扉を組み，2段組の本文に入る |
| `\MMTitleBanner` | — | — | 帯だけを置く（自作の扉を組むとき） |

`\MathMagazineSetup` の鍵．

| 鍵 | 既定 | 内容 |
|---|---|---|
| `feature` | `特集　入試数学の要点をつかむ` | 特集名．空にすると省略 |
| `series` | `講義／数学` | シリーズ名 |
| `title` | `数列の基礎` | 表題 |
| `author` | `数学編集部` | 署名 |
| `deck` | 空 | 導入文 |
| `pattern` | `scales` | 背景パターン（[6.1](#61-31種と三つの系統)） |
| `pattern-tone` | `normal` | パターンの濃度 |
| `pattern-accent` | `none` | パターンの色味 |
| `pattern-scale` | `1` | パターンの倍率 |
| `series-position` | `center` | `center`／`left` |
| `title-fill` | `black` | `black`／`white` |
| `author-position` | `right` | `right`／`center` |
| `author-font` | `mincho` | `mincho`／`gothic` |

### 8.2 講義

| 部品 | 短縮名 | 引数 | 内容 |
|---|---|---|---|
| `mmexample` | — | `[番号]{表題}` | 例題．実線の枠 |
| `mmproblem` | — | `[番号]{表題}` | 問題 |
| `mmsolution` | — | `[解]` | 解答．黒ラベル付き，枠なし |
| `\MMAlternative` | `\MMAlt` | `[★]{見出し}` | 別解 |
| `\MMNote` | — | `{本文}` | 短い注記（▶） |

### 8.3 ベーシック演習

| 部品 | 短縮名 | 引数 | 内容 |
|---|---|---|---|
| `mmproblems` | — | — | 番号付き問題一覧（`1.` 大きめゴシック） |
| `\MMSource` | — | `{26 ○○大・理}` | 出典．右寄せ |
| `\MMExerciseNumber` | `\MMExNum` | `{3}` | 明朝のままの問題番号 |
| `\MMBlackLabel` | `\MMLabel` | `{答}` | 小さな黒ラベル |
| `\MMSolutionLabel` | `\MMSolLabel` | `{解}` | 解答ラベル |
| `\MMBlank` | — | `[12mm]` | 記入欄 |

### 8.4 確認

| 部品 | 短縮名 | 引数 | 内容 |
|---|---|---|---|
| `\MMConfirmationReset` | `\MMReset` | — | 節・小節の番号を振り直す（カウンタを 0 にする） |
| `\MMConfirmationSection` | `\MMSec` | `*{...}` | 大きな節 |
| `\MMConfirmationSubsection` | `\MMSub` | `*{...}` | 節内の小項目 |
| `\MMConfirmationRunInHeading` | `\MMRun` | `{型名}` | 行頭の型名 |
| `mmconfirmationroman` | `mmroman` | — | `(i)` `(ii)` 形式の列挙 |
| `\MMConfirmation*Comment` | `\MMCom`，`\MMComA` | `[番号]{本文}` | 正方形コメント |
| `\MMConfirmation*Note` | `\MMAnn`，`\MMAnnA` | `[番号]{本文}` | 矢印注釈 |
| `mmconfirmationproof` | `mmproof` | `[証明]` | 証明表示 |
| `\MMConfirmationProofLabel` | `\MMProofLabel` | `[証明]` | 証明ラベルだけ |

注記番号は，同じ局所的な説明の中で関連する注記が続く場合だけ付ける．
単発の注記に `[1]` を付けない．新しい系列は `1` から始める．

### 8.5 模試

| 部品 | 短縮名 | 引数 | 内容 |
|---|---|---|---|
| `\MathMockSetup` | `\MMMockSetup` | 鍵と値 | 模試の情報 |
| `\MakeMathMockTitle` | `\MMMockTitle` | — | 模試の扉 |
| `\MMMockBanner` | — | — | 帯だけ |
| `mmmockpaper` | — | `[表題]` | 試験冊子の外枠．分割可 |
| `mmmockquestion` | — | `{番号}[分類]` | 大問 |
| `mmmockparts` | — | — | `（1）` 形式の小問 |
| `\MMMockNumber` | — | `{1}` | 黒丸の大問番号 |

`\MathMockSetup` の鍵：`name`，`course`，`audience`，
`description-label`，`description`，`time-label`，`time`．

### 8.6 コンテスト

| 部品 | 短縮名 | 引数 | 内容 |
|---|---|---|---|
| `\MathContestSetup` | `\MMContestSetup` | 鍵と値 | コンテストの情報 |
| `mmcontestproblem` | `mmcontest` | `[番号]{表題}` | 出題 |
| `\MMContestAssessment` | `\MMAssess` | `[時間]` | 難易と目標時間の表示 |
| `\MakeMathContestAnswerSheet` | `\MMAnswerSheet` | `[...]` | 答案用紙 |
| `\MakeMathContestInfoSheet` | `\MMInfoSheet` | — | 応募要項の面 |
| `\MMContestInfoSection` | `\MMInfoSec` | `{見出し}{本文}` | 要項の一項目 |
| `\MMContestPostalBoxes` | `\MMPostal` | — | 郵便番号枠 |
| `\MMContestRuledLines` | `\MMRuled` | `{行数}` | 罫線 |
| `\MMContestCutRule` | `\MMCut` | `[切り取り線]` | 切り取り線 |
| `\MMContestCellLabel` | `\MMCell` | `{文字}` | 枠内の見出し |

`\MathContestSetup` の鍵：`title`，`issue`，`courses`，`volume`，
`date-code`，`answer-times`，`deadline`，`return-date`．

### 8.7 表紙

| 部品 | 短縮名 | 引数 | 内容 |
|---|---|---|---|
| `\MathCoverSetup` | `\MMCoverSetup` | 鍵と値 | 表紙の情報 |
| `\MakeMathMagazineCover` | `\MMCover` | — | 表紙一面 |
| `\MMCoverMainItem` | — | `{見出し}{説明}` | 大きな目次項目 |
| `\MMCoverSubItem` | — | `{見出し}{説明}` | 小さな目次項目 |
| `\MMCoverClearItems` | — | — | 目次項目を消す |

`\MathCoverSetup` の鍵：`masthead`，`publication-note`，`release-note`，
`month`，`year`，`feature-label`，`feature-title`，`publisher`，
`animal-image`，`animal-x`，`animal-y`，`animal-width`，`animal-opacity`．

### 8.8 難易度と目標時間

| 部品 | 短縮名 | 引数 | 内容 |
|---|---|---|---|
| `\MMLegend` | — | `[断り]{凡例}` | 「◎問題の難易と目標時間」の帯 |
| `\MMDifficulty` | `\MMDiff` | `{A}{20}` | 難易度記号 ＋ 目標時間 |
| `\MMDifficultyItem` | `\MMDiffItem` | `{番号}{A}{20}` | 凡例の1項目．`1⋯A**` の形 |
| `\MMTimeMarks` | — | `{25}` | `**°`．5 の倍数以外は警告 |
| `\MMFiveMinuteMark` | `\MMFive` | — | `°` 単体 |

---

## 9. 記事の種類を選ばない部品

講義・演習・確認・解説記事のどれでも，同じ意味で使う．

### 9.1 強調

和文の強調は，書体・ウェイト・文字サイズを変えない方法を優先する．

| 用途 | 部品 | 引数 |
|---|---|---|
| 文中の一時的な強調 | `\MMKenten` | `{語}` |
| 用語の初出 | `\MMTerm` | `{語}` |
| 読みにくい術語の読み | `\MMRuby` | `{語}{読み}` |

```latex
和の上端と下端は\MMKenten{必ず}確認する．
\MMTerm{階差数列}を $b_n=a_{n+1}-a_n$ とおく．
\MMRuby{漸化式}{ぜんかしき}を立てる．
\MMRuby{階|差|数|列}{かい|さ|すう|れつ}   % 語ごとに区切る
```

圏点の記号は `\MMKentenMark` に入っており，誌面全体の方針として
差し替えられる（既定は本文1字より小さい丸）．記事ごとに切り替えず，
誌面で1種類に統一する．**正方形は使わない**——正方形は確認系の
コメントだけを意味するという規約を，強調のために崩さない．

圏点は行送りを変えない．ルビはその行の行間を 1.5pt 程度押し広げるので，
読みの必要な語だけに使う．

### 9.2 リード文，公式，まとめ

| 用途 | 部品 | 短縮名 | 引数 |
|---|---|---|---|
| 節冒頭のリード文 | `\MMLead` | — | `{本文}` |
| 公式の提示 | `\MMFormulaBox` / `mmformulabox` | `\MMFormula` | `[公式]{本文}` |
| 節末のまとめ | `\MMSummary` / `mmsummary` | — | `[まとめ]{本文}` |

```latex
\MMLead{和の公式は，上端と下端の確認から始める．}

\MMFormulaBox{%
  \[
    \sum_{k=1}^{n}k=\dfrac{n(n+1)}{2}
  \]}

\MMSummary{使える $n$ の範囲を必ず確かめる．}
```

**公式の提示と答の強調は別物である．** `\MMFormulaBox` は閉じた四角では
なく，左の太い罫と淡い地色と「公式」ラベルで構成する．答を示すときは
解答ラベルと通常の別行数式を使う（[4.3](#43-そのほかの記号)）．

`\MMLead` は本文と同じ書体・大きさで組み，細い罫線と字下げだけで
区別する．見出しの代わりに使わない．

### 9.3 図表キャプション

```latex
\MMCaption{等差数列の項は等間隔に並ぶ}   % 図1，図2，…
\MMCaption[table]{よく使う和の公式}      % 表1，表2，…
\MMCaption*{番号を付けないキャプション}
```

図と表は別々に番号が付く．カウンターは `mmfigure` と `mmtable`，
ラベル名は `\MMFigureName`，`\MMTableName` で変更できる．
`\label` を続ければ `\ref` が「図3」のように種別ごと出力する．
図のキャプションは図の下に，表のキャプションは表の上に置く．

### 9.4 一時的に全段幅を使う

1段に収まらない式は，まず式を分ける．それでも収まらないときだけ
全段幅へ逃がす．

```latex
\begin{mmwideblock}
  \[
    \sum_{k=1}^{n}k(k+1)(k+2)(k+3)=\dfrac{n(n+1)(n+2)(n+3)(n+4)}{5}
  \]
\end{mmwideblock}
```

短いものには `\MMWideBlock{...}` を使う．1段組の記事では通常の
別行ブロックとして組まれる．

全段幅ブロックは，そのページで先に組まれた両方の段の下に置かれる．
原稿では1段の途中にあっても，刷り上がりでは左段・右段がそこで打ち切られ，
ブロックはその下へ回る．片方の段の下端に空きが残るのは `\raggedbottom` の
下では正常な結果であり，負の `\vspace` で詰めない．
前後のアキは `\stripsep` が本文の行送りから決める．

記事あたり数か所までとし，本文の流れを細かく分断しない．

---

## 10. 可読性レイヤ

### 10.1 既定で効いている調整

`penalties`（既定 `true`）が次を一括して制御する．紙面の見た目を
変えるのではなく，狭い段で起きる組版上の欠陥を防ぐためのものなので，
通常は有効のまま使う．

- 段末に段落の第1行だけが残ること，段頭に最終行だけが置かれることを禁じる
- 分割された語の後半だけを次の段の先頭へ送らない
- 狭い段の行分割に余裕を持たせ，最後の手段として `\emergencystretch` を使う
- 行内の長い式を関係記号や二項演算子のあとで折り返せるようにする
- 複数行の別行数式が段をまたげるようにする（`\allowdisplaybreaks[1]`）

原稿側で `\clubpenalty`，`\tolerance`，`\allowdisplaybreaks` を
重ねて指定しない．

### 10.2 見た目を変えるオプション

すべて既定 `false`．記事や誌面の設計として選んだときだけ指定する．
**記事ごとに切り替えず，誌面全体で統一する．**

| オプション | 内容 |
|---|---|
| `runninghead` | 2ページ目以降に柱を出す |
| `columnrule` | 段間に 0.25pt の細い罫を引く |
| `interspacing` | 和欧間を `.22\zw plus .1\zw minus .05\zw`，和文間を `0pt plus .25\zw minus .02\zw` にする |

```latex
\usepackage[runninghead,columnrule,interspacing]{surikumi}

\MMRunningHead{数列の確認}             % 左右とも同じ
\MMRunningHead[要点の整理]{数列の確認}  % 左ページ／右ページ
```

`runninghead` の柱は `\MathMagazineSetup` の `series`（左ページ）と
`title`（右ページ）を自動的に使う．長すぎるときだけ
`\MMRunningHead`（短縮名 `\MMHead`）で上書きする．

`columnrule` の罫の長さは，左右の段のうち長いほうの内容の高さに合わせる．
記事の最終ページのように段が短いページでは罫も短くなり，本文の無い
ところへ垂れ下がらない．

`interspacing` が固定するのは和欧間（`xkanjiskip`）で，`.22\zw` を中心に
わずかな伸縮を残す．和文間（`kanjiskip`）は 0 を中心に伸びるだけである．
8pt の本文で行内式が本文へ埋もれるのを防ぐためのもので，既定を変えないのは
既刊の紙面の行分割が変わるためである．

### 10.3 第三の密度

`density=airy` は長時間読ませる記事のための版で，行送り，別行数式の前後，
`align` の行間をまとめて開く（[2.1](#21-surikumi)の表）．

---

## 11. 部品一覧（`surikumi-kaisetsu`）

### 11.1 号と記事

| 部品 | 短縮名 | 引数 | 内容 |
|---|---|---|---|
| `\MathKaisetsuSetup` | `\MKSetup` | 鍵と値 | 号と記事の情報 |
| `\MKMakeTitle` | `\MKTitle` | — | 全段抜きの扉．前に `\clearpage` は要らない |
| `\MKArticleReset` | `\MKReset` | — | 節・小節・数式・図・表・注のカウンタを 0 に戻す |
| `\MKMasthead` | — | — | 題字だけ |
| `\MKFeatureLabel` | `\MKFeat` | `{特集名}` | 特集名だけ |
| `\MKFeatureBar` | `\MKFeatBar` | `[長さ]{特集名}` | 罫で挟んだ特集名 |
| `\MKName` | — | `{姓}{名}` | 姓名の間を全角1字あける |

`\MathKaisetsuSetup` の鍵．

| 鍵 | 内容 |
|---|---|
| `journal-name` | 柱に出す誌名 |
| `masthead-first`，`masthead-second` | 題字の欧文2行 |
| `issue-date`，`issue-number` | 題字の左右 |
| `footer-line` | 柱の文字列を直接指定 |
| `feature` | 特集名．空にすると省略 |
| `title`，`subtitle` | 表題と副題 |
| `author`，`author-reading`，`affiliation` | 署名，読み，所属 |
| `ornament`，`ornament-width` | 扉の飾りとその幅 |
| `align` | `center`（巻頭）／`left`（特集記事） |
| `title-font` | `mincho`（既定）／`gothic` |
| `masthead` | 題字を出すか |
| `feature-bar` | 特集名を罫で挟むか |
| `feature-rule-width` | 特集の罫の長さ |
| `section-style` | 節見出しの型 |
| `footer-placement` | `odd`（既定）／`both`／`none` |

値に `,` を含む鍵は，値全体をもう一重の中括弧で囲む．

### 11.2 本文の部品

| 部品 | 短縮名 | 引数 | 内容 |
|---|---|---|---|
| `\MKSection` | — | `*[型]{...}` | 節見出し（4型．[7.3](#73-解説記事の見出し)） |
| `\MKSubsection` | — | `*{...}` | 小見出し |
| `\MKRunIn` | — | `{注意}` | 行頭の見出し |
| `\MKRemark` | — | `[注意]{本文}` | 注意などの段落 |
| `mkremark` | — | `[注意]` | 同上（複数段落） |
| `mkquote` | — | — | 引用．左を1字下げる |
| `mkfigurebody` | `mkfig` | — | 図の中身を段の中央にそろえる |
| `mkchronology` | `mkchrono` | `{表題}` | 年表 |
| `\MKChronoItem` | — | `{1744}{事項}` | 年表の1行 |
| `mkinsert` | — | — | 段の中の囲み |
| `mkfullinsert` | `mkfull` | `[b]` | 段抜きの囲み |

`mkfullinsert` は浮動体である．紙面の下に置くには，その紙面の組版が
終わる前に宣言しておく必要がある．記事の末尾に書くと次の紙面へ送られる．

### 11.3 番号，注，文献，署名

| 部品 | 短縮名 | 引数 | 内容 |
|---|---|---|---|
| `\MKEquationNumbering` | `\MKEqNum` | `{continuous}` | 数式番号の方式を切り替える |
| `\footnote` | — | `{本文}` | 段下の注（`*1)` 形式） |
| `\MKUnmarkedNote` | `\MKNote` | `{本文}` | 本文に印を出さない注 |
| `mkreferences` | `mkrefs` | `[参考文献]` | 参考文献．見出し＋罫＋`mkreflist` |
| `mkreflist` | — | — | `1)` 形式の番号リストだけ．見出しが要らないとき |
| `\MKCite` | — | `{1,2}` | 肩付きの `1,2)` |
| `\MKByline` | — | — | 記事末の署名 |
| `\MKBylineText` | — | `{本文}` | 署名の文言を差し替える |

注は `*1)`，文献参照は `1)`．形を入れ替えない．

---

## 12. 部品一覧（`surikumi-mondaishu`）

`surikumi` が持たない部品だけを足してある．`surikumi` の再定義はしていない．

| 部品 | 短縮名 | 引数 | 内容 | 使う型 |
|---|---|---|---|---|
| `mshint` | — | `{段}` | 段階ヒント | 4 |
| `\MSHint` | — | `{段}{本文}` | 同上（1行） | 4 |
| `\MSHintLabel` | — | `{段}` | ヒントのラベルだけ | 4 |
| `\MSHintBreak` | — | — | 解答前の区切り罫 | 4 |
| `msdrill` | — | — | 短問の連番リスト | 5, 8 |
| `msanswerstrip` | `msans` | — | 分割不可の答えの帯 | 5, 8 |
| `\MSAns` | — | `{番号}{答}` | 帯の中の1問 | 5, 8 |
| `\MSAnswerStripLabel` | `\MSAnsLabel` | — | 帯のラベル | 5, 8 |
| `msmistake` | — | `[よくある誤答]` | 左罫つき誤答領域 | 6, 7 |
| `\MSWhereWrong` | — | `{本文}` | 誤りの所在 | 6, 7 |
| `msrubric` | — | `[採点基準]` | 採点基準表 | 7, 10 |
| `\MSComment` | — | `{本文}` | 講評 | 7 |
| `\MSPattern` | — | `{型名}` | 通し番号つき型見出し | 8 |
| `\MSPatternReset` | `\MSPReset` | — | 型番号を 0 に戻す | 8 |
| `msprocedure` | `msproc` | — | 手順の列挙 | 8 |
| `msindex` | — | — | 難易度つき一覧表 | 9 |
| `\MSCheckbox` | — | — | チェックボックス | 10 |
| `\MSCheckItem` | — | `{本文}` | 自己確認欄の1行 | 10 |
| `\MSSpreadHeading` | `\MSSpread` | `{見出し}` | 見開きの面見出し | 3, 10 |
| `\MSStartVerso` | — | — | 次を必ず偶数ページ（左）へ送る | 3, 10 |

**表の二つは列の書き方が決まっている．** `\item` ではなく `&` で区切る．

```latex
\begin{msrubric}                              % 観点 & 配点
  場合分けの条件を明記している & 2 \\
\end{msrubric}

\begin{msindex}                               % 番号 & 題材 & 難易 & 出典
  1 & 二次不等式 & \MMDifficulty{A}{10} & 基本 \\
\end{msindex}
```

`\MSPattern` の番号は講座をまたいで固定する．途中で採番を変えると
過去記事の「型3 で処理する」という参照が壊れる．

---

## 13. 短縮名

**長い名前が正式名，短い名前は別名である．どちらで書いても同じものが組まれる．**
既存の原稿は書き換えなくてよい．

名前の作り方は次のとおりで，これを知っていれば大半は推測できる．

| 部分 | 意味 |
|---|---|
| `MM` / `MK` / `MS` | パッケージの接頭辞．変えない |
| `Com` | コメント（正方形） |
| `Ann` | 注釈（矢印） |
| `A` 接尾 | 意欲的な読者向け．無いほうが全読者向け |
| `Sec` / `Sub` / `Run` | 確認系の節・小節・行頭見出し |

短くしたのは，冗長な語（`Confirmation`，`Magazine`，`Math`／`Make`，
`Contest`，`Pattern`）を含む名前と，繰り返し打つ名前だけである．
もともと短い名前はそのままにしてある．

命令の別名は `\NewCommandCopy` による複製で，引数の形もそのまま受け継ぐ．
環境の別名は，長い環境を開いて閉じるだけの包みとして定義してある
（`\NewEnvironmentCopy` で複製すると，確認系の環境ではパッケージの
読み込みが終わらなくなる）．どちらも組み上がりは正式名と同一である．

### 13.1 `surikumi`

| 短縮名 | 正式名 |
|---|---|
| `\MMSetup` | `\MathMagazineSetup` |
| `\MMTitle` | `\MakeMathMagazineTitle` |
| `\MMCover` | `\MakeMathMagazineCover` |
| `\MMCoverSetup` | `\MathCoverSetup` |
| `\MMMockSetup` | `\MathMockSetup` |
| `\MMMockTitle` | `\MakeMathMockTitle` |
| `\MMContestSetup` | `\MathContestSetup` |
| `\MMAnswerSheet` | `\MakeMathContestAnswerSheet` |
| `\MMInfoSheet` | `\MakeMathContestInfoSheet` |
| `\MMReset` | `\MMConfirmationReset` |
| `\MMSec` | `\MMConfirmationSection` |
| `\MMSub` | `\MMConfirmationSubsection` |
| `\MMRun` | `\MMConfirmationRunInHeading` |
| `\MMCom` | `\MMConfirmationGeneralComment` |
| `\MMComA` | `\MMConfirmationAdvancedComment` |
| `\MMAnn` | `\MMConfirmationGeneralNote` |
| `\MMAnnA` | `\MMConfirmationAdvancedNote` |
| `\MMComMark` | `\MMConfirmationStripedMark` |
| `\MMComAMark` | `\MMConfirmationFilledMark` |
| `\MMAnnMark` | `\MMConfirmationStripedNoteMark` |
| `\MMAnnAMark` | `\MMConfirmationFilledNoteMark` |
| `\MMProofLabel` | `\MMConfirmationProofLabel` |
| `\MMSubhead` | `\MMSubheading` |
| `\MMCase` | `\MMCaseHeading` |
| `\MMAlt` | `\MMAlternative` |
| `\MMLabel` | `\MMBlackLabel` |
| `\MMSolLabel` | `\MMSolutionLabel` |
| `\MMExNum` | `\MMExerciseNumber` |
| `\MMDiff` | `\MMDifficulty` |
| `\MMDiffItem` | `\MMDifficultyItem` |
| `\MMFive` | `\MMFiveMinuteMark` |
| `\MMFormula` | `\MMFormulaBox` |
| `\MMHead` | `\MMRunningHead` |
| `\MMPRule` | `\MMPatternRule` |
| `\MMSwatch` | `\MMPatternSwatch` |
| `\MMAssess` | `\MMContestAssessment` |
| `\MMPostal` | `\MMContestPostalBoxes` |
| `\MMRuled` | `\MMContestRuledLines` |
| `\MMCut` | `\MMContestCutRule` |
| `\MMCell` | `\MMContestCellLabel` |
| `\MMInfoSec` | `\MMContestInfoSection` |

環境．

| 短縮名 | 正式名 |
|---|---|
| `mmcom` | `mmconfirmationgeneralcomment` |
| `mmcoma` | `mmconfirmationadvancedcomment` |
| `mmann` | `mmconfirmationgeneralnote` |
| `mmanna` | `mmconfirmationadvancednote` |
| `mmproof` | `mmconfirmationproof` |
| `mmroman` | `mmconfirmationroman` |
| `mmcontest` | `mmcontestproblem` |

### 13.2 `surikumi-kaisetsu`

| 短縮名 | 正式名 |
|---|---|
| `\MKSetup` | `\MathKaisetsuSetup` |
| `\MKTitle` | `\MKMakeTitle` |
| `\MKReset` | `\MKArticleReset` |
| `\MKEqNum` | `\MKEquationNumbering` |
| `\MKFeat` | `\MKFeatureLabel` |
| `\MKFeatBar` | `\MKFeatureBar` |
| `\MKNote` | `\MKUnmarkedNote` |
| `mkchrono` | `mkchronology` |
| `mkrefs` | `mkreferences` |
| `mkfig` | `mkfigurebody` |
| `mkfull` | `mkfullinsert` |

### 13.3 `surikumi-mondaishu`

| 短縮名 | 正式名 |
|---|---|
| `\MSAnsLabel` | `\MSAnswerStripLabel` |
| `\MSSpread` | `\MSSpreadHeading` |
| `\MSPReset` | `\MSPatternReset` |
| `msans` | `msanswerstrip` |
| `msproc` | `msprocedure` |

### 13.4 短くしていないもの

次は既に十分短いので別名を作っていない．これらは正式名がそのまま
短縮名である．

`\MMHeading` `\MMNote` `\MMSource` `\MMBlank` `\MMLegend` `\MMLead`
`\MMTerm` `\MMRuby` `\MMKenten` `\MMSummary` `\MMCaption` `\MMWideBlock`
`\MMTimeMarks` `\MMMockNumber` `\MMTitleBanner` `\MMMockBanner`
`\MMCoverMainItem` `\MMCoverSubItem` `\MMCoverClearItems`
`\MKSection` `\MKSubsection` `\MKRunIn` `\MKRemark` `\MKCite` `\MKByline`
`\MKMasthead` `\MKName` `\MKChronoItem` `\MKBylineText`
`\MSHint` `\MSAns` `\MSComment` `\MSPattern` `\MSCheckbox` `\MSCheckItem`
`\MSWhereWrong` `\MSHintBreak` `\MSStartVerso`

---

## 14. カウンター

番号を記事の途中から始めるときは，最初にその番号を使う部品より前で
`\setcounter` する．リセット命令（`\MMReset`，`\MKReset`）は
これらを 0 に戻す．

| カウンター | 何の番号 | 親 |
|---|---|---|
| `mmconfirmationsection` | 確認の節 | — |
| `mmconfirmationsubsection` | 確認の小節 | `mmconfirmationsection` |
| `mmexample` | 例題 | — |
| `mmproblem` | 問題 | — |
| `mmfigure` | `\MMCaption` の図 | — |
| `mmtable` | `\MMCaption` の表 | — |
| `mmcontestproblem` | コンテストの出題 | — |
| `mspattern` | `\MSPattern` の型番号 | — |
| `mksection` | 解説記事の節．数式番号の親でもある | — |
| `mksubsection` | 解説記事の小節 | `mksection` |

```latex
\setcounter{mmconfirmationsection}{2}
\setcounter{mmfigure}{2}
```

親を持つカウンターは，親が進むと自動的に 0 へ戻る．

---

## 15. 調整点

紙面の寸法や間隔は，すべて名前の付いたマクロか長さに入れてある．
**原稿側では触らない．** パッケージを改造するときの入口として示す．

| 対象 | どこにあるか |
|---|---|
| 垂直リズム（`\lineskip`，`\abovedisplayskip` ほか） | `surikumi.sty` の `\smag@applyverticalrhythm` と `\smag@applyairyrhythm` |
| 行分割・改ページのペナルティ | 同 `\smag@applybreakpenalties` |
| 和欧間・和文間のアキ | 同 `\smag@kanjiskipvalue`，`\smag@xkanjiskipvalue` |
| 柱の文字列と書式 | 同 `\smag@runningheadverso`，`\smag@runningheadrecto`，`\smag@runningheadtext` |
| 段間罫の高さの測り方 | 同 `\smag@measurecolumn`，`\smag@columnrule` |
| パターンのインク計算 | 同 `\smag@preparepatternink`（`SMpatternInk` を作る） |
| Σ の字形と設置 | 同 `\smag@sumglyph`，`\smag@fixedsum`，`\smag@installfixedsum` |
| 全段幅ブロックの位置決め | 同 `\smag@growviper`（`cuted` への当て木） |
| 解説記事の寸法・文字サイズ | `surikumi-kaisetsu.sty` の第3節（`\mk@*`） |

これらは `@` を名前に含む内部マクロである．書き換えるには
`\makeatletter` が要る．紙面の密度や体裁を変えたいだけなら，
まず[2 章](#2-パッケージオプション)のオプションで足りないか確かめる．

---

## 16. 版面の比較

| 項目 | `surikumi` | `surikumi-kaisetsu` |
|---|---|---|
| 判型 | 182×257mm（JIS B5） | 同左 |
| 天 | 14mm | 12mm |
| 地 | 15mm | 20mm |
| 内・外 | 14mm | 18mm |
| 段間 | 8mm | 8mm（`gutter`） |
| 本文 | 8pt / 10.8pt | 9pt / 14.2pt |
| 1段の行数 | 成り行き（`raggedbottom`） | 45行（`lines`） |
| 段の下端 | そろえない | 既定はそろえない．`flushbottom=true` でそろう |
| 柱 | 下（`runninghead` で上にも） | 奇数ページ内側に誌名，外側にノンブル |

---

## 17. 問題集の型（10案）

詳細は [`problem-set-formats.md`](problem-set-formats.md)．

| 型 | 名称 | 構造 | 主な用途 | 原稿 |
|---|---|---|---|---|
| 1 | 講義一体型 | 例題→解説→類題 | 単元の導入 | `ps01-lecture.tex` |
| 2 | 演習・解説分離型 | 問題一覧→解説を後掲 | 単元の定着 | `ps02-separated.tex` |
| 3 | 見開き対応型 | 左に問題／右に解答 | 短時間の自習 | `ps03-spread.tex` |
| 4 | 段階ヒント型 | 問題→ヒント3段→解答 | 手が止まる層 | `ps04-hints.tex` |
| 5 | 高速ドリル型 | 短問多数＋段末に答えの帯 | 計算の速度 | `ps05-drill.tex` |
| 6 | 誤答分析型 | 誤答→誤りの所在→正答 | 「解けたつもり」を崩す | `ps06-mistakes.tex` |
| 7 | 答案添削型 | 採点基準→答案例→講評 | 記述式の得点化 | `ps07-rubric.tex` |
| 8 | 解法パターン型 | 型番号→手順→適用例 | 解法の語彙づくり | `ps08-patterns.tex` |
| 9 | 難易度別総合演習型 | 一覧→問題→略解 | 分野横断の総復習 | `ps09-graded.tex` |
| 10 | 模試型 | 試験冊子＋自己採点欄 | 到達度の測定 | `ps10-mock.tex` |

型5 と 型10 は単独では成立しない．前者は理由を扱う型と，
後者は採点基準を示す型（型7）と組み合わせる．

---

## 18. 用例とビルド

| ディレクトリ | 内容 | ビルド | 出力先 |
|---|---|---|---|
| `examples/catalog/` | この総目録の紙見本 | `make catalog` | `build/public/catalog/` |
| `examples/magazine/` | 誌面部品の確認（`surikumi-*.tex` の4本のみ） | `make` | `build/public/` |
| `examples/kaisetsu/` | 解説記事の用例 | `make kaisetsu` | `build/public/kaisetsu/` |
| `examples/problem-sets/` | 問題集10型 | `make problem-sets` | `build/public/problem-sets/` |

`make check` は `all`・`problem-sets`・`catalog` を組む．
`make clean` は `build/public/` と `*.ltjruby` を消す．

個別の用例．

| 原稿 | 見どころ | `make` |
|---|---|---|
| `examples/catalog/surikumi-catalog.tex` | 本目録の紙見本．書体，記号，部品，短縮名 | `catalog` |
| `examples/catalog/pattern-catalog.tex` | 背景パターン31種の一覧と濃度・色味・寸法 | `catalog` |
| `examples/catalog/kaisetsu-catalog.tex` | 解説記事の部品見本 | `catalog` |
| `examples/magazine/surikumi-confirmation.tex` | 確認記事の部品一式 | `all` |
| `examples/magazine/surikumi-patterns.tex` | パターン31種を扉の帯へ実寸で敷いた全変種 | `all` |
| `examples/magazine/surikumi-readability.tex` | 圏点，用語，ルビ，リード文，公式囲み，まとめ，柱，段間罫 | `all` |
| `examples/magazine/surikumi-symbol-proof.tex` | 正方形・矢印の作図の確認 | `all` |
| `examples/kaisetsu/kaisetsu-opening.tex` | 号の巻頭記事．中央揃えの扉 | `kaisetsu` |
| `examples/kaisetsu/kaisetsu-feature.tex` | 特集記事．副題，飾り，段抜きの囲み | `kaisetsu` |
| `examples/kaisetsu/kaisetsu-components.tex` | 見出しの4型と2本目の記事 | `kaisetsu` |

表紙一面（`\MakeMathMagazineCover`），模試の扉，コンテストの答案用紙と
応募要項には，用例を同梱していない．いずれも 2 段組の本文に挿し込めない
面丸ごとの部品で，鍵と命令は第8章にある．

---

## 19. 避けることの一覧

紙面全体に関わるもの．

- 特定の商業誌のロゴ，題字，飾り，図案をトレースしない．
- 記事の種類をまたいで見出し・注・数式番号を混ぜない．
  `MM` 系と `MK` 系は別系統である．
- 高密度化のために原稿へ負の `\vspace` や局所的な `\linespread` を書かない．
  密度はパッケージオプションで変える．
- 節見出しの型を段落ごとの気分で変えない．
- 柱，段間罫，和欧間アキ，密度を記事ごとに切り替えない．誌面全体で統一する．
- 原稿側で `\clubpenalty`，`\tolerance`，`\allowdisplaybreaks`，
  `\ltjsetparameter` の字間指定を上書きしない．

記号と書体．

- 正方形をコメント以外（見出し，場合分け，箇条書き，強調）に使わない．
- 斜線入りと黒塗りを装飾上の好みで入れ替えない．対象読者で選ぶ．
- 正方形と矢印を原稿側で描き直さない．
- 三角注記の本文だけを `\small` などで縮小・別書体にしない．
- 場合分けの行だけを太字やゴシック体に切り替えない．
- 本文・答案・場合分け・注記の書体とウェイトと大きさを変えない．
- 強調のために太字，色，下線，四角囲みを重ねない．圏点かゴシックを選ぶ．
- 圏点を長い文や段落全体へ打たない．強調の効果が消える．
- 圏点の記号を記事ごとに差し替えない．誌面で1種類に統一する．

数式．

- 原稿側で `amssymb` と `bm` を読み込まない．
- 別行数式の `\sum` だけを大型字形に切り替えない．
- `\sum` の上端と下端を右肩・右下に置かない．`\sum\nolimits` を使わない．
- 行内式全体へ `\displaystyle` を加えない．
- 別行数式の末尾に句読点を入れない．
- 答・最終結果・途中の主要結果を四角い枠で囲まない．
- `\MMFormulaBox` を答や最終結果の強調に使わない．

背景パターン．

- 1本の記事の中で背景パターンを切り替えない．扉ごとに1種類とする．
- 濃いパターンの上へ白抜きの題字を載せない．`pattern-tone` で薄くする．
- `pattern-accent` を本文の色に使わない．背景の色味だけに使う．
- `\MMPatternRule` を見出しの代わりに使わない．節の区切りだけに使う．

番号と文体．

- 単発または互いに独立した注記へ番号を付けない．
- 答案中の場合分けに `[I]`，`（1）`，「場合1」を使わない．`1°` を使う．
- `1°` に黒四角を付けない．
- 解答・解説で「だ・である調」と「です・ます調」を混在させない．
- 全段幅ブロックを段組の代用として連続して使わない．

---

## 20. 資料の地図

| 資料 | 扱う範囲 |
|---|---|
| [`catalog.md`](catalog.md)（本書） | 何があるかの索引と短縮名 |
| [`surikumi-style-guide.md`](surikumi-style-guide.md) | 紙面の方針と部品の使い分け |
| [`kaisetsu-format.md`](kaisetsu-format.md) | 解説記事の体裁 |
| [`notation-style-guide.md`](notation-style-guide.md) | 数式・記号・句読点の表記 |
| [`problem-set-formats.md`](problem-set-formats.md) | 問題集10型の設計 |
| [`../font-development/sugaku-fourier/README.md`](../font-development/sugaku-fourier/README.md) | 自作 Σ フォントの設計と生成 |
