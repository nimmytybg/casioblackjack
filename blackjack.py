#calculator blackjack ver 1.0.1 for CASIO fx-CG50 by nimmy sept 2026
import random
def cls():
    print("\n"*8)
cls()
coins = 0
phand = []
dhand = []
win = False

def count(hand):
    hand = list(hand)
    return int(sum(hand))

def deal():
    phand.append(drawCard())
    phand.append(drawCard())
    if count(phand) == 21:
        print("Blackjack")
def dealD():
    dhand.append(drawCard())
    dhand.append(drawCard())
def drawCard():
    tcard = random.randint(1,11)
    if tcard == 11 and (int(sum(phand))+11)>21:
        tcard = 1
        return tcard
    else:
        return tcard
def hit():
    phand.append(drawCard())
def dhit():
    dcard = random.randint(1,11)
    dhand.append(dcard)
def turnInput():
    global stand
    p = False
    while p == False:
        print("type '1' to hit,")
        print("type '2' to stand,")
        turn = input("press 'EXE' to confirm")
        if turn == '1':
            hit()
            stand = 0
            return
        elif turn == '2':
            stand = stand+1
            if stand == 1:
                print('you are standing,')
                print('stand again to finalise')
            return
        else:
            print('invalid input, please retype')
def resolve():
    print('your total: ',int(sum(phand)))
    print("dealer's total: ",int(sum(dhand)))
    if int(sum(phand)) > int(sum(dhand)):
        print('you win')
    elif int(sum(phand)) < int(sum(dhand)):
        print('you lose')
    else:
        print('draw')
print('welcome to blackjack')
print('press EXE to play,')
info = input('type 1 for info')
if info == '1':
    cls()
    print('calculator blackjack for CASIO fx-CG50')
    print('1.0 sept 26')
    print('by nimmy')
    print('double, split and betting')
    print('have not been implemented yet')
    input('press EXE for page 2')
    cls()
    print('for info and download visit')
    print('https://github.com/nimmytybg')
    print('/casioblackjack')
    print('to download directly from ')
    print('windows terminal type')
    input('press EXE for page 3')
    cls()
    print('wget -O blackjack.py https:')
    print('//github.com/nimmytybg')
    print('/casioblackjack ensure') 
    print('terminal is running as admin')
    input('press EXE to play')
#else:
#    pass
cls()
dealD()
deal()
stand = 0
bust = False
while stand < 2:
    print("dealer's first card ")
    print("is ", dhand[0])
    print("Your cards are: ")
    print(phand)
    turnInput()
    print("Your cards are: ")
    print(phand)
    if int(sum(phand)) > 21:
        print('bust.')
        bust = True
        break
    cls()
if bust == False:
    print("Your cards are: ",phand)
    print("dealer's first card")
    print("is ", dhand[0])
    print("dealer's second card ")
    print("is ", dhand[1])
    input('press EXE to proceed')
    while int(sum(dhand)) < 16:
        cls()
        dhit()
        print("dealer's hand ")
        print("is", dhand)
        print("your hand is: ")
        print(phand)
        print("dealer's sum:")
        print(int(sum(dhand)))
        if int(sum(dhand)) > 21:
            print('dealer bust, player wins')
            win = True
        input('press EXE to proceed')
    if win != True:
        resolve()
