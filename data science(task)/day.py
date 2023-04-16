import datetime


def get_user_day_of_week():
    year = int(input("Введите год: "))
    month = int(input("Введите месяц: "))
    day = int(input("Введите число: "))
    date = datetime.datetime(year, month, day)
    days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье'] 
    return days[date.weekday()] 
    print(get_user_day_of_week())
    


