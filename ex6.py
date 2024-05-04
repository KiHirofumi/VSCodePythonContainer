types_of_people =10
x = f"世の中には{types_of_people}種類の人間がいる。"

binary = "バイナリ"
do_not = "そうでない"
y = f"{binary}を知っている人と、{do_not}人だ。"

print(x)
print(y)

print(f"私は言った：{x}")
print(f'こうとも言った："{y}"')

hilarious = False
joke_evaluation = "このジョークは面白かったかな？！{}"

print(joke_evaluation.format(hilarious))
# これやっちゃうとエラー
# print(joke_evaluation.format(y))
# こっちはまだOK
# print(joke_evaluation)

w = "これは左側のテキストで．．．"
e = "これは右側のテキストです。"

print(w + e)