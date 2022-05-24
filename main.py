adnuno = "TACAAATTTCCCGATCAGTCACTGAAGTCGCTAGCTAGGGGCCCATCGCCGATC"
resultado = ""
for i in adnuno:
    match i:
        case "T":
            resultado += "A"
        case "A":
            resultado += "T"
        case "C":
            resultado += "G"
        case "G":
            resultado += "C"

print(resultado)


