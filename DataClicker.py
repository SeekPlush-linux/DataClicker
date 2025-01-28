from rich import print
import time
import os
import json
import sys
import termios
import tty
import random

# TODO: Optimize the "upgrades" printing to console by using a for loop instead

def save_data():
    with open("data.json", "w") as f:
        json.dump(data, f)
    print("[bright_green]User data saved.[/]")

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

print("DataClicker v1.0.0, ported from C++ to Python")
print("[bright_yellow]Loading user data...[/]")

with open("data.json", "r") as f:
    data = json.load(f)
currency = ['', 'K', 'M', 'G', 'T', 'P']

print("[bright_green]User data loaded.[/]")

os.system("clear")
print("[bold bright_cyan]DataClicker: Data Mining Clicker game; Version 1.0.0[/]")
print("[bright_magenta][bold]Creator:[/] Seek Plush Cool[/]")
print("[bright_blue][bold]My Discord:[/] @3460[/]")
print("If you found bugs or have any questions, please contact me on Discord!\n")
print(" What's new?")
print(" - First Release!\n")
print("[bright_yellow]Press any key to continue.[/]")
getch()
os.system("clear")

while True:
    dmoney = data["money"]
    dclick = data["click"] * data["boost"]
    dclp1 = data["clp1"]
    dclc1 = data["clc1"]
    dclp2 = data["clp2"]
    dclc2 = data["clc2"]
    dclp3 = data["clp3"]
    dclc3 = data["clc3"]
    dclp4 = data["clp4"]
    dclc4 = data["clc4"]
    dclp5 = data["clp5"]
    dclc5 = data["clc5"]
    dclp6 = data["clp6"]
    dclc6 = data["clc6"]
    dclp7 = data["clp7"]
    dclc7 = data["clc7"]
    dclp8 = data["clp8"]
    dclc8 = data["clc8"]
    dclp9 = data["clp9"]
    dclc9 = data["clc9"]
    dclp10 = data["clp10"]
    dclc10 = data["clc10"]

    curg = 0
    curm = 0

    if curg == 0 and data["click"] * data["boost"] >= 1000:
        curg = 1
    if curg == 1:
        dclick = data["click"] * data["boost"] / 1000
    if curg == 1 and data["click"] * data["boost"] >= 1000000:
        curg = 2
    if curg == 2:
        dclick = data["click"] * data["boost"] / 1000000
    if curg == 2 and data["click"] * data["boost"] >= 1000000000:
        curg = 3
    if curg == 3:
        dclick = data["click"] * data["boost"] / 1000000000
    if curg == 3 and data["click"] * data["boost"] >= 1000000000000:
        curg = 4
    if curg == 4:
        dclick = data["click"] * data["boost"] / 1000000000000
    if curg == 4 and data["click"] * data["boost"] >= 1000000000000000:
        curg = 5
    if curg == 5:
        dclick = data["click"] * data["boost"] / 1000000000000000

    if curm == 5 and data["money"] < 1000000000000000:
        curm = 4
    if curm == 4 and data["money"] < 1000000000000:
        curm = 3
    if curm == 3 and data["money"] < 1000000000:
        curm = 2
    if curm == 2 and data["money"] < 1000000:
        curm = 1
    if curm == 1 and data["money"] < 1000:
        curm = 0
    if curm == 0 and data["money"] >= 1000:
        curm = 1
    if curm == 1:
        dmoney = data["money"] / 1000
    if curm == 1 and data["money"] >= 1000000:
        curm = 2
    if curm == 2:
        dmoney = data["money"] / 1000000
    if curm == 2 and data["money"] >= 1000000000:
        curm = 3
    if curm == 3:
        dmoney = data["money"] / 1000000000
    if curm == 3 and data["money"] >= 1000000000000:
        curm = 4
    if curm == 4:
        dmoney = data["money"] / 1000000000000
    if curm == 4 and data["money"] >= 1000000000000000:
        curm = 5
    if curm == 5:
        dmoney = data["money"] / 1000000000000000
    
    curu1 = 0
    curuc1 = 0
    curu2 = 0
    curuc2 = 0
    curu3 = 0
    curuc3 = 0
    curu4 = 0
    curuc4 = 0
    curu5 = 0
    curuc5 = 0
    curu6 = 0
    curuc6 = 0
    curu7 = 0
    curuc7 = 0
    curu8 = 0
    curuc8 = 0
    curu9 = 0
    curuc9 = 0
    curu10 = 0
    curuc10 = 0

    for i in range(1, 11):
        dclp = data[f"clp{i}"]
        dclc = data[f"clc{i}"]
        curu = 0
        curuc = 0

        while dclp >= 1000:
            dclp /= 1000
            curu += 1
        while dclc >= 1000:
            dclc /= 1000
            curuc += 1

        locals()[f"dclp{i}"] = dclp
        locals()[f"dclc{i}"] = dclc
        locals()[f"curu{i}"] = curu
        locals()[f"curuc{i}"] = curuc
    
    dmoney = round(dmoney, 2)
    dclick = round(dclick, 2)

    print(f"[bright_green]Money: {dmoney} {currency[curm]}B[/]    [bright_magenta]Rebirths: {data['rebirth']}[/]    [bright_blue]Boost: {data['boost']}x[/]\n")
    print(f"[bright_green]To earn {dclick} {currency[curg]}B, press 1.[/]")
    print("To open settings, press M.")
    print("To save and exit, press X.\n")
    print("[bold]Upgrades:[/]")
    print(f"1. [bright_cyan]+{dclp1} {currency[curu1]}B[/] for [bright_green]{dclc1} {currency[curuc1]}B[/] [bold white][Q][/]")
    print(f"2. [bright_cyan]+{dclp2} {currency[curu2]}B[/] for [bright_green]{dclc2} {currency[curuc2]}B[/] [bold white][W][/]")
    print(f"3. [bright_cyan]+{dclp3} {currency[curu3]}B[/] for [bright_green]{dclc3} {currency[curuc3]}B[/] [bold white][E][/]")
    print(f"4. [bright_cyan]+{dclp4} {currency[curu4]}B[/] for [bright_green]{dclc4} {currency[curuc4]}B[/] [bold white][R][/]")
    print(f"5. [bright_cyan]+{dclp5} {currency[curu5]}B[/] for [bright_green]{dclc5} {currency[curuc5]}B[/] [bold white][T][/]")
    print(f"6. [bright_cyan]+{dclp6} {currency[curu6]}B[/] for [bright_green]{dclc6} {currency[curuc6]}B[/] [bold white][Y][/]")
    print(f"7. [bright_cyan]+{dclp7} {currency[curu7]}B[/] for [bright_green]{dclc7} {currency[curuc7]}B[/] [bold white][U][/]")
    print(f"8. [bright_cyan]+{dclp8} {currency[curu8]}B[/] for [bright_green]{dclc8} {currency[curuc8]}B[/] [bold white][I][/]")
    print(f"9. [bright_cyan]+{dclp9} {currency[curu9]}B[/] for [bright_green]{dclc9} {currency[curuc9]}B[/] [bold white][O][/]")
    print(f"10. [bright_cyan]+{dclp10} {currency[curu10]}B[/] for [bright_green]{dclc10} {currency[curuc10]}B[/] [bold white][P][/]\n")
    print("[bold]Rebirths [NEW]:[/]")
    print("1. [bright_magenta]+1 Rebirth[/] for [bright_green]100 GB[/] [bold white][A][/]")

    # print("\n\n", data["clc4"])
    # print(data["secrethack"])
    # print(data["clc4"] * 14 - 2010)
    # print("clc4 is 140000") if data["clc4"] == 140000 else print("clc4 is not 140000")

    time.sleep(0.1)
    cmd = getch()

    os.system("clear")

    if cmd == "1":
        data["money"] = data["money"] + data["click"] * data["boost"]
    
    elif cmd == "q" and data["money"] >= data["clc1"]:
        data["money"] -= data["clc1"]
        data["click"] += data["clp1"] * data["boost"]
        data["clp1"] += 1
        data["clc1"] += 0.5
    
    elif cmd == "w" and data["money"] >= data["clc2"]:
        data["money"] -= data["clc2"]
        data["click"] += data["clp2"] * data["boost"]
        data["clp2"] += 10
        data["clc2"] += 100
    
    elif cmd == "e" and data["money"] >= data["clc3"]:
        data["money"] -= data["clc3"]
        data["click"] += data["clp3"] * data["boost"]
        data["clp3"] += 100
        data["clc3"] += 1000
    
    elif cmd == "r" and data["money"] >= data["clc4"]:
        data["money"] -= data["clc4"]
        data["click"] += data["clp4"] * data["boost"]
        data["clp4"] += 1000
        data["clc4"] += 20000
    
    elif cmd == "t" and data["money"] >= data["clc5"]:
        data["money"] -= data["clc5"]
        data["click"] += data["clp5"] * data["boost"]
        data["clp5"] += 5000
        data["clc5"] += 100000
    
    elif cmd == "y" and data["money"] >= data["clc6"]:
        data["money"] -= data["clc6"]
        data["click"] += data["clp6"] * data["boost"]
        data["clp6"] += 80000
        data["clc6"] += 2000000
    
    elif cmd == "u" and data["money"] >= data["clc7"]:
        data["money"] -= data["clc7"]
        data["click"] += data["clp7"] * data["boost"]
        data["clp7"] += 500000
        data["clc7"] += 10000000
    
    elif cmd == "i" and data["money"] >= data["clc8"]:
        data["money"] -= data["clc8"]
        data["click"] += data["clp8"] * data["boost"]
        data["clp8"] += 5000000
        data["clc8"] += 200000000
    
    elif cmd == "o" and data["money"] >= data["clc9"]:
        data["money"] -= data["clc9"]
        data["click"] += data["clp9"] * data["boost"]
        data["clp9"] += 50000000
        data["clc9"] += 3000000000
    
    elif cmd == "p" and data["money"] >= data["clc10"]:
        data["money"] -= data["clc10"]
        data["click"] += data["clp10"] * data["boost"]
        data["clp10"] += 200000000
        data["clc10"] += 15000000000
    
    elif cmd == "m":
        temp = 0
        while cmd != "z":
            os.system("clear")

            if temp == 1:
                print("[yellow]Something suddenly changed in the game's code...[/]\n")
                temp = 0
            elif temp == 2:
                print("[bright_green]You've successfully reset the game and its settings.[/]\n")
                temp = 0

            print("[bold]----Menu----[/]")
            print("To upgrade your clicker, click on the letter shown in the square brackets.")
            print("To enable/disable the rebirth scene, press A.")
            print("To reset the game and its settings, press R.")
            print("To leave this menu and go back to the game, press Z.\n")
            print("[bold]Settings:[/]")
            print(f"Rebirth Scene [bold white][A][/]: {data['rebirthscene']}")
            print("[bright_red]Reset game and settings [blink]!!DANGEROUS!![/][/] [red][R][/]")

            cmd = getch()

            if cmd == "a":
                if data["rebirthscene"] == 0:
                    data["rebirthscene"] = 1
                else:
                    data["rebirthscene"] = 0
            
            elif cmd == "r":
                os.system("clear")
                print("[bright_red]Are you sure you want to reset the game and its settings? [Y/N]")
                print("[red][blink]WARNING:[/] This action is irreversible and will reset your progress (and settings).[/]")
                cmd = getch()
                if cmd == "y":
                    with open("data-default.json", "r") as f:
                        data = json.load(f)
                    os.system("clear")
                    temp = 2
            
            elif cmd == "H":
                cmd = getch()
                if cmd == "A":
                    cmd = getch()
                    if cmd == "C":
                        cmd = getch()
                        if cmd == "K":
                            cmd = getch()
                            if cmd == "E":
                                cmd = getch()
                                if cmd == "R":
                                    cmd = getch()
                                    if cmd == " ":
                                        cmd = getch()
                                        if cmd == "T":
                                            cmd = getch()
                                            if cmd == "I":
                                                cmd = getch()
                                                if cmd == "M":
                                                    cmd = getch()
                                                    if cmd == "E":
                                                        if data["secrethack"] == 1957990:
                                                            data["secrethack"] = 0
                                                        elif data["clc4"] == 140000:
                                                            data["secrethack"] = data["clc4"] * 14 - 2010
                                                        temp = 1
        os.system("clear")

    elif cmd == "a" and data["money"] >= 100000000000:
        print("[bright_yellow]Are you sure you want to +1 rebirth for 100 GB? [Y/N][/]")
        print("[yellow][blink]WARNING:[/] This action is irreversible and will reset your progress.[/]")
        cmd = getch()
        if cmd == "y":
            time.sleep(0.5)
            print("[bright_white]Rebirthing...[/]\n")
            if data["rebirthscene"] == 1:
                os.system("clear")
                time.sleep(0.7)
                progress = ["[          ]  0%", "[█         ]  10%", "[██        ]  20%", "[███       ]  30%", "[████      ]  40%", "[█████     ]  50%", "[██████    ]  60%", "[███████   ]  70%", "[████████  ]  80%", "[█████████ ]  90%", "[██████████]  100%"]
                print("[bright_white]Reseting progress...[/]")
                time.sleep(0.5)
                for i in range(11):
                    print(progress[i], end="\r")
                    time.sleep(random.uniform(0.1, 0.4))
                print(end="\n\n")
                time.sleep(1)
                print("[bright_white]Adding 1.5x boost...[/]")
                time.sleep(0.5)
                for i in range(11):
                    print(progress[i], end="\r")
                    time.sleep(random.uniform(0.05, 0.2))
                print(end="\n\n")
                time.sleep(1)
                print("[bright_white]Preparing new upgrades...[/]")
                time.sleep(0.5)
                for i in range(11):
                    print(progress[i], end="\r")
                    time.sleep(random.uniform(0.2, 0.3))
                print("\n\n[bright_white]Restarting...[/]")
                time.sleep(1.5)
            data["money"] = 0
            data["rebirth"] += 1
            data["click"] = 1
            data["boost"] += 0.5
            data["clp1"] = 1
            data["clc1"] = 0.5
            data["clp2"] = 10
            data["clc2"] = 100
            data["clp3"] = 100
            data["clc3"] = 1000
            data["clp4"] = 1000
            data["clc4"] = 20000
            data["clp5"] = 5000
            data["clc5"] = 100000
            data["clp6"] = 80000
            data["clc6"] = 2000000
            data["clp7"] = 500000
            data["clc7"] = 10000000
            data["clp8"] = 5000000
            data["clc8"] = 200000000
            data["clp9"] = 50000000
            data["clc9"] = 3000000000
            data["clp10"] = 200000000
            data["clc10"] = 15000000000
            os.system("clear")
            time.sleep(2)
            print("[bright_green]Congratulations! You've successfully +1 rebirthed and got a permanent 1.5x boost![/]\n")
        else:
            os.system("clear")
            print("[bright_red]You've cancelled the rebirth process.[/]\n")
    
    elif cmd == "+" and data["secrethack"] == 1957990:
        data["money"] += 100000000000
        print("[bright_green]CHEAT CODE ACTIVATED[/]\n")
    
    elif cmd in ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p"]:
        print("[bright_red]You don't have enough money to buy this upgrade.[/]\n")
    
    elif cmd == "a":
        print("[bright_red]You don't have enough money to rebirth.[/]\n")

    elif cmd == "x":
        save_data()
        print("[bright_green]You've successfully left the game.[/]")
        print("Come back next time!\n")
        print("[bright_yellow]Press any key to exit.[/]")
        getch()
        exit()
