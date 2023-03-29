# User Story: Das Programm zählt, wie viele Tomaten es in einer Liste gibt.
# maximale Anzahl Fehler: 1
gemuese = ["Gurke","Tomate","Zwiebel","Tomate","Gurke"]
print("Mein Gemüsekorb: ", gemuese)

zaehler = 0
for g in gemuese:
    if g is not "Tomate":
        zaehler += 1

print("Du hast ", zaehler, " Tomaten")
