# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution. 
# Student ID: 20210629


dic={}
pass_credit=0
defer_credit=0
fail_credit=0
option=""
def stud_id():
    #=================global veriables=================
    global student_id
    while True:
        #=================insert student id================
        student_id=input("Enter Student ID Number: ")
        if student_id[0]=="w" and len(student_id)==8:
            print("")
            break
        else:
            print("Student ID number is incorrect")

def inputs():
    #=================global veriables=================
    global pass_credit,defer_credit,fail_credit
    while True:
        try:
            #=================get uer inputs for pass credit=================
            pass_credit=int(input("Enter Pass Credit: "))
            if pass_credit not in range(0,121,20):
                print("out of range")
                continue
        except:
            print("Integer required")
            continue
        break
    while True:
        try:
            #=================get uer inputs for defer credit=================
            defer_credit=int(input("Enter Defer Credit: "))
            if defer_credit not in range(0,121,20):
                print("out of range")
                continue
        except:
            print("Integer required")
            continue
        break
    while True:
        try:
            #=================get uer inputs for fail credit=================
            fail_credit=int(input("Enter Fail Credit: "))
            if fail_credit not in range(0,121,20):
                print("out of range")
                continue
        except:
            print("Integer required")
            continue
        break

    
        

def main():
    while True:
        print("")
        print("Would you like to enter another set of data?")
        option=input("Enter 'y' for yes or 'q' to quit and view results: ")
        if option=="q":
            print(dic)
            raise SystemExit
                    
                
        elif option=="y":
            break

        else:
            print ("invalid response")
                

while True:
    stud_id()
    inputs()
    #=================get total and define progrssion out come=================
    t= pass_credit+defer_credit+fail_credit
    if t == 120:
        if pass_credit==120:
            #=================progress=================
            dic[student_id]={}
            dic[student_id]="Progress-",student_id,pass_credit,defer_credit,fail_credit
            main()

        elif pass_credit==100:
            #=================progress(module trailer)=================
            dic[student_id]={}
            dic[student_id]="Progress(module trailer)-",student_id,pass_credit,defer_credit,fail_credit
            main()

        elif fail_credit>=80:
            #=================exclude=================
            dic[student_id]={}
            dic[student_id]="Exclude-",student_id,pass_credit,defer_credit,fail_credit
            main()

        else:
            #=================Do not Progress(module retriever)=================
            dic[student_id]={}
            dic[student_id]="Do not Progress(module retriever)-",student_id,pass_credit,defer_credit,fail_credit
            main()

    else:
        print("Total is incorrect")

