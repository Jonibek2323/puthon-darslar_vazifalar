# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 21:51:01 2021

@author: User

"""

# # file editor (Matn muharriri)
"""02-dars Hello world!
"""
# print() funktsiyasi matn yoki ifodalarni konsolga chiqarish vazifasini bajaradi
# print("Hello world! 'jooj' ") 
# print('Assalom alaykum')
# #print(Hayrli tong!) #sintex xatolik
# print('Hayrli tong!') #bir tirnoq
# print("Hayrli tong!")
# print(2+4*2)
# print(19/2)
# print(2**4) # izoh (коментарие можно написать )
# # konsul tozalash CLEAR


""" 03-dars PRINT(), SINTEKS VA ARIFMETIK AMALLAR
"""
# Sana: 22/11/2021 22:50
# Muallif: Jonibek
# print('men "Shahbozga" katta raxmat deyman')
# print("men \"Shahbozga\" katta raxmat deyman") 
# " oldin qoyiladi \(bek slesh)
# print("""men Shahbozga katta raxmat deyman
# Assalomu alaykum""")
# print("men Shahbozga katta raxmat deyman \n Assalomu allaykum ") 
# \n qatorni ikkiga 
# print(19/2) #jovobi butun o'nlik son ko'rinishida chiqaradi # J: 9.5
# print(15/3) #(xeshteg--#) bunda ham shunaqa # J: 5.0
# print(20//5) # bunda '//' buton son ko'rinishida chiqaradi # J: 4
# print(15/4) # J:3.75
# print(15//4) #J: 3
# print(2**4) # J:16 (2ni kvadrati)
# print("to'qizning kvadrati", 9**2, "ga teng") 
# # J: to'qizning kvadrati 81 ga teng ("matn", ifoda, "matn")
# print('3*3=',3*3) # J: 3*3= 9
# AMALIYOT: "Nexia", "Tico", 'Damas' ko'rganlar qilar havas
# print(" \"Nexia\", \"Tico\", 'Damas' ko\'rganlar qilar havas" ) 
#print("5 ning 4-darajasini toping", 5**4) 
#print("22 ni 4 ga bo'lganda qancha qoldiq qoladi?", "javobi:", 22%4)   
#print("Tomonlari 125 ga teng kvadratning yuzi va perimetrini toping:",'\nS =',125*125,'\nP =',125+125)
# print("Diametri 12 ga teng bo'lgan doiraning yuzini toping(pi=3.14deb oling):", 'S=', 3.14*12/4)
# print("Katetlari 6 va 7 bo'lgan to'g'ri burchakli uchburchakning \ngipotenuzasini toping (Pifagor teoremasidan foydalaning)", 'c =' , (6**2+7**2)**(1/2))
"""
  04-dars O'zgaruvchilar (Variables)  
"""
# o'zgaruvchi(переменный)bilan ishlashda ularga chiroyli nom tanlash 
# ism = "Jonibek"
# yosh = 21
# print(ism)
# # print(yosh)
# ism = "Muhammad"
# print(ism)
# a=5
# b=6
# c=(a+b)**2
# print(c)
# AMALIYOT:1."Hello World!" matnini yangi o'zgaruvchiga yuklang va print() yordamida konsolga chiqaring
# name = "Hello World"
# print(name)
# # 2.xabar deb nomlangan o'zgaruvchiga biror matn yuklang va konsolga chiqaring, keyin esa o'zgaruvchiga yangi qiymat berib uni ham konsolga chiqaring.
# xabar = "Alloh buyuk"
# print(xabar)
# xabar = "Al-kuran"
# print(xabar)
# # 3.class den nomlangan o'zgaruvchi yarating, unga biror qiymat bering va konsolga chiqaring (siz kutgan natija chiqdimi?)
# class = 5:
#     print(class) #SyntaxError: invalid syntax
# radius = 5
# pi = 3.14159
# aylana_yuzi = pi * radius**2
# print("Radiusi", radius,"ga teng aylananing yuzi=", aylana_yuzi)
"""  
  05-dars STRING (MATN)
"""
# ism = "Jonibek"
# familiya = "Каюмов"
# shahar = "Бухара"
# viloyat = "Вобкент"
# matn = "Men maqsadimni erishishim shart!!! 😁"
# smayl = "😁"  
# print(matn)

## String ustida amallar
# ism = "Shahboz"
# print("Menimg do'stimni ismi " + ism)
# ism = "Mirshod"
# familiya = 'Khaitov'
# print(ism + familiya) #J:MirshodKhaitov
# print(ism + " " + familiya) #J:Mirshod Khaitov
## f-string (usulida jamlash)
# ism = "Mirshod"
# familiya = 'Khaitov'
# ism_familiya = f"Assalomu aleykum {ism} {familiya}"
# # print(ism_familiya)
# ism = "Leri"
# familiya = "Jeni"
# print(f"Assalomu aleykum, mening ismim {ism}.{ism} {familiya}!")

# print("Hello world")
# print("Hello \tworld")
# print("Hello \nworld")
 
# string metodlar  (matn.metod())
# ism = "Jonibek"
# familiya = "Qayumov"
# ism_sharif = f"{ism} {familiya}"
# # print(ism_sharif.upper()) # J:JONIBEK QAYUMOV
# # matn.uppper() - hamma harflarni KATTA harfga almashtiradi
# ism_sharif = ism_sharif.upper()
# print(ism_sharif) 
# # matn.lower() - hamma harflarni KICHKINA harfga almashtiradi
# print(ism_sharif.lower()) #J:jonibek qayumov
# # matn.title() - matndagi BIRINCHI harflarini KATTA harflar bilanyozadi
# print(ism_sharif.title()) #J: Jonibek Qayumov
# # matn.capitalize() - matndagi Faqatgina boshidagi BIRINCHI harflarni KATTA harflar bilanyozadi
# print(ism_sharif.capitalize()) #J:Jonibek qayumov

# meva = "     olma        "
# print(meva) # J:     olma        
# print("Men " + meva.lstrip() + "ni yaxshi ko'raman") 
# # J: Menolma        ni yaxshi ko'raman 
# # matn.lstrip() - chap tomondagi bo'shliqni olib tashlaydi
# print("Men " + meva.rstrip() + "ni yaxshi ko'raman") 
# # matn.rstrip() - o'ng tomondagi bo'shliqni olib tashlaydi 
# # J:Men      olmani yaxshi ko'raman
# print("Men " + meva.strip() + "ni yaxshi ko'raman")
# # matn.rstrip() - o'ng va chap tomondagi bo'shliqni olib tashlaydi 
# # J: Men olmani yaxshi ko'raman

# INPUT - foydalanuvchidan qandaydur malumot olish
# ism = input("Ismingni yoz:")
# print("Assalomu aleykum," + ism) 
# J: Ismingni yoz:Jonibek
#    Assalomu aleykum,Jonibek  
# ism = input("Ismingiz nima?\n")
# print("Assaomu aleykum, " + ism.title())
# J: Ismingiz nima?
#    jonik
#    Assaomu aleykum, Jonik

# AMALIYOT
#Quyidagi o'zgaruvchilarni yarating: 
#Yuqoridagi o'zgaruvchilarni jamlab, quyidagi ko'rinishda konsolga chiqaring:
# kocha = "Bog'bon"
# mahalla = "Sog'bon"
# tuman = "Bodomzor"
# viloyat = "Samarqand"
#print(kocha + " ko'chasi, " + mahalla + " mahallasi, " + tuman + " tumani,"+ ' ' + viloyat + " viloyati")  
# J: Bog'bon ko'chasi, Sog'bon mahallasi, Bodomzor tumani, Samarqand viloyati
#Yuqoridagi o'zgaruvchilarning (kocha, mahalla, tuman, viloyat) qiymatini foydalanuvchidan so'rang. Va avvalgi mashqni takrorlang.
"""       MY COD           
ism = input("Ismingizni kiritng: ")
print("\n Assalomu aleykum,"+ism.upper())
soz_boshi = "\nIltimos quyidagi savolinha yozma tariqada javob bersangiz:"
print(soz_boshi)
kocha = input("ko'changizning nomi:\t")
mahalla =  input("mahallangizning nomi:\t")
tuman = input ("qaysi tumanda yashaysiz:\t")
viloyat = input ("viloyatingizning kiriting:\t")
javob = input("Malumotlaringiz to'g'ri kiritingizmi:\t")
print("Malumotlariz taqdim etganiz uchun rahmat!")
malumot = f"Sizning turar manzilingiz: {kocha.capitalize()} ko'chasi, {mahalla.capitalize()} mahallsai, {tuman.capitalize()} tumani, {viloyat.capitalize()} viloyatii"
print(malumot)
print("Malumotlar uchun katta rahmat!\nMen siz haqizdagi malumotlarni bilib oldim, endi tomomsiz\nSo'g'bo'ling va meni kuting:)")
"""
#Yuqoridagi matnni konsolga chiqarishda har bir verguldan keyin yangi qatordan yozing
# print(kocha + " ko'chasi,\n" + mahalla + " mahallasi,\n" +\
#       tuman + " tumani,\n" + viloyat + " viloyati")  
   ##J:Bog'bon ko'chasi,
    #  Sog'bon mahallasi,
    #  Bodomzor tumani,
    #  Samarqand viloyati
#Yuqoridagi matnni f-string yordamida, yangi, manzil deb nomlangan o'zgaruvchiga yuklang
# manzil = f"{kocha} kochasi,\n{mahalla} mahallasi,\n\
# {tuman} tumani,\n{viloyat} viloyati"
# print(manzil)
## J:Bog'bon kochasi,
 #   Sog'bon mahallasi,
 #   Bodomzor tumani,
 #   Samarqand viloyati
# manzil ga biz yuqorida o'rgangan title(), upper(), lower() , capitalize() metodlarini qo'llab ko'ring. 
# manzil = f"{kocha} ko'chasi, {mahalla} mahallasi,\
#     {tuman} tumani, {viloyat} viloyati"
# print(manzil.upper())
# print(manzil.lower())
# print(manzil.title())
# print(manzil.capitalize())
# #J: BOG'BON KO'CHASI, SOG'BON MAHALLASI,BODOMZOR TUMANI, SAMARQAND VILOYATI
# bog'bon ko'chasi, sog'bon mahallasi,bodomzor tumani, samarqand viloyati
# Bog'Bon Ko'Chasi, Sog'Bon Mahallasi,Bodomzor Tumani, Samarqand Viloyati
# Bog'bon ko'chasi, sog'bon mahallasi,bodomzor tumani, samarqand viloyati
"""
   25.11.2021
   06-dars.SONLAR
"""
# #SON BILAN MATNNI QO'SHIB BO'LMAYDI!!!!!!
# a = 20 #int(intger-butun son)
# b = 5.5  #float (floating point namber - o'nlik son) 
# temp = 36.6
# #print(type(a))-- type(a) - oz'garuvchining(a-ning) turini chiqarib beradi
# aholi_soni = 7_599_376_567  # uzun sonlarni o'qish qulay bo'lishi uchun _ qoyamiz
# print("Aholi soni:", aholi_soni) #SON BILAN MATNNI QO'SHIB BO'LMAYDI!!!!!!
# x, y, z = 5, -60.5, 10.6
# print(x)
# c = a*b #natija o'nlik son bo'ladi: 110.0
# print(c)
# d = 100/2 #natija o'nlik son bo'ladi: 50.0
# d = 10//2 #natija butun son bo'ladi: 50
# # CONSTANTA (KATTA SON BILAN YOZILADI)
# radius = 20
# PI = 3.14159
# diametr = 2*radius
# print("Aylananing uzunligi=", PI*diametr) #SON BILAN MATNNI QO'SHIB BO'LMAYDI!!!!!!

# #ism = "Jonibek"
# #yosh = 21
# #xabar = ism + ' ' + yosh + 'da'
# ## print(xabar) #TypeError: can only concatenate str (not "int") to str
# #SON BILAN MATNNI QO'SHIB BO'LMAYDI!!!!!!
# #sonni matnga o'tqazamiz - str() orqali
# ism = "Jonibek"
# yosh = 21
# yosh =str(yosh)
# #xabar = ism + ' ' + yosh + ' yoshda'
# #print(xabar) # J: Jonibek 21 yoshda

# #print(xabar + 10 ) #TypeError: can only concatenate str (not "int") to str
# xabar = ism + ' ' + str(yosh) + ' yoshda'
# print(xabar) #J:Jonibek 21 yoshda

# t_yil = int(input("Tug'ilgan yilizni kiriting: "))
# yosh = 2021 - t_yil
# print("Siz ",str(yosh)," yoshda ekansiz") # J:Siz  20  yoshda ekansiz
#      int()      )
#      float()    } sulardan foydalanib malumotlarni bir turda
#      str()      )         ikinchisiga o'tqazishimiz munkin
# AMALIYOT
# #Foydalanuvchi kiritgan sonning kvadrati va kubini konsolga chiqaruvchi dastur
# son = input("Istalgan son kiriting:\n")
# son = int(son)
# kvad_son = son**2
# kub_son = son**3
# print(son, 'ning kvadrati',kvad_son, "ga teng")
# print(son, 'ning kubi',kub_son, "ga teng")
# # J: Istalgan son kiriting:
# # 45
# # 45 ning kvadrati 2025 ga teng
# # 45 ning kubi 91125 ga teng
   # II-usul
   # x = int(input("Istalgan son kiriting:\n>>>"))
   # print(x, " ning kvadrati ", x**2, " ga teng")
   # print(x, " ning kubi ", x**3, " ga teng")
# #Foydalanuvchining yoshini so'rab, uning tug'ilgan yilini hisoblab, konsolga chiqaruvchi dastur
# yosh = input("Yoshingiz nechida?\n")
# yosh = int(yosh)
# t_yil = 2021-yosh
# print("Siz",t_yil,"da tug'ilgansiz")
# # Foydalanuvchidan ikki son kiritshni so'rab, kiritilgan 
# #sonlarning yig'indisi, ayirmasi, ko'paytmasi va bo'linmasini chiqaruvchi dastur
# bir_son = input("Birinchi sonni kiriting: ")
# bir_son = float(bir_son)
# ikki_son = input("Ikinchi sonni kiriting: ")
# ikki_son = float(ikki_son)
# print(bir_son,'+',ikki_son,'=',bir_son + ikki_son)
# print(bir_son,'-',ikki_son,'=',bir_son - ikki_son)
# print(bir_son,'*',ikki_son,'=',bir_son * ikki_son)
# print(bir_son,'/',ikki_son,'=',bir_son / ikki_son)
# #J:Birinchi sonni kiriting: 25
# # Ikinchi sonni kiriting: 15
# # 25.0 + 15.0 = 40.0
# # 25.0 - 15.0 = 10.0
# # 25.0 * 15.0 = 375.0
# # 25.0 / 15.0 = 1.6666666666666667
# II-usul:
    # a = float(input("Birinchi sonni kiriting: "))
    # b = float(input("Ikkinchi sonni kiriting: "))
    # print(f"{a}+{b}=", a+b)
    # print(f"{a}-{b}=", a-b)
    # print(f"{a}x{b}=", a*b)
    # print(f"{a}/{b}=", a/b)
"""
  25.11.2021  20:05 (21:10)
  07-dars.LIST (RO'YXAT(cписок))
"""
# mevalar = ['olma','anor','banan',"qovun"]
# print(mevalar) #J:['olma', 'anor', 'banan', 'qovun']
# narhlar = [25000,53.45555, 30000,50000,60000,-30,5,100]
# print(narhlar) #J:[25000, 53.45555, 30000, 50000, 60000, -30, 5, 100]
# sonlar = ['bir','ikki',15,-60,60000,0.999,1999]
# print(sonlar) #J:['bir', 'ikki', 15, -60, 60000, 0.999, 1999]
# ismlar = []
# print(ismlar) #[]

# print(mevalar[2]) #J:banan
# print(mevalar[-1]) #J:qovun
# print(mevalar[0].upper()) #J:OLMA

# print(narhlar[0]+narhlar[1]-15000+60000) #J:70053.45555

# mevalar[0] ='limon'
# print(mevalar) #J:['limon', 'anor', 'banan', 'qovun']
 # .append() -- ro'yxatni ohiriga qo'shadi
#mevalar.append('tavuz')
#print(mevalar) #J:['limon', 'anor', 'banan', 'qovun', 'tavuz']
 # .insert() - qayerda qo'shmoqchi biza va + indeksini kiritamiz
# mevalar.insert(6, 'nok') 
# print(mevalar) #J:['limon', 'anor', 'banan', 'qovun', 'tavuz', 'nok']

# cars = []
# cars.append('nexia')  
# cars.append('damas')  
# cars.insert(2,'lasetii')
# print(cars) #J:['nexia', 'damas', 'lasetii']
 #del cars[] - operator qaysi dur elementni uchirib tashlash uchun
# del cars[2]
# print(cars) #J:['nexia', 'damas']
# cars.insert(0,'captiva')
 # cars.remove("____") - Agar o'chiradigan ro'yxatimizdagi 
 #indexni bilmasak(faqatgina birinchsini uchiradi)
# cars.remove("damas")
# print(cars) #J:['captiva', 'nexia']
 # o'zg1 = o'zg2.pop(indexsi) -- o'zgaruvchining birinchisidan
 # olib ikinchisiga qo'shadi(indexsiz oxirgisini oladi)
# bozorlik = ['un', "yog'",'sabzi',"tuxum",'non']
# ukamga = bozorlik.pop(3)
# print(ukamga) #J:tuxum
# print(bozorlik) #J: ['un', "yog'", 'sabzi', 'non']
# singlimga = bozorlik.pop()
# print(singlimga) #J: non
 
# AMALIYOT
 # ismlar degan ro'yxat yarating va kamida 3 ta yaqin do'stingizning ismini kiriting
# ismlar = ['Mirshod','Shahboz','Sherzod','Amal']
 # Ro'yxatdagi har bir do'stingizga qisqa xabar yozib konsolga chiqaring: 
# print(f"Do'stlarim, {ismlar[0]} va {ismlar[1]} yaxshi yuribsizlarmi?")
# print("Assalomu aleykum" + ' ' + ismlar[2],"ko'rinmaysan do'stim")
# print(ismlar[-1],"sen qayerdasan hozir")
 #J:Do'stlarim, Mirshod va Shahboz yaxshi yuribsizlarmi?
 # Assalomu aleykum Sherzod ko'rinmaysan do'stim
 # Amal sen qayerdasan hozir 
 
 # sonlar deb nomlangan ro'yxat yarating va ichiga turli 
   #sonlarni yuklang (musbat, manfiy, butun, o'nlik)
# sonlar = [9000, 5000, -456, 940.56445, -100, 1_789_788_111]
# print(sonlar)
 # Yuqoridagi ro'yxatdagi sonlar ustida turli arifmetik amallar bajarib ko'ring. 
  # Ro'yxatdagi ba'zi sonlarning qiymatini o'zgartiring, ba'zilarini esa almashtiring.    
# print(sonlar[2] + sonlar[0]-sonlar[1])
# sonlar[3] = 2000 + sonlar[0]
# sonlar[4] = 1981
# print(sonlar)
# del sonlar[5]
# print(sonlar[3]-sonlar[4])
# print(sonlar)
# J:[9000, 5000, -456, 940.56445, -100, 1789788111]
# 3544
# [9000, 5000, -456, 11000, 1981, 1789788111]
# 9019
# [9000, 5000, -456, 11000, 1981]
 # t_shaxslar va z_shaxslar degan 2 ta ro'yxat yarating va biriga 
  #o'zingiz eng ko'p hurmat qilgan tarixiy shaxslarning, ikkinchisiga 
  #esa zamonamizdagi tirik bo'lgan shaxslarning ismini kiriting. 
# t_shaxslar = ['Navoiy','Bobur','Temur']
# z_shaxslar = ['Islom','Shavkat','Yulduz']
  # Yuqoridagi ro'yxatlarning har biridan bittadan qiymatni sug'urib olib 
    #(.pop()), quyidagi ko'rinishda chiqaring:
# print(f"\nMen tarixiy shaxslardan {t_shaxslar.pop(0)} bilan,\n\
# zamonaviy shaxslardan {z_shaxslar.pop(1)} bilan\n\
# suhbat qilishni istar edim\n")        
# J:Men tarixiy shaxslardan Navoiy bilan,
# zamonaviy shaxslardan Shavkat bilan
# suhbat qilishni istar edim
  # friends nomli bo'sh ro'yxat tuzing va unga .append() yordamida 5-6 ta
  #  mehmonga chaqirmoqchi bo'lgan do'stlaringizni kiriting. 
# friends = []
# friends.append('Akhror')
# friends.append('Shuxrat')
# friends.append('Jasur')
# friends.append('Kuvonch')
# friends.append('sherali')
# friends.append('Firdavs')
# print(friends) #J:['Akhror', 'Shuxrat', 'Jasur', 'Kuvonch', 'sherali', 'Firdavs']
  #Yuqoridagi ro'yxatdan mehmonga kela olmaydigan odamlarni .remove() metodi yordamida o'chrib tashlang. 
# friends.remove("Jasur")
# friends.remove("Shuxrat")  
# print(friends) #J: ['Akhror', 'Kuvonch', 'sherali', 'Firdavs']
  # Ro'yxatning oxiriga, boshiga va o'rtasiga yangi ismlar qo'shing.
# friends.append('Jonibek')
# friends.insert(0, 'Johon')
# friends.insert(2, 'Jamol')
# print(friends) #J: ['Johon', 'Akhror', 'Jamol', 'Kuvonch', 'sherali', 'Firdavs', 'Jonibek']
  # Yangi mehmonlar deb nomlangan bo'sh ro'yxat yarating. 
  # .pop() va .append() metodlari yordamida mehmonga kelgan do'stlaringizning 
  # ismini friends ro'yxatidan sug'urib olib, mehmonlar ro'yxatiga qo'shing.
# print(friends) #J:['Akhror', 'Shuxrat', 'Jasur', 'Kuvonch', 'sherali', 'Firdavs']
# mehmonlar = []
# mehmonlar.append(friends.pop(0))
# mehmonlar.append(friends.pop(3))
# mehmonlar.append(friends.pop(-1))
# print('Kelgam mehmonlar: ', mehmonlar) 
#J: Kelgam mehmonlar:  ['Akhror', 'sherali', 'Firdavs']

"""
     26.11.2021 8:30 (Cуботта)
    08-dars.RO'YXATLAR BILAN ISHLASH
"""     
# o'zg.sort() -  Tartiblash ro'yxatni, ot A - z 
# cars = ["cobalt", "nexia", "djentra", "captiva", 'matiz',\
# 'damas', 'tiko', 'spark', 'audi', 'bmw']
# print(cars)    
# cars.sort()
# print(cars) 
# #J:['audi', 'bmw', 'captiva', 'cobalt', 'damas', 'djentra', 'matiz', 'nexia', 'spark', 'tiko'] 

#     # o'zg.sort(reverse=True) --  z - A reskari ro'yxat
# cars.sort(reverse = True)
# print (cars)
# # J: ['tiko', 'spark', 'nexia', 'matiz', 'djentra', 'damas', 'cobalt', 'captiva', 'bmw', 'audi']   
#    # sorted()
# cars = ['tiko', 'spark', 'nexia', 'matiz', 'djentra', 'damas', 'cobalt', 'captiva', 'bmw', 'audi']
# print(sorted(cars))
# # J: ['audi', 'bmw', 'captiva', 'cobalt', 'damas', 'djentra', 'matiz', 'nexia', 'spark', 'tiko']
# print(cars) #J: ['tiko', 'spark', 'nexia', 'matiz', 'djentra', 'damas', 'cobalt', 'captiva', 'bmw', 'audi']
# print(sorted(cars, reverse = True))  #??????
 
# sonlar = [12, 45, 2, 999, -7, -7.2, 0.15]
# print(sorted(sonlar)) #J: [-7.2, -7, 0.15, 2, 12, 45, 999]
# print(sonlar) # [12, 45, 2, 999, -7, -7.2, 0.15]
# sonlar.sort()
# print(sonlar) # [-7.2, -7, 0.15, 2, 12, 45, 999]
# sonlar.sort(reverse=True) 
# print(sonlar) # [999, 45, 12, 2, 0.15, -7, -7.2]

# sonlar.reverse()
# print(sonlar) # [-7.2, -7, 0.15, 2, 12, 45, 999]

# # len() - length uzunligini bilish ro'yxatni
# print(len(cars))  # 10
# print(len(sonlar))  # 7

# # range(m , n) yoki range(m, n, k-шаг), max(o'zg), min(o'zg), sum(o'zg)
# sonlar = list(range(0, 9))
# print(sonlar) # [0, 1, 2, 3, 4, 5, 6, 7, 8]
# t_sonlar = list(range(1, 11, 2))
# print(t_sonlar) # [1, 3, 5, 7, 9]
# max_qiymat = max(sonlar)
# print(max_qiymat) # 8
# print(max(sonlar)) # 8
# print(min(t_sonlar)) # 1
# summa = sum(sonlar)
# print(summa) # 36
# print(sum(sonlar)) # 36
#  # Ro'yxatni kisish (ajratib olish)
# cars = ['tiko', 'spark', 'nexia', 'matiz', 'djentra', 'damas', 'cobalt', 'captiva', 'bmw', 'audi']
# print(cars[1:6]) # ['spark', 'nexia', 'matiz', 'djentra', 'damas']
# print(cars[0:6]) # ['tiko', 'spark', 'nexia', 'matiz', 'djentra', 'damas']
# print(cars[6:]) #  ['cobalt', 'captiva', 'bmw', 'audi']
#  # Ro'yxatdan nusxa olish
# cars = ['tiko', 'spark', 'nexia', 'matiz', 'djentra', 'damas', 'cobalt', 'captiva', 'bmw', 'audi']
# my_cars = cars[ : ]  
# print(my_cars) # ['tiko', 'spark', 'nexia', 'matiz', 'djentra', 'damas', 'cobalt', 'captiva', 'bmw', 'audi']
# my_cars.remove('tiko')
# print(my_cars) # ['spark', 'nexia', 'matiz', 'djentra', 'damas', 'cobalt', 'captiva', 'bmw', 'audi']
# print(cars) # ['tiko', 'spark', 'nexia', 'matiz', 'djentra', 'damas', 'cobalt', 'captiva', 'bmw', 'audi']
#   # TUPlE - o'zgarmas ro'yxat -- (____)
# toys = ('bear', 'boll', 'car','bus')
# print(toys[1])  # boll 
# print(toys[ : 2]) # ('bear', 'boll')
#toys [0] = 'teddy' # TypeError: 'tuple' object does not support item assignment
# toys.append('teddy') # AttributeError: 'tuple' object has no attribute 'append'

# toys = list(toys)
# print(type(toys)) # <class 'list'>
# toys.append('teddy')
# print(toys) # ['bear', 'boll', 'car', 'bus', 'teddy']
# toys = tuple(toys)
# print(type(toys)) #
 
# # AMALIYOT
# # O'zingizga ma'lum davlatlarning ro'yxatini tuzing va ro'yxatni konsolga chiqaring
# davlatlar = ['Maskava', 'Amerika', 'Qozoxston', "O'zbekiston" ]
# print(davlatlar) # ['Maskava', 'Amerika', 'Qozoxston', "O'zbekiston"]
# # Ro'yxatning uzunligini konsolga chiqaring
# print(len(davlatlar))  # 4
# # sorted() funktsiyasi yordamida ro'yxatni tartiblangan holda konsolga chiqaring
# print(sorted(davlatlar)) # ['Amerika', 'Maskava', "O'zbekiston", 'Qozoxston']
# # sorted() yordamida ro'yxatni teskari tartibda konsolga chiqaring
# print(sorted(davlatlar, reverse=True)) # ['Qozoxston', "O'zbekiston", 'Maskava', 'Amerika']
# # Asl ro'yxatni qaytadan konsolga chiqaring
# print(davlatlar) # ['Maskava', 'Amerika', 'Qozoxston', "O'zbekiston"]
# # reverse() metodi yordamida ro'yxatni ortidan boshlab chiqaring
# davlatlar.reverse()
# print(davlatlar) # ["O'zbekiston", 'Qozoxston', 'Amerika', 'Maskava']
# # sort() metodi yordamida ro'yxatni avval alifbo bo'yicha, keyin esa alifboga teskari tartibda konsolga chiqaring.
# davlatlar.sort()
# print(davlatlar) # ['Amerika', 'Maskava', "O'zbekiston", 'Qozoxston']
# davlatlar.sort(reverse=True)
# print(davlatlar) # ['Qozoxston', "O'zbekiston", 'Maskava', 'Amerika']
# # 120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzing
# juft_sonlar = list(range(120, 1200, 2))
# print(juft_sonlar) # [120, 122, 124, ....... ,1198, 1200]
# # Ro'yxatdagi sonlar yig'indisini hisoblang va konsolga chiqaring
# print(sum(juft_sonlar)) # 355860
# # Ro'yxatdagi eng katta va eng kichik son o'rtasidagi ayirmani hisoblang va konsolga chiqaring
# min_son = min(juft_sonlar)
# max_son = max(juft_sonlar)
# print(max_son - min_son) # 1078 
# ##yoki### print(max(juft_sonlar)-min(juft_sonlar))
# # Ro'yxatdagi elementlar sonini hisoblang
# print(len(juft_sonlar)) # 540
# # Ro'yxatning boshidan, o'rtasidan va oxiridan 20 ta qiymatni konsolga chiqaring
# print(juft_sonlar[ :20]) 
#  # [120, 122, 124, 126, 128, 130, 132, 134, 136, 138, 140, 142, 144, 146, 148, 150, 152, 154, 156, 158]
# print(juft_sonlar[520: ]) 
# ##yoki### print(sonlar[-20:]) 
#  # [1160, 1162, 1164, 1166, 1168, 1170, 1172, 1174, 1176, 1178, 1180, 1182, 1184, 1186, 1188, 1190, 1192, 1194, 1196, 1198]
# print(juft_sonlar[510:530])  
#  # [1140, 1142, 1144, 1146, 1148, 1150, 1152, 1154, 1156, 1158, 1160, 1162, 1164, 1166, 1168, 1170, 1172, 1174, 1176, 1178]
# # taomlar degan ro'yxat yarating va ichiga istalgan 5ta taomni kiriting
# taomlar = ['osh', 'somsa', 'mastava', 'norin', 'shurva']
# # nonushta degan yangi ro'yxatga taomlardan nusxa oling
# nonushta = taomlar[ : ]
# print(nonushta) # ['osh', 'somsa', 'mastava', 'norin', 'shurva']
# # Yangi ro'yxatda faqat nonushtaga yeyiladigan taomlarni qoldiring, va qo'shimcha 2 ta taom qo'shing
# nonushta_2 = taomlar[0 : 3]
# nonushta_2.append('qovurma')
# nonushta_2.append('halisa')
# print(nonushta_2) # ['osh', 'somsa', 'mastava', 'qovurma', 'halisa']
# # Yuqoridagi nonushta ro'yxatini o'zgarmas ro'yxatga aylantiring va nonushta[0] = "qaymoq va non" deb qiymat berib ko'ring.
# nonushta_2 = tuple(nonushta_2)
# print(nonushta_2) # ('osh', 'somsa', 'mastava', 'qovurma', 'halisa')
# nonushta_2 = list(nonushta_2)
# nonushta_2[0] = "qaymog va non"
# nonushta_2.remove('qovurma') 
# nonushta_2[1] = 'sut'
# nonushta_2.append('asal')
# nonushta_2 = tuple(nonushta_2)
# print(nonushta_2) # ('qaymog va non', 'sut', 'mastava', 'halisa', 'asal')
# nonushta_2[2] = 'kofe'  # TypeError: 'tuple' object does not support item assignment
"""
     27.11.2021     23:13
     09-dars. FOR TAKRORLASH OPERATORI (for -- uchun)
"""
# mehmonlar = ['Hasan','Alisher','Mirshod','Shahboz']
# print('Salom', mehmonlar[0]) #Salom Hasan
# print('Salom', mehmonlar[1]) #Salom Alisher
# print('Salom', mehmonlar[2]) #Salom Mirshod
# print('Salom', mehmonlar[3]) #Salom Shahboz
# for mehmon in mehmonlar :
#     print('Salom', mehmon) 
#     # Salom Hasan
#     # Salom Alisher
#     # Salom Mirshod
#     # Salom Shahboz
#     # Цыкл  to ro'yxatimizdagi ismlar tugamagunicha toxtamaydi
#     print('Hayr,',mehmon)
#     # Salom Hasan
#     # Hayr, Hasan
#     # Salom Alisher
#     # Hayr, Alisher
#     # Salom Mirshod
#     # Hayr, Mirshod
#     # Salom Shahboz
#     # Hayr, Shahboz
# for mehmon in mehmonlar:
#     print(f"Hurmatli {mehmon} sizni 26-dekabr kuni '____'baxt tuyiga taklif qilamiz ")
#     print('Hurmat bilan Qayumovlar oilasi')
#     #Hurmatli Hasan sizni 26-dekabr kuni '____'baxt tuyiga taklif qilamiz 
#     # Hurmat bilan Qayumovlar oilasi
#     # Hurmatli Alisher sizni 26-dekabr kuni '____'baxt tuyiga taklif qilamiz 
#     # Hurmat bilan Qayumovlar oilasi
#     # Hurmatli Mirshod sizni 26-dekabr kuni '____'baxt tuyiga taklif qilamiz 
#     # Hurmat bilan Qayumovlar oilasi
#     # Hurmatli Shahboz sizni 26-dekabr kuni '____'baxt tuyiga taklif qilamiz 
#     # Hurmat bilan Qayumovlar oilasi
# sonlar = list(range(1,11))
# for son in sonlar:
#     print(f"{son} ning kvadrati {son**2} ga teng")
#     # 1 ning kvadrati 1 ga teng
#     # 2 ning kvadrati 4 ga teng
#     # 3 ning kvadrati 9 ga teng
#     # 4 ning kvadrati 16 ga teng
#     # 5 ning kvadrati 25 ga teng
#     # 6 ning kvadrati 36 ga teng
#     # 7 ning kvadrati 49 ga teng
#     # 8 ning kvadrati 64 ga teng
#     # 9 ning kvadrati 81 ga teng
#     # 10 ning kvadrati 100 ga teng
# sonlar = list(range(11))
# sonlar_kvad = []
# for son in sonlar:
#     sonlar_kvad.append(son**2)
# print(sonlar) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(sonlar_kvad) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
  
# dostlar = []
# print("5 ta eng yaqin do'stingiz kim?")
# for n in range(5):
#     dostlar.append(input(f"{n+1} chi do'stingizni ismini kiriting: "))
# print(dostlar)   
# # 5 ta eng yaqin do'stingiz kim?
# 1 chi do'stingizni ismini kiriting: Shahboz
# 2 chi do'stingizni ismini kiriting: Mirshod
# 3 chi do'stingizni ismini kiriting: Sherzod
# 4 chi do'stingizni ismini kiriting: Ali
# 5 chi do'stingizni ismini kiriting: Vali
# ['Shahboz', 'Mirshod', 'Sherzod', 'Ali', 'Vali']
 
 # AMALIYOT
# Kamida 5 elementdan iborat ismlar degan ro'yxat tuzing, va ro'yxatdagi har bir ismga takrorlanuvchi xabar yozing    
# ismlar = ['Jonikek', 'Ibrohim','Akhror','Jasur','Shuxrat']
# for ism in ismlar:
#    print(f"Assalomu aleykum, {ism}")
    # Assalomu aleykum, Jonikek
    # Assalomu aleykum, Ibrohim
    # Assalomu aleykum, Akhror
    # Assalomu aleykum, Jasur
    # Assalomu aleykum, Shuxrat
#Yuoqirdagi tsikl tugaganidan so'ng, ekranga "Kod n marta takrorlandi" degan xabarni chiqaring (n o'rniga kod necha marta takrorlanganini yozing)
# print(f"Kod {len(ismlar)} martta takrorlanadi") # Kod 5 martta takrorlanadi
# # 10 dan 100 gacha bo'lgan toq sonlar ro'yxatini tuzing. Ro'yxatning xar bir elementining kubini yangi qatordan konsolga chiqaring.
# toq_sonlar = (range(11,100,2))
# for son in toq_sonlar:
#     print(f"{son} ning kubi {son**3} ga teng")
#     # 11 ning kubi 1331 ga teng
#     # 13 ning kubi 2197 ga teng
#     # 15 ning kubi 3375 ga ten
#     # ....
# # Foydalanuvchidan 5 ta eng sevimli kinolarini kiritshni so'rang, va kinolar degan ro'yxatga saqlab oling. Natijani konsolga chiqaring.    
# kinolar = [] 
# print("5ta eng sevgan kitobizni kiriting")
# for k in range(5):
#     kinolar.append(input(f"{k+1} - kino:"))
# print(kinolar) # [' AAAA', 'aaaaa', 'aaaaa', 'asasa', 'asasa']
# Foydalanuvchidan bugun nechta odam bilan uchrashganini (suhbatlashganini) so'rang, va har bir suhbatlashgan odamning ismini birma-bir so'rab ro'yxatga yozing. Ro'yxatni konsolga chiqaring.
# n = int(input('Bugun necha kishi bilan uchrashdingiz?>>> ' ))    
# ismlar = []
# for ism in range(0,n):
#     ismlar.append(input(f"{ism+1}-kishini ismini kiriting: "))
# print(ismlar) # ['Mirshod', 'Axror', 'Ibrohim']      



 







     







