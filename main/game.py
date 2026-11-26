import random
import time
player = {
    "name": "rootkid",
    "money": 300,
    "hp": 100,
    "chapter": 0,  # 0 = пролог, 1 = миссия 1, 2 = миссия 2, 3 = конец демки
}


def show_stats():
    stages = {
        0: "Пролог",
        1: "Миссия 1",
        2: "Миссия 2",
        3: "Начало сюжетки пройдено",
    }
    stage_name = stages.get(player["chapter"], "Неизвестно")
    print(f"[{player['name']}] HP: {player['hp']} | Money: ${player['money']} | Этап: {stage_name}")


def heal():
    if player["hp"] >= 100:
        print("HP уже полное.")
        return
    player["hp"] = min(100, player["hp"] + 30)
    print(f"Подлечился. Теперь HP: {player['hp']}")


def prologue():
    print("\n=== ПРОЛОГ: НОЧЬ В РАЙОНЕ ===")
    time.sleep(0.5)
    print("Ты приезжаешь в новый район с парой сотен в кармане и старой машиной.")
    time.sleep(0.5)
    print("На углу мигает фонарь, знакомый кидает наводку на быстрое дело.")
    time.sleep(0.5)
    print("1 - Согласиться сразу и проверить точку (риск -10 HP, +$200)")
    print("2 - Сначала осмотреться и прикупить припасов / передохнуть (безопасно, +$100)")

    choice = input("Выбор (1/2): ").strip()

    
    if choice == "1":
        prologue_random = random.randint(1, 2)

        if prologue_random == 1:
            damage = 10
            reward = 200
            print("В переулке завязалась потасовка, но ты забрал свою долю.")
        
        else:
            damage = 10
            reward = 0
            print("В переулке завязалась потасовка, Тебя избили.")
            
    elif choice == "2":
        damage = 0
        reward = 100
        print("Ты не полез на рожон, присмотрелся к району и взял мелкий заказ.")
    else:
        print("Неверный выбор — пролог не засчитан.")
        return

    player["hp"] = max(0, player["hp"] - damage)
    player["money"] += reward
    player["chapter"] = 1
    print(f"Пролог завершён: -{damage} HP, +${reward}. Открыта Миссия 1!")


def mission_1():
    if player["hp"] <= 0:
        print("Сначала восстанови HP командой heal.")
        return

    print("\n--- МИССИЯ 1: ПЕРЕХВАТ ---")
    print("1 - Пролететь на полной скорости (50/50 по шансам и урону)")
    print("2 - Зайти аккуратно (риск -5 HP, награда $350)")

    choice = input("Выбор (1/2): ").strip()

    if choice == "1":
        roll = random.randint(1, 2)
        if roll == 1:
            reward = 700
            damage = 5
            print("50/50 — повезло! Проскочил чисто и забрал $700.")
        else:
            reward = 0
            damage = 25
            print("50/50 — попал под огонь! Выжил, но потерял 25 HP и взял только $0.")
    elif choice == "2":
        damage = 5
        reward = 350
        print("Забрал груз почти без шума, но поцарапал тачку.")
    else:
        print("Неверный выбор.")
        return

    player["hp"] = max(0, player["hp"] - damage)
    player["money"] += reward
    player["chapter"] = 2
    print(f"Итог: -{damage} HP, +${reward}. Открыта Миссия 2!")


def mission_2():
    if player["hp"] <= 0:
        print("Сначала восстанови HP командой heal.")
        return

    print("\n--- МИССИЯ 2: ВСТРЕЧА НА СКЛАДЕ ---")
    print("После перехвата на связь выходит новый человек и зовёт на старый склад.")
    print("1 - Заехать в лоб и показать уверенность (-20 HP, +$900)")
    print("2 - Оставить тачку за углом и зайти пешком (-5 HP, +$550)")

    choice = input("Выбор (1/2): ").strip()

    if choice == "1":
        damage = 20
        reward = 900
        print("Жёсткий разговор на складе — зацепили, но куш сорвал крупный.")
    elif choice == "2":
        damage = 5
        reward = 550
        print("Сработал тихо, без лишних проблем забрал деньги и ушёл.")
    else:
        print("Неверный выбор.")
        return

    player["hp"] = max(0, player["hp"] - damage)
    player["money"] += reward
    player["chapter"] = 3
    print(f"Итог: -{damage} HP, +${reward}. Начало сюжетки пройдено!")


def play_story():
    if player["chapter"] == 0:
        prologue()
    elif player["chapter"] == 1:
        mission_1()
    elif player["chapter"] == 2:
        mission_2()
    else:
        print("Начало сюжетки уже пройдено! Можешь проверить stats или добавить Миссию 3.")


show_stats()
print("Команды: play, stats, heal, quit")

while True:
    cmd = input("\n> ").strip().lower()

    if cmd == "quit":
        break
    elif cmd == "play":
        play_story()
    elif cmd == "stats":
        show_stats()
    elif cmd == "heal":
        heal()
    else:
        print("Неизвестная команда. Доступно: play, stats, heal, quit")