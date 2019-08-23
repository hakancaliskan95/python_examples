def error_handler():
    try:
        name = int('1232a')
        lastname = ['yilmaz', 'keskin'][3]
        other_dict = {"name":"merve", "lastname": "demir"}
        other_name = other_dict['other_name']
        age = 1/0
        print('OK!')
    except (ZeroDivisionError,ValueError,IndexError,KeyError):
        print('Error')
