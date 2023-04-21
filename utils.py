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
    print('ok1')
    with open('users.json', 'w', encoding='utf-8') as fl:
        dump(users, fl, indent=4, ensure_ascii=False)

def update_changes(login, module, current_score):
    try:
        with open('users.json', 'r+', encoding='utf-8') as fl:
            users = load(fl)
            for user in users:
                if user['login'] == login:
                    print('ok')    
                    user['progress'][module] = current_score
                    break
            return users
            # dump(users, fl, indent=4, ensure_ascii=False)
    except FileNotFoundError:
        pass