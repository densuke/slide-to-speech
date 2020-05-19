# これなに?

GSuiteのスプレッドシートにノートテキストを入れておく。
これをスライドと一緒にデータとして吐き出しておく。

これらを使って、スライドを合成音声付きの動画に変換させるというものです。
要はオンライン授業の時に事前資料として見せたりする目的だけど、自分のダミ声は出したくないという方向けです。

# 必要なもの

- Python3
- GCPのアカウントとプロジェクト
- ffmpegまわり(ffmpeg, ffprobe)
- 怪しいものを使う勇気
- くじけぬ心
- [プレモルを送る財力](https://amzn.to/2Zt1mtJ)があるとうれしいです

# とりあえずの使い方

## 事前設定

1. このリポジトリをクローンしてください
2. [Google上のチュートリアル](https://cloud.google.com/text-to-speech/docs/quickstart-client-libraries?hl=ja)を見て、サービスアカウント用のキーファイル(JSON)を取得しておきます
3. 必要になるライブラリを `pip` で入れてください。
4. 環境変数 `GOOGLE_APPLICATION_CREDENTIALS` に、キーファイル(JSON)へのパスを渡しておいてください
5. 動画化したいスライドのスクリプトとして、Driveにダウンロードするコードをセットして実行します。[設定方法(投げやり)はブログに上げました](https://blog.fuga.jp/?p=4898)。

# 使い方

1. スライドに渡したスクリプトを実行し、スライドをPDFにしたものと各スライドのノートを抽出したファイルを、フォルダごとダウンロードします
2. ソースコードのディレクトリ上に、フォルダを展開します

```

$ cd slide-to-speech # clone済み
$ unzip ~/arhive.zip 
$ cd archive
$ ../make-movie

```

たぶんこれでできるかと。
なおテキストはSSMLとして認識しています。

# Copyright

Copyright: SATO Daisuke <densuke@fuga.jp>
配布ライセンスはGPL3とします

