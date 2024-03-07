import random,time

class password():
    def __init__(self,simple,special):
        self.simple = simple
        self.special = special
    def func(self):
        self.generated_pass = []
        print("\n***** WELCOME TO PASSWORD GENERATOR ***** \n")
        time.sleep(1)
        length = int(input("Please specify the length of your passord: "))
        special_choice = int(input("If you want a complex password then press 0 otherwise 1: "))
        if special_choice == 0:
            for i in range(length):
                self.random_letter = random.choice(self.special)
                self.generated_pass.append(self.random_letter)
        elif special_choice == 1:
            for i in range(length):
                self.random_letter_2 = random.choice(self.simple)
                self.generated_pass.append(self.random_letter_2)
        else:
            print("Please try again with appropiate value.")

        print("LOADING!!!!!!!")
        time.sleep(2)
        word = ''.join(self.generated_pass)
        print(f"Your password is \"{word}\" ")

letters = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
special = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','!','@','#','%','^','&','*','(',')','+','-','_','=','0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
p = password(letters,special)
calling = p.func()