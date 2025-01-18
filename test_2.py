from modules import TwoBetCalculate

calc = TwoBetCalculate()
bet_data = {"true_odd1": 2, "true_odd2": 2}

od1, od2 = calc.fair_odds(bet_data)
print(od1)
print(od2)

