import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Создаем случайные данные для кластеризации
np.random.seed(0)
X = np.random.rand(100, 2) * 10

# Применяем алгоритм K-means с 3 кластерами
kmeans = KMeans(n_clusters=3, random_state=0).fit(X)
labels = kmeans.labels_
centroids = kmeans.cluster_centers_

# Метки для каждого кластера
d = ['Драма', 'Комедия', 'Романтика']

# Визуализируем результаты кластеризации
plt.figure(figsize=(8, 6))

# Отобразим данные, закрашенные по кластерам
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', marker='o', edgecolor='k', s=50)

# Отобразим центроиды кластеров
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', marker='x', s=200, label='Самые популярные жанры')

# Добавим подписи к центроидам
for i, txt in enumerate(d):
    plt.text(centroids[i, 0], centroids[i, 1] + 0.3, txt, fontsize=12, ha='center')

plt.legend()
plt.xlabel('Тексты')
plt.ylabel('Жанры')
plt.title('K-Means Кластеризация текстов по жанрам')
plt.grid(True)
plt.show()