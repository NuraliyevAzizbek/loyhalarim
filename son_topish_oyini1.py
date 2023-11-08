import random as r
import string

def son_oylash():
    """komp 1 dan 10 gacha sonlardan bittasini tanleydi"""
    komp_son = r.randint(1,11)
    return komp_son

        
def imkoniyatlar_soni():
    a = son_oylash()
    i = 1
    print("""Keling siz bilan bir o'yin o'ynaymiz,
Siz o'ylangan 1 dan 100 gacha bo'lgan sonni topishingiz kerak.\n""")
    print("Sonni topib ko'ring")
    while True:
        b = input(">>>")
        if b not in [ f'{i}' for i in range(1,101)]:
            print('Faqat son kiritishingzi mumkin.')
            continue
        if int(b) not in list(range(1,101)):
            print("Faqat 1dan 100 gacha sonlar orasidan kiriting!!!")
            continue
        if int(b) == a:
            print(f"Tabrikleyman siz {i} urunishda topdingiz!!!")
            break
        elif int(b) > a:
            print(f"O'ylangan son {b} dan kichik")
        else:
            print(f"O'ylangan son {b} dan katta")
        print("Qaytadan urunib ko'ring")
        i += 1
    return i