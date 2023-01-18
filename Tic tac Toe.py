def Display_Grid(a):
    print(a[1],"|",a[2],"|",a[3],"|")
    print(a[4],"|",a[5],"|",a[6],"|")
    print(a[7],"|",a[8],"|",a[9],"|")
    

def End(count):
    if count>9:
        return True
    return False



def UpdateGrid(a,postion,pturn):
    if pturn==1 and a[postion]!='X' and a[postion]!='O':
        a[postion]='X'
    elif pturn==2 and a[postion]!='X' and a[postion]!='O':
        a[postion]='O'
    else:
        print("BOX ALREADY PLAYED")
        return False


def Win(a,pturn):
    if (a[1]==a[2]and a[2]==a[3])or(a[4]==a[5]and a[5]==a[6])or(a[7]==a[8]and a[8]==a[9])or(a[1]==a[4]and a[4]==a[7])or(a[2]==a[5]and a[5]==a[8])or(a[3]==a[6]and a[6]==a[9])or(a[1]==a[5]and a[5]==a[9])or(a[3]==a[5]and a[5]==a[7]):
        if pturn==1:
            print("PLAYER 1 WON ")
            return True
        else:
            print("PLAYER 2 WON ")
            return True
    



    
    






a=['#',1,2,3,4,5,6,7,8,9];

Display_Grid(a)
from IPython.core.display import display
from IPython.display import clear_output
count=1;
turn=0;
gameover=False
while gameover!=True:
   if(turn%2==0):
       print('PLAYER 1 -> PLACE YOUR (X) CHOOSE A BOX')
       choose=int(input())
       if UpdateGrid(a,choose,1)==False:
           print("DO UR TURN AGAIN Correctly otherwise you lose your turn")
           choose=int(input())
           UpdateGrid(a,choose,1)
       gameover= Win(a,1)
       if gameover==True:
           Display_Grid(a)
           break
       Display_Grid(a)
       count+=1
       gameover=End(count)
       turn+=1
   else:
        print('PLAYER 2 -> PLACE YOUR (O) CHOOSE A BOX')
        choose=int(input())
        if UpdateGrid(a,choose,2)==False:
           print("DO UR TURN AGAIN Correctly otherwise you lose your turn")
           choose=int(input())
           UpdateGrid(a,choose,2)
        gameover=Win(a,2)
        if gameover==True:
           Display_Grid(a)
           break
        Display_Grid(a)
        count+=1
        gameover=End(count)
        turn+=1


print("game over")