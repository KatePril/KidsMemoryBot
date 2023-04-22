from json import load

def string_progress(progress):
    tmp = ""
    for module in progress:
        tmp += f'{module[0]} - {module[1]}\n'
    return tmp

def sort_progress(progress):
    return sorted(progress.items(), key=lambda item: item[1], reverse=True)

def give_sorted_progress(login):
    return string_progress(sort_progress(get_user(login)))

def get_user(login):
    try:
        with open('users.json', 'r+', encoding='utf-8') as fl:
            users = load(fl)
            for user in users:
                if user['login'] == login:    
                    return user['progress']
    except FileNotFoundError:
        return {}