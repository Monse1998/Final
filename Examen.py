from colorama import init, Fore
init(autoreset=True)

# Inventario simple
inv = {
    "Paracetamol": {"precio": 50, "cantidad": 30},
    "Ibuprofeno": {"precio": 90, "cantidad": 25},
    "Omeprazol": {"precio": 100, "cantidad": 51},
    "Amoxicilina": {"precio": 50, "cantidad": 28},
    "Loratadina": {"precio": 85, "cantidad": 32},
    "Metformina": {"precio": 250, "cantidad": 40},
    "Losartán": {"precio": 128, "cantidad": 15},
    "Aspirina": {"precio": 98, "cantidad": 20},
    "Salbutamol": {"precio": 135, "cantidad": 18},
    "Diclofenaco": {"precio": 187, "cantidad": 29},
    "Ranitidina": {"precio": 69, "cantidad": 17},
    "Naproxeno": {"precio": 234, "cantidad": 20},
    "Cetirizina": {"precio": 398, "cantidad": 10}
}

fila = []

def agregar_cliente(nombre):
    fila.append(nombre)
    print(Fore.GREEN + "✅ Cliente agregado:", nombre)

def ver_clientes():
    if fila:
        print(Fore.CYAN + "\n️Clientes en espera:")
        for c in fila:
            print("➡️", c)
    else:
        print(Fore.YELLOW + "\n 🚫 No hay clientes en espera.")

def ver_inventario():
    print(Fore.BLUE + "\n📦 Inventario:")
    num = 1
    for med in inv:
        print(f"{num}. {med} - Precio: ${inv[med]['precio']} - Cantidad: {inv[med]['cantidad']}")
        num = num + 1

def venta():
    if not fila:
        print(Fore.RED + "🚫 No hay clientes en espera.")
        return

    cliente = fila[0]
    print(Fore.CYAN + f"\n**Registrar venta de: {cliente}**")
    
    compras = []
    total = 0
    nombres = list(inv)

    while True:
        ver_inventario()
        try:
            num = int(input(Fore.MAGENTA +"\n🔹 Elige el número del medicamento: "))
            if num < 1 or num > len(nombres):
                print(Fore.RED + "❌ Número inválido.")
                continue
            med = nombres[num - 1]
        except:
            print(Fore.RED + "❌ Ingresa un número válido.")
            continue

        if inv[med]["cantidad"] == 0:
            print(Fore.RED + "❌ Medicamento agotado.")
            continue

        while True:
            try:
                cant = int(input(f"-Cantidad: "))
                if cant <= 0:
                    print(Fore.YELLOW + "⚠️ Debe ser mayor que cero.")
                elif cant > inv[med]["cantidad"]:
                    print(Fore.RED + "❌ No hay suficiente cantidad.")
                else:
                    sub = cant * inv[med]["precio"]
                    compras.append([med, cant, sub])
                    inv[med]["cantidad"] -= cant
                    total = total + sub
                    break
            except:
                print(Fore.RED + "❌ Ingresa una cantidad válida.")

        while True:
            otra = input("¿Agregar otro medicamento? (s/n): ").strip().lower()
            if otra == "s":
                break
            elif otra == "n":
                break
            else:
                print(Fore.RED + "❌ Opción inválida. Escribe solo 's' o 'n'.")
        if otra == "n":
            break

    if compras:
        print("\n----------------------------------")
        print(Fore.MAGENTA + f"     TICKET DE COMPRA DE {cliente.upper()} " )
        print("----------------------------------")
        print("|                                |")
        for med, cant, sub in compras:
            print(f"| 💊 {med} x{cant} - ${sub}    ")
            print("|--------------------------------|")
        print("|                                |")
        print("| 💰 Total a pagar:$ ", total)
        print("|                                |")
        print("|       ||||||||||||||||||       |")
        print("----------------------------------")
    else:
        print(Fore.YELLOW + "🟡 No se realizó compra.")

def siguiente():
    if fila:
        atendido = fila.pop(0)
        print(Fore.GREEN + " Cliente atendido:", atendido)
    else:
        print(Fore.RED + "🟡 No hay clientes en espera.")

def menu():
    while True:
        print(Fore.CYAN + "\n🩺 MENÚ DE FARMACIA LA PAUU🩺")
        print(Fore.BLUE+"\n1. Agregar cliente")
        print(Fore.BLUE+"2. Ver clientes en espera")
        print(Fore.BLUE+"3. Ver inventario")
        print(Fore.BLUE+"4. Registrar venta")
        print(Fore.BLUE+ "5. Atender siguiente cliente")
        print(Fore.RED +"6. Salir")

        op = input(Fore.YELLOW +"\n🔷 Elige una opción: ")

        if op == "1":
            nom = input("Nombre del cliente: ")
            agregar_cliente(nom)
        elif op == "2":
            ver_clientes()
        elif op == "3":
            ver_inventario()
        elif op == "4":
            venta()
        elif op == "5":
            siguiente()
        elif op == "6":
            print(Fore.MAGENTA + "¡Gracias por usar el sistema!")
            break
        else:
            print(Fore.RED + "❌ Opción no válida.")

menu()
