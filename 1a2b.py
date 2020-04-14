import random
targetNum = random.sample('1234567890',4) 
print (targetNum)


IsWin = False
name=input("輸入'吃葡萄不吐葡萄皮'開始遊戲:")
c=0
d=0
if name=='吃葡萄不吐葡萄皮' :
    while(IsWin == False):
        
        if c==0 :
            c+=1
            print("遊戲開始")


        userNum=list(input("輸入4個不同數字:"))  
        a = 0
        for i in range(4):
            
            if(targetNum[i] == userNum[i]):
                a = a + 1      
        b = 0
        for i in range(4):
            
            if(userNum[i] in targetNum and userNum[i] != targetNum[i]):
                b = b + 1    
        print(a,"A", b, "B")
        
        if (a == 4):
            IsWin = True 
            print("恭喜答對!")
            
                

    