# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.




# Press the green button in the gutter to run the script.
from trie import Trie, make_from_file

if __name__ == '__main__':
    root = make_from_file('./dictionary.txt')
    res = root.search("fuc")
    print(res)
    res = root.search('bach')
    print(res)
    res = root.search('this')
    print(res)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
