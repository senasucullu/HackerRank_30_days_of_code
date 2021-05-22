# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(input(""))
if 1 <= t <= 10:
    for i in range(t):
        s = input("")
        lengtofs = int(len(s))
        total = ""
        result = ""
        if 2 <= lengtofs <= 10000:
            for i in s[0:lengtofs:2]:
                total += i
            for i in s[1:lengtofs:2]:
                result += i
            z = total + result
        print(total + " " + result)