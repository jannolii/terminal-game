# terminal-mäng

## Ülevaade

See projekt on tekstipõhine terminalimäng, kus mängijad liiguvad läbi loo, tehes valikuid, mis mõjutavad tulemust. Mängul on otsustuspuu struktuur, mis viib erinevate lõppudeni, sõltuvalt mängija otsustest.

## Projekti struktuur

```txt
terminal-game
├── src
│   ├── game.py          # Mängu peamine käivituspunkt
│   ├── screens.py       # Funktsioonid erinevate ekraanide kuvamiseks
│   └── decision_tree.py  # Määratleb otsustuspuu struktuuri
├── requirements.txt      # Loetleb sõltuvused
└── README.md             # Projekti dokumentatsioon
```

## Paigaldamine

Mängu käivitamiseks peate installima vajalikud sõltuvused. Seda saate teha, käivitades oma terminalis järgmise käsu:

```bash
pip install -r requirements.txt
```

## Mängu käivitamine

Pärast sõltuvuste installimist saate mängu alustada, käivitades järgmise käsu:

```bash
python src/game.py
```

## Mängu omadused

- **Tervitus**: Mäng algab kaasahaarava tervitusekraaniga, mis seab seikluse tooni.
- **Otsustuspuu**: Mängijad teevad valikuid, mis viivad loo erinevatele radadele, mille tulemuseks on erinevad lõpud.
- **Narratiivsed ekraanid**: Mäng sisaldab mitmeid narratiivseid ekraane, mis rikastavad jutustamiskogemust.

## Kaasamine

Kui soovite projekti panustada, esitage julgelt tõmbepäring või avage arutelu jaoks probleem.

## Litsents

See projekt on avatud lähtekoodiga ja saadaval MIT litsentsi alusel.
