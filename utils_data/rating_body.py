from utils import load_users

def get_users_rating(login):
    users = load_users()
    users = sort_rating(get_users_sums(users))
    current_user_found = False
    reply = ''
    for i in range(len(users)):
        if i < 10:
            if users[i].get('login') == login:
                reply += get_current_user_rating(i, users[i])
                current_user_found = True
            else:
                reply += get_user_rating(i, users[i])
        elif current_user_found:
            break
        else:
            if users[i].get('login') == login:
                reply += '...\n' + get_current_user_rating(i, users[i])
                current_user_found = True
    return reply

def get_user_rating(i, user):
    return f'{i + 1}. {user.get("login")} - {user.get("points")}\n'

def get_current_user_rating(i, user):
    return f'{i + 1}. {user.get("login")}(you) - {user.get("points")}\n'

def get_users_sums(users):
    new_users = []
    for user in users:
        new_users.append({'login' : user.get("login"), 'points' : sum(user.get("progress").values())})
    return new_users

def sort_rating(users):
    swap = True
    while swap:
        swap = False
        
        for i in range(1, len(users) - 1, 2):
            if compare_elements(users[i], users[i+1]):
                change_places(users, i, i+1)
                swap = True
                
        for i in range(0, len(users) - 1, 2):
            if compare_elements(users[i], users[i+1]):
                change_places(users, i, i+1)
                swap = True
    return users
    
def compare_elements(element_1, element_2):
        return element_1.get('points') < element_2.get('points')

def change_places(list, index_1, index_2):
    list[index_1], list[index_2] = list[index_2], list[index_1]