#GET USER NAME
use_nam=input("Enter Your Name =")
print(use_nam)
#GET USER SUBJECTS NAME WITH MARKS
subjects={}
for i in range(5):
    subject=input("Enter subject name :")
    user_marks=int(input("Enter Your Marks Out Of 100 ="))
    subjects[subject]=user_marks
print(subjects)
#CALCULATE THE TOTAL MARKS
total = sum(subjects.values())
#FIND THE GRADE 
def grade():
    if total >=400:
        print("Your Grade Is :A")
    elif total >=350 and total<400:
        print("Your Grade Is :B")
    elif total >=300 and total<350:
        print("Your Grade Is :C")
    elif total >=250 and total<300:
        print("Your Grade Is :D")
    else:
        print("Your Grade Is :F")
grade()
#FIND THE STUDENT IS PASSED OR FAILED
def reslt():
    per=total/500 *100
    print("Your Percentage Is :",per)
    if per >=50:
        print("PASSED")
    else:
        print("FAILED")
reslt()