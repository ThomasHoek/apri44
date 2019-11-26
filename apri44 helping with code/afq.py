print("----this shit shows if your input value can be written as n(n+1) or not----")
x = "n"
while x == "n":
    try:
        s = 0
        print("< now you're expected to input a valid number; >")
        p = int(input())
        for i in range(1, p + 1, 1):
            k = i * (i + 1)
            if k == p:
                print("eligible number. it can be written like;")
                print(str(i) + " x " + str((i + 1)))
                s = 1
        if s == 1:
            pass
        else:
            print("the number you've written can't be defined in n.(n+1) format.")
    except:
        print("fill a integer in.")
    print("exit? y/n")
    x = input()