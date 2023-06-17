# -*- coding: utf-8 -*-
"""
Created on Tue May 16 21:20:36 2023

@author: Hp
"""

# solution-1
# ismlar = ["Nodirbek", "Asliddin", "Aziz"]
# print(ismlar)

# solution-2
# ismlar = ["Nodirbek", "Asliddin", "Aziz"]
# print(ismlar)
# nodirbek = ismlar.pop(0)
# asliddin = ismlar.pop(0)
# aziz = ismlar.pop(0)
# print("Salom " + nodirbek +" ishlaring yaxshimi?")
# print(asliddin + " kurslar bo'lyaptimi?")
# print("nimalar bilan bandsan " + aziz)

# solution-3
# sonlar = []
# sonlar.append(76568435)
# sonlar.insert(1, 7667.5656)
# sonlar.insert(2, -59595)
# print(sonlar)

# solution-4
# sonlar = []
# sonlar.append(76568435)
# sonlar.insert(1, 7667.5656)
# sonlar.insert(2, -59595)
# print(sonlar[0] + sonlar[1])
# print(sonlar[2] - sonlar[1])
# print(sonlar[1] * sonlar[2])
# print(sonlar[0] / sonlar[1])
# sonlar[1] = 2020
# sonlar[0] = sonlar[0] - 75568435
# print(sonlar)

# solution-5
# t_shaxslar = [] 
# z_shaxslar = [] 
# t_shaxslar.append('ibn sino')
# t_shaxslar.insert(0,'xorazmiy')
# t_shaxslar.insert(1, 'amir timur')
# z_shaxslar.append("bobir akhilxonov")
# z_shaxslar.insert(0, "umidjon")
# z_shaxslar.insert(1, "hasanxo'ja")
# ism1 = t_shaxslar.pop(1)
# ism2 = t_shaxslar.pop(0)
# ism3 = t_shaxslar.pop()
# ism_1 = z_shaxslar.pop()
# ism_2 = z_shaxslar.pop(1)
# ism_3 = z_shaxslar.pop(0)
# print("\nMen tarixiy shaxslardan " + ism2.title() + 
#       " bilan,\nzamonviy shaxslardan esa " + ism_3.capitalize() + 
#       " bilan \nsuhbat qilishni istar edim \n" )
# print("Men tarixiy shaxslardan " + ism1.title() + 
#       " bilan,\nzamonviy shaxslardan esa " + ism_2.capitalize() + 
#       " bilan \nsuhbat qilishni istar edim \n" )
# print("Men tarixiy shaxslardan " + ism3.title() + 
#       " bilan,\nzamonviy shaxslardan esa " + ism_1.capitalize() + 
#       " bilan \nsuhbat qilishni istar edim" )

# solution-6
# friends = []
# friends.append('suhrobbek')
# friends.append('asilbek')
# friends.append('azamatjon')
# friends.append('qudrat')
# friends.append('javohir')
# print(friends)

# solution-7,8,9
friends = []
friends.append('suhrobbek')
friends.append('asilbek')
friends.append('azamatjon')
friends.append('qudrat')
friends.append('javohir')
friends.remove('qudrat')
del friends[1]
print(friends)

friends.append('qayumjon')
friends.insert(0, 'alisher')
friends.insert(2, 'damir')
print(friends)

mehmonlar = []
mehmonlar.append('javlon')
mehmonlar.append('zokir')
ism_1 = friends.pop(4)
ism_2 = friends.pop(3)
mehmonlar.append(ism_1)
mehmonlar.append(ism_2)
print(mehmonlar)

