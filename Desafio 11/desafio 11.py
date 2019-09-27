alt = float(input('Informe a largura da parede em cm: '))
larg = float(input('Informe a altura da parede em cm: '))
alt = alt / 100
larg = larg / 100
area = alt * larg
tinta = area / 2
print('Com a largura de: {}m, altura de:{}m e área total de {}m² é necessário {:.1f}L de tinta.'.format(alt,larg,area,tinta))