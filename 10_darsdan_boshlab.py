"""
   29.11.2021  17:40
 10 - dars. IF-ELSE (tarmoqlash -- agar-aks holda)
"""
# autolar = ['audi','gm','bmw','volvo','kia','tesla']
# #for auto in autolar:
#     #print(auto.title())
#     # Audi
#     # Gm           GM
#     # Bmw          BMW     (katta harf bo'lishi kerak)
#     # Volvo
#     # Kia
#     # Tesla
#  # " == " -- "tengmi" degani 
# for auto in autolar:
#     if auto == "bmw" or auto =='gm':
#         print(auto.upper())
#     else:
#         print(auto.title())
#         # Audi
#         # GM
#         # BMW
#         # Volvo
#         # Kia
#         # Tesla
# ism = 'Jonik'
# # ism =='jonik'
# # Out[9]: False
# # ism.lower() =='jonik'
# # Out[10]: True         
 
#   # " != " -- "teng emas"mi
# ism =input("Ismingiz nima?\n>>>")
# if ism.lower() != "ali":
#    print(f"Uzur {ism.title()} biz Alini kutyapmiz")
# else:
#     print("Salom, Ali")

# javob = float(input("12x6 nechiga teng?>>>"))
# if javob != 12*6:
#     print('Javob xato')
#     # 12x6 nechiga teng?>>>74
#     # Javob xato
    
# yosh = int(input("Yoshingiz nechida?>>>"))
# if yosh >=18: #katta yoki tengmi
#     print('Yush kilibsiz')
# else:
#     print('Kirish munkin emas')
#     # Yoshingiz nechida?>>>2555
#     # Yush kilibsiz

# login = input("Yangi login kiriting:\n")
# if len(login) <=5:
#     print("Login 5ta harfdan ko'proq bo'lishi shart!")
#     # Yangi login kiriting:
#     # jonik
#     # Login 5ta harfdan ko'proq bo'lishi shart!

# yil = int(input("Tug'ilgan yilizni kiriting:>>>"))
# if 2021-yil<=18:
#     print(f"Yoshingiz {2021-yil}da ekan")
#     print('Sizga kirish munkin emas')
# else:
#     print('Xush kelibsiz!')
#     # Tug'ilgan yilizni kiriting:>>>2000
#     # Xush kelibsiz!
    
# yosh = int(input("Yoshingiz nichida?>>>"))
# if yosh > 65: print('Siz COVID-19 risk guruxida ekansiz')
# #   Yoshingiz nichida?>>>70
# # Siz COVID-19 risk guruxida ekansiz
  
# x, y =20, 40
# print('x>y') if x>y else print('x<y') # x<y


# AMALIYOT
# Yangi cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia'] degan ro'yxat tuzing, 
# ro'yxat elementlarining birinchi harfini katta qilib konsolga chqaring. 
# GM uchun ikkala harfni katta qiling.
# cars = ['toyota','mazda','hyundai','gm',"kia"]
# for car in cars:
#     if car == "gm":
#         print(car.upper())
#     else:
#         print(car.title())
# Toyota
# Mazda
# Hyundai
# GM
# Kia              

# Yuqoridagi mashqni teng emas (!=) operatori yordamida bajaring. 
# for car in cars:
#     if car != "gm":
#          print(car.title())
#     else:
#          print(car.upper())              
# Toyota
# Mazda
# Hyundai
# GM
# Kia    

# Foydalanuvchi login ismini so'rang. Agar login admin bo'lsa, 
# "Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?" xabarini konsolga chiqaring. 
# Aks holda, "Xush kelibsiz, {foydalanuvchi_ismi}!" matnini konsolga chiqaring.
# login = input("Iltimos loginni kiriting:>>>")
# if  login.lower() == "admin":
#     print(f"Xush kelibsiz, {login.title()}. Foydalanuvchilar ro'yxatini ko'rasizmi?")
# else:
    # print(f"Xush kelibsiz, {login.title()}!")
# Iltimos loginni kiriting:>>>jonik
# Xush kelibsiz, Jonik!

# Iltimos loginni kiriting:>>>ADMIn
# Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?

# Foydalanuvchidan 2 ta son kiritishni so'rang. Agar ikki son bir-biriga teng bo'lsa, 
#"Sonlar teng" ekan degan yozuvni konsolga chiqaring.
# x = float(input("Birinchi sonni kiriting:"))
# y = float(input("Ikkinchi sonni kiriting:"))
# if x == y: print(f"Sonlar teng ekan: {x}={y}")
# Ikkinchi sonni kiriting:15
# Sonlar teng ekan: 15.0=15.0

# Foydalanuvchidan istalgan son kiritishni so'rang. Agar son manfiy bo'lsa konsolga 
# "Manfiy son", agar musbat bo'lsa "Musbat son" degan xabarni chiqaring. 
#1) son = float(input("Istalgan sonni kiriting:"))
# if son<0:
#     print(f"{son} 'Manfiy son'")
# else:
#     print(f"{son} 'Mushbat son'")
# Istalgan sonni kiriting:15
# 15.0 'Mushbat son'
#2) son = float(input("Istalgan son kiriting:"))
# print("Son manfiy") if son<0 else print("Son musbat") 
# Istalgan son kiriting:-60000
# Son manfiy

# Foydalanuvchidan son kiritishni so'rang, agar son musbat bo'lsa uning 
# ildizini hisoblab konsolga chiqaring. Agar son manfiy bo'lsa, 
# "Musbat son kiriting" degan xabarni chiqaring. 

#son = float(input("Son kiriting: "))
# if son > 0:
#     print(f"{int(son)} ning ildizi {son**(1/2)}ga teng")
# else:
#     print("Musbat son kiriting")
    # Son kiriting: 500
    # 500 ning ildizi 22.360679774997898ga teng
#print(son**(1/2)) if son>0 else print("Musbat son kiriting")
    # Son kiriting: 15
    # 3.872983346207417

"""
30.11.2021  21:21
11-dars. BIR NECHTA SHARTLARNI TEKSHIRISH
if-elif-else zanjiri, "and", "or" operatorlari bilan tanishamiz
 
"""    
# elif - aks holda,agar -if va else operatorlar yig'indisi 
# yosh = int(input("Yoshingiz nichida? "))
# if yosh<=4:
#     print("Sizga kirish bepul")
# elif yosh<=12:
#     print('Sizga kirish 5000 so\'m')
# else:
#     print('Sizga kirish 10000 so\'m')
#     # Yoshingiz nichida? 12
#     # Sizga kirish 5000 so'm
    
# # ('elif' istalgancha bo'lishi munkin, Цыкл ичида )
# yosh = int(input("Yoshingiz nichida? "))
# if yosh<=4:
#     narh = 0    
# elif yosh<=12:
#     narh = 5000
# elif yosh<=18:
#     narh = 8000
# else:
#     narh = 10000
# print(f"Sizga kirish {narh} so'm")    
# # Yoshingiz nichida? 10
# # Sizga kirish 5000 so'm

# # or - yoki, and - va | operatorlari
# kun = input("Bigun nima kun?>>>")
# if kun.lower() == 'shanba' or kun.lower()=='yakshanba':
#     print("Bugun dam olish kuni")
# else:
#     print("Bugun ish kuni")
# Bigun nima kun?>>>YAkshanba
# Bugun dam olish kuni    
# kun = input("Bugun nima kun? ")
# harorat = float(input("Havoning harorati qanday? "))
# if kun.lower() == 'yakshanba' and harorat>=30:
#     print("Cho'milgani ketdik! ")
# elif kun.lower() =="yakshanba" and harorat <=30:
#     print('Uyda dam qolamiz!')
#     # Bugun nima kun? yakshanba
#     # Havoning harorati qanday? 25
#     # Uyda dam olamiz!

# kun = input("Bugun nima kun? ")
# harorat = float(input("Havoning harorati qanday? "))
# if (kun.lower() == 'shanba' or kun.lower()=='yakshanba') and harorat>=30:
#     print("Cho'milgani ketdik! ")
# elif (kun.lower() == 'shanba' or kun.lower()=='yakshanba') and harorat <=30:
#     print('Uyda dam qolamiz!')    
# Bugun nima kun? shanba
# Havoning harorati qanday? 45
# Cho'milgani ketdik!
     
 # BOOLEAN -- malumot turi 
# osh =15000
# choy = True
# salat = False
# if choy and salat:
#     narh = osh + 2*5000
# elif choy or salat:    
#     narh = osh + 5000
# print(f"Jami {narh} so'm")  # Jami 20000 so'm
 
# taom = 15000
# non = True #1
# asarti = False #0
# salat = False #0
# choy = True #1
# kompot = True #1
# if choy:
#     print('Mijoz choy oldi.')
#     narh = taom + 2000
# if salat:
#     print("Mijoz salat olda.")
#     narh = taom +3000
# if non:
#     print("Mijoz non oldi.")
#     narh = taom +2000
# if kompot:
#     print("Mijoz kompot oldi.")
#     narh = taom +3000
# if asarti:
#     print("Mijoz asarti oldi.")
#     narh = taom + 5000
# print(f"Jammi {narh} bo'ldi")    
# # Mijoz choy oldi.
# # Mijoz non oldi.
# # Mijoz kompot oldi.
# # Jammi 18000 bo'ldi
  
#   # in -- operatori (malum bir matnni ro'yxatta bormi yokligini bilishimiz munkin)
# # menu = ["osh", 'somsa',"shashklik", "norin",'kozonkabob']
# # 'manti' in menu # menu da manti bormi?   
# # Out[16]: False
# # 'somsa' in menu
# # Out[17]: True

# menu = ["osh", 'somsa',"shashlik", "norin",'kozonkabob']
# ovqat = input('Nima ovqat yeysiz?>>> ')
# if ovqat.lower() in menu:
#     print("Buyurtma qabul qilindi.")
# else:
#     print('Afsuski bizda bunday ovqat yo\'q')    
# Nima ovqat yeysiz?>>> norin
# Buyurtma qabul qilindi.
   
  # not in
# menu = ["osh", 'somsa',"shashlik", "norin",'kozonkabob']
# ovqat = input('Nima ovqat yeysiz?>>> ')
# if ovqat.lower() not in menu:
#     print('Afsuski bizda bunday ovqat yo\'q')
# else:
#     print("Buyurtma qabul qilindi.")
# Nima ovqat yeysiz?>>> sho'rva
# Afsuski bizda bunday ovqat yo'q

# menu = ['osh','qozonkabob','shashlik','norin','somsa']
# buyurtmalar = ['somsa', 'norin',"shorva",'sabzi']
# for taom in buyurtmalar:
#     if  taom in menu:
#         print(f"Menuda {taom} bor")
#     else:
#         print(f"Kechirasiz, menuda {taom} yoq")
#         # Menuda somsa bor
#         # Menuda norin bor
#         # Kechirasiz, menuda shorva yoq
#         # Kechirasiz, menuda sabzi yoq

# if buyurtmalar:
#     print(f"Buyurtmayizda {len(buyurtmalar)} ta taom bor")
# else:
#     print("Ro'yxat bo'sh")    
#     # Buyurtmayizda 4 ta taom bor
    
# menu = ['osh','qozonkabob','shashlik','norin','somsa']
# buyurtmalar = []
# if buyurtmalar:
#     for taom in buyurtmalar:
#          if  taom in menu:
#               print(f"Menuda {taom} bor")
#          else:
#              print(f"Kechirasiz, menuda {taom} yoq")
# else:             
#     print("Ro'yxat bo'sh")    # Ro'yxat bo'sh
    
# AMALIYOT
# Foydalanuvchidan juft son kiritishni so'rang. Agar foydalanuvchi juft son kiritsa "Rahmat!", 
# agar toq son kiritsa "Bu son juft emas" degan xabarni chiqaring.    
# son = float(input("Juft son kiriting:>>> "))
# if son%2:
#     print("Bu son juft emas")
# else:
#     print('Rahmat!')
# Juft son kiriting:>>> 55
# Bu son juft emas    

# Foydalanuvchi yoshini so'rang, va muzeyga kirish uchun chipta narhini quyidagicha chiqaring:
# Agar foydalanuvchi 4 yoshdan kichkina yoki 60 dan katta bo'lsa bepul
# Agar foydalanuvchi 18 dan kichik bo'lsa 10000 so'm
# Agar foydalanuvchi 18 dan katta bo'lsa 20000 so'm
# yosh = int(input("Necha yosh siz?>>>"))
# if yosh <=4 or yosh>=60:
#     narh = 0
# elif yosh <18:
#     narh = 10000
# else: 
#     narh = 20000
# print(f"Sizga kirish {narh} so'm")    

# Foydalanuvchidan ikita son kiritishni so'rang, sonlarni solishtiring va ularning teng 
# yoki katta/kichikligi haqida xabarni chiqaring
# x = float(input("1-sonni kiriting:>>>"))
# y = float(input("2-sonni kiriting:>>>"))
# if x == y:
#     solish = "="
# elif x > y:
#     solish = ">"
# elif x < y:
#     solish = "<"
# print(f"{x} {solish} {y}")  
# 1-sonni kiriting:>>>1

# 2-sonni kiriting:>>>20
# 1.0 < 20.0  
 # 2-usul
# x = float(input("Birinchi sonni kiriting: "))
# y = float(input("Ikkinchi sonni kiriting: "))
# if x==y:
#     print(f"{x}={y}")
# elif x<y:
#     print(f"{x}<{y}")
# else:
#     print(f"{x}>{y}")    
    
# mahsulotlar degan ro'yxat yarating va kamida 10 ta turli mahsulotni kiriting. 
# Yangi, savat degan bo'sh ro'yxat yarating va foydalanuvchidan savatga kamida 
# 5 ta mahsulot kiritishni so'rang. 
# Savatdagi elementlarni, mahsulotlar ro'yxati bilan solishtiring va 
# qaysi biri ro'yxatda bo'lsa "Mahsulot do'konimizda bor" aks holda, 
# "Mahsulot do'konimizda yo'q" degan xabarlarni chiqaring.
# mahsulotlar = ["sabzi", "kartoshka", "piyoz","pamidor","makaron",
#             "tuxum","go'sht",'bodiring',"guruch","gel"]
# savat = []
# for n in range(5):
#     savat.append(input(f"Savatga {n+1}- mahsulotni qo'shing: "))

# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         print(f"Do'konimizda {mahsulot} bor")
#     else:
#         print(f"Do'konimizda {mahsulot} yo'q")
# Savatga 1- mahsulotni qo'shing: sabzi
# Savatga 2- mahsulotni qo'shing: qovun
# Savatga 3- mahsulotni qo'shing: tarbuz
# Savatga 4- mahsulotni qo'shing: go'sht
# Savatga 5- mahsulotni qo'shing: makaron
# Do'konimizda sabzi bor
# Do'konimizda qovun yo'q
# Do'konimizda tarbuz yo'q
# Do'konimizda go'sht bor
# Do'konimizda makaron bor    

# Yuqoridagi dasturni quyidagicha o'zgartiring: foydalanuvchidan 5 ta mahsulot kiritishni so'rang. 
# Foydalanuvchi so'ragan va do'konda bor mahsulotlarni yangi, bor_mahsulotlar degan 
# ro'yxatga, do'konda yo'q mahsulotlarni esa mavjud_emas degan ro'yxatga qo'shing.  
# Agar mavjud_emas ro'yxati bo'sh bo'lsa, "Siz so'ragan barcha mahsulotlar do'konimizda bor" 
# degan xabarni, aks holda esa "Quyidagi mahsulotlar do'konimizda yo'q: ....." degan xabarni chiqaring.             
# mahsulotlar = ["sabzi", "kartoshka", "piyoz","pamidor","makaron",
#             "tuxum","go'sht",'bodiring',"guruch","gel"]
# savat = []

# for n in range(5):
#     savat.append(input(f"Savatga {n+1}- mahsulotni qo'shing: "))
    
# bor_mahsulotlar = []
# mavjud_emas = []
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_mahsulotlar.append(mahsulot) 
#     else:
#         mavjud_emas.append(mahsulot)

# if len(mavjud_emas) == 0:
#     print("Siz so'ragan barcha mahsulotlar do'konimizda bor")
# else:
#     print(f"Quyidagi mahsulotlar do'konda yoq: {mavjud_emas}")
# # 2-usul
# if mavjud_emas:
#   print(f"Do'konimizda quyidagi mahsulotlar yo'q:")
#   for mahsulot in mavjud_emas:
#     print(mahsulot)
# else:
#   print("Siz so'ragan barcha mahsulotlar do'konimizda bor")
    
# Savatga 1- mahsulotni qo'shing: sabzi
# Savatga 2- mahsulotni qo'shing: go'sht
# Savatga 3- mahsulotni qo'shing: guruch
# Savatga 4- mahsulotni qo'shing: qovun
# Savatga 5- mahsulotni qo'shing: tarbuz
# Quyidagi mahsulotlar do'konda yoq: ['qovun', 'tarbuz']

# Savatga 1- mahsulotni qo'shing: sabzi
# Savatga 2- mahsulotni qo'shing: guruch
# Savatga 3- mahsulotni qo'shing: gel
# Savatga 4- mahsulotni qo'shing: piyoz
# Savatga 5- mahsulotni qo'shing: tuxum
# Siz so'ragan barcha mahsulotlar do'konimizda bor    
    
# foydalanuvchilar degan ro'yxat tuzing, va kamida 5 ta login qo'shing. 
# Foydalanuvchidan yangi login tanlashni so'rang va foydalanuvchi kiritgan 
# loginni foydalanuvchilar degan ro'yxatning tarkibi bilan solishtiring. 
# Agar ro'yxatda bunday login mavjud bo'lsa, "Login band, yangi login tanlang!" 
# aks holda "Xush kelibsiz, foydalanuvchi!" xabarini chiqaring.    
                     
# foydalanuvchilar = ['jonik', 'jonibek7', '5134029', 'joni7', '8626268']
# login = input('Iltimos yangi login kiriting:>>> ')
# if login in foydalanuvchilar :
#     print("Login band, yangi login tanlang!")
# else:
#     print(f"Xush kelibsiz, {login.title()}!")
# Iltimos yangi login kiriting:>>> jamoljon
# Xush kelibsiz, Jamoljon!        
# Iltimos yangi login kiriting:>>> jonik
# Login band, yangi login tanlang!

# Foydalanuvchidan biror butun son kiritishni so'rang. 
# Foydalanuvchi kiritgan sonni 2 dan 10 gacha bo'lgan sonlardan qay biriga 
# qoldiqsiz bo'linishini konsolga chiqaring. 
# son =int(input('Butun son kiriting:>>>'))
# for n in range(2,11):
#     if son % n == 0: # if not (son%n):
#         print(f"{son} soni {n} ga qoldiqsiz bo'linadi")
# Butun son kiriting:>>>5000
# 5000 soni 2 ga qoldiqsiz bo'linadi
# 5000 soni 4 ga qoldiqsiz bo'linadi
# 5000 soni 5 ga qoldiqsiz bo'linadi
# 5000 soni 8 ga qoldiqsiz bo'linadi
# 5000 soni 10 ga qoldiqsiz bo'linadi


















































