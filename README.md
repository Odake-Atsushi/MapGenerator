# RosMapGenerator
rosのmapをつくるプログラム

## PDF非対応
対応：Windows

Releasesに実行ファイルがあるので，実行してください．
GIMP等を用いて，PDFファイルは画像ファイルに変換してください．（PNG，JPEG等）

## PDF対応
対応：Windows，Linux，Mac

アナコンダが導入されていない場合，https://docs.conda.io/en/latest/miniconda.html
を参考にしてminicondaを入れる．

https://www.python.jp/install/anaconda/windows/install.html
ここも参考にして，コマンドライン環境の設定も行う．アナコンダのインストールでは無い．

仮想環境構築
``` PowerShell
conda env create --file MG_env.yaml
```

環境を起動
``` PowerShell
conda activate MapGenerator
```

プログラムは，`src`の中に格納されている．
``` PowerShell
python プログラムのパス
```

これで起動できるはず．
