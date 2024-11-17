import random

#Bot AND the player's score(DO NOT DELETE ANY OF THAT UNLESS YOU KNOW WHAT ARE YOU DOING)
bot_puan = 0
oyuncu_puan = 0


#The main event happens here.
while True:        
    #Values here for the game.
    yanit = input("Taş mı?Kağıt mı?Makas mı?")
    bot_yanit = random.randint(1,3)
    bot_yanit_tkm = None

    #exit() command
    if yanit == "exit()":
        print("Closing Rock Paper Scissors : Turkish Edition...")
        break

    #Selecting the value for "bot_yanit_tkm".
    if bot_yanit == 3:
        bot_yanit_tkm = "Makas"
    if bot_yanit == 2:
        bot_yanit_tkm = "Kağıt"
    if bot_yanit == 1:
        bot_yanit_tkm = "Taş"
        
    #The game starts here
    if yanit == "Makas" and bot_yanit_tkm == "Kağıt" or yanit == "Taş" and bot_yanit_tkm == "Makas" and yanit == "Kağıt" and bot_yanit_tkm == "Taş":
        oyuncu_puan = oyuncu_puan + 1
        print(oyuncu_puan, bot_puan)
    else:
        if yanit == "Makas" and bot_yanit_tkm == "Makas" or yanit == "Taş" and bot_yanit_tkm == "Taş" or yanit == "Kağıt" and bot_yanit_tkm == "Kağıt":
            print("Aynı hamle!")
            print(oyuncu_puan,bot_puan)
        else:
            bot_puan = bot_puan + 1
            print(bot_yanit_tkm)
            print(oyuncu_puan,bot_puan)

    #The game ends here
    if oyuncu_puan == 3:
        print("Kazandınız!!!!")
        break

    elif bot_puan == 3:
        print("Kaybettiniz...")
        break