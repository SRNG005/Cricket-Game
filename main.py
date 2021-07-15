import random as rdm

print("{: ^50s}".format("<<<<CRICKET GAME>>>>"))
while True:
    print("RULES: \n1. Only enter a number between 1 and 6 for runs and balls.\n2. If user or the computer selects the same number as the other, it is declared out!.\n3. For "
          "toss, enter 1 for odd and 2 for even.\n3. In the next number prompt, enter a number between 0 & 4.\n5. The toss is done by adding the number "
          "entered in the second prompt and a number chosen by the system and matching it with the odd or even choice.\n6. In the bat or ball prompt,"
          "enter 1 to choose batting and 2 to choose bowling.\n")
    while True:
        print("Valid inputs for toss are 1 and 2.")
        a=int(input("Toss: "))

        if a>2 or a<1:
            print("Invalid Input!")
            continue
        else:
            break
    if a==1:
        print("User choice is Odd.")
        print()
    elif a==2:
        print("User choice is Even.")
        print()
    while True:
        print("Valid inputs in the below prompt are numbers ranging from 0 to 4.")
        b = int(input("Enter a number: "))
        if b>4 or b<0:
            print("Invalid Input!")
            continue
        else:
            break

    c=rdm.randint(0,4)
    d=b+c
    if d%2==0:
        print("The toss is Even!")
        e=2
        if a==e:
            print("User wins the toss!")
            print()
            f=2
        else:
            print("Computer wins the toss!")
            print()
            f=1
    else:
        print("The toss is Odd!")
        e=1
        if a==e:
            print("User wins the toss!")
            print()
            f=2
        else:
            print("Computer wins the toss!")
            print()
            f=1
    if f==2:
        print("Valid inputs for the below prompt are 1 and 2.")
        g=int(input("Do you want to bat or ball?"))
        if g==1:
            print("User chooses to bat first.")
            print()
            h=int(input("How many balls do you want to play?"))
            print("NOW THE USER IS BATTING AND THE COMPUTER IS BOWLING")
            i=[]
            for j in range(h):
                k=rdm.randint(1,6)
                l=int(input("Runs: "))
                x=sum(i)
                if l>6 or l<1:
                    print("Invalid Input!")
                    continue
                elif k==l:
                    print("User is out!")
                    break
                elif k!=l:
                    i.append(l)
            m = sum(i)
            print("User scored",m,"runs.")
            print()
            print("NOW THE COMPUTER IS BATTING AND THE USER IS BOWLING")
            n=[]
            for o in range(h):
                p=rdm.randint(1,6)
                q=int(input("Ball: "))
                r=sum(n)
                if q>6 or q<1:
                    print("Invalid Input!")
                    continue
                elif q==p:
                    print("Computer is out!")
                    break
                elif q!=p:
                    s=n.append(p)
            t=sum(n)
            print()
            if m>t:
                print("User scored", m , "runs.")
                print("Computer scored",t, "runs.")
                print("User wins!")

            elif m==t:
                fscore = m + 1
                print("User adjusted final score is", fscore)
                print("Computer final score is", t)
                print("User wins!")

            else:
                print("User scored",m,"runs.")
                print("Computer scored",t,"runs.")
                print("Computer wins!")


        if g==2:
            print("User chooses to ball first.")
            print()
            a1 = int(input("How many balls do you want to play?"))
            print("NOW THE USER IS BOWLING AND THE COMPUTER IS BATTING")
            b2=[]
            for u in range(a1):
                c2=rdm.randint(1,6)
                d2=int(input("Ball:"))
                e2 = sum(b2)
                if d2>6 or d<1:
                    print("Invalid Input!")
                    continue
                elif d2==c2:
                    print("Computer is out!")
                    break
                elif d2!=c2:
                    f2=b2.append(c2)
            x2=sum(b2)
            print("Computer scored",e2,"runs.")
            print()
            print("NOW THE USER IS BATTING AND THE COMPUTER IS BOWLING")
            i2=[]
            for j2 in range(a1):
                k2=int(input("Runs: "))
                l2=rdm.randint(1,6)
                x3=sum(i2)
                if k2>6 or k2<1:
                    print("Invalid Input!")
                    continue
                elif k2==l2:
                    print("User is out!")
                    break
                elif k2!=l2:
                    i2.append(k2)
            m2 = sum(i2)
            print()
            print("User scored",m2,"runs.")
            if m2>e2:
                print("Computer scored",e2,"runs.")
                print("User wins!")

            elif m2==e2:
                n2=m2+1
                print("User adjusted final score is",n2)
                print("Computer scored",e2,"runs")
                print("User wins!")

            else:
                print("Computer scored",e2,"runs.")
                print("Computer wins!")

    else:
        h=rdm.randint(1,2)
        if h==1:
            print("Computer decides to bat first.")
            print()
            a1=int(input("How many balls do you want to play?"))
            print("NOW THE COMPUTER IS BATTING AND THE USER IS BOWLING ")
            b1=[]
            for c1 in range(a1):
                d1=rdm.randint(1,6)
                e1=int(input("Ball: "))
                g1=sum(b1)
                if e1>6 or e1<1:
                    print("Invalid Input!")
                    continue
                elif e1==d1:
                    print("Computer is out!")
                    break
                elif e1!=d1:
                    b1.append(d1)
            f1 = sum(b1)
            print("Computer scored",f1,"runs.")
            print()
            print("NOW THE USER IS BATTING AND THE COMPUTER IS BOWLING")
            a3=[]
            for b3 in range(a1):
                c3=rdm.randint(1,6)
                d3=int(input("Runs: "))
                e3=sum(a3)
                if d3>6 or d3<1:
                    print("Invalid Input!")
                    continue
                elif d3==c3:
                    print("User is out!")
                    break
                elif d3!=c3:
                    a3.append(d3)
            f3=sum(a3)
            print("User scored",f3,"runs.")
            if f3>f1:
                print("Computer scored",f1,"runs.")
                print("User wins!")

            elif f3==f1:
                adj=f3+1
                print("User adjusted score is",adj)
                print("Computer scored",f3,"runs.")
                print("User wins!")

            else:
                print("Computer scored",f1,"runs.")
                print("Computer wins!")

        if h==2:
            print("Computer decides to ball first.")
            print()
            a4=int(input("How many balls do you want to play? "))
            print("NOW THE USER IS BATTING AND THE COMPUTER IS BOWLING")
            b4=[]
            for c4 in range(a4):
                d4=int(input("Runs: "))
                e4=rdm.randint(1,6)
                f4=sum(b4)
                if d4>6 or d4<1:
                    print("Invalid Input!")
                    continue
                elif d4==e4:
                    print("User is out!")
                    break
                elif d4!=e4:
                    b4.append(d4)
            ff4=sum(b4)
            print("User scored",ff4,"runs.")
            print()
            print("NOW THE COMPUTER IS BATTING AND THE USER IS BOWLING")
            g4=[]
            for h4 in range(a4):
                i4=rdm.randint(1,6)
                j4=int(input("Ball: "))
                k4=sum(g4)
                if j4>6 or j4<1:
                    print("Invalid Input!")
                    continue
                elif j4==i4:
                    print("Computer is out!")
                    break
                elif j4!=i4:
                    g4.append(i4)
            kk4=sum(g4)
            print("Computer scored",kk4,"runs.")
            if ff4>kk4:
                print("User scored",ff4,"runs.")
                print("User wins!")

            elif ff4==kk4:
                adj1=ff4+1
                print("User adjusted score is",adj1)
                print("Computer scored",kk4,"runs.")
                print("User wins!")

            elif ff4<kk4:
                print("User scored",ff4, "runs.")
                print("Computer wins!")
    print()
    print("Do you want to play again?")
    gg=input("Enter y to play again and n to stop the game: ")
    if gg=="n":
        print()
        print("Thank you for playing!")
        break




