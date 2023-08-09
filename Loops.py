#for loop
for i in range(10):
    print("Hi, How are you?")

for i in range(20):
    print(i*2)

answer=0
for i in range(11):
    answer = answer + i
print(answer)

answer = 0
for i in range(5):
    print("First",i,"numbers, when added, gives", answer)

t=input("What tables you would like to display?")
t=int(t)
for i in range(11):
    print(t,"x",i,"=",t*i)

n = 1
c= 1
while(c==1):
    print("Token number",n,"may please come in")
    c=input("Continue?(0/1)")
    c=int(c)
    n=n+1
print("Thank you, this is the end of our day.")