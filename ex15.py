from sys import argv
# 引数（argv）を開きたいファイル名として定義する。
scrirpt, filename = argv
# 引数のファイル名を開く（仮想的に）
txt = open(filename)

print(f"{filename}の内容は次の通りです。：")
# 開いたファイルを読み込んで（read()）、出力する
print(txt.read())

print("もう一度ファイル名を入力しましょう。：")
file_again = input("> ")
# プロンプトから入力した文字をファイル名として開く
txt_again = open(file_again)

print(txt_again.read())