# -*- coding: utf-8 -*-

import time

import numpy as np
from sklearn import metrics
from sklearn.cluster import Birch, KMeans, MiniBatchKMeans


def k_means_demo():
    X = np.array([[1, 2], [1, 4], [1, 0], [4, 2], [4, 4], [4, 0]])

    k_means = KMeans(n_clusters=2, random_state=0).fit(X)
    result = k_means.predict([[0, 0], [4, 4]])

    print(result)

# 用户对电影的评分x
# 用户对未来电影的评分y


# user_id | item_id | rating | timetamp
# 读取电影评分数据
file = open("../tmp/dataset/ml-100k/u1.base")
X_array = []
y_array = []

for line in file.readlines():
    ls = line.strip().split('\t')
    time_local = time.localtime(int(ls[2]))
    # print(time.strftime("%Y-%m-%d %H:%M:%S", time_local))
    y_array.append(int(ls[2]))
    X_array.append([int(ls[0]), int(ls[1]), int(ls[3])])

k_means = KMeans(n_clusters=5, random_state=1).fit(X_array)
mini_k_means = MiniBatchKMeans(
    n_clusters=5, random_state=1).fit(X_array)
birch = Birch(branching_factor=50, n_clusters=5,
              threshold=0.5, compute_labels=True).fit(X_array)


y_predict = k_means.predict(X_array)
y_mini_predict = mini_k_means.predict(X_array)
y_birch_predict = birch.predict(X_array)

for y in y_predict:
    y += 1

for y in y_mini_predict:
    y += 1

for y in y_birch_predict:
    y += 1

print("Score in trainset: ")
print("Metrics for KMeans is: ", metrics.adjusted_rand_score(y_predict, y_array))
print("Metrics for MiniBatchKMeans is: ",
      metrics.adjusted_rand_score(y_mini_predict, y_array))
print("Metrics for Birch is: ", metrics.adjusted_rand_score(
    y_birch_predict, y_array))

u1_test = open("../tmp/dataset/ml-100k/u1.test")

X_test = []
y_test = []

for line in u1_test.readlines():
    ls = line.strip().split('\t')
    y_test.append(int(ls[2]))
    X_test.append([int(ls[0]), int(ls[1]), int(ls[3])])

y_predict = k_means.predict(X_test)
y_mini_predict = mini_k_means.predict(X_test)
y_birch_predict = birch.predict(X_test)

for y in y_predict:
    y += 1

for y in y_mini_predict:
    y += 1

for y in y_birch_predict:
    y += 1

print("Score in testset: ")
print("Metrics for KMeans is: ", metrics.adjusted_rand_score(y_predict, y_test))
print("Metrics for MiniBatchKMeans is: ",
      metrics.adjusted_rand_score(y_mini_predict, y_test))
print("Metrics for Birch is: ", metrics.adjusted_rand_score(
    y_birch_predict, y_test))
