import random 
from tourism import tour
from medicine import med
from store import online_store
from cofe import inf_cofe
from day import get_user_day_of_week




def que():

        user_query = input("Вас приветствует автоинформатор!\nЧто вас интересует?\nИнформация туристической компании - 1\nИнформация медицинской клиники - 2\nИнформация интернет-магазина - 3\nИнформация кофэ - 4\nИнформация про сегодняшний день - 5\nЧтобы выйти, введите - Enter\nВвод: ")

        random_words = ('Прекрасно!', 'Великолепно!', 'Отлично!')

        if user_query == "1":
            print(random.choice(random_words), ' Вы, выбрали - Информацию туристической компании.')
            tour()

        elif user_query == "2":
            print(random.choice(random_words), ' Вы, выбрали - Информацию медицинской клиники.')
            med()

        elif user_query == "3":
            print(random.choice(random_words), ' Вы, выбрали - Информацию интернет-магазина.')
            online_store()
        
        elif user_query == '4':
            print(random.choice(random_words), 'Вы, выбрали - Информацию кофэ.')
            inf_cofe()


        elif user_query == '5':
            print(random.choice(random_words), 'Вы, выбрали информацию про сегодняшний день.')
            print(get_user_day_of_week())


        else:
            print('Досвидания!')


que()

