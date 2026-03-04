import calcular

while True:
    operador = input("Digite +, -, *, / para realizar o calculo, digite (sair) para encerrar a calculadora. ").lower()
    
    if (operador == "sair"):
        break

    a = input("Digite o valor A: ")
    b = input("Digite o valor B: ")

    
    if (operador == "+"):
        try:
            print(f"A soma de {a} + {b} = {calcular.somar(a, b)}")
        except ValueError:
            print("Digite apenas números")
        except:
            print("Erro! Entre em contato com o suporte técnico.")
    if (operador == "-"):
        try:
            print(f"A subtração de {a} - {b} = {calcular.subtrair(a, b)}")
        except ValueError:
            print("Digite apenas números!")
        except:
            print("Erro! Entre em contato com o suporte técnico.")
    if (operador == "*"):
        try:
            print(f"A multiplicação de {a} * {b} = {calcular.multiplicar(a, b)}")
        except ValueError:
            print("Digite apenas números!")
        except:
            print("Erro! Entre em contato com o suporte técnico.")
    if (operador == "/"):
        try:
            print(f"A divisão de {a} / {b} = {calcular.dividir(a, b)}")
        except ValueError:
            print("Digite apenas números!")
        except ZeroDivisionError:
            print("Impossível dividir por zero!")
        except:
            print("Erro! Entre em contato com o suporte técnico.")