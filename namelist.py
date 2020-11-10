"""
Return: a string formatted as a list of names separated by commas except for the last two names,
which should be separated by an ampersand. Example:

namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
# returns 'Bart, Lisa & Maggie'

namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
# returns 'Bart & Lisa'

namelist([ {'name': 'Bart'} ])
# returns 'Bart'

namelist([])
# returns ''
"""


def namelist(names):
    # your code here
    result_list = []
    for list_dict in names:
        for name in list_dict.values():
            result_list.append(name)
    if len(result_list) < 2:
        return ''.join(result_list)
    else:
        return ', '.join(result_list[:-1]) + ' & ' + result_list[-1]


def namelist2(names):
    # your code here
    result_list = [list_dict.values() for list_dict in names]
    print(result_list)


# print(namelist([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}, {'name': 'Homer'}, {'name': 'Marge'}]))
# print(namelist([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]))
# print(namelist([{'name': 'Bart'}, {'name': 'Lisa'}]))
# print(namelist([{'name': 'Bart'}]))
# print(namelist([]))


namelist2([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}, {'name': 'Homer'}, {'name': 'Marge'}])
