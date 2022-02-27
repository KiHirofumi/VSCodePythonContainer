# 定数
# cars:所持している車の数
# space_in_car:車に乗せられる人の数
# drivers:雇用している運転手さんの数
# passengers:乗客
cars =100
space_in_car=4.0
drivers = 30
passengers = 90

# 稼働していない車の数
cars_not_driven = cars - drivers
# 稼働している車の数
cars_driven = drivers
# 運べる人の数
carpool_capacity = cars_driven * space_in_car
# 車に収容する人の数
average_passengers_per_car = passengers / cars_driven

print("今日は", cars, "台の車が利用可能。")
print("今日は", drivers, "人しかドライバーがいない。")
print("だから", cars_not_driven, "台の車にはドライバーがいない。")
print("今日は", carpool_capacity, "人の乗客を運べる。")
print("今日は", passengers, "人の乗客がいる。")
print("一台の車に", average_passengers_per_car, "人を乗せる必要がある。")
