# A PLN to CHF currency converter

def pln_to_chf_converter(pln):
    result_chf = pln * 0.23
    message = str(pln) + " PLN are " + str(result_chf) + " CHF."
    return message

plnString = input("Enter the amount of PLN to convert: ")
pln = float(plnString)

print(pln_to_chf_converter(pln))

if pln > 10000:
    print("It is some money!")

if pln >= 100000:
    print("This is A LOT of money!")
