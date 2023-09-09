import random, os
global partners,c,type1,allout
Bowlers = {"woakes":[0,0,0], "archer":[0,0,0],"liam":[0,0,0],"wood":[0,0,0],"rashid":[0,0,0],"stokes":[0,0,0]} #livingston,mohd ali, sam curran, chris jordan
Bowlers2 = {"jadeja":[0,0,0], "bhuvi":[0,0,0],"pandaya":[0,0,0],"shami":[0,0,0],"bumrah":[0,0,0],"chahal":[0,0,0]}
Batsman = {"singh":[0,0,random.randint(1,10),[False, False, False]],"rohan":[0,0,random.randint(1,10),[False, False, False]],"kishan":[0,0,random.randint(1,8),[False, False, False]],"iyer":[0,0,random.randint(1,8),[False, False, False]],"pant":[0,0,random.randint(1,6),[False, False, False]],"pandaya":[0,0,random.randint(1,6),[False, False, False]],"jadeja":[0,0,random.randint(1,4),[False, False, False]],"bhuvi":[0,0,random.randint(1,3),[False, False, False]],"shami":[0,0,random.randint(1,2),[False, False, False]],"bumrah":[0,0,random.randint(1,2),[False, False, False]],"chahal":[0,0,random.randint(1,2),[False, False, False]]}
Batsman2 = {"roy":[0,0,random.randint(1,10),[False, False, False]],"buttler":[0,0,random.randint(1,10),[False, False, False]],"malan":[0,0,random.randint(1,8),[False, False, False]],"barestrow":[0,0,random.randint(1,8),[False, False, False]],"morgan":[0,0,random.randint(1,6),[False, False, False]],"stokes":[0,0,random.randint(1,6),[False, False, False]],"liam":[0,0,random.randint(1,4),[False, False, False]],"woakes":[0,0,random.randint(1,3),[False, False, False]],"archer":[0,0,random.randint(1,2),[False, False, False]],"rashid":[0,0,random.randint(1,2),[False, False, False]],"wood":[0,0,random.randint(1,2),[False, False, False]]}
names = {"roy":"Jason Roy","buttler":"Josh Buttler","malan":"Dawid Malan","barestrow":"Johhny Barestrow","morgan":"Eoin Morgan","woakes":"Chris Woakes","archer":"Jofra Archer","liam":"Liam Plunkett","wood":"Mark Wood","rashid":"Adil Rashid","stokes":"Ben Stokes","rohan":"Rohan Rajput","bhuvi":"Bhuvneshwar Kumar","kishan":'Ishan Kishan',"singh":"Aditya Singh","pant":"Rishabh Pant","iyer":"Shreyas Iyer","jadeja":"Ravindra Jadeja","pandaya":"Hardik Pandaya","shami":"Mohd Shami","bumrah":"Jasprit Bumrah","chahal":"Yuzvendra Chahal"}
while True:
    type1 = input("What type of match do you want?\n>> ")
    if type1 not in ['odi', 't20i', 'test']:
        print('try again! between (odi, t20i, test)')
        continue
    else:
        break
totalw = {0:0,1:0,2:0,3:0,4:0,6:0,-1:0}
bowlerChoice = []
battinglist = list(Batsman.keys())
def bowlsetup(ml):
    for _ in range(ml[0]):
        bowlerChoice.append(1)
    for _ in range(ml[1]):
        bowlerChoice.append(2)
    for _ in range(ml[2]):
        bowlerChoice.append(4)
    for _ in range(ml[3]):
        bowlerChoice.append(6)
if type1 == "t20i":
    bowlsetup([14,21,26,34])
if type1 == "odi":
    bowlsetup([9,16,31,42])
if type1 == "test":
    bowlsetup([11,12,21,57])
def randomPlay():
    randomPlay1 = []
    randomParameters = {'test':[[random.randint(25,30),50],[4,18],[1,7],[3,random.randint(4,11)],[0,random.randint(1,random.randint(2,random.randint(3,4)))]],'odi':[[14,26],[6,15],[random.randint(2,4),8],[random.randint(3,5),random.randint(8,14)],[random.randint(0,4),random.randint(4,7)]],'t20i':[[9,17],[7,16],[random.randint(2,5),8],[6,random.randint(9,11)],[random.randint(2,4),random.randint(6,random.randint(11,12))]]}
    for _ in range(random.randint(randomParameters[type1][0][0],randomParameters[type1][0][1])):
        randomPlay1.append(0)
    for _ in range(random.randint(randomParameters[type1][1][0],randomParameters[type1][1][1])):
        randomPlay1.append(1)
    for _ in range(random.randint(randomParameters[type1][2][0],randomParameters[type1][2][1])):
        randomPlay1.append(2)
    for _ in range(random.randint(randomParameters[type1][3][0],randomParameters[type1][3][1])):
        randomPlay1.append(4)
    for _ in range(random.randint(randomParameters[type1][4][0],randomParameters[type1][4][1])):
        randomPlay1.append(6)
    return randomPlay1

toss = []

def Toss():
    a = input('Heads or Tails?\n>> ')
    if random.choice(['Heads',"Tails"]) == a:
        b = int(input("You won the toss!\n1. Bat\n2. Bowl\n>> "))
        toss.append(True)
        toss.append(b)
    else:
        toss.append(False)
        t = random.randint(1,2)
        toss.append(t)
        A = {1:'bat',2:'bowl'}
        print(f"England won the toss and decided to {A[t]} first!\n")
Toss()
def batting(partners,target,totalOvers,bowlsPlayed,oversPlayed,wicketsDown,runsScored,Next,a,c,Bowlers,Batsman,names,type1,current,fbfb,totalOvers1,bowlsPlayed1,oversPlayed1,wicketsDown1,runsScored1,a1,c1,Bowlers2,Batsman2):
    while (True):
        maindict = {2:"England",1:"India"}


        if type1!='test' and totalOvers == {'t20i':20,'odi':50}[type1]-1 or wicketsDown == 10:
            if target[0] == -5:
                target.remove(-5)
                target.append(runsScored+1)
                print(f"Target given to other side is {target[0]}")
                
                c1 = input("Choose the First Bowler: ")
                    
                bowling(target,totalOvers1, bowlsPlayed1,oversPlayed1,wicketsDown1,runsScored1,1,a1,c1,Bowlers2,Batsman2,names,type1,firstbattingfirstbowling,totalOvers, bowlsPlayed,oversPlayed,wicketsDown,runsScored,c,Bowlers,Batsman)
                
                return 
            else:
                if target[0]>runsScored:
                    print(f"{maindict[fbfb[0]]} Won the Match by {target[0]-runsScored} Runs!")
                    exit()
                elif target[0]<=runsScored:
                    print(f"{maindict[fbfb[1]]} Won the Match by {10-wicketsDown} Wickets!")
                    exit()
        def scorecard():
            if type1 == "t20i" or type1 == "odi":
                if target[0] !=-5:
                    a = target[0] - runsScored
                    b = {"t20i":120,"odi":300}[type1]
                    totalbowls = oversPlayed*6 + bowlsPlayed
                    rrr = round((a/(b-totalbowls))*6,2)
                print(f"{(f'Target: {target[0]} Runs | Required Run Rate: {rrr} | ') if target[0] != -5 else ''}Net Run Rate: {round((runsScored/(bowlsPlayed if bowlsPlayed !=0 else 1))*6, 2)}\nOvers: {oversPlayed if i!=5 else oversPlayed+1}.{i+1 if i!=5 else 0}\t\t\tScore: {runsScored}-{wicketsDown}\n{names[partners[0][0]]+'*' if Next==1 else names[partners[0][0]]}: {partners[0][1][0]}|{partners[0][1][1]}\t\t{names[partners[1][0]]+'*' if Next==0 else names[partners[1][0]]}: {partners[1][1][0]}|{partners[1][1][1]}\n\nCurrent Over: {' | '.join(currentOver)}\n{names[c]}: {Bowlers[c][0]}-{Bowlers[c][2]} | {Bowlers[c][1] if i!=5 else Bowlers[c][1]+1}.{i+1 if i!=5 else 0}")
            else:
                print(f"\nRun Rate: {round((runsScored/(bowlsPlayed if bowlsPlayed !=0 else 1))*6, 2)}\nOvers: {oversPlayed if i!=5 else oversPlayed+1}.{i+1 if i!=5 else 0}\t\t\tScore: {runsScored}-{wicketsDown}\n{names[partners[0][0]]+'*' if Next==1 else names[partners[0][0]]}: {partners[0][1][0]}|{partners[0][1][1]}\t\t{names[partners[1][0]]+'*' if Next==0 else names[partners[1][0]]}: {partners[1][1][0]}|{partners[1][1][1]}\n\nCurrent Over: {' | '.join(currentOver)}\n{names[c]}: {Bowlers[c][0]}-{Bowlers[c][2]} | {Bowlers[c][1] if i!=5 else Bowlers[c][1]+1}.{i+1 if i!=5 else 0}")
        totalOvers+=1
        currentOver = []
        for i in range(6):
            if target[0]<=runsScored and target[0]!=-5:
                print(f"{maindict[fbfb[1]]} Won the Match by {10-wicketsDown} Wickets!")
                exit()
            bowlsPlayed+=1
            while True:
                d = (input("Enter your choice: "))
                choice = random.choice(bowlerChoice)
                print(choice)
                try:
                    d = int(d)
                    some = totalw[d]
                    break
                except:
                    if d == "w":
                        active = 0 if Next == 1 else 1
                        print(f"{partners[active][0]}'s Wagon Wheel: {partners[active][1][2]}\nTeam Wagon Wheel: {totalw}") 
                    elif d == "b":
                        print(Bowlers)
                    elif d == "B":
                        print(Batsman)
                    elif d == "":
                        d = random.choice(randomPlay())
                        break
                    else:
                        print("Provide a valid input!")
            os.system("cls")
            if d == choice:
                active = 0 if Next == 1 else 1
                if Batsman[partners[active][0]][2]-1 != 0:
                    Batsman[partners[active][0]][2]-=1
                    print(f"One life gone for {names[partners[active][0]]}\nRemaining life: {Batsman[partners[active][0]][2]}")
                    partners[active][1][1]+=1
                    currentOver.append('0')
                    scorecard()
                    
                else:
                    active = 0 if Next == 1 else 1
                    wicketsDown+=1
                    Bowlers[c][2]+=1
                    partners[active][1][1]+=1
                    Batsman[partners[active][0]][0]+=partners[active][1][0]
                    Batsman[partners[active][0]][1]+=partners[active][1][1]
                    currentOver.append('W')
                    while True:
                        try:
                            a = input(f"{partners[active][0]} is out!\nChoose the next batsman!\n>> ")
                            partners[active] = [a,[0,0,{0:0, 1:0,2:0,3:0,4:0,6:0,-1:0}]]
                            D = Batsman[a]
                            break
                        except:
                            print("Batsman not found! Try Again..")
                    
                    scorecard()
            else:
                active = 0 if Next == 1 else 1
                partners[active][1][2][d]+=1
                totalw[d]+=1
                Bowlers[c][0]+=d
                partners[active][1][0]+=d
                partners[active][1][1]+=1
                # print(partners[active][1][3])
                runsScored+=d
                # print(f'before adding {Batsman[partners[active][0]][3][0]} and {partners[active][1][0]}')
                if partners[active][1][0] > 30 and Batsman[partners[active][0]][3][0]==False and partners[active][1][0] < 50:
                    print('inside 30 adding')
                    Batsman[partners[active][0]][2]+=random.randint(1,3)
                    Batsman[partners[active][0]][3][0]=True
                if partners[active][1][0]>50 and Batsman[partners[active][0]][3][1]==False and partners[active][1][0] < 100:
                    Batsman[partners[active][0]][2]+=random.randint(1,2)
                    Batsman[partners[active][0]][3][1]=True
                if partners[active][1][0]>100 and Batsman[partners[active][0]][3][2]==False:
                    Batsman[partners[active][0]][2]+=random.randint(1,2)
                    Batsman[partners[active][0]][3][2]=True              


                currentOver.append(str(d))
                if d%2 != 0:
                    # partners[active] = partners[Next]
                    nexttemp = 0 if Next == 1 else 1
                    Next = nexttemp
                else:
                    pass
                scorecard()
            
            
        
        # partners[active] = partners[Next]
        Bowlers[c][1]+=1
        oversPlayed+=1
        nexttemp = 0 if Next == 1 else 1
        Next = nexttemp
        print(f"Previous Bowler: {names[c]}")
        print(Bowlers)
        while True:
            C = random.choice(['woakes','archer','rashid','stokes','wood','liam'])
            main = {'odi':10,'t20i':4,'test':1000}
            if Bowlers[C][1]>=main[type1]:
                continue
            if C == c:
                continue
            else:
                break                
        c = C

def bowling(target,totalOvers1,bowlsPlayed1,oversPlayed1,wicketsDown1,runsScored1,Next,a1,c1,Bowlers2,Batsman2,names,type1,fbfb,totalOvers,bowlsPlayed,oversPlayed,wicketsDown,runsScored,c,Bowlers,Batsman):
    batterslist = list(Batsman2.keys())
    allout = 0
    def checkPercentage(n,m):
        mCount = 0
        for i in n:
            if i == m:
                mCount+=1
        return round((mCount/len(n))*100)
    
    bowler = []
    while (True):
        maindict = {2:"England",1:"India"}
        if type1 != 'test' and totalOvers1 == {'t20i':20,'odi':50}[type1]-1 or wicketsDown1 == 10:
            if target[0] == -5:
                target.remove(-5)
                target.append(runsScored1+1)
                print(f"Target given to other side is {target[0]} Runs")
                print("Available Batsman to chose from")
                for i,j in Batsman.items():
                    print("-> ",i)
                # a = input("Choose the First Batsman: ")
                # b = input("Choose the Second Batsman: ")
                while True:
                    a = input("Choose the First Batsman: ")
                    if a not in Batsman.keys():
                        print('Try again, batsman not in list.')
                        continue
                    else:
                        break
                while True:
                    b = input("Choose the Second Batsman: ")
                    if b not in Batsman.keys() or b==a:
                        print('Try again, batsman not in list or already chosed.')
                        continue
                    elif b!=a and b in Batsman.keys():
                        break
                    
                partners = [[a,[0,0,{0:0, 1:0,2:0,3:0,4:0,6:0,-1:0}]],[b,[0,0,{0:0,1:0,2:0,3:0,4:0,6:0,-1:0}]]]
                partners[active] = partners[0]
                print(f"Partner 1: {partners[0]} | Partner 2: {partners[1]}")
                batting(partners,target,totalOvers, bowlsPlayed,oversPlayed,wicketsDown,runsScored,1,a,c,Bowlers,Batsman,names,type1,partners[active],firstbattingfirstbowling,totalOvers1,bowlsPlayed1,oversPlayed1,wicketsDown1,runsScored1,a1,0,Bowlers2,Batsman2)

                return 
            else:
                if target[0]>runsScored1:
                    print(f"{maindict[fbfb[0]]} Won the Match by {target[0]-runsScored1} Runs!")
                    exit()
                elif target[0]<=runsScored1:
                    print(f"{maindict[fbfb[1]]} Won the Match by {10-wicketsDown1} Wickets!")
                    exit()

        def scorecard():
            if type1 == "t20i" or type1 == "odi":
                if target[0] != -5:
                    a = target[0] - runsScored1
                    # print(f"a: {a}")
                    b = {"t20i":120,"odi":300}[type1]
                    totalbowls = oversPlayed1*6 + bowlsPlayed1
                    # print(f"total bowls: {totalbowls}")
                    rrr = round((a/(b-totalbowls))*6,2)
                print(f"{(f'Target: {target[0]} Runs | Required Run Rate: {rrr} | ') if target[0] != -5 else ''}Net Run Rate: {round((runsScored1/(bowlsPlayed1 if bowlsPlayed1 !=0 else 1))*6, 2)}\nOvers: {oversPlayed1 if i!=5 else oversPlayed1+1}.{i+1 if i!=5 else 0}\t\t\tScore: {runsScored1}-{wicketsDown1}\n{names[partners1[0][0]]+'*' if Next==1 else names[partners1[0][0]]}: {partners1[0][1][0]}|{partners1[0][1][1]}\t\t{names[partners1[1][0]]+'*' if Next==0 else names[partners1[1][0]]}: {partners1[1][1][0]}|{partners1[1][1][1]}\n\nCurrent Over: {' | '.join(currentOver1)}\n{names[c1]}: {Bowlers2[c1][0]}-{Bowlers2[c1][2]} | {Bowlers2[c1][1] if i!=5 else Bowlers2[c1][1]+1}.{i+1 if i!=5 else 0}")
            else:
                print(f"\nRun Rate: {round((runsScored1/(bowlsPlayed1 if bowlsPlayed1 !=0 else 1))*6, 2)}\nOvers: {oversPlayed1 if i!=5 else oversPlayed1+1}.{i+1 if i!=5 else 0}\t\t\tScore: {runsScored1}-{wicketsDown1}\n{names[partners1[0][0]]+'*' if Next==1 else names[partners1[0][0]]}: {partners1[0][1][0]}|{partners1[0][1][1]}\t\t{names[partners1[1][0]]+'*' if Next==0 else names[partners1[1][0]]}: {partners1[1][1][0]}|{partners1[1][1][1]}\n\nCurrent Over: {' | '.join(currentOver1)}\n{names[c1]}: {Bowlers2[c1][0]}-{Bowlers2[c1][2]} | {Bowlers2[c1][1] if i!=5 else Bowlers2[c1][1]+1}.{i+1 if i!=5 else 0}")
        totalOvers1+=1
        currentOver1 = []
        for i in range(6):
            if target[0]<=runsScored1 and target[0]!=-5:
                print(f"{maindict[fbfb[1]]} Won the Match by {10-wicketsDown1} Wickets!")
                exit()
            bowlsPlayed1+=1
            while True:
                while True:
                    choice = input("Enter your choice of bowling: ")
                    d = random.choice(randomPlay())
                    try:
                        choice = int(choice)
                        some = True if choice in [1,2,3,4,6] else False
                        if some == True:
                            break
                    except:
                        if choice == "w":
                            active = 0 if Next == 1 else 1
                            print(f"{partners1[active][0]}'s Wagon Wheel: {partners1[active][1][2]}\nTeam Wagon Wheel: {totalw}") 
                        elif choice == "b":
                            print(Bowlers2)
                        elif choice == "B":
                            print(Batsman2)
                        elif choice == "":
                            choice = random.choice(bowlerChoice)
                            break
                        else:
                            print("Provide a valid input!")
                if len(bowler)>4 and checkPercentage(bowler,choice) > 30:
                    print(f"Exhausted {choice}--> Try another number!")
                    continue
                else:
                    bowler.append(choice)

                    break

            os.system("cls")
            if d == choice:
                active = 0 if Next == 1 else 1
                if Batsman2[partners1[active][0]][2]-1 != 0:
                    Batsman2[partners1[active][0]][2]-=1
                    print(f"One life gone for {names[partners1[active][0]]}\nRemaining life: {Batsman2[partners1[active][0]][2]}")
                    partners1[active][1][1]+=1
                    currentOver1.append('0')
                    scorecard()
                    
                else:
                    active = 0 if Next == 1 else 1

                    wicketsDown1+=1
                    Bowlers2[c1][2]+=1
                    partners1[active][1][1]+=1
                    Batsman2[partners1[active][0]][0]+=partners1[active][1][0]
                    Batsman2[partners1[active][0]][1]+=partners1[active][1][1]
                    currentOver1.append('W')
                    batterslist.remove(partners1[active][0])
                    while True:
                        try:
                            a1 = batterslist[1]
                            print(f"{names[partners1[active][0]]} is out!\nNext Batsman coming: {names[batterslist[1]]}\n")
                            partners1[active] = [a1,[0,0,{0:0, 1:0,2:0,3:0,4:0,6:0,-1:0}]]
                            D = Batsman2[a1]
                            break
                        except:
                            a1 = batterslist[0]
                            print("Team all out!")
                            partners1[active] = [a1,[0,0,{0:0, 1:0,2:0,3:0,4:0,6:0,-1:0}]]
                            D = Batsman2[a1]
                            allout = True
                            break
                    if allout==True:
                        break
                    scorecard()
            else:
                active = 0 if Next == 1 else 1
                partners1[active][1][2][d]+=1
                totalw[d]+=1
                try:
                    Bowlers2[c1][0]+=d
                except:
                    c1 = random.choice(list(Bowlers2.keys()))
                    Bowlers2[c1][0]+=d
                partners1[active][1][0]+=d
                partners1[active][1][1]+=1
                runsScored1+=d
                # print(f'before adding {Batsman[partners[active][0]][3][0]} and {partners[active][1][0]}')
                if partners1[active][1][0] > 30 and Batsman2[partners1[active][0]][3][0]==False:
                    print('inside 30 adding')
                    Batsman2[partners1[active][0]][2]+=random.randint(1,3)
                    Batsman2[partners1[active][0]][3][0]=True
                if partners1[active][1][0]>50 and Batsman2[partners1[active][0]][3][1]==False:
                    Batsman2[partners1[active][0]][2]+=random.randint(1,2)
                    Batsman2[partners1[active][0]][3][1]=True
                if partners1[active][1][0]>100 and Batsman2[partners1[active][0]][3][2]==False:
                    Batsman2[partners1[active][0]][2]+=random.randint(1,2)
                    Batsman2[partners1[active][0]][3][2]=True   
                currentOver1.append(str(d))
                if d%2 != 0:
                    nexttemp = 0 if Next == 1 else 1
                    Next = nexttemp
                else:
                    pass
                scorecard()
        Bowlers2[c1][1]+=1
        oversPlayed1+=1
        nexttemp = 0 if Next == 1 else 1
        Next = nexttemp
        print(f"Your Previous Bowler: {names[c1]}")
        print(Bowlers2)
        while True:
            C = input("Enter the next bowler\n>> ")
            C = C if C != "" else random.choice(list(Bowlers2.keys()))
            main = {'odi':10,'t20i':4,'test':1000}
            if C not in list(Bowlers2.keys()):
                print("Select a valid bowler")
                continue
            elif Bowlers2[C][1]>=main[type1]:
                print("This bowler has exhausted all his overs!")
                continue
            elif C == c1:
                print("Same bower can't bowl 2 consecutive overs!")
                continue
            else:
                break                
        c1 = C

a1 = list(Batsman2.keys())[0]
b1 = list(Batsman2.keys())[1]
partners1 = [[a1,[0,0,{0:0, 1:0,2:0,3:0,4:0,6:0,-1:0}]],[b1,[0,0,{0:0,1:0,2:0,3:0,4:0,6:0,-1:0}]]]
totalOvers1 = -1
bowlsPlayed1 = 0
oversPlayed1 = 0
wicketsDown1 = 0
firstbattingfirstbowling = [2,1]
runsScored1 = 0
target = [-5]

c = random.choice(list(Bowlers.keys()))
oversPlayed = 0
wicketsDown = 0
runsScored = 0
totalOvers = -1
firstbattingfirstbowling = [1,2]
bowlsPlayed = 0
if toss[0] == True and toss[1] == 2 or toss[0] == False and toss[1] == 1:
    print(Bowlers2)
    c1 = input("Choose the First Bowler: ")
    firstbattingfirstbowling = [2,1]

    
    bowling(target,totalOvers1, bowlsPlayed1,oversPlayed1,wicketsDown1,runsScored1,1,a1,c1,Bowlers2,Batsman2,names,type1,firstbattingfirstbowling,totalOvers, bowlsPlayed,oversPlayed,wicketsDown,runsScored,c,Bowlers,Batsman)
if toss[0] == True and toss[1] == 1 or toss[0] == False and toss[1] == 2:
    print("Available Batsman to chose from")
    for i,j in Batsman.items():
        print("-> ",i)
    while True:
        a = input("Choose the First Batsman: ")
        if a not in Batsman.keys():
            print('Try again, batsman not in list.')
            continue
        else:
            break
    while True:
        b = input("Choose the Second Batsman: ")
        if b not in Batsman.keys() or b==a:
            print('Try again, batsman not in list or already chosed.')
            continue
        else:
            break
        
    firstbattingfirstbowling = [1,2]

    partners = [[a,[0,0,{0:0, 1:0,2:0,3:0,4:0,6:0,-1:0}]],[b,[0,0,{0:0,1:0,2:0,3:0,4:0,6:0,-1:0}]]]
    # print(partners[0][1][3][0])
    current = partners[0]

    batting(partners,target,totalOvers, bowlsPlayed,oversPlayed,wicketsDown,runsScored,1,a,c,Bowlers,Batsman,names,type1,current,firstbattingfirstbowling,totalOvers1,bowlsPlayed1,oversPlayed1,wicketsDown1,runsScored1,a1,0,Bowlers2,Batsman2)


