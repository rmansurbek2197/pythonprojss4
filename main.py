def matn_teskari(matn):
    sozlar = matn.split()
    teskari_sozlar = []
    for soz in sozlar:
        teskari_soz = soz[::-1]
        teskari_sozlar.append(teskari_soz)
    return ' '.join(teskari_sozlar)

def matn_qayta_ishla(matn):
    sozlar = matn.split()
    qayta_ishlangan_sozlar = []
    for soz in sozlar:
        soz = soz.lower()
        soz = soz.capitalize()
        qayta_ishlangan_sozlar.append(soz)
    return ' '.join(qayta_ishlangan_sozlar)

def asosiy_dastur():
    matn = input("Matn kiriting: ")
    teskari_matn = matn[::-1]
    sozlar = matn.split()
    print("Kelgan matn: ", matn)
    print("Teskari matn: ", teskari_matn)
    print("Har bir so'zni alohida qayta ishlangan matn: ", matn_qayta_ishla(matn))
    print("Har bir so'zni teskari tartibda chiqarilgan matn: ", matn_teskari(matn))
    if len(sozlar) > 5:
        print("Matnda 5 tadan ko'p so'z bor")
    else:
        print("Matnda 5 tadan kam so'z bor")

def boshqa_dastur():
    matn = input("Matn kiriting: ")
    sozlar = matn.split()
    for soz in sozlar:
        print(soz)
    qayta_ishlangan_sozlar = []
    for soz in sozlar:
        soz = soz.upper()
        qayta_ishlangan_sozlar.append(soz)
    print("Qayta ishlangan so'zlar: ", qayta_ishlangan_sozlar)

def qoshimcha_dastur():
    matn = input("Matn kiriting: ")
    sozlar = matn.split()
    for i in range(len(sozlar)):
        print(f"{i+1}-so'z: {sozlar[i]}")

asosiy_dastur()
boshqa_dastur()
qoshimcha_dastur()