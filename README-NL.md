# Analyse van Luchtkwaliteitsgegevens

Deze code analyseert luchtkwaliteitsgegevens die zijn verzameld van verschillende sensoren. Het script maakt gebruik van de **Pandas** en **Matplotlib** bibliotheken om de gegevens te lezen, te manipuleren en te visualiseren.

## Aan de slag

Om te beginnen, moet je **Python 3.x** geïnstalleerd hebben op je computer. Daarnaast dien je ook de **Pandas** en **Matplotlib** bibliotheken te installeren.

```` terminal
pip install pandas matplotlib
````

Nadat je **Python** en de benodigde bibliotheken hebt geïnstalleerd, kun je het script uitvoeren met behulp van de volgende opdracht:

```` terminal
python main.py
````

Het script zal je vragen om een ID in te voeren voor de luchtkwaliteitsgegevens die je wilt analyseren. Nadat je een geldig ID hebt ingevoerd, leest het script de gegevens uit een **CSV**-bestand, maakt de gegevens schoon en transformeert ze en maakt het tenslotte een grafiek van de gegevens voor het opgegeven ID.

## Data Cleaning en Transformatie

Het script voert de volgende schoonmaak- en transformatiestappen uit op de luchtkwaliteitsgegevens:

* Kopieert het originele **CSV**-bestand naar een nieuw bestand genaamd **data.csv**.
* Leest de gegevens uit **data.csv** in een **Pandas DataFrame**.
* Vraagt de gebruiker om een ID voor de gegevens die ze willen analyseren.
* Rondt de tijdswaarden in de **DataFrame** af op de dichtstbijzijnde 10 minuten.
* Extraheert het laatste deel van de ID-string uit de eerste kolom in de **DataFrame**.
* Filtert de **DataFrame** om alleen rijen met het opgegeven ID op te nemen.

## Visualisatie

Nadat de gegevens zijn schoongemaakt en getransformeerd, plot het script een grafiek van de gegevens met behulp van **Matplotlib**. De grafiek toont de hoeveelheid verschillende luchtverontreinigende stoffen (**pm1**, **pm2.5**, **pm4** en **pm10**) in de loop van de tijd.

## Conclusie

Dit script biedt een eenvoudig voorbeeld van hoe je luchtkwaliteitsgegevens kunt lezen, schoonmaken, transformeren en visualiseren met behulp van **Python** en de **Pandas** en **Matplotlib** bibliotheken. Met enkele aanpassingen kan dit script ook worden aangepast om andere soorten tijdreeksgegevens te analyseren.
