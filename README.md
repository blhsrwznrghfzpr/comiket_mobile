# Comiket Mobile
これは[Enjoy TRPG in コミケ!! コミックマーケットTRPGジャンル参加者への非公式支援サイト](http://comiket-trpg.sakura.ne.jp/)にて作成されている、TRPGサークル頒布物一覧をhtml形式に変換するスクリプトです。

### 必要環境
* Python3.6.0

※作者が使用してる環境しか確認はしてません。(おそらくPython3系なら動くと思われます。)

### 使い方
1. [Enjoy TRPG in コミケ!! コミックマーケットTRPGジャンル参加者への非公式支援サイト](http://comiket-trpg.sakura.ne.jp/)にて、変換したいスプレッドシートをダウンロードします。
2. スプレッドシートの「ファイル」＞「形式を指定してダウンロード」＞「タブ区切りの値（.tsv、現在のシート）」を選択してdataフォルダにダウンロード
3. comiket_mobile.pyをエディタで開いて、以下の値を修正
```
data_tsv: ダウンロードしたtsvファイル
outputfile: 出力するファイル名
page_title: 出力したページのタイトル
homepage_url: PCサイトのURL
```
4. comiket_mobile.pyを実行
5. 「正常に動作しました」と表示されたら成功
6. (Optional)出力テンプレートを変更したい場合は'data/template/template.html'を変更してください

### 生成されたHTMLページを見るために必要なもの
[jQuery](https://jquery.com/)と[tablesorter](https://github.com/christianbach/tablesorter)

HTMLのheadタグ内で読み込んでるので、いい感じに指定して使ってください。

初期のフォルダ構成は以下のとおりです（表示に必要なもののみ記述）
```
├ css/
│  ├ common.css
│  └ themes/blue/... (tablesorterのテーマ)
├ js/
│  ├ common.js
│  ├ jquery.tablesorter.min.js
│  └ jquery-3.1.0.min.js
└ cXXtable_mobile.html  (生成されるHTML)
```
