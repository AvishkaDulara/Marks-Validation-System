#=================veriables=================
pass_credit=0
defer_credit=0
#=================veriables=================
fail_credit=0
retriever_lists=[]
progress_lists=[]
trailer_lists=[]
excluded_lists=[]
my_list=[]
progress=0
module_trailer=0
module_retriever=0
Exclude=0
progress_count=0
module_trailer_count=0
module_retriver_count=0
exclude_count=0
student_count=0


def inputs():
    global progress_count
    global module_trailer_count
    global module_retriver_count
    global exclude_count
    global progress
    global module_trailer
    global module_retriever
    global Exclude
    while True:
        try:
            #=================input for the pass credit value=================
            pass_credit=int(input("Enter your credits at pass :"))
            if pass_credit not in range(0,121,20):
                print("Pass credit is out of range..")
                continue
        except:
            print("Integer required")
            continue

        break
    while True:
        try:
            #-=================input for the defer credit value=================
            defer_credit=int(input("Enter your credits at defer :"))
            if defer_credit not in range(0,121,20):
                print("Defer credit is out of range..")
                continue
        except:
            print("Integer required")
            continue

        break
    while True:
        try:
            #=================input for the fail credit value=================
            fail_credit=int(input("Enter your credits at fail :"))
            if fail_credit not in range(0,121,20):
                print("Fail credit is out of range..")
                continue
        except:
            print("Integer required")
            continue

        break

    while True:
        #=================get total and define progression out come=================
        t = pass_credit+defer_credit+fail_credit
        
        if t==120:
            
            if pass_credit==120:
                #=================progress=================
                print("~~Progress~~")
                progress = progress + 1
                progress_list=["progress",pass_credit,defer_credit,fail_credit]
                my_list.append(progress_list)
                progress_lists.append(progress_list)
                progress_count =progress_count+1
                break
            elif pass_credit==100:
                #=================progress(module trailer)=================
                print("~~Progress(module trailer)~~")
                module_trailer = module_trailer + 1
                module_trailer_list=["Module trailer",pass_credit,defer_credit,fail_credit]
                my_list.append(module_trailer_list)
                trailer_lists.append(module_trailer_list)
                module_trailer_count =module_trailer_count+1
                break
            elif fail_credit>=80:
                #=================exclued=================
                print("~~Exclued~~")
                Exclude = Exclude + 1
                exclued_list=["Exclued",pass_credit,defer_credit,fail_credit]
                my_list.append(exclued_list)
                excluded_lists.append(exclued_list)
                exclude_count =exclude_count+1
                break
            else:
                #=================Do not progress – module retriever=================
                print("~~Do not progress – module retriever~~")
                module_retriever = module_retriever + 1
                module_retriever_list=["Module retriever",pass_credit,defer_credit,fail_credit]
                my_list.append(module_retriever_list)
                retriever_lists.append(module_retriever_list)
                module_retriver_count =module_retriver_count+1
                break
        else:
            print("Total is out of range")
            
            break

def display():
    print("\n-----------------------Displayed from the list-------------------------\n")
    #inside a list another list is created to call the credits
    for progress_list in progress_lists:
        print("Progress - ",progress_list)
    for trailer_list in trailer_lists:
        print("Progress (module trailer) -",trailer_list)
    for retriever_list in retriever_lists:
        print("Module Retriever - ",retriever_list)
    for excluded_list in excluded_lists:
        print("Exclude - ",excluded_list)


def histrogram():
    #=================global variables=================
    global progress
    global module_trailer
    global module_retriever
    global Exclude
    global progress_count
    global module_trailer_count
    global module_retriver_count
    global exclude_count
    student_count=progress_count+module_trailer_count+exclude_count+module_retriver_count
    #=================To diaplay the output using stars=================
    print("""-------------------------HISTROGRAM-----------------------------------
""")
    print ("Progress ",progress,": ",end="")
    for i in range (progress):
        print("*",end="")
    print("")
    print ("Module trailer ",module_trailer,": ",end="")
    for i in range (module_trailer):
        print("*",end="")
    print("")
    print ("Module retriever ",module_retriever,": ",end="")
    for i in range (module_retriever):
        print("*",end="")
    print("")
    print ("Exclude ",Exclude,": ",end="")
    for i in range (Exclude):
        print("*",end="")
    print("")
    print(student_count,"outcomes in total")
    print("")

    
def textFile():
    print("-------------------Read the text file-----------------------")
    try:
        f = open("myfile.txt", "x")
    except:
        pass
    with open('myfile.txt', 'w') as n:
        for i in range (0,len(my_list)):
            print (*my_list[i],file=n)   
    print("")
    n.close()
    
    with open('myfile.txt', 'r') as fo:
        print (fo.read())
    
    fo.close()
    print ("__________________________E N D_________________________________")


print("""-------------------------------------------------------
Select the option you want:
1)Student vaesion
2)Staff version""")

choice=int(input("Enter your option: "))

if choice==1:
    inputs()

if choice==2:
    inputs()
    print("Would you like to enter another set of data?")
    option=input("Enter 'y' for yes or 'q' to quit and view results: ")
    while True:
        if option=="y":
            inputs()
            student_count = student_count+1
            print("")
            print("Would you like to enter another set of data?")
            option=input("Enter 'y' for yes or 'q' to quit and view results: ")
            continue
        else:
             #=================when the program is quit the functions are called=================
            histrogram()
            display()
            textFile()
            
        break
