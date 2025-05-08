users = {}
# users = {"naam": {"fav_uber": "x", "fav_dest": "rotterdam", "fav_dest_dist": 45},
#          "volgende_naam": {"fav_uber": "van", "fav_dest": "amsterdam", "fav_dest_dist": 100}}
uber = {"black" : 2, "van" : 3.5, "x" : 1.5}
uber_calc = True

def add_user(name):
    fav = input('Met welke Uber wil je reizen? (black/van/x) \n')
    dest = input('Naar welke plaats wil je? \n')
    dist = int(input('Hoeveel km wil je rijden? \n'))
    users[name] = {"fav_uber": fav, "fav_dest": dest, "fav_dest_dist": dist}
    calc(dist, fav, dest)

def calc(dist, service, dest):
    price = round(uber[service] * dist, 2)
    print(f'Je ritprijs van {dist}km naar {dest}, met Uber {service}, kost €{price}')

while uber_calc:
    name = input('Voer je gebruikersnaam in\n')
    if name in users:
        go_fav = input(f'Wil je met {users[name]["fav_uber"]} naar {users[name]["fav_dest"]} reizen? (j/n) \n')
        if go_fav == 'j':
            calc(users[name]["fav_dest_dist"], users[name]["fav_uber"], users[name]["fav_dest"])
        else:
            dest = input('Waar wil je heen reizen? \n')
            dist = int(input('Hoeveel km  wil je reizen? \n'))
            service = input('Wil je met black, van of x reizen? \n')
            calc(dist, service, dest)
    else:
        add_user(name)

    another_trip = input('Wil je nog een ritje maken? (j/n) \n')
    if another_trip != "j":
        print('Bedankt en tot ziens!')
        uber_calc = False