file = open('names.txt','r')
content= file.readlines()
C1 = []
for i in content:
   C1.append(i.replace('\n','').replace('\t',' '))
#print(C1)
file.close()


file = open('c6.txt', 'w')
file.write(str(C1))
file.close()
