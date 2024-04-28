import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from pyArango.connection import Connection

# Установка соединения с базой данных
conn = Connection(username="root", password="")  # замените на ваши учетные данные
db = conn["ProjectDB"]  # замените на имя вашей базы данных
articles = db["Articles"]  # замените на имя вашей коллекции
# Считываем содержимое файлов
# with open('data/articles.txt', 'r', encoding='utf-8') as file:
#     articles_data = file.read()
query = 'FOR doc IN Articles RETURN { Tags: doc.Tags, Article: doc.Article }'
cursor = db.AQLQuery(query, rawResults=True)

articles = []
current_article = {'text': '', 'tags': []}

for data in cursor:
    article_text = data['Article']
    tags = data['Tags']
    
    current_article['text'] = article_text
    current_article['tags'] = tags
    
    # Добавляем скопированный словарь current_article в список статей articles
    articles.append(current_article.copy())

# Проверка, что данные загружены
print(articles)

with open('data/tags.txt', 'r', encoding='utf-8') as file:
    tags_data = file.read().split(', ')

# Запрос пользователя на ввод нового текста статьи
new_article_text = input('Введите текст новой статьи:\n')

# Создаем TF-IDF матрицу для статей и новой статьи
corpus = [article['text'] for article in articles]
corpus.append(new_article_text)

tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(corpus)

# Вычисляем косинусное сходство между TF-IDF векторами
similarity_scores = cosine_similarity(tfidf_matrix[:-1], tfidf_matrix[-1])

# Находим индекс статьи с наибольшим сходством
most_similar_article_idx = similarity_scores.argmax()

# Выводим наиболее подходящий тег для новой статьи
most_similar_tags = articles[most_similar_article_idx]['tags']
print('Наиболее подходящие теги для новой статьи:', ', '.join(most_similar_tags))