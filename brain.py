import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Считываем содержимое файлов
with open('data/articles.txt', 'r', encoding='utf-8') as file:
    articles_data = file.read()

with open('data/tags.txt', 'r', encoding='utf-8') as file:
    tags_data = file.read().split(', ')

# Создаем структуру данных для хранения статей и их тегов
articles = []
current_article = None

for line in articles_data.split('\n'):
    if line.startswith('Article:'):
        current_article = {'text': '', 'tags': []}
        articles.append(current_article)
    elif current_article:
        if line.startswith('Tags:'):
            tags = line.replace('Tags:', '').strip().split(', ')
            current_article['tags'] = tags
        else:
            current_article['text'] += line

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