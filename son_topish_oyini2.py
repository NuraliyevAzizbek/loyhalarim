import random as r
def oyin2():
   print("""Keling o'yinni keyingi qismiga o'tamiz.
Endi siz son o'yleysiz men topishga harakat qilaman.""")
   j=1
   print("Avval sonlar oraligini tanlang :(k-boshlanish,g-tugash)")
   k= 1
   g= 101
   uylov= int(input("siz uylagan son : "))
   qanot= True
   while qanot:
      son = r.randint(k,g)
      print(f"""Siz o'ylagan son {son}ga teng.Agar to'g'ri bo'lsa (t),
kichik bo'lsa (+),katta bo'lsa (-) deb yozing.""")
      ishora=True
      while ishora:
        a = input(">>> ")
        if a == "t":
            print(f"Men {j} urunishda topdim.")
            break
        elif a == "+":
            print(f"{son} men uylagan sondan katta")
            k= son+1
            ishora= False
        elif a == "-":
            print(f"{son} men uylagan sondan kichik")
            g= son-1
            ishora= False
        else:
            print("Sizda bunday tanlov yo'q.Qaytadan urunib ko'ring.")
            continue
        j+=1
      if a=='t':
        qanot= False
   return j