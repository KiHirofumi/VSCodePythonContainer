from cmd import PROMPT
from sys import argv

script, user_name = argv
PROMPT = '> '

print(f"やぁ、{user_name}。私は{script}スクリプトです。")
print("私は君にいくつかの質問をしたいと思います。")
print(f"{user_name}、君は私のことが好きですか？")
likes = input(PROMPT)

print(f"{user_name}ｍ君はどこに住んでいますか？")
lives = input(PROMPT)

print("君はどんな種類のコンピュータを持っていますか？")
computer = input(PROMPT)

print(f"""
いいね。私のことを好きですかと聞いたら、{user_name}は「{likes}」と言った。
{user_name}は{lives}に住んでいる。わたしはわからないけどね。
それに、{user_name}は{computer}コンピュータを持っている。すごいね。
""")