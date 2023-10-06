letraTurno = input('Digite a letra equivalente ao turno que você estuda: M-matutino ou V-Vespertino ou N-Noturno: ')

if letraTurno == 'm' or letraTurno == 'M':
    print('"Bom dia!"')
elif letraTurno == 'v' or letraTurno == 'V':
    print('"Boa tarde!"')
elif letraTurno == 'n' or letraTurno == 'N':
    print('"Boa noite!"')
else:
    print('"Valor Inválido!"')