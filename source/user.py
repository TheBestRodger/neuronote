from pyArango.connection import Connection
from pyArango.collection import Collection, Field
from brain import GenerateMarks
from brain import GenerateAnnotation
from ArangoConnection import make_conn_to_db

db = make_conn_to_db()

def show_article_data(Name):
    query = f'FOR doc IN {Name} RETURN doc'
    cursor = db.AQLQuery(query, rawResults=True)
    i = 0
    for data in cursor:
        Title = data['Название']
        Marks = data['Метки']
        Anotation = data['Аннотация']
        print(f"Данные номер: {i}")
        print(f"Название: {Title}")
        print(f"Жанры: {Marks}")
        print(Anotation, "\n")
        i += 1
        if(i == 5):
            print("Too much")
            break

def Iadd_new_data():
    Title = input('Название:\n')
    Marks = GenerateMarks(Title)
    print(f"Автоматические сгенерированые жанры: {Marks}")
    Anotation = GenerateAnnotation(Title)
    print(f"Автоматические сгенерированые жанры: {Anotation}")

    new_data = {
        "Название": Title,
        "Метки":Marks,
        "Аннотация":Anotation
    }
    if not db.hasCollection("UsersData"):
        col = db.createcollection(name = "UsersData")
    col = db["UsersData"]
    doc = col.createDocument()
    doc.set(new_data)
    doc.save()
    #doc = col.add_document(new_data)
    print(f"Новый документ успешно добавлен с ID: {doc['_id']}")

def Iremove_data_byMarks():
    if not db.hasCollection("UsersData"):
        print("Fatal error collection didn t find")
    col = db["UsersData"]
    gener_to_remove = input('Жанр: ')

    query = f'FOR doc IN `{col.name}` FILTER "{gener_to_remove}" IN doc.`Метки` REMOVE doc IN `{col.name}`'
    doc_to_remove = db.AQLQuery(query, rawResults=True)
    #doc_to_remove = col.fetchByExample({"Метк": "Порода: бешеная дворовая"}, batchSize = 100)
    print(f"Удалено {len(doc_to_remove)} документов с меткой '{gener_to_remove}'")
def Iremove_data_byTitle():
    if not db.hasCollection("UsersData"):
        print("Fatal error collection didn t find")
    col = db["UsersData"]
    title_to_remove = input('Название: ')

    query = f'FOR doc IN `{col.name}` FILTER doc.`Название` == "{title_to_remove}" REMOVE doc IN `{col.name}`'
    doc_to_remove = db.AQLQuery(query, rawResults=True)
    #doc_to_remove = col.fetchByExample({"Метк": "Порода: бешеная дворовая"}, batchSize = 100)
    print(f"Документ с названием '{title_to_remove}' удален")