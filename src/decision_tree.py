"""
decision_tree.py

See moodul sisaldab kahte klassi, Node ja DecisionMap, mis võimaldavad luua ja hallata
mängu otsustuspuu struktuuri. Node klass esindab üksikut sõlme, mis sisaldab teksti ja
valikuid, samas kui DecisionMap klass loob ja haldab kogu mängu kaarti, mis koosneb
erinevatest sõlmedest.

Klassid:
    Node: Esindab otsustuspuu sõlme, mis sisaldab teksti ja valikuid.
    DecisionMap: Loob ja haldab mängu kaardistruktuuri, mis koosneb Node objektidest.
"""

class Node: # pylint: disable=too-few-public-methods
    """
    Node klass esindab otsustuspuu sõlme.
    Atribuudid:
        text (str): Tekst, mis on seotud selle sõlmega.
        choices (list): Valikute loend, mis on seotud selle sõlmega. Vaikimisi on tühi loend.
    Meetodid:
        __init__(text, choices=None): Initsialiseerib Node objekti antud teksti ja valikutega.
    """

    def __init__(self, text, choices=None, hint=None):
        self.text = text
        self.choices = choices or []
        self.hint = hint

class DecisionMap: # pylint: disable=too-few-public-methods
    """
    DecisionMap klass loob mängu kaardistruktuuri, mis koosneb erinevatest sõlmedest 
    (Node objektidest), mis sisaldavad mängu narratiivi ja valikuid. 
    Meetodid:
        __init__(): Initsialiseerib DecisionMap objekti ja loob mängu kaardistruktuuri.
        create_map(): Loob ja tagastab mängu kaardistruktuuri sõlmedega.
    """

    def __init__(self):
        self.nodes = self.create_map()

    def create_map(self):
        """
        Loob mängu kaardistruktuuri sõlmedega.
        Tagastab:
            dict: Sõlmede sõnastik, kus iga võtme väärtuseks on Node objekt, mis sisaldab
                  mängu narratiivi ja valikuid.
        """

        nodes = {
            "welcome": Node(
                "Oled palgasõdur ilma tööta. Seisad pimedal kindluse tänaval. "
                "Viimased kuu aega on taevast sadanud paduvihma. Su keep ja "
                "nahast saapad on läbivettinud. Vajad peavarju.",
                hint="Jätkamiseks vajuta suvalist klahvi..."
            ),
            "start": Node(
                "Oled tänaval. Näed kolme ust. Esimene on baar, mille uks on "
                "õrnalt paokil, seest on kosta muusikat. Teine on mahajäetud "
                "kirik, näha on, et seal pole aastaid tegutsetud. Kuhu lähed?", 
                [
                    {'text': 'Baar', 'node': 'bar'},
                    {'text': 'Kirik', 'node': 'church'},
                ]
            ),
            "bar": Node(
                "Sa astud baari sisse. Ainsaks valgusallikaks on peaaegu "
                "otsalõppenud küünla jupid, seintel on pikad varjud. Võõrad "
                "pilgud vaatavad sind. Kõigist olenditest paistab sulle kõige "
                "rohkem silma üks mees baarileti ees, sinust kaks korda pikem, "
                "kelle küürus selja tagant paistab karvutu kukal. Sa tunnetad,"
                " kuidas ruumis on pinge, kõiki valdab hirm. Suur mees keerab "
                "end ümber, jõulised lihased tõmblevad. Sa näed tema nägu, "
                "tema silmad hõõguvad, ta on ründamisvalmis. Sul on kolm "
                "võimalust:", 
                [
                    {"text": "Sa ründad teda vastu", "node": 'game_lost_in_a_fight'},
                    {"text": "Sa põgened baarist", "node": 'run_away_from_bar'},
                    {"text": "Haarad lähima joogipudeli", "node": 'game_lost_with_poison'},
                ]
            ),
            "church": Node(
                "Sa astud kirikusse. Õhus on tunda niiskust ja kopitust. "
                "Ainus valguse riba, mis siseruumi valgustab on üksik "
                "küünal võõra jumala altari ees. Sa liigud altari juurde."
                " Tõmbad taskust välja oma tühja revolveri ja asetad "
                "selle ikooni ette. Sa kuuled samme, need on nii vaiksed, "
                "et oleksid sul peaaegu märkamata jäänud. Keerad aeglaselt "
                "enda pead ümber, sa ei näe midagi, kirik on pime. Kui "
                "keerad pea tagasi, on revolver läinud. Sa tunned midagi "
                "külma vastu enda kukalt, seda külma metalli tunnet on raske "
                "sassi ajada. \"Anna see siia\", sosistab hääl su vasakusse kõrva, "
                "sinu enda revolver surutud vastu su pead. \"Annan mida?\" sa "
                "vastad segaduses, sa pole enda arust midagi kelleltki "
                "varastanud. \"Sa tead küll mida\". Revolveri hoiak muutus "
                "kindlamaks. Sa hoiad hinge kinni, sul on valik, mida teha.",
                [
                    {
                        'text': 'Ütled, et sul pole tema jaoks midagi',
                        'node': 'game_lost_in_church',
                },
                    {
                        'text': 'Tõmbad taskust esimesena kätte sattuva asja',
                        'node': 'game_won',
                },
                ]
            ),
            "game_lost_in_a_fight": Node(
                "Sa jooksed tema poole, tõmbad taskust välja revolveri, suunad sihiku "
                "mehe poole. Päästikut vajutades saad aru, et sul pole kuule, suur "
                "mees lööb su oimetuks. Oled kaotanud. Mäng on läbi. ",
                hint="Väljumiseks vajuta suvalist klahvi..."
            ),
            'run_away_from_bar': Node(
                "Keerad end ümber ja jooksed täiskiirusel baarist välja. Oled "
                "tagasi tänaval, baarilised ei jälita sind. Neil on parematki "
                "teha. Kuhu soovid minna?", 
                [
                    {'text': 'Baar', 'node': 'bar'},
                    {'text': 'Kirik', 'node': 'church'},
                ]
            ),
            'game_lost_with_poison': Node(
                "Sa haarad tühjast pudelist laua peal ja tõstad selle ähvardavalt "
                "pea kohale. Selgub, et pudelis oli paar tilka mürki, mis tilgub "
                "su pealaele. Sa tunned end uimasena, kukud elutult põrandale. "
                "Oled kaotanud. Mäng on läbi. ",
                hint="Väljumiseks vajuta suvalist klahvi..."
            ),
            'game_lost_in_church': Node(
                "\"Mul ei ole midagi sinu jaoks\", vastad tundmatule. Vari su "
                "seljataga hakkab lõrisema. Ole valmis maailmaga hüvasti "
                "jätma. Sa kuuled kuidas olend vajutab päästikut, käib klõks, "
                "järgneb vaikus. Sul on hea meel, et kuulid olid otsas. Olend "
                "see eest läks marru. Sa tunned küüsi enda kaela sisse lõikamas, "
                "raske on hingata. Oled kaotanud. Mäng on läbi.",
                hint="Väljumiseks vajuta suvalist klahvi..."
            ),
            'game_won': Node(
                "Aeglaste liigutustega võtad taskust kompsu. Olend su selja "
                "taga krabab selle. Ta vabastab revolveri su kuklalt ja "
                "taandub nurka. Kompsust võtab välja peotäie rosinaid ning "
                "hakkab neid nosima. See oli väike laps. Ta oli ilmselt väga "
                "näljane. Palju õnne. Oled võitnud!",
                hint="Väljumiseks vajuta suvalist klahvi..."
            ),
            "end": Node("The End. Thank you for playing!"),
        }
        return nodes
