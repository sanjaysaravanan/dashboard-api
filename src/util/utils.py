""" Common utility functions """


def snake_case(string_to_convert):
    """ Returns snake_case representation of CamelCase string """
    return ''.join(['_'+i.lower() if i.isupper()
                    else i for i in string_to_convert]).lstrip('_')

def words_to_snake_case(string_to_convert):
    """ Returns a snake from words """
    return '_'.join([i.lower() for i in string_to_convert.split(' ')])
