def calculate_risk(deforestation, gunshot, intruder):
    score = 0

    if deforestation:
        score += 40
        print("⚠ Deforestation Risk Added: +40")

    if gunshot:
        score += 35
        print("⚠ Gunshot Risk Added: +35")

    if intruder:
        score += 25
        print("⚠ Intruder Risk Added: +25")

    return min(score, 100)
