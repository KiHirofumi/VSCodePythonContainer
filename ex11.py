print("君の年齢は?", end=' ')
age = input()
print("君の身長は？", end=' ')
height =input()
print("君の体重は？", end=' ')
weight = input()

print(f"君は{age}歳で、身長は{height}cmで、体重は{weight}kgですね。")

# 個人エクササイズ
print("BMIの計算をしますか？ y or n", end=' ')
question = input()

if question == 'y':
    BMI = float(weight) / ((float(height) * 0.01) * (float(height) * 0.01))
    print(f"君のBMIは{BMI}です。")
