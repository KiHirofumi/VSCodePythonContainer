my_name = 'Ki.Hirofumi'
my_age = 36
my_height = 178 # cm
my_weight = 64 # kg
my_eyes = '黒'
my_hair = '黒'
my_teeth = '白色'

print(f"{my_name}についてお話します。")
print(f"彼の身長は{my_height}センチメートル。")
print(f"彼の体重は{my_weight}kg。")
print("実際のところ、そんなに太ってはいない。")
print(f"彼の眼の色は{my_eyes}で、紙の色は{my_hair}です。")
print(f"彼の歯はたいてい{my_teeth}ですが、それはコーヒーとタバコ次第です。")

# この行は不思議に思えるかもしれないが、とにかく試してみよう。
total = my_age + my_height + my_weight
print(f"{my_age}と{my_height}と{my_weight}を足すと{total}です。")

BMI = my_weight / ((my_height * 0.01 ) * (my_height * 0.01))
print(f"BMIは{BMI} になります。")