formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("一", "二", "三", "四"))
print(formatter.format(True, False, True, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "好きな文章を",
    "ここに書いてみましょう。",
    "例えば詩や",
    "歌なんかもよいでしょう。"
))
# print(formatter.format(1,2))
# これだとIndexErrorで怒られる。
# 例外が発生しました: IndexError
# Replacement index 2 out of range for positional args tuple
