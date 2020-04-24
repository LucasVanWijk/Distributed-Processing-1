import requests
import pandas as pd


def read_to_df(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    f.close()

    header_size = 0
    for x in lines:
        if x[0] == "#":
            header_size += 1

    columns = lines[header_size - 2][6:].replace("\n", "").replace(' ', '').split(',')
    columns[0] = 'date'
    values = []
    for x in lines[header_size:]:
        x = x[6:].replace("\n", "").replace(" ", "").split(",")
        values.append(x)
    df = pd.DataFrame(values, columns=columns)
    df.date = pd.to_datetime(df.date, format='%Y-%m-%d')
    return df


def collect_weather(start, end, vars, filename):
    url = "http://projects.knmi.nl/klimatologie/daggegevens/getdata_dag.cgi"
    data = {
        'start': start,
        'end': end,
        'stns': '240',
        'vars': vars
    }
    x = requests.post(url, data=data)

    f = open(filename, 'w')
    f.write(x.text.replace("\n", ""))
    f.close()

data_dictionary = """
DDVEC	Vectorgemiddelde windrichting in graden (360=noord, 90=oost, 180=zuid, 270=west, 0=windstil/variabel). Zie http://www.knmi.nl/kennis-en-datacentrum/achtergrond/klimatologische-brochures-en-boeken
FHVEC	Vectorgemiddelde windsnelheid (in 0.1 m/s). Zie http://www.knmi.nl/kennis-en-datacentrum/achtergrond/klimatologische-brochures-en-boeken
FG	Etmaalgemiddelde windsnelheid (in 0.1 m/s)
FHX	Hoogste uurgemiddelde windsnelheid (in 0.1 m/s)
FHXH	Uurvak waarin FHX is gemeten
FHN	Laagste uurgemiddelde windsnelheid (in 0.1 m/s)
FHNH	Uurvak waarin FHN is gemeten
FXX	Hoogste windstoot (in 0.1 m/s)
FXXH	Uurvak waarin FXX is gemeten
TG	Etmaalgemiddelde temperatuur (in 0.1 graden Celsius)
TN	Minimum temperatuur (in 0.1 graden Celsius)
TNH	Uurvak waarin TN is gemeten
TX	Maximum temperatuur (in 0.1 graden Celsius)
TXH	Uurvak waarin TX is gemeten
T10N	Minimum temperatuur op 10 cm hoogte (in 0.1 graden Celsius)
T10NH	6-uurs tijdvak waarin T10N is gemeten
SQ	Zonneschijnduur (in 0.1 uur) berekend uit de globale straling (-1 voor <0.05 uur)
SP	Percentage van de langst mogelijke zonneschijnduur
Q	Globale straling (in J/cm2)
DR	Duur van de neerslag (in 0.1 uur)
RH	Etmaalsom van de neerslag (in 0.1 mm) (-1 voor <0.05 mm)
RHX	Hoogste uursom van de neerslag (in 0.1 mm) (-1 voor <0.05 mm)
RHXH	Uurvak waarin RHX is gemeten
PG	Etmaalgemiddelde luchtdruk herleid tot zeeniveau (in 0.1 hPa) berekend uit 24 uurwaarden
PX	Hoogste uurwaarde van de luchtdruk herleid tot zeeniveau (in 0.1 hPa)
PXH	Uurvak waarin PX is gemeten
PN	Laagste uurwaarde van de luchtdruk herleid tot zeeniveau (in 0.1 hPa)
PNH	Uurvak waarin PN is gemeten
VVN	Minimum opgetreden zicht
VVNH	Uurvak waarin VVN is gemeten
VVX	Maximum opgetreden zicht
VVXH	Uurvak waarin VVX is gemeten
NG	Etmaalgemiddelde bewolking (bedekkingsgraad van de bovenlucht in achtsten, 9=bovenlucht onzichtbaar)
UG	Etmaalgemiddelde relatieve vochtigheid (in procenten)
UX	Maximale relatieve vochtigheid (in procenten)
UXH	Uurvak waarin UX is gemeten
UN	Minimale relatieve vochtigheid (in procenten)
UNH	Uurvak waarin UN is gemeten
EV24	Referentiegewasverdamping (Makkink) (in 0.1 mm)
"""