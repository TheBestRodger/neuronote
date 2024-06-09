#================
# Интерфейсы    =
#================
import sys
from user import Iadd_new_data, Ishow_All_article_data
from user import Iremove_data_byTitle, find_byTitle, Iupdate_data_byTitle # тупо работает 23.05.2024


def add():
    Iadd_new_data()
def Remove():
    Iremove_data_byTitle()
def Update():
    Iupdate_data_byTitle()
def Display():
    print("\n Достпуные действия: ")
    print("1. Отобразить данные в виде диаграммы.")
    print("2. Поиск данных по названию.")
    print("3. Отобразить все данные.")
    choice = input("Выберите действие (1-3): ")
    if choice == "1":
        add()
    elif choice == "2":
        find_byTitle()
    elif choice == "3":
        Ishow_All_article_data()
def main():
    print("Hello, this is Interface to communicate with BD")
    while True:
        print("\n Достпуные действия: ")
        print("1. Добавить данные.")
        print("2. Удалить  данные.")
        print("3. Изменить данные.")
        print("4. Показать данные.")
        print("5. Выход.")
        choice = input("Выберите действие (1-5): ")
        if choice == "1":
            add()
        elif choice == "2":
            Remove()
        elif choice == "3":
            Update()
        elif choice == "4":
            Display()
        elif choice == "5":
            sys.exc_info()
            sys.exit()
        else:
            print("Неверный выбор. Попробуйте еще раз.")