# Transforming Data into Features
# You are a data scientist at a clothing company and are working with a data set of customer reviews. This dataset is originally from Kaggle and has a lot of potential for various machine learning purposes. You are tasked with transforming some of these features to make the data more useful for analysis. To do this, you will have time to practice the following:
#
# Transforming categorical data
# Scaling your data
# Working with date-time features

# Преобразование данных в признаки
# Вы специалист по данным в швейной компании и работаете с набором данных отзывов клиентов.
# Этот набор данных изначально взят из Kaggle и имеет большой потенциал для различных целей машинного обучения.
# Вам поручено преобразовать некоторые из этих признаков, чтобы сделать данные более полезными для анализа.
# Для этого у вас будет время попрактиковаться в следующем:
# Преобразование категориальных данных
# Масштабирование данных
# Работа с признаками даты и времени

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# import data
reviews = pd.read_csv('reviews.csv')

# print column names/info
print(reviews.columns)
print(reviews.info())
# look at the counts of recommended
print(reviews['recommended'].value_counts())

# create binary dictionary
binary_dict = {True: 1, False: 0}

# transform column
reviews['recommended'] = reviews['recommended'].map(binary_dict)

# print your transformed column
print(reviews['recommended'].value_counts())

# look at the counts of rating
print(reviews['rating'].value_counts())

# create dictionary
rating_dict = {'Loved it': 5, 'Liked it': 4, 'Was okay': 3, 'Not great': 2, 'Hated it': 1}

# transform rating column
reviews['rating'] = reviews['rating'].map(rating_dict)

# print your transformed column values
print(reviews['rating'].value_counts())

# get the number of categories in a feature
print(reviews['department_name'].value_counts())

# perform get_dummies
one_hot = pd.get_dummies(reviews['department_name'])

# join the new columns back onto the original
reviews = reviews.join(one_hot)

# print column names
print(reviews.columns)

# transform review_date to date-time data
reviews['review_date'] = pd.to_datetime(reviews['review_date'])

# print review_date data type
print(reviews['review_date'].dtype)

# get numerical columns
reviews = reviews[['clothing_id', 'age', 'recommended', 'rating', 'Bottoms', 'Dresses', 'Intimate', 'Jackets', 'Tops',
                   'Trend']].copy()

# reset index
reviews = reviews.set_index('clothing_id')

# instantiate standard scaler
scaler = StandardScaler()
scaler.fit_transform(reviews)


