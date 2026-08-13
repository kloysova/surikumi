# Sugaku Fourier

`SugakuFourier-Math-Extension` は，Fourier-GUTenberg の
`Fourier-Math-Extension` を基礎にした，このプロジェクト専用の派生
Type 1 数式拡張フォントである．

現在のリリースは v1.0 である．

## 設計範囲

- Fourier の文字幅，TeX 数式メトリクス，文字コードを維持する．
- 小型和記号 `summationtext`（文字コード 80）を独自輪郭へ置き換える．
- 大型和記号 `summationdisplay`（文字コード 88）を同じ造形原理で置き換える．
- その他の記号は Fourier の派生フォントとして維持する．
- 派生元で検査境界値にあった `BlueScale` を安全側へ補正する．

独自の Σ は，Fourier の軽快な字面を残しながら，高さに対する横幅を
約 1.1 倍に広げ，横棒を短く太くし，右端に縦方向の量感を持たせ，
中央斜線の黒みを増している．中央の折れには小さな曲線を入れ，印刷時に
角が尖りすぎないようにした．文字幅を含む TeX メトリクスも輪郭に
合わせて更新している．参考写真の輪郭はトレースしていない．

## 生成

TeX Live の `fourier-mex.pfb`，`fourier-mex.afm`，
`fourier-mex.tfm` と `t1utils` が必要である．

```sh
make -C font-development/sugaku-fourier
```

生成物はプロジェクトの `texmf/` 以下へ置かれる．
`config/.latexmkrc` はこのプロジェクト内 TeX tree を検索対象へ加える．

## 使用

```latex
\usepackage{sugaku-fouriernc}
```

このパッケージは `fouriernc` を読み，`largesymbols` ファミリーだけを
`SugakuFourier-Math-Extension` へ切り替える．`\sum` 以外の大型記号は
元の Fourier 派生字形を保つ．LuaLaTeX，pdfLaTeX，および
pLaTeX＋dvipdfmxでmapファイルを読み込む．

## 校正用PDF

- `sugaku-fourier-proof.tex`：FourierNC標準字形との並列比較．
- `sugaku-fourier-ptex-proof.tex`：pLaTeX＋dvipdfmxでの確認．

紙面へ組み込んだ状態は，プロジェクト直下で `make` して得られる
`build/public/surikumi-symbol-proof.pdf` で確認する．

生成した Type 1 フォントは `t1lint` で検査し，LuaLaTeX と
pLaTeX＋dvipdfmxの両方でPDFへの埋込みを確認する．

## ライセンス

基礎とした Fourier-GUTenberg および fouriernc は LPPL で配布されて
いる．派生ファイルは原ファイルと異なる名称を持ち，LPPL 1.3c の条件に
従う．完全なライセンス本文は `LICENSE-LPPL-1.3c.txt` に収録する．
