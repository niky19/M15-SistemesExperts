""" 
def waterBillCalculator():
    print("Indica el teu consum mensual en llitres")
    userWater = int(input())
    fixedFee = 6
    finalFee = 0
    if userWater <= 50:
        finalFee = fixedFee
        print(finalFee)
    elif userWater in range(50,200):
        finalFee = userWater * 0.1 + fixedFee
        print(finalFee)
    else:
        finalFee = userWater * 0.3 + fixedFee


waterBillCalculator()

"""

def waterBillCalculator():
    print("Indica el teu consum mensual en llitres")
    userWater = int(input())
    fixedFee = 6
    calculator = 0
    if userWater <= 50:
        calculator = 0
    elif userWater in range(50,200):
        calculator = 0.1
    else:
        calculator = 0.3
    print(fixedFee + userWater * calculator)

waterBillCalculator()