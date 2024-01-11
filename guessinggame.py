value=8
n=0
while n<2:
    user_val=int(input('guess the no:'))
    n+=1
    if user_val==value:
        print('you win!')
        break
    
else:
        print('guess again')



