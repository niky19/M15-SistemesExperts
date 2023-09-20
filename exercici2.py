# Màquina de venda de bitllets de metro

class Ticket:
    def __init__(self, name:str, price:float):
        self.name = name
        self.price = price

    def __repr__(self): #definir como aparece en la lista
        return f"{self.name}"
    
def priceCalculator(zone, ticket:Ticket):
    print(ticket)
    price = ticket.price
    calculator = 0
    if zone == 1:
        calculator = 1
    elif zone == 2:
        calculator = 1.35
    elif zone == 3:
        calculator = 1.89
    result = round(price * calculator,2)
    print(f"Preu: {result}")
    return result

def payment(result):
    moneyGiven = 0
    
    while moneyGiven < result:
        print("Introdueix l'import a pagar.")
        print(f"Falten: {result - moneyGiven}")
        moneyGiven += float(input())
    if moneyGiven >  result:
        print(f"Canvi: {moneyGiven - result}")

def ticketMachine():

    metroTickets = [Ticket("Bitllet Senzill",2.20),
                    Ticket("T-Casual", 10.20),
                    Ticket("T-Mes", 54.00),
                    Ticket("T-Trimeste", 145.30),
                    Ticket("T-Jove", 105.00)]

    print("Si us plau, escull el numero del bitllet vols comprar.")
    for ticket in enumerate(metroTickets):
        print(ticket)
    
    userTicketChoice = int(input())
    selectedTicket = metroTickets[userTicketChoice]
    print(f"Has seleccionat {selectedTicket}. Si us plau, indica quina zona vols a continuacio: 1, 2 o 3")
    payment(priceCalculator(int(input()),selectedTicket))



while True:
    ticketMachine()