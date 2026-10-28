class multiFunctions():

    def subfields():
        list_AIfields=['Machine Learning','Neural Networks','Vision','Robotics''Speech Processing','Natural Language Processing']
        print("Sub-fields in AI are:")
        for temp in list_AIfields:
            print (temp)
    
    def OddEven():
        num1=int(input("Enter your nunber -> "))
        if(num1%2==0):
            print(num1, " is Even number")
        else:
            print(num1, " is Odd number")
    
    def marriageElibile():
        gender=input("Enter you Gender: ")
        age=int(input("Enter you Age: "))
        if(gender=='Male' and age>=21):
            print("ELIGIBLE")
        elif(gender=='Female' and age>18):
            print("ELIGLIBLE")
        else:
            print("NOT ELIGIBLE") 
    
    def percentage():
        sub1 = int(input("Subject1 = "))
        sub2 = int(input("Subject2 = "))
        sub3 = int(input("Subject3 = "))
        sub4 = int(input("Subject4 = "))
        sub5 = int(input("Subject5 = "))
        total=sub1+sub2+sub3+sub4+sub5
        avg=total/5
        print("Total : ", total)
        print("Percentage  : ", avg)
    
    def areaofTriangle():
        height=int(input("Enter the height: "))
        width=int(input("Enter the Width :  "))
        triangleArea=(height*width)/2
        print("Area of Triangle : ", triangleArea)
    
    def perimeterofTriangle():
        height1=int(input("Enter the Height1 : "))
        height2=int(input("Enter the Height2 : "))
        breadth=int(input("Enter the Breadth : "))
        trianglePermeter=height1+height2+breadth
        print("Perimeter of Triangle : ", trianglePermeter)