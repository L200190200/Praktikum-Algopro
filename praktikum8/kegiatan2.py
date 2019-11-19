def konversiSuhu(C = "none", F = "none"):
    if C == "none" and F == "none":
            print("Suhu 0 Celcius setara dengan 32 Fahrenheit")
    elif F == "none":
        C1 = C * 9 / 5 + 32
        C1 = int(C1)
        print("Suhu", C, "Celcius setara dengan", C1, "Fahrenheit")
    elif C == "none":
        F1 = (F - 32) * 5 / 9
        F1 = int(F1)
        print("Suhu", F, "Fahrenheit setara dengan", F1, "Celcius")
