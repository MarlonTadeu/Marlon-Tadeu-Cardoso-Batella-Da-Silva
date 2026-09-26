def classificar_temperatura(temperatura):
    if temperatura < 18:
        return "Frio"
    elif temperatura <= 27:
        return "Agradável"
    else:
        return "Quente"

temperatura = float(input("Digite a temperatura: "))
print("Classificação:", classificar_temperatura(temperatura))