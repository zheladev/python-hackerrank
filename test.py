s = "123456"
for i in range(0, len(s) - 1):
    print(s[0:i] + " " + s[i+1:])
    print(s[len(s)-1:len(s)-1-i:-1] + " " + s[len(s)-2-i::-1])
