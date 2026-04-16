#Um hospital tem três turnos: manhã (6h–14h), tarde (14h–22h) e noite (22h–6h).
# Leia uma hora (inteiro de 0 a 23) e informe em qual turno ela cai.

#entrada
horaTurno = int(input("Digite o horario de inicio do turno: "))

#processamento
if horaTurno >= 6 and horaTurno < 14:
    print (f"Horario - {horaTurno} - você está no turno da manhã!")
elif horaTurno >= 14 and horaTurno < 22:
    print (f"Horario - {horaTurno} - você está no turno da tarde!")
else:
    print (f"Horario - {horaTurno} - você está no turno da noite!")


