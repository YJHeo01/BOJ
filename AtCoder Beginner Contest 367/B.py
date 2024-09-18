c = list(input())

while True:
    tmp = c.pop()
    if tmp == '.':
        break
    if tmp != '0':
        c.append(tmp)
        break

for i in c:
    print(i,end="")
