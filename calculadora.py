def calc(n1, n2, operacao) :
    if operacao == 1 :
        return n1 + n2
    elif operacao == 2 :
        return n1 - n2
    elif operacao == 3 :
        return n1 * n2
    elif operacao == 4 :
        return n1 / n2
    else :
        return 0
    

executar = True

while (executar == True) :
    print ("O que você deseja fazer?")
    print ("1: Soma, 2: Subtração, 3: Multiplicação, 4: Divisão, 5: Sair.")
    operacao = int(input())
    if (operacao < 0) or (operacao > 5) :
        print("Opção inexistente.")
    elif (operacao == 5) :
        print("Encerrando calculadora.")
        break
    else:
        print ("Insira o primeiro número:")
        n1 = int (input())
        print ("Insira o segundo número:")
        n2 = int(input())
        resultado = calc(n1, n2, operacao)
        print("O resultado é:", resultado)