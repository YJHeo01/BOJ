#https://www.acmicpc.net/problem/5635
#https://www.acmicpc.net/source/79565490

def main():
    n = int(input())
    information = []
    for _ in range(n):
        name, day, month, year = input().split()
        information.append([int(year),int(month),int(day),name])
    information.sort()
    print(information[n-1][3])
    print(information[0][3])
    
if __name__ == "__main__":
    main()
