from PIL import Image
import random

end=100
def show_board():
    img=Image.open('laddergame.jpg')
    img.show()
   
def check_ladder(pts):
    if(pts==4):
        print('Ladder')
        return 14
    elif(pts==9):
        print('Ladder')
        return 31
    elif(pts==20):
        print('Ladder')
        return 38
    elif(pts==28):
        print('Ladder')
        return 84
    elif(pts==40):
        print('Ladder')
        return 59
    elif(pts==63):
        print('Ladder')
        return 81
    elif(pts==71):
        print('Ladder')
        return 91
    else:
        return pts
   
 
def check_snake(pts1):
    if(pts1==17):
        print('snake')
        return 7
    elif(pts1==54):
        print('snake')
        return 34
    elif(pts1==62):
        print('snake')
        return 18
   
    elif(pts1==64):
        print('snake')
        return 60
   
    elif(pts1==93):
        print('snake')
        return 73
    elif(pts1==95):
        print('snake')
        return 75
   
    elif(pts1==99):
        print('snake')
        return 78
    else:
        return pts1
   

def reached_end(pts):
    if pts==end:
        return True
    else:
        return False
       
   
def play():
   
     p1_name=input('player1, please enter ur name:')    
     p2_name=input('player2, please enter ur name:')    
     
     pp1=0
     pp2=0
     turn=0
     while(1):
         if(turn%2==0):
             print(p1_name,'your turn')
             
             c=input('press 1 to continue 0 to quit:')
             if(c==0):
                 print(p1_name,'scored',pp1)
                 print(p2_name,'scored',pp2)
                 print('Quitting the game..thanks for playing')
                 break
             
             dice=random.randint(1,6)  
             print('dice showed',dice)
             pp1=pp1+dice
             pp1=check_ladder(pp1)
             pp1=check_snake(pp1)
             if pp1>end:
                 pp1=end
             print(p1_name,"ur score",pp1)
             if reached_end(pp1):
                 print(p1_name,'Won')
                 break
         else:
            print(p2_name,'your turn')
                 
            c=input('press 1 to continue 0 to quit:')
            if(c==0):
                print(p1_name,'scored',pp1)
                print(p2_name,'scored',pp2)
                print('Quitting the game..thanks for playing')
                break
                         
            dice=random.randint(1,6)  
            print('dice showed',dice)
            pp2=pp2+dice
            pp2=check_ladder(pp2)
            pp2=check_snake(pp2)
            if pp2>end:
                 pp2=end
            print(p2_name,"ur score",pp2)
            if reached_end(pp2):
                print(p2_name,'Won')
                break    
         turn=turn+1    
             
          
show_board()
play()
