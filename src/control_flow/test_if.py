"""IF statement

@see: https://docs.python.org/3/tutorial/controlflow.html

There can be zero or more elif parts, and the else part is optional. The keyword ‘elif’ is
short for ‘else if’, and is useful to avoid excessive indentation.

An if … elif … elif … sequence is a substitute for the switch or case statements found
in other languages.
"""


def test_if_statement():
    """IF statement"""

    number = 15
    conclusion = ''

    if number < 0:
        conclusion = 'Number is less than zero'
    elif number == 0:
        conclusion = 'Number equals to zero'
    elif number < 1:
        conclusion = 'Number is greater than zero but less than one'
    else:
        conclusion = 'Number bigger than or equal to one'

    assert conclusion == 'Number bigger than or equal to one'


def test_elif_chain():
    """ELIF chain"""
        
    grade = 71
    conclusion = ''
    
    if grade >= 80:
        conclusion = 'A'
    elif grade >= 70:
        conclusion = 'B'
    elif grade >= 60:
        conclusion = 'C'
    elif grade >= 50:
        conclusion = 'D'
    else:
        conclusion = 'F'

    assert conclusion == 'B'


def test_nested_if():
    """NESTED IF chain"""
        
    number = 13
    conclusion = ''

    if number >= 0:
        if number % 2 == 0:
            conclusion = 'Positive and even.'
        else:
            conclusion = 'Positive and odd.'
    else:
        conclusion = 'Negative.'

    assert conclusion == 'Positive and odd.'
