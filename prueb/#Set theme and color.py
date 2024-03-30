def dic_list(cardio_data):
    divider = ","
    with open(cardio_data, encoding="utf-8") as file:
        next(file)  # Omitir encabezado del archivo
        patients = []
        for line in file:
            line = line.rstrip("\n")
            column = line.split(divider)
            id = column[0]
            age = int(column[1])
            gender = int(column[2])
            height = int(column[3])
            weight = float(column[4])
            ap_hi = int(column[5])
            ap_lo = int(column[6])
            cholesterol = int(column[7])
            gluc = int(column[8])
            smoke = int(column[9])
            alco = int(column[10])
            active = int(column[11])
            cardio = int(column[12])
            patients.append({
                "id": id,
                "age": age,
                "gender": gender,
                "height": height,
                "weight": weight,
                "systolic pressure": ap_hi,
                "diastolic pressure": ap_lo,
                "cholesterol": cholesterol,
                "glucose": gluc,
                "smoke": smoke,
                "acohol": alco,
                "activity": active,
                "disease": cardio,
            })
        return patients