""" ToDo Application Setup """
# import pandas as pd

# df = pd.read_excel('Financial-Sample.xlsx')
# print(df)

def words_to_snake_case(string_to_convert):
    """ Returns a snake from words """
    return '_'.join(string_to_convert.split(' '))

print(words_to_snake_case("Finance Report"))