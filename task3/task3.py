# 1
nums = [i for i in range(1, 1001) if i % 17 == 0]

# 2
nums2 = [i for i in range(1, 1001) if '2' in set(str(i))]

# 3
nums3 = [i for i in range(1, 10001) if str(i) == str(i)[::-1]]

# 4
def cnt_spaces(s):
    return sum([ch == ' ' for ch in s])

# 5
def remove_vowels(s):
    return "".join(ch for ch in s if ch.lower() not in ['a', 'e', 'i', 'o', 'u', 'y'])

# 6
def find_short_words(s):
    return [w for w in s.split() if len(w) <= 5]

# 7
def get_dict(s):
    return {w:len(w) for w in s.split()}

# 8
def get_unique(s):
    return list({ch for ch in s if ch.isalpha()})

# 9
def square(lst):
    return list(map(lambda x: x ** 2, lst))

# 10
def filter_coords(coords):
    return {x:(x[0] ** 2 + x[1] ** 2) ** 0.5 for x in [coord for coord in coords if (coord[0]*5 - 2 == coord[1])]}

# 11
squares = [i**2 for i in range(2, 28) if i % 2 == 0]

# 12
def max_dist(coords):
    return max([(x[0] ** 2 + x[1] ** 2) ** 0.5 for x in coords if x[0] > 0 and x[1] > 0])

# 13
def sum_diff(nums_first, nums_second):
    return [(x[0]+x[1], x[0]-x[1]) for x in zip(nums_first, nums_second)]

# 14
def even_squares(lst):
    return list(map(str, [int(i)**2  for i in lst if int(i)%2 == 0]))

# 15
def convert_to_json(input_str):
    return [{x[0]: x[i] for x in [l.split(",") for l in input_str.split()]} for i in range(1, len(input_str.split()[0].split(",")))]

# 16
def sum_columns(lst):
    return [sum(column) for column in [[x[i] for x in lst] for i in range(len(lst[0]))]]





