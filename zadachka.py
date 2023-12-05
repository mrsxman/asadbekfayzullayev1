# 1
# Uzunlikni santimetrda olish
L_santimetrda = float(input("Uzunlikni santimetrda kiriting: "))

# Uzunlikni metrlarda hisoblash
L_metrlarda = L_santimetrda / 100

# Natijani chiqarish
print(f"{L_santimetrda} santimetr {L_metrlarda} metr ga teng.")

# 2

# Girlikni kilogramda olish
M_kilogramda = float(input("G'irlikni kilogramda kiriting: "))

# Girlikni tonnalarda hisoblash
M_tonnalarda = M_kilogramda / 1000

# Natijani chiqarish
print(f"{M_kilogramda} kilogram {M_tonnalarda} tonnaga teng.")

# 3

# Fayl hajmini baytlarda olish
hajm_bayt = int(input("Fayl hajmini baytlarda kiriting: "))

# Fayl hajmini kilobaytlarda hisoblash
hajm_kilobayt = hajm_bayt / 1024

# Natijani chiqarish
print(f"Fayl hajmi {hajm_bayt} bayt, {hajm_kilobayt} kilobayt ga teng.")

# 4

# A va B ni olish
A = int(input("A ni kiriting: "))
B = int(input("B ni kiriting (A dan kichik): "))

# A kesmasini B kesmasiga necha marta joylashtirish mumkinligini hisoblash
marta_son = A // B

# Natijani chiqarish
print(f"A kesmasini B kesmasiga {marta_son} marta joylashtirish mumkin.")

# 5

# A va B ni olish
A = int(input("A ni kiriting: "))
B = int(input("B ni kiriting (A dan kichik): "))

# Necha marta joylashtirish mumkinligini hisoblash
marta_son = A // B

# Joylashmagan qismini hisoblash
joylanmagan_qism = A % B

# Natijani chiqarish
print(f"A kesmasida B kesmasini {marta_son} marta joylashtirish mumkin.")
print(f"A kesmasida joylashmagan qism uzunligi: {joylanmagan_qism}")

# 7

# Ikki xonali sonni olish
ikki_xonali_son = int(input("Ikki xonali son kiriting: "))

# O'nlik xonasidagi va birlar xonasidagi raqamlarni olish
onlik_xona = ikki_xonali_son // 10
birlar_xona = ikki_xonali_son % 10

# Natijani chiqarish
print(f"O'nlik xonasidagi raqam: {onlik_xona}")
print(f"Birlar xonasidagi raqam: {birlar_xona}")

# 8

# Ikki xonali sonni olish
ikki_xonali_son = int(input("Ikki xonali son kiriting: "))

# Raqamlarni olish
birliklar = ikki_xonali_son % 10
onliklar = ikki_xonali_son // 10

# Raqamlar yig'indisini hisoblash
raqamlar_yigindisi = birliklar + onliklar

# Natijani chiqarish
print(f"Ikki xonali son raqamlari yig'indisi: {raqamlar_yigindisi}")

# 9

# Uch xonali sonni olish
uch_xonali_son = int(input("Uch xonali son kiriting: "))

# Yuzlar xonasidagi raqamni olish
yuzlar_xonasi = uch_xonali_son // 100

# Natijani chiqarish
print(f"Uch xonali sonning yuzlar xonasidagi raqami: {yuzlar_xonasi}")



# 10

# Uch xonali sonni olish
uch_xonali_son = int(input("Uch xonali son kiriting: "))

# Birliklar va o'nliklar xonasidagi raqamlarni olish
birliklar = uch_xonali_son % 10
onliklar = (uch_xonali_son // 10) % 10

# Natijani chiqarish
print(f"Birliklar xonasidagi raqam: {birliklar}")
print(f"O'nliklar xonasidagi raqam: {onliklar}")


# 11

# Uch xonali sonni olish
uch_xonali_son = int(input("Uch xonali son kiriting: "))

# Raqamlarni olish
birliklar = uch_xonali_son % 10
onliklar = (uch_xonali_son // 10) % 10
yuzlar = uch_xonali_son // 100

# Raqamlar yig'indisini hisoblash
raqamlar_yigindisi = birliklar + onliklar + yuzlar

# Natijani chiqarish
print(f"Uch xonali sonning raqamlari yig'indisi: {raqamlar_yigindisi}")

# 12

# Uch xonali sonni olish
uch_xonali_son = int(input("Uch xonali son kiriting: "))

# Raqamlarni olish
birliklar = uch_xonali_son % 10
onliklar = (uch_xonali_son // 10) % 10
yuzlar = uch_xonali_son // 100

# Teskari tartibda raqamlarni yozish
teskari_son = birliklar * 100 + onliklar * 10 + yuzlar

# Natijani chiqarish
print(f"Uch xonali sonning teskari tartibdagi soni: {teskari_son}")

# 13

# Uch xonali sonni olish
uch_xonali_son = int(input("Uch xonali son kiriting: "))

# Chapdan birinchi raqamni o'chirish va o'ng tarafiga yozish
birliklar = uch_xonali_son % 10
onliklar = (uch_xonali_son // 10) % 10
yuzlar = uch_xonali_son // 100

# Yangi sonni hosil qilish
yangi_son = birliklar * 100 + yuzlar * 10 + onliklar

# Natijani chiqarish
print(f"Yangi hosil bo'lgan son: {yangi_son}")


# 14

# Foydalanuvchi kiritgan sonni o'qish
son = int(input("Istalgan sonni kiriting: "))

# Sonni o'ngdan birinchi raqamini olib tashlash
birinchi_raqam = son % 10

# O'ngdan birinchi raqamni o'chirib tashlash
o_chirilgan_son = son // 10

# Yangi sonni aniqlovchi ma'lumotni chiqarish
yangi_son = int(str(birinchi_raqam) + str(o_chirilgan_son))

# Natijani chiqarish
print("Natija:", yangi_son)


# 15


# Foydalanuvchi kiritgan uch xonali sonni o'qish
son = int(input("Uch xonali sonni kiriting: "))

# O'nliklar va yuzliklar xonasidagi raqamlarni olish
uzoq_qism = son // 100
o_nliklar = (son // 10) % 10
birliklar = son % 10

# Raqamlarni almashish
almashgan_son = o_nliklar * 100 + uzoq_qism * 10 + birliklar

# Natijani chiqarish
print("Almashgan son:", almashgan_son)


# 16


# Foydalanuvchi kiritgan uch xonali sonni o'qish
son = int(input("Uch xonali sonni kiriting: "))

# O'nliklar va birliklar xonasidagi raqamlarni olish
o_nliklar = (son // 10) % 10
birliklar = son % 10

# Raqamlarni almashish
almashgan_son = o_nliklar * 10 + birliklar

# Natijani chiqarish
print("Almashgan son:", almashgan_son)


17

# Foydalanuvchidan sonni olish
son = int(input("Butun son kiriting (999 dan katta): "))

# Sonni yuliklar xonasidagi sonni olish
yuliklar_xonasi = son % 10

# Butun qismini va qoldiqni olish
butun_qism = son // 10
qoldiq = son % 10

# Natijani chiqarish
print("Yuliklar xonasidagi son:", yuliklar_xonasi)
print("Butun qism:", butun_qism)
print("Qoldiq:", qoldiq)


# 18

# Foydalanuvchidan sonni olish
son = int(input("Butun son kiriting (999 dan katta): "))

# Mingliklar xonasidagi sonni olish
mingliklar_xonasi = son // 1000

# Butun qismini va qoldiqni olish
butun_qism = son % 1000

# Natijani chiqarish
print("Mingliklar xonasidagi son:", mingliklar_xonasi)
print("Butun qism:", butun_qism)

# 19

# Foydalanuvchidan kun boshidan o'tgan sekundlarni olish
sekundlar = int(input("Kun boshidan o'tgan sekundlarni kiriting: "))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               

# Kunlarni vaqtning kun boshidan qancha kun to'la o'tganligini hisoblash
kunlar = sekundlar // (24 * 60 * 60)

# Natijani chiqarish
print(f"Kun boshidan {sekundlar} sekund o'tganda {kunlar} kun o'tdi.")


# 20

from datetime import datetime, timedelta

def kun_boshidan_boshlab_o_tish(N):
    # Joriy vaqt
    joriy_vaqt = datetime.now()

    # Boshlang'ich kunni hisoblash
    boshlangich_kun = joriy_vaqt.replace(hour=0, minute=0, second=0, microsecond=0)

    # N sekund vaqt o'tishi
    o_tish_vaqt = boshlangich_kun + timedelta(seconds=N)

    # Joriy vaqt va o'tgan vaqt orasidagi farqni hisoblash
    farq = o_tish_vaqt - joriy_vaqt

    # Qancha to'la soat o'tganligini hisoblash
    soat = farq.seconds // 3600
    minut = (farq.seconds % 3600) // 60
    sekund = farq.seconds % 60

    # Natijani chiqarish
    print(f"{N} sekund o'tgandan so'ng {soat} soat, {minut} minut va {sekund} sekund o'tdi.")

# Misol: N = 3600 sekund (1 soat)
kun_boshidan_boshlab_o_tish(3600)


# 21

from datetime import timedelta

def kun_boshidan_boshlab_o_tish(N):
    # N sekund vaqt o'tishi
    o_tish_vaqt = timedelta(seconds=N)

    # Qancha soat, minut, va sekund o'tganligini hisoblash
    soat = o_tish_vaqt.seconds // 3600
    minut = (o_tish_vaqt.seconds % 3600) // 60
    sekund = o_tish_vaqt.seconds % 60

    # Natijani chiqarish
    print(f"{N} sekund o'tgandan so'ng {soat} soat, {minut} minut va {sekund} sekund o'tdi.")

# Misol: N = 3665 sekund
kun_boshidan_boshlab_o_tish(3665)


# 22

from datetime import timedelta

def kun_boshidan_boshlab_o_tish(N):
    # N sekund vaqt o'tishi
    o_tish_vaqt = timedelta(seconds=N)

    # Qancha soat vaqti o'tganligini hisoblash
    soat = o_tish_vaqt.seconds // 3600
    sekund = o_tish_vaqt.seconds % 3600

    # Natijani chiqarish
    print(f"{N} sekund o'tgandan so'ng {soat} soat va {sekund} sekund o'tdi.")

# Misol: N = 3665 sekund
kun_boshidan_boshlab_o_tish(3665)

# 23

from datetime import timedelta

def kun_boshidan_boshlab_o_tish(N):
    # N sekund vaqt o'tishi
    o_tish_vaqt = timedelta(seconds=N)

    # Qancha soat, minut va sekund o'tganligini hisoblash
    soat = o_tish_vaqt.seconds // 3600
    minut = (o_tish_vaqt.seconds % 3600) // 60
    sekund = o_tish_vaqt.seconds % 60

    # Natijani chiqarish
    print(f"{N} sekund o'tgandan so'ng {soat} soat, {minut} minut va {sekund} sekund o'tdi.")

# Misol: N = 3665 sekund
kun_boshidan_boshlab_o_tish(3665)

# 24

def kun_topish(yil, k):
    # 1-yanvar 1-dushanba
    kunlar = ["yekshanba", "dushanba", "seshanba", "chorshanba", "payshanba", "juma", "shanba"]

    # Yilning 1-yanvar kuni
    bir_yanvar = kunlar[(yil - 1 + (yil - 1) // 4 - (yil - 1) // 100 + (yil - 1) // 400) % 7]

    # Yotuvchi soni bo'yicha kiritilgan kunni topish
    topilgan_kun = kunlar[(k + kunlar.index(bir_yanvar)) % 7]

    return topilgan_kun

# Misol: 2023 yili, K=13
yil = 2023  
K = 13

natija = kun_topish(yil, K)
print(f"{yil} yilning {K}-kuni {natija}ga to'g'ri keladi.")


# 25

def kun_topish(yil, k):
    # 1-yanvar 1-payshanba
    kunlar = ["yekshanba", "dushanba", "seshanba", "chorshanba", "payshanba", "juma", "shanba"]

    # Yilning 1-yanvar kuni
    bir_yanvar = kunlar[(yil - 1 + (yil - 1) // 4 - (yil - 1) // 100 + (yil - 1) // 400) % 7]

    # Yotuvchi soni bo'yicha kiritilgan kunni topish
    topilgan_kun = kunlar[(k - kunlar.index(bir_yanvar)) % 7]

    return topilgan_kun

# Misol: 2023 yili, K=13
yil = 2023
K = 13

natija = kun_topish(yil, K)
print(f"{yil} yilning {K}-kuni {natija}ga to'g'ri keladi.")

# 26

def kun_topish(yil, k):
    # 1-yanvar 0-yakshanba
    kunlar = ["yakshanba", "yekshanba", "dushanba", "seshanba", "chorshanba", "payshanba", "juma", "shanba"]

    # Yilning 1-yanvar kuni
    bir_yanvar = kunlar[(yil - 1 + (yil - 1) // 4 - (yil - 1) // 100 + (yil - 1) // 400) % 7]

    # Yotuvchi soni bo'yicha kiritilgan kunni topish
    topilgan_kun = kunlar[(k - kunlar.index(bir_yanvar)) % 7]

    return topilgan_kun

# Misol: 2023 yili, K=13
yil = 2023
K = 13

natija = kun_topish(yil, K)
print(f"{yil} yilning {K}-kuni {natija}ga to'g'ri keladi.")


# 27

def kun_topish(yil, k):
    # 1-yanvar 7-yakshanba
    kunlar = ["yakshanba", "yekshanba", "dushanba", "seshanba", "chorshanba", "payshanba", "juma", "shanba"]

    # Yilning 1-yanvar kuni
    bir_yanvar = kunlar[(yil - 1 + (yil - 1) // 4 - (yil - 1) // 100 + (yil - 1) // 400) % 7]

    # Yotuvchi soni bo'yicha kiritilgan kunni topish
    topilgan_kun = kunlar[(k - kunlar.index(bir_yanvar)) % 7]

    return topilgan_kun

# Misol: 2023 yili, K=13
yil = 2023
K = 13

natija = kun_topish(yil, K)
print(f"{yil} yilning {K}-kuni {natija}ga to'g'ri keladi.")


# 28
def joylashuv(A, B, C):
    # To'rtburchakka joylashtirilgan kvadratlar sonini hisoblash
    eng_kop_kvadratlar = min(A // C, B // C)

    # Joylashmagan qismini hisoblash
    joylashmagan_qism = A * B - (eng_kop_kvadratlar * C**2)

    return eng_kop_kvadratlar, joylashmagan_qism

# Misol: A=8, B=12, C=3
A = 8
B = 12
C = 3

eng_kop_kvadratlar, joylashmagan_qism = joylashuv(A, B, C)
print(f"To'g'ri to'rtburchakka eng ko'p joylashtirilgan kvadratlar soni: {eng_kop_kvadratlar}")
print(f"Joylashmagan qismning yuzasi: {joylashmagan_qism}")

# 30


def yuz_yillikka_kirishi(yil):
    if 1000 <= yil <= 2000:
        yuz_yillik = (yil - 1) // 100 + 1
        print(f"{yil} - yil {yuz_yillik} - yuz yillikka kiradi.")
    else:
        print("Noto'g'ri yil kiritildi. 1000 dan 2000 gacha bo'lgan yilni kiriting.")

# Test qilish
test_yil = 1901  # O'zgartiring, agar boshqa yilni sinov qilmoqchi bo'lsangiz
yuz_yillikka_kirishi(test_yil)
