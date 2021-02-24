# Napisz program zmieniający skalę w stopniach Fahrenheita na naszą w Celcjuszach.
# Program powinen wykonać się w pętli od 0 do 200 stopni Fahrenheit, co 20 stopni.
# C = 5/9 * (F - 32) # wzór Celsjusz → Fahrenheit
# Napisz rozwiązanie zarówno z użyciem pętli while jak i for.

temperature_F = 0
while temperature_F < 201:
    temperature_C = round(5.0/9.0 * (temperature_F - 32),2)
    print("Temperatura to:", temperature_C, "Celsjusza.")
    temperature_F = temperature_F + 20
