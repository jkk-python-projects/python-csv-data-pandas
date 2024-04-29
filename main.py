# import pandas
# import csv


# with open("weather_data.csv") as weather_file:
#     data = weather_file.readlines()
#
# print(data)

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1].strip("'")))
#     print(temperatures)

# data = pandas.read_csv("weather_data.csv")
# data_dict = data.to_dict()
#
# print(data_dict)
#
# temp_list = data["temp"].to_list()
#
# print(temp_list)
#
# average = sum(temp_list) / len(temp_list)
# print(average)
# print(data["temp"].max())
#
# print(data.condition)

# print(data[data.day == "Monday"])
#
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
#
# monday_temp = monday.temp[0]


# def fahrenheit(x):
#     x = x * 1.8 + 32
#     return x
#
#
# print(fahrenheit(monday_temp))

import pandas
import csv

squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

c = squirrel_data["Primary Fur Color"].value_counts().to_csv()
print(c)

squirrel_data["Primary Fur Color"].value_counts().to_csv("squirrel_count.csv")


#squirrel_list = squirrel_data["Primary Fur Color"].to_list()
#print(squirrel_list)
# number_gray = squirrel_data["Primary Fur Color"].value_counts()["Gray"]
# number_cinnamon = squirrel_data["Primary Fur Color"].value_counts()["Cinnamon"]
# number_black = squirrel_data["Primary Fur Color"].value_counts()["Black"]
#
# print(number_gray)
# print(number_cinnamon)
# print(number_black)