from utils import load_users

def get_users_rating(login):
    users = load_users()
    current_user_found = False
    reply = ''
    for i in range(len(users)):
        if i < 10:
            if users[i].get('login') == login:
                reply += get_current_user_rating(i, users[i]) + '\n'
                current_user_found = True
            else:
                reply += get_user_rating(i, users[i]) + '\n'
        elif current_user_found:
            break
        else:
            if users[i].get('login') == login:
                reply += get_current_user_rating(i, users[i]) + '\n'
                current_user_found = True
    return reply

def get_user_rating(i, user):
    return f'{i + 1}. {user.get("login")} - {sum(user.get("progress").values())}'

def get_current_user_rating(i, user):
    return f'{i + 1}. {user.get("login")}(you) - {sum(user.get("progress").values())}'