#Tuplas são imutáveis
lanche = ('Hambúrguer','Suco','Pizza','Pudim')
for cont in range(0,len(lanche)):
    print(f'Eu vou comer ',lanche[cont])

for pos,comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

for comida in (lanche):
  print(f'Eu vou comer {comida}')

#  Sorted Ordena
print(sorted(lanche))

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
# Sorted ordena
print(sorted(c))
# Count conta quantas vezes aparece
print(c.count(2))
print(c)
# Index mostra em qual posição
print(c.index(5))