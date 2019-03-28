print("Welcome to 'I don't have dice for D&D!' dice roller!")
while True:
    que1=str(input("what dice are you rolling today?\n")).lower()
    ans1="d4"
    ans2="d6"
    ans3="d8"
    ans4="d10"
    ans5="d12"
    ans6="d20"
    ans7="d100"
    ans8="end"
    if ans1==que1:
        import random
        print(random.randint(1, 4))
    elif ans2==que1:
        import random
        print(random.randint(1, 6))
    elif ans3==que1:
        import random
        print(random.randint(1, 8))
    elif ans4==que1:
        import random
        print(random.randint(1, 10))
    elif ans5==que1:
        import random
        print(random.randint(1, 12))
    elif ans6==que1:
        import random
        print(random.randint(1, 20))
    elif ans7==que1:
        import random
        random=(random.randint(0, 9))
        print(random * 10)
    elif ans8==que1:
        break
    
        
