import pandas as pd

from math import log2

def calculate_information_gain(p, n):
  try:
    return round((-p/(p + n)) * log2(p/ (p + n)) - (n/(p + n)) * log2(n/(p + n))  , 3)
  except:
    return 0

def calculate_entropy(pi, ni, p, n):
  return round(((pi + ni) / (p + n) ) * calculate_information_gain(pi, ni), 3)

def calculate_daytime(df, p, n):
    pi1 = 0
    ni1 = 0
    for data in df.index:
        if(df['Daytime'][data] == "Afternoon" and df['Drink_Coffee'][data] == "Yes"):
            pi1 += 1
        elif(df['Daytime'][data] == "Afternoon" and df['Drink_Coffee'][data] == "No"):
            ni1 += 1

    ent1 = calculate_entropy(pi1, ni1, p, n)
    print("P:", pi1)
    print("N:", ni1)
    print("IG Afternoon:", calculate_information_gain(pi1, ni1))

    pi2 = 0
    ni2 = 0
    for data in df.index:
        if(df['Daytime'][data] == "Evening" and df['Drink_Coffee'][data] == "Yes"):
            pi2 += 1
        elif(df['Daytime'][data] == "Evening" and df['Drink_Coffee'][data] == "No"):
            ni2 += 1

    ent2 = calculate_entropy(pi2, ni2, p, n)
    print("P:", pi2)
    print("N:", ni2)
    print("IG Evening:", calculate_information_gain(pi2, ni2))

    pi3 = 0
    ni3 = 0
    for data in df.index:
        if(df['Daytime'][data] == "Morning" and df['Drink_Coffee'][data] == "Yes"):
            pi3 += 1
        elif(df['Daytime'][data] == "Morning" and df['Drink_Coffee'][data] == "No"):
            ni3 += 1
    
    ent3 = calculate_entropy(pi3, ni3, p, n)
    print("P:", pi3)
    print("N:", ni3)
    print("IG Morning:", calculate_information_gain(pi3, ni3))
    
    print(ent1, ent2, ent3)
    return round((ent1 + ent2 + ent3), 3)

def calculate_sugar(df, p, n):
    pi1 = 0
    ni1 = 0
    for data in df.index:
        if(df['Sugar'][data] == "Zero" and df['Drink_Coffee'][data] == "Yes"):
            pi1 += 1
        elif(df['Sugar'][data] == "Zero" and df['Drink_Coffee'][data] == "No"):
            ni1 += 1
    
    ent1 = calculate_entropy(pi1, ni1, p, n)
    print("P:", pi1)
    print("N:", ni1)
    print("IG Zero:", calculate_information_gain(pi1, ni1))

    pi2 = 0
    ni2 = 0
    for data in df.index:
        if(df['Sugar'][data] == "Less" and df['Drink_Coffee'][data] == "Yes"):
            pi2 += 1
        elif(df['Sugar'][data] == "Less" and df['Drink_Coffee'][data] == "No"):
            ni2 += 1
    
    ent2 = calculate_entropy(pi2, ni2, p, n)
    print("P:", pi2)
    print("N:", ni2)
    print("IG Less:", calculate_information_gain(pi2, ni2))

    pi3 = 0
    ni3 = 0
    for data in df.index:
        if(df['Sugar'][data] == "Normal" and df['Drink_Coffee'][data] == "Yes"):
            pi3 += 1
        elif(df['Sugar'][data] == "Normal" and df['Drink_Coffee'][data] == "No"):
            ni3 += 1
    
    ent3 = calculate_entropy(pi3, ni3, p, n)
    print("P:", pi3)
    print("N:", ni3)
    print("IG Normal:", calculate_information_gain(pi3, ni3))
    
    print(ent1, ent2, ent3)
    return round((ent1 + ent2 + ent3), 3)

def calculate_milk(df, p, n):
    pi1 = 0
    ni1 = 0
    for data in df.index:
        if(df['Milk'][data] == True and df['Drink_Coffee'][data] == "Yes"):
            pi1 += 1
        elif(df['Milk'][data] == True and df['Drink_Coffee'][data] == "No"):
            ni1 += 1
    
    ent1 = calculate_entropy(pi1, ni1, p, n)
    print("P:", pi1)
    print("N:", ni1)
    print("IG TRUE:", calculate_information_gain(pi1, ni1))

    pi2 = 0
    ni2 = 0
    for data in df.index:
        if(df['Milk'][data] == False and df['Drink_Coffee'][data] == "Yes"):
            pi2 += 1
        elif(df['Milk'][data] == False and df['Drink_Coffee'][data] == "No"):
            ni2 += 1
    
    ent2 = calculate_entropy(pi2, ni2, p, n)
    print("P:", pi2)
    print("N:", ni2)
    print("IG FALSE:", calculate_information_gain(pi2, ni2))

    print(ent1, ent2)
    return round((ent1 + ent2 ), 3)

def calculate_eaten(df, p, n):
    pi1 = 0
    ni1 = 0
    for data in df.index:
        if(df['Eaten'][data] == True and df['Drink_Coffee'][data] == "Yes"):
            pi1 += 1
        elif(df['Eaten'][data] == True and df['Drink_Coffee'][data] == "No"):
            ni1 += 1
    
    ent1 = calculate_entropy(pi1, ni1, p, n)
    print("P:", pi1)
    print("N:", ni1)
    print("IG TRUE:", calculate_information_gain(pi1, ni1))

    pi2 = 0
    ni2 = 0
    for data in df.index:
        if(df['Eaten'][data] == False and df['Drink_Coffee'][data] == "Yes"):
            pi2 += 1
        elif(df['Eaten'][data] == False and df['Drink_Coffee'][data] == "No"):
            ni2 += 1
    
    ent2 = calculate_entropy(pi2, ni2, p, n)
    print("P:", pi2)
    print("N:", ni2)
    print("IG FALSE:", calculate_information_gain(pi2, ni2))

    print(ent1, ent2)
    return round((ent1 + ent2), 3)

def main():
    
    df = pd.read_excel('coffee_data.xlsx')
    p = 0
    n = 0
    
    for data in df.index:
        if(df['Drink_Coffee'][data] == "Yes"):
            p += 1
        else:
            n += 1
    
    igp = calculate_information_gain(p, n)
    print("P:", p)
    print("N:", n)
    print("IG Parent:", igp)

    print("#########################")

    ed = calculate_daytime(df, p, n)
    print("Entropy Daytime:", ed)

    print("Gain Daytime:", round(igp - ed, 3))

    print("#########################")

    es = calculate_sugar(df, p, n)
    print("Entropy Sugar:", es)
    
    print("Gain Sugar:", round(igp - es, 3))

    print("#########################")

    em = calculate_milk(df, p, n)
    print("Entropy Milk:", em)
    
    print("Gain Milk:", round(igp - em, 3))

    print("#########################")

    ee = calculate_eaten(df, p, n)
    print("Entropy Eaten:", ee)
    
    print("Gain Eaten:", round(igp - ee, 3))

if __name__=="__main__":
	main()