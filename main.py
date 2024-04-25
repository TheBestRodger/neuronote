from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import MultiLabelBinarizer

# Считывание статьи из файла
with open('data/article1.txt', 'r', encoding='utf-8') as file:
    article = file.read()

# Считывание тегов из файла
with open('data/tags.txt', 'r', encoding='utf-8') as file:
    tags = file.readlines()
tags = [tag.strip() for tag in tags]  # Убираем лишние пробелы и символы переноса строки

# Вывод статьи и соответствующих тегов
print('Статья:')
print(article)
print('Теги:')
print(tags)