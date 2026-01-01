# 실습1 연산자
# 시작 용돈은 30만원입니다.
# 개강 첫 주에 책을 사느라 8만원을 썼습니다.
# 평일 점심값으로 9천원씩 5일간 사용했습니다.
# 과외 아르바이트를 하며 12만원을 벌었습니다.
# 부모님이 용돈을 더 주셔서 현재 금액의 20%를 추가로 받았습니다.
# 하지만 전기요금 등 공과금으로 남은 돈의 1/3을 빠져나갔습니다.

start = 300000
book = 80000
lunch = 9000
parttime = 120000
final= (start - book - lunch*5 + parttime)*1.2/3*2
print(f'최종 남은 돈은 {int(final)}원 입니다.')

# result
# 최종 남은 돈은 374000원 입니다.

#시작 용돈
money = 300000
# 책 구매
money -= 80000
# 평일 점심값(9천원씩 5일간)
money -= 9000 * 5
#과외 알바 수입
money += 120000
#부모님 추가 용돈(현재 금액의 20%)
money += money*0.2
#전기요금 등으로 1/3 지출
money -= money/3
#최종 남은 돈  
print(f'최종 남은 돈은 {int(money)}원 입니다.')

# result
# 최종 남은 돈은 374000원 입니다.


# 실습2 EDM 리믐 트랙 만들기
# +,* 연산자만 사용해서 아래와 같이 출력해주세요.
# 둠칫두둠칫두둠칫두둠칫

intro ="둠칫"
drop ="두둠칫"

remix = intro + drop*3
print(remix)

# result
# 둠칫두둠칫두둠칫두둠칫

# 사용자 입력
x = input("아무 숫자나 입력하세요: ")
print(x)

name = input("이름을 입력하세요: ")
print("안녕하세요, ", name)

# 이름을 입력하세요: 홍길동
# 안녕하세요,  홍길동

score = int(input("점수를 입력하세요: "))
print(f"입력한 점수는 {score}점 입니다.")

# 점수를 입력하세요: 85
# 입력한 점수는 85점 입니다.

name = input("이름을 입력하세요: ")
score = int(input("점수를 입력하세요: "))

print(f"이름은 {name} 입니다.")
print(f"입력한 점수는 {score}점 입니다.")

#이름을 입력하세요: 김철수
#점수를 입력하세요: 90

#이름은 김철수 입니다.
#입력한 점수는 90점 입니다.

a= int(input('첫 번째 값: '))
b= int(input('두 번째 값: '))

print(f"두 수의 합은 {a+b}입니다.")

# 첫 번째 값: 10
# 두 번째 값: 20

# 두 수의 합은 30입니다.

# 스플릿
fruit = '사과 참외 수박'.split()
print(fruit)

# result
# ['사과', '참외', '수박']


#실습 3 input 연습하기
# 사용자로부터 이름과 나이를 입력받아, 다음 형식으로 출력하세요.
# 안녕하세요. 저는 [이름]이고, [나이]살 입니다.
name = input("이름을 입력하세요: ")
age = int(input("나이를 숫자로 입력하세요: "))

print(f"안녕하세요. 저는 {name}이고,{age}살 입니다.")

# result
# 이름을 입력하세요: 홍길동
# 나이를 숫자로 입력하세요: 25
# 안녕하세요. 저는 홍길동이고,25살 입니다.

# 실습 4 입력과 연산 연습하기
#1. 사용자로 부터 가로와 세로 길이를 입력받아 넓이와 둘레를 계산하세요.
length = int(input("가로 길이를 입력하세요: "))
width = int(input("세로 길이를 입력하세요: "))

print(f"넓이: {length*width}")
print(f"둘레: {(length+width)*2}")

# result
# 가로 길이를 입력하세요: 5
# 세로 길이를 입력하세요: 10

# 넓이: 50
# 둘레: 30

#2. 네 자릿수 정수를 입력 받고, 각 자릿수를 분리하여 출력하세요.
number= input("네 자릿수 정수를 입력하세요: ")

number_list= list(str(number))
print(f'''천의 자리: {number_list[0]}
백의 자리: {number_list[1]}
십의 자리: {number_list[2]}
일의 자리: {number_list[3]} ''')

# result
# 네 자릿수 정수를 입력하세요: 1234
# 천의 자리: 1
# 백의 자리: 2
# 십의 자리: 3
# 일의 자리: 4

#실습5. 날짜와 시간
# 년, 월, 일과 시, 분, 초를 한번에 입력받아 아래와 같이 출력하세요.
# 첫번째 입력에서 년, 월, 일을 입력해주세요.(.으로 구분)
# 두번째 입력에서 시, 분, 초를 입력해주세요.(:으로 구분)
#출력 예시와 같이 출력해주세요.
# RE3의 개강일은 2025년 07월 07일
# 시작 시간은 09시 05분 30초입니다.

date = input("년,월,일을 .으로 구분하여 입력하세요: ")
time = input("시,분,초를 :으로 구분하여 입력하세요: ")

date_list= date.split('.')
time_list= time.split(':')

print(f'''RE3의 개강일은 {date_list[0]}년 {date_list[1]}월 {date_list[2]}일
시작 시간은 {time_list[0]}시 {time_list[1]}분 {time_list[2]}초입니다.''')

# result
# 년,월,일을 .으로 구분하여 입력하세요: 2025.07.07
# 시,분,초를 :으로 구분하여 입력하세요: 09:05:30
# RE3의 개강일은 2025년 07월 07일
# 시작 시간은 09시 05분 30초입니다.

# 리스트
list1 = list()

#문자열을 리스트로
strlist = list("codingOn")

print(list1)
print(strlist)

# []
# ['c', 'o', 'd', 'i', 'n', 'g', 'O', 'n']

sample = [10, 20, 30, 40, 5, 60, 70, 80, 90, 100,1]

print(sample[-2])
print(sample[len(sample)-2]) 
print(sample[int(len(sample)/2)])

# 100
# 100
# 60

fruits = ['apple', 'banana', 'cherry']
fruits[0] = 'orange'
print(fruits)

# ['orange', 'banana', 'cherry']

nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(nums[:4])
print(nums[-1:-4:-1])

# [10, 20, 30, 40]
# [90, 80, 70]

# 실습1. 인덱싱, 슬라이싱 복습문제
#문제 1. 첫 번째 요소와 마지막 요소 출력하기
nums = [10, 20, 30, 40, 50]
print(nums[0])
print(nums[-1])

#10
#50

#문제 2. 가운데 세 개의 요소 추출하기
nums = [100, 200, 300, 400, 500, 600, 700]
print(nums[2:5])

#[300, 400, 500]

#문제 3. 리스트 원소 두배 하기
nums = [1, 2, 3, 4, 5]
nums_2=[nums[0]*2, nums[1]*2, nums[2]*2, nums[3]*2, nums[4]*2]
print(nums_2)

#[2, 4, 6, 8, 10]

#문제 4. 리스트 뒤집어서 출력하기
items = ["a", "b", "c", "d", "e"]
print(items[-1::-1])

#['e', 'd', 'c', 'b', 'a']

#문제 5. 리스트에서 짝수 인덱스 요소만 출력하기
data =["zero", "one", "two", "three", "four", "five"]
print(data[0:len(data):2])

#['zero', 'two', 'four']

#문제 6. 슬라이싱으로 리스트 수정하기
#슬라이싱으로 "어벤져스","라라랜드"를 "매트릭스","타이타닉"으로 변경
movies = ["인셉션", "인터스텔라","어벤져스","라라랜드","기생충"]
movies[2:4] = ["매트릭스","타이타닉"]
print(movies)

#['인셉션', '인터스텔라', '매트릭스', '타이타닉', '기생충']

#문제7. 특정 규칙에 따라 요소 추출
#다음 리스트에서 "물리","생물","지구과학"만 순서대로 추출하여 새로운 리스트로 만드세요.
subjects = ["국어", "영어", "수학", "물리", "화학", "생물", "역사","지구과학","윤리"]
new_subjects = [subjects[3], subjects[5], subjects[7]]
print(new_subjects)

#['물리', '생물', '지구과학']

#문제8. 리스트를 3개 구간으로 나누어 역순 병합
#다음 리스트를[1~3번째 요소]+[4~6번째 요소]+[7~9번째 요소]로 3개 구간으로 
#나눈 후, 각 구간을 역순으로 출력하세요. 단, 출력 시 한 줄로 출력되게 출력해주세요.
data = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
print( data[2::-1],  data [5:2:-1],  data [8:5:-1])

#['C', 'B', 'A'] ['F', 'E', 'D'] ['I', 'H', 'G']

#실습2. 리스트 연산 복습문제(1)
#문제 1. 부분 삭제 후 연결
#가운데 3요소를 삭제한 뒤, 나머지 리스트를 연결하여 새 리스트 result를 출력
fruits = ['apple', 'banana', 'cherry', 'grape', 'watermelon', 'strawberry']
result = fruits[:1] + fruits[4:]
print(result)

#['apple', 'watermelon', 'strawberry']

#문제 2. 반복 리스트 내부 요소 삭제
#다음 리스트를 3번 반복한 후, 전체 결과에서 중간에 있는 "A"만 삭제 후 최종 리스트 출력
letters = ["A", "B"]
letters = letters * 3
del letters[2]
print(letters)

#['A', 'B', 'B', 'A', 'B']

#실습3
'''
*문제 설명*
한 학생의 소비 기록을 관리하는 프로그램을 작성하시오.
프로그램은 사용자 입력을 기반으로 리스트를 생성하고,
리스트 조작 메서드를 활용해 데이터를 추가, 삽입, 삭제, 분석해야 한다.
조건문(if), 반복문(for/while) 사용 금지
함수 정의 금지
1단계: 초기 데이터 입력
사용자로부터 10개의 정수를 입력받아 리스트 data에 저장하라.
(1일차 ~ 10일차 소비 금액)
2단계: 리스트 수정
마지막에 5000원을 추가하라.
리스트의 맨 앞에 3000원을 삽입하라.
값이 0인 요소를 삭제하라.
(0은 정확히 한 번만 존재함)
3단계: 부분 분석
처음 5일 소비 내역을 슬라이싱으로 출력하라.
마지막 5일 소비 내역을 슬라이싱으로 출력하라.
4단계: 계산
전체 소비 금액을 출력하라.
전체 평균 소비 금액을 출력하라.
처음 5일 평균 소비 금액을 출력하라.
마지막 5일 평균 소비 금액을 출력하라.
5단계: 리스트 복사 및 추가 수정
data를 슬라이싱으로 복사하여 data_copy를 만들어라.
data_copy에서 첫 번째 요소를 삭제하라.
data_copy에서 마지막 요소를 삭제하라.
수정된 data_copy를 출력하라.
원본 data를 출력하라.
6단계: 출력 형식
아래 출력 형식과 완전히 동일하게 출력하시오.
-입력-
1000
2000
0
3000
4000
5000
6000
7000
8000
9000
-출력-
처음 5일: [3000, 1000, 2000, 3000, 4000]
마지막 5일: [6000, 7000, 8000, 9000, 5000]
총 소비: 53000
전체 평균: 4818.181818181818
처음 5일 평균: 2600.0
마지막 5일 평균: 7000.0
수정된 리스트: [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000]
원본 리스트: [3000, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 5000]'''
# 엔터로 구분하여 10개의 값을 입력받아 리스트로 저장
# 1단계
data1 = int(input("-입력-\n"))
input_list = []
input_list.append(data1)
data2 = int(input())
input_list.append(data2)
data3 = int(input())
input_list.append(data3)
data4 = int(input())
input_list.append(data4)
data5 = int(input())
input_list.append(data5)
data6 = int(input())
input_list.append(data6)
data7 = int(input())
input_list.append(data7)
data8 = int(input())
input_list.append(data8)
data9 = int(input())
input_list.append(data9)
data10 = int(input())
input_list.append(data10)
# 2단계
input_list.append(5000)  #마지막에 5000 추가
input_list.insert(0,3000)    #맨 앞에 3000 추가
input_list.remove(0)     #0 삭제
# 3단계
# input_list[0:5]    #처음 5일 소비내역 슬라이싱
# input_list[-5::]    #마지막 5일 소비내역 슬라이싱
# 4단계
# sum(input_list)   #전체 소비내역 출력
# sum(input_list)/len(input_list)   #평균 소비내역 출력
# sum(input_list[:5])/5   #처음 5일 평균 소비내역 출력
# sum(input_list[-5:])/5   #마지막 5일 평균 소비내역 출력
# 5단계
data_copy = input_list.copy()   #리스트 복사
del data_copy[0]  #data_copy에서 첫 번째 요소 삭제
del data_copy[-1]  #data_copy에서 마지막 요소 삭제

print(f'''
-출력-
처음 5일:{input_list[0:5]}
마지막 5일: {input_list[-5::]}
총 소비: {sum(input_list)}
전체 평균: {sum(input_list)/len(input_list)}
처음 5일 평균: {sum(input_list[:5])/5}
마지막 5일 평균: {sum(input_list[-5:])/5}
수정된 리스트: {data_copy}
원본 리스트: {input_list}''')

# -입력-
# 1000
# 2000
# 0
# 3000
# 4000
# 5000
# 6000
# 7000
# 8000
# 9000
# -출력-
# 처음 5일:[3000, 1000, 2000, 3000, 4000]
# 마지막 5일: [6000, 7000, 8000, 9000, 5000]
# 총 소비: 53000
# 전체 평균: 4818.181818181818
# 처음 5일 평균: 2600.0
# 마지막 5일 평균: 7000.0
# 수정된 리스트: [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000]
# 원본 리스트: [3000, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 5000]
