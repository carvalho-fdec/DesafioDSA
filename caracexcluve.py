"""
Implementar um algoritmo para determinar se uma string possui todos os caracteres exclusivos.

Premissas
Podemos assumir que a string é ASCII? Sim
Nota: As cadeias de caracteres Unicode podem exigir tratamento especial dependendo do seu idioma
Podemos supor que há distinção entre maiúsculas e minúsculas? * Sim
Podemos usar estruturas de dados adicionais? * Sim

Teste Cases
None -> False
'' -> True
'foo' -> False
'bar' -> True
"""


def caracexclusiv (palavra):
    tam = len(palavra)
    palavra = palavra.lower()
    if tam == 0:
        return True
    else:
        contadoraux = 0

    for c1 in range(0, tam):
        for c2 in range(0, tam):
            if palavra[c1] == palavra[c2]:
                contadoraux += 1

    if contadoraux/tam == 1:
        return True
    else:
        return False



def main ():
    outra = 's'
    while outra == 's':
        palavra = input('Digite a palavra: ')
        if caracexclusiv(palavra):
            print(f'Verdadeiro. A palavra "{palavra}" possui todos os caracteres exclusivos')
        else:
            print(f'Falso. A palavra "{palavra}" não possui todos os caracteres exclusivos')
        outra = input('Outra palavra? [S/N] ').lower()

if __name__ == '__main__': main()