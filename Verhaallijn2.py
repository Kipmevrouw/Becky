import os, sys, time

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Het is eindelijk weekend na dat je super lang gewerkt heb aan school.")
print("Je hoort ineens dat je moeder en vader zeggen dat je zondag naar de moskee moet met je familie,")
print("je kan dus niet 2 dagen lang bij je beste vriendin slapen waar je dus al maanden lang op zit te wachten.")
print("Je vind dat oneerlijk omdat je ouders al weken lang hebben verteld dat je naar je beste vriendin mag gaan.")

print("\nJe besluit om…")
print("A. …toch stiekem zaterdag te gaan naar je beste vriendin. 10")
print("B. …toch mee te gaan met je ouders en je familie. 6")
antwoord1 = input("Maak je keuze: ")
if antwoord1 == ("A") or ("a"):
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Je besluit toch stiekem te gaan zaterdag naar je beste vriendin.")
    print("Het is laat je besluit om naar bed te gaan.")
    print("Ze vertelt je dat ze dit weekend niet kan door redenen waar ze absoluut niet over mag praten van haar ouders.")
    print("Ze vraagt je of je morgen ochtend voor 7 uur in de ochtend in de speeltuin wilt komen.")

    print("\nJe vertelt haar…")
    print("A. …dat je dit weekend ook niet kon komen. 9")
    print("B. …dat er naar uit kijkt tot morgen! 4")
    antwoord2 = input("Maak je keuze: ")
    if antwoord2 == ("A") or ("a"):
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("En je vertelt haar dat je dit weekend ook niet kon komen. Je krijgt daar geen reactie op.")
        print("Je nog steeds niks binnen. Maar je hoort wel allemaal geritsel thuis.")
        print("Je ziet je moeder en vader heel veel dingen bij elkaar aan het zoeken zijn. Je vraagt wat er aan de hand is.")
        print("Ze zeggen dat je je moet opschieten en je nu per direct je spullen bij elkaar moet zoeken.")
        print("Was het al te laat dus voor al die spullen. Je moeder en vader nemen je rennend mee in de auto.")
        print("Op weg naar de grens. Je ouders worden net om de hoek aangehouden. De mensen die je ouders aanhouden vragen waar jullie heen gaan.")
        print("Je ouders zeggen; alsjeblieft neem mijn kind mee over grens wij blijven hier.")
        print("Alsjeblieft! Jij begint enorm te huilen je weet niet wat er aan de hand is.")
        print("De mensen trekken je uit de auto en nemen je mee.")

        print("\nJij kiest ervoor om..")
        print("A. Toch met je ouders te blijven en met hun mee te gaan. 12")
        print("B. Mee te gaan met die mensen. 11")
        antwoord3 = input("Maak je keuze: ")
        if antwoord3 == ("A") or ("a"):
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("Jij kiest ervoor om toch te blijven met je ouders. Maar je ouder dwingen je en ze helpen je eruit.")
            print("En je word mee genomen met die mensen. Ze vertellen je dat het gevaarlijk is hier en dat je je ouders willen beschermen.")
            print("Jij vraagt wat er aan de hand is.. De kennissen van je ouders dat zijn wij en mochten niet vertellen wat er aan de hand is maar.")
            print("Er brak gisteren oorlog uit in Syrië. En dit is de laatste keer dat je je ouders ooit nog gaat zien.")
            print("Je brak van binnen je wist niest meer je was er enorm stil van en je stond zo stijf dat je maar de auto in ging van de kennissen.")
            print("De kennissen vertelde dat je word gebracht naar de grens van Europa en daar wacht een ander groep op je.")
            print("Je rijdt naar de grens van Europa waar een boot staan die je naar Italië brengt. Dat ging allemaal goed tot dat de auto bij de grens kwam van Europa.")
            print("Je hoorde mensen praten *Je kan niet in Europa zonder een geldig paspoort*.Maar jij heb die niet.")

            print("\nDe groep kon daar beslissen om..")
            print("A. …5 maanden voor de grens te wachten tot dat je een bewijs krijgt dat je in dat land mag. 1")
            print("B. …gelijk met de boot weg alleen was dat enorm gevaarlijk. Er is namelijk een grote kans dat je het niet haalt. 13")
            antwoord4 = input("Maak je keuze: ")
            if antwoord4 == ("A") or ("a"):
                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("De groep kon daar beslissen om 5 maanden voor de grens te wachten tot dat je een bewijs krijgt dat je in dat land mag. De groep ging akkoord!")
                print("Na een lang tijd waren de 5 maanden voorbij. Ze hadden een vluchtelingen verblijf aangeboden hier in Europa.")
                print("Ze vroeg aan je of je daar wilde blijven.")

                print("\nEn jij besloot…")
                print("A. Verder met dit formulier te reizen naar Nederland. 2")
                print("B. Daar te blijven. 3")
                antwoord5 = input("Maak je keuze: ")
                if antwoord5 == ("A") or ("a"):
                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    print("Je moest enorm veel uren reizen vanaf hier naar Nederland.")
                    print("Je maakte voor jezelf een keuze of je niet eerst in Duitsland wilde verblijven of gelijk door naar Nederland,")
                    print("aangezien je had gehoord dat het super lastig is om in Nederland te blijven mogen leven.")

                    print("\nJe kiest ervoor om naar..")
                    print("A. Duitsland te gaan. 5")
                    print("B. Nederland te gaan. 8")
                    antwoord6 = input("Maak je keuze: ")
                    if antwoord6 == ("A") or ("a"):
                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        print("Eerst maar even naar Duitsland. Uren ging voorbij je komt bij de grens van Duitsland aan ze vragen om je paspoort.")
                        print("Je hebt geen geldig paspoort behalve dan de vluchtelingen formulier.")
                        print("In Duitsland is het zo dat je dan ook maanden moet gaan wacht voor dat je in dat land mag komen verblijven.")
                        print("Er gingen weer 5 maanden voorbij. Je kreeg toegang tot Duitsland je mocht er wonen. Je kreeg een verblijf aan geboden.")

                        print("\nMaar jij wilde kiezen tussen..")
                        print("A. De reis naar Nederland. 14")
                        print("B. Een verblijf in Duitsland. 7")
                        antwoord7 = input("Maak je keuze: ")
                        if antwoord7 == ("A") or ("a"):
                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            print("De reis naar Nederland is begonnen. Je laat alles achter in Duitsland. En neemt je koffertje mee.")
                            print("Na een paar dagen kom je aan in op bij de grens van Nederland je mag hier niet zomaar verblijven daar heb je een verblijfsvergunning voor nodig.")
                            print("En dat duurde langer dan je had verwacht maar je ontvangt een verblijf met allerlei andere mensen uit Syrië waarbij je kan overnachten tot dat het zo ver is.")
                            print("Maar toen je daar aan kwam voelde je als een pas geboren baby zonder moeder. Je kende de taal niet je kende helemaal niks hier.")
                            print(". Alleen maar de mensen die dezelfde taal spraken. Na 5 dagen in het verblijf te hebben gezeten kwam de ijs man toevallig..")

                            print("\nJe kon kiezen tussen de ijsjes..")
                            print("A. Chocolade ijs 15")
                            print("B. Aardbei ijs 15")
                            antwoord8 = input("Maak je keuze: ")
                            if antwoord8 == ("A") or ("a"):
                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print("Yammie lekker ijsje! Je hebt die al jaren niet meer gehad. Het proefden echt enorm lekker. Na zo een lange tijd.")
                                print("Na 5 maanden ontvangen jullie een verblijfsvergunning. Je mogen hier net zo lang blijven tot dat de oorlog voorbij is in jullie land.")

                                print("\nJe mag kiezen of je gebracht word naar het verblijf waar je mag blijven of dat je met de trein wilt…")
                                print("A. …met de trein 18")
                                print("B. …gebracht worden 19")
                                antwoord9 = input("Maak je keuze: ")
                                if antwoord9 == ("A") or ("a"):
                                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    print("Je neemt de trein naar je verblijf. Eindelijk! De plek waar je enorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                                    print("\n Je mag kiezen welke behang je doet in je kamer…")
                                    print("A. roze behang 21")
                                    print("B. blauw behang 21")
                                    antwoord10 = input("Maak je keuze: ")
                                    if antwoord10 == ("A") or ("a"):
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                        print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                        print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                        print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                        print("\n[Einde]")
                                        while True:
                                            while True:
                                                restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                if restart in ("1") or ("2"):
                                                    break
                                            if restart == "1":
                                                print("Laten we het verhaal opnieuw spelen")
                                                time.sleep(0.8)
                                                os.system("cls")
                                                time.sleep(1)
                                                os.system("py Verhaallijn.py")
                                            elif restart == "2":
                                                print("Oke, bedankt voor het spelen. Tot ziens!")
                                                time.sleep(0.6)
                                                os.system("taskkill /IM cmd.exe")
                                            else:
                                                print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                time.sleep(0.7)
                                                os.system("cls")
                                    else:
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                        print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                        print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                        print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                        print("\n[Einde]")
                                        while True:
                                            while True:
                                                restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                if restart in ("1") or ("2"):
                                                    break
                                            if restart == "1":
                                                print("Laten we het verhaal opnieuw spelen")
                                                time.sleep(0.8)
                                                os.system("cls")
                                                time.sleep(1)
                                                os.system("py Verhaallijn.py")
                                            elif restart == "2":
                                                print("Oke, bedankt voor het spelen. Tot ziens!")
                                                time.sleep(0.6)
                                                os.system("taskkill /IM cmd.exe")
                                            else:
                                                print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                time.sleep(0.7)
                                                os.system("cls")
                                else:
                                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    print("Je word gebracht. Eindelijk! De plek waarjeenorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                                    print("\nJe mag kiezen welke behang je doet in je kamer...")
                                    print("A. ...roze behang 21")
                                    print("B. ...blauw behang 21")
                                    antwoord88 = input("Maak je keuze: ")
                                    if antwoord88 == ("A") or ("a"):
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                        print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                        print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                        print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                        print("\n[Einde]")
                                        while True:
                                            while True:
                                                restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                if restart in ("1") or ("2"):
                                                    break
                                            if restart == "1":
                                                print("Laten we het verhaal opnieuw spelen")
                                                time.sleep(0.8)
                                                os.system("cls")
                                                time.sleep(1)
                                                os.system("py Verhaallijn.py")
                                            elif restart == "2":
                                                print("Oke, bedankt voor het spelen. Tot ziens!")
                                                time.sleep(0.6)
                                                os.system("taskkill /IM cmd.exe")
                                            else:
                                                print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                time.sleep(0.7)
                                                os.system("cls")
                                    else:
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                        print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                        print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                        print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                        print("\n[Einde]")
                                        while True:
                                            while True:
                                                restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                if restart in ("1") or ("2"):
                                                    break
                                            if restart == "1":
                                                print("Laten we het verhaal opnieuw spelen")
                                                time.sleep(0.8)
                                                os.system("cls")
                                                time.sleep(1)
                                                os.system("py Verhaallijn.py")
                                            elif restart == "2":
                                                print("Oke, bedankt voor het spelen. Tot ziens!")
                                                time.sleep(0.6)
                                                os.system("taskkill /IM cmd.exe")
                                            else:
                                                print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                time.sleep(0.7)
                                                os.system("cls")   
                        else:
                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            print("Het huisje in Duitsland. Je wilde eerst daar de taal kennen. Effe tot rust komen en dan later de reis te gemoed komen naar Nederland.")
                            print("Daar ging 2 jaar over heen.Je wilde weg hier je wilde naar Nederland.")

                            print("\nJe kon kiezen tussen..")
                            print("A. ...met de trein gaan. 14")
                            print("B. ...lopend naar Nederland want dat was niet zo ver. 14")
                            antwoord77 = input("Maak je keuze: ")
                            if antwoord77 == ("A") or ("a"): 
                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print("De reis naar Nederland is begonnen. Je laat alles achter in Duitsland. En neemt je koffertje mee.")
                                print("Na een paar dagen kom je aan in op bij de grens van Nederland je mag hier niet zomaar verblijven daar heb je een verblijfsvergunning voor nodig.")
                                print("En dat duurde langer dan je had verwacht maar je ontvangt een verblijf met allerlei andere mensen uit Syrië waarbij je kan overnachten tot dat het zo ver is.")
                                print("Maar toen je daar aan kwam voelde je als een pas geboren baby zonder moeder. Je kende de taal niet je kende helemaal niks hier.")
                                print(". Alleen maar de mensen die dezelfde taal spraken. Na 5 dagen in het verblijf te hebben gezeten kwam de ijs man toevallig..")

                                print("\nJe kon kiezen tussen de ijsjes..")
                                print("A. Chocolade ijs 15")
                                print("B. Aardbei ijs 15")
                                antwoord777 = input("Maak je keuze: ")
                                if antwoord777 == ("A") or ("a"):
                                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    print("Yammie lekker ijsje! Je hebt die al jaren niet meer gehad. Het proefden echt enorm lekker. Na zo een lange tijd.")
                                    print("Na 5 maanden ontvangen jullie een verblijfsvergunning. Je mogen hier net zo lang blijven tot dat de oorlog voorbij is in jullie land.")

                                    print("\nJe mag kiezen of je gebracht word naar het verblijf waar je mag blijven of dat je met de trein wilt…")
                                    print("A. …met de trein 18")
                                    print("B. …gebracht worden 19")
                                    antwoord7777 = input("Maak je keuze: ")
                                    if antwoord7777 == ("A") or ("a"):
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("Je neemt de trein naar je verblijf. Eindelijk! De plek waar je enorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                                        print("\n Je mag kiezen welke behang je doet in je kamer…")
                                        print("A. roze behang 21")
                                        print("B. blauw behang 21")
                                        antwoord77777 = input("Maak je keuze: ")
                                        if antwoord77777 == ("A") or ("a"):
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                            print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                            print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                            print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                            print("\n[Einde]")
                                            while True:
                                                while True:
                                                    restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                    if restart in ("1") or ("2"):
                                                        break
                                                if restart == "1":
                                                    print("Laten we het verhaal opnieuw spelen")
                                                    time.sleep(0.8)
                                                    os.system("cls")
                                                    time.sleep(1)
                                                    os.system("py Verhaallijn.py")
                                                elif restart == "2":
                                                    print("Oke, bedankt voor het spelen. Tot ziens!")
                                                    time.sleep(0.6)
                                                    os.system("taskkill /IM cmd.exe")
                                                else:
                                                    print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                    time.sleep(0.7)
                                                    os.system("cls")
                                        else:
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                            print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                            print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                            print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                            print("\n[Einde]")
                                            while True:
                                                while True:
                                                    restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                    if restart in ("1") or ("2"):
                                                        break
                                                if restart == "1":
                                                    print("Laten we het verhaal opnieuw spelen")
                                                    time.sleep(0.8)
                                                    os.system("cls")
                                                    time.sleep(1)
                                                    os.system("py Verhaallijn.py")
                                                elif restart == "2":
                                                    print("Oke, bedankt voor het spelen. Tot ziens!")
                                                    time.sleep(0.6)
                                                    os.system("taskkill /IM cmd.exe")
                                                else:
                                                    print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                    time.sleep(0.7)
                                                    os.system("cls")
                                    else:
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("Je word gebracht. Eindelijk! De plek waarjeenorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                                        print("\nJe mag kiezen welke behang je doet in je kamer...")
                                        print("A. ...roze behang 21")
                                        print("B. ...blauw behang 21")
                                        antwoord777777 = input("Maak je keuze: ")
                                        if antwoord777777 == ("A") or ("a"):
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                            print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                            print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                            print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                            print("\n[Einde]")
                                            while True:
                                                while True:
                                                    restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                    if restart in ("1") or ("2"):
                                                        break
                                                if restart == "1":
                                                    print("Laten we het verhaal opnieuw spelen")
                                                    time.sleep(0.8)
                                                    os.system("cls")
                                                    time.sleep(1)
                                                    os.system("py Verhaallijn.py")
                                                elif restart == "2":
                                                    print("Oke, bedankt voor het spelen. Tot ziens!")
                                                    time.sleep(0.6)
                                                    os.system("taskkill /IM cmd.exe")
                                                else:
                                                    print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                    time.sleep(0.7)
                                                    os.system("cls")
                                        else:
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                            print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                            print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                            print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                            print("\n[Einde]")
                                            while True:
                                                while True:
                                                    restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                    if restart in ("1") or ("2"):
                                                        break
                                                if restart == "1":
                                                    print("Laten we het verhaal opnieuw spelen")
                                                    time.sleep(0.8)
                                                    os.system("cls")
                                                    time.sleep(1)
                                                    os.system("py Verhaallijn.py")
                                                elif restart == "2":
                                                    print("Oke, bedankt voor het spelen. Tot ziens!")
                                                    time.sleep(0.6)
                                                    os.system("taskkill /IM cmd.exe")
                                                else:
                                                    print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                    time.sleep(0.7)
                                                    os.system("cls") 
                    else:
                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        print("Op naar Nederland!De reis is enorm lastig om vanaf hier‘Italië’naarNederland te gaan.Dagen gingen voorbij. Je komt aan na 5 dagen lopen in Zwitserlandaan.")
                        print("Je ontmoet iemand die alleen de kinderen willen mee nemen naar België en die persoon zoulater dan de volwassen meenemen als ze hier wachten op haar.")
                        print("Ze wilt namelijk graag de kinderen helpen en ze snel opweg nemen naar iets veiligs en ze wist iemand waar hunuit eindelijkkonden verblijven.")

                        print("\nJij kiest ervoor om...")
                        print("A. ...mee te gaan 16")
                        print("B. ...niet mee te gaan 17")
                        antwoord66 = input("Maak je keuze: ")
                        if antwoord66 == ("A") or ("a"):
                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            print("Je neemt de trein naar je verblijf. Eindelijk! De plek waar je enorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                            print("\n Je mag kiezen welke behang je doet in je kamer…")
                            print("A. roze behang 21")
                            print("B. blauw behang 21")
                            antwoord666 = input("Maak je keuze: ")
                            if antwoord666 == ("A") or ("a"):
                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                print("\n[Einde]")
                                while True:
                                    while True:
                                        restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                        if restart in ("1") or ("2"):
                                            break
                                        if restart == "1":
                                            print("Laten we het verhaal opnieuw spelen")
                                            time.sleep(0.8)
                                            os.system("cls")
                                            time.sleep(1)
                                            os.system("py Verhaallijn.py")
                                        elif restart == "2":
                                            print("Oke, bedankt voor het spelen. Tot ziens!")
                                            time.sleep(0.6)
                                            os.system("taskkill /IM cmd.exe")
                                        else:
                                            print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                            time.sleep(0.7)
                                            os.system("cls")
                            else:
                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                print("\n[Einde]")
                                while True:
                                    while True:
                                        restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                        if restart in ("1") or ("2"):
                                            break
                                        if restart == "1":
                                            print("Laten we het verhaal opnieuw spelen")
                                            time.sleep(0.8)
                                            os.system("cls")
                                            time.sleep(1)
                                            os.system("py Verhaallijn.py")
                                        elif restart == "2":
                                            print("Oke, bedankt voor het spelen. Tot ziens!")
                                            time.sleep(0.6)
                                            os.system("taskkill /IM cmd.exe")
                                        else:
                                            print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                            time.sleep(0.7)
                                            os.system("cls")
                        else:
                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            print("Je gaat niet mee met de vrouw en gaat met groep weg. Na 1 dag gezeten te hebben in Zwitserland.")
                            print("Komt er een politie naar jullie toe en die merkt zich op dat jullie hier illegaalzijn. En die neemt jullie allemaal mee naar de gevangenis")

                            print("\n[Einde]")
                            while True:
                                while True:
                                    restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                    if restart in ("1") or ("2"):
                                        break
                                    if restart == "1":
                                        print("Laten we het verhaal opnieuw spelen")
                                        time.sleep(0.8)
                                        os.system("cls")
                                        time.sleep(1)
                                        os.system("py Verhaallijn.py")
                                    elif restart == "2":
                                        print("Oke, bedankt voor het spelen. Tot ziens!")
                                        time.sleep(0.6)
                                        os.system("taskkill /IM cmd.exe")
                                    else:
                                        print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                        time.sleep(0.7)
                                        os.system("cls")
                else:
                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    print("Na3 maanden daar verbleven te hebben besluit je toch maar naar Nederland te gaan. Daar gingen veel uren aan voorbij")

                    print("\nMaar omdat je hoorde dat je moeilijk in Nederland te recht komt gaf je jezelf de keuzenaar welke land je eerst wilde gaan.")
                    print("A. ...Duitsland 5")
                    print("B. ...Nederland 8")
                    antwoord55 = input("Maak je keuze: ")
                    if antwoord55 == ("A") or ("a"):
                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        print("Eerst maar even naar Duitsland. Uren ging voorbij je komt bij de grens van Duitsland aan ze vragen om je paspoort.")
                        print("Je hebt geen geldig paspoort behalve dan de vluchtelingen formulier.")
                        print("In Duitsland is het zo dat je dan ook maanden moet gaan wacht voor dat je in dat land mag komen verblijven.")
                        print("Er gingen weer 5 maanden voorbij. Je kreeg toegang tot Duitsland je mocht er wonen. Je kreeg een verblijf aan geboden.")

                        print("\nMaar jij wilde kiezen tussen..")
                        print("A. De reis naar Nederland. 14")
                        print("B. Een verblijf in Duitsland. 7")
                        antwoord555 = input("Maak je keuze: ")
                        if antwoord555 == ("A") or ("a"):
                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            print("De reis naar Nederland is begonnen. Je laat alles achter in Duitsland. En neemt je koffertje mee.")
                            print("Na een paar dagen kom je aan in op bij de grens van Nederland je mag hier niet zomaar verblijven daar heb je een verblijfsvergunning voor nodig.")
                            print("En dat duurde langer dan je had verwacht maar je ontvangt een verblijf met allerlei andere mensen uit Syrië waarbij je kan overnachten tot dat het zo ver is.")
                            print("Maar toen je daar aan kwam voelde je als een pas geboren baby zonder moeder. Je kende de taal niet je kende helemaal niks hier.")
                            print(". Alleen maar de mensen die dezelfde taal spraken. Na 5 dagen in het verblijf te hebben gezeten kwam de ijs man toevallig..")

                            print("\nJe kon kiezen tussen de ijsjes..")
                            print("A. Chocolade ijs 15")
                            print("B. Aardbei ijs 15")
                            antwoord5555 = input("Maak je keuze: ")
                            if antwoord5555 == ("A") or ("a"):
                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print("Yammie lekker ijsje! Je hebt die al jaren niet meer gehad. Het proefden echt enorm lekker. Na zo een lange tijd.")
                                print("Na 5 maanden ontvangen jullie een verblijfsvergunning. Je mogen hier net zo lang blijven tot dat de oorlog voorbij is in jullie land.")

                                print("\nJe mag kiezen of je gebracht word naar het verblijf waar je mag blijven of dat je met de trein wilt…")
                                print("A. …met de trein 18")
                                print("B. …gebracht worden 19")
                                antwoord55555 = input("Maak je keuze: ")
                                if antwoord55555 == ("A") or ("a"):
                                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    print("Je neemt de trein naar je verblijf. Eindelijk! De plek waar je enorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                                    print("\n Je mag kiezen welke behang je doet in je kamer…")
                                    print("A. roze behang 21")
                                    print("B. blauw behang 21")
                                    antwoord555555 = input("Maak je keuze: ")
                                    if antwoord555555 == ("A") or ("a"):
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                        print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                        print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                        print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                        print("\n[Einde]")
                                        while True:
                                            while True:
                                                restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                if restart in ("1") or ("2"):
                                                    break
                                                if restart == "1":
                                                    print("Laten we het verhaal opnieuw spelen")
                                                    time.sleep(0.8)
                                                    os.system("cls")
                                                    time.sleep(1)
                                                    os.system("py Verhaallijn.py")
                                                elif restart == "2":
                                                    print("Oke, bedankt voor het spelen. Tot ziens!")
                                                    time.sleep(0.6)
                                                    os.system("taskkill /IM cmd.exe")
                                                else:
                                                    print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                    time.sleep(0.7)
                                                    os.system("cls")
                                    else:
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                        print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                        print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                        print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                        print("\n[Einde]")
                                        while True:
                                            while True:
                                                restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                if restart in ("1") or ("2"):
                                                    break
                                                if restart == "1":
                                                    print("Laten we het verhaal opnieuw spelen")
                                                    time.sleep(0.8)
                                                    os.system("cls")
                                                    time.sleep(1)
                                                    os.system("py Verhaallijn.py")
                                                elif restart == "2":
                                                    print("Oke, bedankt voor het spelen. Tot ziens!")
                                                    time.sleep(0.6)
                                                    os.system("taskkill /IM cmd.exe")
                                                else:
                                                    print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                    time.sleep(0.7)
                                                    os.system("cls")
                                else:
                                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    print("Je word gebracht. Eindelijk! De plek waarjeenorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                                    print("\nJe mag kiezen welke behang je doet in je kamer...")
                                    print("A. ...roze behang 21")
                                    print("B. ...blauw behang 21")
                                    antwoord555556 = input("Maak je keuze: ")
                                    if antwoord555556 == ("A") or ("a"):
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                        print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                        print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                        print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                        print("\n[Einde]")
                                        while True:
                                            while True:
                                                restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                if restart in ("1") or ("2"):
                                                    break
                                                if restart == "1":
                                                    print("Laten we het verhaal opnieuw spelen")
                                                    time.sleep(0.8)
                                                    os.system("cls")
                                                    time.sleep(1)
                                                    os.system("py Verhaallijn.py")
                                                elif restart == "2":
                                                    print("Oke, bedankt voor het spelen. Tot ziens!")
                                                    time.sleep(0.6)
                                                    os.system("taskkill /IM cmd.exe")
                                                else:
                                                    print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                    time.sleep(0.7)
                                                    os.system("cls")
                                    else:
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                        print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                        print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                        print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                        print("\n[Einde]")
                                        while True:
                                            while True:
                                                restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                if restart in ("1") or ("2"):
                                                    break
                                                if restart == "1":
                                                    print("Laten we het verhaal opnieuw spelen")
                                                    time.sleep(0.8)
                                                    os.system("cls")
                                                    time.sleep(1)
                                                    os.system("py Verhaallijn.py")
                                                elif restart == "2":
                                                    print("Oke, bedankt voor het spelen. Tot ziens!")
                                                    time.sleep(0.6)
                                                    os.system("taskkill /IM cmd.exe")
                                                else:
                                                    print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                    time.sleep(0.7)
                                                    os.system("cls")
                            else:
                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print("Yammie lekker ijsje! Je hebt die al jaren niet meer gehad. Het proefden echt enorm lekker. Na zo een lange tijd.")
                                print("Na 5 maanden ontvangen jullie een verblijfsvergunning. Je mogen hier net zo lang blijven tot dat de oorlog voorbij is in jullie land.")

                                print("\nJe mag kiezen of je gebracht word naar het verblijf waar je mag blijven of dat je met de trein wilt…")
                                print("A. …met de trein 18")
                                print("B. …gebracht worden 19")
                                antwoord5555566 = input("Maak je keuze: ")
                                if antwoord5555566 == ("A") or ("a"):
                                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    print("Je neemt de trein naar je verblijf. Eindelijk! De plek waar je enorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                                    print("\n Je mag kiezen welke behang je doet in je kamer…")
                                    print("A. roze behang 21")
                                    print("B. blauw behang 21")
                                    antwoord555555666 = input("Maak je keuze: ")
                                    if antwoord555555666 == ("A") or ("a"):
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                        print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                        print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                        print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                        print("\n[Einde]")
                                        while True:
                                            while True:
                                                restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                if restart in ("1") or ("2"):
                                                    break
                                                if restart == "1":
                                                    print("Laten we het verhaal opnieuw spelen")
                                                    time.sleep(0.8)
                                                    os.system("cls")
                                                    time.sleep(1)
                                                    os.system("py Verhaallijn.py")
                                                elif restart == "2":
                                                    print("Oke, bedankt voor het spelen. Tot ziens!")
                                                    time.sleep(0.6)
                                                    os.system("taskkill /IM cmd.exe")
                                                else:
                                                    print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                    time.sleep(0.7)
                                                    os.system("cls")
                                    else:
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                        print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                        print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                        print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                        print("\n[Einde]")
                                        while True:
                                            while True:
                                                restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                if restart in ("1") or ("2"):
                                                    break
                                                if restart == "1":
                                                    print("Laten we het verhaal opnieuw spelen")
                                                    time.sleep(0.8)
                                                    os.system("cls")
                                                    time.sleep(1)
                                                    os.system("py Verhaallijn.py")
                                                elif restart == "2":
                                                    print("Oke, bedankt voor het spelen. Tot ziens!")
                                                    time.sleep(0.6)
                                                    os.system("taskkill /IM cmd.exe")
                                                else:
                                                    print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                    time.sleep(0.7)
                                                    os.system("cls")
                                else:
                                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    print("Je word gebracht. Eindelijk! De plek waarjeenorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                                    print("\nJe mag kiezen welke behang je doet in je kamer...")
                                    print("A. ...roze behang 21")
                                    print("B. ...blauw behang 21")
                                    antwoord5555566 = input("Maak je keuze: ")
                                    if antwoord5555566 == ("A") or ("a"):
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                        print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                        print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                        print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                        print("\n[Einde]")
                                        while True:
                                            while True:
                                                restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                if restart in ("1") or ("2"):
                                                    break
                                                if restart == "1":
                                                    print("Laten we het verhaal opnieuw spelen")
                                                    time.sleep(0.8)
                                                    os.system("cls")
                                                    time.sleep(1)
                                                    os.system("py Verhaallijn.py")
                                                elif restart == "2":
                                                    print("Oke, bedankt voor het spelen. Tot ziens!")
                                                    time.sleep(0.6)
                                                    os.system("taskkill /IM cmd.exe")
                                                else:
                                                    print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                    time.sleep(0.7)
                                                    os.system("cls")
                                    else:
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                        print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                        print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                        print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                        print("\n[Einde]")
                                        while True:
                                            while True:
                                                restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                if restart in ("1") or ("2"):
                                                    break
                                                if restart == "1":
                                                    print("Laten we het verhaal opnieuw spelen")
                                                    time.sleep(0.8)
                                                    os.system("cls")
                                                    time.sleep(1)
                                                    os.system("py Verhaallijn.py")
                                                elif restart == "2":
                                                    print("Oke, bedankt voor het spelen. Tot ziens!")
                                                    time.sleep(0.6)
                                                    os.system("taskkill /IM cmd.exe")
                                                else:
                                                    print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                    time.sleep(0.7)
                                                    os.system("cls")
                        else:
                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            print("Het huisje in Duitsland. Je wilde eerst daar de taal kennen. Effe tot rust komen en dan later de reis te gemoed komen naar Nederland.")
                            print("Daar ging 2 jaar over heen.Je wilde weg hier je wilde naar Nederland.")

                            print("\nJe kon kiezen tussen..")
                            print("A. ...met de trein gaan. 14")
                            print("B. ...lopend naar Nederland want dat was niet zo ver. 14")
                            antwoordd5555 = input("Maak je keuze: ")
                            if antwoordd5555 == ("A") or ("a"):
                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print("De reis naar Nederland is begonnen. Je laat alles achter in Duitsland. En neemt je koffertje mee.")
                                print("Na een paar dagen kom je aan in op bij de grens van Nederland je mag hier niet zomaar verblijven daar heb je een verblijfsvergunning voor nodig.")
                                print("En dat duurde langer dan je had verwacht maar je ontvangt een verblijf met allerlei andere mensen uit Syrië waarbij je kan overnachten tot dat het zo ver is.")
                                print("Maar toen je daar aan kwam voelde je als een pas geboren baby zonder moeder. Je kende de taal niet je kende helemaal niks hier.")
                                print(". Alleen maar de mensen die dezelfde taal spraken. Na 5 dagen in het verblijf te hebben gezeten kwam de ijs man toevallig..")

                                print("\nJe kon kiezen tussen de ijsjes..")
                                print("A. Chocolade ijs 15")
                                print("B. Aardbei ijs 15")
                                anttwoordd5555 = input("Maak je keuze: ")
                                if anttwoordd5555 == ("A") or ("a"):
                                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    print("Yammie lekker ijsje! Je hebt die al jaren niet meer gehad. Het proefden echt enorm lekker. Na zo een lange tijd.")
                                    print("Na 5 maanden ontvangen jullie een verblijfsvergunning. Je mogen hier net zo lang blijven tot dat de oorlog voorbij is in jullie land.")

                                    print("\nJe mag kiezen of je gebracht word naar het verblijf waar je mag blijven of dat je met de trein wilt…")
                                    print("A. …met de trein 18")
                                    print("B. …gebracht worden 19")
                                    anttwoordd55555 = input("Maak je keuze: ")
                                    if anttwoordd55555 == ("A") or ("a"):
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("Je neemt de trein naar je verblijf. Eindelijk! De plek waar je enorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                                        print("\n Je mag kiezen welke behang je doet in je kamer…")
                                        print("A. roze behang 21")
                                        print("B. blauw behang 21")
                                        anttwoordd555555 = input("Maak je keuze: ")
                                        if anttwoordd555555 == ("A") or ("a"):
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                            print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                            print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                            print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                            print("\n[Einde]")
                                            while True:
                                                while True:
                                                    restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                    if restart in ("1") or ("2"):
                                                        break
                                                    if restart == "1":
                                                        print("Laten we het verhaal opnieuw spelen")
                                                        time.sleep(0.8)
                                                        os.system("cls")
                                                        time.sleep(1)
                                                        os.system("py Verhaallijn.py")
                                                    elif restart == "2":
                                                        print("Oke, bedankt voor het spelen. Tot ziens!")
                                                        time.sleep(0.6)
                                                        os.system("taskkill /IM cmd.exe")
                                                    else:
                                                        print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                        time.sleep(0.7)
                                                        os.system("cls")
                                        else:
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                            print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                            print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                            print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                            print("\n[Einde]")
                                            while True:
                                                while True:
                                                    restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                    if restart in ("1") or ("2"):
                                                        break
                                                    if restart == "1":
                                                        print("Laten we het verhaal opnieuw spelen")
                                                        time.sleep(0.8)
                                                        os.system("cls")
                                                        time.sleep(1)
                                                        os.system("py Verhaallijn.py")
                                                    elif restart == "2":
                                                        print("Oke, bedankt voor het spelen. Tot ziens!")
                                                        time.sleep(0.6)
                                                        os.system("taskkill /IM cmd.exe")
                                                    else:
                                                        print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                        time.sleep(0.7)
                                                        os.system("cls")
                                    else:
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("Je word gebracht. Eindelijk! De plek waarjeenorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                                        print("\nJe mag kiezen welke behang je doet in je kamer...")
                                        print("A. ...roze behang 21")
                                        print("B. ...blauw behang 21")
                                        anttwooordd55555 = input("Maak je keuze: ")
                                        if anttwooordd55555 == ("A") or ("a"):
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                            print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                            print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                            print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                            print("\n[Einde]")
                                            while True:
                                                while True:
                                                    restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                    if restart in ("1") or ("2"):
                                                        break
                                                    if restart == "1":
                                                        print("Laten we het verhaal opnieuw spelen")
                                                        time.sleep(0.8)
                                                        os.system("cls")
                                                        time.sleep(1)
                                                        os.system("py Verhaallijn.py")
                                                    elif restart == "2":
                                                        print("Oke, bedankt voor het spelen. Tot ziens!")
                                                        time.sleep(0.6)
                                                        os.system("taskkill /IM cmd.exe")
                                                    else:
                                                        print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                        time.sleep(0.7)
                                                        os.system("cls")                    
                                        else:
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                            print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                            print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                            print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                            print("\n[Einde]")
                                            while True:
                                                while True:
                                                    restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                    if restart in ("1") or ("2"):
                                                        break
                                                    if restart == "1":
                                                        print("Laten we het verhaal opnieuw spelen")
                                                        time.sleep(0.8)
                                                        os.system("cls")
                                                        time.sleep(1)
                                                        os.system("py Verhaallijn.py")
                                                    elif restart == "2":
                                                        print("Oke, bedankt voor het spelen. Tot ziens!")
                                                        time.sleep(0.6)
                                                        os.system("taskkill /IM cmd.exe")
                                                    else:
                                                        print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                        time.sleep(0.7)
                                                        os.system("cls")
                                else:
                                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    print("Yammie lekker ijsje! Je hebt die al jaren niet meer gehad. Het proefden echt enorm lekker. Na zo een lange tijd.")
                                    print("Na 5 maanden ontvangen jullie een verblijfsvergunning. Je mogen hier net zo lang blijven tot dat de oorlog voorbij is in jullie land.")

                                    print("\nJe mag kiezen of je gebracht word naar het verblijf waar je mag blijven of dat je met de trein wilt…")
                                    print("A. …met de trein 18")
                                    print("B. …gebracht worden 19")
                                    aanttwoordd55555 = input("Maak je keuze: ")
                                    if aanttwoordd55555 == ("A") or ("a"):
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("Je neemt de trein naar je verblijf. Eindelijk! De plek waar je enorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                                        print("\n Je mag kiezen welke behang je doet in je kamer…")
                                        print("A. roze behang 21")
                                        print("B. blauw behang 21")
                                        annttwoordd555555 = input("Maak je keuze: ")
                                        if annttwoordd555555 == ("A") or ("a"):
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                            print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                            print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                            print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                            print("\n[Einde]")
                                            while True:
                                                while True:
                                                    restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                    if restart in ("1") or ("2"):
                                                        break
                                                    if restart == "1":
                                                        print("Laten we het verhaal opnieuw spelen")
                                                        time.sleep(0.8)
                                                        os.system("cls")
                                                        time.sleep(1)
                                                        os.system("py Verhaallijn.py")
                                                    elif restart == "2":
                                                        print("Oke, bedankt voor het spelen. Tot ziens!")
                                                        time.sleep(0.6)
                                                        os.system("taskkill /IM cmd.exe")
                                                    else:
                                                        print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                        time.sleep(0.7)
                                                        os.system("cls")
                                        else:
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                            print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                            print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                            print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                            print("\n[Einde]")
                                            while True:
                                                while True:
                                                    restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                    if restart in ("1") or ("2"):
                                                        break
                                                    if restart == "1":
                                                        print("Laten we het verhaal opnieuw spelen")
                                                        time.sleep(0.8)
                                                        os.system("cls")
                                                        time.sleep(1)
                                                        os.system("py Verhaallijn.py")
                                                    elif restart == "2":
                                                        print("Oke, bedankt voor het spelen. Tot ziens!")
                                                        time.sleep(0.6)
                                                        os.system("taskkill /IM cmd.exe")
                                                    else:
                                                        print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                        time.sleep(0.7)
                                                        os.system("cls")
                                    else:
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("Je word gebracht. Eindelijk! De plek waarjeenorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                                        print("\nJe mag kiezen welke behang je doet in je kamer...")
                                        print("A. ...roze behang 21")
                                        print("B. ...blauw behang 21")
                                        anttwooorddd55555 = input("Maak je keuze: ")
                                        if anttwooorddd55555 == ("A") or ("a"):
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                            print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                            print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                            print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                            print("\n[Einde]")
                                            while True:
                                                while True:
                                                    restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                    if restart in ("1") or ("2"):
                                                        break
                                                    if restart == "1":
                                                        print("Laten we het verhaal opnieuw spelen")
                                                        time.sleep(0.8)
                                                        os.system("cls")
                                                        time.sleep(1)
                                                        os.system("py Verhaallijn.py")
                                                    elif restart == "2":
                                                        print("Oke, bedankt voor het spelen. Tot ziens!")
                                                        time.sleep(0.6)
                                                        os.system("taskkill /IM cmd.exe")
                                                    else:
                                                        print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                        time.sleep(0.7)
                                                        os.system("cls")                    
                                        else:
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                            print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                            print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                            print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                            print("\n[Einde]")
                                            while True:
                                                while True:
                                                    restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                    if restart in ("1") or ("2"):
                                                        break
                                                    if restart == "1":
                                                        print("Laten we het verhaal opnieuw spelen")
                                                        time.sleep(0.8)
                                                        os.system("cls")
                                                        time.sleep(1)
                                                        os.system("py Verhaallijn.py")
                                                    elif restart == "2":
                                                        print("Oke, bedankt voor het spelen. Tot ziens!")
                                                        time.sleep(0.6)
                                                        os.system("taskkill /IM cmd.exe")
                                                    else:
                                                        print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                        time.sleep(0.7)
                                                        os.system("cls")
                            else:
                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print("De reis naar Nederland is begonnen. Je laat alles achter in Duitsland. En neemt je koffertje mee.")
                                print("Na een paar dagen kom je aan in op bij de grens van Nederland je mag hier niet zomaar verblijven daar heb je een verblijfsvergunning voor nodig.")
                                print("En dat duurde langer dan je had verwacht maar je ontvangt een verblijf met allerlei andere mensen uit Syrië waarbij je kan overnachten tot dat het zo ver is.")
                                print("Maar toen je daar aan kwam voelde je als een pas geboren baby zonder moeder. Je kende de taal niet je kende helemaal niks hier.")
                                print(". Alleen maar de mensen die dezelfde taal spraken. Na 5 dagen in het verblijf te hebben gezeten kwam de ijs man toevallig..")

                                print("\nJe kon kiezen tussen de ijsjes..")
                                print("A. Chocolade ijs 15")
                                print("B. Aardbei ijs 15")
                                anttwooordd5555 = input("Maak je keuze: ")
                                if anttwooordd5555 == ("A") or ("a"):
                                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    print("Yammie lekker ijsje! Je hebt die al jaren niet meer gehad. Het proefden echt enorm lekker. Na zo een lange tijd.")
                                    print("Na 5 maanden ontvangen jullie een verblijfsvergunning. Je mogen hier net zo lang blijven tot dat de oorlog voorbij is in jullie land.")

                                    print("\nJe mag kiezen of je gebracht word naar het verblijf waar je mag blijven of dat je met de trein wilt…")
                                    print("A. …met de trein 18")
                                    print("B. …gebracht worden 19")
                                    anttwooorrdd55555 = input("Maak je keuze: ")
                                    if anttwooorrdd55555 == ("A") or ("a"):
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("Je neemt de trein naar je verblijf. Eindelijk! De plek waar je enorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                                        print("\n Je mag kiezen welke behang je doet in je kamer…")
                                        print("A. roze behang 21")
                                        print("B. blauw behang 21")
                                        anttwwoordd555555 = input("Maak je keuze: ")
                                        if anttwwoordd555555 == ("A") or ("a"):
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                            print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                            print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                            print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                            print("\n[Einde]")
                                            while True:
                                                while True:
                                                    restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                    if restart in ("1") or ("2"):
                                                        break
                                                    if restart == "1":
                                                        print("Laten we het verhaal opnieuw spelen")
                                                        time.sleep(0.8)
                                                        os.system("cls")
                                                        time.sleep(1)
                                                        os.system("py Verhaallijn.py")
                                                    elif restart == "2":
                                                        print("Oke, bedankt voor het spelen. Tot ziens!")
                                                        time.sleep(0.6)
                                                        os.system("taskkill /IM cmd.exe")
                                                    else:
                                                        print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                        time.sleep(0.7)
                                                        os.system("cls")
                                        else:
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                            print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                            print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                            print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                            print("\n[Einde]")
                                            while True:
                                                while True:
                                                    restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                    if restart in ("1") or ("2"):
                                                        break
                                                    if restart == "1":
                                                        print("Laten we het verhaal opnieuw spelen")
                                                        time.sleep(0.8)
                                                        os.system("cls")
                                                        time.sleep(1)
                                                        os.system("py Verhaallijn.py")
                                                    elif restart == "2":
                                                        print("Oke, bedankt voor het spelen. Tot ziens!")
                                                        time.sleep(0.6)
                                                        os.system("taskkill /IM cmd.exe")
                                                    else:
                                                        print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                        time.sleep(0.7)
                                                        os.system("cls")
                                    else:
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("Je word gebracht. Eindelijk! De plek waarjeenorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                                        print("\nJe mag kiezen welke behang je doet in je kamer...")
                                        print("A. ...roze behang 21")
                                        print("B. ...blauw behang 21")
                                        anttwoooordd55555 = input("Maak je keuze: ")
                                        if anttwoooordd55555 == ("A") or ("a"):
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                            print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                            print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                            print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                            print("\n[Einde]")
                                            while True:
                                                while True:
                                                    restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                    if restart in ("1") or ("2"):
                                                        break
                                                    if restart == "1":
                                                        print("Laten we het verhaal opnieuw spelen")
                                                        time.sleep(0.8)
                                                        os.system("cls")
                                                        time.sleep(1)
                                                        os.system("py Verhaallijn.py")
                                                    elif restart == "2":
                                                        print("Oke, bedankt voor het spelen. Tot ziens!")
                                                        time.sleep(0.6)
                                                        os.system("taskkill /IM cmd.exe")
                                                    else:
                                                        print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                        time.sleep(0.7)
                                                        os.system("cls")                    
                                        else:
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                            print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                            print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                            print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                            print("\n[Einde]")
                                            while True:
                                                while True:
                                                    restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                    if restart in ("1") or ("2"):
                                                        break
                                                    if restart == "1":
                                                        print("Laten we het verhaal opnieuw spelen")
                                                        time.sleep(0.8)
                                                        os.system("cls")
                                                        time.sleep(1)
                                                        os.system("py Verhaallijn.py")
                                                    elif restart == "2":
                                                        print("Oke, bedankt voor het spelen. Tot ziens!")
                                                        time.sleep(0.6)
                                                        os.system("taskkill /IM cmd.exe")
                                                    else:
                                                        print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                        time.sleep(0.7)
                                                        os.system("cls")
                                else:
                                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    print("Yammie lekker ijsje! Je hebt die al jaren niet meer gehad. Het proefden echt enorm lekker. Na zo een lange tijd.")
                                    print("Na 5 maanden ontvangen jullie een verblijfsvergunning. Je mogen hier net zo lang blijven tot dat de oorlog voorbij is in jullie land.")

                                    print("\nJe mag kiezen of je gebracht word naar het verblijf waar je mag blijven of dat je met de trein wilt…")
                                    print("A. …met de trein 18")
                                    print("B. …gebracht worden 19")
                                    aanttwoordd557555 = input("Maak je keuze: ")
                                    if aanttwoordd557555 == ("A") or ("a"):
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("Je neemt de trein naar je verblijf. Eindelijk! De plek waar je enorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                                        print("\n Je mag kiezen welke behang je doet in je kamer…")
                                        print("A. roze behang 21")
                                        print("B. blauw behang 21")
                                        annttwoordd5585555 = input("Maak je keuze: ")
                                        if annttwoordd5585555 == ("A") or ("a"):
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                            print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                            print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                            print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                            print("\n[Einde]")
                                            while True:
                                                while True:
                                                    restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                    if restart in ("1") or ("2"):
                                                        break
                                                    if restart == "1":
                                                        print("Laten we het verhaal opnieuw spelen")
                                                        time.sleep(0.8)
                                                        os.system("cls")
                                                        time.sleep(1)
                                                        os.system("py Verhaallijn.py")
                                                    elif restart == "2":
                                                        print("Oke, bedankt voor het spelen. Tot ziens!")
                                                        time.sleep(0.6)
                                                        os.system("taskkill /IM cmd.exe")
                                                    else:
                                                        print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                        time.sleep(0.7)
                                                        os.system("cls")
                                        else:
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                            print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                            print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                            print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                            print("\n[Einde]")
                                            while True:
                                                while True:
                                                    restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                    if restart in ("1") or ("2"):
                                                        break
                                                    if restart == "1":
                                                        print("Laten we het verhaal opnieuw spelen")
                                                        time.sleep(0.8)
                                                        os.system("cls")
                                                        time.sleep(1)
                                                        os.system("py Verhaallijn.py")
                                                    elif restart == "2":
                                                        print("Oke, bedankt voor het spelen. Tot ziens!")
                                                        time.sleep(0.6)
                                                        os.system("taskkill /IM cmd.exe")
                                                    else:
                                                        print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                        time.sleep(0.7)
                                                        os.system("cls")
                                    else:
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("Je word gebracht. Eindelijk! De plek waarjeenorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                                        print("\nJe mag kiezen welke behang je doet in je kamer...")
                                        print("A. ...roze behang 21")
                                        print("B. ...blauw behang 21")
                                        anttwooorddd555550 = input("Maak je keuze: ")
                                        if anttwooorddd555550 == ("A") or ("a"):
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                            print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                            print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                            print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                            print("\n[Einde]")
                                            while True:
                                                while True:
                                                    restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                    if restart in ("1") or ("2"):
                                                        break
                                                    if restart == "1":
                                                        print("Laten we het verhaal opnieuw spelen")
                                                        time.sleep(0.8)
                                                        os.system("cls")
                                                        time.sleep(1)
                                                        os.system("py Verhaallijn.py")
                                                    elif restart == "2":
                                                        print("Oke, bedankt voor het spelen. Tot ziens!")
                                                        time.sleep(0.6)
                                                        os.system("taskkill /IM cmd.exe")
                                                    else:
                                                        print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                        time.sleep(0.7)
                                                        os.system("cls")                    
                                        else:
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                            print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                            print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                            print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                            print("\n[Einde]")
                                            while True:
                                                while True:
                                                    restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                    if restart in ("1") or ("2"):
                                                        break
                                                    if restart == "1":
                                                        print("Laten we het verhaal opnieuw spelen")
                                                        time.sleep(0.8)
                                                        os.system("cls")
                                                        time.sleep(1)
                                                        os.system("py Verhaallijn.py")
                                                    elif restart == "2":
                                                        print("Oke, bedankt voor het spelen. Tot ziens!")
                                                        time.sleep(0.6)
                                                        os.system("taskkill /IM cmd.exe")
                                                    else:
                                                        print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                        time.sleep(0.7)
                                                        os.system("cls")
                    else:
                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        print("Op naar Nederland!De reis is enorm lastig om vanaf hier‘Italië’naarNederland te gaan.Dagen gingen voorbij. Je komt aan na 5 dagen lopen in Zwitserlandaan.")
                        print("Je ontmoet iemand die alleen de kinderen willen mee nemen naar België en die persoon zoulater dan de volwassen meenemen als ze hier wachten op haar.")
                        print("Ze wilt namelijk graag de kinderen helpen en ze snel opweg nemen naar iets veiligs en ze wist iemand waar hunuit eindelijkkonden verblijven.")

                        print("\nJij kiest ervoor om...")
                        print("A. ...mee te gaan 16")
                        print("B. ...niet mee te gaan 17")
                        aantwoord55 = input("Maak je keuze: ")
                        if aantwoord55 == ("A") or ("a"):
                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            print("Je neemt de trein naar je verblijf. Eindelijk! De plek waar je enorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                            print("\n Je mag kiezen welke behang je doet in je kamer…")
                            print("A. roze behang 21")
                            print("B. blauw behang 21")
                            aaantwoord55 = input("Maak je keuze: ")
                            if aaantwoord55 == ("A") or ("a"):
                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                print("\n[Einde]")
                                while True:
                                    while True:
                                        restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                        if restart in ("1") or ("2"):
                                            break
                                        if restart == "1":
                                            print("Laten we het verhaal opnieuw spelen")
                                            time.sleep(0.8)
                                            os.system("cls")
                                            time.sleep(1)
                                            os.system("py Verhaallijn.py")
                                        elif restart == "2":
                                            print("Oke, bedankt voor het spelen. Tot ziens!")
                                            time.sleep(0.6)
                                            os.system("taskkill /IM cmd.exe")
                                        else:
                                            print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                            time.sleep(0.7)
                                            os.system("cls")  
                            else:
                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                print("\n[Einde]")
                                while True:
                                    while True:
                                        restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                        if restart in ("1") or ("2"):
                                            break
                                        if restart == "1":
                                            print("Laten we het verhaal opnieuw spelen")
                                            time.sleep(0.8)
                                            os.system("cls")
                                            time.sleep(1)
                                            os.system("py Verhaallijn.py")
                                        elif restart == "2":
                                            print("Oke, bedankt voor het spelen. Tot ziens!")
                                            time.sleep(0.6)
                                            os.system("taskkill /IM cmd.exe")
                                        else:
                                            print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                            time.sleep(0.7)
                                            os.system("cls")
                        else:
                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            print("Je gaat niet mee met de vrouw en gaat met groep weg. Na 1 dag gezeten te hebben in Zwitserland.")
                            print("Komt er een politie naar jullie toe en die merkt zich op dat jullie hier illegaalzijn. En die neemt jullie allemaal mee naar de gevangenis")

                            print("\n[Einde]")
                            while True:
                                while True:
                                    restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                    if restart in ("1") or ("2"):
                                        break
                                    if restart == "1":
                                        print("Laten we het verhaal opnieuw spelen")
                                        time.sleep(0.8)
                                        os.system("cls")
                                        time.sleep(1)
                                        os.system("py Verhaallijn.py")
                                    elif restart == "2":
                                        print("Oke, bedankt voor het spelen. Tot ziens!")
                                        time.sleep(0.6)
                                        os.system("taskkill /IM cmd.exe")
                                    else:
                                        print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                        time.sleep(0.7)
                                        os.system("cls") 
            else:
                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("Je gaat niet mee met de vrouw en gaat met groep weg. Na 1 dag gezeten te hebben in Zwitserland.")
                print("Komt er een politie naar jullie toe en die merkt zich op dat jullie hier illegaalzijn. En die neemt jullie allemaal mee naar de gevangenis")

                print("\n[Einde]")
                while True:
                    while True:
                        restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                        if restart in ("1") or ("2"):
                            break
                        if restart == "1":
                            print("Laten we het verhaal opnieuw spelen")
                            time.sleep(0.8)
                            os.system("cls")
                            time.sleep(1)
                            os.system("py Verhaallijn.py")
                        elif restart == "2":
                            print("Oke, bedankt voor het spelen. Tot ziens!")
                            time.sleep(0.6)
                            os.system("taskkill /IM cmd.exe")
                        else:
                            print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                            time.sleep(0.7)
                            os.system("cls")   
        else:
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("Je kiest ervoor om toch mee te gaan met die mensen. En je ouders liet je achter.")
            print("De mensen die je meenamen waren kennissen van je ouders vertelde ze je en die zorgde ervoor dat jij veilig weg zou komen hier uit Syrië.")
            print("En ze vertelde je dat de oorlog uitbrak. En dat het voor jou niet veilig was en je ouders wilde dat jij een goede toekomst zou hebben.")
            print("De kennissen vertelde dat je zo direct met een auto word mee genomen. En dat je vanaf daar met een grote groep mensen met de boot naar Italië zou varen.")
            print("Het was op dat moment te veel voor je dat je het effe niet meer kon plaatsen wat er gebeurden en je ging maar mee in de auto. Onder weg naar de boot naar Italië.")
            print("Dat ging allemaal goed tot dat de auto bij de grens kwam van Europa. Je hoorde mensen praten *Je kan niet in Europa zonder een geldig paspoort*.Maar jij heb die niet.")

            print("\nDe groep kon daar beslissen om..")
            print("A. …5 maanden voor de grens te wachten tot dat je een bewijs krijgt dat je in dat land mag. 1")
            print("B. …gelijk met de boot weg alleen was dat enorm gevaarlijk. Er is namelijk een grote kans dat je het niet haalt. 13")
            antwoord33 = input("Maak je keuze: ")
            if antwoord33 == ("A") or ("a"):
                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("De groep kon daar beslissen om 5 maanden voor de grens te wachten tot dat je een bewijs krijgt dat je in dat land mag. De groep ging akkoord!")
                print("Na een lang tijd waren de 5 maanden voorbij. Ze hadden een vluchtelingen verblijf aangeboden hier in Europa.")
                print("Ze vroeg aan je of je daar wilde blijven.")

                print("\nEn jij besloot…")
                print("A. Verder met dit formulier te reizen naar Nederland. 2")
                print("B. Daar te blijven. 3")
                antwoord333 = input("Maak je keuze: ")
                if antwoord333 == ("A") or ("a"):
                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    print("Je moest enorm veel uren reizen vanaf hier naar Nederland.")
                    print("Je maakte voor jezelf een keuze of je niet eerst in Duitsland wilde verblijven of gelijk door naar Nederland,")
                    print("aangezien je had gehoord dat het super lastig is om in Nederland te blijven mogen leven.")

                    print("\nJe kiest ervoor om naar..")
                    print("A. Duitsland te gaan. 5")
                    print("B. Nederland te gaan. 8")
                    antwoord3333 = input("Maak je keuze: ")
                    if antwoord3333 == ("A") or ("a"):
                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        print("Eerst maar even naar Duitsland. Uren ging voorbij je komt bij de grens van Duitsland aan ze vragen om je paspoort.")
                        print("Je hebt geen geldig paspoort behalve dan de vluchtelingen formulier.")
                        print("In Duitsland is het zo dat je dan ook maanden moet gaan wacht voor dat je in dat land mag komen verblijven.")
                        print("Er gingen weer 5 maanden voorbij. Je kreeg toegang tot Duitsland je mocht er wonen. Je kreeg een verblijf aan geboden.")

                        print("\nMaar jij wilde kiezen tussen..")
                        print("A. De reis naar Nederland. 14")
                        print("B. Een verblijf in Duitsland. 7")
                        antwoord33333 = input("Maak je keuze: ")
                        if antwoord33333 == ("A") or ("a"):
                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            print("De reis naar Nederland is begonnen. Je laat alles achter in Duitsland. En neemt je koffertje mee.")
                            print("Na een paar dagen kom je aan in op bij de grens van Nederland je mag hier niet zomaar verblijven daar heb je een verblijfsvergunning voor nodig.")
                            print("En dat duurde langer dan je had verwacht maar je ontvangt een verblijf met allerlei andere mensen uit Syrië waarbij je kan overnachten tot dat het zo ver is.")
                            print("Maar toen je daar aan kwam voelde je als een pas geboren baby zonder moeder. Je kende de taal niet je kende helemaal niks hier.")
                            print(". Alleen maar de mensen die dezelfde taal spraken. Na 5 dagen in het verblijf te hebben gezeten kwam de ijs man toevallig..")

                            print("\nJe kon kiezen tussen de ijsjes..")
                            print("A. Chocolade ijs 15")
                            print("B. Aardbei ijs 15")
                            antwoord333333 = input("Maak je keuze: ")
                            if antwoord333333 == ("A") or ("a"):
                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print("Yammie lekker ijsje! Je hebt die al jaren niet meer gehad. Het proefden echt enorm lekker. Na zo een lange tijd.")
                                print("Na 5 maanden ontvangen jullie een verblijfsvergunning. Je mogen hier net zo lang blijven tot dat de oorlog voorbij is in jullie land.")

                                print("\nJe mag kiezen of je gebracht word naar het verblijf waar je mag blijven of dat je met de trein wilt…")
                                print("A. …met de trein 18")
                                print("B. …gebracht worden 19")
                                antwoord333333 = input("Maak je keuze: ")
                                if antwoord333333 == ("A") or ("a"):
                                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    print("Je neemt de trein naar je verblijf. Eindelijk! De plek waar je enorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                                    print("\n Je mag kiezen welke behang je doet in je kamer…")
                                    print("A. roze behang 21")
                                    print("B. blauw behang 21")
                                    antwoord3333333 = input("Maak je keuze: ")
                                    if antwoord3333333 == ("A") or ("a"):
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                        print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                        print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                        print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                        print("\n[Einde]")
                                        while True:
                                            while True:
                                                restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                if restart in ("1") or ("2"):
                                                    break
                                                if restart == "1":
                                                    print("Laten we het verhaal opnieuw spelen")
                                                    time.sleep(0.8)
                                                    os.system("cls")
                                                    time.sleep(1)
                                                    os.system("py Verhaallijn.py")
                                                elif restart == "2":
                                                    print("Oke, bedankt voor het spelen. Tot ziens!")
                                                    time.sleep(0.6)
                                                    os.system("taskkill /IM cmd.exe")
                                                else:
                                                    print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                    time.sleep(0.7)
                                                    os.system("cls")
                                            QR1 = input("Maak je keuze: ")
                                    else:
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                        print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                        print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                        print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                        print("\n[Einde]")
                                        while True:
                                            while True:
                                                restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                if restart in ("1") or ("2"):
                                                    break
                                                if restart == "1":
                                                    print("Laten we het verhaal opnieuw spelen")
                                                    time.sleep(0.8)
                                                    os.system("cls")
                                                    time.sleep(1)
                                                    os.system("py Verhaallijn.py")
                                                elif restart == "2":
                                                    print("Oke, bedankt voor het spelen. Tot ziens!")
                                                    time.sleep(0.6)
                                                    os.system("taskkill /IM cmd.exe")
                                                else:
                                                    print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                    time.sleep(0.7)
                                                    os.system("cls")
                                            QR1 = input("Maak je keuze: ") 
                                else:
                                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    print("Je word gebracht. Eindelijk! De plek waarjeenorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                                    print("\nJe mag kiezen welke behang je doet in je kamer...")
                                    print("A. ...roze behang 21")
                                    print("B. ...blauw behang 21")
                                    antwoord33333333 = input("Maak je keuze: ")
                                    if antwoord33333333 == ("A") or ("a"):
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                        print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                        print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                        print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                        print("\n[Einde]")
                                        while True:
                                            while True:
                                                restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                if restart in ("1") or ("2"):
                                                    break
                                                if restart == "1":
                                                    print("Laten we het verhaal opnieuw spelen")
                                                    time.sleep(0.8)
                                                    os.system("cls")
                                                    time.sleep(1)
                                                    os.system("py Verhaallijn.py")
                                                elif restart == "2":
                                                    print("Oke, bedankt voor het spelen. Tot ziens!")
                                                    time.sleep(0.6)
                                                    os.system("taskkill /IM cmd.exe")
                                                else:
                                                    print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                    time.sleep(0.7)
                                                    os.system("cls")
                                            QR1 = input("Maak je keuze: ")
                                    else:
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                        print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                        print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                        print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                        print("\n[Einde]")
                                        while True:
                                            while True:
                                                restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                if restart in ("1") or ("2"):
                                                    break
                                                if restart == "1":
                                                    print("Laten we het verhaal opnieuw spelen")
                                                    time.sleep(0.8)
                                                    os.system("cls")
                                                    time.sleep(1)
                                                    os.system("py Verhaallijn.py")
                                                elif restart == "2":
                                                    print("Oke, bedankt voor het spelen. Tot ziens!")
                                                    time.sleep(0.6)
                                                    os.system("taskkill /IM cmd.exe")
                                                else:
                                                    print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                    time.sleep(0.7)
                                                    os.system("cls")
                                            QR1 = input("Maak je keuze: ")
                            else:
                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print("Yammie lekker ijsje! Je hebt die al jaren niet meer gehad. Het proefden echt enorm lekker. Na zo een lange tijd.")
                                print("Na 5 maanden ontvangen jullie een verblijfsvergunning. Je mogen hier net zo lang blijven tot dat de oorlog voorbij is in jullie land.")

                                print("\nJe mag kiezen of je gebracht word naar het verblijf waar je mag blijven of dat je met de trein wilt…")
                                print("A. …met de trein 18")
                                print("B. …gebracht worden 19")
                                antwoordd333333 = input("Maak je keuze: ")
                                if antwoordd333333 == ("A") or ("a"):
                                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    print("Je neemt de trein naar je verblijf. Eindelijk! De plek waar je enorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                                    print("\n Je mag kiezen welke behang je doet in je kamer…")
                                    print("A. roze behang 21")
                                    print("B. blauw behang 21")
                                    antwooordd3333333 = input("Maak je keuze: ")
                                    if antwooordd3333333 == ("A") or ("a"):
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                        print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                        print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                        print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                        print("\n[Einde]")
                                        while True:
                                            while True:
                                                restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                if restart in ("1") or ("2"):
                                                    break
                                                if restart == "1":
                                                    print("Laten we het verhaal opnieuw spelen")
                                                    time.sleep(0.8)
                                                    os.system("cls")
                                                    time.sleep(1)
                                                    os.system("py Verhaallijn.py")
                                                elif restart == "2":
                                                    print("Oke, bedankt voor het spelen. Tot ziens!")
                                                    time.sleep(0.6)
                                                    os.system("taskkill /IM cmd.exe")
                                                else:
                                                    print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                    time.sleep(0.7)
                                                    os.system("cls")
                                            QR1 = input("Maak je keuze: ")
                                    else:
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                        print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                        print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                        print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                        print("\n[Einde]")
                                        while True:
                                            while True:
                                                restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                if restart in ("1") or ("2"):
                                                    break
                                                if restart == "1":
                                                    print("Laten we het verhaal opnieuw spelen")
                                                    time.sleep(0.8)
                                                    os.system("cls")
                                                    time.sleep(1)
                                                    os.system("py Verhaallijn.py")
                                                elif restart == "2":
                                                    print("Oke, bedankt voor het spelen. Tot ziens!")
                                                    time.sleep(0.6)
                                                    os.system("taskkill /IM cmd.exe")
                                                else:
                                                    print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                    time.sleep(0.7)
                                                    os.system("cls")
                                            QR1 = input("Maak je keuze: ") 
                                else:
                                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    print("Je word gebracht. Eindelijk! De plek waarjeenorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                                    print("\nJe mag kiezen welke behang je doet in je kamer...")
                                    print("A. ...roze behang 21")
                                    print("B. ...blauw behang 21")
                                    antwoord333333334 = input("Maak je keuze: ")
                                    if antwoord333333334 == ("A") or ("a"):
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                        print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                        print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                        print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                        print("\n[Einde]")
                                        while True:
                                            while True:
                                                restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                if restart in ("1") or ("2"):
                                                    break
                                                if restart == "1":
                                                    print("Laten we het verhaal opnieuw spelen")
                                                    time.sleep(0.8)
                                                    os.system("cls")
                                                    time.sleep(1)
                                                    os.system("py Verhaallijn.py")
                                                elif restart == "2":
                                                    print("Oke, bedankt voor het spelen. Tot ziens!")
                                                    time.sleep(0.6)
                                                    os.system("taskkill /IM cmd.exe")
                                                else:
                                                    print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                    time.sleep(0.7)
                                                    os.system("cls")
                                            QR1 = input("Maak je keuze: ")
                                    else:
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                        print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                        print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                        print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                        print("\n[Einde]")
                                        while True:
                                            while True:
                                                restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                if restart in ("1") or ("2"):
                                                    break
                                                if restart == "1":
                                                    print("Laten we het verhaal opnieuw spelen")
                                                    time.sleep(0.8)
                                                    os.system("cls")
                                                    time.sleep(1)
                                                    os.system("py Verhaallijn.py")
                                                elif restart == "2":
                                                    print("Oke, bedankt voor het spelen. Tot ziens!")
                                                    time.sleep(0.6)
                                                    os.system("taskkill /IM cmd.exe")
                                                else:
                                                    print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                    time.sleep(0.7)
                                                    os.system("cls")
                        else:
                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            print("Het huisje in Duitsland. Je wilde eerst daar de taal kennen. Effe tot rust komen en dan later de reis te gemoed komen naar Nederland.")
                            print("Daar ging 2 jaar over heen.Je wilde weg hier je wilde naar Nederland.")

                            print("\nJe kon kiezen tussen..")
                            print("A. ...met de trein gaan. 14")
                            print("B. ...lopend naar Nederland want dat was niet zo ver. 14")
                            antwoord333330 = input("Maak je keuze: ")
                            if antwoord333330 == ("A") or ("a"):
                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print("De reis naar Nederland is begonnen. Je laat alles achter in Duitsland. En neemt je koffertje mee.")
                                print("Na een paar dagen kom je aan in op bij de grens van Nederland je mag hier niet zomaar verblijven daar heb je een verblijfsvergunning voor nodig.")
                                print("En dat duurde langer dan je had verwacht maar je ontvangt een verblijf met allerlei andere mensen uit Syrië waarbij je kan overnachten tot dat het zo ver is.")
                                print("Maar toen je daar aan kwam voelde je als een pas geboren baby zonder moeder. Je kende de taal niet je kende helemaal niks hier.")
                                print(". Alleen maar de mensen die dezelfde taal spraken. Na 5 dagen in het verblijf te hebben gezeten kwam de ijs man toevallig..")

                                print("\nJe kon kiezen tussen de ijsjes..")
                                print("A. Chocolade ijs 15")
                                print("B. Aardbei ijs 15")   
                                antwoord3333300 = input("Maak je keuze: ")
                                if antwoord3333300 == ("A") or ("a"): 
                                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    print("Yammie lekker ijsje! Je hebt die al jaren niet meer gehad. Het proefden echt enorm lekker. Na zo een lange tijd.")
                                    print("Na 5 maanden ontvangen jullie een verblijfsvergunning. Je mogen hier net zo lang blijven tot dat de oorlog voorbij is in jullie land.")

                                    print("\nJe mag kiezen of je gebracht word naar het verblijf waar je mag blijven of dat je met de trein wilt…")
                                    print("A. …met de trein 18")
                                    print("B. …gebracht worden 19") 
                                    antwoord33333300 = input("Maak je keuze: ")
                                    if antwoord33333300 == ("A") or ("a"):
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("Je neemt de trein naar je verblijf. Eindelijk! De plek waar je enorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                                        print("\n Je mag kiezen welke behang je doet in je kamer…")
                                        print("A. roze behang 21")
                                        print("B. blauw behang 21") 
                                        antwoord333333800 = input("Maak je keuze: ")
                                        if antwoord333333800 == ("A") or ("a"): 
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                            print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                            print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                            print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                            print("\n[Einde]")
                                            while True:
                                                while True:
                                                    restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                    if restart in ("1") or ("2"):
                                                        break
                                                    if restart == "1":
                                                        print("Laten we het verhaal opnieuw spelen")
                                                        time.sleep(0.8)
                                                        os.system("cls")
                                                        time.sleep(1)
                                                        os.system("py Verhaallijn.py")
                                                    elif restart == "2":
                                                        print("Oke, bedankt voor het spelen. Tot ziens!")
                                                        time.sleep(0.6)
                                                        os.system("taskkill /IM cmd.exe")
                                                    else:
                                                        print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                        time.sleep(0.7)
                                                        os.system("cls") 
                                        else:
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                            print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                            print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                            print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                            print("\n[Einde]")
                                            while True:
                                                while True:
                                                    restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                    if restart in ("1") or ("2"):
                                                        break
                                                    if restart == "1":
                                                        print("Laten we het verhaal opnieuw spelen")
                                                        time.sleep(0.8)
                                                        os.system("cls")
                                                        time.sleep(1)
                                                        os.system("py Verhaallijn.py")
                                                    elif restart == "2":
                                                        print("Oke, bedankt voor het spelen. Tot ziens!")
                                                        time.sleep(0.6)
                                                        os.system("taskkill /IM cmd.exe")
                                                    else:
                                                        print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                        time.sleep(0.7)
                                                        os.system("cls")
                                    else:
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("Je word gebracht. Eindelijk! De plek waarjeenorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                                        print("\nJe mag kiezen welke behang je doet in je kamer...")
                                        print("A. ...roze behang 21")
                                        print("B. ...blauw behang 21") 
                                        antwoord3343333800 = input("Maak je keuze: ")
                                        if antwoord3343333800 == ("A") or ("a"): 
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                            print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                            print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                            print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                            print("\n[Einde]")
                                            while True:
                                                while True:
                                                    restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                    if restart in ("1") or ("2"):
                                                        break
                                                    if restart == "1":
                                                        print("Laten we het verhaal opnieuw spelen")
                                                        time.sleep(0.8)
                                                        os.system("cls")
                                                        time.sleep(1)
                                                        os.system("py Verhaallijn.py")
                                                    elif restart == "2":
                                                        print("Oke, bedankt voor het spelen. Tot ziens!")
                                                        time.sleep(0.6)
                                                        os.system("taskkill /IM cmd.exe")
                                                    else:
                                                        print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                        time.sleep(0.7)
                                                        os.system("cls") 
                                        else:
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                            print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                            print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                            print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                            print("\n[Einde]")
                                            while True:
                                                while True:
                                                    restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                    if restart in ("1") or ("2"):
                                                        break
                                                    if restart == "1":
                                                        print("Laten we het verhaal opnieuw spelen")
                                                        time.sleep(0.8)
                                                        os.system("cls")
                                                        time.sleep(1)
                                                        os.system("py Verhaallijn.py")
                                                    elif restart == "2":
                                                        print("Oke, bedankt voor het spelen. Tot ziens!")
                                                        time.sleep(0.6)
                                                        os.system("taskkill /IM cmd.exe")
                                                    else:
                                                        print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                        time.sleep(0.7)
                                                        os.system("cls")
                                else:
                                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    print("Yammie lekker ijsje! Je hebt die al jaren niet meer gehad. Het proefden echt enorm lekker. Na zo een lange tijd.")
                                    print("Na 5 maanden ontvangen jullie een verblijfsvergunning. Je mogen hier net zo lang blijven tot dat de oorlog voorbij is in jullie land.")

                                    print("\nJe mag kiezen of je gebracht word naar het verblijf waar je mag blijven of dat je met de trein wilt…")
                                    print("A. …met de trein 18")
                                    print("B. …gebracht worden 19") 
                                    antwoord3333443300 = input("Maak je keuze: ")
                                    if antwoord3333443300 == ("A") or ("a"):
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("Je neemt de trein naar je verblijf. Eindelijk! De plek waar je enorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                                        print("\n Je mag kiezen welke behang je doet in je kamer…")
                                        print("A. roze behang 21")
                                        print("B. blauw behang 21") 
                                        antwoord3353333800 = input("Maak je keuze: ")
                                        if antwoord3353333800 == ("A") or ("a"): 
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                            print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                            print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                            print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                            print("\n[Einde]")
                                            while True:
                                                while True:
                                                    restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                    if restart in ("1") or ("2"):
                                                        break
                                                    if restart == "1":
                                                        print("Laten we het verhaal opnieuw spelen")
                                                        time.sleep(0.8)
                                                        os.system("cls")
                                                        time.sleep(1)
                                                        os.system("py Verhaallijn.py")
                                                    elif restart == "2":
                                                        print("Oke, bedankt voor het spelen. Tot ziens!")
                                                        time.sleep(0.6)
                                                        os.system("taskkill /IM cmd.exe")
                                                    else:
                                                        print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                        time.sleep(0.7)
                                                        os.system("cls") 
                                        else:
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                            print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                            print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                            print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                            print("\n[Einde]")
                                            while True:
                                                while True:
                                                    restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                    if restart in ("1") or ("2"):
                                                        break
                                                    if restart == "1":
                                                        print("Laten we het verhaal opnieuw spelen")
                                                        time.sleep(0.8)
                                                        os.system("cls")
                                                        time.sleep(1)
                                                        os.system("py Verhaallijn.py")
                                                    elif restart == "2":
                                                        print("Oke, bedankt voor het spelen. Tot ziens!")
                                                        time.sleep(0.6)
                                                        os.system("taskkill /IM cmd.exe")
                                                    else:
                                                        print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                        time.sleep(0.7)
                                                        os.system("cls")
                                    else:
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("Je word gebracht. Eindelijk! De plek waarjeenorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                                        print("\nJe mag kiezen welke behang je doet in je kamer...")
                                        print("A. ...roze behang 21")
                                        print("B. ...blauw behang 21") 
                                        antwoord33433338005 = input("Maak je keuze: ")
                                        if antwoord33433338005 == ("A") or ("a"): 
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                            print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                            print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                            print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                            print("\n[Einde]")
                                            while True:
                                                while True:
                                                    restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                    if restart in ("1") or ("2"):
                                                        break
                                                    if restart == "1":
                                                        print("Laten we het verhaal opnieuw spelen")
                                                        time.sleep(0.8)
                                                        os.system("cls")
                                                        time.sleep(1)
                                                        os.system("py Verhaallijn.py")
                                                    elif restart == "2":
                                                        print("Oke, bedankt voor het spelen. Tot ziens!")
                                                        time.sleep(0.6)
                                                        os.system("taskkill /IM cmd.exe")
                                                    else:
                                                        print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                        time.sleep(0.7)
                                                        os.system("cls") 
                                        else:
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                            print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                            print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                            print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                            print("\n[Einde]")
                                            while True:
                                                while True:
                                                    restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                    if restart in ("1") or ("2"):
                                                        break
                                                    if restart == "1":
                                                        print("Laten we het verhaal opnieuw spelen")
                                                        time.sleep(0.8)
                                                        os.system("cls")
                                                        time.sleep(1)
                                                        os.system("py Verhaallijn.py")
                                                    elif restart == "2":
                                                        print("Oke, bedankt voor het spelen. Tot ziens!")
                                                        time.sleep(0.6)
                                                        os.system("taskkill /IM cmd.exe")
                                                    else:
                                                        print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                        time.sleep(0.7)
                                                        os.system("cls")
                            else:
                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print("De reis naar Nederland is begonnen. Je laat alles achter in Duitsland. En neemt je koffertje mee.")
                                print("Na een paar dagen kom je aan in op bij de grens van Nederland je mag hier niet zomaar verblijven daar heb je een verblijfsvergunning voor nodig.")
                                print("En dat duurde langer dan je had verwacht maar je ontvangt een verblijf met allerlei andere mensen uit Syrië waarbij je kan overnachten tot dat het zo ver is.")
                                print("Maar toen je daar aan kwam voelde je als een pas geboren baby zonder moeder. Je kende de taal niet je kende helemaal niks hier.")
                                print(". Alleen maar de mensen die dezelfde taal spraken. Na 5 dagen in het verblijf te hebben gezeten kwam de ijs man toevallig..")

                                print("\nJe kon kiezen tussen de ijsjes..")
                                print("A. Chocolade ijs 15")
                                print("B. Aardbei ijs 15")   
                                antwoord333330099 = input("Maak je keuze: ")
                                if antwoord333330099 == ("A") or ("a"): 
                                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    print("Yammie lekker ijsje! Je hebt die al jaren niet meer gehad. Het proefden echt enorm lekker. Na zo een lange tijd.")
                                    print("Na 5 maanden ontvangen jullie een verblijfsvergunning. Je mogen hier net zo lang blijven tot dat de oorlog voorbij is in jullie land.")

                                    print("\nJe mag kiezen of je gebracht word naar het verblijf waar je mag blijven of dat je met de trein wilt…")
                                    print("A. …met de trein 18")
                                    print("B. …gebracht worden 19") 
                                    antwoord33333300990 = input("Maak je keuze: ")
                                    if antwoord33333300990 == ("A") or ("a"):
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("Je neemt de trein naar je verblijf. Eindelijk! De plek waar je enorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                                        print("\n Je mag kiezen welke behang je doet in je kamer…")
                                        print("A. roze behang 21")
                                        print("B. blauw behang 21") 
                                        antwoord3333338090 = input("Maak je keuze: ")
                                        if antwoord3333338090 == ("A") or ("a"): 
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                            print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                            print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                            print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                            print("\n[Einde]")
                                            while True:
                                                while True:
                                                    restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                    if restart in ("1") or ("2"):
                                                        break
                                                    if restart == "1":
                                                        print("Laten we het verhaal opnieuw spelen")
                                                        time.sleep(0.8)
                                                        os.system("cls")
                                                        time.sleep(1)
                                                        os.system("py Verhaallijn.py")
                                                    elif restart == "2":
                                                        print("Oke, bedankt voor het spelen. Tot ziens!")
                                                        time.sleep(0.6)
                                                        os.system("taskkill /IM cmd.exe")
                                                    else:
                                                        print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                        time.sleep(0.7)
                                                        os.system("cls") 
                                        else:
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                            print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                            print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                            print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                            print("\n[Einde]")
                                            while True:
                                                while True:
                                                    restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                    if restart in ("1") or ("2"):
                                                        break
                                                    if restart == "1":
                                                        print("Laten we het verhaal opnieuw spelen")
                                                        time.sleep(0.8)
                                                        os.system("cls")
                                                        time.sleep(1)
                                                        os.system("py Verhaallijn.py")
                                                    elif restart == "2":
                                                        print("Oke, bedankt voor het spelen. Tot ziens!")
                                                        time.sleep(0.6)
                                                        os.system("taskkill /IM cmd.exe")
                                                    else:
                                                        print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                        time.sleep(0.7)
                                                        os.system("cls")
                                    else:
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("Je word gebracht. Eindelijk! De plek waarjeenorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                                        print("\nJe mag kiezen welke behang je doet in je kamer...")
                                        print("A. ...roze behang 21")
                                        print("B. ...blauw behang 21") 
                                        antwoord33433373800 = input("Maak je keuze: ")
                                        if antwoord33433373800 == ("A") or ("a"): 
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                            print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                            print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                            print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                            print("\n[Einde]")
                                            while True:
                                                while True:
                                                    restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                    if restart in ("1") or ("2"):
                                                        break
                                                    if restart == "1":
                                                        print("Laten we het verhaal opnieuw spelen")
                                                        time.sleep(0.8)
                                                        os.system("cls")
                                                        time.sleep(1)
                                                        os.system("py Verhaallijn.py")
                                                    elif restart == "2":
                                                        print("Oke, bedankt voor het spelen. Tot ziens!")
                                                        time.sleep(0.6)
                                                        os.system("taskkill /IM cmd.exe")
                                                    else:
                                                        print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                        time.sleep(0.7)
                                                        os.system("cls") 
                                        else:
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                            print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                            print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                            print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                            print("\n[Einde]")
                                            while True:
                                                while True:
                                                    restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                    if restart in ("1") or ("2"):
                                                        break
                                                    if restart == "1":
                                                        print("Laten we het verhaal opnieuw spelen")
                                                        time.sleep(0.8)
                                                        os.system("cls")
                                                        time.sleep(1)
                                                        os.system("py Verhaallijn.py")
                                                    elif restart == "2":
                                                        print("Oke, bedankt voor het spelen. Tot ziens!")
                                                        time.sleep(0.6)
                                                        os.system("taskkill /IM cmd.exe")
                                                    else:
                                                        print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                        time.sleep(0.7)
                                                        os.system("cls")
                                else:
                                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    print("Yammie lekker ijsje! Je hebt die al jaren niet meer gehad. Het proefden echt enorm lekker. Na zo een lange tijd.")
                                    print("Na 5 maanden ontvangen jullie een verblijfsvergunning. Je mogen hier net zo lang blijven tot dat de oorlog voorbij is in jullie land.")

                                    print("\nJe mag kiezen of je gebracht word naar het verblijf waar je mag blijven of dat je met de trein wilt…")
                                    print("A. …met de trein 18")
                                    print("B. …gebracht worden 19") 
                                    antwoord33334433010 = input("Maak je keuze: ")
                                    if antwoord33334433010 == ("A") or ("a"):
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("Je neemt de trein naar je verblijf. Eindelijk! De plek waar je enorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                                        print("\n Je mag kiezen welke behang je doet in je kamer…")
                                        print("A. roze behang 21")
                                        print("B. blauw behang 21") 
                                        antwoord335333380110 = input("Maak je keuze: ")
                                        if antwoord335333380110 == ("A") or ("a"): 
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                            print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                            print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                            print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                            print("\n[Einde]")
                                            while True:
                                                while True:
                                                    restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                    if restart in ("1") or ("2"):
                                                        break
                                                    if restart == "1":
                                                        print("Laten we het verhaal opnieuw spelen")
                                                        time.sleep(0.8)
                                                        os.system("cls")
                                                        time.sleep(1)
                                                        os.system("py Verhaallijn.py")
                                                    elif restart == "2":
                                                        print("Oke, bedankt voor het spelen. Tot ziens!")
                                                        time.sleep(0.6)
                                                        os.system("taskkill /IM cmd.exe")
                                                    else:
                                                        print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                        time.sleep(0.7)
                                                        os.system("cls") 
                                        else:
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                            print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                            print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                            print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                            print("\n[Einde]")
                                            while True:
                                                while True:
                                                    restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                    if restart in ("1") or ("2"):
                                                        break
                                                    if restart == "1":
                                                        print("Laten we het verhaal opnieuw spelen")
                                                        time.sleep(0.8)
                                                        os.system("cls")
                                                        time.sleep(1)
                                                        os.system("py Verhaallijn.py")
                                                    elif restart == "2":
                                                        print("Oke, bedankt voor het spelen. Tot ziens!")
                                                        time.sleep(0.6)
                                                        os.system("taskkill /IM cmd.exe")
                                                    else:
                                                        print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                        time.sleep(0.7)
                                                        os.system("cls")
                                    else:
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("Je word gebracht. Eindelijk! De plek waarjeenorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                                        print("\nJe mag kiezen welke behang je doet in je kamer...")
                                        print("A. ...roze behang 21")
                                        print("B. ...blauw behang 21") 
                                        antwoord334333380051 = input("Maak je keuze: ")
                                        if antwoord334333380051 == ("A") or ("a"): 
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                            print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                            print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                            print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                            print("\n[Einde]")
                                            while True:
                                                while True:
                                                    restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                    if restart in ("1") or ("2"):
                                                        break
                                                    if restart == "1":
                                                        print("Laten we het verhaal opnieuw spelen")
                                                        time.sleep(0.8)
                                                        os.system("cls")
                                                        time.sleep(1)
                                                        os.system("py Verhaallijn.py")
                                                    elif restart == "2":
                                                        print("Oke, bedankt voor het spelen. Tot ziens!")
                                                        time.sleep(0.6)
                                                        os.system("taskkill /IM cmd.exe")
                                                    else:
                                                        print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                        time.sleep(0.7)
                                                        os.system("cls") 
                                        else:
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                            print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                            print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                            print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                            print("\n[Einde]")
                                            while True:
                                                while True:
                                                    restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                    if restart in ("1") or ("2"):
                                                        break
                                                    if restart == "1":
                                                        print("Laten we het verhaal opnieuw spelen")
                                                        time.sleep(0.8)
                                                        os.system("cls")
                                                        time.sleep(1)
                                                        os.system("py Verhaallijn.py")
                                                    elif restart == "2":
                                                        print("Oke, bedankt voor het spelen. Tot ziens!")
                                                        time.sleep(0.6)
                                                        os.system("taskkill /IM cmd.exe")
                                                    else:
                                                        print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                        time.sleep(0.7)
                                                        os.system("cls")
                    else:
                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        print("Op naar Nederland!De reis is enorm lastig om vanaf hier‘Italië’naarNederland te gaan.Dagen gingen voorbij. Je komt aan na 5 dagen lopen in Zwitserlandaan.")
                        print("Je ontmoet iemand die alleen de kinderen willen mee nemen naar België en die persoon zoulater dan de volwassen meenemen als ze hier wachten op haar.")
                        print("Ze wilt namelijk graag de kinderen helpen en ze snel opweg nemen naar iets veiligs en ze wist iemand waar hunuit eindelijkkonden verblijven.")

                        print("\nJij kiest ervoor om...")
                        print("A. ...mee te gaan 16")
                        print("B. ...niet mee te gaan 17") 
                        antwoord3333m = input("Maak je keuze: ")
                        if antwoord3333m == ("A") or ("a"):
                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            print("Je neemt de trein naar je verblijf. Eindelijk! De plek waar je enorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                            print("\n Je mag kiezen welke behang je doet in je kamer…")
                            print("A. roze behang 21")
                            print("B. blauw behang 21")
                            antwoord3333m1 = input("Maak je keuze: ")
                            if antwoord3333m1 == ("A") or ("a"):
                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                print("\n[Einde]")
                                while True:
                                    while True:
                                        restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                        if restart in ("1") or ("2"):
                                            break
                                        if restart == "1":
                                            print("Laten we het verhaal opnieuw spelen")
                                            time.sleep(0.8)
                                            os.system("cls")
                                            time.sleep(1)
                                            os.system("py Verhaallijn.py")
                                        elif restart == "2":
                                            print("Oke, bedankt voor het spelen. Tot ziens!")
                                            time.sleep(0.6)
                                            os.system("taskkill /IM cmd.exe")
                                        else:
                                            print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                            time.sleep(0.7)
                                            os.system("cls") 
                            else:
                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                print("\n[Einde]")
                                while True:
                                    while True:
                                        restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                        if restart in ("1") or ("2"):
                                            break
                                        if restart == "1":
                                            print("Laten we het verhaal opnieuw spelen")
                                            time.sleep(0.8)
                                            os.system("cls")
                                            time.sleep(1)
                                            os.system("py Verhaallijn.py")
                                        elif restart == "2":
                                            print("Oke, bedankt voor het spelen. Tot ziens!")
                                            time.sleep(0.6)
                                            os.system("taskkill /IM cmd.exe")
                                        else:
                                            print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                            time.sleep(0.7)
                                            os.system("cls")    
                        else:
                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            print("Je gaat niet mee met de vrouw en gaat met groep weg. Na 1 dag gezeten te hebben in Zwitserland.")
                            print("Komt er een politie naar jullie toe en die merkt zich op dat jullie hier illegaalzijn. En die neemt jullie allemaal mee naar de gevangenis")

                            print("\n[Einde]")
                            while True:
                                while True:
                                    restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                    if restart in ("1") or ("2"):
                                        break
                                    if restart == "1":
                                        print("Laten we het verhaal opnieuw spelen")
                                        time.sleep(0.8)
                                        os.system("cls")
                                        time.sleep(1)
                                        os.system("py Verhaallijn.py")
                                    elif restart == "2":
                                        print("Oke, bedankt voor het spelen. Tot ziens!")
                                        time.sleep(0.6)
                                        os.system("taskkill /IM cmd.exe")
                                    else:
                                        print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                        time.sleep(0.7)
                                        os.system("cls")     
                else:
                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    print("Na3 maanden daar verbleven te hebben besluit je toch maar naar Nederland te gaan. Daar gingen veel uren aan voorbij")

                    print("\nMaar omdat je hoorde dat je moeilijk in Nederland te recht komt gaf je jezelf de keuzenaar welke land je eerst wilde gaan.")
                    print("A. ...Duitsland 5")
                    print("B. ...Nederland 8")
                    antwoord333m = input("Maak je keuze: ")
                    if antwoord333m == ("A") or ("a"):
                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        print("Eerst maar even naar Duitsland. Uren ging voorbij je komt bij de grens van Duitsland aan ze vragen om je paspoort.")
                        print("Je hebt geen geldig paspoort behalve dan de vluchtelingen formulier.")
                        print("In Duitsland is het zo dat je dan ook maanden moet gaan wacht voor dat je in dat land mag komen verblijven.")
                        print("Er gingen weer 5 maanden voorbij. Je kreeg toegang tot Duitsland je mocht er wonen. Je kreeg een verblijf aan geboden.")

                        print("\nMaar jij wilde kiezen tussen..")
                        print("A. De reis naar Nederland. 14")
                        print("B. Een verblijf in Duitsland. 7")
                        antwoord333mm = input("Maak je keuze: ")
                        if antwoord333mm == ("A") or ("a"): 
                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            print("De reis naar Nederland is begonnen. Je laat alles achter in Duitsland. En neemt je koffertje mee.")
                            print("Na een paar dagen kom je aan in op bij de grens van Nederland je mag hier niet zomaar verblijven daar heb je een verblijfsvergunning voor nodig.")
                            print("En dat duurde langer dan je had verwacht maar je ontvangt een verblijf met allerlei andere mensen uit Syrië waarbij je kan overnachten tot dat het zo ver is.")
                            print("Maar toen je daar aan kwam voelde je als een pas geboren baby zonder moeder. Je kende de taal niet je kende helemaal niks hier.")
                            print(". Alleen maar de mensen die dezelfde taal spraken. Na 5 dagen in het verblijf te hebben gezeten kwam de ijs man toevallig..")

                            print("\nJe kon kiezen tussen de ijsjes..")
                            print("A. Chocolade ijs 15")
                            print("B. Aardbei ijs 15")
                            antwoord333m8 = input("Maak je keuze: ")
                            if antwoord333m8 == ("A") or ("a"):
                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print("Yammie lekker ijsje! Je hebt die al jaren niet meer gehad. Het proefden echt enorm lekker. Na zo een lange tijd.")
                                print("Na 5 maanden ontvangen jullie een verblijfsvergunning. Je mogen hier net zo lang blijven tot dat de oorlog voorbij is in jullie land.")

                                print("\nJe mag kiezen of je gebracht word naar het verblijf waar je mag blijven of dat je met de trein wilt…")
                                print("A. …met de trein 18")
                                print("B. …gebracht worden 19")
                                antwoord333m8m = input("Maak je keuze: ")
                                if antwoord333m8m == ("A") or ("a"):
                                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    print("Je neemt de trein naar je verblijf. Eindelijk! De plek waar je enorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                                    print("\n Je mag kiezen welke behang je doet in je kamer…")
                                    print("A. roze behang 21")
                                    print("B. blauw behang 21")
                                    antwoord333m8mm = input("Maak je keuze: ")
                                    if antwoord333m8mm == ("A") or ("a"): 
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                        print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                        print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                        print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                        print("\n[Einde]")
                                        while True:
                                            while True:
                                                restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                if restart in ("1") or ("2"):
                                                    break
                                                if restart == "1":
                                                    print("Laten we het verhaal opnieuw spelen")
                                                    time.sleep(0.8)
                                                    os.system("cls")
                                                    time.sleep(1)
                                                    os.system("py Verhaallijn.py")
                                                elif restart == "2":
                                                    print("Oke, bedankt voor het spelen. Tot ziens!")
                                                    time.sleep(0.6)
                                                    os.system("taskkill /IM cmd.exe")
                                                else:
                                                    print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                    time.sleep(0.7)
                                                    os.system("cls") 
                                    else:
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                        print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                        print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                        print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                        print("\n[Einde]")
                                        while True:
                                            while True:
                                                restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                if restart in ("1") or ("2"):
                                                    break
                                                if restart == "1":
                                                    print("Laten we het verhaal opnieuw spelen")
                                                    time.sleep(0.8)
                                                    os.system("cls")
                                                    time.sleep(1)
                                                    os.system("py Verhaallijn.py")
                                                elif restart == "2":
                                                    print("Oke, bedankt voor het spelen. Tot ziens!")
                                                    time.sleep(0.6)
                                                    os.system("taskkill /IM cmd.exe")
                                                else:
                                                    print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                    time.sleep(0.7)
                                                    os.system("cls")
                                else:
                                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    print("Je word gebracht. Eindelijk! De plek waarjeenorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                                    print("\nJe mag kiezen welke behang je doet in je kamer...")
                                    print("A. ...roze behang 21")
                                    print("B. ...blauw behang 21")
                                    antwoord333m8mmz = input("Maak je keuze: ")
                                    if antwoord333m8mmz == ("A") or ("a"):
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                        print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                        print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                        print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                        print("\n[Einde]")
                                        while True:
                                            while True:
                                                restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                if restart in ("1") or ("2"):
                                                    break
                                                if restart == "1":
                                                    print("Laten we het verhaal opnieuw spelen")
                                                    time.sleep(0.8)
                                                    os.system("cls")
                                                    time.sleep(1)
                                                    os.system("py Verhaallijn.py")
                                                elif restart == "2":
                                                    print("Oke, bedankt voor het spelen. Tot ziens!")
                                                    time.sleep(0.6)
                                                    os.system("taskkill /IM cmd.exe")
                                                else:
                                                    print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                    time.sleep(0.7)
                                                    os.system("cls")    
                                    else:
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                        print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                        print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                        print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                        print("\n[Einde]")
                                        while True:
                                            while True:
                                                restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                if restart in ("1") or ("2"):
                                                    break
                                                if restart == "1":
                                                    print("Laten we het verhaal opnieuw spelen")
                                                    time.sleep(0.8)
                                                    os.system("cls")
                                                    time.sleep(1)
                                                    os.system("py Verhaallijn.py")
                                                elif restart == "2":
                                                    print("Oke, bedankt voor het spelen. Tot ziens!")
                                                    time.sleep(0.6)
                                                    os.system("taskkill /IM cmd.exe")
                                                else:
                                                    print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                    time.sleep(0.7)
                                                    os.system("cls")                         
                            else:
                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print("Yammie lekker ijsje! Je hebt die al jaren niet meer gehad. Het proefden echt enorm lekker. Na zo een lange tijd.")
                                print("Na 5 maanden ontvangen jullie een verblijfsvergunning. Je mogen hier net zo lang blijven tot dat de oorlog voorbij is in jullie land.")

                                print("\nJe mag kiezen of je gebracht word naar het verblijf waar je mag blijven of dat je met de trein wilt…")
                                print("A. …met de trein 18")
                                print("B. …gebracht worden 19")
                                antwoord333m8mq = input("Maak je keuze: ")
                                if antwoord333m8mq == ("A") or ("a"):
                                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    print("Je neemt de trein naar je verblijf. Eindelijk! De plek waar je enorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                                    print("\n Je mag kiezen welke behang je doet in je kamer…")
                                    print("A. roze behang 21")
                                    print("B. blauw behang 21")
                                    antwoord333m8mms = input("Maak je keuze: ")
                                    if antwoord333m8mms == ("A") or ("a"): 
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                        print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                        print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                        print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                        print("\n[Einde]")
                                        while True:
                                            while True:
                                                restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                if restart in ("1") or ("2"):
                                                    break
                                                if restart == "1":
                                                    print("Laten we het verhaal opnieuw spelen")
                                                    time.sleep(0.8)
                                                    os.system("cls")
                                                    time.sleep(1)
                                                    os.system("py Verhaallijn.py")
                                                elif restart == "2":
                                                    print("Oke, bedankt voor het spelen. Tot ziens!")
                                                    time.sleep(0.6)
                                                    os.system("taskkill /IM cmd.exe")
                                                else:
                                                    print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                    time.sleep(0.7)
                                                    os.system("cls") 
                                    else:
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                        print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                        print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                        print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                        print("\n[Einde]")
                                        while True:
                                            while True:
                                                restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                if restart in ("1") or ("2"):
                                                    break
                                                if restart == "1":
                                                    print("Laten we het verhaal opnieuw spelen")
                                                    time.sleep(0.8)
                                                    os.system("cls")
                                                    time.sleep(1)
                                                    os.system("py Verhaallijn.py")
                                                elif restart == "2":
                                                    print("Oke, bedankt voor het spelen. Tot ziens!")
                                                    time.sleep(0.6)
                                                    os.system("taskkill /IM cmd.exe")
                                                else:
                                                    print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                    time.sleep(0.7)
                                                    os.system("cls")
                                else:
                                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    print("Je word gebracht. Eindelijk! De plek waarjeenorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                                    print("\nJe mag kiezen welke behang je doet in je kamer...")
                                    print("A. ...roze behang 21")
                                    print("B. ...blauw behang 21")
                                    antwoord333m8mmzs = input("Maak je keuze: ")
                                    if antwoord333m8mmzs == ("A") or ("a"):
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                        print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                        print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                        print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                        print("\n[Einde]")
                                        while True:
                                            while True:
                                                restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                if restart in ("1") or ("2"):
                                                    break
                                                if restart == "1":
                                                    print("Laten we het verhaal opnieuw spelen")
                                                    time.sleep(0.8)
                                                    os.system("cls")
                                                    time.sleep(1)
                                                    os.system("py Verhaallijn.py")
                                                elif restart == "2":
                                                    print("Oke, bedankt voor het spelen. Tot ziens!")
                                                    time.sleep(0.6)
                                                    os.system("taskkill /IM cmd.exe")
                                                else:
                                                    print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                    time.sleep(0.7)
                                                    os.system("cls")    
                                    else:
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                        print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                        print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                        print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                        print("\n[Einde]")
                                        while True:
                                            while True:
                                                restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                if restart in ("1") or ("2"):
                                                    break
                                                if restart == "1":
                                                    print("Laten we het verhaal opnieuw spelen")
                                                    time.sleep(0.8)
                                                    os.system("cls")
                                                    time.sleep(1)
                                                    os.system("py Verhaallijn.py")
                                                elif restart == "2":
                                                    print("Oke, bedankt voor het spelen. Tot ziens!")
                                                    time.sleep(0.6)
                                                    os.system("taskkill /IM cmd.exe")
                                                else:
                                                    print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                    time.sleep(0.7)
                                                    os.system("cls")
                        else:
                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            print("Het huisje in Duitsland. Je wilde eerst daar de taal kennen. Effe tot rust komen en dan later de reis te gemoed komen naar Nederland.")
                            print("Daar ging 2 jaar over heen.Je wilde weg hier je wilde naar Nederland.")

                            print("\nJe kon kiezen tussen..")
                            print("A. ...met de trein gaan. 14")
                            print("B. ...lopend naar Nederland want dat was niet zo ver. 14")
                            antwoord333m8b = input("Maak je keuze: ")
                            if antwoord333m8b == ("A") or ("a"):
                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print("De reis naar Nederland is begonnen. Je laat alles achter in Duitsland. En neemt je koffertje mee.")
                                print("Na een paar dagen kom je aan in op bij de grens van Nederland je mag hier niet zomaar verblijven daar heb je een verblijfsvergunning voor nodig.")
                                print("En dat duurde langer dan je had verwacht maar je ontvangt een verblijf met allerlei andere mensen uit Syrië waarbij je kan overnachten tot dat het zo ver is.")
                                print("Maar toen je daar aan kwam voelde je als een pas geboren baby zonder moeder. Je kende de taal niet je kende helemaal niks hier.")
                                print(". Alleen maar de mensen die dezelfde taal spraken. Na 5 dagen in het verblijf te hebben gezeten kwam de ijs man toevallig..")

                                print("\nJe kon kiezen tussen de ijsjes..")
                                print("A. Chocolade ijs 15")
                                print("B. Aardbei ijs 15")
                                antwoord333m8zz = input("Maak je keuze: ")
                                if antwoord333m8zz == ("A") or ("a"):
                                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    print("Yammie lekker ijsje! Je hebt die al jaren niet meer gehad. Het proefden echt enorm lekker. Na zo een lange tijd.")
                                    print("Na 5 maanden ontvangen jullie een verblijfsvergunning. Je mogen hier net zo lang blijven tot dat de oorlog voorbij is in jullie land.")

                                    print("\nJe mag kiezen of je gebracht word naar het verblijf waar je mag blijven of dat je met de trein wilt…")
                                    print("A. …met de trein 18")
                                    print("B. …gebracht worden 19")
                                    antwoord333m8mff = input("Maak je keuze: ")
                                    if antwoord333m8mff == ("A") or ("a"):
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("Je neemt de trein naar je verblijf. Eindelijk! De plek waar je enorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                                        print("\n Je mag kiezen welke behang je doet in je kamer…")
                                        print("A. roze behang 21")
                                        print("B. blauw behang 21")
                                        antwoord333m8mm66 = input("Maak je keuze: ")
                                        if antwoord333m8mm66 == ("A") or ("a"): 
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                            print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                            print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                            print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                            print("\n[Einde]")
                                            while True:
                                                while True:
                                                    restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                    if restart in ("1") or ("2"):
                                                        break
                                                    if restart == "1":
                                                        print("Laten we het verhaal opnieuw spelen")
                                                        time.sleep(0.8)
                                                        os.system("cls")
                                                        time.sleep(1)
                                                        os.system("py Verhaallijn.py")
                                                    elif restart == "2":
                                                        print("Oke, bedankt voor het spelen. Tot ziens!")
                                                        time.sleep(0.6)
                                                        os.system("taskkill /IM cmd.exe")
                                                    else:
                                                        print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                        time.sleep(0.7)
                                                        os.system("cls") 
                                        else:
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                            print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                            print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                            print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                            print("\n[Einde]")
                                            while True:
                                                while True:
                                                    restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                    if restart in ("1") or ("2"):
                                                        break
                                                    if restart == "1":
                                                        print("Laten we het verhaal opnieuw spelen")
                                                        time.sleep(0.8)
                                                        os.system("cls")
                                                        time.sleep(1)
                                                        os.system("py Verhaallijn.py")
                                                    elif restart == "2":
                                                        print("Oke, bedankt voor het spelen. Tot ziens!")
                                                        time.sleep(0.6)
                                                        os.system("taskkill /IM cmd.exe")
                                                    else:
                                                        print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                        time.sleep(0.7)
                                                        os.system("cls")
                                    else:
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("Je word gebracht. Eindelijk! De plek waarjeenorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                                        print("\nJe mag kiezen welke behang je doet in je kamer...")
                                        print("A. ...roze behang 21")
                                        print("B. ...blauw behang 21")
                                        antwoord333m8mm09 = input("Maak je keuze: ")
                                        if antwoord333m8mm09== ("A") or ("a"):
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                            print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                            print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                            print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                            print("\n[Einde]")
                                            while True:
                                                while True:
                                                    restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                    if restart in ("1") or ("2"):
                                                        break
                                                    if restart == "1":
                                                        print("Laten we het verhaal opnieuw spelen")
                                                        time.sleep(0.8)
                                                        os.system("cls")
                                                        time.sleep(1)
                                                        os.system("py Verhaallijn.py")
                                                    elif restart == "2":
                                                        print("Oke, bedankt voor het spelen. Tot ziens!")
                                                        time.sleep(0.6)
                                                        os.system("taskkill /IM cmd.exe")
                                                    else:
                                                        print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                        time.sleep(0.7)
                                                        os.system("cls")    
                                        else:
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                            print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                            print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                            print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                            print("\n[Einde]")
                                            while True:
                                                while True:
                                                    restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                    if restart in ("1") or ("2"):
                                                        break
                                                    if restart == "1":
                                                        print("Laten we het verhaal opnieuw spelen")
                                                        time.sleep(0.8)
                                                        os.system("cls")
                                                        time.sleep(1)
                                                        os.system("py Verhaallijn.py")
                                                    elif restart == "2":
                                                        print("Oke, bedankt voor het spelen. Tot ziens!")
                                                        time.sleep(0.6)
                                                        os.system("taskkill /IM cmd.exe")
                                                    else:
                                                        print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                        time.sleep(0.7)
                                                        os.system("cls")                         
                                else:
                                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    print("Yammie lekker ijsje! Je hebt die al jaren niet meer gehad. Het proefden echt enorm lekker. Na zo een lange tijd.")
                                    print("Na 5 maanden ontvangen jullie een verblijfsvergunning. Je mogen hier net zo lang blijven tot dat de oorlog voorbij is in jullie land.")

                                    print("\nJe mag kiezen of je gebracht word naar het verblijf waar je mag blijven of dat je met de trein wilt…")
                                    print("A. …met de trein 18")
                                    print("B. …gebracht worden 19")
                                    antwoord333m8mq9 = input("Maak je keuze: ")
                                    if antwoord333m8mq == ("A") or ("a"):
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("Je neemt de trein naar je verblijf. Eindelijk! De plek waar je enorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                                        print("\n Je mag kiezen welke behang je doet in je kamer…")
                                        print("A. roze behang 21")
                                        print("B. blauw behang 21")
                                        antwoord333m8mms9 = input("Maak je keuze: ")
                                        if antwoord333m8mms9 == ("A") or ("a"): 
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                            print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                            print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                            print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                            print("\n[Einde]")
                                            while True:
                                                while True:
                                                    restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                    if restart in ("1") or ("2"):
                                                        break
                                                    if restart == "1":
                                                        print("Laten we het verhaal opnieuw spelen")
                                                        time.sleep(0.8)
                                                        os.system("cls")
                                                        time.sleep(1)
                                                        os.system("py Verhaallijn.py")
                                                    elif restart == "2":
                                                        print("Oke, bedankt voor het spelen. Tot ziens!")
                                                        time.sleep(0.6)
                                                        os.system("taskkill /IM cmd.exe")
                                                    else:
                                                        print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                        time.sleep(0.7)
                                                        os.system("cls") 
                                        else:
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                            print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                            print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                            print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                            print("\n[Einde]")
                                            while True:
                                                while True:
                                                    restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                    if restart in ("1") or ("2"):
                                                        break
                                                    if restart == "1":
                                                        print("Laten we het verhaal opnieuw spelen")
                                                        time.sleep(0.8)
                                                        os.system("cls")
                                                        time.sleep(1)
                                                        os.system("py Verhaallijn.py")
                                                    elif restart == "2":
                                                        print("Oke, bedankt voor het spelen. Tot ziens!")
                                                        time.sleep(0.6)
                                                        os.system("taskkill /IM cmd.exe")
                                                    else:
                                                        print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                        time.sleep(0.7)
                                                        os.system("cls")
                                    else:
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("Je word gebracht. Eindelijk! De plek waarjeenorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                                        print("\nJe mag kiezen welke behang je doet in je kamer...")
                                        print("A. ...roze behang 21")
                                        print("B. ...blauw behang 21")
                                        antwoord333m8mmzs9 = input("Maak je keuze: ")
                                        if antwoord333m8mmzs9 == ("A") or ("a"):
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                            print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                            print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                            print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                            print("\n[Einde]")
                                            while True:
                                                while True:
                                                    restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                    if restart in ("1") or ("2"):
                                                        break
                                                    if restart == "1":
                                                        print("Laten we het verhaal opnieuw spelen")
                                                        time.sleep(0.8)
                                                        os.system("cls")
                                                        time.sleep(1)
                                                        os.system("py Verhaallijn.py")
                                                    elif restart == "2":
                                                        print("Oke, bedankt voor het spelen. Tot ziens!")
                                                        time.sleep(0.6)
                                                        os.system("taskkill /IM cmd.exe")
                                                    else:
                                                        print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                        time.sleep(0.7)
                                                        os.system("cls")    
                                        else:
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                            print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                            print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                            print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                            print("\n[Einde]")
                                            while True:
                                                while True:
                                                    restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                    if restart in ("1") or ("2"):
                                                        break
                                                    if restart == "1":
                                                        print("Laten we het verhaal opnieuw spelen")
                                                        time.sleep(0.8)
                                                        os.system("cls")
                                                        time.sleep(1)
                                                        os.system("py Verhaallijn.py")
                                                    elif restart == "2":
                                                        print("Oke, bedankt voor het spelen. Tot ziens!")
                                                        time.sleep(0.6)
                                                        os.system("taskkill /IM cmd.exe")
                                                    else:
                                                        print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                        time.sleep(0.7)
                                                        os.system("cls")
                    else:
                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        print("Op naar Nederland!De reis is enorm lastig om vanaf hier‘Italië’naarNederland te gaan.Dagen gingen voorbij. Je komt aan na 5 dagen lopen in Zwitserlandaan.")
                        print("Je ontmoet iemand die alleen de kinderen willen mee nemen naar België en die persoon zoulater dan de volwassen meenemen als ze hier wachten op haar.")
                        print("Ze wilt namelijk graag de kinderen helpen en ze snel opweg nemen naar iets veiligs en ze wist iemand waar hunuit eindelijkkonden verblijven.")

                        print("\nJij kiest ervoor om...")
                        print("A. ...mee te gaan 16")
                        print("B. ...niet mee te gaan 17")
                        antwoord333m3 = input("Maak je keuze: ")
                        if antwoord333m3 == ("A") or ("a"):
                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            print("Je neemt de trein naar je verblijf. Eindelijk! De plek waar je enorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                            print("\n Je mag kiezen welke behang je doet in je kamer…")
                            print("A. roze behang 21")
                            print("B. blauw behang 21")
                            antwoord333m33 = input("Maak je keuze: ")
                            if antwoord333m33 == ("A") or ("a"):
                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                print("\n[Einde]")
                                while True:
                                    while True:
                                        restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                        if restart in ("1") or ("2"):
                                            break
                                        if restart == "1":
                                            print("Laten we het verhaal opnieuw spelen")
                                            time.sleep(0.8)
                                            os.system("cls")
                                            time.sleep(1)
                                            os.system("py Verhaallijn.py")
                                        elif restart == "2":
                                            print("Oke, bedankt voor het spelen. Tot ziens!")
                                            time.sleep(0.6)
                                            os.system("taskkill /IM cmd.exe")
                                        else:
                                            print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                            time.sleep(0.7)
                                            os.system("cls")
                            else:
                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                print("\n[Einde]")
                                while True:
                                    while True:
                                        restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                        if restart in ("1") or ("2"):
                                            break
                                        if restart == "1":
                                            print("Laten we het verhaal opnieuw spelen")
                                            time.sleep(0.8)
                                            os.system("cls")
                                            time.sleep(1)
                                            os.system("py Verhaallijn.py")
                                        elif restart == "2":
                                            print("Oke, bedankt voor het spelen. Tot ziens!")
                                            time.sleep(0.6)
                                            os.system("taskkill /IM cmd.exe")
                                        else:
                                            print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                            time.sleep(0.7)
                                            os.system("cls")     
                        else:
                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            print("Je gaat niet mee met de vrouw en gaat met groep weg. Na 1 dag gezeten te hebben in Zwitserland.")
                            print("Komt er een politie naar jullie toe en die merkt zich op dat jullie hier illegaalzijn. En die neemt jullie allemaal mee naar de gevangenis")

                            print("\n[Einde]")
                            while True:
                                while True:
                                    restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                    if restart in ("1") or ("2"):
                                        break
                                    if restart == "1":
                                        print("Laten we het verhaal opnieuw spelen")
                                        time.sleep(0.8)
                                        os.system("cls")
                                        time.sleep(1)
                                        os.system("py Verhaallijn.py")
                                    elif restart == "2":
                                        print("Oke, bedankt voor het spelen. Tot ziens!")
                                        time.sleep(0.6)
                                        os.system("taskkill /IM cmd.exe")
                                    else:
                                        print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                        time.sleep(0.7)
                                        os.system("cls")    
            else:
                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("Je kiest ervoor om met de boot weg tegaan. Een nadeel is alleen dat het enorm gevaarlijk grote kans dat je het niet haalt en is het enorm illegaal.")
                print("Je ging met auto naar het water om via daar naar Europa te gaan. De boot die ze daar hadden was veelte klein voor ons allemaal.")
                print("Als de boot zo omslaan zouden we allemaal dood gaan niemand van ons had leren zwemmen en ik kon dat al helemaal niet ik ben bang voor water..")
                print("En daar moesten we 1 dag zitten... Veelte eng!De kinderen moest voorin en de ouderen achterin op elkaar.")
                print("Na 10 uur op elkaar moest iedereen een beetje bewegen de boot bewoog zo ergdat alle mensen aan de rechte kan ging zitten waardoor de boot omsloeg...")

                print("\n[Einde]")
                while True:
                    while True:
                        restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                        if restart in ("1") or ("2"):
                            break
                        if restart == "1":
                            print("Laten we het verhaal opnieuw spelen")
                            time.sleep(0.8)
                            os.system("cls")
                            time.sleep(1)
                            os.system("py Verhaallijn.py")
                        elif restart == "2":
                            print("Oke, bedankt voor het spelen. Tot ziens!")
                            time.sleep(0.6)
                            os.system("taskkill /IM cmd.exe")
                        else:
                            print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                            time.sleep(0.7)
                            os.system("cls")
    else:
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Je verstuurde het berichtje. En je gaat verder met het tandenpoetsen. Je krijgt maar steeds geen berichtje terug.")
        print("Na 2 uur besluit je maar te gaan slapen.*Ring* *Ring* Je wekker gaat af het is half 7.")
        print("Je sluipt zachtjes naar beneden doet je jas aan en vertrekt. Terwijl je onderweg bent bedenk je je of het toch niet zo goed idee was.")

        print("\nEn je besluit om…")
        print("A. …toch terug te gaan naar huis. En weer in bed te liggen 9")
        print("B. …toch door te gaan naar je beste vriendin haar huis. 20")
        antwoord21 = input("Maak je keuze: ")
        if antwoord21 == ("A") or ("a"):
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("En je vertelt haar dat je dit weekend ook niet kon komen. Je krijgt daar geen reactie op.")
            print("Je nog steeds niks binnen. Maar je hoort wel allemaal geritsel thuis.")
            print("Je ziet je moeder en vader heel veel dingen bij elkaar aan het zoeken zijn. Je vraagt wat er aan de hand is.")
            print("Ze zeggen dat je je moet opschieten en je nu per direct je spullen bij elkaar moet zoeken.")
            print("Was het al te laat dus voor al die spullen. Je moeder en vader nemen je rennend mee in de auto.")
            print("Op weg naar de grens. Je ouders worden net om de hoek aangehouden. De mensen die je ouders aanhouden vragen waar jullie heen gaan.")
            print("Je ouders zeggen; alsjeblieft neem mijn kind mee over grens wij blijven hier.")
            print("Alsjeblieft! Jij begint enorm te huilen je weet niet wat er aan de hand is.")
            print("De mensen trekken je uit de auto en nemen je mee.")

            print("\nJij kiest ervoor om..")
            print("A. Toch met je ouders te blijven en met hun mee te gaan. 12")
            print("B. Mee te gaan met die mensen. 11")
            antwoord22 = input("Maak je keuze: ")
            if antwoord22 == ("A") or ("a"):
                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("Jij kiest ervoor om toch te blijven met je ouders. Maar je ouder dwingen je en ze helpen je eruit.")
                print("En je word mee genomen met die mensen. Ze vertellen je dat het gevaarlijk is hier en dat je je ouders willen beschermen.")
                print("Jij vraagt wat er aan de hand is.. De kennissen van je ouders dat zijn wij en mochten niet vertellen wat er aan de hand is maar.")
                print("Er brak gisteren oorlog uit in Syrië. En dit is de laatste keer dat je je ouders ooit nog gaat zien.")
                print("Je brak van binnen je wist niest meer je was er enorm stil van en je stond zo stijf dat je maar de auto in ging van de kennissen.")
                print("De kennissen vertelde dat je word gebracht naar de grens van Europa en daar wacht een ander groep op je.")
                print("Je rijdt naar de grens van Europa waar een boot staan die je naar Italië brengt. Dat ging allemaal goed tot dat de auto bij de grens kwam van Europa.")
                print("Je hoorde mensen praten *Je kan niet in Europa zonder een geldig paspoort*.Maar jij heb die niet.")

                print("\nDe groep kon daar beslissen om..")
                print("A. …5 maanden voor de grens te wachten tot dat je een bewijs krijgt dat je in dat land mag. 1")
                print("B. …gelijk met de boot weg alleen was dat enorm gevaarlijk. Er is namelijk een grote kans dat je het niet haalt. 13")
                antwoord23 = input("Maak je keuze: ")
                if antwoord23 == ("A") or ("a"):
                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    print("De groep kon daar beslissen om 5 maanden voor de grens te wachten tot dat je een bewijs krijgt dat je in dat land mag. De groep ging akkoord!")
                    print("Na een lang tijd waren de 5 maanden voorbij. Ze hadden een vluchtelingen verblijf aangeboden hier in Europa.")
                    print("Ze vroeg aan je of je daar wilde blijven.")

                    print("\nEn jij besloot…")
                    print("A. Verder met dit formulier te reizen naar Nederland. 2")
                    print("B. Daar te blijven. 3")
                    antwoord24 = input("Maak je keuze: ")
                    if antwoord24 == ("A") or ("a"):
                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        print("Je moest enorm veel uren reizen vanaf hier naar Nederland.")
                        print("Je maakte voor jezelf een keuze of je niet eerst in Duitsland wilde verblijven of gelijk door naar Nederland,")
                        print("aangezien je had gehoord dat het super lastig is om in Nederland te blijven mogen leven.")

                        print("\nJe kiest ervoor om naar..")
                        print("A. Duitsland te gaan. 5")
                        print("B. Nederland te gaan. 8")   
                        antwoord25 = input("Maak je keuze: ")
                        if antwoord25 == ("A") or ("a"): 
                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            print("Eerst maar even naar Duitsland. Uren ging voorbij je komt bij de grens van Duitsland aan ze vragen om je paspoort.")
                            print("Je hebt geen geldig paspoort behalve dan de vluchtelingen formulier.")
                            print("In Duitsland is het zo dat je dan ook maanden moet gaan wacht voor dat je in dat land mag komen verblijven.")
                            print("Er gingen weer 5 maanden voorbij. Je kreeg toegang tot Duitsland je mocht er wonen. Je kreeg een verblijf aan geboden.")

                            print("\nMaar jij wilde kiezen tussen..")
                            print("A. De reis naar Nederland. 14")
                            print("B. Een verblijf in Duitsland. 7") 
                            antwoord26 = input("Maak je keuze: ")
                            if antwoord26 == ("A") or ("a"): 
                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print("De reis naar Nederland is begonnen. Je laat alles achter in Duitsland. En neemt je koffertje mee.")
                                print("Na een paar dagen kom je aan in op bij de grens van Nederland je mag hier niet zomaar verblijven daar heb je een verblijfsvergunning voor nodig.")
                                print("En dat duurde langer dan je had verwacht maar je ontvangt een verblijf met allerlei andere mensen uit Syrië waarbij je kan overnachten tot dat het zo ver is.")
                                print("Maar toen je daar aan kwam voelde je als een pas geboren baby zonder moeder. Je kende de taal niet je kende helemaal niks hier.")
                                print(". Alleen maar de mensen die dezelfde taal spraken. Na 5 dagen in het verblijf te hebben gezeten kwam de ijs man toevallig..")

                                print("\nJe kon kiezen tussen de ijsjes..")
                                print("A. Chocolade ijs 15")
                                print("B. Aardbei ijs 15")
                                antwoord27 = input("Maak je keuze: ")
                                if antwoord27 == ("A") or ("a"):
                                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    print("Yammie lekker ijsje! Je hebt die al jaren niet meer gehad. Het proefden echt enorm lekker. Na zo een lange tijd.")
                                    print("Na 5 maanden ontvangen jullie een verblijfsvergunning. Je mogen hier net zo lang blijven tot dat de oorlog voorbij is in jullie land.")

                                    print("\nJe mag kiezen of je gebracht word naar het verblijf waar je mag blijven of dat je met de trein wilt…")
                                    print("A. …met de trein 18")
                                    print("B. …gebracht worden 19")
                                    antwoord28 = input("Maak je keuze: ")
                                    if antwoord28 == ("A") or ("a"):
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("Je neemt de trein naar je verblijf. Eindelijk! De plek waar je enorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                                        print("\n Je mag kiezen welke behang je doet in je kamer…")
                                        print("A. roze behang 21")
                                        print("B. blauw behang 21")  
                                        antwoord29 = input("Maak je keuze: ")
                                        if antwoord29 == ("A") or ("a"):
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                            print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                            print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                            print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                            print("\n[Einde]")
                                            while True:
                                                while True:
                                                    restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                    if restart in ("1") or ("2"):
                                                        break
                                                    if restart == "1":
                                                        print("Laten we het verhaal opnieuw spelen")
                                                        time.sleep(0.8)
                                                        os.system("cls")
                                                        time.sleep(1)
                                                        os.system("py Verhaallijn.py")
                                                    elif restart == "2":
                                                        print("Oke, bedankt voor het spelen. Tot ziens!")
                                                        time.sleep(0.6)
                                                        os.system("taskkill /IM cmd.exe")
                                                    else:
                                                        print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                        time.sleep(0.7)
                                                        os.system("cls")    
                                        else:
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                            print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                            print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                            print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                            print("\n[Einde]")
                                            while True:
                                                while True:
                                                    restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                    if restart in ("1") or ("2"):
                                                        break
                                                    if restart == "1":
                                                        print("Laten we het verhaal opnieuw spelen")
                                                        time.sleep(0.8)
                                                        os.system("cls")
                                                        time.sleep(1)
                                                        os.system("py Verhaallijn.py")
                                                    elif restart == "2":
                                                        print("Oke, bedankt voor het spelen. Tot ziens!")
                                                        time.sleep(0.6)
                                                        os.system("taskkill /IM cmd.exe")
                                                    else:
                                                        print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                        time.sleep(0.7)
                                                        os.system("cls") 
                                    else:
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("Je word gebracht. Eindelijk! De plek waarjeenorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                                        print("\nJe mag kiezen welke behang je doet in je kamer...")
                                        print("A. ...roze behang 21")
                                        print("B. ...blauw behang 21")     
                                        antwoord299 = input("Maak je keuze: ")
                                        if antwoord299 == ("A") or ("a"):
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                            print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                            print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                            print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                            print("\n[Einde]")
                                            while True:
                                                while True:
                                                    restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                    if restart in ("1") or ("2"):
                                                        break
                                                    if restart == "1":
                                                        print("Laten we het verhaal opnieuw spelen")
                                                        time.sleep(0.8)
                                                        os.system("cls")
                                                        time.sleep(1)
                                                        os.system("py Verhaallijn.py")
                                                    elif restart == "2":
                                                        print("Oke, bedankt voor het spelen. Tot ziens!")
                                                        time.sleep(0.6)
                                                        os.system("taskkill /IM cmd.exe")
                                                    else:
                                                        print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                        time.sleep(0.7)
                                                        os.system("cls")    
                                        else:
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                            print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                            print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                            print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                            print("\n[Einde]")
                                            while True:
                                                while True:
                                                    restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                    if restart in ("1") or ("2"):
                                                        break
                                                    if restart == "1":
                                                        print("Laten we het verhaal opnieuw spelen")
                                                        time.sleep(0.8)
                                                        os.system("cls")
                                                        time.sleep(1)
                                                        os.system("py Verhaallijn.py")
                                                    elif restart == "2":
                                                        print("Oke, bedankt voor het spelen. Tot ziens!")
                                                        time.sleep(0.6)
                                                        os.system("taskkill /IM cmd.exe")
                                                    else:
                                                        print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                        time.sleep(0.7)
                                                        os.system("cls") 
                                else:
                                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    print("Yammie lekker ijsje! Je hebt die al jaren niet meer gehad. Het proefden echt enorm lekker. Na zo een lange tijd.")
                                    print("Na 5 maanden ontvangen jullie een verblijfsvergunning. Je mogen hier net zo lang blijven tot dat de oorlog voorbij is in jullie land.")

                                    print("\nJe mag kiezen of je gebracht word naar het verblijf waar je mag blijven of dat je met de trein wilt…")
                                    print("A. …met de trein 18")
                                    print("B. …gebracht worden 19")
                                    antwoord2990 = input("Maak je keuze: ")
                                    if antwoord2990 == ("A") or ("a"):
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("Je neemt de trein naar je verblijf. Eindelijk! De plek waar je enorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                                        print("\n Je mag kiezen welke behang je doet in je kamer…")
                                        print("A. roze behang 21")
                                        print("B. blauw behang 21")  
                                        antwoord2999 = input("Maak je keuze: ")
                                        if antwoord2999 == ("A") or ("a"):
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                            print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                            print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                            print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                            print("\n[Einde]")
                                            while True:
                                                while True:
                                                    restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                    if restart in ("1") or ("2"):
                                                        break
                                                    if restart == "1":
                                                        print("Laten we het verhaal opnieuw spelen")
                                                        time.sleep(0.8)
                                                        os.system("cls")
                                                        time.sleep(1)
                                                        os.system("py Verhaallijn.py")
                                                    elif restart == "2":
                                                        print("Oke, bedankt voor het spelen. Tot ziens!")
                                                        time.sleep(0.6)
                                                        os.system("taskkill /IM cmd.exe")
                                                    else:
                                                        print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                        time.sleep(0.7)
                                                        os.system("cls")    
                                        else:
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                            print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                            print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                            print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                            print("\n[Einde]")
                                            while True:
                                                while True:
                                                    restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                    if restart in ("1") or ("2"):
                                                        break
                                                    if restart == "1":
                                                        print("Laten we het verhaal opnieuw spelen")
                                                        time.sleep(0.8)
                                                        os.system("cls")
                                                        time.sleep(1)
                                                        os.system("py Verhaallijn.py")
                                                    elif restart == "2":
                                                        print("Oke, bedankt voor het spelen. Tot ziens!")
                                                        time.sleep(0.6)
                                                        os.system("taskkill /IM cmd.exe")
                                                    else:
                                                        print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                        time.sleep(0.7)
                                                        os.system("cls") 
                                    else:
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("Je word gebracht. Eindelijk! De plek waarjeenorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                                        print("\nJe mag kiezen welke behang je doet in je kamer...")
                                        print("A. ...roze behang 21")
                                        print("B. ...blauw behang 21")     
                                        antwoord29999 = input("Maak je keuze: ")
                                        if antwoord29999 == ("A") or ("a"):
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                            print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                            print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                            print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                            print("\n[Einde]")
                                            while True:
                                                while True:
                                                    restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                    if restart in ("1") or ("2"):
                                                        break
                                                    if restart == "1":
                                                        print("Laten we het verhaal opnieuw spelen")
                                                        time.sleep(0.8)
                                                        os.system("cls")
                                                        time.sleep(1)
                                                        os.system("py Verhaallijn.py")
                                                    elif restart == "2":
                                                        print("Oke, bedankt voor het spelen. Tot ziens!")
                                                        time.sleep(0.6)
                                                        os.system("taskkill /IM cmd.exe")
                                                    else:
                                                        print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                        time.sleep(0.7)
                                                        os.system("cls")    
                                        else:
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                            print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                            print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                            print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                            print("\n[Einde]")
                                            while True:
                                                while True:
                                                    restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                    if restart in ("1") or ("2"):
                                                        break
                                                    if restart == "1":
                                                        print("Laten we het verhaal opnieuw spelen")
                                                        time.sleep(0.8)
                                                        os.system("cls")
                                                        time.sleep(1)
                                                        os.system("py Verhaallijn.py")
                                                    elif restart == "2":
                                                        print("Oke, bedankt voor het spelen. Tot ziens!")
                                                        time.sleep(0.6)
                                                        os.system("taskkill /IM cmd.exe")
                                                    else:
                                                        print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                        time.sleep(0.7)
                                                        os.system("cls")
                            else:
                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print("Het huisje in Duitsland. Je wilde eerst daar de taal kennen. Effe tot rust komen en dan later de reis te gemoed komen naar Nederland.")
                                print("Daar ging 2 jaar over heen.Je wilde weg hier je wilde naar Nederland.")

                                print("\nJe kon kiezen tussen..")
                                print("A. ...met de trein gaan. 14")
                                print("B. ...lopend naar Nederland want dat was niet zo ver. 14")  
                                antwoord26a = input("Maak je keuze: ")
                                if antwoord26a == ("A") or ("a"): 
                                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    print("De reis naar Nederland is begonnen. Je laat alles achter in Duitsland. En neemt je koffertje mee.")
                                    print("Na een paar dagen kom je aan in op bij de grens van Nederland je mag hier niet zomaar verblijven daar heb je een verblijfsvergunning voor nodig.")
                                    print("En dat duurde langer dan je had verwacht maar je ontvangt een verblijf met allerlei andere mensen uit Syrië waarbij je kan overnachten tot dat het zo ver is.")
                                    print("Maar toen je daar aan kwam voelde je als een pas geboren baby zonder moeder. Je kende de taal niet je kende helemaal niks hier.")
                                    print(". Alleen maar de mensen die dezelfde taal spraken. Na 5 dagen in het verblijf te hebben gezeten kwam de ijs man toevallig..")

                                    print("\nJe kon kiezen tussen de ijsjes..")
                                    print("A. Chocolade ijs 15")
                                    print("B. Aardbei ijs 15")
                                    antwoord27b = input("Maak je keuze: ")
                                    if antwoord27b == ("A") or ("a"):
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("Yammie lekker ijsje! Je hebt die al jaren niet meer gehad. Het proefden echt enorm lekker. Na zo een lange tijd.")
                                        print("Na 5 maanden ontvangen jullie een verblijfsvergunning. Je mogen hier net zo lang blijven tot dat de oorlog voorbij is in jullie land.")

                                        print("\nJe mag kiezen of je gebracht word naar het verblijf waar je mag blijven of dat je met de trein wilt…")
                                        print("A. …met de trein 18")
                                        print("B. …gebracht worden 19")
                                        antwoord28c = input("Maak je keuze: ")
                                        if antwoord28c == ("A") or ("a"):
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("Je neemt de trein naar je verblijf. Eindelijk! De plek waar je enorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                                            print("\n Je mag kiezen welke behang je doet in je kamer…")
                                            print("A. roze behang 21")
                                            print("B. blauw behang 21")  
                                            antwoord29d = input("Maak je keuze: ")
                                            if antwoord29d == ("A") or ("a"):
                                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                                print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                                print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                                print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                                print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                                print("\n[Einde]")
                                                while True:
                                                    while True:
                                                        restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                        if restart in ("1") or ("2"):
                                                            break
                                                        if restart == "1":
                                                            print("Laten we het verhaal opnieuw spelen")
                                                            time.sleep(0.8)
                                                            os.system("cls")
                                                            time.sleep(1)
                                                            os.system("py Verhaallijn.py")
                                                        elif restart == "2":
                                                            print("Oke, bedankt voor het spelen. Tot ziens!")
                                                            time.sleep(0.6)
                                                            os.system("taskkill /IM cmd.exe")
                                                        else:
                                                            print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                            time.sleep(0.7)
                                                            os.system("cls")    
                                            else:
                                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                                print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                                print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                                print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                                print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                                print("\n[Einde]")
                                                while True:
                                                    while True:
                                                        restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                        if restart in ("1") or ("2"):
                                                            break
                                                        if restart == "1":
                                                            print("Laten we het verhaal opnieuw spelen")
                                                            time.sleep(0.8)
                                                            os.system("cls")
                                                            time.sleep(1)
                                                            os.system("py Verhaallijn.py")
                                                        elif restart == "2":
                                                            print("Oke, bedankt voor het spelen. Tot ziens!")
                                                            time.sleep(0.6)
                                                            os.system("taskkill /IM cmd.exe")
                                                        else:
                                                            print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                            time.sleep(0.7)
                                                            os.system("cls") 
                                        else:
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("Je word gebracht. Eindelijk! De plek waarjeenorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                                            print("\nJe mag kiezen welke behang je doet in je kamer...")
                                            print("A. ...roze behang 21")
                                            print("B. ...blauw behang 21")     
                                            antwoord299e = input("Maak je keuze: ")
                                            if antwoord299e == ("A") or ("a"):
                                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                                print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                                print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                                print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                                print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                                print("\n[Einde]")
                                                while True:
                                                    while True:
                                                        restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                        if restart in ("1") or ("2"):
                                                            break
                                                        if restart == "1":
                                                            print("Laten we het verhaal opnieuw spelen")
                                                            time.sleep(0.8)
                                                            os.system("cls")
                                                            time.sleep(1)
                                                            os.system("py Verhaallijn.py")
                                                        elif restart == "2":
                                                            print("Oke, bedankt voor het spelen. Tot ziens!")
                                                            time.sleep(0.6)
                                                            os.system("taskkill /IM cmd.exe")
                                                        else:
                                                            print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                            time.sleep(0.7)
                                                            os.system("cls")    
                                            else:
                                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                                print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                                print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                                print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                                print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                                print("\n[Einde]")
                                                while True:
                                                    while True:
                                                        restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                        if restart in ("1") or ("2"):
                                                            break
                                                        if restart == "1":
                                                            print("Laten we het verhaal opnieuw spelen")
                                                            time.sleep(0.8)
                                                            os.system("cls")
                                                            time.sleep(1)
                                                            os.system("py Verhaallijn.py")
                                                        elif restart == "2":
                                                            print("Oke, bedankt voor het spelen. Tot ziens!")
                                                            time.sleep(0.6)
                                                            os.system("taskkill /IM cmd.exe")
                                                        else:
                                                            print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                            time.sleep(0.7)
                                                            os.system("cls") 
                                    else:
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("Yammie lekker ijsje! Je hebt die al jaren niet meer gehad. Het proefden echt enorm lekker. Na zo een lange tijd.")
                                        print("Na 5 maanden ontvangen jullie een verblijfsvergunning. Je mogen hier net zo lang blijven tot dat de oorlog voorbij is in jullie land.")

                                        print("\nJe mag kiezen of je gebracht word naar het verblijf waar je mag blijven of dat je met de trein wilt…")
                                        print("A. …met de trein 18")
                                        print("B. …gebracht worden 19")
                                        antwoord2990f = input("Maak je keuze: ")
                                        if antwoord2990f == ("A") or ("a"):
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("Je neemt de trein naar je verblijf. Eindelijk! De plek waar je enorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                                            print("\n Je mag kiezen welke behang je doet in je kamer…")
                                            print("A. roze behang 21")
                                            print("B. blauw behang 21")  
                                            antwoord2999g = input("Maak je keuze: ")
                                            if antwoord2999g == ("A") or ("a"):
                                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                                print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                                print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                                print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                                print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                                print("\n[Einde]")
                                                while True:
                                                    while True:
                                                        restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                        if restart in ("1") or ("2"):
                                                            break
                                                        if restart == "1":
                                                            print("Laten we het verhaal opnieuw spelen")
                                                            time.sleep(0.8)
                                                            os.system("cls")
                                                            time.sleep(1)
                                                            os.system("py Verhaallijn.py")
                                                        elif restart == "2":
                                                            print("Oke, bedankt voor het spelen. Tot ziens!")
                                                            time.sleep(0.6)
                                                            os.system("taskkill /IM cmd.exe")
                                                        else:
                                                            print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                            time.sleep(0.7)
                                                            os.system("cls")    
                                            else:
                                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                                print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                                print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                                print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                                print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                                print("\n[Einde]")
                                                while True:
                                                    while True:
                                                        restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                        if restart in ("1") or ("2"):
                                                            break
                                                        if restart == "1":
                                                            print("Laten we het verhaal opnieuw spelen")
                                                            time.sleep(0.8)
                                                            os.system("cls")
                                                            time.sleep(1)
                                                            os.system("py Verhaallijn.py")
                                                        elif restart == "2":
                                                            print("Oke, bedankt voor het spelen. Tot ziens!")
                                                            time.sleep(0.6)
                                                            os.system("taskkill /IM cmd.exe")
                                                        else:
                                                            print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                            time.sleep(0.7)
                                                            os.system("cls") 
                                        else:
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("Je word gebracht. Eindelijk! De plek waarjeenorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                                            print("\nJe mag kiezen welke behang je doet in je kamer...")
                                            print("A. ...roze behang 21")
                                            print("B. ...blauw behang 21")     
                                            antwoord29999h = input("Maak je keuze: ")
                                            if antwoord29999h == ("A") or ("a"):
                                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                                print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                                print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                                print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                                print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                                print("\n[Einde]")
                                                while True:
                                                    while True:
                                                        restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                        if restart in ("1") or ("2"):
                                                            break
                                                        if restart == "1":
                                                            print("Laten we het verhaal opnieuw spelen")
                                                            time.sleep(0.8)
                                                            os.system("cls")
                                                            time.sleep(1)
                                                            os.system("py Verhaallijn.py")
                                                        elif restart == "2":
                                                            print("Oke, bedankt voor het spelen. Tot ziens!")
                                                            time.sleep(0.6)
                                                            os.system("taskkill /IM cmd.exe")
                                                        else:
                                                            print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                            time.sleep(0.7)
                                                            os.system("cls")    
                                            else:
                                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                                print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                                print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                                print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                                print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                                print("\n[Einde]")
                                                while True:
                                                    while True:
                                                        restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                        if restart in ("1") or ("2"):
                                                            break
                                                        if restart == "1":
                                                            print("Laten we het verhaal opnieuw spelen")
                                                            time.sleep(0.8)
                                                            os.system("cls")
                                                            time.sleep(1)
                                                            os.system("py Verhaallijn.py")
                                                        elif restart == "2":
                                                            print("Oke, bedankt voor het spelen. Tot ziens!")
                                                            time.sleep(0.6)
                                                            os.system("taskkill /IM cmd.exe")
                                                        else:
                                                            print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                            time.sleep(0.7)
                                                            os.system("cls")
                        else:
                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            print("Op naar Nederland!De reis is enorm lastig om vanaf hier‘Italië’naarNederland te gaan.Dagen gingen voorbij. Je komt aan na 5 dagen lopen in Zwitserlandaan.")
                            print("Je ontmoet iemand die alleen de kinderen willen mee nemen naar België en die persoon zoulater dan de volwassen meenemen als ze hier wachten op haar.")
                            print("Ze wilt namelijk graag de kinderen helpen en ze snel opweg nemen naar iets veiligs en ze wist iemand waar hunuit eindelijkkonden verblijven.")

                            print("\nJij kiest ervoor om...")
                            print("A. ...mee te gaan 16")
                            print("B. ...niet mee te gaan 17") 
                            antwoord25a = input("Maak je keuze: ")
                            if antwoord25a == ("A") or ("a"): 
                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print("Je neemt de trein naar je verblijf. Eindelijk! De plek waar je enorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                                print("\n Je mag kiezen welke behang je doet in je kamer…")
                                print("A. roze behang 21")
                                print("B. blauw behang 21")
                                antwoord25b = input("Maak je keuze: ")
                                if antwoord25b == ("A") or ("a"): 
                                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                    print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                    print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                    print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                    print("\n[Einde]")
                                    while True:
                                        while True:
                                            restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                            if restart in ("1") or ("2"):
                                                break
                                            if restart == "1":
                                                print("Laten we het verhaal opnieuw spelen")
                                                time.sleep(0.8)
                                                os.system("cls")
                                                time.sleep(1)
                                                os.system("py Verhaallijn.py")
                                            elif restart == "2":
                                                print("Oke, bedankt voor het spelen. Tot ziens!")
                                                time.sleep(0.6)
                                                os.system("taskkill /IM cmd.exe")
                                            else:
                                                print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                time.sleep(0.7)
                                                os.system("cls")    
                                else:
                                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                    print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                    print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                    print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                    print("\n[Einde]")
                                    while True:
                                        while True:
                                            restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                            if restart in ("1") or ("2"):
                                                break
                                            if restart == "1":
                                                print("Laten we het verhaal opnieuw spelen")
                                                time.sleep(0.8)
                                                os.system("cls")
                                                time.sleep(1)
                                                os.system("py Verhaallijn.py")
                                            elif restart == "2":
                                                print("Oke, bedankt voor het spelen. Tot ziens!")
                                                time.sleep(0.6)
                                                os.system("taskkill /IM cmd.exe")
                                            else:
                                                print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                time.sleep(0.7)
                                                os.system("cls")     
                            else:
                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print("Je gaat niet mee met de vrouw en gaat met groep weg. Na 1 dag gezeten te hebben in Zwitserland.")
                                print("Komt er een politie naar jullie toe en die merkt zich op dat jullie hier illegaalzijn. En die neemt jullie allemaal mee naar de gevangenis")

                                print("\n[Einde]")
                                while True:
                                    while True:
                                        restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                        if restart in ("1") or ("2"):
                                            break
                                        if restart == "1":
                                            print("Laten we het verhaal opnieuw spelen")
                                            time.sleep(0.8)
                                            os.system("cls")
                                            time.sleep(1)
                                            os.system("py Verhaallijn.py")
                                        elif restart == "2":
                                            print("Oke, bedankt voor het spelen. Tot ziens!")
                                            time.sleep(0.6)
                                            os.system("taskkill /IM cmd.exe")
                                        else:
                                            print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                            time.sleep(0.7)
                                            os.system("cls")   
                    else:
                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        print("Na3 maanden daar verbleven te hebben besluit je toch maar naar Nederland te gaan. Daar gingen veel uren aan voorbij")

                        print("\nMaar omdat je hoorde dat je moeilijk in Nederland te recht komt gaf je jezelf de keuzenaar welke land je eerst wilde gaan.")
                        print("A. ...Duitsland 5")
                        print("B. ...Nederland 8")  
                        antwoord24a = input("Maak je keuze: ")
                        if antwoord24a == ("A") or ("a"): 
                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            print("Eerst maar even naar Duitsland. Uren ging voorbij je komt bij de grens van Duitsland aan ze vragen om je paspoort.")
                            print("Je hebt geen geldig paspoort behalve dan de vluchtelingen formulier.")
                            print("In Duitsland is het zo dat je dan ook maanden moet gaan wacht voor dat je in dat land mag komen verblijven.")
                            print("Er gingen weer 5 maanden voorbij. Je kreeg toegang tot Duitsland je mocht er wonen. Je kreeg een verblijf aan geboden.")

                            print("\nMaar jij wilde kiezen tussen..")
                            print("A. De reis naar Nederland. 14")
                            print("B. Een verblijf in Duitsland. 7") 
                            antwoord24b = input("Maak je keuze: ")
                            if antwoord24b == ("A") or ("a"): 
                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print("De reis naar Nederland is begonnen. Je laat alles achter in Duitsland. En neemt je koffertje mee.")
                                print("Na een paar dagen kom je aan in op bij de grens van Nederland je mag hier niet zomaar verblijven daar heb je een verblijfsvergunning voor nodig.")
                                print("En dat duurde langer dan je had verwacht maar je ontvangt een verblijf met allerlei andere mensen uit Syrië waarbij je kan overnachten tot dat het zo ver is.")
                                print("Maar toen je daar aan kwam voelde je als een pas geboren baby zonder moeder. Je kende de taal niet je kende helemaal niks hier.")
                                print(". Alleen maar de mensen die dezelfde taal spraken. Na 5 dagen in het verblijf te hebben gezeten kwam de ijs man toevallig..")

                                print("\nJe kon kiezen tussen de ijsjes..")
                                print("A. Chocolade ijs 15")
                                print("B. Aardbei ijs 15")
                                antwoord24c = input("Maak je keuze: ")
                                if antwoord24c == ("A") or ("a"):
                                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    print("Yammie lekker ijsje! Je hebt die al jaren niet meer gehad. Het proefden echt enorm lekker. Na zo een lange tijd.")
                                    print("Na 5 maanden ontvangen jullie een verblijfsvergunning. Je mogen hier net zo lang blijven tot dat de oorlog voorbij is in jullie land.")

                                    print("\nJe mag kiezen of je gebracht word naar het verblijf waar je mag blijven of dat je met de trein wilt…")
                                    print("A. …met de trein 18")
                                    print("B. …gebracht worden 19")
                                    antwoord24d = input("Maak je keuze: ")
                                    if antwoord24d == ("A") or ("a"):
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("Je neemt de trein naar je verblijf. Eindelijk! De plek waar je enorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                                        print("\n Je mag kiezen welke behang je doet in je kamer…")
                                        print("A. roze behang 21")
                                        print("B. blauw behang 21")  
                                        antwoord24e = input("Maak je keuze: ")
                                        if antwoord24e == ("A") or ("a"):
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                            print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                            print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                            print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                            print("\n[Einde]")
                                            while True:
                                                while True:
                                                    restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                    if restart in ("1") or ("2"):
                                                        break
                                                    if restart == "1":
                                                        print("Laten we het verhaal opnieuw spelen")
                                                        time.sleep(0.8)
                                                        os.system("cls")
                                                        time.sleep(1)
                                                        os.system("py Verhaallijn.py")
                                                    elif restart == "2":
                                                        print("Oke, bedankt voor het spelen. Tot ziens!")
                                                        time.sleep(0.6)
                                                        os.system("taskkill /IM cmd.exe")
                                                    else:
                                                        print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                        time.sleep(0.7)
                                                        os.system("cls")    
                                        else:
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                            print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                            print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                            print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                            print("\n[Einde]")
                                            while True:
                                                while True:
                                                    restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                    if restart in ("1") or ("2"):
                                                        break
                                                    if restart == "1":
                                                        print("Laten we het verhaal opnieuw spelen")
                                                        time.sleep(0.8)
                                                        os.system("cls")
                                                        time.sleep(1)
                                                        os.system("py Verhaallijn.py")
                                                    elif restart == "2":
                                                        print("Oke, bedankt voor het spelen. Tot ziens!")
                                                        time.sleep(0.6)
                                                        os.system("taskkill /IM cmd.exe")
                                                    else:
                                                        print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                        time.sleep(0.7)
                                                        os.system("cls") 
                                    else:
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("Je word gebracht. Eindelijk! De plek waarjeenorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                                        print("\nJe mag kiezen welke behang je doet in je kamer...")
                                        print("A. ...roze behang 21")
                                        print("B. ...blauw behang 21")     
                                        antwoord24f = input("Maak je keuze: ")
                                        if antwoord24f == ("A") or ("a"):
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                            print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                            print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                            print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                            print("\n[Einde]")
                                            while True:
                                                while True:
                                                    restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                    if restart in ("1") or ("2"):
                                                        break
                                                    if restart == "1":
                                                        print("Laten we het verhaal opnieuw spelen")
                                                        time.sleep(0.8)
                                                        os.system("cls")
                                                        time.sleep(1)
                                                        os.system("py Verhaallijn.py")
                                                    elif restart == "2":
                                                        print("Oke, bedankt voor het spelen. Tot ziens!")
                                                        time.sleep(0.6)
                                                        os.system("taskkill /IM cmd.exe")
                                                    else:
                                                        print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                        time.sleep(0.7)
                                                        os.system("cls")    
                                        else:
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                            print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                            print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                            print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                            print("\n[Einde]")
                                            while True:
                                                while True:
                                                    restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                    if restart in ("1") or ("2"):
                                                        break
                                                    if restart == "1":
                                                        print("Laten we het verhaal opnieuw spelen")
                                                        time.sleep(0.8)
                                                        os.system("cls")
                                                        time.sleep(1)
                                                        os.system("py Verhaallijn.py")
                                                    elif restart == "2":
                                                        print("Oke, bedankt voor het spelen. Tot ziens!")
                                                        time.sleep(0.6)
                                                        os.system("taskkill /IM cmd.exe")
                                                    else:
                                                        print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                        time.sleep(0.7)
                                                        os.system("cls") 
                                else:
                                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    print("Yammie lekker ijsje! Je hebt die al jaren niet meer gehad. Het proefden echt enorm lekker. Na zo een lange tijd.")
                                    print("Na 5 maanden ontvangen jullie een verblijfsvergunning. Je mogen hier net zo lang blijven tot dat de oorlog voorbij is in jullie land.")

                                    print("\nJe mag kiezen of je gebracht word naar het verblijf waar je mag blijven of dat je met de trein wilt…")
                                    print("A. …met de trein 18")
                                    print("B. …gebracht worden 19")
                                    antwoord24g = input("Maak je keuze: ")
                                    if antwoord24g == ("A") or ("a"):
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("Je neemt de trein naar je verblijf. Eindelijk! De plek waar je enorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                                        print("\n Je mag kiezen welke behang je doet in je kamer…")
                                        print("A. roze behang 21")
                                        print("B. blauw behang 21")  
                                        antwoord24h = input("Maak je keuze: ")
                                        if antwoord24h == ("A") or ("a"):
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                            print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                            print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                            print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                            print("\n[Einde]")
                                            while True:
                                                while True:
                                                    restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                    if restart in ("1") or ("2"):
                                                        break
                                                    if restart == "1":
                                                        print("Laten we het verhaal opnieuw spelen")
                                                        time.sleep(0.8)
                                                        os.system("cls")
                                                        time.sleep(1)
                                                        os.system("py Verhaallijn.py")
                                                    elif restart == "2":
                                                        print("Oke, bedankt voor het spelen. Tot ziens!")
                                                        time.sleep(0.6)
                                                        os.system("taskkill /IM cmd.exe")
                                                    else:
                                                        print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                        time.sleep(0.7)
                                                        os.system("cls")    
                                        else:
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                            print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                            print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                            print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                            print("\n[Einde]")
                                            while True:
                                                while True:
                                                    restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                    if restart in ("1") or ("2"):
                                                        break
                                                    if restart == "1":
                                                        print("Laten we het verhaal opnieuw spelen")
                                                        time.sleep(0.8)
                                                        os.system("cls")
                                                        time.sleep(1)
                                                        os.system("py Verhaallijn.py")
                                                    elif restart == "2":
                                                        print("Oke, bedankt voor het spelen. Tot ziens!")
                                                        time.sleep(0.6)
                                                        os.system("taskkill /IM cmd.exe")
                                                    else:
                                                        print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                        time.sleep(0.7)
                                                        os.system("cls") 
                                    else:
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("Je word gebracht. Eindelijk! De plek waarjeenorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                                        print("\nJe mag kiezen welke behang je doet in je kamer...")
                                        print("A. ...roze behang 21")
                                        print("B. ...blauw behang 21")     
                                        antwoord24i = input("Maak je keuze: ")
                                        if antwoord24i == ("A") or ("a"):
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                            print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                            print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                            print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                            print("\n[Einde]")
                                            while True:
                                                while True:
                                                    restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                    if restart in ("1") or ("2"):
                                                        break
                                                    if restart == "1":
                                                        print("Laten we het verhaal opnieuw spelen")
                                                        time.sleep(0.8)
                                                        os.system("cls")
                                                        time.sleep(1)
                                                        os.system("py Verhaallijn.py")
                                                    elif restart == "2":
                                                        print("Oke, bedankt voor het spelen. Tot ziens!")
                                                        time.sleep(0.6)
                                                        os.system("taskkill /IM cmd.exe")
                                                    else:
                                                        print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                        time.sleep(0.7)
                                                        os.system("cls")    
                                        else:
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                            print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                            print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                            print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                            print("\n[Einde]")
                                            while True:
                                                while True:
                                                    restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                    if restart in ("1") or ("2"):
                                                        break
                                                    if restart == "1":
                                                        print("Laten we het verhaal opnieuw spelen")
                                                        time.sleep(0.8)
                                                        os.system("cls")
                                                        time.sleep(1)
                                                        os.system("py Verhaallijn.py")
                                                    elif restart == "2":
                                                        print("Oke, bedankt voor het spelen. Tot ziens!")
                                                        time.sleep(0.6)
                                                        os.system("taskkill /IM cmd.exe")
                                                    else:
                                                        print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                        time.sleep(0.7)
                                                        os.system("cls")
                            else:
                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print("Het huisje in Duitsland. Je wilde eerst daar de taal kennen. Effe tot rust komen en dan later de reis te gemoed komen naar Nederland.")
                                print("Daar ging 2 jaar over heen.Je wilde weg hier je wilde naar Nederland.")

                                print("\nJe kon kiezen tussen..")
                                print("A. ...met de trein gaan. 14")
                                print("B. ...lopend naar Nederland want dat was niet zo ver. 14")  
                                antwoord24j = input("Maak je keuze: ")
                                if antwoord24j == ("A") or ("a"): 
                                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    print("De reis naar Nederland is begonnen. Je laat alles achter in Duitsland. En neemt je koffertje mee.")
                                    print("Na een paar dagen kom je aan in op bij de grens van Nederland je mag hier niet zomaar verblijven daar heb je een verblijfsvergunning voor nodig.")
                                    print("En dat duurde langer dan je had verwacht maar je ontvangt een verblijf met allerlei andere mensen uit Syrië waarbij je kan overnachten tot dat het zo ver is.")
                                    print("Maar toen je daar aan kwam voelde je als een pas geboren baby zonder moeder. Je kende de taal niet je kende helemaal niks hier.")
                                    print(". Alleen maar de mensen die dezelfde taal spraken. Na 5 dagen in het verblijf te hebben gezeten kwam de ijs man toevallig..")

                                    print("\nJe kon kiezen tussen de ijsjes..")
                                    print("A. Chocolade ijs 15")
                                    print("B. Aardbei ijs 15")
                                    antwoord24k = input("Maak je keuze: ")
                                    if antwoord24k == ("A") or ("a"):
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("Yammie lekker ijsje! Je hebt die al jaren niet meer gehad. Het proefden echt enorm lekker. Na zo een lange tijd.")
                                        print("Na 5 maanden ontvangen jullie een verblijfsvergunning. Je mogen hier net zo lang blijven tot dat de oorlog voorbij is in jullie land.")

                                        print("\nJe mag kiezen of je gebracht word naar het verblijf waar je mag blijven of dat je met de trein wilt…")
                                        print("A. …met de trein 18")
                                        print("B. …gebracht worden 19")
                                        antwoord24l = input("Maak je keuze: ")
                                        if antwoord24l == ("A") or ("a"):
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("Je neemt de trein naar je verblijf. Eindelijk! De plek waar je enorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                                            print("\n Je mag kiezen welke behang je doet in je kamer…")
                                            print("A. roze behang 21")
                                            print("B. blauw behang 21")  
                                            antwoord24m = input("Maak je keuze: ")
                                            if antwoord24m == ("A") or ("a"):
                                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                                print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                                print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                                print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                                print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                                print("\n[Einde]")
                                                while True:
                                                    while True:
                                                        restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                        if restart in ("1") or ("2"):
                                                            break
                                                        if restart == "1":
                                                            print("Laten we het verhaal opnieuw spelen")
                                                            time.sleep(0.8)
                                                            os.system("cls")
                                                            time.sleep(1)
                                                            os.system("py Verhaallijn.py")
                                                        elif restart == "2":
                                                            print("Oke, bedankt voor het spelen. Tot ziens!")
                                                            time.sleep(0.6)
                                                            os.system("taskkill /IM cmd.exe")
                                                        else:
                                                            print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                            time.sleep(0.7)
                                                            os.system("cls")    
                                            else:
                                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                                print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                                print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                                print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                                print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                                print("\n[Einde]")
                                                while True:
                                                    while True:
                                                        restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                        if restart in ("1") or ("2"):
                                                            break
                                                        if restart == "1":
                                                            print("Laten we het verhaal opnieuw spelen")
                                                            time.sleep(0.8)
                                                            os.system("cls")
                                                            time.sleep(1)
                                                            os.system("py Verhaallijn.py")
                                                        elif restart == "2":
                                                            print("Oke, bedankt voor het spelen. Tot ziens!")
                                                            time.sleep(0.6)
                                                            os.system("taskkill /IM cmd.exe")
                                                        else:
                                                            print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                            time.sleep(0.7)
                                                            os.system("cls") 
                                        else:
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("Je word gebracht. Eindelijk! De plek waarjeenorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                                            print("\nJe mag kiezen welke behang je doet in je kamer...")
                                            print("A. ...roze behang 21")
                                            print("B. ...blauw behang 21")     
                                            antwoord24n = input("Maak je keuze: ")
                                            if antwoord24n == ("A") or ("a"):
                                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                                print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                                print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                                print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                                print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                                print("\n[Einde]")
                                                while True:
                                                    while True:
                                                        restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                        if restart in ("1") or ("2"):
                                                            break
                                                        if restart == "1":
                                                            print("Laten we het verhaal opnieuw spelen")
                                                            time.sleep(0.8)
                                                            os.system("cls")
                                                            time.sleep(1)
                                                            os.system("py Verhaallijn.py")
                                                        elif restart == "2":
                                                            print("Oke, bedankt voor het spelen. Tot ziens!")
                                                            time.sleep(0.6)
                                                            os.system("taskkill /IM cmd.exe")
                                                        else:
                                                            print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                            time.sleep(0.7)
                                                            os.system("cls")    
                                            else:
                                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                                print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                                print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                                print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                                print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                                print("\n[Einde]")
                                                while True:
                                                    while True:
                                                        restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                        if restart in ("1") or ("2"):
                                                            break
                                                        if restart == "1":
                                                            print("Laten we het verhaal opnieuw spelen")
                                                            time.sleep(0.8)
                                                            os.system("cls")
                                                            time.sleep(1)
                                                            os.system("py Verhaallijn.py")
                                                        elif restart == "2":
                                                            print("Oke, bedankt voor het spelen. Tot ziens!")
                                                            time.sleep(0.6)
                                                            os.system("taskkill /IM cmd.exe")
                                                        else:
                                                            print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                            time.sleep(0.7)
                                                            os.system("cls") 
                                    else:
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("Yammie lekker ijsje! Je hebt die al jaren niet meer gehad. Het proefden echt enorm lekker. Na zo een lange tijd.")
                                        print("Na 5 maanden ontvangen jullie een verblijfsvergunning. Je mogen hier net zo lang blijven tot dat de oorlog voorbij is in jullie land.")

                                        print("\nJe mag kiezen of je gebracht word naar het verblijf waar je mag blijven of dat je met de trein wilt…")
                                        print("A. …met de trein 18")
                                        print("B. …gebracht worden 19")
                                        antwoord24o = input("Maak je keuze: ")
                                        if antwoord24o == ("A") or ("a"):
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("Je neemt de trein naar je verblijf. Eindelijk! De plek waar je enorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                                            print("\n Je mag kiezen welke behang je doet in je kamer…")
                                            print("A. roze behang 21")
                                            print("B. blauw behang 21")  
                                            antwoord24p = input("Maak je keuze: ")
                                            if antwoord24p == ("A") or ("a"):
                                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                                print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                                print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                                print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                                print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                                print("\n[Einde]")
                                                while True:
                                                    while True:
                                                        restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                        if restart in ("1") or ("2"):
                                                            break
                                                        if restart == "1":
                                                            print("Laten we het verhaal opnieuw spelen")
                                                            time.sleep(0.8)
                                                            os.system("cls")
                                                            time.sleep(1)
                                                            os.system("py Verhaallijn.py")
                                                        elif restart == "2":
                                                            print("Oke, bedankt voor het spelen. Tot ziens!")
                                                            time.sleep(0.6)
                                                            os.system("taskkill /IM cmd.exe")
                                                        else:
                                                            print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                            time.sleep(0.7)
                                                            os.system("cls")    
                                            else:
                                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                                print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                                print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                                print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                                print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                                print("\n[Einde]")
                                                while True:
                                                    while True:
                                                        restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                        if restart in ("1") or ("2"):
                                                            break
                                                        if restart == "1":
                                                            print("Laten we het verhaal opnieuw spelen")
                                                            time.sleep(0.8)
                                                            os.system("cls")
                                                            time.sleep(1)
                                                            os.system("py Verhaallijn.py")
                                                        elif restart == "2":
                                                            print("Oke, bedankt voor het spelen. Tot ziens!")
                                                            time.sleep(0.6)
                                                            os.system("taskkill /IM cmd.exe")
                                                        else:
                                                            print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                            time.sleep(0.7)
                                                            os.system("cls") 
                                        else:
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("Je word gebracht. Eindelijk! De plek waarjeenorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                                            print("\nJe mag kiezen welke behang je doet in je kamer...")
                                            print("A. ...roze behang 21")
                                            print("B. ...blauw behang 21")     
                                            antwoord24q = input("Maak je keuze: ")
                                            if antwoord24q == ("A") or ("a"):
                                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                                print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                                print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                                print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                                print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                                print("\n[Einde]")
                                                while True:
                                                    while True:
                                                        restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                        if restart in ("1") or ("2"):
                                                            break
                                                        if restart == "1":
                                                            print("Laten we het verhaal opnieuw spelen")
                                                            time.sleep(0.8)
                                                            os.system("cls")
                                                            time.sleep(1)
                                                            os.system("py Verhaallijn.py")
                                                        elif restart == "2":
                                                            print("Oke, bedankt voor het spelen. Tot ziens!")
                                                            time.sleep(0.6)
                                                            os.system("taskkill /IM cmd.exe")
                                                        else:
                                                            print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                            time.sleep(0.7)
                                                            os.system("cls")    
                                            else:
                                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                                print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                                print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                                print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                                print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                                print("\n[Einde]")
                                                while True:
                                                    while True:
                                                        restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                        if restart in ("1") or ("2"):
                                                            break
                                                        if restart == "1":
                                                            print("Laten we het verhaal opnieuw spelen")
                                                            time.sleep(0.8)
                                                            os.system("cls")
                                                            time.sleep(1)
                                                            os.system("py Verhaallijn.py")
                                                        elif restart == "2":
                                                            print("Oke, bedankt voor het spelen. Tot ziens!")
                                                            time.sleep(0.6)
                                                            os.system("taskkill /IM cmd.exe")
                                                        else:
                                                            print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                            time.sleep(0.7)
                                                            os.system("cls")
                        else:
                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            print("Op naar Nederland!De reis is enorm lastig om vanaf hier‘Italië’naarNederland te gaan.Dagen gingen voorbij. Je komt aan na 5 dagen lopen in Zwitserlandaan.")
                            print("Je ontmoet iemand die alleen de kinderen willen mee nemen naar België en die persoon zoulater dan de volwassen meenemen als ze hier wachten op haar.")
                            print("Ze wilt namelijk graag de kinderen helpen en ze snel opweg nemen naar iets veiligs en ze wist iemand waar hunuit eindelijkkonden verblijven.")

                            print("\nJij kiest ervoor om...")
                            print("A. ...mee te gaan 16")
                            print("B. ...niet mee te gaan 17") 
                            antwoord24r = input("Maak je keuze: ")
                            if antwoord24r == ("A") or ("a"): 
                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print("Je neemt de trein naar je verblijf. Eindelijk! De plek waar je enorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                                print("\n Je mag kiezen welke behang je doet in je kamer…")
                                print("A. roze behang 21")
                                print("B. blauw behang 21")
                                antwoord24s = input("Maak je keuze: ")
                                if antwoord24s == ("A") or ("a"): 
                                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                    print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                    print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                    print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                    print("\n[Einde]")
                                    while True:
                                        while True:
                                            restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                            if restart in ("1") or ("2"):
                                                break
                                            if restart == "1":
                                                print("Laten we het verhaal opnieuw spelen")
                                                time.sleep(0.8)
                                                os.system("cls")
                                                time.sleep(1)
                                                os.system("py Verhaallijn.py")
                                            elif restart == "2":
                                                print("Oke, bedankt voor het spelen. Tot ziens!")
                                                time.sleep(0.6)
                                                os.system("taskkill /IM cmd.exe")
                                            else:
                                                print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                time.sleep(0.7)
                                                os.system("cls")    
                                else:
                                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                    print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                    print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                    print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                    print("\n[Einde]")
                                    while True:
                                        while True:
                                            restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                            if restart in ("1") or ("2"):
                                                break
                                            if restart == "1":
                                                print("Laten we het verhaal opnieuw spelen")
                                                time.sleep(0.8)
                                                os.system("cls")
                                                time.sleep(1)
                                                os.system("py Verhaallijn.py")
                                            elif restart == "2":
                                                print("Oke, bedankt voor het spelen. Tot ziens!")
                                                time.sleep(0.6)
                                                os.system("taskkill /IM cmd.exe")
                                            else:
                                                print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                time.sleep(0.7)
                                                os.system("cls")     
                            else:
                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print("Je gaat niet mee met de vrouw en gaat met groep weg. Na 1 dag gezeten te hebben in Zwitserland.")
                                print("Komt er een politie naar jullie toe en die merkt zich op dat jullie hier illegaalzijn. En die neemt jullie allemaal mee naar de gevangenis")

                                print("\n[Einde]")
                                while True:
                                    while True:
                                        restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                        if restart in ("1") or ("2"):
                                            break
                                        if restart == "1":
                                            print("Laten we het verhaal opnieuw spelen")
                                            time.sleep(0.8)
                                            os.system("cls")
                                            time.sleep(1)
                                            os.system("py Verhaallijn.py")
                                        elif restart == "2":
                                            print("Oke, bedankt voor het spelen. Tot ziens!")
                                            time.sleep(0.6)
                                            os.system("taskkill /IM cmd.exe")
                                        else:
                                            print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                            time.sleep(0.7)
                                            os.system("cls")
                else:
                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    print("Je kiest ervoor om met de boot weg tegaan. Een nadeel is alleen dat het enorm gevaarlijk grote kans dat je het niet haalt en is het enorm illegaal.")
                    print("Je ging met auto naar het water om via daar naar Europa te gaan. De boot die ze daar hadden was veelte klein voor ons allemaal.")
                    print("Als de boot zo omslaan zouden we allemaal dood gaan niemand van ons had leren zwemmen en ik kon dat al helemaal niet ik ben bang voor water..")
                    print("En daar moesten we 1 dag zitten... Veelte eng!De kinderen moest voorin en de ouderen achterin op elkaar.")
                    print("Na 10 uur op elkaar moest iedereen een beetje bewegen de boot bewoog zo ergdat alle mensen aan de rechte kan ging zitten waardoor de boot omsloeg...")

                    print("\n[Einde]")
                    while True:
                        while True:
                            restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                            if restart in ("1") or ("2"):
                                break
                            if restart == "1":
                                print("Laten we het verhaal opnieuw spelen")
                                time.sleep(0.8)
                                os.system("cls")
                                time.sleep(1)
                                os.system("py Verhaallijn.py")
                            elif restart == "2":
                                print("Oke, bedankt voor het spelen. Tot ziens!")
                                time.sleep(0.6)
                                os.system("taskkill /IM cmd.exe")
                            else:
                                print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                time.sleep(0.7)
                                os.system("cls")     
            else:
                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("Je kiest ervoor om toch mee te gaan met die mensen. En je ouders liet je achter.")
                print("De mensen die je meenamen waren kennissen van je ouders vertelde ze je en die zorgde ervoor dat jij veilig weg zou komen hier uit Syrië.")
                print("En ze vertelde je dat de oorlog uitbrak. En dat het voor jou niet veilig was en je ouders wilde dat jij een goede toekomst zou hebben.")
                print("De kennissen vertelde dat je zo direct met een auto word mee genomen. En dat je vanaf daar met een grote groep mensen met de boot naar Italië zou varen.")
                print("Het was op dat moment te veel voor je dat je het effe niet meer kon plaatsen wat er gebeurden en je ging maar mee in de auto. Onder weg naar de boot naar Italië.")
                print("Dat ging allemaal goed tot dat de auto bij de grens kwam van Europa. Je hoorde mensen praten *Je kan niet in Europa zonder een geldig paspoort*.Maar jij heb die niet.")

                print("\nDe groep kon daar beslissen om..")
                print("A. …5 maanden voor de grens te wachten tot dat je een bewijs krijgt dat je in dat land mag. 1")
                print("B. …gelijk met de boot weg alleen was dat enorm gevaarlijk. Er is namelijk een grote kans dat je het niet haalt. 13")
                antwoord22a = input("Maak je keuze: ")
                if antwoord22a == ("A") or ("a"):
                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    print("De groep kon daar beslissen om 5 maanden voor de grens te wachten tot dat je een bewijs krijgt dat je in dat land mag. De groep ging akkoord!")
                    print("Na een lang tijd waren de 5 maanden voorbij. Ze hadden een vluchtelingen verblijf aangeboden hier in Europa.")
                    print("Ze vroeg aan je of je daar wilde blijven.")

                    print("\nEn jij besloot…")
                    print("A. Verder met dit formulier te reizen naar Nederland. 2")
                    print("B. Daar te blijven. 3")
                    antwoord22b = input("Maak je keuze: ")
                    if antwoord22b == ("A") or ("a"):
                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        print("Je moest enorm veel uren reizen vanaf hier naar Nederland.")
                        print("Je maakte voor jezelf een keuze of je niet eerst in Duitsland wilde verblijven of gelijk door naar Nederland,")
                        print("aangezien je had gehoord dat het super lastig is om in Nederland te blijven mogen leven.")

                        print("\nJe kiest ervoor om naar..")
                        print("A. Duitsland te gaan. 5")
                        print("B. Nederland te gaan. 8")
                        antwoord22c = input("Maak je keuze: ")
                        if antwoord22c == ("A") or ("a"):
                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            print("Eerst maar even naar Duitsland. Uren ging voorbij je komt bij de grens van Duitsland aan ze vragen om je paspoort.")
                            print("Je hebt geen geldig paspoort behalve dan de vluchtelingen formulier.")
                            print("In Duitsland is het zo dat je dan ook maanden moet gaan wacht voor dat je in dat land mag komen verblijven.")
                            print("Er gingen weer 5 maanden voorbij. Je kreeg toegang tot Duitsland je mocht er wonen. Je kreeg een verblijf aan geboden.")

                            print("\nMaar jij wilde kiezen tussen..")
                            print("A. De reis naar Nederland. 14")
                            print("B. Een verblijf in Duitsland. 7")
                            antwoord22d = input("Maak je keuze: ")
                            if antwoord22d == ("A") or ("a"):
                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print("De reis naar Nederland is begonnen. Je laat alles achter in Duitsland. En neemt je koffertje mee.")
                                print("Na een paar dagen kom je aan in op bij de grens van Nederland je mag hier niet zomaar verblijven daar heb je een verblijfsvergunning voor nodig.")
                                print("En dat duurde langer dan je had verwacht maar je ontvangt een verblijf met allerlei andere mensen uit Syrië waarbij je kan overnachten tot dat het zo ver is.")
                                print("Maar toen je daar aan kwam voelde je als een pas geboren baby zonder moeder. Je kende de taal niet je kende helemaal niks hier.")
                                print(". Alleen maar de mensen die dezelfde taal spraken. Na 5 dagen in het verblijf te hebben gezeten kwam de ijs man toevallig..")

                                print("\nJe kon kiezen tussen de ijsjes..")
                                print("A. Chocolade ijs 15")
                                print("B. Aardbei ijs 15")
                                antwoord22e = input("Maak je keuze: ")
                                if antwoord22e == ("A") or ("a"):
                                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    print("Yammie lekker ijsje! Je hebt die al jaren niet meer gehad. Het proefden echt enorm lekker. Na zo een lange tijd.")
                                    print("Na 5 maanden ontvangen jullie een verblijfsvergunning. Je mogen hier net zo lang blijven tot dat de oorlog voorbij is in jullie land.")

                                    print("\nJe mag kiezen of je gebracht word naar het verblijf waar je mag blijven of dat je met de trein wilt…")
                                    print("A. …met de trein 18")
                                    print("B. …gebracht worden 19")
                                    antwoord22f = input("Maak je keuze: ")
                                    if antwoord22f == ("A") or ("a"):
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("Je neemt de trein naar je verblijf. Eindelijk! De plek waar je enorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                                        print("\n Je mag kiezen welke behang je doet in je kamer…")
                                        print("A. roze behang 21")
                                        print("B. blauw behang 21")
                                        antwoord22g = input("Maak je keuze: ")
                                        if antwoord22g == ("A") or ("a"):
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                            print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                            print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                            print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                            print("\n[Einde]")
                                            while True:
                                                while True:
                                                    restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                    if restart in ("1") or ("2"):
                                                        break
                                                    if restart == "1":
                                                        print("Laten we het verhaal opnieuw spelen")
                                                        time.sleep(0.8)
                                                        os.system("cls")
                                                        time.sleep(1)
                                                        os.system("py Verhaallijn.py")
                                                    elif restart == "2":
                                                        print("Oke, bedankt voor het spelen. Tot ziens!")
                                                        time.sleep(0.6)
                                                        os.system("taskkill /IM cmd.exe")
                                                    else:
                                                        print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                        time.sleep(0.7)
                                                        os.system("cls")
                                        else:
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                            print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                            print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                            print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                            print("\n[Einde]")
                                            while True:
                                                while True:
                                                    restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                    if restart in ("1") or ("2"):
                                                        break
                                                    if restart == "1":
                                                        print("Laten we het verhaal opnieuw spelen")
                                                        time.sleep(0.8)
                                                        os.system("cls")
                                                        time.sleep(1)
                                                        os.system("py Verhaallijn.py")
                                                    elif restart == "2":
                                                        print("Oke, bedankt voor het spelen. Tot ziens!")
                                                        time.sleep(0.6)
                                                        os.system("taskkill /IM cmd.exe")
                                                    else:
                                                        print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                        time.sleep(0.7)
                                                        os.system("cls")
                                    else:
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("Je word gebracht. Eindelijk! De plek waarjeenorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                                        print("\nJe mag kiezen welke behang je doet in je kamer...")
                                        print("A. ...roze behang 21")
                                        print("B. ...blauw behang 21")    
                                        antwoord22h = input("Maak je keuze: ")
                                        if antwoord22h == ("A") or ("a"):
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                            print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                            print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                            print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                            print("\n[Einde]")
                                            while True:
                                                while True:
                                                    restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                    if restart in ("1") or ("2"):
                                                        break
                                                    if restart == "1":
                                                        print("Laten we het verhaal opnieuw spelen")
                                                        time.sleep(0.8)
                                                        os.system("cls")
                                                        time.sleep(1)
                                                        os.system("py Verhaallijn.py")
                                                    elif restart == "2":
                                                        print("Oke, bedankt voor het spelen. Tot ziens!")
                                                        time.sleep(0.6)
                                                        os.system("taskkill /IM cmd.exe")
                                                    else:
                                                        print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                        time.sleep(0.7)
                                                        os.system("cls")
                                        else:
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                            print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                            print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                            print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                            print("\n[Einde]")
                                            while True:
                                                while True:
                                                    restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                    if restart in ("1") or ("2"):
                                                        break
                                                    if restart == "1":
                                                        print("Laten we het verhaal opnieuw spelen")
                                                        time.sleep(0.8)
                                                        os.system("cls")
                                                        time.sleep(1)
                                                        os.system("py Verhaallijn.py")
                                                    elif restart == "2":
                                                        print("Oke, bedankt voor het spelen. Tot ziens!")
                                                        time.sleep(0.6)
                                                        os.system("taskkill /IM cmd.exe")
                                                    else:
                                                        print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                        time.sleep(0.7)
                                                        os.system("cls") 
                                else:
                                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    print("Yammie lekker ijsje! Je hebt die al jaren niet meer gehad. Het proefden echt enorm lekker. Na zo een lange tijd.")
                                    print("Na 5 maanden ontvangen jullie een verblijfsvergunning. Je mogen hier net zo lang blijven tot dat de oorlog voorbij is in jullie land.")

                                    print("\nJe mag kiezen of je gebracht word naar het verblijf waar je mag blijven of dat je met de trein wilt…")
                                    print("A. …met de trein 18")
                                    print("B. …gebracht worden 19")
                                    antwoord22i = input("Maak je keuze: ")
                                    if antwoord22i == ("A") or ("a"):
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("Je neemt de trein naar je verblijf. Eindelijk! De plek waar je enorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                                        print("\n Je mag kiezen welke behang je doet in je kamer…")
                                        print("A. roze behang 21")
                                        print("B. blauw behang 21")
                                        antwoord22j = input("Maak je keuze: ")
                                        if antwoord22j == ("A") or ("a"):
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                            print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                            print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                            print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                            print("\n[Einde]")
                                            while True:
                                                while True:
                                                    restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                    if restart in ("1") or ("2"):
                                                        break
                                                    if restart == "1":
                                                        print("Laten we het verhaal opnieuw spelen")
                                                        time.sleep(0.8)
                                                        os.system("cls")
                                                        time.sleep(1)
                                                        os.system("py Verhaallijn.py")
                                                    elif restart == "2":
                                                        print("Oke, bedankt voor het spelen. Tot ziens!")
                                                        time.sleep(0.6)
                                                        os.system("taskkill /IM cmd.exe")
                                                    else:
                                                        print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                        time.sleep(0.7)
                                                        os.system("cls")
                                        else:
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                            print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                            print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                            print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                            print("\n[Einde]")
                                            while True:
                                                while True:
                                                    restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                    if restart in ("1") or ("2"):
                                                        break
                                                    if restart == "1":
                                                        print("Laten we het verhaal opnieuw spelen")
                                                        time.sleep(0.8)
                                                        os.system("cls")
                                                        time.sleep(1)
                                                        os.system("py Verhaallijn.py")
                                                    elif restart == "2":
                                                        print("Oke, bedankt voor het spelen. Tot ziens!")
                                                        time.sleep(0.6)
                                                        os.system("taskkill /IM cmd.exe")
                                                    else:
                                                        print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                        time.sleep(0.7)
                                                        os.system("cls")
                                    else:
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("Je word gebracht. Eindelijk! De plek waarjeenorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                                        print("\nJe mag kiezen welke behang je doet in je kamer...")
                                        print("A. ...roze behang 21")
                                        print("B. ...blauw behang 21")    
                                        antwoord22k = input("Maak je keuze: ")
                                        if antwoord22k == ("A") or ("a"):
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                            print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                            print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                            print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                            print("\n[Einde]")
                                            while True:
                                                while True:
                                                    restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                    if restart in ("1") or ("2"):
                                                        break
                                                    if restart == "1":
                                                        print("Laten we het verhaal opnieuw spelen")
                                                        time.sleep(0.8)
                                                        os.system("cls")
                                                        time.sleep(1)
                                                        os.system("py Verhaallijn.py")
                                                    elif restart == "2":
                                                        print("Oke, bedankt voor het spelen. Tot ziens!")
                                                        time.sleep(0.6)
                                                        os.system("taskkill /IM cmd.exe")
                                                    else:
                                                        print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                        time.sleep(0.7)
                                                        os.system("cls")
                                        else:
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                            print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                            print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                            print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                            print("\n[Einde]")
                                            while True:
                                                while True:
                                                    restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                    if restart in ("1") or ("2"):
                                                        break
                                                    if restart == "1":
                                                        print("Laten we het verhaal opnieuw spelen")
                                                        time.sleep(0.8)
                                                        os.system("cls")
                                                        time.sleep(1)
                                                        os.system("py Verhaallijn.py")
                                                    elif restart == "2":
                                                        print("Oke, bedankt voor het spelen. Tot ziens!")
                                                        time.sleep(0.6)
                                                        os.system("taskkill /IM cmd.exe")
                                                    else:
                                                        print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                        time.sleep(0.7)
                                                        os.system("cls")                                                       
                            else:
                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print("Het huisje in Duitsland. Je wilde eerst daar de taal kennen. Effe tot rust komen en dan later de reis te gemoed komen naar Nederland.")
                                print("Daar ging 2 jaar over heen.Je wilde weg hier je wilde naar Nederland.")

                                print("\nJe kon kiezen tussen..")
                                print("A. ...met de trein gaan. 14")
                                print("B. ...lopend naar Nederland want dat was niet zo ver. 14")
                                antwoord221 = input("Maak je keuze: ")
                                if antwoord221 == ("A") or ("a"):
                                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    print("De reis naar Nederland is begonnen. Je laat alles achter in Duitsland. En neemt je koffertje mee.")
                                    print("Na een paar dagen kom je aan in op bij de grens van Nederland je mag hier niet zomaar verblijven daar heb je een verblijfsvergunning voor nodig.")
                                    print("En dat duurde langer dan je had verwacht maar je ontvangt een verblijf met allerlei andere mensen uit Syrië waarbij je kan overnachten tot dat het zo ver is.")
                                    print("Maar toen je daar aan kwam voelde je als een pas geboren baby zonder moeder. Je kende de taal niet je kende helemaal niks hier.")
                                    print(". Alleen maar de mensen die dezelfde taal spraken. Na 5 dagen in het verblijf te hebben gezeten kwam de ijs man toevallig..")

                                    print("\nJe kon kiezen tussen de ijsjes..")
                                    print("A. Chocolade ijs 15")
                                    print("B. Aardbei ijs 15")
                                    antwoord222 = input("Maak je keuze: ")
                                    if antwoord222 == ("A") or ("a"):
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("Yammie lekker ijsje! Je hebt die al jaren niet meer gehad. Het proefden echt enorm lekker. Na zo een lange tijd.")
                                        print("Na 5 maanden ontvangen jullie een verblijfsvergunning. Je mogen hier net zo lang blijven tot dat de oorlog voorbij is in jullie land.")

                                        print("\nJe mag kiezen of je gebracht word naar het verblijf waar je mag blijven of dat je met de trein wilt…")
                                        print("A. …met de trein 18")
                                        print("B. …gebracht worden 19")
                                        antwoord223 = input("Maak je keuze: ")
                                        if antwoord223 == ("A") or ("a"):
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("Je neemt de trein naar je verblijf. Eindelijk! De plek waar je enorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                                            print("\n Je mag kiezen welke behang je doet in je kamer…")
                                            print("A. roze behang 21")
                                            print("B. blauw behang 21")
                                            antwoord224 = input("Maak je keuze: ")
                                            if antwoord224 == ("A") or ("a"):
                                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                                print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                                print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                                print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                                print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                                print("\n[Einde]")
                                                while True:
                                                    while True:
                                                        restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                        if restart in ("1") or ("2"):
                                                            break
                                                        if restart == "1":
                                                            print("Laten we het verhaal opnieuw spelen")
                                                            time.sleep(0.8)
                                                            os.system("cls")
                                                            time.sleep(1)
                                                            os.system("py Verhaallijn.py")
                                                        elif restart == "2":
                                                            print("Oke, bedankt voor het spelen. Tot ziens!")
                                                            time.sleep(0.6)
                                                            os.system("taskkill /IM cmd.exe")
                                                        else:
                                                            print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                            time.sleep(0.7)
                                                            os.system("cls")
                                            else:
                                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                                print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                                print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                                print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                                print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                                print("\n[Einde]")
                                                while True:
                                                    while True:
                                                        restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                        if restart in ("1") or ("2"):
                                                            break
                                                        if restart == "1":
                                                            print("Laten we het verhaal opnieuw spelen")
                                                            time.sleep(0.8)
                                                            os.system("cls")
                                                            time.sleep(1)
                                                            os.system("py Verhaallijn.py")
                                                        elif restart == "2":
                                                            print("Oke, bedankt voor het spelen. Tot ziens!")
                                                            time.sleep(0.6)
                                                            os.system("taskkill /IM cmd.exe")
                                                        else:
                                                            print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                            time.sleep(0.7)
                                                            os.system("cls")  
                                        else:
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("Je word gebracht. Eindelijk! De plek waarjeenorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                                            print("\nJe mag kiezen welke behang je doet in je kamer...")
                                            print("A. ...roze behang 21")
                                            print("B. ...blauw behang 21")
                                            antwoord225 = input("Maak je keuze: ")
                                            if antwoord225 == ("A") or ("a"):
                                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                                print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                                print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                                print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                                print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                                print("\n[Einde]")
                                                while True:
                                                    while True:
                                                        restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                        if restart in ("1") or ("2"):
                                                            break
                                                        if restart == "1":
                                                            print("Laten we het verhaal opnieuw spelen")
                                                            time.sleep(0.8)
                                                            os.system("cls")
                                                            time.sleep(1)
                                                            os.system("py Verhaallijn.py")
                                                        elif restart == "2":
                                                            print("Oke, bedankt voor het spelen. Tot ziens!")
                                                            time.sleep(0.6)
                                                            os.system("taskkill /IM cmd.exe")
                                                        else:
                                                            print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                            time.sleep(0.7)
                                                            os.system("cls")
                                            else:
                                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                                print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                                print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                                print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                                print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                                print("\n[Einde]")
                                                while True:
                                                    while True:
                                                        restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                        if restart in ("1") or ("2"):
                                                            break
                                                        if restart == "1":
                                                            print("Laten we het verhaal opnieuw spelen")
                                                            time.sleep(0.8)
                                                            os.system("cls")
                                                            time.sleep(1)
                                                            os.system("py Verhaallijn.py")
                                                        elif restart == "2":
                                                            print("Oke, bedankt voor het spelen. Tot ziens!")
                                                            time.sleep(0.6)
                                                            os.system("taskkill /IM cmd.exe")
                                                        else:
                                                            print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                            time.sleep(0.7)
                                                            os.system("cls")
                                    else:
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("Yammie lekker ijsje! Je hebt die al jaren niet meer gehad. Het proefden echt enorm lekker. Na zo een lange tijd.")
                                        print("Na 5 maanden ontvangen jullie een verblijfsvergunning. Je mogen hier net zo lang blijven tot dat de oorlog voorbij is in jullie land.")

                                        print("\nJe mag kiezen of je gebracht word naar het verblijf waar je mag blijven of dat je met de trein wilt…")
                                        print("A. …met de trein 18")
                                        print("B. …gebracht worden 19")
                                        antwoord226 = input("Maak je keuze: ")
                                        if antwoord226 == ("A") or ("a"):
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("Je neemt de trein naar je verblijf. Eindelijk! De plek waar je enorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                                            print("\n Je mag kiezen welke behang je doet in je kamer…")
                                            print("A. roze behang 21")
                                            print("B. blauw behang 21")
                                            antwoord227 = input("Maak je keuze: ")
                                            if antwoord227 == ("A") or ("a"):
                                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                                print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                                print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                                print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                                print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                                print("\n[Einde]")
                                                while True:
                                                    while True:
                                                        restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                        if restart in ("1") or ("2"):
                                                            break
                                                        if restart == "1":
                                                            print("Laten we het verhaal opnieuw spelen")
                                                            time.sleep(0.8)
                                                            os.system("cls")
                                                            time.sleep(1)
                                                            os.system("py Verhaallijn.py")
                                                        elif restart == "2":
                                                            print("Oke, bedankt voor het spelen. Tot ziens!")
                                                            time.sleep(0.6)
                                                            os.system("taskkill /IM cmd.exe")
                                                        else:
                                                            print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                            time.sleep(0.7)
                                                            os.system("cls")
                                            else:
                                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                                print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                                print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                                print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                                print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                                print("\n[Einde]")
                                                while True:
                                                    while True:
                                                        restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                        if restart in ("1") or ("2"):
                                                            break
                                                        if restart == "1":
                                                            print("Laten we het verhaal opnieuw spelen")
                                                            time.sleep(0.8)
                                                            os.system("cls")
                                                            time.sleep(1)
                                                            os.system("py Verhaallijn.py")
                                                        elif restart == "2":
                                                            print("Oke, bedankt voor het spelen. Tot ziens!")
                                                            time.sleep(0.6)
                                                            os.system("taskkill /IM cmd.exe")
                                                        else:
                                                            print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                            time.sleep(0.7)
                                                            os.system("cls")  
                                        else:
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("Je word gebracht. Eindelijk! De plek waarjeenorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                                            print("\nJe mag kiezen welke behang je doet in je kamer...")
                                            print("A. ...roze behang 21")
                                            print("B. ...blauw behang 21")
                                            antwoord228 = input("Maak je keuze: ")
                                            if antwoord228 == ("A") or ("a"):
                                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                                print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                                print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                                print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                                print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                                print("\n[Einde]")
                                                while True:
                                                    while True:
                                                        restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                        if restart in ("1") or ("2"):
                                                            break
                                                        if restart == "1":
                                                            print("Laten we het verhaal opnieuw spelen")
                                                            time.sleep(0.8)
                                                            os.system("cls")
                                                            time.sleep(1)
                                                            os.system("py Verhaallijn.py")
                                                        elif restart == "2":
                                                            print("Oke, bedankt voor het spelen. Tot ziens!")
                                                            time.sleep(0.6)
                                                            os.system("taskkill /IM cmd.exe")
                                                        else:
                                                            print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                            time.sleep(0.7)
                                                            os.system("cls")
                                            else:
                                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                                print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                                print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                                print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                                print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                                print("\n[Einde]")
                                                while True:
                                                    while True:
                                                        restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                        if restart in ("1") or ("2"):
                                                            break
                                                        if restart == "1":
                                                            print("Laten we het verhaal opnieuw spelen")
                                                            time.sleep(0.8)
                                                            os.system("cls")
                                                            time.sleep(1)
                                                            os.system("py Verhaallijn.py")
                                                        elif restart == "2":
                                                            print("Oke, bedankt voor het spelen. Tot ziens!")
                                                            time.sleep(0.6)
                                                            os.system("taskkill /IM cmd.exe")
                                                        else:
                                                            print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                            time.sleep(0.7)
                                                            os.system("cls") 
                                else:
                                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    print("De reis naar Nederland is begonnen. Je laat alles achter in Duitsland. En neemt je koffertje mee.")
                                    print("Na een paar dagen kom je aan in op bij de grens van Nederland je mag hier niet zomaar verblijven daar heb je een verblijfsvergunning voor nodig.")
                                    print("En dat duurde langer dan je had verwacht maar je ontvangt een verblijf met allerlei andere mensen uit Syrië waarbij je kan overnachten tot dat het zo ver is.")
                                    print("Maar toen je daar aan kwam voelde je als een pas geboren baby zonder moeder. Je kende de taal niet je kende helemaal niks hier.")
                                    print(". Alleen maar de mensen die dezelfde taal spraken. Na 5 dagen in het verblijf te hebben gezeten kwam de ijs man toevallig..")

                                    print("\nJe kon kiezen tussen de ijsjes..")
                                    print("A. Chocolade ijs 15")
                                    print("B. Aardbei ijs 15")
                                    antwoord229 = input("Maak je keuze: ")
                                    if antwoord229 == ("A") or ("a"):
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("Yammie lekker ijsje! Je hebt die al jaren niet meer gehad. Het proefden echt enorm lekker. Na zo een lange tijd.")
                                        print("Na 5 maanden ontvangen jullie een verblijfsvergunning. Je mogen hier net zo lang blijven tot dat de oorlog voorbij is in jullie land.")

                                        print("\nJe mag kiezen of je gebracht word naar het verblijf waar je mag blijven of dat je met de trein wilt…")
                                        print("A. …met de trein 18")
                                        print("B. …gebracht worden 19")
                                        antwoord2210 = input("Maak je keuze: ")
                                        if antwoord2210 == ("A") or ("a"):
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("Je neemt de trein naar je verblijf. Eindelijk! De plek waar je enorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                                            print("\n Je mag kiezen welke behang je doet in je kamer…")
                                            print("A. roze behang 21")
                                            print("B. blauw behang 21")
                                            antwoord2211 = input("Maak je keuze: ")
                                            if antwoord2211 == ("A") or ("a"):
                                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                                print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                                print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                                print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                                print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                                print("\n[Einde]")
                                                while True:
                                                    while True:
                                                        restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                        if restart in ("1") or ("2"):
                                                            break
                                                        if restart == "1":
                                                            print("Laten we het verhaal opnieuw spelen")
                                                            time.sleep(0.8)
                                                            os.system("cls")
                                                            time.sleep(1)
                                                            os.system("py Verhaallijn.py")
                                                        elif restart == "2":
                                                            print("Oke, bedankt voor het spelen. Tot ziens!")
                                                            time.sleep(0.6)
                                                            os.system("taskkill /IM cmd.exe")
                                                        else:
                                                            print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                            time.sleep(0.7)
                                                            os.system("cls")
                                            else:
                                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                                print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                                print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                                print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                                print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                                print("\n[Einde]")
                                                while True:
                                                    while True:
                                                        restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                        if restart in ("1") or ("2"):
                                                            break
                                                        if restart == "1":
                                                            print("Laten we het verhaal opnieuw spelen")
                                                            time.sleep(0.8)
                                                            os.system("cls")
                                                            time.sleep(1)
                                                            os.system("py Verhaallijn.py")
                                                        elif restart == "2":
                                                            print("Oke, bedankt voor het spelen. Tot ziens!")
                                                            time.sleep(0.6)
                                                            os.system("taskkill /IM cmd.exe")
                                                        else:
                                                            print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                            time.sleep(0.7)
                                                            os.system("cls")  
                                        else:
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("Je word gebracht. Eindelijk! De plek waarjeenorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                                            print("\nJe mag kiezen welke behang je doet in je kamer...")
                                            print("A. ...roze behang 21")
                                            print("B. ...blauw behang 21")
                                            antwoord2212 = input("Maak je keuze: ")
                                            if antwoord2212 == ("A") or ("a"):
                                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                                print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                                print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                                print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                                print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                                print("\n[Einde]")
                                                while True:
                                                    while True:
                                                        restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                        if restart in ("1") or ("2"):
                                                            break
                                                        if restart == "1":
                                                            print("Laten we het verhaal opnieuw spelen")
                                                            time.sleep(0.8)
                                                            os.system("cls")
                                                            time.sleep(1)
                                                            os.system("py Verhaallijn.py")
                                                        elif restart == "2":
                                                            print("Oke, bedankt voor het spelen. Tot ziens!")
                                                            time.sleep(0.6)
                                                            os.system("taskkill /IM cmd.exe")
                                                        else:
                                                            print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                            time.sleep(0.7)
                                                            os.system("cls")
                                            else:
                                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                                print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                                print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                                print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                                print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                                print("\n[Einde]")
                                                while True:
                                                    while True:
                                                        restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                        if restart in ("1") or ("2"):
                                                            break
                                                        if restart == "1":
                                                            print("Laten we het verhaal opnieuw spelen")
                                                            time.sleep(0.8)
                                                            os.system("cls")
                                                            time.sleep(1)
                                                            os.system("py Verhaallijn.py")
                                                        elif restart == "2":
                                                            print("Oke, bedankt voor het spelen. Tot ziens!")
                                                            time.sleep(0.6)
                                                            os.system("taskkill /IM cmd.exe")
                                                        else:
                                                            print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                            time.sleep(0.7)
                                                            os.system("cls")
                                    else:
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("Yammie lekker ijsje! Je hebt die al jaren niet meer gehad. Het proefden echt enorm lekker. Na zo een lange tijd.")
                                        print("Na 5 maanden ontvangen jullie een verblijfsvergunning. Je mogen hier net zo lang blijven tot dat de oorlog voorbij is in jullie land.")

                                        print("\nJe mag kiezen of je gebracht word naar het verblijf waar je mag blijven of dat je met de trein wilt…")
                                        print("A. …met de trein 18")
                                        print("B. …gebracht worden 19")
                                        antwoord2213 = input("Maak je keuze: ")
                                        if antwoord2213 == ("A") or ("a"):
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("Je neemt de trein naar je verblijf. Eindelijk! De plek waar je enorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                                            print("\n Je mag kiezen welke behang je doet in je kamer…")
                                            print("A. roze behang 21")
                                            print("B. blauw behang 21")
                                            antwoord2214 = input("Maak je keuze: ")
                                            if antwoord2214 == ("A") or ("a"):
                                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                                print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                                print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                                print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                                print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                                print("\n[Einde]")
                                                while True:
                                                    while True:
                                                        restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                        if restart in ("1") or ("2"):
                                                            break
                                                        if restart == "1":
                                                            print("Laten we het verhaal opnieuw spelen")
                                                            time.sleep(0.8)
                                                            os.system("cls")
                                                            time.sleep(1)
                                                            os.system("py Verhaallijn.py")
                                                        elif restart == "2":
                                                            print("Oke, bedankt voor het spelen. Tot ziens!")
                                                            time.sleep(0.6)
                                                            os.system("taskkill /IM cmd.exe")
                                                        else:
                                                            print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                            time.sleep(0.7)
                                                            os.system("cls")
                                            else:
                                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                                print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                                print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                                print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                                print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                                print("\n[Einde]")
                                                while True:
                                                    while True:
                                                        restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                        if restart in ("1") or ("2"):
                                                            break
                                                        if restart == "1":
                                                            print("Laten we het verhaal opnieuw spelen")
                                                            time.sleep(0.8)
                                                            os.system("cls")
                                                            time.sleep(1)
                                                            os.system("py Verhaallijn.py")
                                                        elif restart == "2":
                                                            print("Oke, bedankt voor het spelen. Tot ziens!")
                                                            time.sleep(0.6)
                                                            os.system("taskkill /IM cmd.exe")
                                                        else:
                                                            print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                            time.sleep(0.7)
                                                            os.system("cls")  
                                        else:
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("Je word gebracht. Eindelijk! De plek waarjeenorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                                            print("\nJe mag kiezen welke behang je doet in je kamer...")
                                            print("A. ...roze behang 21")
                                            print("B. ...blauw behang 21")
                                            antwoord2215 = input("Maak je keuze: ")
                                            if antwoord2215 == ("A") or ("a"):
                                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                                print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                                print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                                print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                                print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                                print("\n[Einde]")
                                                while True:
                                                    while True:
                                                        restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                        if restart in ("1") or ("2"):
                                                            break
                                                        if restart == "1":
                                                            print("Laten we het verhaal opnieuw spelen")
                                                            time.sleep(0.8)
                                                            os.system("cls")
                                                            time.sleep(1)
                                                            os.system("py Verhaallijn.py")
                                                        elif restart == "2":
                                                            print("Oke, bedankt voor het spelen. Tot ziens!")
                                                            time.sleep(0.6)
                                                            os.system("taskkill /IM cmd.exe")
                                                        else:
                                                            print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                            time.sleep(0.7)
                                                            os.system("cls")
                                            else:
                                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                                print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                                print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                                print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                                print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                                print("\n[Einde]")
                                                while True:
                                                    while True:
                                                        restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                        if restart in ("1") or ("2"):
                                                            break
                                                        if restart == "1":
                                                            print("Laten we het verhaal opnieuw spelen")
                                                            time.sleep(0.8)
                                                            os.system("cls")
                                                            time.sleep(1)
                                                            os.system("py Verhaallijn.py")
                                                        elif restart == "2":
                                                            print("Oke, bedankt voor het spelen. Tot ziens!")
                                                            time.sleep(0.6)
                                                            os.system("taskkill /IM cmd.exe")
                                                        else:
                                                            print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                            time.sleep(0.7)
                                                            os.system("cls")
                        else:
                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            print("Op naar Nederland!De reis is enorm lastig om vanaf hier‘Italië’naarNederland te gaan.Dagen gingen voorbij. Je komt aan na 5 dagen lopen in Zwitserlandaan.")
                            print("Je ontmoet iemand die alleen de kinderen willen mee nemen naar België en die persoon zoulater dan de volwassen meenemen als ze hier wachten op haar.")
                            print("Ze wilt namelijk graag de kinderen helpen en ze snel opweg nemen naar iets veiligs en ze wist iemand waar hunuit eindelijkkonden verblijven.")

                            print("\nJij kiest ervoor om...")
                            print("A. ...mee te gaan 16")
                            print("B. ...niet mee te gaan 17")   
                            antwoord22c1 = input("Maak je keuze: ")
                            if antwoord22c1 == ("A") or ("a"): 
                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print("Je neemt de trein naar je verblijf. Eindelijk! De plek waar je enorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                                print("\n Je mag kiezen welke behang je doet in je kamer…")
                                print("A. roze behang 21")
                                print("B. blauw behang 21")
                                antwoord22c2 = input("Maak je keuze: ")
                                if antwoord22c2 == ("A") or ("a"):
                                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                    print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                    print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                    print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                    print("\n[Einde]")
                                    while True:
                                        while True:
                                            restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                            if restart in ("1") or ("2"):
                                                break
                                            if restart == "1":
                                                print("Laten we het verhaal opnieuw spelen")
                                                time.sleep(0.8)
                                                os.system("cls")
                                                time.sleep(1)
                                                os.system("py Verhaallijn.py")
                                            elif restart == "2":
                                                print("Oke, bedankt voor het spelen. Tot ziens!")
                                                time.sleep(0.6)
                                                os.system("taskkill /IM cmd.exe")
                                            else:
                                                print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                time.sleep(0.7)
                                                os.system("cls")  
                                else:
                                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                    print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                    print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                    print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                    print("\n[Einde]")
                                    while True:
                                        while True:
                                            restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                            if restart in ("1") or ("2"):
                                                break
                                            if restart == "1":
                                                print("Laten we het verhaal opnieuw spelen")
                                                time.sleep(0.8)
                                                os.system("cls")
                                                time.sleep(1)
                                                os.system("py Verhaallijn.py")
                                            elif restart == "2":
                                                print("Oke, bedankt voor het spelen. Tot ziens!")
                                                time.sleep(0.6)
                                                os.system("taskkill /IM cmd.exe")
                                            else:
                                                print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                time.sleep(0.7)
                                                os.system("cls")   
                            else:
                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print("Je gaat niet mee met de vrouw en gaat met groep weg. Na 1 dag gezeten te hebben in Zwitserland.")
                                print("Komt er een politie naar jullie toe en die merkt zich op dat jullie hier illegaalzijn. En die neemt jullie allemaal mee naar de gevangenis")

                                print("\n[Einde]")
                                while True:
                                    while True:
                                        restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                        if restart in ("1") or ("2"):
                                            break
                                        if restart == "1":
                                            print("Laten we het verhaal opnieuw spelen")
                                            time.sleep(0.8)
                                            os.system("cls")
                                            time.sleep(1)
                                            os.system("py Verhaallijn.py")
                                        elif restart == "2":
                                            print("Oke, bedankt voor het spelen. Tot ziens!")
                                            time.sleep(0.6)
                                            os.system("taskkill /IM cmd.exe")
                                        else:
                                            print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                            time.sleep(0.7)
                                            os.system("cls")  
                    else:
                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        print("Na3 maanden daar verbleven te hebben besluit je toch maar naar Nederland te gaan. Daar gingen veel uren aan voorbij")

                        print("\nMaar omdat je hoorde dat je moeilijk in Nederland te recht komt gaf je jezelf de keuzenaar welke land je eerst wilde gaan.")
                        print("A. ...Duitsland 5")
                        print("B. ...Nederland 8")
                        antwoord22b1 = input("Maak je keuze: ")
                        if antwoord22b1 == ("A") or ("a"): 
                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            print("Eerst maar even naar Duitsland. Uren ging voorbij je komt bij de grens van Duitsland aan ze vragen om je paspoort.")
                            print("Je hebt geen geldig paspoort behalve dan de vluchtelingen formulier.")
                            print("In Duitsland is het zo dat je dan ook maanden moet gaan wacht voor dat je in dat land mag komen verblijven.")
                            print("Er gingen weer 5 maanden voorbij. Je kreeg toegang tot Duitsland je mocht er wonen. Je kreeg een verblijf aan geboden.")

                            print("\nMaar jij wilde kiezen tussen..")
                            print("A. De reis naar Nederland. 14")
                            print("B. Een verblijf in Duitsland. 7")
                            antwoord22b2 = input("Maak je keuze: ")
                            if antwoord22b2 == ("A") or ("a"):
                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print("De reis naar Nederland is begonnen. Je laat alles achter in Duitsland. En neemt je koffertje mee.")
                                print("Na een paar dagen kom je aan in op bij de grens van Nederland je mag hier niet zomaar verblijven daar heb je een verblijfsvergunning voor nodig.")
                                print("En dat duurde langer dan je had verwacht maar je ontvangt een verblijf met allerlei andere mensen uit Syrië waarbij je kan overnachten tot dat het zo ver is.")
                                print("Maar toen je daar aan kwam voelde je als een pas geboren baby zonder moeder. Je kende de taal niet je kende helemaal niks hier.")
                                print(". Alleen maar de mensen die dezelfde taal spraken. Na 5 dagen in het verblijf te hebben gezeten kwam de ijs man toevallig..")

                                print("\nJe kon kiezen tussen de ijsjes..")
                                print("A. Chocolade ijs 15")
                                print("B. Aardbei ijs 15") 
                                antwoord22b3 = input("Maak je keuze: ")
                                if antwoord22b3 == ("A") or ("a"):
                                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    print("Yammie lekker ijsje! Je hebt die al jaren niet meer gehad. Het proefden echt enorm lekker. Na zo een lange tijd.")
                                    print("Na 5 maanden ontvangen jullie een verblijfsvergunning. Je mogen hier net zo lang blijven tot dat de oorlog voorbij is in jullie land.")

                                    print("\nJe mag kiezen of je gebracht word naar het verblijf waar je mag blijven of dat je met de trein wilt…")
                                    print("A. …met de trein 18")
                                    print("B. …gebracht worden 19") 
                                    antwoord22b4 = input("Maak je keuze: ")
                                    if antwoord22b4 == ("A") or ("a"): 
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("Je neemt de trein naar je verblijf. Eindelijk! De plek waar je enorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                                        print("\n Je mag kiezen welke behang je doet in je kamer…")
                                        print("A. roze behang 21")
                                        print("B. blauw behang 21")   
                                        antwoord22b5 = input("Maak je keuze: ")
                                        if antwoord22b5 == ("A") or ("a"):
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                            print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                            print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                            print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                            print("\n[Einde]")
                                            while True:
                                                while True:
                                                    restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                    if restart in ("1") or ("2"):
                                                        break
                                                    if restart == "1":
                                                        print("Laten we het verhaal opnieuw spelen")
                                                        time.sleep(0.8)
                                                        os.system("cls")
                                                        time.sleep(1)
                                                        os.system("py Verhaallijn.py")
                                                    elif restart == "2":
                                                        print("Oke, bedankt voor het spelen. Tot ziens!")
                                                        time.sleep(0.6)
                                                        os.system("taskkill /IM cmd.exe")
                                                    else:
                                                        print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                        time.sleep(0.7)
                                                        os.system("cls")
                                        else:
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                            print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                            print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                            print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                            print("\n[Einde]")
                                            while True:
                                                while True:
                                                    restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                    if restart in ("1") or ("2"):
                                                        break
                                                    if restart == "1":
                                                        print("Laten we het verhaal opnieuw spelen")
                                                        time.sleep(0.8)
                                                        os.system("cls")
                                                        time.sleep(1)
                                                        os.system("py Verhaallijn.py")
                                                    elif restart == "2":
                                                        print("Oke, bedankt voor het spelen. Tot ziens!")
                                                        time.sleep(0.6)
                                                        os.system("taskkill /IM cmd.exe")
                                                    else:
                                                        print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                        time.sleep(0.7)
                                                        os.system("cls")
                                    else:
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("Je word gebracht. Eindelijk! De plek waarjeenorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                                        print("\nJe mag kiezen welke behang je doet in je kamer...")
                                        print("A. ...roze behang 21")
                                        print("B. ...blauw behang 21") 
                                        antwoord22b6 = input("Maak je keuze: ")
                                        if antwoord22b6 == ("A") or ("a"):
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                            print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                            print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                            print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                            print("\n[Einde]")
                                            while True:
                                                while True:
                                                    restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                    if restart in ("1") or ("2"):
                                                        break
                                                    if restart == "1":
                                                        print("Laten we het verhaal opnieuw spelen")
                                                        time.sleep(0.8)
                                                        os.system("cls")
                                                        time.sleep(1)
                                                        os.system("py Verhaallijn.py")
                                                    elif restart == "2":
                                                        print("Oke, bedankt voor het spelen. Tot ziens!")
                                                        time.sleep(0.6)
                                                        os.system("taskkill /IM cmd.exe")
                                                    else:
                                                        print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                        time.sleep(0.7)
                                                        os.system("cls")
                                        else:
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                            print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                            print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                            print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                            print("\n[Einde]")
                                            while True:
                                                while True:
                                                    restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                    if restart in ("1") or ("2"):
                                                        break
                                                    if restart == "1":
                                                        print("Laten we het verhaal opnieuw spelen")
                                                        time.sleep(0.8)
                                                        os.system("cls")
                                                        time.sleep(1)
                                                        os.system("py Verhaallijn.py")
                                                    elif restart == "2":
                                                        print("Oke, bedankt voor het spelen. Tot ziens!")
                                                        time.sleep(0.6)
                                                        os.system("taskkill /IM cmd.exe")
                                                    else:
                                                        print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                        time.sleep(0.7)
                                                        os.system("cls")
                                else:
                                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    print("Yammie lekker ijsje! Je hebt die al jaren niet meer gehad. Het proefden echt enorm lekker. Na zo een lange tijd.")
                                    print("Na 5 maanden ontvangen jullie een verblijfsvergunning. Je mogen hier net zo lang blijven tot dat de oorlog voorbij is in jullie land.")

                                    print("\nJe mag kiezen of je gebracht word naar het verblijf waar je mag blijven of dat je met de trein wilt…")
                                    print("A. …met de trein 18")
                                    print("B. …gebracht worden 19") 
                                    antwoord22b7 = input("Maak je keuze: ")
                                    if antwoord22b7 == ("A") or ("a"): 
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("Je neemt de trein naar je verblijf. Eindelijk! De plek waar je enorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                                        print("\n Je mag kiezen welke behang je doet in je kamer…")
                                        print("A. roze behang 21")
                                        print("B. blauw behang 21")   
                                        antwoord22b8 = input("Maak je keuze: ")
                                        if antwoord22b8 == ("A") or ("a"):
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                            print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                            print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                            print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                            print("\n[Einde]")
                                            while True:
                                                while True:
                                                    restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                    if restart in ("1") or ("2"):
                                                        break
                                                    if restart == "1":
                                                        print("Laten we het verhaal opnieuw spelen")
                                                        time.sleep(0.8)
                                                        os.system("cls")
                                                        time.sleep(1)
                                                        os.system("py Verhaallijn.py")
                                                    elif restart == "2":
                                                        print("Oke, bedankt voor het spelen. Tot ziens!")
                                                        time.sleep(0.6)
                                                        os.system("taskkill /IM cmd.exe")
                                                    else:
                                                        print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                        time.sleep(0.7)
                                                        os.system("cls")
                                        else:
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                            print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                            print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                            print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                            print("\n[Einde]")
                                            while True:
                                                while True:
                                                    restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                    if restart in ("1") or ("2"):
                                                        break
                                                    if restart == "1":
                                                        print("Laten we het verhaal opnieuw spelen")
                                                        time.sleep(0.8)
                                                        os.system("cls")
                                                        time.sleep(1)
                                                        os.system("py Verhaallijn.py")
                                                    elif restart == "2":
                                                        print("Oke, bedankt voor het spelen. Tot ziens!")
                                                        time.sleep(0.6)
                                                        os.system("taskkill /IM cmd.exe")
                                                    else:
                                                        print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                        time.sleep(0.7)
                                                        os.system("cls")
                                    else:
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("Je word gebracht. Eindelijk! De plek waarjeenorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                                        print("\nJe mag kiezen welke behang je doet in je kamer...")
                                        print("A. ...roze behang 21")
                                        print("B. ...blauw behang 21") 
                                        antwoord22b9 = input("Maak je keuze: ")
                                        if antwoord22b9 == ("A") or ("a"):
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                            print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                            print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                            print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                            print("\n[Einde]")
                                            while True:
                                                while True:
                                                    restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                    if restart in ("1") or ("2"):
                                                        break
                                                    if restart == "1":
                                                        print("Laten we het verhaal opnieuw spelen")
                                                        time.sleep(0.8)
                                                        os.system("cls")
                                                        time.sleep(1)
                                                        os.system("py Verhaallijn.py")
                                                    elif restart == "2":
                                                        print("Oke, bedankt voor het spelen. Tot ziens!")
                                                        time.sleep(0.6)
                                                        os.system("taskkill /IM cmd.exe")
                                                    else:
                                                        print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                        time.sleep(0.7)
                                                        os.system("cls")
                                        else:
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                            print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                            print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                            print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                            print("\n[Einde]")
                                            while True:
                                                while True:
                                                    restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                    if restart in ("1") or ("2"):
                                                        break
                                                    if restart == "1":
                                                        print("Laten we het verhaal opnieuw spelen")
                                                        time.sleep(0.8)
                                                        os.system("cls")
                                                        time.sleep(1)
                                                        os.system("py Verhaallijn.py")
                                                    elif restart == "2":
                                                        print("Oke, bedankt voor het spelen. Tot ziens!")
                                                        time.sleep(0.6)
                                                        os.system("taskkill /IM cmd.exe")
                                                    else:
                                                        print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                        time.sleep(0.7)
                                                        os.system("cls")
                            else:
                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print("Het huisje in Duitsland. Je wilde eerst daar de taal kennen. Effe tot rust komen en dan later de reis te gemoed komen naar Nederland.")
                                print("Daar ging 2 jaar over heen.Je wilde weg hier je wilde naar Nederland.")

                                print("\nJe kon kiezen tussen..")
                                print("A. ...met de trein gaan. 14")
                                print("B. ...lopend naar Nederland want dat was niet zo ver. 14") 
                                antwoord22aa = input("Maak je keuze: ")
                                if antwoord22aa == ("A") or ("a"):
                                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    print("De reis naar Nederland is begonnen. Je laat alles achter in Duitsland. En neemt je koffertje mee.")
                                    print("Na een paar dagen kom je aan in op bij de grens van Nederland je mag hier niet zomaar verblijven daar heb je een verblijfsvergunning voor nodig.")
                                    print("En dat duurde langer dan je had verwacht maar je ontvangt een verblijf met allerlei andere mensen uit Syrië waarbij je kan overnachten tot dat het zo ver is.")
                                    print("Maar toen je daar aan kwam voelde je als een pas geboren baby zonder moeder. Je kende de taal niet je kende helemaal niks hier.")
                                    print(". Alleen maar de mensen die dezelfde taal spraken. Na 5 dagen in het verblijf te hebben gezeten kwam de ijs man toevallig..")

                                    print("\nJe kon kiezen tussen de ijsjes..")
                                    print("A. Chocolade ijs 15")
                                    print("B. Aardbei ijs 15") 
                                    antwoord22bb = input("Maak je keuze: ")
                                    if antwoord22bb == ("A") or ("a"):
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("Yammie lekker ijsje! Je hebt die al jaren niet meer gehad. Het proefden echt enorm lekker. Na zo een lange tijd.")
                                        print("Na 5 maanden ontvangen jullie een verblijfsvergunning. Je mogen hier net zo lang blijven tot dat de oorlog voorbij is in jullie land.")

                                        print("\nJe mag kiezen of je gebracht word naar het verblijf waar je mag blijven of dat je met de trein wilt…")
                                        print("A. …met de trein 18")
                                        print("B. …gebracht worden 19") 
                                        antwoord22bbb = input("Maak je keuze: ")
                                        if antwoord22bbb == ("A") or ("a"): 
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("Je neemt de trein naar je verblijf. Eindelijk! De plek waar je enorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                                            print("\n Je mag kiezen welke behang je doet in je kamer…")
                                            print("A. roze behang 21")
                                            print("B. blauw behang 21")   
                                            antwoord22bbbb = input("Maak je keuze: ")
                                            if antwoord22bbbb == ("A") or ("a"):
                                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                                print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                                print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                                print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                                print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                                print("\n[Einde]")
                                                while True:
                                                    while True:
                                                        restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                        if restart in ("1") or ("2"):
                                                            break
                                                        if restart == "1":
                                                            print("Laten we het verhaal opnieuw spelen")
                                                            time.sleep(0.8)
                                                            os.system("cls")
                                                            time.sleep(1)
                                                            os.system("py Verhaallijn.py")
                                                        elif restart == "2":
                                                            print("Oke, bedankt voor het spelen. Tot ziens!")
                                                            time.sleep(0.6)
                                                            os.system("taskkill /IM cmd.exe")
                                                        else:
                                                            print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                            time.sleep(0.7)
                                                            os.system("cls")
                                            else:
                                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                                print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                                print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                                print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                                print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                                print("\n[Einde]")
                                                while True:
                                                    while True:
                                                        restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                        if restart in ("1") or ("2"):
                                                            break
                                                        if restart == "1":
                                                            print("Laten we het verhaal opnieuw spelen")
                                                            time.sleep(0.8)
                                                            os.system("cls")
                                                            time.sleep(1)
                                                            os.system("py Verhaallijn.py")
                                                        elif restart == "2":
                                                            print("Oke, bedankt voor het spelen. Tot ziens!")
                                                            time.sleep(0.6)
                                                            os.system("taskkill /IM cmd.exe")
                                                        else:
                                                            print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                            time.sleep(0.7)
                                                            os.system("cls")
                                        else:
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("Je word gebracht. Eindelijk! De plek waarjeenorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                                            print("\nJe mag kiezen welke behang je doet in je kamer...")
                                            print("A. ...roze behang 21")
                                            print("B. ...blauw behang 21") 
                                            antwoord22b6b = input("Maak je keuze: ")
                                            if antwoord22b6b == ("A") or ("a"):
                                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                                print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                                print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                                print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                                print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                                print("\n[Einde]")
                                                while True:
                                                    while True:
                                                        restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                        if restart in ("1") or ("2"):
                                                            break
                                                        if restart == "1":
                                                            print("Laten we het verhaal opnieuw spelen")
                                                            time.sleep(0.8)
                                                            os.system("cls")
                                                            time.sleep(1)
                                                            os.system("py Verhaallijn.py")
                                                        elif restart == "2":
                                                            print("Oke, bedankt voor het spelen. Tot ziens!")
                                                            time.sleep(0.6)
                                                            os.system("taskkill /IM cmd.exe")
                                                        else:
                                                            print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                            time.sleep(0.7)
                                                            os.system("cls")
                                            else:
                                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                                print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                                print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                                print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                                print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                                print("\n[Einde]")
                                                while True:
                                                    while True:
                                                        restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                        if restart in ("1") or ("2"):
                                                            break
                                                        if restart == "1":
                                                            print("Laten we het verhaal opnieuw spelen")
                                                            time.sleep(0.8)
                                                            os.system("cls")
                                                            time.sleep(1)
                                                            os.system("py Verhaallijn.py")
                                                        elif restart == "2":
                                                            print("Oke, bedankt voor het spelen. Tot ziens!")
                                                            time.sleep(0.6)
                                                            os.system("taskkill /IM cmd.exe")
                                                        else:
                                                            print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                            time.sleep(0.7)
                                                            os.system("cls")
                                    else:
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("Yammie lekker ijsje! Je hebt die al jaren niet meer gehad. Het proefden echt enorm lekker. Na zo een lange tijd.")
                                        print("Na 5 maanden ontvangen jullie een verblijfsvergunning. Je mogen hier net zo lang blijven tot dat de oorlog voorbij is in jullie land.")

                                        print("\nJe mag kiezen of je gebracht word naar het verblijf waar je mag blijven of dat je met de trein wilt…")
                                        print("A. …met de trein 18")
                                        print("B. …gebracht worden 19") 
                                        antwoord22b7b = input("Maak je keuze: ")
                                        if antwoord22b7b == ("A") or ("a"): 
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("Je neemt de trein naar je verblijf. Eindelijk! De plek waar je enorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                                            print("\n Je mag kiezen welke behang je doet in je kamer…")
                                            print("A. roze behang 21")
                                            print("B. blauw behang 21")   
                                            antwoord22b8b = input("Maak je keuze: ")
                                            if antwoord22b8b == ("A") or ("a"):
                                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                                print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                                print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                                print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                                print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                                print("\n[Einde]")
                                                while True:
                                                    while True:
                                                        restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                        if restart in ("1") or ("2"):
                                                            break
                                                        if restart == "1":
                                                            print("Laten we het verhaal opnieuw spelen")
                                                            time.sleep(0.8)
                                                            os.system("cls")
                                                            time.sleep(1)
                                                            os.system("py Verhaallijn.py")
                                                        elif restart == "2":
                                                            print("Oke, bedankt voor het spelen. Tot ziens!")
                                                            time.sleep(0.6)
                                                            os.system("taskkill /IM cmd.exe")
                                                        else:
                                                            print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                            time.sleep(0.7)
                                                            os.system("cls")
                                            else:
                                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                                print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                                print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                                print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                                print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                                print("\n[Einde]")
                                                while True:
                                                    while True:
                                                        restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                        if restart in ("1") or ("2"):
                                                            break
                                                        if restart == "1":
                                                            print("Laten we het verhaal opnieuw spelen")
                                                            time.sleep(0.8)
                                                            os.system("cls")
                                                            time.sleep(1)
                                                            os.system("py Verhaallijn.py")
                                                        elif restart == "2":
                                                            print("Oke, bedankt voor het spelen. Tot ziens!")
                                                            time.sleep(0.6)
                                                            os.system("taskkill /IM cmd.exe")
                                                        else:
                                                            print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                            time.sleep(0.7)
                                                            os.system("cls")
                                        else:
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("Je word gebracht. Eindelijk! De plek waarjeenorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                                            print("\nJe mag kiezen welke behang je doet in je kamer...")
                                            print("A. ...roze behang 21")
                                            print("B. ...blauw behang 21") 
                                            antwoord22b9b = input("Maak je keuze: ")
                                            if antwoord22b9b == ("A") or ("a"):
                                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                                print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                                print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                                print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                                print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                                print("\n[Einde]")
                                                while True:
                                                    while True:
                                                        restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                        if restart in ("1") or ("2"):
                                                            break
                                                        if restart == "1":
                                                            print("Laten we het verhaal opnieuw spelen")
                                                            time.sleep(0.8)
                                                            os.system("cls")
                                                            time.sleep(1)
                                                            os.system("py Verhaallijn.py")
                                                        elif restart == "2":
                                                            print("Oke, bedankt voor het spelen. Tot ziens!")
                                                            time.sleep(0.6)
                                                            os.system("taskkill /IM cmd.exe")
                                                        else:
                                                            print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                            time.sleep(0.7)
                                                            os.system("cls")
                                            else:
                                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                                print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                                print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                                print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                                print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                                print("\n[Einde]")
                                                while True:
                                                    while True:
                                                        restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                        if restart in ("1") or ("2"):
                                                            break
                                                        if restart == "1":
                                                            print("Laten we het verhaal opnieuw spelen")
                                                            time.sleep(0.8)
                                                            os.system("cls")
                                                            time.sleep(1)
                                                            os.system("py Verhaallijn.py")
                                                        elif restart == "2":
                                                            print("Oke, bedankt voor het spelen. Tot ziens!")
                                                            time.sleep(0.6)
                                                            os.system("taskkill /IM cmd.exe")
                                                        else:
                                                            print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                            time.sleep(0.7)
                                                            os.system("cls")
                        else:
                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            print("Op naar Nederland!De reis is enorm lastig om vanaf hier‘Italië’naarNederland te gaan.Dagen gingen voorbij. Je komt aan na 5 dagen lopen in Zwitserlandaan.")
                            print("Je ontmoet iemand die alleen de kinderen willen mee nemen naar België en die persoon zoulater dan de volwassen meenemen als ze hier wachten op haar.")
                            print("Ze wilt namelijk graag de kinderen helpen en ze snel opweg nemen naar iets veiligs en ze wist iemand waar hunuit eindelijkkonden verblijven.")

                            print("\nJij kiest ervoor om...")
                            print("A. ...mee te gaan 16")
                            print("B. ...niet mee te gaan 17")
                            antwoord22b10 = input("Maak je keuze: ")
                            if antwoord22b10 == ("A") or ("a"):
                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print("Je neemt de trein naar je verblijf. Eindelijk! De plek waar je enorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                                print("\n Je mag kiezen welke behang je doet in je kamer…")
                                print("A. roze behang 21")
                                print("B. blauw behang 21")
                                antwoord22b11 = input("Maak je keuze: ")
                                if antwoord22b11 == ("A") or ("a"):
                                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                    print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                    print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                    print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                    print("\n[Einde]")
                                    while True:
                                        while True:
                                            restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                            if restart in ("1") or ("2"):
                                                break
                                            if restart == "1":
                                                print("Laten we het verhaal opnieuw spelen")
                                                time.sleep(0.8)
                                                os.system("cls")
                                                time.sleep(1)
                                                os.system("py Verhaallijn.py")
                                            elif restart == "2":
                                                print("Oke, bedankt voor het spelen. Tot ziens!")
                                                time.sleep(0.6)
                                                os.system("taskkill /IM cmd.exe")
                                            else:
                                                print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                time.sleep(0.7)
                                                os.system("cls")
                                else:
                                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                    print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                    print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                    print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                    print("\n[Einde]")
                                    while True:
                                        while True:
                                            restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                            if restart in ("1") or ("2"):
                                                break
                                            if restart == "1":
                                                print("Laten we het verhaal opnieuw spelen")
                                                time.sleep(0.8)
                                                os.system("cls")
                                                time.sleep(1)
                                                os.system("py Verhaallijn.py")
                                            elif restart == "2":
                                                print("Oke, bedankt voor het spelen. Tot ziens!")
                                                time.sleep(0.6)
                                                os.system("taskkill /IM cmd.exe")
                                            else:
                                                print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                time.sleep(0.7)
                                                os.system("cls")   
                            else:
                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print("Je gaat niet mee met de vrouw en gaat met groep weg. Na 1 dag gezeten te hebben in Zwitserland.")
                                print("Komt er een politie naar jullie toe en die merkt zich op dat jullie hier illegaalzijn. En die neemt jullie allemaal mee naar de gevangenis")

                                print("\n[Einde]")
                                while True:
                                    while True:
                                        restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                        if restart in ("1") or ("2"):
                                            break
                                        if restart == "1":
                                            print("Laten we het verhaal opnieuw spelen")
                                            time.sleep(0.8)
                                            os.system("cls")
                                            time.sleep(1)
                                            os.system("py Verhaallijn.py")
                                        elif restart == "2":
                                            print("Oke, bedankt voor het spelen. Tot ziens!")
                                            time.sleep(0.6)
                                            os.system("taskkill /IM cmd.exe")
                                        else:
                                            print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                            time.sleep(0.7)
                                            os.system("cls") 
                else:
                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    print("Je kiest ervoor om met de boot weg tegaan. Een nadeel is alleen dat het enorm gevaarlijk grote kans dat je het niet haalt en is het enorm illegaal.")
                    print("Je ging met auto naar het water om via daar naar Europa te gaan. De boot die ze daar hadden was veelte klein voor ons allemaal.")
                    print("Als de boot zo omslaan zouden we allemaal dood gaan niemand van ons had leren zwemmen en ik kon dat al helemaal niet ik ben bang voor water..")
                    print("En daar moesten we 1 dag zitten... Veelte eng!De kinderen moest voorin en de ouderen achterin op elkaar.")
                    print("Na 10 uur op elkaar moest iedereen een beetje bewegen de boot bewoog zo ergdat alle mensen aan de rechte kan ging zitten waardoor de boot omsloeg...")

                    print("\n[Einde]")
                    while True:
                        while True:
                            restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                            if restart in ("1") or ("2"):
                                break
                            if restart == "1":
                                print("Laten we het verhaal opnieuw spelen")
                                time.sleep(0.8)
                                os.system("cls")
                                time.sleep(1)
                                os.system("py Verhaallijn.py")
                            elif restart == "2":
                                print("Oke, bedankt voor het spelen. Tot ziens!")
                                time.sleep(0.6)
                                os.system("taskkill /IM cmd.exe")
                            else:
                                print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                time.sleep(0.7)
                                os.system("cls") 
        else:
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("Je besluit om toch naar je beste vriendin haar huis te gaan. Na 20 min te hebben gelopen kom je aan bij haar huis ze was er nog niet? Je bekijkt je telefoon je ziet dat het pas 5 voor 7 is. Nog 5 min?")
            print("Niks voor haar om zo perfect op tijd te komen. Het is 10 over 7.. Ze is er nog steeds niet?? Waar blijft ze? ")
            print("Je hoort ineens een keiharde knal waar je enorm van schrikt en er van op de grondvalt. Je weet niet wat je over komt.")
            print("Wat is dit? Je rent naar huis. Maar voor dat je dat kon doen viel er enorm veel puin op je. Je kon geen kant op.")
            print("Je hoort geschreeuw. Je hoort mensen schieten? Wat gebeurt hier?? Je roep keihard help.")
            print("Niemand hoorde je. Je telefoon was kapot gegaan van toen je net gevallen was. Hoe nu? De puin komt steeds een steeds dichterbij... *Klets*")

            print("\n[Einde]")
            while True:
                while True:
                    restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                    if restart in ("1") or ("2"):
                        break
                    if restart == "1":
                        print("Laten we het verhaal opnieuw spelen")
                        time.sleep(0.8)
                        os.system("cls")
                        time.sleep(1)
                        os.system("py Verhaallijn.py")
                    elif restart == "2":
                        print("Oke, bedankt voor het spelen. Tot ziens!")
                        time.sleep(0.6)
                        os.system("taskkill /IM cmd.exe")
                    else:
                        print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                        time.sleep(0.7)
                        os.system("cls")   
else:
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Je besluit om toch mee te gaan met je ouders en familie. Je vind dat familie altijd boven aan staat en daarom je familie nooit kan teleurstellen.")
    print("Het is al laat, je bent al de hele avond aan het bedenken hoe je beste vriendin moet gaan vertellen dat je niet mag komen.")
    print("Daar ben je erg verdrietig om. Je gaat verdrietig naar boven… Naar je eigenkamer.")
    print("Je maakte je klaar voor dat je naar bed wilt gaan. Terwijl je bezig was met het tanden poetsen krijg je een bericht van je beste vriendin.")
    print("Ze verteld je dat ze dit weekend niet komt wegens redenen waar ze absoluut niet over mocht praten van haar ouders.")
    print("Ze vraagt je of je morgen ochtend voor 7 uur in de ochtend nog naar de speeltuin kan komen.")

    print("\n En jij vertelt haar...")
    print("A. ...dat je dit weekend ook niet kon komen. 9")
    print("B. ...dat je er naar uit kijkt. Tot morgen! 4")
    vraag = input("Maak je keuze: ")
    if vraag == ("A") or ("a"):
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("En je vertelt haar dat je dit weekend ook niet kon komen. Je krijgt daar geen reactie op.")
        print("Je nog steeds niks binnen. Maar je hoort wel allemaal geritsel thuis.")
        print("Je ziet je moeder en vader heel veel dingen bij elkaar aan het zoeken zijn. Je vraagt wat er aan de hand is.")
        print("Ze zeggen dat je je moet opschieten en je nu per direct je spullen bij elkaar moet zoeken.")
        print("Was het al te laat dus voor al die spullen. Je moeder en vader nemen je rennend mee in de auto.")
        print("Op weg naar de grens. Je ouders worden net om de hoek aangehouden. De mensen die je ouders aanhouden vragen waar jullie heen gaan.")
        print("Je ouders zeggen; alsjeblieft neem mijn kind mee over grens wij blijven hier.")
        print("Alsjeblieft! Jij begint enorm te huilen je weet niet wat er aan de hand is.")
        print("De mensen trekken je uit de auto en nemen je mee.")

        print("\nJij kiest ervoor om..")
        print("A. Toch met je ouders te blijven en met hun mee te gaan. 12")
        print("B. Mee te gaan met die mensen. 11")
        vraag1 = input("Maak je keuze: ")
        if vraag1 == ("A") or ("a"):
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("Jij kiest ervoor om toch te blijven met je ouders. Maar je ouder dwingen je en ze helpen je eruit.")
            print("En je word mee genomen met die mensen. Ze vertellen je dat het gevaarlijk is hier en dat je je ouders willen beschermen.")
            print("Jij vraagt wat er aan de hand is.. De kennissen van je ouders dat zijn wij en mochten niet vertellen wat er aan de hand is maar.")
            print("Er brak gisteren oorlog uit in Syrië. En dit is de laatste keer dat je je ouders ooit nog gaat zien.")
            print("Je brak van binnen je wist niest meer je was er enorm stil van en je stond zo stijf dat je maar de auto in ging van de kennissen.")
            print("De kennissen vertelde dat je word gebracht naar de grens van Europa en daar wacht een ander groep op je.")
            print("Je rijdt naar de grens van Europa waar een boot staan die je naar Italië brengt. Dat ging allemaal goed tot dat de auto bij de grens kwam van Europa.")
            print("Je hoorde mensen praten *Je kan niet in Europa zonder een geldig paspoort*.Maar jij heb die niet.")

            print("\nDe groep kon daar beslissen om..")
            print("A. …5 maanden voor de grens te wachten tot dat je een bewijs krijgt dat je in dat land mag. 1")
            print("B. …gelijk met de boot weg alleen was dat enorm gevaarlijk. Er is namelijk een grote kans dat je het niet haalt. 13")
            vraag2 = input("Maak je keuze: ")
            if vraag2 == ("A") or ("a"):
                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("Na3 maanden daar verbleven te hebben besluit je toch maar naar Nederland te gaan. Daar gingen veel uren aan voorbij")

                print("\nMaar omdat je hoorde dat je moeilijk in Nederland te recht komt gaf je jezelf de keuzenaar welke land je eerst wilde gaan.")
                print("A. ...Duitsland 5")
                print("B. ...Nederland 8")
                vraag3 = input("Maak je keuze: ")
                if vraag3 == ("A") or ("a"):
                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    print("Eerst maar even naar Duitsland. Uren ging voorbij je komt bij de grens van Duitsland aan ze vragen om je paspoort.")
                    print("Je hebt geen geldig paspoort behalve dan de vluchtelingen formulier.")
                    print("In Duitsland is het zo dat je dan ook maanden moet gaan wacht voor dat je in dat land mag komen verblijven.")
                    print("Er gingen weer 5 maanden voorbij. Je kreeg toegang tot Duitsland je mocht er wonen. Je kreeg een verblijf aan geboden.")

                    print("\nMaar jij wilde kiezen tussen..")
                    print("A. De reis naar Nederland. 14")
                    print("B. Een verblijf in Duitsland. 7")
                    vraag4 = input("Maak je keuze: ")
                    if vraag4 == ("A") or ("a"):
                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        print("De reis naar Nederland is begonnen. Je laat alles achter in Duitsland. En neemt je koffertje mee.")
                        print("Na een paar dagen kom je aan in op bij de grens van Nederland je mag hier niet zomaar verblijven daar heb je een verblijfsvergunning voor nodig.")
                        print("En dat duurde langer dan je had verwacht maar je ontvangt een verblijf met allerlei andere mensen uit Syrië waarbij je kan overnachten tot dat het zo ver is.")
                        print("Maar toen je daar aan kwam voelde je als een pas geboren baby zonder moeder. Je kende de taal niet je kende helemaal niks hier.")
                        print(". Alleen maar de mensen die dezelfde taal spraken. Na 5 dagen in het verblijf te hebben gezeten kwam de ijs man toevallig..")

                        print("\nJe kon kiezen tussen de ijsjes..")
                        print("A. Chocolade ijs 15")
                        print("B. Aardbei ijs 15")
                        vraag5 = input("Maak je keuze: ")
                        if vraag5 == ("A") or ("a"):
                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            print("Yammie lekker ijsje! Je hebt die al jaren niet meer gehad. Het proefden echt enorm lekker. Na zo een lange tijd.")
                            print("Na 5 maanden ontvangen jullie een verblijfsvergunning. Je mogen hier net zo lang blijven tot dat de oorlog voorbij is in jullie land.")

                            print("\nJe mag kiezen of je gebracht word naar het verblijf waar je mag blijven of dat je met de trein wilt…")
                            print("A. …met de trein 18")
                            print("B. …gebracht worden 19")
                            vraag6 = input("Maak je keuze: ")
                            if vraag6 == ("A") or ("a"):
                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print("Je neemt de trein naar je verblijf. Eindelijk! De plek waar je enorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                                print("\n Je mag kiezen welke behang je doet in je kamer…")
                                print("A. roze behang 21")
                                print("B. blauw behang 21")
                                vraag7 = input("Maak je keuze: ")
                                if vraag7 == ("A") or ("a"):
                                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                    print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                    print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                    print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                    print("\n[Einde]")
                                    while True:
                                        while True:
                                            restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                            if restart in ("1") or ("2"):
                                                break
                                            if restart == "1":
                                                print("Laten we het verhaal opnieuw spelen")
                                                time.sleep(0.8)
                                                os.system("cls")
                                                time.sleep(1)
                                                os.system("py Verhaallijn.py")
                                            elif restart == "2":
                                                print("Oke, bedankt voor het spelen. Tot ziens!")
                                                time.sleep(0.6)
                                                os.system("taskkill /IM cmd.exe")
                                            else:
                                                print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                time.sleep(0.7)
                                                os.system("cls")
                                else:
                                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                    print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                    print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                    print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                    print("\n[Einde]")
                                    while True:
                                        while True:
                                            restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                            if restart in ("1") or ("2"):
                                                break
                                            if restart == "1":
                                                print("Laten we het verhaal opnieuw spelen")
                                                time.sleep(0.8)
                                                os.system("cls")
                                                time.sleep(1)
                                                os.system("py Verhaallijn.py")
                                            elif restart == "2":
                                                print("Oke, bedankt voor het spelen. Tot ziens!")
                                                time.sleep(0.6)
                                                os.system("taskkill /IM cmd.exe")
                                            else:
                                                print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                time.sleep(0.7)
                                                os.system("cls")   
                            else:
                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print("Je word gebracht. Eindelijk! De plek waarjeenorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                                print("\nJe mag kiezen welke behang je doet in je kamer...")
                                print("A. ...roze behang 21")
                                print("B. ...blauw behang 21")
                                vraag6a = input("Maak je keuze: ")
                                if vraag6a == ("A") or ("a"):
                                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                    print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                    print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                    print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                    print("\n[Einde]")
                                    while True:
                                        while True:
                                            restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                            if restart in ("1") or ("2"):
                                                break
                                            if restart == "1":
                                                print("Laten we het verhaal opnieuw spelen")
                                                time.sleep(0.8)
                                                os.system("cls")
                                                time.sleep(1)
                                                os.system("py Verhaallijn.py")
                                            elif restart == "2":
                                                print("Oke, bedankt voor het spelen. Tot ziens!")
                                                time.sleep(0.6)
                                                os.system("taskkill /IM cmd.exe")
                                            else:
                                                print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                time.sleep(0.7)
                                                os.system("cls")
                                else:
                                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                    print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                    print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                    print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                    print("\n[Einde]")
                                    while True:
                                        while True:
                                            restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                            if restart in ("1") or ("2"):
                                                break
                                            if restart == "1":
                                                print("Laten we het verhaal opnieuw spelen")
                                                time.sleep(0.8)
                                                os.system("cls")
                                                time.sleep(1)
                                                os.system("py Verhaallijn.py")
                                            elif restart == "2":
                                                print("Oke, bedankt voor het spelen. Tot ziens!")
                                                time.sleep(0.6)
                                                os.system("taskkill /IM cmd.exe")
                                            else:
                                                print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                time.sleep(0.7)
                                                os.system("cls")
                        else:
                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            print("Yammie lekker ijsje! Je hebt die al jaren niet meer gehad. Het proefden echt enorm lekker. Na zo een lange tijd.")
                            print("Na 5 maanden ontvangen jullie een verblijfsvergunning. Je mogen hier net zo lang blijven tot dat de oorlog voorbij is in jullie land.")

                            print("\nJe mag kiezen of je gebracht word naar het verblijf waar je mag blijven of dat je met de trein wilt…")
                            print("A. …met de trein 18")
                            print("B. …gebracht worden 19")
                            vraag5a = input("Maak je keuze: ")
                            if vraag5a == ("A") or ("a"):
                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print("Je neemt de trein naar je verblijf. Eindelijk! De plek waar je enorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                                print("\n Je mag kiezen welke behang je doet in je kamer…")
                                print("A. roze behang 21")
                                print("B. blauw behang 21")
                                vraag5b = input("Maak je keuze: ")
                                if vraag5b == ("A") or ("a"):
                                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                    print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                    print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                    print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                    print("\n[Einde]")
                                    while True:
                                        while True:
                                            restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                            if restart in ("1") or ("2"):
                                                break
                                            if restart == "1":
                                                print("Laten we het verhaal opnieuw spelen")
                                                time.sleep(0.8)
                                                os.system("cls")
                                                time.sleep(1)
                                                os.system("py Verhaallijn.py")
                                            elif restart == "2":
                                                print("Oke, bedankt voor het spelen. Tot ziens!")
                                                time.sleep(0.6)
                                                os.system("taskkill /IM cmd.exe")
                                            else:
                                                print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                time.sleep(0.7)
                                                os.system("cls")
                                else:
                                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                    print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                    print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                    print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                    print("\n[Einde]")
                                    while True:
                                        while True:
                                            restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                            if restart in ("1") or ("2"):
                                                break
                                            if restart == "1":
                                                print("Laten we het verhaal opnieuw spelen")
                                                time.sleep(0.8)
                                                os.system("cls")
                                                time.sleep(1)
                                                os.system("py Verhaallijn.py")
                                            elif restart == "2":
                                                print("Oke, bedankt voor het spelen. Tot ziens!")
                                                time.sleep(0.6)
                                                os.system("taskkill /IM cmd.exe")
                                            else:
                                                print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                time.sleep(0.7)
                                                os.system("cls")   
                            else:
                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print("Je word gebracht. Eindelijk! De plek waarjeenorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                                print("\nJe mag kiezen welke behang je doet in je kamer...")
                                print("A. ...roze behang 21")
                                print("B. ...blauw behang 21")
                                vraag7c = input("Maak je keuze: ")
                                if vraag7c == ("A") or ("a"):
                                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                    print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                    print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                    print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                    print("\n[Einde]")
                                    while True:
                                        while True:
                                            restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                            if restart in ("1") or ("2"):
                                                break
                                            if restart == "1":
                                                print("Laten we het verhaal opnieuw spelen")
                                                time.sleep(0.8)
                                                os.system("cls")
                                                time.sleep(1)
                                                os.system("py Verhaallijn.py")
                                            elif restart == "2":
                                                print("Oke, bedankt voor het spelen. Tot ziens!")
                                                time.sleep(0.6)
                                                os.system("taskkill /IM cmd.exe")
                                            else:
                                                print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                time.sleep(0.7)
                                                os.system("cls")
                                else:
                                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                    print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                    print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                    print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                    print("\n[Einde]")
                                    while True:
                                        while True:
                                            restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                            if restart in ("1") or ("2"):
                                                break
                                            if restart == "1":
                                                print("Laten we het verhaal opnieuw spelen")
                                                time.sleep(0.8)
                                                os.system("cls")
                                                time.sleep(1)
                                                os.system("py Verhaallijn.py")
                                            elif restart == "2":
                                                print("Oke, bedankt voor het spelen. Tot ziens!")
                                                time.sleep(0.6)
                                                os.system("taskkill /IM cmd.exe")
                                            else:
                                                print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                time.sleep(0.7)
                                                os.system("cls")
                    else:
                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        print("Het huisje in Duitsland. Je wilde eerst daar de taal kennen. Effe tot rust komen en dan later de reis te gemoed komen naar Nederland.")
                        print("Daar ging 2 jaar over heen.Je wilde weg hier je wilde naar Nederland.")

                        print("\nJe kon kiezen tussen..")
                        print("A. ...met de trein gaan. 14")
                        print("B. ...lopend naar Nederland want dat was niet zo ver. 14")
                        vraag4a = input("Maak je keuze: ")
                        if vraag4a == ("A") or ("a"):  
                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            print("De reis naar Nederland is begonnen. Je laat alles achter in Duitsland. En neemt je koffertje mee.")
                            print("Na een paar dagen kom je aan in op bij de grens van Nederland je mag hier niet zomaar verblijven daar heb je een verblijfsvergunning voor nodig.")
                            print("En dat duurde langer dan je had verwacht maar je ontvangt een verblijf met allerlei andere mensen uit Syrië waarbij je kan overnachten tot dat het zo ver is.")
                            print("Maar toen je daar aan kwam voelde je als een pas geboren baby zonder moeder. Je kende de taal niet je kende helemaal niks hier.")
                            print(". Alleen maar de mensen die dezelfde taal spraken. Na 5 dagen in het verblijf te hebben gezeten kwam de ijs man toevallig..")

                            print("\nJe kon kiezen tussen de ijsjes..")
                            print("A. Chocolade ijs 15")
                            print("B. Aardbei ijs 15")
                            vraag4b = input("Maak je keuze: ")
                            if vraag4b == ("A") or ("a"): 
                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print("Yammie lekker ijsje! Je hebt die al jaren niet meer gehad. Het proefden echt enorm lekker. Na zo een lange tijd.")
                                print("Na 5 maanden ontvangen jullie een verblijfsvergunning. Je mogen hier net zo lang blijven tot dat de oorlog voorbij is in jullie land.")

                                print("\nJe mag kiezen of je gebracht word naar het verblijf waar je mag blijven of dat je met de trein wilt…")
                                print("A. …met de trein 18")
                                print("B. …gebracht worden 19")
                                vraag4c = input("Maak je keuze: ")
                                if vraag4c == ("A") or ("a"):
                                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    print("Je neemt de trein naar je verblijf. Eindelijk! De plek waar je enorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                                    print("\n Je mag kiezen welke behang je doet in je kamer…")
                                    print("A. roze behang 21")
                                    print("B. blauw behang 21")
                                    vraag4d = input("Maak je keuze: ")
                                    if vraag4d == ("A") or ("a"):
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                        print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                        print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                        print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                        print("\n[Einde]")
                                        while True:
                                            while True:
                                                restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                if restart in ("1") or ("2"):
                                                    break
                                                if restart == "1":
                                                    print("Laten we het verhaal opnieuw spelen")
                                                    time.sleep(0.8)
                                                    os.system("cls")
                                                    time.sleep(1)
                                                    os.system("py Verhaallijn.py")
                                                elif restart == "2":
                                                    print("Oke, bedankt voor het spelen. Tot ziens!")
                                                    time.sleep(0.6)
                                                    os.system("taskkill /IM cmd.exe")
                                                else:
                                                    print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                    time.sleep(0.7)
                                                    os.system("cls")
                                    else:
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                        print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                        print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                        print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                        print("\n[Einde]")
                                        while True:
                                            while True:
                                                restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                if restart in ("1") or ("2"):
                                                    break
                                                if restart == "1":
                                                    print("Laten we het verhaal opnieuw spelen")
                                                    time.sleep(0.8)
                                                    os.system("cls")
                                                    time.sleep(1)
                                                    os.system("py Verhaallijn.py")
                                                elif restart == "2":
                                                    print("Oke, bedankt voor het spelen. Tot ziens!")
                                                    time.sleep(0.6)
                                                    os.system("taskkill /IM cmd.exe")
                                                else:
                                                    print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                    time.sleep(0.7)
                                                    os.system("cls")   
                                else:
                                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    print("Je word gebracht. Eindelijk! De plek waarjeenorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                                    print("\nJe mag kiezen welke behang je doet in je kamer...")
                                    print("A. ...roze behang 21")
                                    print("B. ...blauw behang 21")
                                    vraag4e = input("Maak je keuze: ")
                                    if vraag4e == ("A") or ("a"):
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                        print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                        print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                        print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                        print("\n[Einde]")
                                        while True:
                                            while True:
                                                restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                if restart in ("1") or ("2"):
                                                    break
                                                if restart == "1":
                                                    print("Laten we het verhaal opnieuw spelen")
                                                    time.sleep(0.8)
                                                    os.system("cls")
                                                    time.sleep(1)
                                                    os.system("py Verhaallijn.py")
                                                elif restart == "2":
                                                    print("Oke, bedankt voor het spelen. Tot ziens!")
                                                    time.sleep(0.6)
                                                    os.system("taskkill /IM cmd.exe")
                                                else:
                                                    print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                    time.sleep(0.7)
                                                    os.system("cls")
                                    else:
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                        print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                        print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                        print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                        print("\n[Einde]")
                                        while True:
                                            while True:
                                                restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                if restart in ("1") or ("2"):
                                                    break
                                                if restart == "1":
                                                    print("Laten we het verhaal opnieuw spelen")
                                                    time.sleep(0.8)
                                                    os.system("cls")
                                                    time.sleep(1)
                                                    os.system("py Verhaallijn.py")
                                                elif restart == "2":
                                                    print("Oke, bedankt voor het spelen. Tot ziens!")
                                                    time.sleep(0.6)
                                                    os.system("taskkill /IM cmd.exe")
                                                else:
                                                    print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                    time.sleep(0.7)
                                                    os.system("cls")
                            else:
                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print("Yammie lekker ijsje! Je hebt die al jaren niet meer gehad. Het proefden echt enorm lekker. Na zo een lange tijd.")
                                print("Na 5 maanden ontvangen jullie een verblijfsvergunning. Je mogen hier net zo lang blijven tot dat de oorlog voorbij is in jullie land.")

                                print("\nJe mag kiezen of je gebracht word naar het verblijf waar je mag blijven of dat je met de trein wilt…")
                                print("A. …met de trein 18")
                                print("B. …gebracht worden 19")
                                vraag4f = input("Maak je keuze: ")
                                if vraag4f == ("A") or ("a"):
                                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    print("Je neemt de trein naar je verblijf. Eindelijk! De plek waar je enorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                                    print("\n Je mag kiezen welke behang je doet in je kamer…")
                                    print("A. roze behang 21")
                                    print("B. blauw behang 21")
                                    vraag4g = input("Maak je keuze: ")
                                    if vraag4g == ("A") or ("a"):
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                        print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                        print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                        print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                        print("\n[Einde]")
                                        while True:
                                            while True:
                                                restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                if restart in ("1") or ("2"):
                                                    break
                                                if restart == "1":
                                                    print("Laten we het verhaal opnieuw spelen")
                                                    time.sleep(0.8)
                                                    os.system("cls")
                                                    time.sleep(1)
                                                    os.system("py Verhaallijn.py")
                                                elif restart == "2":
                                                    print("Oke, bedankt voor het spelen. Tot ziens!")
                                                    time.sleep(0.6)
                                                    os.system("taskkill /IM cmd.exe")
                                                else:
                                                    print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                    time.sleep(0.7)
                                                    os.system("cls")
                                    else:
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                        print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                        print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                        print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                        print("\n[Einde]")
                                        while True:
                                            while True:
                                                restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                if restart in ("1") or ("2"):
                                                    break
                                                if restart == "1":
                                                    print("Laten we het verhaal opnieuw spelen")
                                                    time.sleep(0.8)
                                                    os.system("cls")
                                                    time.sleep(1)
                                                    os.system("py Verhaallijn.py")
                                                elif restart == "2":
                                                    print("Oke, bedankt voor het spelen. Tot ziens!")
                                                    time.sleep(0.6)
                                                    os.system("taskkill /IM cmd.exe")
                                                else:
                                                    print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                    time.sleep(0.7)
                                                    os.system("cls")   
                                else:
                                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    print("Je word gebracht. Eindelijk! De plek waarjeenorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                                    print("\nJe mag kiezen welke behang je doet in je kamer...")
                                    print("A. ...roze behang 21")
                                    print("B. ...blauw behang 21")
                                    vraag4h = input("Maak je keuze: ")
                                    if vraag4h == ("A") or ("a"):
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                        print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                        print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                        print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                        print("\n[Einde]")
                                        while True:
                                            while True:
                                                restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                if restart in ("1") or ("2"):
                                                    break
                                                if restart == "1":
                                                    print("Laten we het verhaal opnieuw spelen")
                                                    time.sleep(0.8)
                                                    os.system("cls")
                                                    time.sleep(1)
                                                    os.system("py Verhaallijn.py")
                                                elif restart == "2":
                                                    print("Oke, bedankt voor het spelen. Tot ziens!")
                                                    time.sleep(0.6)
                                                    os.system("taskkill /IM cmd.exe")
                                                else:
                                                    print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                    time.sleep(0.7)
                                                    os.system("cls")
                                    else:
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                        print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                        print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                        print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                        print("\n[Einde]")
                                        while True:
                                            while True:
                                                restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                if restart in ("1") or ("2"):
                                                    break
                                                if restart == "1":
                                                    print("Laten we het verhaal opnieuw spelen")
                                                    time.sleep(0.8)
                                                    os.system("cls")
                                                    time.sleep(1)
                                                    os.system("py Verhaallijn.py")
                                                elif restart == "2":
                                                    print("Oke, bedankt voor het spelen. Tot ziens!")
                                                    time.sleep(0.6)
                                                    os.system("taskkill /IM cmd.exe")
                                                else:
                                                    print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                    time.sleep(0.7)
                                                    os.system("cls")
                else:
                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    print("Op naar Nederland!De reis is enorm lastig om vanaf hier‘Italië’naarNederland te gaan.Dagen gingen voorbij. Je komt aan na 5 dagen lopen in Zwitserlandaan.")
                    print("Je ontmoet iemand die alleen de kinderen willen mee nemen naar België en die persoon zoulater dan de volwassen meenemen als ze hier wachten op haar.")
                    print("Ze wilt namelijk graag de kinderen helpen en ze snel opweg nemen naar iets veiligs en ze wist iemand waar hunuit eindelijkkonden verblijven.")

                    print("\nJij kiest ervoor om...")
                    print("A. ...mee te gaan 16")
                    print("B. ...niet mee te gaan 17") 
                    vraag3a = input("Maak je keuze: ")
                    if vraag3a == ("A") or ("a"): 
                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        print("Je neemt de trein naar je verblijf. Eindelijk! De plek waar je enorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                        print("\n Je mag kiezen welke behang je doet in je kamer…")
                        print("A. roze behang 21")
                        print("B. blauw behang 21")
                        vraag3b = input("Maak je keuze: ")
                        if vraag3b == ("A") or ("a"):  
                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                            print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                            print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                            print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                            print("\n[Einde]")
                            while True:
                                while True:
                                    restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                    if restart in ("1") or ("2"):
                                        break
                                    if restart == "1":
                                        print("Laten we het verhaal opnieuw spelen")
                                        time.sleep(0.8)
                                        os.system("cls")
                                        time.sleep(1)
                                        os.system("py Verhaallijn.py")
                                    elif restart == "2":
                                        print("Oke, bedankt voor het spelen. Tot ziens!")
                                        time.sleep(0.6)
                                        os.system("taskkill /IM cmd.exe")
                                    else:
                                        print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                        time.sleep(0.7)
                                        os.system("cls") 
                        else:
                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                            print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                            print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                            print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                            print("\n[Einde]")
                            while True:
                                while True:
                                    restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                    if restart in ("1") or ("2"):
                                        break
                                    if restart == "1":
                                        print("Laten we het verhaal opnieuw spelen")
                                        time.sleep(0.8)
                                        os.system("cls")
                                        time.sleep(1)
                                        os.system("py Verhaallijn.py")
                                    elif restart == "2":
                                        print("Oke, bedankt voor het spelen. Tot ziens!")
                                        time.sleep(0.6)
                                        os.system("taskkill /IM cmd.exe")
                                    else:
                                        print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                        time.sleep(0.7)
                                        os.system("cls")   
                    else:
                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        print("Je gaat niet mee met de vrouw en gaat met groep weg. Na 1 dag gezeten te hebben in Zwitserland.")
                        print("Komt er een politie naar jullie toe en die merkt zich op dat jullie hier illegaalzijn. En die neemt jullie allemaal mee naar de gevangenis")

                        print("\n[Einde]")
                        while True:
                            while True:
                                restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                if restart in ("1") or ("2"):
                                    break
                                if restart == "1":
                                    print("Laten we het verhaal opnieuw spelen")
                                    time.sleep(0.8)
                                    os.system("cls")
                                    time.sleep(1)
                                    os.system("py Verhaallijn.py")
                                elif restart == "2":
                                    print("Oke, bedankt voor het spelen. Tot ziens!")
                                    time.sleep(0.6)
                                    os.system("taskkill /IM cmd.exe")
                                else:
                                    print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                    time.sleep(0.7)
                                    os.system("cls")   
            else:
                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("Je kiest ervoor om met de boot weg tegaan. Een nadeel is alleen dat het enorm gevaarlijk grote kans dat je het niet haalt en is het enorm illegaal.")
                print("Je ging met auto naar het water om via daar naar Europa te gaan. De boot die ze daar hadden was veelte klein voor ons allemaal.")
                print("Als de boot zo omslaan zouden we allemaal dood gaan niemand van ons had leren zwemmen en ik kon dat al helemaal niet ik ben bang voor water..")
                print("En daar moesten we 1 dag zitten... Veelte eng!De kinderen moest voorin en de ouderen achterin op elkaar.")
                print("Na 10 uur op elkaar moest iedereen een beetje bewegen de boot bewoog zo ergdat alle mensen aan de rechte kan ging zitten waardoor de boot omsloeg...")

                print("\n[Einde]")
                while True:
                    while True:
                        restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                        if restart in ("1") or ("2"):
                            break
                        if restart == "1":
                            print("Laten we het verhaal opnieuw spelen")
                            time.sleep(0.8)
                            os.system("cls")
                            time.sleep(1)
                            os.system("py Verhaallijn.py")
                        elif restart == "2":
                            print("Oke, bedankt voor het spelen. Tot ziens!")
                            time.sleep(0.6)
                            os.system("taskkill /IM cmd.exe")
                        else:
                            print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                            time.sleep(0.7)
                            os.system("cls")
        else:
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("Je kiest ervoor om toch mee te gaan met die mensen. En je ouders liet je achter.")
            print("De mensen die je meenamen waren kennissen van je ouders vertelde ze je en die zorgde ervoor dat jij veilig weg zou komen hier uit Syrië.")
            print("En ze vertelde je dat de oorlog uitbrak. En dat het voor jou niet veilig was en je ouders wilde dat jij een goede toekomst zou hebben.")
            print("De kennissen vertelde dat je zo direct met een auto word mee genomen. En dat je vanaf daar met een grote groep mensen met de boot naar Italië zou varen.")
            print("Het was op dat moment te veel voor je dat je het effe niet meer kon plaatsen wat er gebeurden en je ging maar mee in de auto. Onder weg naar de boot naar Italië.")
            print("Dat ging allemaal goed tot dat de auto bij de grens kwam van Europa. Je hoorde mensen praten *Je kan niet in Europa zonder een geldig paspoort*.Maar jij heb die niet.")

            print("\nDe groep kon daar beslissen om..")
            print("A. …5 maanden voor de grens te wachten tot dat je een bewijs krijgt dat je in dat land mag. 1")
            print("B. …gelijk met de boot weg alleen was dat enorm gevaarlijk. Er is namelijk een grote kans dat je het niet haalt. 13")
            vraag1a = input("Maak je keuze: ")
            if vraag1a == ("A") or ("a"):
                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("Na3 maanden daar verbleven te hebben besluit je toch maar naar Nederland te gaan. Daar gingen veel uren aan voorbij")

                print("\nMaar omdat je hoorde dat je moeilijk in Nederland te recht komt gaf je jezelf de keuzenaar welke land je eerst wilde gaan.")
                print("A. ...Duitsland 5")
                print("B. ...Nederland 8")
                vraag1b = input("Maak je keuze: ")
                if vraag1b == ("A") or ("a"):
                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    print("Eerst maar even naar Duitsland. Uren ging voorbij je komt bij de grens van Duitsland aan ze vragen om je paspoort.")
                    print("Je hebt geen geldig paspoort behalve dan de vluchtelingen formulier.")
                    print("In Duitsland is het zo dat je dan ook maanden moet gaan wacht voor dat je in dat land mag komen verblijven.")
                    print("Er gingen weer 5 maanden voorbij. Je kreeg toegang tot Duitsland je mocht er wonen. Je kreeg een verblijf aan geboden.")

                    print("\nMaar jij wilde kiezen tussen..")
                    print("A. De reis naar Nederland. 14")
                    print("B. Een verblijf in Duitsland. 7")
                    vraag1c = input("Maak je keuze: ")
                    if vraag1c == ("A") or ("a"):
                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        print("De reis naar Nederland is begonnen. Je laat alles achter in Duitsland. En neemt je koffertje mee.")
                        print("Na een paar dagen kom je aan in op bij de grens van Nederland je mag hier niet zomaar verblijven daar heb je een verblijfsvergunning voor nodig.")
                        print("En dat duurde langer dan je had verwacht maar je ontvangt een verblijf met allerlei andere mensen uit Syrië waarbij je kan overnachten tot dat het zo ver is.")
                        print("Maar toen je daar aan kwam voelde je als een pas geboren baby zonder moeder. Je kende de taal niet je kende helemaal niks hier.")
                        print(". Alleen maar de mensen die dezelfde taal spraken. Na 5 dagen in het verblijf te hebben gezeten kwam de ijs man toevallig..")

                        print("\nJe kon kiezen tussen de ijsjes..")
                        print("A. Chocolade ijs 15")
                        print("B. Aardbei ijs 15")
                        vraag1d = input("Maak je keuze: ")
                        if vraag1d == ("A") or ("a"):
                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            print("Yammie lekker ijsje! Je hebt die al jaren niet meer gehad. Het proefden echt enorm lekker. Na zo een lange tijd.")
                            print("Na 5 maanden ontvangen jullie een verblijfsvergunning. Je mogen hier net zo lang blijven tot dat de oorlog voorbij is in jullie land.")

                            print("\nJe mag kiezen of je gebracht word naar het verblijf waar je mag blijven of dat je met de trein wilt…")
                            print("A. …met de trein 18")
                            print("B. …gebracht worden 19")
                            vraag1e = input("Maak je keuze: ")
                            if vraag1e == ("A") or ("a"):
                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print("Je neemt de trein naar je verblijf. Eindelijk! De plek waar je enorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                                print("\n Je mag kiezen welke behang je doet in je kamer…")
                                print("A. roze behang 21")
                                print("B. blauw behang 21")
                                vraag1f = input("Maak je keuze: ")
                                if vraag1f == ("A") or ("a"):
                                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                    print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                    print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                    print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                    print("\n[Einde]")
                                    while True:
                                        while True:
                                            restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                            if restart in ("1") or ("2"):
                                                break
                                            if restart == "1":
                                                print("Laten we het verhaal opnieuw spelen")
                                                time.sleep(0.8)
                                                os.system("cls")
                                                time.sleep(1)
                                                os.system("py Verhaallijn.py")
                                            elif restart == "2":
                                                print("Oke, bedankt voor het spelen. Tot ziens!")
                                                time.sleep(0.6)
                                                os.system("taskkill /IM cmd.exe")
                                            else:
                                                print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                time.sleep(0.7)
                                                os.system("cls")
                                else:
                                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                    print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                    print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                    print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                    print("\n[Einde]")
                                    while True:
                                        while True:
                                            restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                            if restart in ("1") or ("2"):
                                                break
                                            if restart == "1":
                                                print("Laten we het verhaal opnieuw spelen")
                                                time.sleep(0.8)
                                                os.system("cls")
                                                time.sleep(1)
                                                os.system("py Verhaallijn.py")
                                            elif restart == "2":
                                                print("Oke, bedankt voor het spelen. Tot ziens!")
                                                time.sleep(0.6)
                                                os.system("taskkill /IM cmd.exe")
                                            else:
                                                print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                time.sleep(0.7)
                                                os.system("cls")   
                            else:
                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print("Je word gebracht. Eindelijk! De plek waarjeenorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                                print("\nJe mag kiezen welke behang je doet in je kamer...")
                                print("A. ...roze behang 21")
                                print("B. ...blauw behang 21")
                                vraag1g = input("Maak je keuze: ")
                                if vraag1g == ("A") or ("a"):
                                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                    print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                    print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                    print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                    print("\n[Einde]")
                                    while True:
                                        while True:
                                            restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                            if restart in ("1") or ("2"):
                                                break
                                            if restart == "1":
                                                print("Laten we het verhaal opnieuw spelen")
                                                time.sleep(0.8)
                                                os.system("cls")
                                                time.sleep(1)
                                                os.system("py Verhaallijn.py")
                                            elif restart == "2":
                                                print("Oke, bedankt voor het spelen. Tot ziens!")
                                                time.sleep(0.6)
                                                os.system("taskkill /IM cmd.exe")
                                            else:
                                                print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                time.sleep(0.7)
                                                os.system("cls")
                                else:
                                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                    print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                    print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                    print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                    print("\n[Einde]")
                                    while True:
                                        while True:
                                            restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                            if restart in ("1") or ("2"):
                                                break
                                            if restart == "1":
                                                print("Laten we het verhaal opnieuw spelen")
                                                time.sleep(0.8)
                                                os.system("cls")
                                                time.sleep(1)
                                                os.system("py Verhaallijn.py")
                                            elif restart == "2":
                                                print("Oke, bedankt voor het spelen. Tot ziens!")
                                                time.sleep(0.6)
                                                os.system("taskkill /IM cmd.exe")
                                            else:
                                                print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                time.sleep(0.7)
                                                os.system("cls")
                        else:
                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            print("Yammie lekker ijsje! Je hebt die al jaren niet meer gehad. Het proefden echt enorm lekker. Na zo een lange tijd.")
                            print("Na 5 maanden ontvangen jullie een verblijfsvergunning. Je mogen hier net zo lang blijven tot dat de oorlog voorbij is in jullie land.")

                            print("\nJe mag kiezen of je gebracht word naar het verblijf waar je mag blijven of dat je met de trein wilt…")
                            print("A. …met de trein 18")
                            print("B. …gebracht worden 19")
                            vraag1h = input("Maak je keuze: ")
                            if vraag1h == ("A") or ("a"):
                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print("Je neemt de trein naar je verblijf. Eindelijk! De plek waar je enorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                                print("\n Je mag kiezen welke behang je doet in je kamer…")
                                print("A. roze behang 21")
                                print("B. blauw behang 21")
                                vraag1i = input("Maak je keuze: ")
                                if vraag1i == ("A") or ("a"):
                                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                    print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                    print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                    print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                    print("\n[Einde]")
                                    while True:
                                        while True:
                                            restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                            if restart in ("1") or ("2"):
                                                break
                                            if restart == "1":
                                                print("Laten we het verhaal opnieuw spelen")
                                                time.sleep(0.8)
                                                os.system("cls")
                                                time.sleep(1)
                                                os.system("py Verhaallijn.py")
                                            elif restart == "2":
                                                print("Oke, bedankt voor het spelen. Tot ziens!")
                                                time.sleep(0.6)
                                                os.system("taskkill /IM cmd.exe")
                                            else:
                                                print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                time.sleep(0.7)
                                                os.system("cls")
                                else:
                                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                    print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                    print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                    print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                    print("\n[Einde]")
                                    while True:
                                        while True:
                                            restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                            if restart in ("1") or ("2"):
                                                break
                                            if restart == "1":
                                                print("Laten we het verhaal opnieuw spelen")
                                                time.sleep(0.8)
                                                os.system("cls")
                                                time.sleep(1)
                                                os.system("py Verhaallijn.py")
                                            elif restart == "2":
                                                print("Oke, bedankt voor het spelen. Tot ziens!")
                                                time.sleep(0.6)
                                                os.system("taskkill /IM cmd.exe")
                                            else:
                                                print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                time.sleep(0.7)
                                                os.system("cls")   
                            else:
                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print("Je word gebracht. Eindelijk! De plek waarjeenorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                                print("\nJe mag kiezen welke behang je doet in je kamer...")
                                print("A. ...roze behang 21")
                                print("B. ...blauw behang 21")
                                vraag1j = input("Maak je keuze: ")
                                if vraag1j == ("A") or ("a"):
                                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                    print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                    print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                    print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                    print("\n[Einde]")
                                    while True:
                                        while True:
                                            restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                            if restart in ("1") or ("2"):
                                                break
                                            if restart == "1":
                                                print("Laten we het verhaal opnieuw spelen")
                                                time.sleep(0.8)
                                                os.system("cls")
                                                time.sleep(1)
                                                os.system("py Verhaallijn.py")
                                            elif restart == "2":
                                                print("Oke, bedankt voor het spelen. Tot ziens!")
                                                time.sleep(0.6)
                                                os.system("taskkill /IM cmd.exe")
                                            else:
                                                print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                time.sleep(0.7)
                                                os.system("cls")
                                else:
                                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                    print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                    print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                    print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                    print("\n[Einde]")
                                    while True:
                                        while True:
                                            restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                            if restart in ("1") or ("2"):
                                                break
                                            if restart == "1":
                                                print("Laten we het verhaal opnieuw spelen")
                                                time.sleep(0.8)
                                                os.system("cls")
                                                time.sleep(1)
                                                os.system("py Verhaallijn.py")
                                            elif restart == "2":
                                                print("Oke, bedankt voor het spelen. Tot ziens!")
                                                time.sleep(0.6)
                                                os.system("taskkill /IM cmd.exe")
                                            else:
                                                print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                time.sleep(0.7)
                                                os.system("cls")
                    else:
                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        print("Het huisje in Duitsland. Je wilde eerst daar de taal kennen. Effe tot rust komen en dan later de reis te gemoed komen naar Nederland.")
                        print("Daar ging 2 jaar over heen.Je wilde weg hier je wilde naar Nederland.")

                        print("\nJe kon kiezen tussen..")
                        print("A. ...met de trein gaan. 14")
                        print("B. ...lopend naar Nederland want dat was niet zo ver. 14")
                        vraag1k = input("Maak je keuze: ")
                        if vraag1k == ("A") or ("a"):  
                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            print("De reis naar Nederland is begonnen. Je laat alles achter in Duitsland. En neemt je koffertje mee.")
                            print("Na een paar dagen kom je aan in op bij de grens van Nederland je mag hier niet zomaar verblijven daar heb je een verblijfsvergunning voor nodig.")
                            print("En dat duurde langer dan je had verwacht maar je ontvangt een verblijf met allerlei andere mensen uit Syrië waarbij je kan overnachten tot dat het zo ver is.")
                            print("Maar toen je daar aan kwam voelde je als een pas geboren baby zonder moeder. Je kende de taal niet je kende helemaal niks hier.")
                            print(". Alleen maar de mensen die dezelfde taal spraken. Na 5 dagen in het verblijf te hebben gezeten kwam de ijs man toevallig..")

                            print("\nJe kon kiezen tussen de ijsjes..")
                            print("A. Chocolade ijs 15")
                            print("B. Aardbei ijs 15")
                            vraag1l = input("Maak je keuze: ")
                            if vraag1l == ("A") or ("a"): 
                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print("Yammie lekker ijsje! Je hebt die al jaren niet meer gehad. Het proefden echt enorm lekker. Na zo een lange tijd.")
                                print("Na 5 maanden ontvangen jullie een verblijfsvergunning. Je mogen hier net zo lang blijven tot dat de oorlog voorbij is in jullie land.")

                                print("\nJe mag kiezen of je gebracht word naar het verblijf waar je mag blijven of dat je met de trein wilt…")
                                print("A. …met de trein 18")
                                print("B. …gebracht worden 19")
                                vraag1m = input("Maak je keuze: ")
                                if vraag1m == ("A") or ("a"):
                                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    print("Je neemt de trein naar je verblijf. Eindelijk! De plek waar je enorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                                    print("\n Je mag kiezen welke behang je doet in je kamer…")
                                    print("A. roze behang 21")
                                    print("B. blauw behang 21")
                                    vraag1n = input("Maak je keuze: ")
                                    if vraag1n == ("A") or ("a"):
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                        print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                        print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                        print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                        print("\n[Einde]")
                                        while True:
                                            while True:
                                                restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                if restart in ("1") or ("2"):
                                                    break
                                                if restart == "1":
                                                    print("Laten we het verhaal opnieuw spelen")
                                                    time.sleep(0.8)
                                                    os.system("cls")
                                                    time.sleep(1)
                                                    os.system("py Verhaallijn.py")
                                                elif restart == "2":
                                                    print("Oke, bedankt voor het spelen. Tot ziens!")
                                                    time.sleep(0.6)
                                                    os.system("taskkill /IM cmd.exe")
                                                else:
                                                    print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                    time.sleep(0.7)
                                                    os.system("cls")
                                    else:
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                        print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                        print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                        print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                        print("\n[Einde]")
                                        while True:
                                            while True:
                                                restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                if restart in ("1") or ("2"):
                                                    break
                                                if restart == "1":
                                                    print("Laten we het verhaal opnieuw spelen")
                                                    time.sleep(0.8)
                                                    os.system("cls")
                                                    time.sleep(1)
                                                    os.system("py Verhaallijn.py")
                                                elif restart == "2":
                                                    print("Oke, bedankt voor het spelen. Tot ziens!")
                                                    time.sleep(0.6)
                                                    os.system("taskkill /IM cmd.exe")
                                                else:
                                                    print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                    time.sleep(0.7)
                                                    os.system("cls")   
                                else:
                                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    print("Je word gebracht. Eindelijk! De plek waarjeenorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                                    print("\nJe mag kiezen welke behang je doet in je kamer...")
                                    print("A. ...roze behang 21")
                                    print("B. ...blauw behang 21")
                                    vraag1o = input("Maak je keuze: ")
                                    if vraag1o == ("A") or ("a"):
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                        print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                        print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                        print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                        print("\n[Einde]")
                                        while True:
                                            while True:
                                                restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                if restart in ("1") or ("2"):
                                                    break
                                                if restart == "1":
                                                    print("Laten we het verhaal opnieuw spelen")
                                                    time.sleep(0.8)
                                                    os.system("cls")
                                                    time.sleep(1)
                                                    os.system("py Verhaallijn.py")
                                                elif restart == "2":
                                                    print("Oke, bedankt voor het spelen. Tot ziens!")
                                                    time.sleep(0.6)
                                                    os.system("taskkill /IM cmd.exe")
                                                else:
                                                    print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                    time.sleep(0.7)
                                                    os.system("cls")
                                    else:
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                        print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                        print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                        print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                        print("\n[Einde]")
                                        while True:
                                            while True:
                                                restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                if restart in ("1") or ("2"):
                                                    break
                                                if restart == "1":
                                                    print("Laten we het verhaal opnieuw spelen")
                                                    time.sleep(0.8)
                                                    os.system("cls")
                                                    time.sleep(1)
                                                    os.system("py Verhaallijn.py")
                                                elif restart == "2":
                                                    print("Oke, bedankt voor het spelen. Tot ziens!")
                                                    time.sleep(0.6)
                                                    os.system("taskkill /IM cmd.exe")
                                                else:
                                                    print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                    time.sleep(0.7)
                                                    os.system("cls")
                            else:
                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print("Yammie lekker ijsje! Je hebt die al jaren niet meer gehad. Het proefden echt enorm lekker. Na zo een lange tijd.")
                                print("Na 5 maanden ontvangen jullie een verblijfsvergunning. Je mogen hier net zo lang blijven tot dat de oorlog voorbij is in jullie land.")

                                print("\nJe mag kiezen of je gebracht word naar het verblijf waar je mag blijven of dat je met de trein wilt…")
                                print("A. …met de trein 18")
                                print("B. …gebracht worden 19")
                                vraag1p = input("Maak je keuze: ")
                                if vraag1p == ("A") or ("a"):
                                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    print("Je neemt de trein naar je verblijf. Eindelijk! De plek waar je enorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                                    print("\n Je mag kiezen welke behang je doet in je kamer…")
                                    print("A. roze behang 21")
                                    print("B. blauw behang 21")
                                    vraag1q = input("Maak je keuze: ")
                                    if vraag1q == ("A") or ("a"):
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                        print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                        print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                        print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                        print("\n[Einde]")
                                        while True:
                                            while True:
                                                restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                if restart in ("1") or ("2"):
                                                    break
                                                if restart == "1":
                                                    print("Laten we het verhaal opnieuw spelen")
                                                    time.sleep(0.8)
                                                    os.system("cls")
                                                    time.sleep(1)
                                                    os.system("py Verhaallijn.py")
                                                elif restart == "2":
                                                    print("Oke, bedankt voor het spelen. Tot ziens!")
                                                    time.sleep(0.6)
                                                    os.system("taskkill /IM cmd.exe")
                                                else:
                                                    print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                    time.sleep(0.7)
                                                    os.system("cls")
                                    else:
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                        print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                        print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                        print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                        print("\n[Einde]")
                                        while True:
                                            while True:
                                                restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                if restart in ("1") or ("2"):
                                                    break
                                                if restart == "1":
                                                    print("Laten we het verhaal opnieuw spelen")
                                                    time.sleep(0.8)
                                                    os.system("cls")
                                                    time.sleep(1)
                                                    os.system("py Verhaallijn.py")
                                                elif restart == "2":
                                                    print("Oke, bedankt voor het spelen. Tot ziens!")
                                                    time.sleep(0.6)
                                                    os.system("taskkill /IM cmd.exe")
                                                else:
                                                    print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                    time.sleep(0.7)
                                                    os.system("cls")   
                                else:
                                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    print("Je word gebracht. Eindelijk! De plek waarjeenorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                                    print("\nJe mag kiezen welke behang je doet in je kamer...")
                                    print("A. ...roze behang 21")
                                    print("B. ...blauw behang 21")
                                    vraag1r = input("Maak je keuze: ")
                                    if vraag1r == ("A") or ("a"):
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                        print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                        print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                        print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                        print("\n[Einde]")
                                        while True:
                                            while True:
                                                restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                if restart in ("1") or ("2"):
                                                    break
                                                if restart == "1":
                                                    print("Laten we het verhaal opnieuw spelen")
                                                    time.sleep(0.8)
                                                    os.system("cls")
                                                    time.sleep(1)
                                                    os.system("py Verhaallijn.py")
                                                elif restart == "2":
                                                    print("Oke, bedankt voor het spelen. Tot ziens!")
                                                    time.sleep(0.6)
                                                    os.system("taskkill /IM cmd.exe")
                                                else:
                                                    print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                    time.sleep(0.7)
                                                    os.system("cls")
                                    else:
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                        print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                        print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                        print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                        print("\n[Einde]")
                                        while True:
                                            while True:
                                                restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                if restart in ("1") or ("2"):
                                                    break
                                                if restart == "1":
                                                    print("Laten we het verhaal opnieuw spelen")
                                                    time.sleep(0.8)
                                                    os.system("cls")
                                                    time.sleep(1)
                                                    os.system("py Verhaallijn.py")
                                                elif restart == "2":
                                                    print("Oke, bedankt voor het spelen. Tot ziens!")
                                                    time.sleep(0.6)
                                                    os.system("taskkill /IM cmd.exe")
                                                else:
                                                    print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                    time.sleep(0.7)
                                                    os.system("cls")
                else:
                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    print("Op naar Nederland!De reis is enorm lastig om vanaf hier‘Italië’naarNederland te gaan.Dagen gingen voorbij. Je komt aan na 5 dagen lopen in Zwitserlandaan.")
                    print("Je ontmoet iemand die alleen de kinderen willen mee nemen naar België en die persoon zoulater dan de volwassen meenemen als ze hier wachten op haar.")
                    print("Ze wilt namelijk graag de kinderen helpen en ze snel opweg nemen naar iets veiligs en ze wist iemand waar hunuit eindelijkkonden verblijven.")

                    print("\nJij kiest ervoor om...")
                    print("A. ...mee te gaan 16")
                    print("B. ...niet mee te gaan 17") 
                    vraag1s = input("Maak je keuze: ")
                    if vraag1s == ("A") or ("a"): 
                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        print("Je neemt de trein naar je verblijf. Eindelijk! De plek waar je enorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                        print("\n Je mag kiezen welke behang je doet in je kamer…")
                        print("A. roze behang 21")
                        print("B. blauw behang 21")
                        vraag1t = input("Maak je keuze: ")
                        if vraag1t == ("A") or ("a"):  
                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                            print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                            print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                            print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                            print("\n[Einde]")
                            while True:
                                while True:
                                    restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                    if restart in ("1") or ("2"):
                                        break
                                    if restart == "1":
                                        print("Laten we het verhaal opnieuw spelen")
                                        time.sleep(0.8)
                                        os.system("cls")
                                        time.sleep(1)
                                        os.system("py Verhaallijn.py")
                                    elif restart == "2":
                                        print("Oke, bedankt voor het spelen. Tot ziens!")
                                        time.sleep(0.6)
                                        os.system("taskkill /IM cmd.exe")
                                    else:
                                        print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                        time.sleep(0.7)
                                        os.system("cls") 
                        else:
                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                            print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                            print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                            print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                            print("\n[Einde]")
                            while True:
                                while True:
                                    restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                    if restart in ("1") or ("2"):
                                        break
                                    if restart == "1":
                                        print("Laten we het verhaal opnieuw spelen")
                                        time.sleep(0.8)
                                        os.system("cls")
                                        time.sleep(1)
                                        os.system("py Verhaallijn.py")
                                    elif restart == "2":
                                        print("Oke, bedankt voor het spelen. Tot ziens!")
                                        time.sleep(0.6)
                                        os.system("taskkill /IM cmd.exe")
                                    else:
                                        print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                        time.sleep(0.7)
                                        os.system("cls")   
                    else:
                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        print("Je gaat niet mee met de vrouw en gaat met groep weg. Na 1 dag gezeten te hebben in Zwitserland.")
                        print("Komt er een politie naar jullie toe en die merkt zich op dat jullie hier illegaalzijn. En die neemt jullie allemaal mee naar de gevangenis")

                        print("\n[Einde]")
                        while True:
                            while True:
                                restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                if restart in ("1") or ("2"):
                                    break
                                if restart == "1":
                                    print("Laten we het verhaal opnieuw spelen")
                                    time.sleep(0.8)
                                    os.system("cls")
                                    time.sleep(1)
                                    os.system("py Verhaallijn.py")
                                elif restart == "2":
                                    print("Oke, bedankt voor het spelen. Tot ziens!")
                                    time.sleep(0.6)
                                    os.system("taskkill /IM cmd.exe")
                                else:
                                    print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                    time.sleep(0.7)
                                    os.system("cls")   
            else:
                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("Je kiest ervoor om met de boot weg tegaan. Een nadeel is alleen dat het enorm gevaarlijk grote kans dat je het niet haalt en is het enorm illegaal.")
                print("Je ging met auto naar het water om via daar naar Europa te gaan. De boot die ze daar hadden was veelte klein voor ons allemaal.")
                print("Als de boot zo omslaan zouden we allemaal dood gaan niemand van ons had leren zwemmen en ik kon dat al helemaal niet ik ben bang voor water..")
                print("En daar moesten we 1 dag zitten... Veelte eng!De kinderen moest voorin en de ouderen achterin op elkaar.")
                print("Na 10 uur op elkaar moest iedereen een beetje bewegen de boot bewoog zo ergdat alle mensen aan de rechte kan ging zitten waardoor de boot omsloeg...")

                print("\n[Einde]")
                while True:
                    while True:
                        restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                        if restart in ("1") or ("2"):
                            break
                        if restart == "1":
                            print("Laten we het verhaal opnieuw spelen")
                            time.sleep(0.8)
                            os.system("cls")
                            time.sleep(1)
                            os.system("py Verhaallijn.py")
                        elif restart == "2":
                            print("Oke, bedankt voor het spelen. Tot ziens!")
                            time.sleep(0.6)
                            os.system("taskkill /IM cmd.exe")
                        else:
                            print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                            time.sleep(0.7)
                            os.system("cls")
    else:
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Je verstuurde het berichtje. En je gaat verder met het tandenpoetsen. Je krijgt maar steeds geen berichtje terug.")
        print("Na 2 uur besluit je maar te gaan slapen.*Ring* *Ring* Je wekker gaat af het is half 7.")
        print("Je sluipt zachtjes naar beneden doet je jas aan en vertrekt. Terwijl je onderweg bent bedenk je je of het toch niet zo goed idee was.")

        print("\nEn je besluit om…")
        print("A. …toch terug te gaan naar huis. En weer in bed te liggen 9")
        print("B. …toch door te gaan naar je beste vriendin haar huis. 20")
        vraaga = input("Maak je keuze: ")
        if vraaga == ("A") or ("a"):
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("En je vertelt haar dat je dit weekend ook niet kon komen. Je krijgt daar geen reactie op.")
            print("Je nog steeds niks binnen. Maar je hoort wel allemaal geritsel thuis.")
            print("Je ziet je moeder en vader heel veel dingen bij elkaar aan het zoeken zijn. Je vraagt wat er aan de hand is.")
            print("Ze zeggen dat je je moet opschieten en je nu per direct je spullen bij elkaar moet zoeken.")
            print("Was het al te laat dus voor al die spullen. Je moeder en vader nemen je rennend mee in de auto.")
            print("Op weg naar de grens. Je ouders worden net om de hoek aangehouden. De mensen die je ouders aanhouden vragen waar jullie heen gaan.")
            print("Je ouders zeggen; alsjeblieft neem mijn kind mee over grens wij blijven hier.")
            print("Alsjeblieft! Jij begint enorm te huilen je weet niet wat er aan de hand is.")
            print("De mensen trekken je uit de auto en nemen je mee.")

            print("\nJij kiest ervoor om..")
            print("A. Toch met je ouders te blijven en met hun mee te gaan. 12")
            print("B. Mee te gaan met die mensen. 11")
            vraagb = input("Maak je keuze: ")
            if vraagb == ("A") or ("a"):
                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("Jij kiest ervoor om toch te blijven met je ouders. Maar je ouder dwingen je en ze helpen je eruit.")
                print("En je word mee genomen met die mensen. Ze vertellen je dat het gevaarlijk is hier en dat je je ouders willen beschermen.")
                print("Jij vraagt wat er aan de hand is.. De kennissen van je ouders dat zijn wij en mochten niet vertellen wat er aan de hand is maar.")
                print("Er brak gisteren oorlog uit in Syrië. En dit is de laatste keer dat je je ouders ooit nog gaat zien.")
                print("Je brak van binnen je wist niest meer je was er enorm stil van en je stond zo stijf dat je maar de auto in ging van de kennissen.")
                print("De kennissen vertelde dat je word gebracht naar de grens van Europa en daar wacht een ander groep op je.")
                print("Je rijdt naar de grens van Europa waar een boot staan die je naar Italië brengt. Dat ging allemaal goed tot dat de auto bij de grens kwam van Europa.")
                print("Je hoorde mensen praten *Je kan niet in Europa zonder een geldig paspoort*.Maar jij heb die niet.")

                print("\nDe groep kon daar beslissen om..")
                print("A. …5 maanden voor de grens te wachten tot dat je een bewijs krijgt dat je in dat land mag. 1")
                print("B. …gelijk met de boot weg alleen was dat enorm gevaarlijk. Er is namelijk een grote kans dat je het niet haalt. 13")
                vraagc = input("Maak je keuze: ")
                if vraagc == ("A") or ("a"):
                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    print("Na3 maanden daar verbleven te hebben besluit je toch maar naar Nederland te gaan. Daar gingen veel uren aan voorbij")

                    print("\nMaar omdat je hoorde dat je moeilijk in Nederland te recht komt gaf je jezelf de keuzenaar welke land je eerst wilde gaan.")
                    print("A. ...Duitsland 5")
                    print("B. ...Nederland 8")
                    vraagd = input("Maak je keuze: ")
                    if vraagd == ("A") or ("a"):
                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        print("Eerst maar even naar Duitsland. Uren ging voorbij je komt bij de grens van Duitsland aan ze vragen om je paspoort.")
                        print("Je hebt geen geldig paspoort behalve dan de vluchtelingen formulier.")
                        print("In Duitsland is het zo dat je dan ook maanden moet gaan wacht voor dat je in dat land mag komen verblijven.")
                        print("Er gingen weer 5 maanden voorbij. Je kreeg toegang tot Duitsland je mocht er wonen. Je kreeg een verblijf aan geboden.")

                        print("\nMaar jij wilde kiezen tussen..")
                        print("A. De reis naar Nederland. 14")
                        print("B. Een verblijf in Duitsland. 7")
                        vraage = input("Maak je keuze: ")
                        if vraage == ("A") or ("a"):
                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            print("De reis naar Nederland is begonnen. Je laat alles achter in Duitsland. En neemt je koffertje mee.")
                            print("Na een paar dagen kom je aan in op bij de grens van Nederland je mag hier niet zomaar verblijven daar heb je een verblijfsvergunning voor nodig.")
                            print("En dat duurde langer dan je had verwacht maar je ontvangt een verblijf met allerlei andere mensen uit Syrië waarbij je kan overnachten tot dat het zo ver is.")
                            print("Maar toen je daar aan kwam voelde je als een pas geboren baby zonder moeder. Je kende de taal niet je kende helemaal niks hier.")
                            print(". Alleen maar de mensen die dezelfde taal spraken. Na 5 dagen in het verblijf te hebben gezeten kwam de ijs man toevallig..")

                            print("\nJe kon kiezen tussen de ijsjes..")
                            print("A. Chocolade ijs 15")
                            print("B. Aardbei ijs 15")
                            vraagf = input("Maak je keuze: ")
                            if vraagf == ("A") or ("a"):
                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print("Yammie lekker ijsje! Je hebt die al jaren niet meer gehad. Het proefden echt enorm lekker. Na zo een lange tijd.")
                                print("Na 5 maanden ontvangen jullie een verblijfsvergunning. Je mogen hier net zo lang blijven tot dat de oorlog voorbij is in jullie land.")

                                print("\nJe mag kiezen of je gebracht word naar het verblijf waar je mag blijven of dat je met de trein wilt…")
                                print("A. …met de trein 18")
                                print("B. …gebracht worden 19")
                                vraagg = input("Maak je keuze: ")
                                if vraagg == ("A") or ("a"):
                                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    print("Je neemt de trein naar je verblijf. Eindelijk! De plek waar je enorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                                    print("\n Je mag kiezen welke behang je doet in je kamer…")
                                    print("A. roze behang 21")
                                    print("B. blauw behang 21")
                                    vraage = input("Maak je keuze: ")
                                    if vraage == ("A") or ("a"):
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                        print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                        print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                        print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                        print("\n[Einde]")
                                        while True:
                                            while True:
                                                restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                if restart in ("1") or ("2"):
                                                    break
                                                if restart == "1":
                                                    print("Laten we het verhaal opnieuw spelen")
                                                    time.sleep(0.8)
                                                    os.system("cls")
                                                    time.sleep(1)
                                                    os.system("py Verhaallijn.py")
                                                elif restart == "2":
                                                    print("Oke, bedankt voor het spelen. Tot ziens!")
                                                    time.sleep(0.6)
                                                    os.system("taskkill /IM cmd.exe")
                                                else:
                                                    print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                    time.sleep(0.7)
                                                    os.system("cls")
                                    else:
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                        print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                        print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                        print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                        print("\n[Einde]")
                                        while True:
                                            while True:
                                                restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                if restart in ("1") or ("2"):
                                                    break
                                                if restart == "1":
                                                    print("Laten we het verhaal opnieuw spelen")
                                                    time.sleep(0.8)
                                                    os.system("cls")
                                                    time.sleep(1)
                                                    os.system("py Verhaallijn.py")
                                                elif restart == "2":
                                                    print("Oke, bedankt voor het spelen. Tot ziens!")
                                                    time.sleep(0.6)
                                                    os.system("taskkill /IM cmd.exe")
                                                else:
                                                    print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                    time.sleep(0.7)
                                                    os.system("cls")   
                                else:
                                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    print("Je word gebracht. Eindelijk! De plek waarjeenorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                                    print("\nJe mag kiezen welke behang je doet in je kamer...")
                                    print("A. ...roze behang 21")
                                    print("B. ...blauw behang 21")
                                    vraagf = input("Maak je keuze: ")
                                    if vraagf == ("A") or ("a"):
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                        print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                        print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                        print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                        print("\n[Einde]")
                                        while True:
                                            while True:
                                                restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                if restart in ("1") or ("2"):
                                                    break
                                                if restart == "1":
                                                    print("Laten we het verhaal opnieuw spelen")
                                                    time.sleep(0.8)
                                                    os.system("cls")
                                                    time.sleep(1)
                                                    os.system("py Verhaallijn.py")
                                                elif restart == "2":
                                                    print("Oke, bedankt voor het spelen. Tot ziens!")
                                                    time.sleep(0.6)
                                                    os.system("taskkill /IM cmd.exe")
                                                else:
                                                    print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                    time.sleep(0.7)
                                                    os.system("cls")
                                    else:
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                        print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                        print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                        print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                        print("\n[Einde]")
                                        while True:
                                            while True:
                                                restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                if restart in ("1") or ("2"):
                                                    break
                                                if restart == "1":
                                                    print("Laten we het verhaal opnieuw spelen")
                                                    time.sleep(0.8)
                                                    os.system("cls")
                                                    time.sleep(1)
                                                    os.system("py Verhaallijn.py")
                                                elif restart == "2":
                                                    print("Oke, bedankt voor het spelen. Tot ziens!")
                                                    time.sleep(0.6)
                                                    os.system("taskkill /IM cmd.exe")
                                                else:
                                                    print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                    time.sleep(0.7)
                                                    os.system("cls")
                            else:
                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print("Yammie lekker ijsje! Je hebt die al jaren niet meer gehad. Het proefden echt enorm lekker. Na zo een lange tijd.")
                                print("Na 5 maanden ontvangen jullie een verblijfsvergunning. Je mogen hier net zo lang blijven tot dat de oorlog voorbij is in jullie land.")

                                print("\nJe mag kiezen of je gebracht word naar het verblijf waar je mag blijven of dat je met de trein wilt…")
                                print("A. …met de trein 18")
                                print("B. …gebracht worden 19")
                                vraagh = input("Maak je keuze: ")
                                if vraagh == ("A") or ("a"):
                                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    print("Je neemt de trein naar je verblijf. Eindelijk! De plek waar je enorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                                    print("\n Je mag kiezen welke behang je doet in je kamer…")
                                    print("A. roze behang 21")
                                    print("B. blauw behang 21")
                                    vraagi = input("Maak je keuze: ")
                                    if vraagi == ("A") or ("a"):
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                        print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                        print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                        print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                        print("\n[Einde]")
                                        while True:
                                            while True:
                                                restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                if restart in ("1") or ("2"):
                                                    break
                                                if restart == "1":
                                                    print("Laten we het verhaal opnieuw spelen")
                                                    time.sleep(0.8)
                                                    os.system("cls")
                                                    time.sleep(1)
                                                    os.system("py Verhaallijn.py")
                                                elif restart == "2":
                                                    print("Oke, bedankt voor het spelen. Tot ziens!")
                                                    time.sleep(0.6)
                                                    os.system("taskkill /IM cmd.exe")
                                                else:
                                                    print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                    time.sleep(0.7)
                                                    os.system("cls")
                                    else:
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                        print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                        print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                        print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                        print("\n[Einde]")
                                        while True:
                                            while True:
                                                restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                if restart in ("1") or ("2"):
                                                    break
                                                if restart == "1":
                                                    print("Laten we het verhaal opnieuw spelen")
                                                    time.sleep(0.8)
                                                    os.system("cls")
                                                    time.sleep(1)
                                                    os.system("py Verhaallijn.py")
                                                elif restart == "2":
                                                    print("Oke, bedankt voor het spelen. Tot ziens!")
                                                    time.sleep(0.6)
                                                    os.system("taskkill /IM cmd.exe")
                                                else:
                                                    print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                    time.sleep(0.7)
                                                    os.system("cls")   
                                else:
                                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    print("Je word gebracht. Eindelijk! De plek waarjeenorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                                    print("\nJe mag kiezen welke behang je doet in je kamer...")
                                    print("A. ...roze behang 21")
                                    print("B. ...blauw behang 21")
                                    vraagj = input("Maak je keuze: ")
                                    if vraagj == ("A") or ("a"):
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                        print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                        print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                        print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                        print("\n[Einde]")
                                        while True:
                                            while True:
                                                restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                if restart in ("1") or ("2"):
                                                    break
                                                if restart == "1":
                                                    print("Laten we het verhaal opnieuw spelen")
                                                    time.sleep(0.8)
                                                    os.system("cls")
                                                    time.sleep(1)
                                                    os.system("py Verhaallijn.py")
                                                elif restart == "2":
                                                    print("Oke, bedankt voor het spelen. Tot ziens!")
                                                    time.sleep(0.6)
                                                    os.system("taskkill /IM cmd.exe")
                                                else:
                                                    print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                    time.sleep(0.7)
                                                    os.system("cls")
                                    else:
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                        print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                        print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                        print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                        print("\n[Einde]")
                                        while True:
                                            while True:
                                                restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                if restart in ("1") or ("2"):
                                                    break
                                                if restart == "1":
                                                    print("Laten we het verhaal opnieuw spelen")
                                                    time.sleep(0.8)
                                                    os.system("cls")
                                                    time.sleep(1)
                                                    os.system("py Verhaallijn.py")
                                                elif restart == "2":
                                                    print("Oke, bedankt voor het spelen. Tot ziens!")
                                                    time.sleep(0.6)
                                                    os.system("taskkill /IM cmd.exe")
                                                else:
                                                    print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                    time.sleep(0.7)
                                                    os.system("cls")
                        else:
                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            print("Het huisje in Duitsland. Je wilde eerst daar de taal kennen. Effe tot rust komen en dan later de reis te gemoed komen naar Nederland.")
                            print("Daar ging 2 jaar over heen.Je wilde weg hier je wilde naar Nederland.")

                            print("\nJe kon kiezen tussen..")
                            print("A. ...met de trein gaan. 14")
                            print("B. ...lopend naar Nederland want dat was niet zo ver. 14")
                            vraagk = input("Maak je keuze: ")
                            if vraagk == ("A") or ("a"):  
                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print("De reis naar Nederland is begonnen. Je laat alles achter in Duitsland. En neemt je koffertje mee.")
                                print("Na een paar dagen kom je aan in op bij de grens van Nederland je mag hier niet zomaar verblijven daar heb je een verblijfsvergunning voor nodig.")
                                print("En dat duurde langer dan je had verwacht maar je ontvangt een verblijf met allerlei andere mensen uit Syrië waarbij je kan overnachten tot dat het zo ver is.")
                                print("Maar toen je daar aan kwam voelde je als een pas geboren baby zonder moeder. Je kende de taal niet je kende helemaal niks hier.")
                                print(". Alleen maar de mensen die dezelfde taal spraken. Na 5 dagen in het verblijf te hebben gezeten kwam de ijs man toevallig..")

                                print("\nJe kon kiezen tussen de ijsjes..")
                                print("A. Chocolade ijs 15")
                                print("B. Aardbei ijs 15")
                                vraagl = input("Maak je keuze: ")
                                if vraagl == ("A") or ("a"): 
                                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    print("Yammie lekker ijsje! Je hebt die al jaren niet meer gehad. Het proefden echt enorm lekker. Na zo een lange tijd.")
                                    print("Na 5 maanden ontvangen jullie een verblijfsvergunning. Je mogen hier net zo lang blijven tot dat de oorlog voorbij is in jullie land.")

                                    print("\nJe mag kiezen of je gebracht word naar het verblijf waar je mag blijven of dat je met de trein wilt…")
                                    print("A. …met de trein 18")
                                    print("B. …gebracht worden 19")
                                    vraagm = input("Maak je keuze: ")
                                    if vraagm == ("A") or ("a"):
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("Je neemt de trein naar je verblijf. Eindelijk! De plek waar je enorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                                        print("\n Je mag kiezen welke behang je doet in je kamer…")
                                        print("A. roze behang 21")
                                        print("B. blauw behang 21")
                                        vraagn = input("Maak je keuze: ")
                                        if vraagn == ("A") or ("a"):
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                            print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                            print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                            print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                            print("\n[Einde]")
                                            while True:
                                                while True:
                                                    restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                    if restart in ("1") or ("2"):
                                                        break
                                                    if restart == "1":
                                                        print("Laten we het verhaal opnieuw spelen")
                                                        time.sleep(0.8)
                                                        os.system("cls")
                                                        time.sleep(1)
                                                        os.system("py Verhaallijn.py")
                                                    elif restart == "2":
                                                        print("Oke, bedankt voor het spelen. Tot ziens!")
                                                        time.sleep(0.6)
                                                        os.system("taskkill /IM cmd.exe")
                                                    else:
                                                        print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                        time.sleep(0.7)
                                                        os.system("cls")
                                        else:
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                            print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                            print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                            print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                            print("\n[Einde]")
                                            while True:
                                                while True:
                                                    restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                    if restart in ("1") or ("2"):
                                                        break
                                                    if restart == "1":
                                                        print("Laten we het verhaal opnieuw spelen")
                                                        time.sleep(0.8)
                                                        os.system("cls")
                                                        time.sleep(1)
                                                        os.system("py Verhaallijn.py")
                                                    elif restart == "2":
                                                        print("Oke, bedankt voor het spelen. Tot ziens!")
                                                        time.sleep(0.6)
                                                        os.system("taskkill /IM cmd.exe")
                                                    else:
                                                        print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                        time.sleep(0.7)
                                                        os.system("cls")   
                                    else:
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("Je word gebracht. Eindelijk! De plek waarjeenorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                                        print("\nJe mag kiezen welke behang je doet in je kamer...")
                                        print("A. ...roze behang 21")
                                        print("B. ...blauw behang 21")
                                        vraago = input("Maak je keuze: ")
                                        if vraago == ("A") or ("a"):
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                            print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                            print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                            print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                            print("\n[Einde]")
                                            while True:
                                                while True:
                                                    restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                    if restart in ("1") or ("2"):
                                                        break
                                                    if restart == "1":
                                                        print("Laten we het verhaal opnieuw spelen")
                                                        time.sleep(0.8)
                                                        os.system("cls")
                                                        time.sleep(1)
                                                        os.system("py Verhaallijn.py")
                                                    elif restart == "2":
                                                        print("Oke, bedankt voor het spelen. Tot ziens!")
                                                        time.sleep(0.6)
                                                        os.system("taskkill /IM cmd.exe")
                                                    else:
                                                        print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                        time.sleep(0.7)
                                                        os.system("cls")
                                        else:
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                            print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                            print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                            print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                            print("\n[Einde]")
                                            while True:
                                                while True:
                                                    restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                    if restart in ("1") or ("2"):
                                                        break
                                                    if restart == "1":
                                                        print("Laten we het verhaal opnieuw spelen")
                                                        time.sleep(0.8)
                                                        os.system("cls")
                                                        time.sleep(1)
                                                        os.system("py Verhaallijn.py")
                                                    elif restart == "2":
                                                        print("Oke, bedankt voor het spelen. Tot ziens!")
                                                        time.sleep(0.6)
                                                        os.system("taskkill /IM cmd.exe")
                                                    else:
                                                        print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                        time.sleep(0.7)
                                                        os.system("cls")
                                else:
                                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    print("Yammie lekker ijsje! Je hebt die al jaren niet meer gehad. Het proefden echt enorm lekker. Na zo een lange tijd.")
                                    print("Na 5 maanden ontvangen jullie een verblijfsvergunning. Je mogen hier net zo lang blijven tot dat de oorlog voorbij is in jullie land.")

                                    print("\nJe mag kiezen of je gebracht word naar het verblijf waar je mag blijven of dat je met de trein wilt…")
                                    print("A. …met de trein 18")
                                    print("B. …gebracht worden 19")
                                    vraagp = input("Maak je keuze: ")
                                    if vraagp == ("A") or ("a"):
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("Je neemt de trein naar je verblijf. Eindelijk! De plek waar je enorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                                        print("\n Je mag kiezen welke behang je doet in je kamer…")
                                        print("A. roze behang 21")
                                        print("B. blauw behang 21")
                                        vraagq = input("Maak je keuze: ")
                                        if vraagq == ("A") or ("a"):
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                            print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                            print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                            print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                            print("\n[Einde]")
                                            while True:
                                                while True:
                                                    restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                    if restart in ("1") or ("2"):
                                                        break
                                                    if restart == "1":
                                                        print("Laten we het verhaal opnieuw spelen")
                                                        time.sleep(0.8)
                                                        os.system("cls")
                                                        time.sleep(1)
                                                        os.system("py Verhaallijn.py")
                                                    elif restart == "2":
                                                        print("Oke, bedankt voor het spelen. Tot ziens!")
                                                        time.sleep(0.6)
                                                        os.system("taskkill /IM cmd.exe")
                                                    else:
                                                        print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                        time.sleep(0.7)
                                                        os.system("cls")
                                        else:
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                            print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                            print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                            print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                            print("\n[Einde]")
                                            while True:
                                                while True:
                                                    restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                    if restart in ("1") or ("2"):
                                                        break
                                                    if restart == "1":
                                                        print("Laten we het verhaal opnieuw spelen")
                                                        time.sleep(0.8)
                                                        os.system("cls")
                                                        time.sleep(1)
                                                        os.system("py Verhaallijn.py")
                                                    elif restart == "2":
                                                        print("Oke, bedankt voor het spelen. Tot ziens!")
                                                        time.sleep(0.6)
                                                        os.system("taskkill /IM cmd.exe")
                                                    else:
                                                        print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                        time.sleep(0.7)
                                                        os.system("cls")   
                                    else:
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("Je word gebracht. Eindelijk! De plek waarjeenorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                                        print("\nJe mag kiezen welke behang je doet in je kamer...")
                                        print("A. ...roze behang 21")
                                        print("B. ...blauw behang 21")
                                        vraagr = input("Maak je keuze: ")
                                        if vraagr == ("A") or ("a"):
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                            print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                            print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                            print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                            print("\n[Einde]")
                                            while True:
                                                while True:
                                                    restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                    if restart in ("1") or ("2"):
                                                        break
                                                    if restart == "1":
                                                        print("Laten we het verhaal opnieuw spelen")
                                                        time.sleep(0.8)
                                                        os.system("cls")
                                                        time.sleep(1)
                                                        os.system("py Verhaallijn.py")
                                                    elif restart == "2":
                                                        print("Oke, bedankt voor het spelen. Tot ziens!")
                                                        time.sleep(0.6)
                                                        os.system("taskkill /IM cmd.exe")
                                                    else:
                                                        print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                        time.sleep(0.7)
                                                        os.system("cls")
                                        else:
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                            print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                            print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                            print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                            print("\n[Einde]")
                                            while True:
                                                while True:
                                                    restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                    if restart in ("1") or ("2"):
                                                        break
                                                    if restart == "1":
                                                        print("Laten we het verhaal opnieuw spelen")
                                                        time.sleep(0.8)
                                                        os.system("cls")
                                                        time.sleep(1)
                                                        os.system("py Verhaallijn.py")
                                                    elif restart == "2":
                                                        print("Oke, bedankt voor het spelen. Tot ziens!")
                                                        time.sleep(0.6)
                                                        os.system("taskkill /IM cmd.exe")
                                                    else:
                                                        print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                        time.sleep(0.7)
                                                        os.system("cls")
                    else:
                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        print("Op naar Nederland!De reis is enorm lastig om vanaf hier‘Italië’naarNederland te gaan.Dagen gingen voorbij. Je komt aan na 5 dagen lopen in Zwitserlandaan.")
                        print("Je ontmoet iemand die alleen de kinderen willen mee nemen naar België en die persoon zoulater dan de volwassen meenemen als ze hier wachten op haar.")
                        print("Ze wilt namelijk graag de kinderen helpen en ze snel opweg nemen naar iets veiligs en ze wist iemand waar hunuit eindelijkkonden verblijven.")

                        print("\nJij kiest ervoor om...")
                        print("A. ...mee te gaan 16")
                        print("B. ...niet mee te gaan 17") 
                        vraags = input("Maak je keuze: ")
                        if vraags == ("A") or ("a"): 
                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            print("Je neemt de trein naar je verblijf. Eindelijk! De plek waar je enorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                            print("\n Je mag kiezen welke behang je doet in je kamer…")
                            print("A. roze behang 21")
                            print("B. blauw behang 21")
                            vraagt = input("Maak je keuze: ")
                            if vraagt == ("A") or ("a"):  
                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                print("\n[Einde]")
                                while True:
                                    while True:
                                        restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                        if restart in ("1") or ("2"):
                                            break
                                        if restart == "1":
                                            print("Laten we het verhaal opnieuw spelen")
                                            time.sleep(0.8)
                                            os.system("cls")
                                            time.sleep(1)
                                            os.system("py Verhaallijn.py")
                                        elif restart == "2":
                                            print("Oke, bedankt voor het spelen. Tot ziens!")
                                            time.sleep(0.6)
                                            os.system("taskkill /IM cmd.exe")
                                        else:
                                            print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                            time.sleep(0.7)
                                            os.system("cls") 
                            else:
                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                print("\n[Einde]")
                                while True:
                                    while True:
                                        restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                        if restart in ("1") or ("2"):
                                            break
                                        if restart == "1":
                                            print("Laten we het verhaal opnieuw spelen")
                                            time.sleep(0.8)
                                            os.system("cls")
                                            time.sleep(1)
                                            os.system("py Verhaallijn.py")
                                        elif restart == "2":
                                            print("Oke, bedankt voor het spelen. Tot ziens!")
                                            time.sleep(0.6)
                                            os.system("taskkill /IM cmd.exe")
                                        else:
                                            print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                            time.sleep(0.7)
                                            os.system("cls")   
                        else:
                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            print("Je gaat niet mee met de vrouw en gaat met groep weg. Na 1 dag gezeten te hebben in Zwitserland.")
                            print("Komt er een politie naar jullie toe en die merkt zich op dat jullie hier illegaalzijn. En die neemt jullie allemaal mee naar de gevangenis")

                            print("\n[Einde]")
                            while True:
                                while True:
                                    restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                    if restart in ("1") or ("2"):
                                        break
                                    if restart == "1":
                                        print("Laten we het verhaal opnieuw spelen")
                                        time.sleep(0.8)
                                        os.system("cls")
                                        time.sleep(1)
                                        os.system("py Verhaallijn.py")
                                    elif restart == "2":
                                        print("Oke, bedankt voor het spelen. Tot ziens!")
                                        time.sleep(0.6)
                                        os.system("taskkill /IM cmd.exe")
                                    else:
                                        print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                        time.sleep(0.7)
                                        os.system("cls")   
                else:
                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    print("Je kiest ervoor om met de boot weg tegaan. Een nadeel is alleen dat het enorm gevaarlijk grote kans dat je het niet haalt en is het enorm illegaal.")
                    print("Je ging met auto naar het water om via daar naar Europa te gaan. De boot die ze daar hadden was veelte klein voor ons allemaal.")
                    print("Als de boot zo omslaan zouden we allemaal dood gaan niemand van ons had leren zwemmen en ik kon dat al helemaal niet ik ben bang voor water..")
                    print("En daar moesten we 1 dag zitten... Veelte eng!De kinderen moest voorin en de ouderen achterin op elkaar.")
                    print("Na 10 uur op elkaar moest iedereen een beetje bewegen de boot bewoog zo ergdat alle mensen aan de rechte kan ging zitten waardoor de boot omsloeg...")

                    print("\n[Einde]")
                    while True:
                        while True:
                            restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                            if restart in ("1") or ("2"):
                                break
                            if restart == "1":
                                print("Laten we het verhaal opnieuw spelen")
                                time.sleep(0.8)
                                os.system("cls")
                                time.sleep(1)
                                os.system("py Verhaallijn.py")
                            elif restart == "2":
                                print("Oke, bedankt voor het spelen. Tot ziens!")
                                time.sleep(0.6)
                                os.system("taskkill /IM cmd.exe")
                            else:
                                print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                time.sleep(0.7)
                                os.system("cls")
            else:
                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("Je kiest ervoor om toch mee te gaan met die mensen. En je ouders liet je achter.")
                print("De mensen die je meenamen waren kennissen van je ouders vertelde ze je en die zorgde ervoor dat jij veilig weg zou komen hier uit Syrië.")
                print("En ze vertelde je dat de oorlog uitbrak. En dat het voor jou niet veilig was en je ouders wilde dat jij een goede toekomst zou hebben.")
                print("De kennissen vertelde dat je zo direct met een auto word mee genomen. En dat je vanaf daar met een grote groep mensen met de boot naar Italië zou varen.")
                print("Het was op dat moment te veel voor je dat je het effe niet meer kon plaatsen wat er gebeurden en je ging maar mee in de auto. Onder weg naar de boot naar Italië.")
                print("Dat ging allemaal goed tot dat de auto bij de grens kwam van Europa. Je hoorde mensen praten *Je kan niet in Europa zonder een geldig paspoort*.Maar jij heb die niet.")

                print("\nDe groep kon daar beslissen om..")
                print("A. …5 maanden voor de grens te wachten tot dat je een bewijs krijgt dat je in dat land mag. 1")
                print("B. …gelijk met de boot weg alleen was dat enorm gevaarlijk. Er is namelijk een grote kans dat je het niet haalt. 13")
                vraagu = input("Maak je keuze: ")
                if vraagu == ("A") or ("a"):
                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    print("Na3 maanden daar verbleven te hebben besluit je toch maar naar Nederland te gaan. Daar gingen veel uren aan voorbij")

                    print("\nMaar omdat je hoorde dat je moeilijk in Nederland te recht komt gaf je jezelf de keuzenaar welke land je eerst wilde gaan.")
                    print("A. ...Duitsland 5")
                    print("B. ...Nederland 8")
                    vraagv = input("Maak je keuze: ")
                    if vraagv == ("A") or ("a"):
                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        print("Eerst maar even naar Duitsland. Uren ging voorbij je komt bij de grens van Duitsland aan ze vragen om je paspoort.")
                        print("Je hebt geen geldig paspoort behalve dan de vluchtelingen formulier.")
                        print("In Duitsland is het zo dat je dan ook maanden moet gaan wacht voor dat je in dat land mag komen verblijven.")
                        print("Er gingen weer 5 maanden voorbij. Je kreeg toegang tot Duitsland je mocht er wonen. Je kreeg een verblijf aan geboden.")

                        print("\nMaar jij wilde kiezen tussen..")
                        print("A. De reis naar Nederland. 14")
                        print("B. Een verblijf in Duitsland. 7")
                        vraagw = input("Maak je keuze: ")
                        if vraagw == ("A") or ("a"):
                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            print("De reis naar Nederland is begonnen. Je laat alles achter in Duitsland. En neemt je koffertje mee.")
                            print("Na een paar dagen kom je aan in op bij de grens van Nederland je mag hier niet zomaar verblijven daar heb je een verblijfsvergunning voor nodig.")
                            print("En dat duurde langer dan je had verwacht maar je ontvangt een verblijf met allerlei andere mensen uit Syrië waarbij je kan overnachten tot dat het zo ver is.")
                            print("Maar toen je daar aan kwam voelde je als een pas geboren baby zonder moeder. Je kende de taal niet je kende helemaal niks hier.")
                            print(". Alleen maar de mensen die dezelfde taal spraken. Na 5 dagen in het verblijf te hebben gezeten kwam de ijs man toevallig..")

                            print("\nJe kon kiezen tussen de ijsjes..")
                            print("A. Chocolade ijs 15")
                            print("B. Aardbei ijs 15")
                            vraagx = input("Maak je keuze: ")
                            if vraagx == ("A") or ("a"):
                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print("Yammie lekker ijsje! Je hebt die al jaren niet meer gehad. Het proefden echt enorm lekker. Na zo een lange tijd.")
                                print("Na 5 maanden ontvangen jullie een verblijfsvergunning. Je mogen hier net zo lang blijven tot dat de oorlog voorbij is in jullie land.")

                                print("\nJe mag kiezen of je gebracht word naar het verblijf waar je mag blijven of dat je met de trein wilt…")
                                print("A. …met de trein 18")
                                print("B. …gebracht worden 19")
                                vraagy = input("Maak je keuze: ")
                                if vraagy == ("A") or ("a"):
                                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    print("Je neemt de trein naar je verblijf. Eindelijk! De plek waar je enorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                                    print("\n Je mag kiezen welke behang je doet in je kamer…")
                                    print("A. roze behang 21")
                                    print("B. blauw behang 21")
                                    vraagz = input("Maak je keuze: ")
                                    if vraagz == ("A") or ("a"):
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                        print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                        print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                        print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                        print("\n[Einde]")
                                        while True:
                                            while True:
                                                restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                if restart in ("1") or ("2"):
                                                    break
                                                if restart == "1":
                                                    print("Laten we het verhaal opnieuw spelen")
                                                    time.sleep(0.8)
                                                    os.system("cls")
                                                    time.sleep(1)
                                                    os.system("py Verhaallijn.py")
                                                elif restart == "2":
                                                    print("Oke, bedankt voor het spelen. Tot ziens!")
                                                    time.sleep(0.6)
                                                    os.system("taskkill /IM cmd.exe")
                                                else:
                                                    print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                    time.sleep(0.7)
                                                    os.system("cls")
                                    else:
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                        print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                        print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                        print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                        print("\n[Einde]")
                                        while True:
                                            while True:
                                                restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                if restart in ("1") or ("2"):
                                                    break
                                                if restart == "1":
                                                    print("Laten we het verhaal opnieuw spelen")
                                                    time.sleep(0.8)
                                                    os.system("cls")
                                                    time.sleep(1)
                                                    os.system("py Verhaallijn.py")
                                                elif restart == "2":
                                                    print("Oke, bedankt voor het spelen. Tot ziens!")
                                                    time.sleep(0.6)
                                                    os.system("taskkill /IM cmd.exe")
                                                else:
                                                    print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                    time.sleep(0.7)
                                                    os.system("cls")   
                                else:
                                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    print("Je word gebracht. Eindelijk! De plek waarjeenorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                                    print("\nJe mag kiezen welke behang je doet in je kamer...")
                                    print("A. ...roze behang 21")
                                    print("B. ...blauw behang 21")
                                    vraaga1 = input("Maak je keuze: ")
                                    if vraaga1 == ("A") or ("a"):
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                        print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                        print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                        print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                        print("\n[Einde]")
                                        while True:
                                            while True:
                                                restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                if restart in ("1") or ("2"):
                                                    break
                                                if restart == "1":
                                                    print("Laten we het verhaal opnieuw spelen")
                                                    time.sleep(0.8)
                                                    os.system("cls")
                                                    time.sleep(1)
                                                    os.system("py Verhaallijn.py")
                                                elif restart == "2":
                                                    print("Oke, bedankt voor het spelen. Tot ziens!")
                                                    time.sleep(0.6)
                                                    os.system("taskkill /IM cmd.exe")
                                                else:
                                                    print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                    time.sleep(0.7)
                                                    os.system("cls")
                                    else:
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                        print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                        print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                        print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                        print("\n[Einde]")
                                        while True:
                                            while True:
                                                restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                if restart in ("1") or ("2"):
                                                    break
                                                if restart == "1":
                                                    print("Laten we het verhaal opnieuw spelen")
                                                    time.sleep(0.8)
                                                    os.system("cls")
                                                    time.sleep(1)
                                                    os.system("py Verhaallijn.py")
                                                elif restart == "2":
                                                    print("Oke, bedankt voor het spelen. Tot ziens!")
                                                    time.sleep(0.6)
                                                    os.system("taskkill /IM cmd.exe")
                                                else:
                                                    print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                    time.sleep(0.7)
                                                    os.system("cls")
                            else:
                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print("Yammie lekker ijsje! Je hebt die al jaren niet meer gehad. Het proefden echt enorm lekker. Na zo een lange tijd.")
                                print("Na 5 maanden ontvangen jullie een verblijfsvergunning. Je mogen hier net zo lang blijven tot dat de oorlog voorbij is in jullie land.")

                                print("\nJe mag kiezen of je gebracht word naar het verblijf waar je mag blijven of dat je met de trein wilt…")
                                print("A. …met de trein 18")
                                print("B. …gebracht worden 19")
                                vraaga2 = input("Maak je keuze: ")
                                if vraaga2 == ("A") or ("a"):
                                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    print("Je neemt de trein naar je verblijf. Eindelijk! De plek waar je enorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                                    print("\n Je mag kiezen welke behang je doet in je kamer…")
                                    print("A. roze behang 21")
                                    print("B. blauw behang 21")
                                    vraaga3 = input("Maak je keuze: ")
                                    if vraaga3 == ("A") or ("a"):
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                        print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                        print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                        print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                        print("\n[Einde]")
                                        while True:
                                            while True:
                                                restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                if restart in ("1") or ("2"):
                                                    break
                                                if restart == "1":
                                                    print("Laten we het verhaal opnieuw spelen")
                                                    time.sleep(0.8)
                                                    os.system("cls")
                                                    time.sleep(1)
                                                    os.system("py Verhaallijn.py")
                                                elif restart == "2":
                                                    print("Oke, bedankt voor het spelen. Tot ziens!")
                                                    time.sleep(0.6)
                                                    os.system("taskkill /IM cmd.exe")
                                                else:
                                                    print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                    time.sleep(0.7)
                                                    os.system("cls")
                                    else:
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                        print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                        print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                        print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                        print("\n[Einde]")
                                        while True:
                                            while True:
                                                restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                if restart in ("1") or ("2"):
                                                    break
                                                if restart == "1":
                                                    print("Laten we het verhaal opnieuw spelen")
                                                    time.sleep(0.8)
                                                    os.system("cls")
                                                    time.sleep(1)
                                                    os.system("py Verhaallijn.py")
                                                elif restart == "2":
                                                    print("Oke, bedankt voor het spelen. Tot ziens!")
                                                    time.sleep(0.6)
                                                    os.system("taskkill /IM cmd.exe")
                                                else:
                                                    print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                    time.sleep(0.7)
                                                    os.system("cls")   
                                else:
                                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    print("Je word gebracht. Eindelijk! De plek waarjeenorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                                    print("\nJe mag kiezen welke behang je doet in je kamer...")
                                    print("A. ...roze behang 21")
                                    print("B. ...blauw behang 21")
                                    vraaga4 = input("Maak je keuze: ")
                                    if vraaga4 == ("A") or ("a"):
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                        print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                        print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                        print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                        print("\n[Einde]")
                                        while True:
                                            while True:
                                                restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                if restart in ("1") or ("2"):
                                                    break
                                                if restart == "1":
                                                    print("Laten we het verhaal opnieuw spelen")
                                                    time.sleep(0.8)
                                                    os.system("cls")
                                                    time.sleep(1)
                                                    os.system("py Verhaallijn.py")
                                                elif restart == "2":
                                                    print("Oke, bedankt voor het spelen. Tot ziens!")
                                                    time.sleep(0.6)
                                                    os.system("taskkill /IM cmd.exe")
                                                else:
                                                    print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                    time.sleep(0.7)
                                                    os.system("cls")
                                    else:
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                        print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                        print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                        print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                        print("\n[Einde]")
                                        while True:
                                            while True:
                                                restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                if restart in ("1") or ("2"):
                                                    break
                                                if restart == "1":
                                                    print("Laten we het verhaal opnieuw spelen")
                                                    time.sleep(0.8)
                                                    os.system("cls")
                                                    time.sleep(1)
                                                    os.system("py Verhaallijn.py")
                                                elif restart == "2":
                                                    print("Oke, bedankt voor het spelen. Tot ziens!")
                                                    time.sleep(0.6)
                                                    os.system("taskkill /IM cmd.exe")
                                                else:
                                                    print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                    time.sleep(0.7)
                                                    os.system("cls")
                        else:
                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            print("Het huisje in Duitsland. Je wilde eerst daar de taal kennen. Effe tot rust komen en dan later de reis te gemoed komen naar Nederland.")
                            print("Daar ging 2 jaar over heen.Je wilde weg hier je wilde naar Nederland.")

                            print("\nJe kon kiezen tussen..")
                            print("A. ...met de trein gaan. 14")
                            print("B. ...lopend naar Nederland want dat was niet zo ver. 14")
                            vraaga5 = input("Maak je keuze: ")
                            if vraaga5 == ("A") or ("a"):  
                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print("De reis naar Nederland is begonnen. Je laat alles achter in Duitsland. En neemt je koffertje mee.")
                                print("Na een paar dagen kom je aan in op bij de grens van Nederland je mag hier niet zomaar verblijven daar heb je een verblijfsvergunning voor nodig.")
                                print("En dat duurde langer dan je had verwacht maar je ontvangt een verblijf met allerlei andere mensen uit Syrië waarbij je kan overnachten tot dat het zo ver is.")
                                print("Maar toen je daar aan kwam voelde je als een pas geboren baby zonder moeder. Je kende de taal niet je kende helemaal niks hier.")
                                print(". Alleen maar de mensen die dezelfde taal spraken. Na 5 dagen in het verblijf te hebben gezeten kwam de ijs man toevallig..")

                                print("\nJe kon kiezen tussen de ijsjes..")
                                print("A. Chocolade ijs 15")
                                print("B. Aardbei ijs 15")
                                vraaga6 = input("Maak je keuze: ")
                                if vraaga6 == ("A") or ("a"): 
                                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    print("Yammie lekker ijsje! Je hebt die al jaren niet meer gehad. Het proefden echt enorm lekker. Na zo een lange tijd.")
                                    print("Na 5 maanden ontvangen jullie een verblijfsvergunning. Je mogen hier net zo lang blijven tot dat de oorlog voorbij is in jullie land.")

                                    print("\nJe mag kiezen of je gebracht word naar het verblijf waar je mag blijven of dat je met de trein wilt…")
                                    print("A. …met de trein 18")
                                    print("B. …gebracht worden 19")
                                    vraaga7 = input("Maak je keuze: ")
                                    if vraaga7 == ("A") or ("a"):
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("Je neemt de trein naar je verblijf. Eindelijk! De plek waar je enorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                                        print("\n Je mag kiezen welke behang je doet in je kamer…")
                                        print("A. roze behang 21")
                                        print("B. blauw behang 21")
                                        vraaga8 = input("Maak je keuze: ")
                                        if vraaga8 == ("A") or ("a"):
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                            print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                            print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                            print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                            print("\n[Einde]")
                                            while True:
                                                while True:
                                                    restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                    if restart in ("1") or ("2"):
                                                        break
                                                    if restart == "1":
                                                        print("Laten we het verhaal opnieuw spelen")
                                                        time.sleep(0.8)
                                                        os.system("cls")
                                                        time.sleep(1)
                                                        os.system("py Verhaallijn.py")
                                                    elif restart == "2":
                                                        print("Oke, bedankt voor het spelen. Tot ziens!")
                                                        time.sleep(0.6)
                                                        os.system("taskkill /IM cmd.exe")
                                                    else:
                                                        print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                        time.sleep(0.7)
                                                        os.system("cls")
                                        else:
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                            print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                            print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                            print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                            print("\n[Einde]")
                                            while True:
                                                while True:
                                                    restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                    if restart in ("1") or ("2"):
                                                        break
                                                    if restart == "1":
                                                        print("Laten we het verhaal opnieuw spelen")
                                                        time.sleep(0.8)
                                                        os.system("cls")
                                                        time.sleep(1)
                                                        os.system("py Verhaallijn.py")
                                                    elif restart == "2":
                                                        print("Oke, bedankt voor het spelen. Tot ziens!")
                                                        time.sleep(0.6)
                                                        os.system("taskkill /IM cmd.exe")
                                                    else:
                                                        print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                        time.sleep(0.7)
                                                        os.system("cls")   
                                    else:
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("Je word gebracht. Eindelijk! De plek waarjeenorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                                        print("\nJe mag kiezen welke behang je doet in je kamer...")
                                        print("A. ...roze behang 21")
                                        print("B. ...blauw behang 21")
                                        vraaga9 = input("Maak je keuze: ")
                                        if vraaga9 == ("A") or ("a"):
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                            print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                            print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                            print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                            print("\n[Einde]")
                                            while True:
                                                while True:
                                                    restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                    if restart in ("1") or ("2"):
                                                        break
                                                    if restart == "1":
                                                        print("Laten we het verhaal opnieuw spelen")
                                                        time.sleep(0.8)
                                                        os.system("cls")
                                                        time.sleep(1)
                                                        os.system("py Verhaallijn.py")
                                                    elif restart == "2":
                                                        print("Oke, bedankt voor het spelen. Tot ziens!")
                                                        time.sleep(0.6)
                                                        os.system("taskkill /IM cmd.exe")
                                                    else:
                                                        print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                        time.sleep(0.7)
                                                        os.system("cls")
                                        else:
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                            print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                            print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                            print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                            print("\n[Einde]")
                                            while True:
                                                while True:
                                                    restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                    if restart in ("1") or ("2"):
                                                        break
                                                    if restart == "1":
                                                        print("Laten we het verhaal opnieuw spelen")
                                                        time.sleep(0.8)
                                                        os.system("cls")
                                                        time.sleep(1)
                                                        os.system("py Verhaallijn.py")
                                                    elif restart == "2":
                                                        print("Oke, bedankt voor het spelen. Tot ziens!")
                                                        time.sleep(0.6)
                                                        os.system("taskkill /IM cmd.exe")
                                                    else:
                                                        print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                        time.sleep(0.7)
                                                        os.system("cls")
                                else:
                                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    print("Yammie lekker ijsje! Je hebt die al jaren niet meer gehad. Het proefden echt enorm lekker. Na zo een lange tijd.")
                                    print("Na 5 maanden ontvangen jullie een verblijfsvergunning. Je mogen hier net zo lang blijven tot dat de oorlog voorbij is in jullie land.")

                                    print("\nJe mag kiezen of je gebracht word naar het verblijf waar je mag blijven of dat je met de trein wilt…")
                                    print("A. …met de trein 18")
                                    print("B. …gebracht worden 19")
                                    vraaga10 = input("Maak je keuze: ")
                                    if vraaga10 == ("A") or ("a"):
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("Je neemt de trein naar je verblijf. Eindelijk! De plek waar je enorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                                        print("\n Je mag kiezen welke behang je doet in je kamer…")
                                        print("A. roze behang 21")
                                        print("B. blauw behang 21")
                                        vraagb1 = input("Maak je keuze: ")
                                        if vraagb1 == ("A") or ("a"):
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                            print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                            print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                            print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                            print("\n[Einde]")
                                            while True:
                                                while True:
                                                    restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                    if restart in ("1") or ("2"):
                                                        break
                                                    if restart == "1":
                                                        print("Laten we het verhaal opnieuw spelen")
                                                        time.sleep(0.8)
                                                        os.system("cls")
                                                        time.sleep(1)
                                                        os.system("py Verhaallijn.py")
                                                    elif restart == "2":
                                                        print("Oke, bedankt voor het spelen. Tot ziens!")
                                                        time.sleep(0.6)
                                                        os.system("taskkill /IM cmd.exe")
                                                    else:
                                                        print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                        time.sleep(0.7)
                                                        os.system("cls")
                                        else:
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                            print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                            print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                            print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                            print("\n[Einde]")
                                            while True:
                                                while True:
                                                    restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                    if restart in ("1") or ("2"):
                                                        break
                                                    if restart == "1":
                                                        print("Laten we het verhaal opnieuw spelen")
                                                        time.sleep(0.8)
                                                        os.system("cls")
                                                        time.sleep(1)
                                                        os.system("py Verhaallijn.py")
                                                    elif restart == "2":
                                                        print("Oke, bedankt voor het spelen. Tot ziens!")
                                                        time.sleep(0.6)
                                                        os.system("taskkill /IM cmd.exe")
                                                    else:
                                                        print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                        time.sleep(0.7)
                                                        os.system("cls")   
                                    else:
                                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("Je word gebracht. Eindelijk! De plek waarjeenorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                                        print("\nJe mag kiezen welke behang je doet in je kamer...")
                                        print("A. ...roze behang 21")
                                        print("B. ...blauw behang 21")
                                        vraagb2 = input("Maak je keuze: ")
                                        if vraagb2 == ("A") or ("a"):
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                            print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                            print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                            print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                            print("\n[Einde]")
                                            while True:
                                                while True:
                                                    restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                    if restart in ("1") or ("2"):
                                                        break
                                                    if restart == "1":
                                                        print("Laten we het verhaal opnieuw spelen")
                                                        time.sleep(0.8)
                                                        os.system("cls")
                                                        time.sleep(1)
                                                        os.system("py Verhaallijn.py")
                                                    elif restart == "2":
                                                        print("Oke, bedankt voor het spelen. Tot ziens!")
                                                        time.sleep(0.6)
                                                        os.system("taskkill /IM cmd.exe")
                                                    else:
                                                        print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                        time.sleep(0.7)
                                                        os.system("cls")
                                        else:
                                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                            print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                            print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                            print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                            print("\n[Einde]")
                                            while True:
                                                while True:
                                                    restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                                    if restart in ("1") or ("2"):
                                                        break
                                                    if restart == "1":
                                                        print("Laten we het verhaal opnieuw spelen")
                                                        time.sleep(0.8)
                                                        os.system("cls")
                                                        time.sleep(1)
                                                        os.system("py Verhaallijn.py")
                                                    elif restart == "2":
                                                        print("Oke, bedankt voor het spelen. Tot ziens!")
                                                        time.sleep(0.6)
                                                        os.system("taskkill /IM cmd.exe")
                                                    else:
                                                        print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                                        time.sleep(0.7)
                                                        os.system("cls")
                    else:
                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        print("Op naar Nederland!De reis is enorm lastig om vanaf hier‘Italië’naarNederland te gaan.Dagen gingen voorbij. Je komt aan na 5 dagen lopen in Zwitserlandaan.")
                        print("Je ontmoet iemand die alleen de kinderen willen mee nemen naar België en die persoon zoulater dan de volwassen meenemen als ze hier wachten op haar.")
                        print("Ze wilt namelijk graag de kinderen helpen en ze snel opweg nemen naar iets veiligs en ze wist iemand waar hunuit eindelijkkonden verblijven.")

                        print("\nJij kiest ervoor om...")
                        print("A. ...mee te gaan 16")
                        print("B. ...niet mee te gaan 17") 
                        vraagb3 = input("Maak je keuze: ")
                        if vraagb3 == ("A") or ("a"): 
                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            print("Je neemt de trein naar je verblijf. Eindelijk! De plek waar je enorm veilig bent. De plek van je je toekomst. Je mag naar school.")

                            print("\n Je mag kiezen welke behang je doet in je kamer…")
                            print("A. roze behang 21")
                            print("B. blauw behang 21")
                            vraagb4 = input("Maak je keuze: ")
                            if vraagb4 == ("A") or ("a"):  
                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                print("\n[Einde]")
                                while True:
                                    while True:
                                        restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                        if restart in ("1") or ("2"):
                                            break
                                        if restart == "1":
                                            print("Laten we het verhaal opnieuw spelen")
                                            time.sleep(0.8)
                                            os.system("cls")
                                            time.sleep(1)
                                            os.system("py Verhaallijn.py")
                                        elif restart == "2":
                                            print("Oke, bedankt voor het spelen. Tot ziens!")
                                            time.sleep(0.6)
                                            os.system("taskkill /IM cmd.exe")
                                        else:
                                            print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                            time.sleep(0.7)
                                            os.system("cls") 
                            else:
                                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print("\nEen leuk behangetje voor een leuke kamer. Hihi!")
                                print("Na een paar maanden hier te hebben verbleven heb je de conclusie getrokken dat het heel belangrijk is om de Nederlandse taal te kennen om hier te verblijven.")
                                print("En dat het heel belangrijk is om hier een tussenweg te vinden tussen beide culturen die van jou en die van de Nederlandse cultuur.")
                                print("Na wat er allemaal is gebeurt kan ik jij vertellen dat je de toekomst voor je ziet en dat alles alleen maar beter word.")

                                print("\n[Einde]")
                                while True:
                                    while True:
                                        restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                        if restart in ("1") or ("2"):
                                            break
                                        if restart == "1":
                                            print("Laten we het verhaal opnieuw spelen")
                                            time.sleep(0.8)
                                            os.system("cls")
                                            time.sleep(1)
                                            os.system("py Verhaallijn.py")
                                        elif restart == "2":
                                            print("Oke, bedankt voor het spelen. Tot ziens!")
                                            time.sleep(0.6)
                                            os.system("taskkill /IM cmd.exe")
                                        else:
                                            print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                            time.sleep(0.7)
                                            os.system("cls")   
                        else:
                            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            print("Je gaat niet mee met de vrouw en gaat met groep weg. Na 1 dag gezeten te hebben in Zwitserland.")
                            print("Komt er een politie naar jullie toe en die merkt zich op dat jullie hier illegaalzijn. En die neemt jullie allemaal mee naar de gevangenis")

                            print("\n[Einde]")
                            while True:
                                while True:
                                    restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                                    if restart in ("1") or ("2"):
                                        break
                                    if restart == "1":
                                        print("Laten we het verhaal opnieuw spelen")
                                        time.sleep(0.8)
                                        os.system("cls")
                                        time.sleep(1)
                                        os.system("py Verhaallijn.py")
                                    elif restart == "2":
                                        print("Oke, bedankt voor het spelen. Tot ziens!")
                                        time.sleep(0.6)
                                        os.system("taskkill /IM cmd.exe")
                                    else:
                                        print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                        time.sleep(0.7)
                                        os.system("cls")   
                else:
                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    print("Je kiest ervoor om met de boot weg tegaan. Een nadeel is alleen dat het enorm gevaarlijk grote kans dat je het niet haalt en is het enorm illegaal.")
                    print("Je ging met auto naar het water om via daar naar Europa te gaan. De boot die ze daar hadden was veelte klein voor ons allemaal.")
                    print("Als de boot zo omslaan zouden we allemaal dood gaan niemand van ons had leren zwemmen en ik kon dat al helemaal niet ik ben bang voor water..")
                    print("En daar moesten we 1 dag zitten... Veelte eng!De kinderen moest voorin en de ouderen achterin op elkaar.")
                    print("Na 10 uur op elkaar moest iedereen een beetje bewegen de boot bewoog zo ergdat alle mensen aan de rechte kan ging zitten waardoor de boot omsloeg...")

                    print("\n[Einde]")
                    while True:
                        while True:
                            restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                            if restart in ("1") or ("2"):
                                break
                            if restart == "1":
                                print("Laten we het verhaal opnieuw spelen")
                                time.sleep(0.8)
                                os.system("cls")
                                time.sleep(1)
                                os.system("py Verhaallijn.py")
                            elif restart == "2":
                                print("Oke, bedankt voor het spelen. Tot ziens!")
                                time.sleep(0.6)
                                os.system("taskkill /IM cmd.exe")
                            else:
                                print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                                time.sleep(0.7)
                                os.system("cls")
        else:
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("Je besluit om toch naar je beste vriendin haar huis te gaan. Na 20 min te hebben gelopen kom je aan bij haar huis ze was er nog niet? Je bekijkt je telefoon je ziet dat het pas 5 voor 7 is. Nog 5 min?")
            print("Niks voor haar om zo perfect op tijd te komen. Het is 10 over 7.. Ze is er nog steeds niet?? Waar blijft ze? ")
            print("Je hoort ineens een keiharde knal waar je enorm van schrikt en er van op de grondvalt. Je weet niet wat je over komt.")
            print("Wat is dit? Je rent naar huis. Maar voor dat je dat kon doen viel er enorm veel puin op je. Je kon geen kant op.")
            print("Je hoort geschreeuw. Je hoort mensen schieten? Wat gebeurt hier?? Je roep keihard help.")
            print("Niemand hoorde je. Je telefoon was kapot gegaan van toen je net gevallen was. Hoe nu? De puin komt steeds een steeds dichterbij... *Klets*")

            print("\n[Einde]")
            while True:
                while True:
                    restart = input("1. opnieuw spelen\n2. afsluiten\n:")
                    if restart in ("1") or ("2"):
                        break
                    if restart == "1":
                        print("Laten we het verhaal opnieuw spelen")
                        time.sleep(0.8)
                        os.system("cls")
                        time.sleep(1)
                        os.system("py Verhaallijn.py")
                    elif restart == "2":
                        print("Oke, bedankt voor het spelen. Tot ziens!")
                        time.sleep(0.6)
                        os.system("taskkill /IM cmd.exe")
                    else:
                        print('Probeer het opnieuw.. Kies 1 of 2 >>>')
                        time.sleep(0.7)
                        os.system("cls")                         
                        