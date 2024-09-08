# Find out common letters between two strings Using Python

def common_letters():
    name1 = input("Enter name 1:\t")
    name2 = input("Enter name 2:\t")
    s1 = set(name1.lower())
    s2 = set(name2.lower())
    com = s1 & s2
    print(s1)
    print(s2)
    print("")
    print(com)


common_letters()
