import requests
from bs4 import BeautifulSoup
from ArangoConnection import make_conn_to_db

'''
https://pyarango.readthedocs.io/en/latest/
https://arangodb.com/tutorials/tutorial-python/
'''

def take_fic_janr():
    genre_titles = []
    for i in [1, 2]:
        url = f"https://ficbook.net/tag-categories-8533967/25?p={i}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        }

        response = requests.get(url, headers=headers)

        soup = BeautifulSoup(response.text, 'html.parser')

        genre_elements = soup.find_all('a', class_='font-bold')

        genre_titles += [genre_element.get('title') for genre_element in genre_elements]

    return genre_titles

def add_test_data_to_db(collection):
    # Добавление данных в коллекцию
    data1 = {
        "Tags": ["Юридический", "Научный"],
        "Article": "Сложность анализа административно-правового статуса публичного акционерного общества"
                    "с государственным участием заключается в недостаточном урегулировании статуса таких"
                    "акционерных обществ в одноименном федеральном законе от 26.12.1995 N 208-ФЗ \"Об"
                    "акционерных обществах 1\", поэтому в целях раскрытия данной темы представляется"
                    "необходимым обратиться к анализу отраслевого законодательства. В настоящей работе будут"
                    "рассмотрены такие нормативно правовые акты как: \"Градостроительный кодекс2 Российской"
                    "Федерации\" от 29.12.2004 N 190-ФЗ, Федеральный закон \"О закупках товаров, работ, услуг"
                    "отдельными видами юридических лиц\" от 18.07.2011 N 223-ФЗ 3, \"Арбитражный"
                    "процессуальный кодекс Российской Федерации\" от 24.07.2002 N 95-ФЗ и другие."
    }
    data2 = {
        "Tags": ["Медицинский", "Научный"],
        "Article": "Наноструктуры, изготовленные из этих материалов, поддерживают регенерацию тканей полости рта, охватывая все основные области стоматологии - от пародонтологии и эндодонтии до лечения костей."
                    "Доступная литература показывает, что на сегодняшний день PLGA является наиболее часто используемым полимером для изготовления наночастиц в стоматологии. "
                    "Его свойства делают его особенно подходящим в качестве надежной системы доставки лекарств, но до сих пор нет единого мнения о преимуществах наночастиц PLGA при использовании их отдельно в терапии регенерации костной ткани."
    }
    data3 = {
        "Tags": ["Юридический", "Научный"],
        "Article": "В статье анализируется сущность коррупции с правовой точки зрения. Автор исследует теоретические и практические аспекты коррупции через ключевые аспекты дефиниции этого явления в контексте законодательства."
                    "Осуществлен обзор юридического определения коррупции, с учетом различных аспектов этого явления, такие как злоупотребление властью, взяточничество, мошенничество и иные формы незаконного использования полномочий."
                    "Основываясь на имеющемся определении, автор так же анализирует элементы коррупционных правонарушений, описывая их характеристики, последствия и способы предотвращения."
    }
    data4 = {
        "Tags": ["Медицинский", "Научный"],
        "Article":
                "Ожирение – это хроническое заболевание обмена веществ, развивающееся в результате дисбаланса потребления и расхода энергии, проявляющееся избыточным развитием жировой ткани, прогрессирующее при естественном течении, имеющее определенный круг осложнений, повышающее риск развития различных заболеваний и обладающее высокой вероятностью рецидива после окончания курса лечения [3]. "
                "Проблема ожирения в наше время становится все более актуальной и начинает представлять социальную угрозу для жизни людей. "
                "Значимость проблемы ожирения определяется угрозой инвалидизации пациентов молодого возраста и снижением общей продолжительности жизни в связи с частым развитием тяжелых сопутствующих заболеваний. "
                "Ожирение снижает устойчивость к простудным и инфекционным заболеваниям, а также резко увеличивает риск осложнений при оперативных вмешательствах и травме [4]."
                "Проблема качества жизни пациентов, страдающих ожирением, в современном обществе является социально значимой." 
                "В последние десятилетия социальные и техногенные факторы общества способствуют распространенности ожирения."
    }
    new_doc1 = collection.createDocument(data1)
    new_doc2 = collection.createDocument(data2)
    new_doc3 = collection.createDocument(data3)
    new_doc4 = collection.createDocument(data4)
    new_doc1.save()
    new_doc2.save()
    new_doc3.save()
    new_doc4.save()
    print("Данные успешно добавлены в коллекцию 'Articles'.")


def read_all_docs(documents):
    for doc in documents.fetchAll():
        print(doc)
    return documents.fetchAll()


def create_genre_coll(db):
    if not db.hasCollection("Genres"):
        Collection = db.createcollection(name = "Genres")
    return Collection


def create_fanf_coll(db):
    if not db.hasCollection("Fanfics"):
        Collection = db.createcollection(name = "Fanfics")
    return Collection


def fill_genre_collection(db):
    Genres = db["Genres"]

    data = {
        "Title": "Genres",
        "list_of_genres": str(take_fic_janr())
    }

    new_doc = Genres.createDocument(data)
    new_doc.save()
    print(data)
    return data


def take_fic_info(pg_num=1, genre_titles = []):

    if not genre_titles: return {}

    url = f"https://ficbook.net/fanfiction?p={pg_num}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    fanfics = soup.find_all('div', class_='js-toggle-description')
    genre_titles = set(genre_titles)

    data = []

    for fic in fanfics:
        try:
            title = fic.find('a', class_='visit-link').text.strip()

            # Находим метки
            tags = fic.find('div', class_='tags').text.strip().split('\n\n', 2)[0].split(':\n', 2)[1]
            tags = set(tags.split('\n'))
            tags = list(tags.intersection(genre_titles))

            if not tags:
                continue

            # Находим аннотацию книги
            annotation = fic.find('div', class_='fanfic-description').text.strip()
            data += [{
                'Название': title,
                'Метки': tags,
                'Аннотация': annotation
            }]
        except: continue
    print(data)
    return data


def fill_ficInfo_collection(db):
    docs = read_all_docs(db["Genres"])
    genres = docs[0]["list_of_genres"].replace("[", "").replace("]", "").replace("'", "").split(", ")
    print(genres)
    fanf = create_fanf_coll(db)
    fanf = db["Fanfics"]

    for p in range(1, 50):
        page_data = take_fic_info(p, genres)
        for data in page_data:
            new_doc = fanf.createDocument(data)
            new_doc.save()


db = make_conn_to_db()
create_genre_coll(db)
fill_genre_collection(db)
fill_ficInfo_collection(db)



