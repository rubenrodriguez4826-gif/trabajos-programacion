from datetime import date, timedelta

inicio = date(1901, 1, 1)
fin = date(2000, 12, 31)

domingos = 0
domingos_primero = 0

dia = inicio
while dia <= fin:
    if dia.weekday() == 6:      # lunes = 0, ..., domingo = 6
        domingos += 1
        if dia.day == 1:        # domingo que cae en día 1 del mes
            domingos_primero += 1
    dia += timedelta(days=1)

print("Domingos en total:", domingos)
print("Domingos en día 1 de mes:", domingos_primero)