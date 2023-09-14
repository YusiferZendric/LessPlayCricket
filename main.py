import random
import os
# import openai
global partners, c, type1, allout, EnglishBatsman, IndianBatsman, IndianBowlers, EnglishBowlers
with open('highlights.txt', 'w') as e:
  e.write("")
EnglishBowlers = {
    "afridi": [0, 0, 0],
    "shah": [0, 0, 0],
    "ashraf": [0, 0, 0],
    "rauf": [0, 0, 0],
    "khan": [0, 0, 0],
    "ahmed": [0, 0, 0]
}  #livingston,mohd ali, sam curran, chris jordan
with open('highlights.txt', 'w') as c:
  c.write("")
IndianBowlers = {
    "bumrah": [0, 0, 0],
    "siraj": [0, 0, 0],
    "pandya": [0, 0, 0],
    "thakur": [0, 0, 0],
    "yadav": [0, 0, 0],
    "jadeja": [0, 0, 0]
}

names = {
    "sharma": "Rohit Sharma",
    "gill": "Shubhman gill",
    "kohli": "Virat Kohli (C)",
    "rahul": "KL Rahul",
    "kishan": "Ishan Kishan (WK)",
    "pandya": "Hardik Pandya",
    "jadeja": "Ravindra Jadeja",
    "thakur": "Shardul Thakur",
    "yadav": "Kuldeep Yadav",
    "siraj": "Mohammed Siraj",
    "bumrah": "Jasprit Bumrah",
    "zaman": "Fakhar Zaman",
    "haq": "Imam-ul-Haq",
    "azam": 'Babar Azam (C)',
    "rizwan": "Mohammad Rizwan (WK)",
    "agha": "Salman Ali Agha",
    "ashraf": "Faheem Ashraf",
    "afridi": "Shaheen Afridi",
    "shah": "Naseem Shah",
    "rauf": "Haris Rauf",
    "ahmed": "Iftikhar Ahmed",
    "khan": "Shadab Khan"
}
while True:
  type1 = [
      'test', 'odi', 't20i'
  ][int(input(
      "What type of match do you want?\n1. test\n2. odi\n3. t20i\n>> ")) - 1]
  if type1 not in ['odi', 't20i', 'test']:
    print('try again! between (odi, t20i, test)')
    continue
  else:
    break
arg = {'odi': 9, "test": 8, 't20i': 5}[type1]
IndianBatsman = {
    "sharma": [0, 0,
              random.randint(1, arg), [False, False, False], [0, 0]],
    "gill": [0, 0,
              random.randint(1, arg), [False, False, False], [0, 0]],
    "rahul":
    [0, 0, random.randint(1, arg - 1), [False, False, False], [0, 0]],
    "kohli": [0, 0,
              random.randint(1, arg+1), [False, False, False], [0, 0]],
    "kishan": [0, 0,
             random.randint(1, arg - 1), [False, False, False], [0, 0]],
    "pandya":
    [0, 0, random.randint(1, arg - 2), [False, False, False], [0, 0]],
    "jadeja":
    [0, 0, random.randint(1, arg - 3), [False, False, False], [0, 0]],
    "thakur": [0, 0,
              random.randint(1, arg - 3), [False, False, False], [0, 0]],
    "yadav": [0, 0, random.randint(1, 2), [False, False, False], [0, 0]],
    "siraj": [0, 0, random.randint(1, 2), [False, False, False], [0, 0]],
    "bumrah": [0, 0, random.randint(1, 2), [False, False, False], [0, 0]]
}
EnglishBatsman = {
    "zaman": [0, 0, random.randint(1, arg), [False, False, False], [0, 0]],
    "haq": [0, 0,
                random.randint(1, arg), [False, False, False], [0, 0]],
    "azam": [0, 0,
              random.randint(1, arg + 1), [False, False, False], [0, 0]],
    "rizwan": [0, 0,
                  random.randint(1, arg-1), [False, False, False], [0, 0]],
    "agha":
    [0, 0, random.randint(1, arg - 1), [False, False, False], [0, 0]],
    "ahmed":
    [0, 0, random.randint(1, arg - 2), [False, False, False], [0, 0]],
    "khan": [0, 0,
             random.randint(1, arg - 3), [False, False, False], [0, 0]],
    "ashraf":
    [0, 0, random.randint(1, arg - 3), [False, False, False], [0, 0]],
    "afridi": [0, 0, random.randint(1, 2), [False, False, False], [0, 0]],
    "shah": [0, 0, random.randint(1, 2), [False, False, False], [0, 0]],
    "rauf": [0, 0, random.randint(1, 2), [False, False, False], [0, 0]]
}
totalw = {
    'Pakistan': {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        6: 0,
        -1: 0
    },
    "India": {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        6: 0,
        -1: 0
    }
}
combinedStars = 0
combinedStars2 = 0
for i, j in IndianBatsman.items():
  combinedStars += j[2]
for i, j in EnglishBatsman.items():
  combinedStars2 += j[2]
bowlerChoice = []
battinglist = list(IndianBatsman.keys())


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
  bowlsetup([14, 21, 26, 34])
if type1 == "odi":
  bowlsetup([9, 16, 31, 42])
if type1 == "test":
  bowlsetup([11, 12, 21, 57])


def randomPlay(perc, team):
  totalStars = 0
  reqStars = 0
  choice = ''
  if team == "India":
    totalStars = combinedStars
    for i, j in IndianBatsman.items():
      reqStars += j[2]
  if team == "Pakistan":
    totalStars = combinedStars2
    for i, j in EnglishBatsman.items():
      reqStars += j[2]
  starsRemains = round((reqStars / totalStars) * 100)

  if perc > 0 and perc < 25 and starsRemains > 90:
    choice = 'attack'
  if perc > 0 and perc < 25 and starsRemains < 85 and starsRemains > 75:
    choice = 'neutral'
  if perc > 0 and perc < 25 and starsRemains < 75:
    choice = 'defense'
  if perc > 25 and perc < 75 and starsRemains > 85:
    choice = 'attack'
  if perc > 25 and perc < 75 and starsRemains < 85 and starsRemains > 65:
    choice == 'neutral'
  if perc > 25 and perc < 75 and starsRemains < 65:
    choice = 'defense'
  if perc > 25 and perc < 75 and starsRemains < 45:
    choice = 'super defense'
  if perc > 75 and starsRemains > 65:
    choice = 'super attack'
  if perc > 75 and starsRemains < 65 and starsRemains > 45:
    choice = 'attack'
  if perc > 75 and starsRemains < 45 and starsRemains > 25:
    choice = 'neutral'
  if perc > 75 and starsRemains < 25:
    choice = 'defense'
  if choice == "": choice = 'neutral'
  # input(f"")

  randomParameters = {
      'neutral': {
          'test':
          [[random.randint(25, 30), 50], [4, 18], [1, 7],
           [3, random.randint(4, 11)],
           [0, random.randint(1, random.randint(2, random.randint(3, 4)))]],
          'odi': [[19, 30], [6, 15], [random.randint(2, 4), 8],
                  [random.randint(3, 5),
                   random.randint(8, 14)],
                  [random.randint(0, 4),
                   random.randint(4, 7)]],
          't20i':
          [[9, 17], [8, 19], [random.randint(2, 5), 9],
           [6, random.randint(9, 15)],
           [random.randint(1, 4),
            random.randint(4, random.randint(8, 11))]]
      },
      'attack': {
          'test':
          [[random.randint(25, 30), 50], [4, 18], [1, 7],
           [3, random.randint(4, 11)],
           [0, random.randint(1, random.randint(2, random.randint(3, 4)))]],
          'odi': [[9, 18], [10, 22], [random.randint(2, 4), 8],
                  [random.randint(5, 8),
                   random.randint(10, 17)],
                  [random.randint(1, 5),
                   random.randint(6, 10)]],
          't20i':
          [[7, 15], [9, 22], [random.randint(2, 4), 10],
           [8, random.randint(10, 15)],
           [random.randint(2, 4),
            random.randint(5, random.randint(8, 13))]]
      },
      'defense': {
          'test':
          [[random.randint(25, 30), 50], [4, 18], [1, 7],
           [3, random.randint(4, 11)],
           [0, random.randint(1, random.randint(2, random.randint(3, 4)))]],
          'odi': [[24, 39], [5, 13], [random.randint(2, 4), 6],
                  [random.randint(3, 5),
                   random.randint(6, 13)],
                  [random.randint(0, 2),
                   random.randint(3, 6)]],
          't20i':
          [[11, 22], [15, 22], [random.randint(2, 5), 10],
           [2, random.randint(2, 7)],
           [random.randint(0, 2),
            random.randint(3, random.randint(3, 5))]]
      },
      'super attack': {
          'test':
          [[random.randint(25, 30), 50], [4, 18], [1, 7],
           [3, random.randint(4, 11)],
           [0, random.randint(1, random.randint(2, random.randint(3, 4)))]],
          'odi': [[8, 16], [9, 20], [random.randint(2, 5), 11],
                  [random.randint(6, 10),
                   random.randint(10, 20)],
                  [random.randint(2, 5),
                   random.randint(6, 12)]],
          't20i':
          [[4, 9], [11, 20], [random.randint(2, 6), 10],
           [7, random.randint(8, 15)],
           [random.randint(2, 5),
            random.randint(6, random.randint(7, 12))]]
      },
      'super defense': {
          'test':
          [[random.randint(25, 30), 50], [4, 18], [1, 7],
           [3, random.randint(4, 11)],
           [0, random.randint(1, random.randint(2, random.randint(3, 4)))]],
          'odi': [[30, 45], [9, 19], [random.randint(3, 5), 8],
                  [random.randint(2, 4),
                   random.randint(4, 9)],
                  [random.randint(0, 2),
                   random.randint(3, 4)]],
          't20i':
          [[15, 27], [18, 25], [random.randint(2, 4), 9],
           [1, random.randint(2, 5)],
           [random.randint(0, 2),
            random.randint(3, random.randint(3, 4))]]
      }
  }

  randomPlay1 = []
  for _ in range(
      random.randint(randomParameters[choice][type1][0][0],
                     randomParameters[choice][type1][0][1])):
    randomPlay1.append(0)
  for _ in range(
      random.randint(randomParameters[choice][type1][1][0],
                     randomParameters[choice][type1][1][1])):
    randomPlay1.append(1)
  for _ in range(
      random.randint(randomParameters[choice][type1][2][0],
                     randomParameters[choice][type1][2][1])):
    randomPlay1.append(2)
  for _ in range(
      random.randint(randomParameters[choice][type1][3][0],
                     randomParameters[choice][type1][3][1])):
    randomPlay1.append(4)
  for _ in range(
      random.randint(randomParameters[choice][type1][4][0],
                     randomParameters[choice][type1][4][1])):
    randomPlay1.append(6)
  # input(f"randomplay: {randomPlay1} and {starsRemains} and {choice} and {perc}%")
  return randomPlay1


toss = []


def SaveScores(text):
  with open("highlights.txt", 'a') as a:
    a.write(text)


SaveScores(f"{type1} match between India vs Pakistan\n")


def Toss():
  a = random.choice(['Heads', 'Tails'])
  if random.choice(['Heads', "Tails"]) == a:
    A = {1: 'bat', 2: 'bowl'}
    # b = random.randint(1, 2)
    b = int(input(("India won the toss, what to do? (chose the corresponding number) \n1. Bat\n2. Bowl\n")))
    toss.append(True)
    toss.append(b)
    SaveScores(f"India won the toss and decided to {A[b]} first!\n")
    print(f"India won the toss and decided to {A[b]} first!\n")
  else:
    toss.append(False)
    t = random.randint(1, 2)
    toss.append(t)
    A = {1: 'bat', 2: 'bowl'}
    SaveScores(f"Pakistan won the toss and decided to {A[t]} first!\n")
    print(f"Pakistan won the toss and decided to {A[t]} first!\n")


Toss()


def batting(partners, target, totalOvers, bowlsPlayed, oversPlayed,
            wicketsDown, runsScored, Next, a, c, EnglishBowlers, IndianBatsman,
            names, type1, current, fbfb, totalOvers1, bowlsPlayed1,
            oversPlayed1, wicketsDown1, runsScored1, a1, c1, IndianBowlers,
            EnglishBatsman):
  batterslist = list(IndianBatsman.keys())
  batterchoices = []
  while (True):
    maindict = {2: "Pakistan", 1: "India"}

    if type1 != 'test' and totalOvers == {
        't20i': 20,
        'odi': 50
    }[type1] - 1 or wicketsDown == 10:

      if target[0] == -5:
        target.remove(-5)
        target.append(runsScored + 1)
        for i, j in IndianBatsman.items():
          if j[1] != 0 and j[2] != 0:
            SaveScores(
                f"Indian player {names[i]} is Not Out with {j[0]} Runs in {j[1]} Bowls\n"
            )
        SaveScores(
            f"Pakistan has to chase down {target[0]} runs, set by India\n")
        print(f"Target for Pakistan team: {target[0]}")
        print(f"Batsman: {IndianBatsman}")
        for bowlers, j in IndianBowlers.items():
          print("->", bowlers)
          pass
        while True:       
          c1 = input("Choose the First Bowler: ")
          if c1 not in list(IndianBowlers.keys()):
              print("Chose a valid bowler")
              continue
          else:
              break

        bowling(target, totalOvers1, bowlsPlayed1, oversPlayed1, wicketsDown1,
                runsScored1, 1, a1, c1, IndianBowlers, EnglishBatsman, names,
                type1, firstbattingfirstbowling, totalOvers, bowlsPlayed,
                oversPlayed, wicketsDown, runsScored, c, EnglishBowlers,
                IndianBatsman)

        return
      else:
        if target[0] > runsScored:
          for i, j in IndianBatsman.items():
            if j[1] != 0 and j[2] != 0:
              SaveScores(
                  f"Indian player {names[i]} is Not Out with {j[0]} Runs in {j[1]}  Bowls\n"
              )
          print(
              f"{maindict[fbfb[0]]} Won the Match by {target[0]-runsScored} Runs!"
          )
          SaveScores(
              f"{maindict[fbfb[0]]} Won the Match by {target[0]-runsScored} Runs!\n"
          )

        elif target[0] <= runsScored:
          for i, j in IndianBatsman.items():
            if j[1] != 0 and j[2] != 0:
              SaveScores(
                  f"Indian player {names[i]} is Not Out with {j[0]} Runs in {j[1]}  Bowls\n"
              )
          print(
              f"{maindict[fbfb[1]]} Won the Match by {10-wicketsDown} Wickets!"
          )
          SaveScores(
              f"{maindict[fbfb[1]]} Won the Match by {10-wicketsDown} Wickets!\n"
          )
        SaveScores("Indian Team\n")
        for i, j in IndianBatsman.items():
          SaveScores(
              f"{names[i]}: {j[0]} Runs | {j[1]} Bowls | {j[4][0]} Fours | {j[4][1]} Sixes\n"
          )
        SaveScores("Pakistani Team\n")
        for i, j in EnglishBatsman.items():
          SaveScores(
              f"{names[i]}: {j[0]} Runs | {j[1]} Bowls | {j[4][0]} Fours | {j[4][1]} Sixes\n"
          )
        SaveScores("Indian Bowlers\n")
        for i, j in IndianBowlers.items():
          SaveScores(
              f"{names[i]}: {j[0]} Runs | {j[1]} Overs | {j[2]} wickets\n")
        SaveScores("Pakistani Bowlers\n")
        for i, j in EnglishBowlers.items():
          SaveScores(
              f"{names[i]}: {j[0]} Runs | {j[1]} Overs | {j[2]} wickets\n")
        SaveScores(f"India: {runsScored}-{wicketsDown}\n")
        SaveScores(f"Pakistan: {runsScored1}-{wicketsDown1}\n")
        with open("highlights.txt") as e:
          print(e.read())
        # print(commentry())
        exit()

    def scorecard():
      if type1 == "t20i" or type1 == "odi":
        if target[0] != -5:
          a = target[0] - runsScored
          b = {"t20i": 120, "odi": 300}[type1]
          totalbowls = bowlsPlayed
          # print(totalbowls)
          # print(a)
          rrr = round((a/(b-totalbowls))*6,2)
        print(
            f"{(f'Target: {target[0]} Runs | Required Run Rate: {rrr} | ') if target[0] != -5 else ''}Net Run Rate: {round((runsScored/(bowlsPlayed if bowlsPlayed !=0 else 1))*6, 2)}\nOvers: {oversPlayed if i!=5 else oversPlayed+1}.{i+1 if i!=5 else 0}\t\t\tScore: {runsScored}-{wicketsDown}\n{names[partners[0][0]]+'*' if Next==1 else names[partners[0][0]]}: {partners[0][1][0]}|{partners[0][1][1]}\t\t{names[partners[1][0]]+'*' if Next==0 else names[partners[1][0]]}: {partners[1][1][0]}|{partners[1][1][1]}\n\nCurrent Over: {' | '.join(currentOver)}\n{names[c]}: {EnglishBowlers[c][0]}-{EnglishBowlers[c][2]} | {EnglishBowlers[c][1] if i!=5 else EnglishBowlers[c][1]+1}.{i+1 if i!=5 else 0}"
        )
      # elif type1 == 't20i' and type1 'odi'
      else:
        print(
            f"\nRun Rate: {round((runsScored/(bowlsPlayed if bowlsPlayed !=0 else 1))*6, 2)}\nOvers: {oversPlayed if i!=5 else oversPlayed+1}.{i+1 if i!=5 else 0}\t\t\tScore: {runsScored}-{wicketsDown}\n{names[partners[0][0]]+'*' if Next==1 else names[partners[0][0]]}: {partners[0][1][0]}|{partners[0][1][1]}\t\t{names[partners[1][0]]+'*' if Next==0 else names[partners[1][0]]}: {partners[1][1][0]}|{partners[1][1][1]}\n\nCurrent Over: {' | '.join(currentOver)}\n{names[c]}: {EnglishBowlers[c][0]}-{EnglishBowlers[c][2]} | {EnglishBowlers[c][1] if i!=5 else EnglishBowlers[c][1]+1}.{i+1 if i!=5 else 0}"
        )
        pass
      
    totalOvers += 1
    currentOver = []
    for i in range(6):
      if target[0] <= runsScored and target[0] != -5:
        for i, j in IndianBatsman.items():
          if j[1] != 0 and j[2] != 0:
            SaveScores(
                f"Indian player {names[i]} is Not Out with {j[0]} Runs in {j[1]} Bowls\n"
            )
        print(
            f"{maindict[fbfb[1]]} Won the Match by {10-wicketsDown} Wickets!")
        SaveScores(
            f"{maindict[fbfb[1]]} Won the Match by {10-wicketsDown} Wickets!")
        SaveScores("Indian Team\n")
        for i, j in IndianBatsman.items():
          SaveScores(
              f"{names[i]}: {j[0]} Runs | {j[1]} Bowls | {j[4][0]} Fours | {j[4][1]} Sixes\n"
          )
        SaveScores("Pakistani Team\n")
        for i, j in EnglishBatsman.items():
          SaveScores(
              f"{names[i]}: {j[0]} Runs | {j[1]} Bowls | {j[4][0]} Fours | {j[4][1]} Sixes\n"
          )
        SaveScores("Indian Bowlers\n")
        for i, j in IndianBowlers.items():
          SaveScores(
              f"{names[i]}: {j[0]} Runs | {j[1]} Overs | {j[2]} wickets\n")
        SaveScores("Pakistani Bowlers\n")
        for i, j in EnglishBowlers.items():
          SaveScores(
              f"{names[i]}: {j[0]} Runs | {j[1]} Overs | {j[2]} wickets\n")
        SaveScores(f"India: {runsScored}-{wicketsDown}\n")
        SaveScores(f"Pakistan: {runsScored1}-{wicketsDown1}\n")
        with open("highlights.txt") as e:
          print(e.read())
          # print(commentry())
      bowlsPlayed += 1

      battingTeam = 1
      while True:

        d = input("Enter your choice (in numbers. ex: 0,1,2,4,6): ")
        # print(IndianBatsman)
        choice = random.choice(bowlerChoice)
        # print(choice)
        try:
          # print(f"D error: {type(d)} {d}")
          d = int(d)
          batterchoices.append(d)

          if round((batterchoices.count(d) / len(batterchoices)) *
                   100) > 35 and d == 6 and len(batterchoices) > 6:
            print("6 Quota full. Try other options!")
            continue
          if round((batterchoices.count(d) / len(batterchoices)) *
                   100) > 55 and d == 4 and len(batterchoices) > 6:
            print("4 Quota full. Try other options!")
            continue

          some = totalw[maindict[fbfb[0]]][d]
          break
        except:
          if d == "w":
            active = 0 if Next == 1 else 1
            print(
                f"{partners[active][0]}'s Wagon Wheel: {partners[active][1][2]}\nTeam Wagon Wheel: {totalw[maindict[battingTeam]]}"
            )
          elif d == "b":
            print(EnglishBowlers)
            # pass
          elif d == "B":
            print(IndianBatsman)
            # break
            # pass
          elif d == "":
            reqdict = {'t20i': 120, 'odi': 300, 'test':10000}[type1]
            totalss = round((bowlsPlayed / reqdict) * 100)
            # input(f"{totalss}:{bowlsPlayed}:{reqdict}")

            d = random.choice(randomPlay(totalss, "India"))
            batterchoices.append(d)
            if round((batterchoices.count(d) / len(batterchoices)) *
                     100) > 35 and d == 6 and len(batterchoices) > 6:
              print("6 Quota full. Try other options!")
              continue
            if round((batterchoices.count(d) / len(batterchoices)) *
                     100) > 55 and d == 4 and len(batterchoices) > 6:
              print("4 Quota full. Try other options!")
              continue
            break

          else:
            print("Provide a valid input!")
            pass
      os.system("cls")
      if d == choice:
        active = 0 if Next == 1 else 1
        if IndianBatsman[partners[active][0]][2] - 1 > 0:
          IndianBatsman[partners[active][0]][2] -= 1
          print(
              f"One life gone for {names[partners[active][0]]}\nRemaining life: {IndianBatsman[partners[active][0]][2]}"
          )
          partners[active][1][1] += 1
          IndianBatsman[partners[active][0]][1] += 1

          currentOver.append('0')
          scorecard()

        elif IndianBatsman[partners[active][0]][2] - 1 == 0:
          IndianBatsman[partners[active][0]][2] = 0
          print("Batsman: ", IndianBatsman)
          active = 0 if Next == 1 else 1
          wicketsDown += 1
          EnglishBowlers[c][2] += 1
          partners[active][1][1] += 1
          # IndianBatsman[partners[active][0]][0]+=partners[active][1][0]
          IndianBatsman[partners[active][0]][1] += 1
          # print(c)
          SaveScores(
              f"Indian Player {names[partners[active][0]]} out after scoring {IndianBatsman[partners[active][0]][0]} Runs | {IndianBatsman[partners[active][0]][1]} Bowls, wicket by bowler {names[c]} | Current Wicket count of {names[c]}: {EnglishBowlers[c][2]} wickets Bowler has bowled {EnglishBowlers[c][1]} overs and given {EnglishBowlers[c][0]} Runs\n"
          )
          currentOver.append('W')
          for batsman, second in IndianBatsman.items():
            print("-> ", batsman)
            pass
          if wicketsDown == 10 or len(batterslist) == 1:
            print("Team All out! :(")
            SaveScores(f"Team India all out!\n")
            break
            # print("Team all out!")
            # partners1[active] = [a1,[0,0,{0:0, 1:0,2:0,3:0,4:0,6:0,-1:0}]]
            # D = EnglishBatsman[a1]
            # break
            # allout = True

          try:
            batterslist.remove(partners[1][0])
          except:
            pass
          try:

            batterslist.remove(partners[0][0])
          except:
            pass

          # print(f"{batterslist}")
          while True:

            # print(batterslist)
            
            a = input(
                f"{partners[active][0]} is out!\nChoose the next Batsman! (respond with 'B' to look for names) \n>> "
            )
            
              # continue


            # if a in partners1[0] or a in partners[1]:
            #     a = batterslist[0]
            
            if a not in batterslist:
              if a == 'B':
                print(f"Available Batsman next: {batterslist}")
                # print('Batsman already used! Choose any other.')
              else:
                print('Batsman already used! Choose any other.')

              # continue
            elif a in batterslist:
              partners[active] = [
                  a, [0, 0, {
                      0: 0,
                      1: 0,
                      2: 0,
                      3: 0,
                      4: 0,
                      6: 0,
                      -1: 0
                  }]
              ]
              # D = IndianBatsman[a]
              break

          scorecard()
      else:
        active = 0 if Next == 1 else 1
        partners[active][1][2][d] += 1
        totalw[maindict[battingTeam]][d] += 1
        EnglishBowlers[c][0] += d
        partners[active][1][0] += d
        # print(IndianBatsman)
        if d == 6: IndianBatsman[partners[active][0]][4][1] += 1
        if d == 4: IndianBatsman[partners[active][0]][4][0] += 1
        partners[active][1][1] += 1
        IndianBatsman[partners[active][0]][0] += d
        IndianBatsman[partners[active][0]][1] += 1
        # print(partners[active][1][3])
        runsScored += d
        # print(f'before adding {IndianBatsman[partners[active][0]][3][0]} and {partners[active][1][0]}')
        if partners[active][1][0] > 30 and IndianBatsman[partners[active][0]][
            3][0] == False and partners[active][1][0] < 50:
          # print('inside 30 adding')
          IndianBatsman[partners[active][0]][2] += random.randint(1, 2)
          IndianBatsman[partners[active][0]][3][0] = True
        if partners[active][1][0] > 50 and IndianBatsman[partners[active][0]][
            3][1] == False and partners[active][1][0] < 100:
          IndianBatsman[partners[active][0]][2] += random.randint(1, 2)
          IndianBatsman[partners[active][0]][3][1] = True
        if partners[active][1][0] > 100 and IndianBatsman[partners[active]
                                                          [0]][3][2] == False:
          IndianBatsman[partners[active][0]][2] += random.randint(1, 2)
          IndianBatsman[partners[active][0]][3][2] = True

        currentOver.append(str(d))
        if d % 2 != 0:
          # partners[active] = partners[Next]
          nexttemp = 0 if Next == 1 else 1
          Next = nexttemp
        else:
          pass
        scorecard()

    # partners[active] = partners[Next]
    EnglishBowlers[c][1] += 1
    oversPlayed += 1
    nexttemp = 0 if Next == 1 else 1
    Next = nexttemp
    print(f"Previous Bowler: {names[c]}")
    # print(EnglishBowlers)
    while True:
      C = random.choice(
          list(EnglishBowlers.keys()))
      main = {'odi': 10, 't20i': 4, 'test': 1000}
      if EnglishBowlers[C][1] >= main[type1]:
        continue
      if C == c:
        continue
      else:
        break
    c = C


def bowling(target, totalOvers1, bowlsPlayed1, oversPlayed1, wicketsDown1,
            runsScored1, Next, a1, c1, IndianBowlers, EnglishBatsman, names,
            type1, fbfb, totalOvers, bowlsPlayed, oversPlayed, wicketsDown,
            runsScored, c, EnglishBowlers, IndianBatsman):
  batterslist = list(EnglishBatsman.keys())
  allout = 0

  def checkPercentage(n, m):
    mCount = 0
    for i in n:
      if i == m:
        mCount += 1
    return round((mCount / len(n)) * 100)

  bowler = []
  while (True):
    maindict = {2: "Pakistan", 1: "India"}
    if type1 != 'test' and totalOvers1 == {
        't20i': 20,
        'odi': 50
    }[type1] - 1 or wicketsDown1 == 10:
      if target[0] == -5:
        target.remove(-5)
        target.append(runsScored1 + 1)
        for i, j in EnglishBatsman.items():
          if j[1] != 0 and j[2] != 0:
            SaveScores(
                f"Pakistani Player {names[i]} is Not Out with {j[0]} Runs in {j[1]} Bowls\n"
            )
        print(f"Target for India to chase: {target[0]} Runs")
        # print(f"EnglishBatsman: {EnglishBatsman}")
        SaveScores(
            f"India has to chase down {target[0]} runs, set by Pakistan\n")

        print("Available Batsman to chose from")
        for i, j in IndianBatsman.items():
          print("-> ", i)

        while True:
          a = input(
              "Choose the First Batsman (through short name. ex: kishan, kohli etc): "
          )

          # a = list(IndianBatsman.keys())[0]
          if a not in IndianBatsman.keys():
            print('Try again, Batsman not in list.')
          else:
            break
        while True:
          # b = list(IndianBatsman.keys())[1]
          b = input(
              "Choose the Second Batsman (through short name. ex: kishan, kohli etc): "
          )

          if b not in IndianBatsman.keys() or b == a:
            print('Try again, Batsman not in list or already chosed.')
            continue
          elif b != a and b in IndianBatsman.keys():
            break

        partners = [[a, [0, 0, {
            0: 0,
            1: 0,
            2: 0,
            3: 0,
            4: 0,
            6: 0,
            -1: 0
        }]], [b, [0, 0, {
            0: 0,
            1: 0,
            2: 0,
            3: 0,
            4: 0,
            6: 0,
            -1: 0
        }]]]
        partners[active] = partners[0]
        if partners[0][0] == partners[1][0]:
          print('both mf are same')
          partners[0][0] = list(IndianBatsman.keys())[0]
          partners[1][0] = list(IndianBatsman.keys())[1]
          # continue
          batting(partners, target, totalOvers, bowlsPlayed, oversPlayed,
                  wicketsDown, runsScored, 1, a, c, EnglishBowlers,
                  IndianBatsman, names, type1, partners[active],
                  firstbattingfirstbowling, totalOvers1, bowlsPlayed1,
                  oversPlayed1, wicketsDown1, runsScored1, a1, 0,
                  IndianBowlers, EnglishBatsman)
          # break
          break
        else:
          print(f"Partner 1: {partners[0]} | Partner 2: {partners[1]}")
          batting(partners, target, totalOvers, bowlsPlayed, oversPlayed,
                  wicketsDown, runsScored, 1, a, c, EnglishBowlers,
                  IndianBatsman, names, type1, partners[active],
                  firstbattingfirstbowling, totalOvers1, bowlsPlayed1,
                  oversPlayed1, wicketsDown1, runsScored1, a1, 0,
                  IndianBowlers, EnglishBatsman)
          break
        return
      else:
        if target[0] > runsScored1:
          for i, j in EnglishBatsman.items():
            if j[1] != 0 and j[2] != 0:
              SaveScores(
                  f"Pakistani Player {names[i]} is Not Out with {j[0]} Runs in {j[1]} Bowls\n"
              )
          print(
              f"{maindict[fbfb[0]]} Won the Match by {target[0]-runsScored1} Runs!"
          )
          SaveScores(
              f"{maindict[fbfb[0]]} Won the Match by {target[0]-runsScored1} Runs!\n"
          )
        elif target[0] <= runsScored1:
          for i, j in EnglishBatsman.items():
            if j[1] != 0 and j[2] != 0:
              SaveScores(
                  f"Pakistani Player {names[i]} is Not Out with {j[0]} Runs in {j[1]} Bowls\n"
              )
          print(
              f"{maindict[fbfb[1]]} Won the Match by {10-wicketsDown1} Wickets!"
          )
          SaveScores(
              f"{maindict[fbfb[1]]} Won the Match by {10-wicketsDown1} Wickets!\n"
          )

        SaveScores("Indian Team\n")
        for i, j in IndianBatsman.items():
          SaveScores(
              f"{names[i]}: {j[0]} Runs | {j[1]} Bowls | {j[4][0]} Fours | {j[4][1]} Sixes\n"
          )
        SaveScores("Pakistani Team\n")
        for i, j in EnglishBatsman.items():
          SaveScores(
              f"{names[i]}: {j[0]} Runs | {j[1]} Bowls | {j[4][0]} Fours | {j[4][1]} Sixes\n"
          )
        SaveScores("Indian Bowlers\n")
        for i, j in IndianBowlers.items():
          SaveScores(
              f"{names[i]}: {j[0]} Runs | {j[1]} Overs | {j[2]} wickets\n")
        SaveScores("Pakistani Bowlers\n")
        for i, j in EnglishBowlers.items():
          SaveScores(
              f"{names[i]}: {j[0]} Runs | {j[1]} Overs | {j[2]} wickets\n")
        SaveScores(f"India: {runsScored}-{wicketsDown}\n")
        SaveScores(f"Pakistan: {runsScored1}-{wicketsDown1}\n")
        with open("highlights.txt") as e:
          print(e.read())
        # print(commentry())
        exit()

    def scorecard():
      if type1 == "t20i" or type1 == "odi":
        if target[0] != -5:
          a = target[0] - runsScored1
          # print(f"a: {a}")
          b = {"t20i": 120, "odi": 300}[type1]
          totalbowls = bowlsPlayed1
          # print(f"total bowls: {totalbowls}")
          # print(totalbowls)
          # print(a)
          rrr = round((a / (b - totalbowls)) * 6, 2)
          # rrr = 69
        print(
            f"{(f'Target: {target[0]} Runs | Required Run Rate: {rrr} | ') if target[0] != -5 else ''}Net Run Rate: {round((runsScored1/(bowlsPlayed1 if bowlsPlayed1 !=0 else 1))*6, 2)}\nOvers: {oversPlayed1 if i!=5 else oversPlayed1+1}.{i+1 if i!=5 else 0}\t\t\tScore: {runsScored1}-{wicketsDown1}\n{names[partners1[0][0]]+'*' if Next==1 else names[partners1[0][0]]}: {partners1[0][1][0]}|{partners1[0][1][1]}\t\t{names[partners1[1][0]]+'*' if Next==0 else names[partners1[1][0]]}: {partners1[1][1][0]}|{partners1[1][1][1]}\n\nCurrent Over: {' | '.join(currentOver1)}\n{names[c1]}: {IndianBowlers[c1][0]}-{IndianBowlers[c1][2]} | {IndianBowlers[c1][1] if i!=5 else IndianBowlers[c1][1]+1}.{i+1 if i!=5 else 0}"
        )
      else:
        print(
            f"\nRun Rate: {round((runsScored1/(bowlsPlayed1 if bowlsPlayed1 !=0 else 1))*6, 2)}\nOvers: {oversPlayed1 if i!=5 else oversPlayed1+1}.{i+1 if i!=5 else 0}\t\t\tScore: {runsScored1}-{wicketsDown1}\n{names[partners1[0][0]]+'*' if Next==1 else names[partners1[0][0]]}: {partners1[0][1][0]}|{partners1[0][1][1]}\t\t{names[partners1[1][0]]+'*' if Next==0 else names[partners1[1][0]]}: {partners1[1][1][0]}|{partners1[1][1][1]}\n\nCurrent Over: {' | '.join(currentOver1)}\n{names[c1]}: {IndianBowlers[c1][0]}-{IndianBowlers[c1][2]} | {IndianBowlers[c1][1] if i!=5 else IndianBowlers[c1][1]+1}.{i+1 if i!=5 else 0}"
        )
        pass

    totalOvers1 += 1
    currentOver1 = []
    for i in range(6):
      if target[0] <= runsScored1 and target[0] != -5:
        for i, j in EnglishBatsman.items():
          if j[1] != 0 and j[2] != 0:
            SaveScores(
                f"Pakistani Player {names[i]} is Not Out with {j[0]} Runs in {j[1]} Bowls\n"
            )
        print(
            f"{maindict[fbfb[1]]} Won the Match by {10-wicketsDown1} Wickets!")
        SaveScores(
            f"{maindict[fbfb[1]]} Won the Match by {10-wicketsDown1} Wickets!")
        SaveScores("Indian Team\n")
        for i, j in IndianBatsman.items():
          SaveScores(
              f"{names[i]}: {j[0]} Runs | {j[1]} Bowls | {j[4][0]} Fours | {j[4][1]} Sixes\n"
          )
        SaveScores("Pakistani Team\n")
        for i, j in EnglishBatsman.items():
          SaveScores(
              f"{names[i]}: {j[0]} Runs | {j[1]} Bowls | {j[4][0]} Fours | {j[4][1]} Sixes\n"
          )
        SaveScores("Indian Bowlers\n")
        for i, j in IndianBowlers.items():
          SaveScores(
              f"{names[i]}: {j[0]} Runs | {j[1]} Overs | {j[2]} wickets\n")
        SaveScores("Pakistani Bowlers\n")
        for i, j in EnglishBowlers.items():
          SaveScores(
              f"{names[i]}: {j[0]} Runs | {j[1]} Overs | {j[2]} wickets\n")
        SaveScores(f"India: {runsScored}-{wicketsDown}\n")
        SaveScores(f"Pakistan: {runsScored1}-{wicketsDown1}\n")
        with open("highlights.txt") as e:
          print(e.read())
        # print(commentry())
        exit()
      bowlsPlayed1 += 1
      while True:
        battingTeam = 2

        while True:
          print(IndianBowlers)
          choice = input(
              "Enter your choice of bowling (in numbers. ex: 1,2,4,6): ")
          reqdict = {'odi': 300, 't20i': 120, 'test': 10000}[type1]
          totalss = round((bowlsPlayed1 / reqdict) * 100)
          d = random.choice(randomPlay(totalss, "Pakistan"))
          try:
            choice = int(choice)
            some = True if choice in [1, 2, 3, 4, 6] else False
            if some == True:
              break
          except:
            if choice == "w":
              active = 0 if Next == 1 else 1
              print(
                  f"{partners1[active][0]}'s Wagon Wheel: {partners1[active][1][2]}\nTeam Wagon Wheel: {totalw[maindict[battingTeam]]}"
              )
            elif choice == "b":
              print(IndianBowlers)
              # break
            elif choice == "B":
              print(EnglishBatsman)
              # break
            elif choice == "":
              choice = random.choice(bowlerChoice)
              break
            else:

              print("Provide a valid input!")
        if len(bowler) > 4 and checkPercentage(bowler, choice) > 30:
          print(f"Exhausted {choice}--> Try another number!")
          continue
        else:
          bowler.append(choice)
          break

      os.system("cls")
      if d == choice:
        active = 0 if Next == 1 else 1
        if EnglishBatsman[partners1[active][0]][2] - 1 > 0:
          EnglishBatsman[partners1[active][0]][2] -= 1
          print(
              f"One life gone for {names[partners1[active][0]]}\nRemaining life: {EnglishBatsman[partners1[active][0]][2]}"
          )
          partners1[active][1][1] += 1
          EnglishBatsman[partners1[active][0]][1] += 1

          currentOver1.append('0')
          scorecard()

        elif EnglishBatsman[partners1[active][0]][2] - 1 == 0:
          EnglishBatsman[partners1[active][0]][2] = 0
          active = 0 if Next == 1 else 1
          # EnglishBatsman[partners1[active][0]][2]-=1
          wicketsDown1 += 1
          IndianBowlers[c1][2] += 1
          partners1[active][1][1] += 1
          # EnglishBatsman[partners1[active][0]][0]+=partners1[active][1][0]
          EnglishBatsman[partners1[active][0]][1] += 1
          currentOver1.append('W')
          # print(batterslist)
          SaveScores(
              f"Pakistani player {names[partners1[active][0]]} out after scoring {EnglishBatsman[partners1[active][0]][0]} Runs | {EnglishBatsman[partners1[active][0]][1]} Bowls, wicket by Indian bowler {names[c1]}:  | Current Wicket count of {names[c1]}: {IndianBowlers[c1][2]} wickets.Bowler has bowled {IndianBowlers[c1][1]} overs and given {IndianBowlers[c1][0]} Runs\n"
          )

          print(partners1[active][0])
          print(
              f"Removing Batsman: {partners1[active][0]} from {batterslist}\nactives: {partners1[1][0]} and {partners1[0][0]}"
          )
          try:
            try:
              batterslist.remove(partners1[1][0])
            except:
              pass
            try:

              batterslist.remove(partners1[0][0])
            except:
              pass
          except:
            if len(batterslist) == 1:
              pass
          while True:
            try:
              # print(batterslist)

              a1 = batterslist[0]
              if a1 in partners1[0] or a1 in partners1[1]:
                a1 = batterslist[0]
              try:
                print(
                    f"{names[partners1[active][0]]} is out!\nNext Batsman coming: {names[batterslist[1]]}\n"
                )
              except:
                print(
                    f"{names[partners1[active][0]]} is out!\nNext Batsman coming: {names[batterslist[0]]}\n"
                )
              partners1[active] = [
                  a1, [0, 0, {
                      0: 0,
                      1: 0,
                      2: 0,
                      3: 0,
                      4: 0,
                      6: 0,
                      -1: 0
                  }]
              ]
              # D = EnglishBatsman[a1]
              break
            except:
              # if wicketsDown1==10:
              #     break
              # a1 = batterslist[0]
              print("Team all out!")
              # SaveScores("Pakistan Team All out!\n")
              # partners1[active] = [a1,[0,0,{0:0, 1:0,2:0,3:0,4:0,6:0,-1:0}]]
              # D = EnglishBatsman[a1]
              allout = True
              break
          if allout == True:
            if wicketsDown1 == 10:
              SaveScores("Pakistan Team All out!\n")
            break
          scorecard()
      else:
        active = 0 if Next == 1 else 1
        partners1[active][1][2][d] += 1
        totalw[maindict[battingTeam]][d] += 1
        try:
          IndianBowlers[c1][0] += d
        except:
          c1 = random.choice(list(IndianBowlers.keys()))
          IndianBowlers[c1][0] += d
        if d == 6: EnglishBatsman[partners1[active][0]][4][1] += 1
        if d == 4: EnglishBatsman[partners1[active][0]][4][0] += 1
        partners1[active][1][0] += d
        partners1[active][1][1] += 1
        EnglishBatsman[partners1[active][0]][0] += d
        EnglishBatsman[partners1[active][0]][1] += 1
        # print(f"After adding: {EnglishBatsman}")

        runsScored1 += d
        # print(f'before adding {IndianBatsman[partners[active][0]][3][0]} and {partners[active][1][0]}')
        if partners1[active][1][0] > 30 and EnglishBatsman[partners1[active]
                                                           [0]][3][0] == False:
          # print('inside 30 adding')
          EnglishBatsman[partners1[active][0]][2] += random.randint(1, 2)
          EnglishBatsman[partners1[active][0]][3][0] = True
        if partners1[active][1][0] > 50 and EnglishBatsman[partners1[active]
                                                           [0]][3][1] == False:
          EnglishBatsman[partners1[active][0]][2] += random.randint(1, 2)
          EnglishBatsman[partners1[active][0]][3][1] = True
        if partners1[active][1][0] > 100 and EnglishBatsman[
            partners1[active][0]][3][2] == False:
          EnglishBatsman[partners1[active][0]][2] += random.randint(1, 2)
          EnglishBatsman[partners1[active][0]][3][2] = True
        currentOver1.append(str(d))
        if d % 2 != 0:
          nexttemp = 0 if Next == 1 else 1
          Next = nexttemp
        else:
          pass
        scorecard()
    IndianBowlers[c1][1] += 1
    oversPlayed1 += 1
    nexttemp = 0 if Next == 1 else 1
    Next = nexttemp
    print(f"Your Previous Bowler: {names[c1]}")
    # print(IndianBowlers)
    while True:
      C = input(
          "Enter the next bowler (respond with 'b' to display bowlers name and stats)\n>> "
      )
      if C == "b":
        print(IndianBowlers)
      C = C if C != "" else random.choice(list(IndianBowlers.keys()))
      main = {'odi': 10, 't20i': 4, 'test': 1000}
      if C not in list(IndianBowlers.keys()):
        print("Select a valid bowler")
        continue
      elif IndianBowlers[C][1] >= main[type1]:
        print("This bowler has exhausted all his overs!")
        continue
      elif C == c1:
        print("Same bower can't bowl 2 consecutive overs!")
        continue
      else:
        break
    c1 = C


a1 = list(EnglishBatsman.keys())[0]
b1 = list(EnglishBatsman.keys())[1]
partners1 = [[a1, [0, 0, {
    0: 0,
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    6: 0,
    -1: 0
}]], [b1, [0, 0, {
    0: 0,
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    6: 0,
    -1: 0
}]]]
totalOvers1 = -1
bowlsPlayed1 = 0
oversPlayed1 = 0
wicketsDown1 = 0
firstbattingfirstbowling = [2, 1]
runsScored1 = 0
target = [-5]

c = random.choice(list(EnglishBowlers.keys()))
oversPlayed = 0
wicketsDown = 0
runsScored = 0
totalOvers = -1
firstbattingfirstbowling = [1, 2]
bowlsPlayed = 0
if toss[0] == True and toss[1] == 2 or toss[0] == False and toss[1] == 1:
  print(IndianBowlers)
  c1 = input(
      "Choose the First Bowler (in short names. Ex: jadeja, bumrah etc.): ")
  firstbattingfirstbowling = [2, 1]

  bowling(target, totalOvers1, bowlsPlayed1, oversPlayed1, wicketsDown1,
          runsScored1, 1, a1, c1, IndianBowlers, EnglishBatsman, names, type1,
          firstbattingfirstbowling, totalOvers, bowlsPlayed, oversPlayed,
          wicketsDown, runsScored, c, EnglishBowlers, IndianBatsman)
if toss[0] == True and toss[1] == 1 or toss[0] == False and toss[1] == 2:
  print("Available Batsman to chose from: ")
  for i, j in IndianBatsman.items():
    print("-> ", i)
  while True:
    a = input(
        "Choose the First Batsman (in short names. Ex: kohli, rohit etc.): ")
    if a not in IndianBatsman.keys():
      print('Try again, Batsman not in list.')
    else:
      break
  while True:
    b = input(
        "Choose the Second Batsman (in short names. Ex: kohli, rohit etc.): ")
    if b not in IndianBatsman.keys() or b == a:
      print('Try again, Batsman not in list or already chosed.')
      continue
    else:
      break

  firstbattingfirstbowling = [1, 2]

  partners = [[a, [0, 0, {
      0: 0,
      1: 0,
      2: 0,
      3: 0,
      4: 0,
      6: 0,
      -1: 0
  }]], [b, [0, 0, {
      0: 0,
      1: 0,
      2: 0,
      3: 0,
      4: 0,
      6: 0,
      -1: 0
  }]]]
  # print(partners[0][1][3][0])
  current = partners[0]

  batting(partners, target, totalOvers, bowlsPlayed, oversPlayed, wicketsDown,
          runsScored, 1, a, c, EnglishBowlers, IndianBatsman, names, type1,
          current, firstbattingfirstbowling, totalOvers1, bowlsPlayed1,
          oversPlayed1, wicketsDown1, runsScored1, a1, 0, IndianBowlers,
          EnglishBatsman)
