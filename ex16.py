from sys import argv

script, filename = argv

print(f"これから{filename}を消去する。")
print("消去したくなければ ctrl ＋ c を入力し、")
print("消去してもいいなら Enter を入力してください。")

input("? ")

print("では、ファイルを開きます...")
target = open(filename, 'w')

print("ファイルを切り捨てます。グッバイ！")
target.truncate()

print("3行分の内容を入力します。")

line1 = input("1行目：")
line2 = input("2行目：")
line3 = input("3行目：")

print("これらをファイルに書き込みます。")

target.write(line1)
target.write("\n")
target.write(line2 + "\n" + line3 + "\n")
print("最後にファイルを閉じます。")
target.close()

######## 書き込まれた内容を表示してあげる。 #########
print(".....\n書き込まれました！")
print("以下の通りとなります")
print(f"ファイル名：{filename}")

print(open(filename).read())
##################################################