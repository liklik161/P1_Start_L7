woordenboek = {
    'hond': 'dog',
    'kat': 'cat',
    'huis': 'house',
    'boom': 'tree',
    'auto': 'car'
}

te_zoeken_vertaling =input("voer een woord in voor de vertaling:")
if te_zoeken_vertaling in woordenboek:
    print(f"de vertaling van {te_zoeken_vertaling} is {woordenboek[te_zoeken_vertaling]}.")
else:
    print("daar is geen vertaling voor in het woordenboek")