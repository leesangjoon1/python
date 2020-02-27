#%%
def correct_sentence(text: str) -> str:
    """
        returns a corrected sentence which starts with a capital letter
        and ends with a dot.
    """
    # your code here
    b = list(text)
    if b[-1] == '.' :
        pass
    else:
        b.append('.')
    if b[0].isupper() != True:
        b[0] = b[0].upper()
    c="".join(b)    
    return c


if __name__ == '__main__':
    print("Example:")
    print(correct_sentence("greetings, friends"))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert correct_sentence("greetings, friends") == "Greetings, friends."
    assert correct_sentence("Greetings, friends") == "Greetings, friends."
    assert correct_sentence("Greetings, friends.") == "Greetings, friends."
    assert correct_sentence("hi") == "Hi."
    assert correct_sentence("welcome to New York") == "Welcome to New York."
    
    print("Coding complete? Click 'Check' to earn cool rewards!")


# %%
