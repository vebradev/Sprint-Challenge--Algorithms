'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    target = "th" # set the search term
    location = word.find(target)  # returns index of first occurence
    if word[:len(target)] == target or location > 0:
        return 1 + count_th(word[location + len(target):]) # move the starting index by length of search term and repeat
    else:
        return 0
    
# print(count_th("thooooothoooooooooothooooothooth")) # => 5