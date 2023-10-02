# Màquina de venda de bitllets de metro


class Ticket:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __repr__(self):  # definir como aparece en la lista
        return f"{self.name}"


def priceCalculator(zone, ticket: Ticket):
    print(ticket)
    price = ticket.price
    calculator = 0
    if zone == 1:
        calculator = 1
    elif zone == 2:
        calculator = 1.35
    elif zone == 3:
        calculator = 1.89
    result = round(price * calculator, 2)
    print(f"Preu: {result}")
    return result


def payment(result):
    allowedMoney = [0.05, 0.10, 0.20, 0.50, 1, 2, 5, 10, 20, 50]
    moneyGiven = 0
    while moneyGiven < result:
        print("Introdueix l'import a pagar.")
        print(f"Falten: {round(result - moneyGiven, 2)}")
        input_money = float(input())
        if input_money in allowedMoney:
            moneyGiven += input_money
        else:
            print(
                "Aquesta moneda/billet no és vàlida. Si us plau, utilitza només les següents monedes i bitllets:"
            )
            print("Monedes: 0.5ct, 1ct, 2ct, 5ct, 10ct, 20ct, 50ct, 1€, 2€")
            print("Bitllets: 5€, 10€, 20€, 50€")


def ticketMachine():
    metroTickets = [
        Ticket("Bitllet Senzill", 2.40),
        Ticket("T-Casual", 11.35),
        Ticket("T-Usual", 20.00),
        Ticket("T-Grup", 79.45),
        Ticket("T-Jove", 40.00),
    ]

    print(
        "Benvingut a la màquina de venda de tiquets. Si us plau, escull el numero del bitllet que vols comprar."
    )
    for idx, ticket in enumerate(metroTickets):
        print(f"{idx} -> {ticket}")
    userTicketChoice = int(input())
    selectedTicket = metroTickets[userTicketChoice]
    print(
        f"Has seleccionat {selectedTicket}. Si us plau, indica quina zona vols a continuacio: 1, 2 o 3"
    )
    payment(priceCalculator(int(input()), selectedTicket))


while True:
    ticketMachine()
