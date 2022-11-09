#1번
A = int(input('A는?'))
B = int(input('B는?'))

if A > B:
    print('>')
elif A < B:
    print('<')
elif A == B:
    print('==')

#2번
score = float(input('당신의 성적은?'))

if 90<=score<=100:
    print('A')
elif 80<=score<=89:
    print('B')
elif 70<=score<=79:
    print('C')
elif 60<=score<=69:
    print('D')
else:
    print('E')

#3번
year = int(input(''))

if 1<=year<=4000 and year//4 == 0:
    if year//100:
        print(1)
else:
    print(0)

#5번
H = int(input('몇시'))
M = int(input('몇분'))

if M >= 45:
    M = M-45
    print(H, M)

else:
    H = H - 1
    M = M + 15
    print(H, M)

#6번
A = int(input('몇시'))
B = int(input('몇분'))
C = int(input('조리시간'))

if B + C >=60:
    if A<23:
        print(A+1, B+C-60)
    else:
        print(0, B+C-60)
else:
    print(A, B+C)

#7번

a = int(input(''))
b = int(input(''))
c = int(input(''))

if a == b:
    if b == c:
        print(13000)
if a == b or b == c:
    if a !== c:
        print(1200)
if a == c:
    print(1200)
else:
    if a >b>c or a > c > b:
        print(a * 100)
    if b >a > c or b>c>a:
        print(b * 100)
    if  c>a>b or c>b>a:
        print(c*100)

        