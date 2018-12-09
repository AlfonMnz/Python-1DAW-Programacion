B = {'ramon', 'paco', 'tessa'}

F = {'José Manuel'}
I = {'paco', 'Belén', 'blas', 'manolo', 'jose', 'paqui', 'Jamón Jomán'}

H = {'Paco', 'Blas', 'Manolo', 'jose', 'Ramón'}
M = {'tessa', 'Belen', 'Paqui'}

a = F | I - B
b = F | I
c = H - B
d = M & B
e = B ^ I
f = H - B - F

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
