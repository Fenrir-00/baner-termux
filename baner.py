import os, sys, time, io
class color:
    morado = '\033[95m'
    blanco = '\033[97m'
    cyan = '\033[96m'
    azul  = '\033[94m'
    verde = '\033[92m'
    amarillo = '\033[93m'
    rojo = '\033[91m'
    fin = '\033[0m'

os.system("pkg install openssh")
os.system("pkg install ruby")
os.system("gem install lolcat")

def banner():
 os.system("clear")
 print(f"""{color.cyan}
███████╗███████╗███╗  ██╗██████╗ ██╗██████╗
██╔════ ██╔════╝████╗ ██║██╔══██╗██║██╔══██╗
█████╗  █████╗  ██╔██╗██║██████╔╝██║██████╔╝
██╔══   ██╔══╝  ██║╚████║██╔══██╗██║██╔══██╗
██║     ███████╗██║ ╚███║██║  ██║██║██║  ██║
╚═╝     ╚══════╝╚═╝  ╚══╝╚═╝  ╚═╝╚═╝╚═╝  ╚═╝""")
 print(f"{color.fin}")

#barra de carga
def carga():
    print(f"{color.verde}")
    print("""Loading…
    █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒""")
    time.sleep(1)
    os.system("clear")
    banner()
    print(f"{color.verde}")
    print("""Loading…10%
    ███▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒""")
    time.sleep(1)
    os.system("clear")
    banner()
    print(f"{color.verde}")
    print("""Loading…30%
    █████▒▒▒▒▒▒▒▒▒▒▒▒▒▒""")
    time.sleep(1)
    os.system("clear")
    banner()
    print(f"{color.verde}")
    print("""Loading…50%
    ██████████▒▒▒▒▒▒▒▒▒""")
    time.sleep(1)
    os.system("clear")
    banner()
    print(f"{color.verde}")
    print("""Loading…70%
    █████████████▒▒▒▒▒▒""")
    time.sleep(1)
    os.system("clear")
    banner()
    print(f"{color.verde}")
    print("""Loading…100%
    ███████████████████""")
    time.sleep(1)
    os.system("clear")
    banner()

#menu principal

def menu():
    os.system("clear")
    banner()
    carga()
    print(f"{color.verde}    QUE BANER TE GUSTARIA PONER")
    print("")
    print(f"{color.verde}[1]LOBO")
    print(f"{color.verde}[2]OSO")
    print(f"{color.verde}[3]MARIO")
    print(f"{color.verde}[4]BATMAN")
    print(f"{color.verde}[5]MIKI")
    print(f"{color.verde}[6]FUCK")
    print(f"{color.verde}[7]MEGAMAN")
    print(f"{color.verde}[8]TANKE")
    print(f"{color.verde}[9]HELICOPTERO")
    print(f"{color.rojo}[0]SALIR{color.fin}")
    eleccion =input(f"{color.cyan}ELIJE UN NUMERO >>{color.fin} ")
    if eleccion == "1" :
        banner()
        lobo()
        print(f"{color.amarillo}CIERRA LA CONSOLA PARA VER LOS CAMBIOS")

    elif eleccion == "2" :
        banner()
        oso()
        print(f"{color.amarillo}CIERRA LA CONSOLA PARA VER LOS CAMBIOS")
    elif eleccion == "3" :
     banner()
     mario()
     print(f"{color.amarillo}CIERRA LA CONSOLA PARA VER LOS CAMBIOS")
    elif eleccion == "4" :
     banner()
     batman()
     print(f"{color.amarillo}CIERRA LA CONSOLA PARA VER LOS CAMBIOS")
    elif eleccion == "5" :
     banner()
     miki()
     print(f"{color.amarillo}CIERRA LA CONSOLA PARA VER LOS CAMBIOS")
    elif eleccion == "6" :
     banner()
     dedo()
     print(f"{color.amarillo}CIERRA LA CONSOLA PARA VER LOS CAMBIOS")   
    elif eleccion == "7" :
     banner()
     megaman()
     print(f"{color.amarillo}CIERRA LA CONSOLA PARA VER LOS CAMBIOS")
    elif eleccion == "8" :
     banner()
     tanke()
     print(f"{color.amarillo}CIERRA LA CONSOLA PARA VER LOS CAMBIOS")
    elif eleccion == "9" :
     banner()
     helicoptero()
     print(f"{color.amarillo}CIERRA LA CONSOLA PARA VER LOS CAMBIOS")
    elif eleccion == "0" :
     banner()
     salir() 
    elif eleccion == "99" :
     banner()
     fenrir()
     print(f"{color.amarillo}CIERRA LA CONSOLA PARA VER LOS CAMBIOS")
  
    else:
        incorrecto()

def incorrecto():
    os.system("clear")
    print(f"""{color.rojo}
░█████╗░██████╗░░█████╗░██╗░█████╗░███╗░░██╗
██╔══██╗██╔══██╗██╔══██╗██║██╔══██╗████╗░██║
██║░░██║██████╔╝██║░░╚═╝██║██║░░██║██╔██╗██║
██║░░██║██╔═══╝░██║░░██╗██║██║░░██║██║╚████║
╚█████╔╝██║░░░░░╚█████╔╝██║╚█████╔╝██║░╚███║
░╚════╝░╚═╝░░░░░░╚════╝░╚═╝░╚════╝░╚═╝░░╚══╝


██╗███╗░░██╗░█████╗░░█████╗░██████╗░██████╗░
██║████╗░██║██╔══██╗██╔══██╗██╔══██╗██╔══██╗
██║██╔██╗██║██║░░╚═╝██║░░██║██████╔╝██████╔╝
██║██║╚████║██║░░██╗██║░░██║██╔══██╗██╔══██╗
██║██║░╚███║╚█████╔╝╚█████╔╝██║░░██║██║░░██║
╚═╝╚═╝░░╚══╝░╚════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝

███████╗░█████╗░████████╗░█████╗░
██╔════╝██╔══██╗╚══██╔══╝██╔══██╗
█████╗░░██║░░╚═╝░░░██║░░░███████║
██╔══╝░░██║░░██╗░░░██║░░░██╔══██║
███████╗╚█████╔╝░░░██║░░░██║░░██║
╚══════╝░╚════╝░░░░╚═╝░░░╚═╝░░╚═╝{color.fin}""")
    time.sleep(4)
    menu()

def salir():
    os.system("clear")
    banner()
    print(f"{color.rojo}")
    print("""SALIENDO…
    █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒""")
    time.sleep(1)
    os.system("clear")
    banner()
    print(f"{color.rojo}")
    print("""SALIENDO…10%
    ███▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒""")
    time.sleep(1)
    os.system("clear")
    banner()
    print(f"{color.rojo}")
    print("""SALIENDO…30%
    █████▒▒▒▒▒▒▒▒▒▒▒▒▒▒""")
    time.sleep(1)
    os.system("clear")
    banner()
    print(f"{color.rojo}")
    print("""SALIENDO…50%
    ██████████▒▒▒▒▒▒▒▒▒""")
    time.sleep(1)
    os.system("clear")
    banner()
    print(f"{color.rojo}")
    print("""SALIENDO…70%
    █████████████▒▒▒▒▒▒""")
    time.sleep(1)
    os.system("clear")
    banner()
    print(f"{color.rojo}")
    print("""SALIENDO…100%
    ███████████████████""")
    time.sleep(1)
    os.system("clear")
    print(f"{color.fin}")
    sys.exit()
def lobo():
 salto = "\n"
 fd = open("/data/data/com.termux/files/usr/etc/bash.bashrc","w")
 fd.write(f"clear{salto}")
 fd.write("""echo -e '''▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒
▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄░░▒▒▒▒▒
▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██▌░░▒▒▒▒
▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░▄▄███▀░░░░▒▒▒
▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░█████░▄█░░░░▒▒
▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░▄████████▀░░░░▒▒
▒▒░░░░░░░░░░░░░░░░░░░░░░░░▄█████████░░░░░░░▒
▒░░░░░░░░░░░░░░░░░░░░░░░░░░▄███████▌░░░░░░░▒
▒░░░░░░░░░░░░░░░░░░░░░░░░▄█████████░░░░░░░░▒
▒░░░░░░░░░░░░░░░░░░░░░▄███████████▌░░░░░░░░▒
▒░░░░░░░░░░░░░░░▄▄▄▄██████████████▌░░░░░░░░▒
▒░░░░░░░░░░░▄▄███████████████████▌░░░░░░░░░▒
▒░░░░░░░░░▄██████████████████████▌░░░░░░░░░▒
▒░░░░░░░░████████████████████████░░░░░░░░░░▒
▒█░░░░░▐██████████▌░▀▀███████████░░░░░░░░░░▒
▐██░░░▄██████████▌░░░░░░░░░▀██▐█▌░░░░░░░░░▒▒
▒██████░█████████░░░░░░░░░░░▐█▐█▌░░░░░░░░░▒▒
▒▒▀▀▀▀░░░██████▀░░░░░░░░░░░░▐█▐█▌░░░░░░░░▒▒▒
▒▒▒▒▒░░░░▐█████▌░░░░░░░░░░░░▐█▐█▌░░░░░░░▒▒▒▒
▒▒▒▒▒▒░░░░███▀██░░░░░░░░░░░░░█░█▌░░░░░░▒▒▒▒▒
▒▒▒▒▒▒▒▒░▐██░░░██░░░░░░░░▄▄████████▄▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒██▌░░░░█▄░░░░░░▄███████████████████
▒▒▒▒▒▒▒▒▒▐██▒▒░░░██▄▄███████████████████████
▒▒▒▒▒▒▒▒▒▒▐██▒▒▄████████████████████████████
▒▒▒▒▒▒▒▒▒▒▄▄████████████████████████████████
████████████████████████████████████████████''' |lolcat""")
 fd.write(f"{salto}PS1='\[\e[0;32m\]\w\[\e[0m\] \[\e[0;97m\]\$\[\e[0m\] '")
 fd.close()
def helicopter():
 salto = "\n"
 fd = open("/data/data/com.termux/files/usr/etc/bash.bashrc","w")
 fd.write(f"clear{salto}")
 fd.write("""echo -e '''  ''' |lolcat""")
 fd.write(f"{salto}PS1='$'")
 fd.close()


def oso():
 salto = "\n"
 fd = open("/data/data/com.termux/files/usr/etc/bash.bashrc","w")
 fd.write(f"clear{salto}")
 fd.write("""echo -e '''───▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄───
───█▒▒░░░░░░░░░▒▒█───
────█░░█░░░░░█░░█────
─▄▄──█░░░▀█▀░░░█──▄▄─
█░░█─▀▄░░░░░░░▄▀─█░░█
█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
█░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█
█░░║║║╠─║─║─║║║║║╠─░░█
█░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█
█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█  ''' |lolcat""")
 fd.write(f"{salto}PS1='\[\e[0;32m\]\w\[\e[0m\] \[\e[0;97m\]\$\[\e[0m\] '")
 fd.close()


def mario():
 salto = "\n"
 fd = open("/data/data/com.termux/files/usr/etc/bash.bashrc","w")
 fd.write(f"clear{salto}")
 fd.write("""echo -e '''░░░░█████░░░░░░░░
░░░█▓▓▒▓▓██░░░░░░
░░░█▓▒▒▒▓▓▓█░░░░░
░░███████▓▓▓█░░░░
░██████████▓▓█░░░
░███████████▓▓█░░
░░██░░▒░░▒██▓██░░
░░░█░█▒█░▒▒██▒▒█░
░░█▒░█▒█░▒▒██▒▒█░
░░█▒▒▒▒▒▒▒██▒▒▒█░
░░█▒▒▒▒██▒▒█▒▒▒█░
░░███████▒▒▒██░░░
░░██████▒▒▒▒██░░░
░░░░█▒▒▒▒▒▒██░░░░
░░░░░██████░░░░░░ ''' |lolcat""")
 fd.write(f"{salto}PS1='\[\e[0;32m\]\w\[\e[0m\] \[\e[0;97m\]\$\[\e[0m\] '")
 fd.close()

def batman():
 salto = "\n"
 fd = open("/data/data/com.termux/files/usr/etc/bash.bashrc","w")
 fd.write(f"clear{salto}")
 fd.write("""echo -e '''░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░▄█░░░░░░░░░░░░██░░░
░░░░░▄██░░░░░░░░░░░███░░░
░░░░░███░░░░░░░░░░████░░░
░░░░████░░▄▄▄▄░░░█████░░░
░░░███████████████████░░░
░░░███████████████████░░░
░▄█████████████████████░░
░██████████████████████░░
░██████████████████████░░
░█░▀████████▀░▄████████░░
▄██▄▄█████▄▄▄██████████▄░
██▀███████▀▀█▀▀░░███████░
░█░░░▀▀▀░░░░▀▀░░░███████░
░█░░░████▄░░░░░░░████████
░█░░░░░░░░░░░░░░░████████
░██░░░░░░░░░░░░░░████████
░░█░░░░░░░░░░░░▄█████████  ''' |lolcat""")
 fd.write(f"{salto}PS1='\[\e[0;32m\]\w\[\e[0m\] \[\e[0;97m\]\$\[\e[0m\] '")
 fd.close()

def miki():
 salto = "\n"
 fd = open("/data/data/com.termux/files/usr/etc/bash.bashrc","w")
 fd.write(f"clear{salto}")
 fd.write("""echo -e '''▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓█████▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓████████▓▓▓▓▓▓▓▓▓
▓▓▓▓████████▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓█████████▓▓▓▓▓▓▓▓
████▓▓█████▓░▓██▓▓▓▓▓▓
█████▒▓███▒░░░▓█▓▓▓▓▓▓
██████████░░░░█▒██▓▓▓▓
██████▒░░█░░░░█▒█▓▓▓▓▓
█████▓░░░░░░░░█▒███▓██
█████░░▒▒░░░░░█░▓▒░███
▓▓▓▓█▒░░▒░░░░░░░░░░░█▓
▓▓▓▓█▓░░░▓░░░░░░░░░▒█▓
▓▓▓▓▓█▒░░██░░░░░░░▒█▓▓
▓▓▓▓▓▓█▓▒▓███▓▒▒▒▓█▓▓▓
▓▓▓▓▓▓▓██▒███░████▓▓▓▓
▓▓▓▓▓▓▓██▓░▒░▓█████▓▓▓  ''' |lolcat""")
 fd.write(f"{salto}PS1='\[\e[0;32m\]\w\[\e[0m\] \[\e[0;97m\]\$\[\e[0m\] '")
 fd.close()

def tanke():
 salto = "\n"
 fd = open("/data/data/com.termux/files/usr/etc/bash.bashrc","w")
 fd.write(f"clear{salto}")
 fd.write("""echo -e '''-----██████████ ]▄▄▄▄▄▄▄▄▄▄▄▄▃
▂▄▅█████████▅▄▃▂
I███████████████████].
◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙◤...  ''' |lolcat""")
 fd.write(f"{salto}PS1='\[\e[0;32m\]\w\[\e[0m\] \[\e[0;97m\]\$\[\e[0m\] '")
 fd.close()

def dedo():
 salto = "\n"
 fd = open("/data/data/com.termux/files/usr/etc/bash.bashrc","w")
 fd.write(f"clear{salto}")
 fd.write("""echo -e '''░░░░░░░░░░░░░░░▄▄░░░░░░░░░░░
░░░░░░░░░░░░░░█░░█░░░░░░░░░░
░░░░░░░░░░░░░░█░░█░░░░░░░░░░
░░░░░░░░░░░░░░█░░█░░░░░░░░░░
░░░░░░░░░░░░░░█░░█░░░░░░░░░░
██████▄███▄████░░███▄░░░░░░░
▓▓▓▓▓▓█░░░█░░░█░░█░░░███░░░░
▓▓▓▓▓▓█░░░█░░░█░░█░░░█░░█░░░
▓▓▓▓▓▓█░░░░░░░░░░░░░░█░░█░░░
▓▓▓▓▓▓█░░░░░░░░░░░░░░░░█░░░░
▓▓▓▓▓▓█░░░░░░░░░░░░░░██░░░░░
▓▓▓▓▓▓█████░░░░░░░░░██░░░░░░  ''' |lolcat""")
 fd.write(f"{salto}PS1='\[\e[0;32m\]\w\[\e[0m\] \[\e[0;97m\]\$\[\e[0m\] '")
 fd.close()

def megaman():
 salto = "\n"
 fd = open("/data/data/com.termux/files/usr/etc/bash.bashrc","w")
 fd.write(f"clear{salto}")
 fd.write("""echo -e '''░░░░░░░░░░▄▄█▀▀▄░░░░
░░░░░░░░▄█████▄▄█▄░░░░
░░░░░▄▄▄▀██████▄▄██░░░░
░░▄██░░█░█▀░░▄▄▀█░█░░░▄▄▄▄
▄█████░░██░░░▀▀░▀░█▀▀██▀▀▀█▀▄
█████░█░░▀█░▀▀▀▀▄▀░░░███████▀
░▀▀█▄░██▄▄░▀▀▀▀█▀▀▀▀▀░▀▀▀▀
░▄████████▀▀▀▄▀░░░░
██████░▀▀█▄░░░█▄░░░░
░▀▀▀▀█▄▄▀░██████▄░░░░
░░░░░░░░░█████████░░░░  ''' |lolcat""")
 fd.write(f"{salto}PS1='\[\e[0;32m\]\w\[\e[0m\] \[\e[0;97m\]\$\[\e[0m\] '")
 fd.close() 


def helicoptero():
 salto = "\n"
 fd = open("/data/data/com.termux/files/usr/etc/bash.bashrc","w")
 fd.write(f"clear{salto}")
 fd.write("""echo -e '''──▀▀▀▀▀▀▀▀▀▀▀▄▄▀▀▀▀▀▀▀▀▀▀▀
────────────█▀▀█
───────────█▓▓▓▓█
───────══▄▀█▓▓▓▓█▀▄══
──▄▄▄▄▄▄▄█▒█▓▓▓▓█▒█▄▄▄▄▄▄▄
──█▀▀▀▀█▀███▄▓▓▄███▀█▀▀▀▀█
─▄█▄──▄█▄───▀██▀───▄█▄──▄█▄
─█▒█──█▒█──────────█▒█──█▒█
─▀▀▀──▀▀▀──────────▀▀▀──▀▀▀  ''' |lolcat""")
 fd.write(f"{salto}PS1='\[\e[0;32m\]\w\[\e[0m\] \[\e[0;97m\]\$\[\e[0m\] '")
 fd.close() 

def fernrir():
 salto = "\n"
 fd = open("/data/data/com.termux/files/usr/etc/bash.bashrc","w")
 fd.write(f"clear{salto}")
 fd.write("""echo -e '''███████╗███████╗███╗  ██╗██████╗ ██╗██████╗
██╔════ ██╔════╝████╗ ██║██╔══██╗██║██╔══██╗
█████╗  █████╗  ██╔██╗██║██████╔╝██║██████╔╝
██╔══   ██╔══╝  ██║╚████║██╔══██╗██║██╔══██╗
██║     ███████╗██║ ╚███║██║  ██║██║██║  ██║
╚═╝     ╚══════╝╚═╝  ╚══╝╚═╝  ╚═╝╚═╝╚═╝  ╚═╝ ''' |lolcat""")
 fd.write(f"{salto}PS1='\[\e[0;32m\]\w\[\e[0m\] \[\e[0;97m\]\$\[\e[0m\] '")
 fd.close() 




menu()
