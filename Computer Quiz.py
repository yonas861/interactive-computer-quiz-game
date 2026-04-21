print("welcome to my computer game ")
playing=input("Do you want to play? ")
if playing.lower() != "yes":
    quit()
print("okay! Let's play!")
score=0
incorrect=0
answer=input("1,computer's which chip counts up Arithmetic and Logic? ")
if answer.lower()==("microprocessor"):
    print("correct")
    score+=1
else:
    print("incorrect")
    incorrect+=1
answer=input("2,shortcut key to paste? ")
if answer.lower()==("ctrl+v"):
    print("correct")
    score+=1
else:
    print("incorrect")
    incorrect+=1
answer=input("3,How many Bytes are there in 1KB? ")
if answer.lower()==("1kb=1024 bytes"):
    print("correct")
    score+=1
else:
    print("incorrect")
    incorrect+=1
answer=input("4, What is PYTHON? ")
if answer.lower()==("it is a programming language"):
    print("correct")
    score+=1
else:
    print("incorrect")
    incorrect+=1
answer=input("5,what is a compiler? ")
if answer.lower()==("compiler is a software that translates computer code written in one programming language into another programming language"):
    print("correct")
    score+=1
else:
    print("incorrect")
    incorrect+=1
answer=input("6,what is cloud computing? ")
if answer.lower()==("cloud computing is the delivery of computing services over the internet"):
    print("correct")
    score+=1
else:
    print("incorrect")
    incorrect+=1
answer=input("7,A set of instructions that a computer needs to carry out its tasks is known as____________. ")
if answer.lower()==("software"):
    print("correct")
    score+=1
else:
    print("incorrect")
    incorrect+=1
answer=input("8,_______is a set of raw facts and figures. ")
if answer.lower()==("data"):
    print("correct")
    score+=1
else:
    print("incorrect")
    incorrect+=1
answer=input("9,A computer system consists of both ____ and _____. ")
if answer.lower()==("hardware and software"):
    print("correct")
    score+=1
else:
    print("incorrect")
    incorrect+=1
answer=input("10,______translate information processed by the computer into a form that the user can understand. ")
if answer.lower()==("output devices"):
    print("correct")
    score+=1
else:
    print("incorrect")
    incorrect+=1

print("INSTRUCTION:TRUE or FALSE")

answer=input("11,Data and information are the same. ")
if answer.lower()==("false"):
    print("correct")
    score+=1
else:
    print("incorrect")
    incorrect+=1
answer=input("12,The CPU is the brain of the computer. ")
if answer.lower()==("true"):
    print("correct")
    score+=1
else:
    print("incorrect")
    incorrect+=1
answer=input("13,Input,processing and output are the three stages of data processing. ")
if answer.lower()==("true"):
    print("correct")
    score+=1
else:
    print("incorrect")
    incorrect+=1
answer=input("14,A laptop computer is a portable version of a PC. ")
if answer.lower()==("true"):
    print("correct")
    score+=1
else:
    print("incorrect")
    incorrect+=1
answer=input("15,A computer virus can be spread to other computers when an infected disk is used in other computers. ")
if answer.lower()==("true"):
    print("correct")
    score+=1
else:
    print("incorrect")
    incorrect+=1
answer=input("16,A router is an interface that enables communication between two different networks. ")
if answer.lower()==("true"):
    print("correct")
    score+=1
else:
    print("incorrect")
    incorrect+=1
print("you have got " + str(score) + " correct questions.")
print("you have got " + str(incorrect) + " incorrect questions.")
print("you have got " + str((score/16)*100) + " correct questions.")
print("you have got " + str((incorrect/16)*100) + " incorrect questions.")

if score > 12:
    print("Excellent performance!")
elif score > 8:
    print("Good job, keep practicing!")
else:
    print("Needs improvement, study harder!")

playing = input("Do you want to play another game? ")

if playing.lower() == "yes":
    print("Great! Starting another game...")
else:
    print("Thanks for playing!")
    quit()

    