str1 = "멋쟁이 사자처럼"
str2 = "좋은 동아리입니다."
str3 = "멋쟁이 사자처럼은 사랑스러워"
str4 = "사과,바나나,포도"

print(str1 + str2)                #문자열 실습 1

print(str1 * 3)                   #문자열 실습 2

print(str1[0])                    #문자열 실습 3

print(str1[3])                    #문자열 실습 4

print(str1[4:6])                  #문자열 실습 5

print(len(str1))                  #문자열 실습 6

print(str3.count("사"))           #문자열 실습 7

print(str3.split())               #문자열 실습 8

print(str4.split(","))            #문자열 실습 9

print("find: ", str3.find("쟁"))  #문자열 실습 10
print("find: ", str3.index("쟁"))

print("find: ", str3.find("무"))  #문자열 실습 11
print("find: ", str3.index("무"))