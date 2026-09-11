class multipleFunctions :

    def Subfields():
        print ("""Sub-fields in AI are:
        Machine Learning
        Neural Networks
        Vision
        Robotics
        Speech Processing
        Natural Language Processing""")

    def oddeven():
        num=int(input("Enter a number:"))
        if(num %2==0):
           print(num,"is Even number")
           func=num
        else:
           print(num,"is Odd number")
           func=num

    def triangle():
        Height=int(input("Height:"))
        Breadth=int(input("Breadth:"))
        Area_formula=(Height*Breadth)/2
        print("Area of Triangle:",Area_formula)
        Height1=int(input("Height1:"))
        Height2=int(input("Height2:"))
        Breadth=int(input("Breadth:"))
        Perimeter_formula=Height1+Height2+Breadth
        print("Perimeter of Triangle:",Perimeter_formula)

    def marriage():
        gen=input("Enter your Gender :")
        age=int(input("Enter Age:"))
        if gen=='male' and age >=21:
          print("Eligible")
        elif gen=='female' and age>=18:
            print("Eligible")
        else:
            print("Not Eligible")
        return gen
        print(gen)
    marriage()

def sub ():
    sub1=int(input("Subject 1 :"))
    sub2=int(input("Subject 2 :"))
    sub3=int(input("Subject 3 :"))
    sub4=int(input("Subject 4 :"))
    sub5=int(input("Subject 5 :"))
    Total=sub1+sub2+sub3+sub4+sub5
    print("Total:",Total)
    Percentage=Total/5
    print("Percentage:",Percentage)
sub()