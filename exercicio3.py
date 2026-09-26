def converter_minutos(horas):
    return horas * 60

horas = float(input("Digite a quantidade de horas: "))
minutos = converter_minutos(horas)
print("Isso corresponde a", minutos, "minutos.")
