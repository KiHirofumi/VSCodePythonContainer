from sys import argv
# exists は引数として渡した名前のファイルが存在すればTrueを返し、なければFalseを返す
from os.path import exists

script, from_file, to_file =argv

print(f"{from_file}から{to_file}へコピーします。")

in_data = open(from_file, 'rb').read()

print(f"入力ファイルの大きさは{len(in_data)}バイトです。")

print(f'出力ファイルは存在しますか？　{exists(to_file)}')
print("準備ができました。続行するにはEnterキーを押下してください。")
print("中断するためには ctrl + c を押下してください。")
input()

out_file = open(to_file, 'wb')
out_file.write(in_data)

print("すべて完了しました。")

out_file.close()
