# from pyArango.connection import Connection
# from pyArango.collection import Collection, Field
from brain import GenerateMarks
from brain import GenerateAnnotation
from ArangoConnection import make_conn_to_db

db = make_conn_to_db()
def check_collection(name = "UsersData"):
    if not db.hasCollection(name):
        print("Fatal error collection didn t find")
    col = db[name]
    return col
def Ishow_All_article_data(Name = "UsersData"):
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
        if(i == 10):
            print("Show more&")
            break
def find_byTitle():
    title = input('Название:\n')
    query = f'FOR doc IN `UsersData` RETURN doc'
    cursor = db.AQLQuery(query, rawResults=True)
    document = next((doc for doc in cursor if doc["Название"] == title), None)
    # print("Название:")
    # print(document["Название"])
    print("Жанры:")
    print(document["Метки"])
    print("Аннотация:")
    print(document["Аннотация"])
def Iadd_new_data():
    Title = input('Название:\n')
    Marks = GenerateMarks(Title)
    print(f"Автоматические сгенерированые жанры: {Marks}")
    Anotation = GenerateAnnotation(Title)
    print(f"Автоматические сгенерированая аннотация: {Anotation}")

    new_data = {
        "Название": Title,
        "Метки":Marks,
        "Аннотация":Anotation
    }
    col = check_collection()
    doc = col.createDocument()
    doc.set(new_data)
    doc.save()
    #doc = col.add_document(new_data)
    print(f"Новый документ успешно добавлен с ID: {doc['_id']}")

def Iremove_data_byMarks():
    col = check_collection()
    gener_to_remove = input('Жанр: ')

    query = f'FOR doc IN `{col.name}` FILTER "{gener_to_remove}" IN doc.`Метки` REMOVE doc IN `{col.name}`'
    doc_to_remove = db.AQLQuery(query, rawResults=True)
    #doc_to_remove = col.fetchByExample({"Метк": "Порода: бешеная дворовая"}, batchSize = 100)
    print(f"Удалено {len(doc_to_remove)} документов с меткой '{gener_to_remove}'")
def Iremove_data_byTitle(): 
    col = check_collection()
    title_to_remove = input('Название: ')

    query = f'FOR doc IN `{col.name}` FILTER doc.`Название` == "{title_to_remove}" REMOVE doc IN `{col.name}`'
    doc_to_remove = db.AQLQuery(query, rawResults=True)
    #doc_to_remove = col.fetchByExample({"Метк": "Порода: бешеная дворовая"}, batchSize = 100)
    print(f"Документ с названием '{title_to_remove}' удален")
def remove_data_byTitle(name): 
    col = check_collection()
    title_to_remove = name

    query = f'FOR doc IN `{col.name}` FILTER doc.`Название` == "{title_to_remove}" REMOVE doc IN `{col.name}`'
    db.AQLQuery(query, rawResults=True)
def Iupdate_data_byTitle():
    col = check_collection()
    query = f'FOR doc IN `UsersData` RETURN doc'
    cursor = db.AQLQuery(query, rawResults=True)
    title = input('Название: ')

    document = next((doc for doc in cursor if doc["Название"] == title), None)
    if(document):
        marks = input('Жанры: ')
        marks = [str(value) for value in marks.split(',')]
        document["Метки"] = marks
        doc = col.createDocument()
        doc.set(document)
        doc.save()
    #remove_data_byTitle(title)