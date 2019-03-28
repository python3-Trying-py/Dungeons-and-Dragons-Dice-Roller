print("Welcome to 'I don't have dice for D&D!' dice roller!")
while True:
    que1=input("what dice are you rolling today?\n")
    ans1="D4"
    ans2="D6"
    ans3="D8"
    ans4="D10"
    ans5="D12"
    ans6="D20"
    ans7="D100"
    ans8="End"
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
    
        
