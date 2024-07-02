# python-pdf

pythonのインストール
https://www.python.org/ftp/python/3.12.4/python-3.12.4-amd64.exe

各種ライブラリのインストールが必要
コマンドプロンプトを右クリック管理者メニューで開き、以下を実行

```
C:\Python312\python.exe -m pip install --upgrade pip
```

以下のコマンドを実行
```
pip install PyPDF2
pip install pdfplumber
pip install reportlab

```

importPyPDF2.pyをコピーしてドキュメントフォルダに配置する。
その後、コマンドプロンプトで以下のコマンドをたたく
```
cd Documents
```
ドキュメントの中にファイルを分割したいpdfを配置する。
ファイル名をinput.pdfに名前変更する。
その後以下のコマンドプロンプトで以下のコマンドを実行する

```
python importPyPDF2.py
```
output_pagesフォルダにPDFファイルが配置される。
