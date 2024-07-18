def q1():
    lista = ""
    ano = int(input("Digite o ano: "))
    periodicidade = int(input("Periodicidade: "))
    cont = 1
    while cont <= 4:
        if cont == 4:
            proximo_ano = ano + periodicidade
            lista += f"{proximo_ano}"
            cont += 1
            ano = proximo_ano
        else:
            proximo_ano = ano + periodicidade
            lista += f"{proximo_ano} "
            cont += 1
            ano = proximo_ano
    print(lista, end=" ")
    


def q2():
    numero = 0
    divisores = 0
    parar = False
    while parar == False:
        numero = int(input("Digite: "))
        if numero == -1:
            break
        for i in range(1, numero + 1):
            if numero % i == 0:
                divisores += 1
        if divisores == 2:
            print("Primo")
        else:
            print("Não")



def q3():
    valor = 0
    soma = 0
    cont = 0
    media = 0
    Continue = True
    while Continue == True:
        valor = float(input("Digite: "))
        if valor > 0:
            soma += valor
            cont += 1
        else:
            Continue = False
        
    if cont <= 0:
        print("0.00")
        print("0.00")
    else:
        print(f"{soma:.2f}")
        media = soma/cont
        print(f"{media:.2f}")




def q4():
    dias = int(input("Dias: "))
    quilometragem = int(input("Quilometragem: "))
    if quilometragem<100:
        preço = 90*dias
    else:
        sobra = quilometragem - 100
        preço = (90*dias + (sobra*12))
    if dias == 0:
        print("Valor inválido")
    else:
        print(f"{preço:.2f}")


def q5():
    pass

if __name__=="__main__":
    # teste sua questão manualmente aqui
    
    pass
