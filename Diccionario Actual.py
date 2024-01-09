meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "CREEPY": "Algo aterrador o siniestro",
            "ROFL": "Es una respuesta a una broma",
            "SHEESH": "Es una ligera desaprobación",
            "AGGRO" : "Es ponerse agresivo/enojado",
            }
while True:
    word = input("Escribe una palabra que no entiendas (Con Mayúsculas!!!):")
    
    if word in meme_dict.keys():
        # ¿Qué debemos hacer si se encuentra la palabra?
        print(meme_dict[word])
        salir = input("Quieres seguir investigando? (Si, No):")
        if salir == "No":
            break
        else:
            None
    else:
        # ¿Qué hacer si no se encuentra la palabra?
        print("Esa palabra no se encuentra en mi diccionario!")
