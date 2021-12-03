"""
     02.12.2021   19:32
 12-dars. XATOLAR BILAN ISHLASH
Dasturchi xato qiladi. Yaxshi dasturchi esa ko'p xato qiladi.

"""     
# SyntaxError
# print "Hello World!"
# SyntaxError: Missing parentheses in call to 'print'. Did you mean print("Hello World!")?
# print ("Hello World"
# SyntaxError: unexpected EOF(end of fuctuon) while parsing       

#   print("Hello World")
#   ^
# IndentationError: unexpected indent  # kutulmagan joyda bo'sh joy

# print("O'ngacha sanaymiz")
# for n in range(10):
# print(n+1)  # for tsiklini badani buu   # space bosamiz 4x yoki tab
# ^
# IndentationError: expected an indented block # joy tashlamagan siz

# Run time error:
# TypeError
# son = input("Istalgan son kiriting: ") # son = int(son)
# print(f"{son} ning kvadrati {son**2}ga teng")
# # TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
# type(son)
# Out[69]: str
 
# NameError
# prit("Hello World!")  # print
# NameError: name 'prit' is not defined

#ValueError
# son = int(input("Istalgan butun sonkiriting: "))
# if son>=0:
#     print("Musbat son")
# else:
#     print("Manfiy son")
# Istalgan butun sonkiriting: 25.03    #float qiymat bu 25.03
# ValueError: invalid literal for int() with base 10: '25.03'    

#IndexError
# mavalar = ['olma', 'anor', 'uzum']
# print(mavalar[3])
# IndexError: list index out of range # chegarsdan chiqib ketti

#ZeroDevisionError
# x,y =50, 50
# z =250/(x-y)
# ZeroDivisionError: division by zero


# Mantiqiy xatolar
# radius = 5
# pi = 4.14  # 3.14 bo'lishi kerak
# aylana_yuzi = pi*radius**2
# print(aylana_yuzi) # 103.49999999999999: xato pi=3.14

# a =49
# ildiz = 49*1/2  
# print(ildiz) # 24.5: xato 49*(1/2) yoki 49*0.5

# AMALIYOT
# Kodlardagi xatolarni toping va to'g'rilang. 
# Har bir dasturda bir nechta xatolar mavjud bo'lishi mumkin. 
# Xatolarni topish uchun dasturlarni bir necha marta, 
# turli qiymatlar bilan bajarib ko'ring. 
# son = float(input("Juft son kiriting: ")) # XATO: )
# if son%2!=0: # !=
#     print("Bu son juft emas.") # "
# else:
#     print("Rahmat!") # )

# yosh = int(input("Yoshingiz nechida?")) # int
# if yosh<=4 or yosh>=60:
#     narh = 0
# elif yosh < 18: # :
#     narh = 10000
# else:
#     narh = 20000
# print(f"Chipta {narh} so'm") # probel bo'lmaydi


# x = float(input("Birinchi sonni kiriting: ")) # )
# y = float(input("Ikkinchi sonni kiriting: ")) # )
# if x==y:
#     print(f"{x}={y}")
# elif x<y:
#     print(f"{x}<{y}") # " 
# else: # :
#     print(f"{x}>{y}")

# mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
#                'kartoshka', 'olma', 'banan', 'uzum', 'qovun'] # ]
# savat = [] # savat= [] yoq edi
# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

# if savat:
#     for mahsulot in savat: # :
#         if mahsulot in mahsulotlar:
#             print(f"Do'konimizda {mahsulot} bor")
#         else:
#             print(f"Do'konimizda {mahsulot} yo'q")
# else: 
#     print("Savatingiz bo'sh")            

# mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
#                'kartoshka', 'olma', 'banan', 'uzum', 'qovun']


# savat = []
# for n in range(5):
#     savat.append(input(f'Savatga {n+1}-mahsulotni qo\'shing: '))

# bor_mahsulotlar = []
# mavjud_emas = []
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_mahsulotlar.append(mahsulot) # mahsulot
#     else:
#         mavjud_emas.append(mahsulot)

# if mavjud_emas:
#     print("Do'konimizda quyidagi mahsulotlar yo'q:")
#     for mahsulot in mavjud_emas:
#         print(mahsulot)
# else:
#     print("Siz so'ragan barcha mahsulotlar do'konimizda bor")

# users = ['alisher1983','aziza','yasina', 'umar'] # , 
# login = input("Yangi login tanlang: ") # "

# if login in users:
#     print('Login band, yangi login tanalng!')
# else:
#     print("Xush kelibsiz!")







 