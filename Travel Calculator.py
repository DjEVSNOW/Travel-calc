#Узнаем у пользователя данные.
price_of_flight = int(input('Введите стоимость перелета\n'))
price_of_food = int(input('Введите среднюю стоимость ежедневного питания\n'))
hotel_cost = int(input("Стоимость отеля за ночь\n"))
num_of_days = int(input('Введите количество дней пребывания\n'))
#Движок
hotel_price = int(num_of_days-1)*hotel_cost
sum_of_all_prices = int((num_of_days*price_of_food)+(hotel_price+price_of_flight*2))
print("Итого: ",sum_of_all_prices, "у.е")
