import calcular

while True:
    operador = input("Digite +, -, *, / para realizar o calculo, digite (sair) para encerrar a calculadora. ").lower()
    
    if (operador == "sair"):
        break

    a = float(input("Digite o valor A: "))
    b = float(input("Digite o valor B: "))

    if (operador == "+"):
        try:
            print(f"A soma de {a:.2f} + {b:.2f} = {calcular.somar(a, b):.2f}")
        except ValueError:
            print("Digite apenas números")
        except:
            print("Erro! Entre em contato com o suporte técnico.")
    if (operador == "-"):
        try:
            print(f"A subtração de {a:.2f} - {b:.2f} = {calcular.subtrair(a, b):.2f}")
        except ValueError:
            print("Digite apenas números!")
        except:
            print("Erro! Entre em contato com o suporte técnico.")
    if (operador == "*"):
        try:
            print(f"A multiplicação de {a:.2f} * {b:.2f} = {calcular.multiplicar(a, b):.2f}")
        except ValueError:
            print("Digite apenas números!")
        except:
            print("Erro! Entre em contato com o suporte técnico.")
    if (operador == "/"):
        try:
            print(f"A divisão de {a:.2f} / {b:.2f} = {calcular.dividir(a, b):.2f}")
        except ValueError:
            print("Digite apenas números!")
        except ZeroDivisionError:
            print("Impossível dividir por zero!")
        except:
            print("Erro! Entre em contato com o suporte técnico.")