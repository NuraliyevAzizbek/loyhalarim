from son_topish_oyini1 import imkoniyatlar_soni
from son_topish_oyini2 import oyin2

while True:
    i = imkoniyatlar_soni()
    j = oyin2()
    if i < j:
        print(f"\nBu o'yinda siz yutdingiz.Men {j} urunishda topdim.Siz {i} urunishda topdingiz.")
    elif i == j:
        print(f"\nBu o'yinda durrang bo'ldi.Men {j} urunishda topdim.Siz {i} urunishda topdingiz.")
    else:
        print(f"\nBu o'yinda men yutdim.Men {j} urunishda topdim.Siz {i} urunishda topdingiz.")
    yana = input("Yana o'ynashni hohlaysizmi(ha(1)\yo'q(0))>>>")
    if yana == "1":
        continue
    else:
        break
print("Ishtirokingiz uchun tashakkur!!!")