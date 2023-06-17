
# =============================================================================
# #4-5-solutions
# mahsulotlar = ['olma','anor','uzum','behi','anjir','qovun','tarvuz','olcha']
# savat = []
# bor_mahsulotlar = []
# mavjud_emas = []
# 
# for a in range(5):
#     savat.append(input(f"{a+1}-mahsulotni kiriting: "))
#     
# for taom in savat:
#     if taom in mahsulotlar:
#         bor_mahsulotlar.append(taom)
#     else:
#          mavjud_emas.append(taom)
# if mavjud_emas:
#     print("quyidagi yo'q")
#     for n in mavjud_emas:
#         print(n)
# else:
#     print("Siz so'ragan hammasi bor")
#             
# =============================================================================
    


# =============================================================================
# 6-solution
#
# foydalanuvchilar = ['nodirbek','azamat','suhrob','elyor','anvar']
# foydalanuvchi = input("Login kiriting: ")
# if foydalanuvchi.lower() in foydalanuvchilar:
#     print("Login band, yangi login tanlang!")
# else:
#     print(f"Xush kelibsiz, {foydalanuvchi}")
# =============================================================================

sonlar = []
son = int(input("Son kiriting: "))
for n in range(2,11):
    if son%n == 0:
        sonlar.append(n)
print(f"{son} {sonlar}larga bo'linadi.")
