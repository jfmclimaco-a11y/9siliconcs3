list = []
def list_of_cat(list):
    Name = input("Input its name: ")
    FurColor = input("Input its fur color: ")
    EyeColor = input("Input its eye color: ")
    Breed = input("Input its breed: ")
    Height = int(input("Input its height: "))
    Length = int(input("Input its length: "))
    list_of_cat = [Name, EyeColor, FurColor, Breed, Height, Length]
    list.append(list_of_cat)
    return list
i = 0
while i == 0:
    a = 0
    while a == 0:
        reply_1 = input("Would you like to list a cat's information? (Answer with Yes or No)")
        if reply_1 == "No":
            a = 1
        else:
            Name = list_of_cat(list)
    reply_2 = int(input(f"""What would you like to do with the cat?
    -----------------------
    1 - Get its eye color
    2 - Get its fur color
    3 - Get its breed
    4 - Measure its Height
    5 - Measure its Length
    -----------------------
    Input: """))
    if reply_2 == 1:
        reply_2_1 = input("What's the name of the cat you're trying to get the eye color? ")
        for x in range(len(list)):
            if list[x][0] == reply_2_1:
                print(f'The eye color of the cat named "{list[x][0]}" is {list[x][1]}')
                break
    if reply_2 == 2:
        reply_2_2 = input("What's the name of the cat you're trying to get the fur color? ")
        for y in range(len(list)):
            if list[y][0] == reply_2_2:
                print(f'The fur color of the cat named "{list[y][0]}" is {list[y][2]}')
                break
    if reply_2 == 3:
        reply_2_3 = input("What's the name of the cat you're trying to get the breed? ")
        for z in range(len(list)):
            if list[z][0] == reply_2_3:
                print(f'The breed of the cat named "{list[z][0]}" is {list[z][3]}')
                break
    if reply_2 == 4:
        reply_2_4 = input("What's the name of the cat you're trying to get the height? ")
        for w in range(len(list)):
            if list[w][0] == reply_2_4:
                print(f'The height of the cat named "{list[w][0]}" is {list[w][4]}')
                break
    if reply_2 == 5:
        reply_2_5 = input("What's the name of the cat you're trying to get the length? ")
        for v in range(len(list)):
            if list[v][0] == reply_2_5:
                print(f'The length of the cat named "{list[v][0]}" is {list[v][5]}')
                break
