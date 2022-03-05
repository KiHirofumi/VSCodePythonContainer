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

# ここからinputを使った練習
a = input("+ or - ：")
if a == "+":
    ans = int(first) + int(second) + int(third)
    print(f"{first} + {second} + {third} = {ans}")
elif a == "-":
    ans = int(first) - int(second) - int(third)
    print(f"{first} - {second} - {third} = {ans}")
else:
    print("+ か - を入力してね。それ以外だったのでおわります。")