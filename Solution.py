# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

inp = input().split(" ")
text = inp[0]
num = int(inp[1])

liste = list(permutations(text,num))
liste.sort()

for x in liste:
    temp = ""
    for char in x:
        temp += char
    print(temp)
