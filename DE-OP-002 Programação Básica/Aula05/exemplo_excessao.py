while True:
    try:
        x = int(input('Digite um número inteiro: '))
        break 
    except ValueError:
        print('Não é um número inteiro, por favor digite um número inteiro')