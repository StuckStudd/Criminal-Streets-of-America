
player = {"name": "rootkid", "money": 500, "location": "home"}

locations = {
    "home": {"text": "Ты дома.", "exits": ["street"]},
    "street": {"text": "Улица. Идёт дождь.", "exits": ["home", "shop"]},
    "shop": {"text": "Магазин. Тут тихо.", "exits": ["street"]},
}


def look(args):
    loc = locations[player['location']]
    print(loc['text'])
    print("Выходы:", ", ".join(loc['exits']))


def go(args):
    if not args:
        print("Куда идти? Пример: go shop")
        return

    place = args[0]

    if place in locations[player['location']]['exits']:
        player['location'] = place
        look([])
    else:
        print("Туда не пройти.")


def money(args):
    print("Деньги:", player['money'], "$")


commands = {
    "look": look,
    "go": go,
    "money": money,
}


while True:
    parts = input("> ").split()

    if not parts:
        continue

    if parts[0] == "quit":
        break

    action = commands.get(parts[0])

    if action:
        action(parts[1:])
    else:
        print("Не понял команду")
