from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from ArangoConnection import GetCursorToCollectionFromDB
def Annotation():
    cursor = GetCursorToCollectionFromDB()
    current_article = {}
    articles = []
    for data in cursor:
        article_text = data['Аннотация']
        annot = data['Метки']
        
        current_article['text'] = article_text
        current_article['tags'] = annot
        
        # Добавляем скопированный словарь current_article в список статей articles
        articles.append(current_article.copy())
    return articles
def Marks():
    cursor = GetCursorToCollectionFromDB()
    current_article = {}
    articles = []
    for data in cursor:
        article_text = data['Название']
        tags = data['Метки']
        
        current_article['text'] = article_text
        current_article['tags'] = tags
        
        # Добавляем скопированный словарь current_article в список статей articles
        articles.append(current_article.copy())
    return articles
def Title():
    cursor = GetCursorToCollectionFromDB()
    current_article = {}
    articles = []
    for data in cursor:
        article_text = data['Annotation']
        tags = data['Метки']
        
        current_article['text'] = article_text
        current_article['tags'] = tags
        
        # Добавляем скопированный словарь current_article в список статей articles
        articles.append(current_article.copy())
    return articles
def GenerateAnnotation(new_article_text): 
    articles = Annotation()
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
    most_similar_tags = articles[most_similar_article_idx]['text']
    return most_similar_tags
def GenerateTitle(new_article_text): 
    articles = Marks()
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
    most_similar_tags = articles[most_similar_article_idx]['text']
    return most_similar_tags
def GenerateMarks(new_article_text): 
    articles = Marks()
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
    return most_similar_tags
    #print('Наиболее подходящие теги для новой статьи:', ', '.join(most_similar_tags))
