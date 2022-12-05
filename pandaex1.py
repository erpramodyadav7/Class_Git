import pandas as pd
import csv
data = pd.read_csv("Automobile_data.csv")
# print(data.info()) #total 61 entries
# # Exercise 1: From the given dataset print the first and last five rows
print(data.head())
print(data.tail())
# # Clean the/ dataset and update the CSV file Replace all column values which contain ?, n.a, or NaN./
df1=data.dropna()
print(df1.head())
# print(df1.info()) #total 58entires
# print(df1.describe())
# Exercise 3: Find the most expensive car company name Print most expensive cars company name and price.
# df2=df1[["company","price"]][df1.price==df1['price'].max()]
# print(df2)
# print(df2.head())
# maxprice_car = df2.max(axis = 0)
# # maxprice_car= df2.groupby("company")["price"].max() #gives copany wise max price
# print(maxprice_car)
# Exercise 4: Print All Toyota Cars details
# toyota_cars= df1[(data["company"]=="toyota")]
# print(toyota_cars)
# Exercise 5: Count total cars per company
# car_per_company= df2.groupby("company").count()
# print(car_per_company)
# Exercise 6: Find each companyâ€™s Higesht price car
# companywise_highst = df2.groupby("company").max()
# print(companywise_highst)
# Exercise 7: Find the average mileage of each car making company
# df3=df1[["company","average-mileage"]]
# milege_company= df3.groupby("company").max("average-mileage")
# print(milege_company)
# Exercise 8: Sort all cars by Price column
# sorting_byprice= df1.sort_values(by=['price'], ascending=False)
# sorting_byprice= df1.sort_values(by=['price'])
# print(sorting_byprice)
# Exercise 9: Concatenate two data frames
# GermanCars = pd.DataFrame({'Company': ['Ford', 'Mercedes', 'BMV', 'Audi'],
#               'Price': [23845, 171995, 135925 , 71400]},)
# japaneseCars = pd.DataFrame({'Company': ['Toyota', 'Honda', 'Nissan', 'Mitsubishi'],
#                 'Price': [29995, 23600, 61500 , 58900]},)
#
# frames = [GermanCars , japaneseCars]
# result = pd.concat(frames)
# print(result)
# Exercise 10: Merge two data frames
# Car_Price = pd.DataFrame({'Company': ['Toyota', 'Honda', 'BMV', 'Audi'],
#                           'Price':[23845, 17995, 135925 , 71400]},)
# car_Horsepower = pd.DataFrame({'Company': ['Toyota', 'Honda', 'BMV', 'Audi'],
#                                'horsepower': [141, 80, 182 , 160]},)
# result=pd.merge(Car_Price,car_Horsepower)
# print(result)