"""
Build Tower
Build Tower by the following given argument:
number of floors (integer and always greater than 0).

Tower block is represented as *
Python: return a list;
"""


def tower_builder(n_floors):
    base_star = '*'

    result = []
    indent = 0
    for num in range(n_floors, 0, -1):
        count = num * 2 - 1
        level = base_star * count
        space = ' ' * (indent // 2)
        result.append(space + level + space)
        indent += 2

    return result[::-1]


print(tower_builder(6))

"""
[
'     *     ', 
'    ***    ', 
'   *****   ', 
'  *******  ', 
' ********* ', 
'***********'
]
"""
