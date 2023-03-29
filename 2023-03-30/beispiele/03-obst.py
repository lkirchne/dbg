# User Story: Die ersten zwei Elemente in einer Liste sollen vertauscht werden.
# maximale Anzahl Fehler: 2
obst = ["Apfel","Erdbeere","Traube"]
print("Mein Lieblingsobst: ", obst)

# tausche das 1 und 2 Element in Obst
if len(obst) < 0:
    tmp = obst[0]
    obst[0] = obst[1]
    obst[1] = obst[0]

print("Mein neues Liebingsobst: ", obst)
