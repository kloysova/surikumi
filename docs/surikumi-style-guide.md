# 数理組版ガイド

## 1. 目的

`surikumi.sty` は，日本語数学教材のための独自の高密度組版を提供する．
特定の商業誌，出版社，ロゴ，図案とは関係のない独立したプロジェクトである．

数式・記号・句読点は，必ず先に [`notation-style-guide.md`](notation-style-guide.md) に従う．本書は，その内容を紙面上でどう構成するかを定める．

## 2. 共通する紙面方針

- JIS B5 判，縦長，2 段組を基本とする．
- 本文は明朝体，見出しは太めのゴシック体を基本とする．
- 本文は 8 pt，行送り 10.8 pt を既定とする．`density=compact` の垂直リズムにより，本文行送り，別行数式の前後，`align` の行間を連動して詰める．背の高い行では最低行間が安全弁として働くため，字面を接触させない．
- 本文中の解説，答案，場合分け，注記は，本文と同じ明朝体・通常ウェイト・同じ文字サイズで組む．見出し，ラベル，図中文字など，役割上の区別が必要な要素だけを例外とする．
- 行送りを個別指定するときは `bodyleading` オプションを使い，本文中で局所的な `\linespread` を重ねない．従来相当のゆとりへ戻す場合は `density=standard,bodyleading=12pt` を指定する．
- 長い式変形は等号を縦に揃え，説明文と数式を無理に同じ行へ詰め込まない．
- 記事扉のパターンは TeX で生成した独自図形を使い，参考紙面の図案を複製しない．
- 見出し，列挙，注記，証明表示は，記事の種類に合わせて選ぶ．全記事を一つの型へ統一しない．

## 3. 記事の種類

### 3.1 講義

講義では，例題や問題を入口にして解説を進める従来の形式を使う．十進見出し，ローマ数字の公式列挙，斜線入り注記，`[証明]` を自動的に加えない．

```latex
\MakeMathMagazineTitle

導入文を置く．

\begin{mmexample}[1.1]{等差数列と二次方程式}
  ...
\end{mmexample}

解説本文を置く．

\MMAlternative{漸化式から見る}
別解の本文を置く．

\MMNote{解法上の注意を短く補う．}
```

講義で使う主な部品は，`mmexample`，`mmproblem`，`mmsolution`，`\MMAlternative`，`\MMNote` である．`\MMNote` は従来どおり行頭に右向きの三角を置くが，三角と注記本文は本文と同じ基準文字サイズで組み，注記本文を `\small` などで縮小しない．注記本文の書体とウェイトも本文と同じにする．

### 3.2 ベーシック演習

ベーシック演習では，番号付き問題一覧と出典，続く解説ページという従来の形式を使う．「確認」用の十進見出しや `(i)` 列挙は必須ではない．

```latex
\begin{mmproblems}
  \item 問題文を置く．
  \MMSource{26 ○○大・理}
\end{mmproblems}

\MMHeading{解\qquad 説}

\begin{mmproblems}
  \item 解説を置く．
\end{mmproblems}
```

### 3.3 確認系の記事

公式や要点を短く整理する「確認」系の記事に限り，次の部品を選んで使える．

- `1.`，`1.1.` 形式の見出し
- `(i)`，`(ii)`，`(iii)` 形式の列挙
- 斜線入り正方形による全読者向けコメント
- 黒塗り正方形による意欲的な読者向けコメント
- 斜線入りの「矢印＋注」による全読者向け注釈
- 黒塗りの「矢印＋注」による意欲的な読者向け注釈
- `[証明]` 表示
- 行頭の太字見出し

これらは「確認」系のための選択部品であり，他の記事へ自動適用しない．

```latex
\MakeMathMagazineTitle
\MMConfirmationReset

\MMConfirmationSection{基本的な数列}
\MMConfirmationSubsection{等差数列}

\begin{mmconfirmationroman}
  \item $a_{n+1}-a_n=d$
  \item $a_n=a_1+(n-1)d$
\end{mmconfirmationroman}

\MMConfirmationGeneralComment{和から一般項を求めた後は，$n=1$ を確認する．}

\begin{mmconfirmationproof}
$n=1$ のとき命題は成り立つ．
\end{mmconfirmationproof}
```

正方形は「コメント」だけを意味する．見出し，場合分け，箇条書きなどの
装飾には使わない．斜線入り正方形は，すべての読者が読むコメントを表す．
黒塗り正方形は，発展的内容など，意欲的な読者向けのコメントを表す．
見た目だけで選ばず，対象読者によって使い分ける．どちらも，四角の
幾何学的中心をコメント本文の第1行の字面中央に揃える．正方形は本文1字
より一回り小さくし，本文より強く見せない．

```latex
\MMConfirmationGeneralComment{添字の上端と下端を先に確認する．}

\MMConfirmationAdvancedComment{同じ考え方を重み付きの和へ応用できる．}
```

複数段落や別行数式を含むコメントには，対象読者に応じて
`mmconfirmationgeneralcomment` または `mmconfirmationadvancedcomment`
を使う．

```latex
\begin{mmconfirmationgeneralcomment}
差を取ると中間項が消える．
\[
  \sum_{k=1}^{n}(b_{k+1}-b_k)=b_{n+1}-b_1
\]
\end{mmconfirmationgeneralcomment}
```

「矢印＋注」は注釈を意味する．正方形と同じ読者区分を使い，斜線入りは
すべての読者向け，黒塗りは意欲的な読者向けとする．矢印は本文1字程度の
高さに収め，軸を細くして，注釈本文より強く見せない．

確認系の正方形と矢印は，必ず `surikumi.sty` の共通記号描画部品を
使う．斜線は記号自身のローカル座標に固定した同一の角度，間隔，線幅，
開始位置で描き，出現位置によって位相を変えない．黒塗り版と斜線版も
同一の輪郭寸法，外周線，基準位置を共有する．原稿側で Unicode 記号，
罫線文字，TikZ の汎用パターンなどを用いて類似記号を作り足さない．

```latex
\MMConfirmationGeneralNote{$r=1$ の場合は別に確認する．}

\MMConfirmationAdvancedNote{母関数を用いる見方もある．}
```

複数段落や別行数式を含む注釈には，`mmconfirmationgeneralnote` または
`mmconfirmationadvancednote` を使う．`\MMConfirmationNote` と
`mmconfirmationnote` は斜線入りの全読者向け注釈を意味する互換名である．
正方形の互換環境 `mmconfirmationcomment` は，斜線入りの全読者向け
コメントを意味する．新規執筆では，対象読者と用途が名前から分かる
明示的な命令を使う．

#### 注記番号

番号は，同じ局所的な説明の中で，関連する注記が一つの系列として連続する場合だけ付ける．単発の注記には番号を付けない．見出し，話題，例題などの境界を越えて番号を持ち越さず，新しい系列は `1` から始める．離れた独立注記を誌面全体の通し番号にしてはならない．

```latex
\MMConfirmationGeneralNote[1]{$S_n-S_{n-1}$ を計算する．}
\MMConfirmationGeneralNote[2]{$n=1$ は別に確認する．}
```

上のように，番号付き注記は同じ系列で続けて用いる．次のような単発番号は使わない．

```latex
% 不可：続く注記系列がない
\MMConfirmationGeneralNote[1]{$n=1$ を確認する．}
```

行頭の型名には，`\MMConfirmationRunInHeading` を使う．

```latex
\MMConfirmationRunInHeading{等比型}
$a_{n+1}=ra_n$ のとき，$a_n=r^{n-1}a_1$ である．
```

記事の途中番号から始めるときは，最初の見出しより前でカウンターを設定する．

```latex
\setcounter{mmconfirmationsection}{2}
\MMConfirmationSection{数学的帰納法}
```

番号を付けない見出しには，星付き形式を使う．

```latex
\MMConfirmationSection*{補足}
\MMConfirmationSubsection*{別の見方}
```

### 3.4 記事の種類を選ばない部品

強調（圏点，用語のゴシック，ルビ），リード文，公式囲み，まとめ，図表
キャプション，一時的な全段幅ブロックは，記事の種類によらず同じ意味で使う．
第 11 章にまとめてある．行分割と改ページの調整も同様で，既定で全記事に効く．

紙面全体の設計にかかわるもの——柱，段間罫，和欧間アキ，本文の密度——は
パッケージオプションで決め，記事ごとに切り替えない．

## 4. 数式書体と `\sum`

`surikumi.sty` は本文用の和文・欧文書体に加え，それらと調和する数式書体を設定する．

既定の書体は次のとおりである．

| 用途 | 書体 |
|---|---|
| 和文本文 | Noto Serif CJK JP |
| 和文見出し | Noto Sans CJK JP |
| 欧文本文 | TeX Gyre Termes |
| 欧文見出し | TeX Gyre Heros |
| 数式 | TeX Gyre Termes Math |

和文は Noto CJK JP を優先する．同じ設計は Noto Serif JP／Noto Sans JP という
別名の可変フォントでも配布されており，こちらはウェイトごとの名前を持たない．
そのため名前でウェイトを指定しても選べず，従来はファミリ全体が jlreq の既定
書体へ落ちていた．現在は可変フォントしか無い環境ではウェイト軸（`wght`）で
本文 400，太字 700，題字 900，著者名 600 を指定し，同等の太さを得る．
どちらの名前も見つからない場合は jlreq の既定書体を使う．

数式書体は欧文本文と同じ Termes 系である．これを指定しないと，欧文本文が
Termes であるのに数式だけ Latin Modern になり，同じ行の中で字面と太さが
食い違う．Σ をはじめとする数式記号も本文となじまない．

本文書体を利用側で全面指定するときは，次のように既定指定を止める．
`fonts` は和文・欧文の本文書体だけを制御し，数式書体は `mathfont` が
独立して制御する．本文書体を差し替えても数式は Termes 系のままにできる．

```latex
\usepackage[fonts=false]{surikumi}
```

数式書体を文書側で選ぶ，あるいは従来どおり LaTeX の既定に任せるときは，
次のようにする．

```latex
% 別の OpenType 数式書体を使う
\usepackage[mathfontname={STIX Two Math}]{surikumi}

% 数式書体を設定させない（Latin Modern に戻る）
\usepackage[mathfont=false]{surikumi}
```

`unicode-math` または指定した数式書体が見つからない場合は，警告を出した
うえで数式書体を設定せずに処理を続ける．

### 4.1 数式書体にともなう約束

数式書体の適用には `unicode-math` を用いる．これに関して，原稿側で守る
ことが二つある．

- **`amssymb` と `bm` を読み込まない．** どちらも旧来の記号フォントを
  登録し，そうなると `\sum` の上下限が行内式で Σ の右肩・右下へ戻って
  しまう．`unicode-math` が本パッケージと本ガイドで使う記号をすべて
  提供するため，追加の読み込みは不要である．読み込まれた場合は警告する．
- **ベクトルは従来どおり `\bm` でよい．** `unicode-math` 環境では
  `\bm` は `\symbf` の別名として定義される．`bold-style=ISO` を指定して
  あるため，`\bm{v}` も `\bm{\omega}` も太字斜体になる．
  `\symbf` を直接書いてもよい．

`amssymb` 由来の名前のうち，`unicode-math` が定義しない `\square` と
`\blacksquare` はパッケージ側で補っている．

雑誌組版の `\sum` は，行内式と `\[...\]` などの別行数式で同じ `textstyle` 用小型 Σ を使う．別行数式だからといって，大型字形へ切り替えない．

```latex
和 $S_n=\sum_{k=1}^{n}a_k$ を考える．

\[
  S_n=\sum_{k=1}^{n}a_k
\]
```

上の二つでは，Σ 本体の大きさが等しくなる．和の上端と下端は，どちらも Σ の真上と真下へ置く．右肩・右下へ置く形式は使用しない．`surikumi.sty` が通常の `\sum` に字形と上下配置を自動適用するため，原稿側で `\textstyle` や `\limits` を繰り返す必要はない．`\sum\nolimits` は使用しない．

`\MMCompactSum{下限}{上限}` は既存ソースとの互換性のために残すが，新規原稿では通常の `\sum` を使う．`\scriptstyle` で式全体を縮小したり，Σ，上限，下限を疑似スタックとして手作業で重ねたりしてはならない．

### 4.2 コンパクト垂直リズム

既定の `density=compact` は，単なる行送り変更ではなく，次を一括して制御する．

- 本文の基準行送り
- 通常の別行数式と短い別行数式の前後
- `align`，`align*` などの各行へ加える間隔
- 背の高い行が隣の行へ接触しないための最低行間

したがって，原稿側で負の `\vspace`，局所的な `\linespread`，
`\abovedisplayskip` の上書きを重ねない．紙面全体の密度を変えるときは，
パッケージオプションだけを変更する．

```latex
% 既定：高密度
\usepackage[density=compact]{surikumi}

% 従来相当のゆとり
\usepackage[density=standard,bodyleading=12pt]{surikumi}
```

## 5. 数式の置き方

- 本文中の短い式は行内に置く．
- 公式，結論，2 段以上の変形は別行にする．
- 連続する変形は `align*` で等号を揃える．
- 行内式を `\displaystyle` で一律に拡大しない．
- 行内式と別行数式で，Σ 本体の大きさを変えない．
- `\sum` の上下限は，行内式でも必ず Σ の真上と真下に置く．
- 別行数式の末尾に句読点を入れない．句読点は数式の前後の本文に置く．
- 分数，積，微分，ベクトルなどの書き方は `notation-style-guide.md` を優先する．

```latex
和 $S_n=\sum_{k=1}^{n}a_k$ を考える．

したがって，
\begin{align*}
  \sum_{k=1}^{n}(b_{k+1}-b_k)
    &= (b_2-b_1)+\cdots+(b_{n+1}-b_n) \\
    &= b_{n+1}-b_1
\end{align*}
である．
```

## 6. 解答の文体と場合分け

解答，解説および答案例は「だ・である調」で統一する．同じ解答の中で
「です・ます調」を混在させない．

答案中で場合分けをするときは，`1°`，`2°`，`3°`，…を使う．
問題の小問番号と場合分けの番号は別物であり，小問 `(1)` の解答中でも，
場合分けは `1°` から始める．`[I]`，`[II]` や `（1）`，`（2）` を
場合分けの記号として使わない．`1°` 自体を見出し記号とするため，
黒四角を併記しない．通常の `\MMSubheading` ではなく，
`\MMCaseHeading` を使う．この命令は改段落と余白だけを整え，
文字は本文と同じ明朝体・通常ウェイト・同じ大きさで組む．
太字やゴシック体へ切り替えない．

```latex
\MMCaseHeading{1}{$x\geq0$ のとき}
本文を「だ・である調」で書く．

\MMCaseHeading{2}{$x<0$ のとき}
本文を「だ・である調」で書く．
```

答，最終結果および途中の主要結果は四角い枠で囲まない．
`\boxed`，`\fbox`，`\framebox` を強調目的で用いず，「答」などの解答ラベルと
通常の別行数式によって示す．問題欄や解説見出しなど，紙面構造を示す枠とは
区別する．

## 7. 部品の使い分け

| 記事 | 内容 | 使用する部品 |
|---|---|---|
| 講義 | 例題 | `mmexample` |
| 講義 | 問題 | `mmproblem` |
| 講義 | 解答 | `mmsolution` |
| 講義 | 別解 | `\MMAlternative` |
| 講義 | 短い注記 | `\MMNote` |
| すべて | 本文書体のまま組む場合分け | `\MMCaseHeading` |
| ベーシック演習 | 問題・解説一覧 | `mmproblems` |
| ベーシック演習 | 出典 | `\MMSource` |
| ベーシック演習 | 解説見出し | `\MMHeading` |
| 確認 | 大きな節 | `\MMConfirmationSection` |
| 確認 | 節内の小項目 | `\MMConfirmationSubsection` |
| 確認 | 行頭の型名 | `\MMConfirmationRunInHeading` |
| 確認 | 公式や証明手順 | `mmconfirmationroman` |
| 確認 | 全読者向けの短いコメント | `\MMConfirmationGeneralComment` |
| 確認 | 意欲的な読者向けの短いコメント | `\MMConfirmationAdvancedComment` |
| 確認 | 全読者向けの長いコメント | `mmconfirmationgeneralcomment` |
| 確認 | 意欲的な読者向けの長いコメント | `mmconfirmationadvancedcomment` |
| 確認 | 全読者向けの短い「矢印＋注」 | `\MMConfirmationGeneralNote` |
| 確認 | 意欲的な読者向けの短い「矢印＋注」 | `\MMConfirmationAdvancedNote` |
| 確認 | 全読者向けの長い「矢印＋注」 | `mmconfirmationgeneralnote` |
| 確認 | 意欲的な読者向けの長い「矢印＋注」 | `mmconfirmationadvancednote` |
| 確認 | 証明 | `mmconfirmationproof` |

次の部品は記事の種類を選ばない．どの記事でも同じ意味で使う．

| 内容 | 使用する部品 |
|---|---|
| 文中の一時的な強調 | `\MMKenten`（記号は `\MMKentenMark`） |
| 用語の初出 | `\MMTerm` |
| 読みにくい術語の読み | `\MMRuby` |
| 節冒頭のリード文 | `\MMLead` |
| 公式の提示 | `\MMFormulaBox` ／ `mmformulabox` |
| 節末のまとめ | `\MMSummary` ／ `mmsummary` |
| 図表のキャプション | `\MMCaption`（名前は `\MMFigureName` ／ `\MMTableName`） |
| 一時的に全段幅を使う | `mmwideblock` ／ `\MMWideBlock` |
| 節の区切りの帯，行中の見本 | `\MMPatternRule` ／ `\MMPatternSwatch` |
| 柱の上書き | `\MMRunningHead` |

## 8. 避けること

- 特定の商業誌のロゴ，図案，飾り文字をトレースしない．
- 講義やベーシック演習を，「確認」系の十進見出しや注記へ一律に変更しない．
- 正方形をコメント以外の見出し，場合分け，箇条書きなどに使わない．
- 斜線入りと黒塗りの正方形または「矢印＋注」を，装飾上の好みで入れ替えない．
- 正方形と矢印を原稿側で描き直し，斜線の角度，間隔，線幅，開始位置をばらつかせない．
- 単発または互いに独立した注記へ番号を付けない．
- 解答・解説で「だ・である調」と「です・ます調」を混在させない．
- 答案中の場合分けに `[I]`，`（1）`，「場合1」を使わない．
- `1°`，`2°` の場合分け見出しに黒四角を付けない．
- 場合分けの行だけを太字やゴシック体へ切り替えない．
- 答，最終結果および途中の主要結果を四角い枠で囲まない．
- 三角注記の本文だけを `\small` などで縮小したり，別書体へ切り替えたりしない．
- 高密度化のために，原稿中へ負の `\vspace` や局所的な `\linespread` を追加しない．
- 行内式全体へ `\displaystyle` を加え，行送りを不必要に広げない．
- 別行数式の `\sum` だけを大型字形へ切り替えない．
- `\sum` の上端と下端を右肩・右下へ置かない．
- 1 段の中へ長すぎる式を押し込まない．必要なら式を分けるか，一時的に全段幅を使う．
- 強調のために本文の書体，ウェイト，文字サイズを変えない．圏点，用語のゴシック，ルビから選ぶ（§10.4）．
- 圏点の記号（`\MMKentenMark`）を記事ごとに差し替えない．誌面で 1 種類に統一する．
- 全段幅ブロックを段組の代用として連続して使わない．前後へ `\vspace` を足して位置を調整しない．
- 柱，段間罫，和欧間アキ，密度を記事ごとに切り替えない．誌面全体で統一する．

## 9. 背景パターン

### 9.1 三つの系統

記事扉のバナーに敷く背景パターンは，`\MathMagazineSetup` の `pattern` キーで
選ぶ．名前はすべて小文字ローマ字である．現在 31 種あり，出自で三つに分かれる．

| 系統 | 種類数 | 名前 |
|---|---|---|
| 幾何（既存） | 12 | `scales` `triangles` `diamonds` `chevrons` `weave` `hexagons` `pinwheels` `zigzags` `checker` `parquet` `origami` `ribbons` |
| 和柄 | 10 | `asanoha` `seigaiha` `shippou` `kikkou` `sayagata` `kagome` `yagasuri` `tatewaku` `mitsukuzushi` `ajiro` |
| 数学的モチーフ | 9 | `truchet` `isocubes` `sierpinski` `lattice` `moire` `envelopes` `girih` `packing` `spirals` |

いずれも公有の意匠を pgf のパスで独自に作図したものである．参考紙面の図案を
複製しない，という第 1 章の方針は変わらない．

薄いものから濃いものへ並べると，数学的モチーフはおよそ
`lattice` ＜ `sierpinski` ＜ `envelopes` ＜ `truchet` ＜ `spirals` ＜
`packing` ＜ `girih` ＜ `moire` ＜ `isocubes` の順になる．
和柄では線画の 6 種（`asanoha` `seigaiha` `shippou` `kikkou` `sayagata`
`kagome`）が薄く，面塗りの 4 種（`yagasuri` `tatewaku` `mitsukuzushi`
`ajiro`）が濃い．白抜きの題字（`title-fill=white`）を載せるときは，薄い側か
`pattern-tone=pale` / `light` を合わせる．

### 9.2 濃度・色味・寸法

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

`pattern-tone=normal` は従来の見え方をそのまま再現する．題字が読みにくいとき
だけ `pale` か `light` へ落とす．`strong` は白ベールを外すので，題字を載せない
帯にだけ使う．

`pattern-scale` は数学的モチーフの 9 種にだけ効く．幾何 12 種と和柄 10 種は
タイル寸法が宣言時に固定されるため，指定しても黙って無視される（誤りではない）．

`pattern-accent` と `pattern-tone` は，PDF の uncolored pattern に外側から
インクを与える仕組みで実装している．和柄 10 種は inherently coloured
pattern として宣言してあり，タイル内部の階調（`SMrule` / `SMpale` /
`SMpatternA` / `SMpatternB`）をそのまま出力へ残すため，`pattern-tone` と
`pattern-accent` のうちインク色の指定は効かない．白ベールだけが効く．

### 9.3 バナー以外の部品

| 命令 | 用途 |
|---|---|
| `\MMPatternRule[高さ]` | 節の区切りに使う細い帯 |
| `\MMPatternSwatch[高さ]{幅}` | 行中に置く見本 |

どちらも `\MathMagazineSetup` で選んだパターンと濃度をそのまま使う．小さな
見本では `pattern-scale` を 1 未満にして，図柄が 1 単位分収まるようにする．

### 9.4 避けること

- 1 本の記事の中で背景パターンを切り替えない．扉ごとに 1 種類とする．
- 濃いパターンの上へ白抜きの題字を載せない．`pattern-tone` で薄くする．
- `pattern-accent` を本文の色に使わない．背景の色味だけに使う．
- `\MMPatternRule` を見出しの代わりに使わない．節の区切りだけに使う．

## 10. 可読性のための工夫

本文 8 pt，行送り 10.8 pt，JIS B5 判 2 段組という条件では，紙面の密度そのものよりも，行分割，改ページ，字間，強調の扱いが読みやすさを決める．この章の部品は，密度を落とさずにそれらを整えるためのものである．

### 10.1 既定で有効になっている調整

次の調整は `penalties` オプションで一括して制御し，既定は `true` である．紙面の見た目を変えるのではなく，狭い段で起きる組版上の欠陥を防ぐためのものなので，通常は有効のまま使う．

- 段の末尾に段落の第 1 行だけが残ること（`\clubpenalty`），段の先頭に段落の最終行だけが置かれること（`\widowpenalty`，`\displaywidowpenalty`）を禁じる．`\raggedbottom` が有効なので，段が 1 行短くなるだけで済む．
- 分割された語の後半だけを次の段の先頭へ送らない（`\brokenpenalty`）．
- 狭い段の行分割に余裕を持たせ，最後の手段として `\emergencystretch` を使う（`\tolerance`，`\emergencystretch`）．
- 行内の長い式を関係記号や二項演算子のあとで折り返せるようにする（`\relpenalty`，`\binoppenalty`）．
- 複数行の別行数式が段をまたげるようにする（`\allowdisplaybreaks[1]`）．段の下端に大きな空きが生まれにくくなる．

```latex
% 上をすべて止める場合だけ指定する
\usepackage[penalties=false]{surikumi}
```

原稿側で `\clubpenalty` や `\allowdisplaybreaks` を重ねて指定しない．紙面全体の方針はパッケージオプションで決める．

### 10.2 見た目を変えるオプション

次のオプションはすべて既定 `false` である．記事や誌面の設計として選んだときだけ指定する．

| オプション | 既定 | 内容 |
|---|---|---|
| `runninghead` | false | 2 ページ目以降に柱を出す |
| `columnrule` | false | 段間に細い罫を引く |
| `interspacing` | false | 和欧間・和文間のアキを調整する |

`runninghead` を指定すると，記事の扉以外のページに柱が出る．柱の内容は `\MathMagazineSetup` の `series`（左ページ）と `title`（右ページ）を自動的に使う．長すぎるときだけ `\MMRunningHead` で上書きする．

```latex
\usepackage[runninghead]{surikumi}

\MMRunningHead{数列の確認}          % 左右とも同じ文字列
\MMRunningHead[要点の整理]{数列の確認}  % 左ページ／右ページ
```

`columnrule` は，段と段の間に 0.25 pt の細い罫を `SMrule` の色で引く．罫の長さは，左右の段のうち長いほうの内容の高さに合わせる．したがって記事の最終ページのように段が短いページでは罫も短くなり，本文の無いところへ垂れ下がらない．全段幅ブロック（§10.7）の上では，罫はブロックまで届く．なお，段を版面いっぱいへ伸ばす LaTeX 標準の `\flushbottom` を使う文書では，罫も版面の高さいっぱいに引かれる．

`interspacing` は，和文と欧文・行内数式の間のアキを 0.22 倍角に固定し，伸縮を控えめにする．8 pt の本文では，このアキがないと行内式が本文に埋もれる．既定を変えないのは，既刊の紙面の行分割が変わるためである．

### 10.3 第三の密度

`density` には既存の `compact`，`standard` に加えて `airy` を指定できる．長時間読ませる記事のための版で，行送り，別行数式の前後，`align` の行間をまとめて開く．`compact` と `standard` の値は変わらない．

```latex
% 既定：高密度
\usepackage[density=compact]{surikumi}

% 従来相当のゆとり
\usepackage[density=standard,bodyleading=12pt]{surikumi}

% 読者が疲れにくい版
\usepackage[density=airy,interspacing]{surikumi}
```

`density=airy` は，`bodyleading` を指定していない場合にかぎり，行送りを 12.2 pt へ広げる．`bodyleading` を明示したときは，その値をそのまま使う．

### 10.4 強調

和文の強調は，書体・ウェイト・文字サイズを変えない方法を優先する．

| 用途 | 部品 |
|---|---|
| 文中の一時的な強調 | `\MMKenten` |
| 用語の初出 | `\MMTerm` |
| 読みにくい術語の読み | `\MMRuby` |

```latex
和の上端と下端は\MMKenten{必ず}確認する．
\MMTerm{階差数列}を $b_n=a_{n+1}-a_n$ とおく．
\MMRuby{漸化式}{ぜんかしき}を立てる．
\MMRuby{階|差|数|列}{かい|さ|すう|れつ}のように語ごとに区切れる．
```

圏点は本文の書体のまま強調できるので，本文中の強調にはまずこれを使う．圏点の記号は本文 1 字より小さい丸とし，正方形は使わない．正方形は確認系のコメントだけを意味するという規約を，強調のために崩さない．

圏点の記号は `\MMKentenMark` に入っており，誌面全体の方針として差し替えられる．既定は本文 1 字より小さい丸である．胡麻点にするときは，プリアンブルで次のように書き換える．記事ごとに切り替えず，誌面で 1 種類に統一する．正方形など，確認系の記号と紛らわしい形は使わない．

```latex
\renewcommand{\MMKentenMark}{﹅}
```

`\MMTerm` は用語の初出だけに使い，同じ用語を繰り返しゴシックにしない．太字を重ねない．

圏点は，通常の本文では行送りを変えない．圏点の丸は親文字の上端で終わり，行間の余りに収まる寸法に調整してある．前の行が極端に深いときだけ，衝突を避けるために行間が開く．

ルビは，その行の行間を 1.5 pt 程度押し広げる．高密度の紙面では目立つので，読みの必要な語だけに使い，同じ語に繰り返し付けない．

### 10.5 リード文，公式，まとめ

| 用途 | 部品 |
|---|---|
| 節冒頭のリード文 | `\MMLead` |
| 公式の提示 | `\MMFormulaBox` / `mmformulabox` |
| 節末のまとめ | `\MMSummary` / `mmsummary` |

```latex
\MMConfirmationSection{和の公式}

\MMLead{和の公式は，上端と下端の確認から始める．}

\MMFormulaBox{%
  \[
    \sum_{k=1}^{n}k=\dfrac{n(n+1)}{2}
  \]}

\MMSummary{使える $n$ の範囲を必ず確かめる．}
```

**公式の提示と答の強調は別物である．** 第 6 章の規約は変わらない．答，最終結果および途中の主要結果は四角い枠で囲まない．`\MMFormulaBox` は閉じた四角ではなく，左の太い罫と淡い地色と「公式」ラベルで構成する．答を示すときは，`\MMFormulaBox` ではなく解答ラベルと通常の別行数式を使う．

`\MMSummary` は上下の罫だけで囲む．どちらもラベルを差し替えられる．

```latex
\MMFormulaBox[要点]{...}
\MMSummary[この節のまとめ]{...}
```

`\MMLead` は本文と同じ書体・大きさで組み，細い罫線と字下げだけで区別する．見出しの代わりに使わない．

### 10.6 図表キャプション

```latex
\MMCaption{等差数列の項は等間隔に並ぶ}   % 図1，図2，…
\MMCaption[table]{よく使う和の公式}      % 表1，表2，…
\MMCaption*{番号を付けないキャプション}
```

図と表は別々に番号が付く．`\label` を続ければ相互参照でき，`\ref` は「図3」のように種別ごと出力する．ラベル名は `\MMFigureName`，`\MMTableName` で変更できる．

図のキャプションは図の下に，表のキャプションは表の上に置く．

番号のカウンターは図が `mmfigure`，表が `mmtable` である．§3.3 の `mmconfirmationsection` と同じ扱いで，記事の途中番号から始めるときだけ，最初のキャプションより前で設定する．

```latex
\setcounter{mmfigure}{2}
\setcounter{mmtable}{1}
```

### 10.7 一時的に全段幅を使う

1 段に収まらない式は，まず式を分ける．それでも収まらないときだけ全段幅へ逃がす．

```latex
\begin{mmwideblock}
  \[
    \sum_{k=1}^{n}k(k+1)(k+2)(k+3)=\dfrac{n(n+1)(n+2)(n+3)(n+4)}{5}
  \]
\end{mmwideblock}
```

短いものには `\MMWideBlock{...}` を使ってもよい．1 段組の記事では，通常の別行ブロックとして組まれる．全段幅ブロックは記事あたり数か所までとし，本文の流れを細かく分断しない．

全段幅ブロックは，そのページで先に組まれた両方の段の下に置かれる．原稿では 1 段の途中にあっても，刷り上がりでは左段・右段がそこで打ち切られ，ブロックはその下へ回る．したがって次の点に注意する．

- ブロックの直前の材料が両段へ均等に割れないとき，片方の段の下端に空きが残る．これは `\raggedbottom` の下では正常な結果であり，負の `\vspace` で詰めない．空きが大きすぎるときは，ブロックの位置を段落の切れ目へ移す．
- ブロックの前後のアキは `\stripsep` で本文の行送りから決まる．原稿側で `\vspace` を足さない．
- 段の高さがそろわない位置に置いても，本文と重なって刷られることはない．重なりが見えたら組版側の不具合として報告する．

### 10.8 この章で避けること

- 強調のために太字，色，下線，四角囲みを重ねない．圏点かゴシックのどちらかを選ぶ．
- 圏点を長い文や段落全体へ打たない．強調の効果が消える．
- `\MMFormulaBox` を答や最終結果の強調に使わない．
- 柱と段間罫を記事ごとに切り替えない．誌面全体で統一する．
- 原稿側で `\clubpenalty`，`\tolerance`，`\allowdisplaybreaks`，`\ltjsetparameter` の字間指定を上書きしない．
- 全段幅ブロックを段組の代用として連続して使わない．
