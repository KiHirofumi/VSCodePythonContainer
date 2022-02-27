from ast import arg
from sys import argv

# このコードを実行する方法は？
# このままデバッグ実行するとエラーとなる。
# 通常の実行であれば引数として３つ渡せばいいのだが、デバッグには設定ファイルが必要
script, first, second, third = argv

print("このスクリプトの名前は：", script)
print("first変数の値は：", first)
print("second変数の値は：", second)
print("third変数の値は：", third)