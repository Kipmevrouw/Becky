#Doel: Programma in python waar iets te voorschijn

print("Hello you!, ik ben Becky")
print("Wie ben jij?")
naam = input("Typ je naam in:")

print("Hello " + naam )
print("--------------------------------------------------------------")
print("Ik ben een nieuwkomer op het Mediacollege Amsterdam")
print("Door een aantal vragen over mij te beandwoorden leer je mij beter kennen.")

print("--------------------------------------------------------------")

print("Voor ik naar het MBO op het Mediacollege Amsterdam kwam, zat ik op het")

print("A. Noorderlicht")
print("B. Had ik geen school")
print("C. Clusiuscollege")
antwoord = input("Kies A, B of C >>>>")
if(antwoord == "A"):
	print("Correct!")
elif(antwoord == "B"):
	print("Fout!")
elif(antwoord == "C"):
	print("Fout!")
print("--------------------------------------------------------------")
print("Hoe oud ben ik?")
print("A. 50")
print("B. 36")
print("C. 16")
antwoord = input("Kies A, B of C >>>>")
if(antwoord == "A"):
	print("Fout!")
elif(antwoord == "B"):
	print("Fout!")
elif(antwoord == "C"):
	print("Correct!")
print("--------------------------------------------------------------")
print("Heb ik huisdieren?")
print("A. Ja, een hond")
print("B. Ja, een hond en een hamster")
print("C. Ja, een kat")
antwoord = input("Kies A, B of C >>>>")
if(antwoord == "A"):
	print("Zou ik dan nog een ander dier hebben?")
	print("JA. ze heeft nog een hamster")
	print("NEE. ze heeft verder geen huisdieren")
	keuze = input("Typ je antwoord in:")
	if(keuze == "JA"):
		print("Ja, helemaal goed!")
	else:
		print("Dat is helaas onjuist")
elif(antwoord == "B"):
	print("Zou ik dan nog een ander dier hebben?")
	print("JA. ze heeft nog een kat")
	print("NEE. ze heeft verder geen huisdieren")
	keuze = input("Typ je antwoord in:")
	if(keuze == "JA"):
		print("Antwoord was onjuist maar ik heb wel 2 huisdieren.")
	else:
		print("Correct en tevens juist.")
elif(antwoord == "C"):
	print("Zou ik dan nog een ander dier hebben?")
	print("JA. ze heeft nog een hond")
	print("NEE. antwoord is onjuist ze heeft verder geen huisdieren")
	keuze = input("Typ je antwoord in:")
	if(keuze == "JA"):
		print("Onjuist ze heeft geen katten. Maar wel 1 hond en 1 hamster.")
	else:
		print("Onjuist ze heeft geen katten. Maar wel 1 hond en 1 hamster.")

print("Bedankt voor het beantwoorden van de vragen.")





