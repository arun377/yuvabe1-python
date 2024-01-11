first='arun'
last =' karthic'
msg= first +last 
print('\n'+msg)


#formatted string 
msg=f'{first} {last} is a coder 1'
print(msg+'\n')

#String length
print(len(msg))

#String methods
print(msg.upper()+'\n')
print(msg.find('k'))
print('ar' in msg)
print(msg.replace('a','pa'))