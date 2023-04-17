'''
dict_tmp = {'domesticated animals' : 5
                , 'wild animals' : 10
                , 'pets' : 0
                , 'jobs' : 2
                , 'fruits' : 7
                , 'vegetables' : 3}
'''

def string_progress(progress):
    tmp = ""
    for module in progress:
        tmp += f'{module[0]} - {module[1]}\n'
    return tmp

def sort_progress(progress):
    return sorted(progress.items(), key=lambda item: item[1], reverse=True)

def give_sorted_progress(progress):
    return string_progress(sort_progress(progress))