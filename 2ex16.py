from sys import argv

script, filename = argv

print(f"これから{filename}を消去する。")
print("消去したくないならCtrl -cを入力し、")
print("消去しても良いならEnterキーを入力する。")

input("?")

print("ではファイルを開こう。。。")
target = open(filename, 'w')

print("ファイルを切り捨てる。グッバイ！")
target.truncate()

print("3行分の内容を入力する。")

line1 = input("line1:")
line2 = input("line2:")
line3 = input("line3:")

print("これらをファイルに書き込みます。")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
### ここから追加 ###
# これはうまく働かなかった
print(open(filename).read())
### ここまで ###
print("最後にファイルを閉じます。")
target.close()
# ここで再度オープンするとはたらいた。セーブされていないからだと思う
print(f"書き込まれた文言は書きです{open(filename).read()}")