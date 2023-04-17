from json import load, dump

def load_users():
    try:
        with open('users.json', 'r', encoding='utf-8') as fl:
            try:
                return load(fl)
            except:
                return []
    except FileNotFoundError:
        return []

def save_users(users):
    with open('users.json', 'w', encoding='utf-8') as fl:
        dump(users, fl, indent=4, ensure_ascii=False)

def change_users(login, module, current_score):
    try:
        with open('users.json', 'r+', encoding='utf-8') as fl:
            users = load(fl)
            users[login]['progress'][module] = current_score
            dump(users, fl, indent=4, ensure_ascii=False)
    except FileNotFoundError:
        pass