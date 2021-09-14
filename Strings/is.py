def add_to_string(string):
    if "is" in string[:2]:
        return "\"is\" is already in the begining of the word "
    else:
        return "is " + string

print(add_to_string(input("Write a string with or whitout \"is\": ")))

