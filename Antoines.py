import math
A = {
    "Acetic acid": 16.8080,
    "Acetone": 16.6513,
    "Ammonia": 16.9481,
    "Benzene": 15.9008,
    "Carbon disulfide": 15.9844,
    "Carbon tetrachloride":  15.8742,
    "Chloroform": 15.9732,
    "Cyclohexane": 15.7527,
    "Ethyl acetate": 16.1516,
    "Ethyl alcohol": 18.5242,
    "Ethyl bromide": 15.9338,
    "n-Heptane": 15.8737,
    "n-Hexane": 15.8366,
    "Methyl alcohol": 18.5875,
    "n-Pentane": 15.8333,
    "Sulfur dioxide": 16.7680,
    "Toluene": 16.0137,
    "Water": 18.3036
}

B = {
    "Acetic acid":  3405.57,
    "Acetone": 2940.46,
    "Ammonia": 2132.50,
    "Benzene":  2788.51,
    "Carbon disulfide":  2690.85,
    "Carbon tetrachloride":  2808.19,
    "Chloroform":  2696.79,
    "Cyclohexane": 2766.63,
    "Ethyl acetate": 2790.50,
    "Ethyl alcohol": 3578.91,
    "Ethyl bromide": 2511.68,
    "n-Heptane": 2911.32,
    "n-Hexane": 2697.55,
    "Methyl alcohol": 3626.55,
    "n-Pentane": 2477.07,
    "Sulfur dioxide": 2302.35,
    "Toluene": 3096.52,
    "Water": 3816.44
}

C = {
    "Acetic acid": -56.34,
    "Acetone": -35.93,
    "Ammonia": -32.98,
    "Benzene": -52.36,
    "Carbon disulfide": -31.62,
    "Carbon tetrachloride": -45.99,
    "Chloroform": -46.16,
    "Cyclohexane": -50.50,
    "Ethyl acetate": -57.15,
    "Ethyl alcohol": -50.50,
    "Ethyl bromide": -41.44,
    "n-Heptane": -56.51,
    "n-Hexane": -48.78,
    "Methyl alcohol": -34.29,
    "n-Pentane": -39.94,
    "Sulfur dioxide": -35.97,
    "Toluene": -53.67,
    "Water": -46.13,
}

compound = str(input("What compound will be evaluated? "))
if compound in A:
    unknown = str(input("What do you want to solve for, pressure or temperature? "))
    if unknown == "pressure":
        t = input("What is the temperature in Kelvin? ")
        p = math.exp(A[compound] - (B[compound]/(C[compound] + float(t))))
        print("The vapor pressure of " + compound + " at temperature " + str(t) + "K is: " + str(p) + " mm Hg")
    elif unknown == "temperature":
        p = input("What is the pressure in mm Hg? ")
        t = (B[compound]/(A[compound] - (math.log(float(p))))) - C[compound]
        print("The temperature of " + compound + " at vapor pressure " + str(p) + " mm Hg is: " + str(t) + "K")
    else:
        print("Please enter \"pressure\" or \"temperature\" exactly as shown.")
else:
    print("Data for that compound is not currently stored in this program.")