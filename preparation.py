import pandas as pd

df = pd.read_csv("2019_accidents_vehicles_gu_bcn_.csv")

trad_dias = {
    "Dilluns": "Lunes",
    "Dimarts": "Martes",
    "Dimecres": "Miércoles",
    "Dijous": "Jueves",
    "Divendres": "Viernes",
    "Dissabte": "Sábado",
    "Diumenge": "Domingo",
}

trad_meses = {
    "Gener": "Enero",
    "Febrer": "Febrero",
    "Març": "Marzo",
    "Abril": "Abril",
    "Maig": "Mayo",
    "Juny": "Junio",
    "Juliol": "Julio",
    "Agost": "Agosto",
    "Setembre": "Septiembre",
    "Octubre": "Octubre",
    "Novembre": "Noviembre",
    "Desembre": "Diciembre",
}

map_causas = {
    "Desobeir el senyal del semàfor": "Sí",
    "Desobeir altres senyals": "Sí",
    "Transitar a peu per la calçada": "Sí",
    "Creuar per fora pas de vianants": "Sí",
    "No és causa del  vianant": "No",
    "Altres": "No",
}

map_tipo_vehic = {
    "Altres vehicles amb motor": "Otros",
    "Autobús articulat": "Autobús",
    "Camió rígid <= 3,5 tones": "Camión",
    "Camió rígid > 3,5 tones": "Camión",
    "Tot terreny": "Turismo",
    "Tractor camió": "Camión",
    "Tren o tramvia": "Tren o tranvia",
    "Turisme": "Turismo",
    "Veh. mobilitat personal sense motor": "Patinete/patín",
    "Veh. mobilitat personal amb motor": "Patinete/patín",
}

df["Descripcio_dia_setmana"] = df["Descripcio_dia_setmana"].replace(trad_dias)
df["Nom_mes"] = df["Nom_mes"].replace(trad_meses)
df["Descripcio_causa_vianant"] = df["Descripcio_causa_vianant"].replace(map_causas)
df["tipo_vehiculo"] = df["Descripcio_tipus_vehicle"].replace(map_tipo_vehic)


cols = [
    "Nom_districte",
    "Nom_barri",
    "Descripcio_dia_setmana",
    "Nom_mes",
    "Dia_mes",
    "Hora_dia",
    "Descripcio_causa_vianant",
    "Descripcio_tipus_vehicle",
    "tipo_vehiculo",
    "Descripcio_model",
    "Descripcio_marca",
    "Descripcio_color",
    "Descripcio_carnet",
    "Antiguitat_carnet",
    "Longitud",
    "Latitud",
]
df = df[cols]
df.to_csv("dataset_accidentes.csv", index=False)
