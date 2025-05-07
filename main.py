uber = {'black' : 2, 'van' : 3.5, 'x' : 1.5}

def get_user_choice():
    validate = True
    while validate:
        choice = input('Welke Uber wil je pakken? (black/van/x) \n')
        if choice not in uber:
            print('Onjuiste keuze\n')
        else:
            validate = False
            return choice

# def distance():
#     while validate = True
#         km = int(input('Hoeveel km wil je rijden? \n'))
#         if type(km) == 'float':
#             print('Voer een juist aantal kilometers in \n')
#         else:
#             validate = False
#             return km

def calculate_costs(choice, km):
    ritprijs = round(uber[choice] * km, 2)
    return ritprijs

choice = get_user_choice()
# km = distance()
km = float(input('Hoeveel km wil je rijden? '))
ritprijs = calculate_costs(choice, km)

print(f'{km} km rijden met Uber {choice} kost €{ritprijs:.2f}')