import random
def pass_gen():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    print("Welcome to the PyPassword Generator!")
    nr_letters = random.randint(5,7)#int(input("How many letters would you like in your password?\n"))
    nr_symbols = random.randint(5,7)#int(input(f"How many symbols would you like?\n"))
    nr_numbers = random.randint(5,7)#int(input(f"How many numbers would you like?\n"))

    library = [letters, numbers, symbols]
    randlet = random.randint(0, len(letters) - 1)

    sh_letters = [random.choice(letters) for x in range(nr_letters)]
    sh_symbols = [random.choice(symbols) for x in range(nr_symbols)]
    sh_numbers = [random.choice(numbers) for x in range(nr_numbers)]

    password = sh_numbers + sh_symbols + sh_letters
    random.shuffle(password)
    password = "".join(password)
    print(password)

pass_gen()