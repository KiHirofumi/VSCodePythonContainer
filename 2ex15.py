# argvを使用するための宣言
from sys import argv
# scriptとfilenameを使う。filenameにはargv（引数）を入れる
# あれ、scriptってなんだ？どこでも使ってないぞ。
# そうだ。scriptにはこのファイル名が入ってくるんだ。
script, filename = argv
# txtにfilenameで指定したものをオープンして入れる
txt = open(filename)
# 引数のファイルを表示するにはprint(hoge.read())でオープンしたのを読ませる
print(f"{filename}の内容は次の通り：")
print(txt.read())

print("もう一度ファイル名を入力しよう：")
file_again = input(">")

txt_again = open(file_again)

print(txt_again.read())
