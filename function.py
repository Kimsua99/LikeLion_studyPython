#예제 1) 리턴문도 없고 인자도 없는 함수
# def printHello():
#     print("Hello, user")
# printHello()

#예제 2) 리턴문이 없는 함수
# def printHi(name):
#     print('HI', name)
# name = input("당신의 이름은?")
# printHi(name)

#예제 3)리턴문이 있는 함수
# def printWelcome(user):
#     word = "Welcome, " + str(user)
#     return word
# user = input("당신의 이름은?")
# print(printWelcome(user))

#예제 4)세 개의 값을 동시에 리턴하는 함수
# def func_mul(x):
#     y1 = x * 10
#     y2 = x * 20
#     y3 = x * 30
#     return y1, y2, y3
# a, b, c = func_mul(10)
# print(a, b, c)

#1_ 문자열에 숫자 바로 대입하기
# print("저는 덕성 멋사 {}기 입니다.".format(9))

#2_ 문자열에 문자열 입력받아 대입하기
# fruit = input("당신이 좋아하는 과일은?")

#3_2개 이상의 값 넣기(숫자는 인덱스, 문자는 이름으로 대입)
# print("내가 좋아하는 과일은 {}입니다.".format(fruit))
# print("저는 {0}학번 {major}과 입니다.".format(18,major="IT미디어공학"))
