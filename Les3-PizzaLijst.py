# opdracht 1.

# In deze oefening ga je een pizza maken. Dat ga je doen door een lijst met toppings te maken

# Stap 1 is zodoende:

# Maak een variabele `toppings` waarin je een lijst met strings als waarde zet. Zorg dat er minimaal 5 toppings/strings
# op je pizza zitten. Bijvoorbeeld een pizza met salami, kaas, tomaat, ananas en banaan

toppings = ['gorgonzola', 'champignons', 'tomaat', 'ansjovis', 'ui']

# opdracht 2

# We gaan nu op verschillende manieren onze pizza laten zien.
# - Laat zien wat jou eerste topping is
# - Laat zien wat jou derde topping is
# - Laat zien wat jou laatste topping is
# - Laat al je toppings zien.
# Het is natuurlijk de bedoeling dat je deze toppings niet zelf opschrijft, maar dat je ze uit de lijst haalt.

print (f'De eerste topping op mijn pizza is {toppings[0]}')
print (f'De derde topping op mijn pizza is {toppings[2]}')
print (f'De laatste topping op mijn pizza is {toppings[-1]}')
print (f'Mijn pizza bevat de volgende toppings: {toppings[0:]}')

# opdracht 3

# Gebruik `input` om de gebruiker van je applicatie te vragen welke topping ze nog meer zouden willen zien.
# Voeg deze deze topping vervolgens ook toe aan je `toppings` lijst.
# Welke lijst.methode() gebruik je ook al weer om iets toe te voegen aan de lijst?
# Tip: Zorg dat je de uitkomst van `input` opslaat in in variabele, anders kun je het niet gebruiken

extra_topping = input('Welke topping wil je er nog extra bij hebben?\n')
toppings.append(extra_topping)
print (f'Mijn pizza bevat nu de volgende toppings: {toppings} ')

# opdracht 4

# Nu een moeilijke opdracht. Gebruik nogmaals de `input` functie. Vraag ditmaal welke topping de gebruiker niet
# lekker vind. Probeer deze topping vervolgens te verwijderen uit je lijst.
# Welke lijst.methode() gebruik je ook alweer om iets te verwijderen uit een lijst?
# Let op, het kan ook een topping zijn die niet bestaat. Wat gebeurt er dan?

# Zorg er dus voor dat je een `if statement` gebruikt, met het `in` keyword, om te controleren
# of de opgegeven topping wel echt in de lijst staat. Alleen als dat zo is, dan kun je het
# verwijderen en print je de toppings weer om het te bewijzen.

# Als de gekozen topping niet in de lijst staat, print dan dat het niet in de lijst staat.

topping_verwijderen = input ('Welke topping vind je niet lekker?\n')

if topping_verwijderen in toppings:
    toppings.remove(topping_verwijderen)
    print(f'{topping_verwijderen} is verwijderd uit de lijst. De toppings zijn: {toppings}')
else:
    print(f'{topping_verwijderen} staat niet in de lijst. De toppings zijn: {toppings}')