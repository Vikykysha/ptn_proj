def get_int(start_message, error_message, end_message):
   """ Получает на вход начальные и конечные сообщения. ПРосит ввести
   число. Если, то что ввели - число, печает end_message и возвращает
   число. Использовать функцию isdigit не получится, так как данная функция не понимает нецелых чисел
   либо знаков - и + """
    print(start_message)
    while True:
        try:
            i = int(input())
            print(end_message)
            return i
        except ValueError:
            print(error_message)
