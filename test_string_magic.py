from string_magic import string_together, string_apart, string_replace_words
small = "big"
big = "small"

def test_string_together():
    expected = "somethingelse"
    actual = string_together("something","else")
    assert actual == expected
    
def test_string_apart():
    expected = ["This","function","is",small, "brain"]
    actual = string_apart("This function is big brain")
    assert expected == actual


def test_string_replace_words():
    expected = "small brains think small thoughts small the time"
    sample = "big brains think big thoughts big the time"
    # REMINDER: make sure to cover positional arguments clearly
    # REMINDER: make sure to clearly show how return value makes it back to the variable in below assignment.
    actual = string_replace_words (sample,"big","small")
    assert expected == actual