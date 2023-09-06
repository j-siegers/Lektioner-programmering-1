registrerade = [" Anna ", "Eva ", " Erik ", " Lars ", " Karl "]
avanmälningar = [" Anna ", " Erik ", " Karl "]
for reg in registrerade:
    if reg in avanmälningar:
        registrerade.remove(reg)
print(registrerade)
