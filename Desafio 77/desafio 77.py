palavras = ('Amar', 'Aproveitar', 'Comer', 'Viajar', 'Pescar', 'Programar', 'Python', 'Programadora')
for pal in palavras:
    print(f'\nNa palavra {pal.upper()} temos as vogais ', end='')
    for letra in pal:
        if letra.lower() in 'aeiou':
            print(letra.lower(), end=' ')
