import json

hair = {
    "black": "CCAGCAATCGC",
    "brown": "GCCAGTGCCG",
    "blonde": "TTAGCTATCGC"
}

facial = {
    "square": "GCCACGG",
    "round": "ACCACAA",
    "oval": "AGGCCTCA"
}

eye = {
    "blue": "TTGTGGTGGC",
    "green": "GGGAGGTGGC",
    "brown": "AAGTAGTGAC"
}

gender = {
    "female": "TGAAGGACCTTC",
    "male": "TGCAGGAACTTC"
}

race = {
    "white": "AAAACCTCA",
    "black": "CGACTACAG",
    "asian": "CGCGGGCCG"
}

with open("dna.txt", "r") as dna:
    dna_read = dna.read()

print("Program for matching dna with evidence dna from crime scene...")
new_suspect = input("Do you need to enter suspect characteristics into evaluation (y/n): ")

if new_suspect.lower() == "y":
    suspect_name = input("Input name of the suspect: ")
    suspect_gender = input("Input gender of the suspect (female/male): ")
    suspect_race = input("Input race of the suspect (white/black/asian): ")
    suspect_hair_color = input("Input hair color of the suspect (black/brown/blonde): ")
    suspect_eye_color = input("Input eye color of the suspect (blue/green/brown): ")
    suspect_facial = input("Input face shape of the suspect (square/round/oval): ")

    with open("suspects.json", "r") as suspects:
        suspects_list = json.loads(suspects.read())

    suspects_list.append({"name": suspect_name.lower(),
                          "gender": suspect_gender.lower(),
                          "race": suspect_race.lower(),
                          "hair": suspect_hair_color.lower(),
                          "eye": suspect_eye_color.lower(),
                          "facial": suspect_facial.lower()})

    with open("suspects.json", "w") as suspects:
        suspects.write(json.dumps(suspects_list))


execute = input("Do you want to match suspects dna and evidence dna from crime scene? (y/n): ")
if execute.lower() == "y":
    with open("suspects.json", "r") as suspects:
        suspects_list = json.loads(suspects.read())

        for item in suspects_list:
            name_match = item["name"]
            gender_match = item["gender"]
            race_match = item["race"]
            hair_match = item["hair"]
            eye_match = item["eye"]
            facial_match = item["facial"]

            if dna_read.find(gender[gender_match]) != -1\
                    and dna_read.find(race[race_match]) != -1\
                    and dna_read.find(hair[hair_match]) != -1\
                    and dna_read.find(eye[eye_match]) != -1\
                    and dna_read.find(facial[facial_match]) != -1:
                print(f"Suspect which characteristics that are matching dna evidence is {name_match.upper()}.")
