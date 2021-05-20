#예제1) 85점 이상이면 pass, 85점 이하이면 fail 출력해보자!

score = int(input("점수를 입력하세요.: "))
if(score >= 85):

    print("pass")

else:
    print("fail")


#예제2) 친구한테 멋사자인지 물어보고, 멋사자이면 기쁨의 반응을 아니면 시무룩한반응
question = input("너 멋쟁이 사자처럼이니?")

if(question == "Yes"):
    print("wow~")

else:
    print("oh..my..")


#예제3) 친구와 밥을 먹을건데, 친구 수중에 있는 돈에 따라서 메뉴를 골라보자
#오만원 이상이면 아웃백, 만원 이상이면 학식, 
#오천원 이상이면 컵밥, 천원 이상이면 컵라면
#천원 미만이면 집에가서 먹자

money = int(input("얼마 있니? "))

if(money >= 50000):
    print("아웃백ㄱㄱ")

elif(money >= 10000):
     print("학식ㄱㄱ")

elif(money >= 5000):
     print("컵밥ㄱㄱ")

elif(money >= 1000):
     print("컵라면ㄱㄱ")

else:
     print("집ㄱㄱ")


#ex1) num에 1씩 더하다가 3을 만났을 때 반복문을 정지시켜보자.
num = 0
while(True):
     print(num)
     num += 1
     if(num == 3):
         break

#ex2) 1~10의 범위 중 홀수만 출력해보자
for i in range(10):
    if(i % 2 == 0):
        continue
    print(i)