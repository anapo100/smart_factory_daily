# print 함수 사용법
name, age, grade = "Alice", 14, 2

print("이름:", name)
print("나이:", age)
print("학년:", grade)

# result
# 이름: Alice
# 나이: 14
# 학년: 2

# 값의 교환
x=1
y=2

x,y = y,x
print(x,y)

# result
# 2 1

# 변수와 자료형
a= 1
b = 3.14
c = '안녕'
d = True

print(type(a))
print(type(b))
print(type(c))
print(type(d))

# result
# <class 'int'>
# <class 'float'>
# <class 'str'>
# <class 'bool'>

# 형 변환

# 가능한 경우
print(int(3.7)) 
print(float(5)) 
print(int(True)) 
print(int(False)) 
print(str(100)) 

# result
# 3 (소수점 아래 절삭)
# 5.0
# 1
# 0
# 100




# 불가능한 경우
'''
print(int("3.14")) 
print(int("abc"))

#result
# ValueError: invalid literal for int() with base 10: '3.14'
# ValueError: invalid literal for int() with base 10: 'abc'
'''

#문자열 포매팅: f-string
cat='고양이'
age=15
gender='수컷'
name='꽁꽁이'
skill='냥냥 펀치'

print(f'''우리집 {cat}는 나이가 {age}살이고 성별은 {gender}입니다.
이름은 {name}이고 주특기는 {skill}입니다.''')

# result
# 우리집 고양이는 나이가 15살이고 성별은 수컷입니다.
# 이름은 꽁꽁이이고 주특기는 냥냥 펀치입니다.

# 실습 1번
# 영화 정보를 변수로 만들어 한번에 출력해보세요.

영화_제목='아바타: 불과 재'
상영_상태='상영 중'
개봉_날짜='2025.12.17'
줄거리= """판도라를 위협하는 재의 부족, 더 이상 인간만이 적이 아니다! 
모두의 운명을 뒤흔들 거대한 전투가 시작된다! 인간들과의 전쟁으로 첫째
아들 ‘네테이얌’을 잃은 후, ‘제이크’와 ‘네이티리’는 깊은 슬픔에 빠진다.
상실에 빠진 이들 앞에 '바랑'이 이끄는 재의 부족이 등장하면서, 판도라는
더욱 큰 위험에 빠지게 되고,‘설리’ 가족은 선택의 기로에 서게 되는데…"""
장르='SF'
국가='미국'
실관람객_평점= 8.95
네티즌_평점= 8.15
순위= '1위'
누적_관객수='417만명'

print(f'''영화 제목: {영화_제목}\n상영 상태: {상영_상태}\n개봉 날짜: {개봉_날짜}
줄거리: {줄거리}\n장르: {장르}\n국가: {국가}\n실관람객 평점: {str(실관람객_평점)}
네티즌 평점: {str(네티즌_평점)}\n순위: {순위}\n누적 관객수: {누적_관객수}''')

# result
# 영화 제목: 아바타: 불과 재
# 상영 상태: 상영 중
# 개봉 날짜: 2025.12.17
# 줄거리: 판도라를 위협하는 재의 부족, 더 이상 인간만이 적이 아니다!
# 모두의 운명을 뒤흔들 거대한 전투가 시작된다! 인간들과의 전쟁으로 첫째
# 아들 ‘네테이얌’을 잃은 후, ‘제이크’와 ‘네이티리’는 깊은 슬픔에 빠진다.
# 상실에 빠진 이들 앞에 '바랑'이 이끄는 재의 부족이 등장하면서, 판도라는
# 더욱 큰 위험에 빠지게 되고,‘설리’ 가족은 선택의 기로에 서게 되는데…
# 장르: SF
# 국가: 미국
# 실관람객 평점: 8.95
# 네티즌 평점: 8.15
# 순위: 1위
# 누적 관객수: 417만명

# 실습 2번
# 자신의 정보를 변수로 만들어 한번에 출력해보세요. 변수는 20개 이상 만드세요.
name, age, MBTI, hobby, ability = "이하일",25,"INTP","기타 연주","문제 풀기"
region, like_food,color,animal,season = "포항","치킨","파란색","고양이","가을"
music_genre,sport,movie_genre,book_genre,game_genre = "발라드", "축구","SF","판타지","RPG"
musicians,directors,authors,gamers,travel_destination = "정성하", "크리스토퍼 놀란", "J.K. 롤링", "Faker", "일본"

print(f'''제 이름은 {name}입니다. 저는 {age}살 입니다. MBTI는 {MBTI}입니다. 
저는 {hobby}를 좋아합니다. 저는 {ability}를 잘합니다. 가장 좋아하는 뮤지션은 {musicians}입니다. 
저는 {region}에서 왔습니다. 저는 {like_food}을 가장 좋아합니다. 좋아하는 색과 동물은 {color}과 {animal}입니다.
가장 좋아하는 계절은 {season}입니다. 저는 보통 {music_genre}를 듣습니다. 저는 {sport}를 보는것을 좋아합니다.
저는 {movie_genre}장르의 영화가 좋고, 최고의 작품은 {directors}의 인터스텔라 입니다.
저는 {book_genre} 장르의 책을 좋아하고 가장 좋아하는 작가는 {authors}입니다. 
저는 {game_genre}를 좋아하지만 좋아하는 게이머는 {gamers}입니다. 저는 {travel_destination}으로 여행을 가고 싶습니다.''')

# result
# 제 이름은 이하일입니다. 저는 25살 입니다. MBTI는 INTP입니다.
# 저는 기타 연주를 좋아합니다. 저는 문제 풀기를 잘합니다. 가장 좋아하는 뮤지션은 정성하입니다.
# 저는 포항에서 왔습니다. 저는 치킨을 가장 좋아합니다. 좋아하는 색과 동물은 파란색과 고양이입니다.
# 가장 좋아하는 계절은 가을입니다. 저는 보통 발라드를 듣습니다. 저는 축구를 보는것을 좋아합니다.
# 저는 SF장르의 영화가 좋고, 최고의 작품은 크리스토퍼 놀란의 인터스텔라 입니다.
# 저는 판타지 장르의 책을 좋아하고 가장 좋아하는 작가는 J.K. 롤링입니다.
# 저는 RPG를 좋아하지만 좋아하는 게이머는 Faker입니다. 저는 일본으로 여행을 가고 싶습니다.