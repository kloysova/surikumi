# 数理組版ガイド

## 1. 目的

`surikumi.sty` は，日本語数学教材のための独自の高密度組版を提供する．
特定の商業誌，出版社，ロゴ，図案とは関係のない独立したプロジェクトである．

数式・記号・句読点は，必ず先に [`notation-style-guide.md`](notation-style-guide.md) に従う．本書は，その内容を紙面上でどう構成するかを定める．

月刊の学術解説誌の体裁で組む記事には，追加パッケージ `surikumi-kaisetsu.sty` を使う．その部品と規約は [`kaisetsu-format.md`](kaisetsu-format.md) にまとめてある．本書の共通方針は解説記事にも及ぶが，見出し，注，数式番号の形は解説記事のものを使う．

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

講義で使う主な部品は，`mmexample`，`mmproblem`，`mmsolution`，`\MMAlternative`，`\MMNote` である．`\MMNote` は従来どおり行頭に三角を置くが，三角と注記本文は本文と同じ基準文字サイズで組み，注記本文を `\small` などで縮小しない．注記本文の書体とウェイトも本文と同じにする．

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

### 3.4 解説記事

月刊の学術解説誌の体裁で読み物を組む記事には，`surikumi-kaisetsu.sty` を使う．本文 9 pt・行送り 14.2 pt，1 段 45 行の版面に，号の題字，特集の扉，罫を伴う節見出し，`(1.1)` 形式の数式番号，`*1)` 形式の段下の注，年表，参考文献，署名を置く．

```latex
\usepackage{surikumi-kaisetsu}

\MathKaisetsuSetup{title={変分原理の考え方},author={\MKName{数理}{太郎}}}

\MKMakeTitle
\MKArticleReset

\MKSection{停留値としての運動}
本文を置く\footnote{注は段の下に集める．}．
```

解説記事の見出し，注，数式番号は，講義・演習・確認の各形式とは別系統である．一方の部品をもう一方へ持ち込まない．詳しくは [`kaisetsu-format.md`](kaisetsu-format.md) を参照する．

## 4. 数式書体と `\sum`

`surikumi.sty` は本文用の和文・欧文書体を設定する．数式書体の輪郭は，
`\sum` を除いて文書側で選択された書体を尊重する．

既定の本文書体は次のとおりである．

| 用途 | 書体 |
|---|---|
| 和文本文 | Noto Serif CJK JP |
| 和文見出し | Noto Sans CJK JP |
| 欧文本文 | TeX Gyre Termes |
| 欧文見出し | TeX Gyre Heros |
| 数式 | 文書側の標準数式書体 |
| `\sum` | SugakuFourier-Math-Extension（自作） |

本文書体を利用側で全面指定するときは，次のように既定指定を止める．この指定だけで数式書体は変わらない．

```latex
\usepackage[fonts=false]{surikumi}
```

### 4.1 Σ の書体

`\sum` の字形は，既定でプロジェクト自作の
`SugakuFourier-Math-Extension` から取る．設計の意図は
[`font-development/sugaku-fourier/README.md`](../font-development/sugaku-fourier/README.md)
を参照する．差し替わるのは Σ だけであり，積分，総乗，根号，
可変寸法の括弧は文書側の数式書体のまま変わらない．

文書側の数式書体の Σ に戻す場合は次のように指定する．

```latex
\usepackage[sigma=document]{surikumi}
```

自作フォントはプロジェクト内の `texmf/` にある．
`config/.latexmkrc` とルートの `Makefile` が検索パスへ加えるため，
通常のビルド手順では追加設定は要らない．検索パスを通さずに組んだ場合は，
警告を出したうえで文書側の Σ へ自動的に戻る．

数式全体を Fourier 系へそろえたい文書では，従来どおり
`sugaku-fouriernc` を併用してよい．両者は競合しない．

### 4.2 Σ の大きさと上下限

雑誌組版の `\sum` は，行内式と `\[...\]` などの別行数式で同じ `textstyle` 用小型 Σ を使う．別行数式だからといって，大型字形へ切り替えない．

```latex
和 $S_n=\sum_{k=1}^{n}a_k$ を考える．

\[
  S_n=\sum_{k=1}^{n}a_k
\]
```

上の二つでは，Σ 本体の大きさが等しくなる．和の上端と下端は，どちらも Σ の真上と真下へ置く．右肩・右下へ置く形式は使用しない．`surikumi.sty` が通常の `\sum` に字形と上下配置を自動適用するため，原稿側で `\textstyle` や `\limits` を繰り返す必要はない．`\sum\nolimits` は使用しない．

`\MMCompactSum{下限}{上限}` は既存ソースとの互換性のために残すが，新規原稿では通常の `\sum` を使う．`\scriptstyle` で式全体を縮小したり，Σ，上限，下限を疑似スタックとして手作業で重ねたりしてはならない．

### 4.3 コンパクト垂直リズム

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
| 解説記事 | 記事の扉 | `\MKMakeTitle` |
| 解説記事 | 節と小見出し | `\MKSection`，`\MKSubsection` |
| 解説記事 | 段下の注 | `\footnote` |
| 解説記事 | 参考文献と署名 | `mkreferences`，`\MKByline` |

解説記事の部品は `surikumi-kaisetsu.sty` にあり，一覧は [`kaisetsu-format.md`](kaisetsu-format.md) にまとめている．

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
- 解説記事の見出し，注，数式番号を，講義・演習・確認の記事へ持ち込まない．逆も同じである．
