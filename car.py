while True:
    user_val=input()
    if user_val=='help':
        print('''start-"car started"
                  stop-"car got stopped"
                 quit-"end the program"''')
    if user_val=='quit':
         break
    if user_val=='start':
        print('car started')
    elif user_val=='stop':
        print('car got stopped')
    else:
        print("sorry i don't understood it")
