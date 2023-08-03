
#s = 'whitechocolatespaceegg'
#print(s[:5])
#print(s[5:14])
#print(s[14:19])
#print(s[19:])

#b = 'King Arthur'
#print(b[::2])
#print(b[1::2])
#print(b[-1:4:-1])
#print(b[::-1])

#a = 'java python c++ fortran'
#print(a.isalpha())


#print(','.join(('one','two','three')))
#print('\n'.join(reversed(['one','two','three'])))
#print(' '.join('hello'))

#c = 'Jan Feb Mar Apr May Jun'
#print(c.split())
#d = 'J. M. Brown AND B. Mencken AND R. P. van`t'
#print(d.split('AND'))

#heading = '| Index of Dutch Tulip Prices |'
#line = '+' + '-'*16 + '-'*13 + '+'
#linex = '+' + '-'*29 + '+'
#print(line, heading, line,
 #      '|    Nov 23 1636 |        100 |',
 #      '|    Nov 25 1636 |        673 |',
 #      '|    Feb  1 1637 |       1366 |', linex, sep='\n')


#print('{:11,d}'.format(1000000))
#print('{:11,.1f}'.format(1000000)) #1f: un float despues del .

stack = []
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)
#print(stack)
#print(stack.pop())
#print(stack)

ListaA = [1, 2, 3]
ListaB = [4, 5 ,6]
print('Lista A: ', ListaA)
print('Lista B: ', ListaB)
ListaA.extend(ListaB)
print('Lista A con B: ', ListaA)

print(ListaA.pop())

ListaC = []
for n in range (1,4):
    ListaC.append(n)
    print('Lista c: ', ListaC)
listaD = [i for i in range(1, 4)]
print(listaD)