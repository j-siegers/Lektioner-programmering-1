class BankAccount:
    def __init__(self, konto_nr, saldo: int):
        self.konto_nr = konto_nr
        self.saldo = saldo

    def insattning(self, pengar_in: int):
        self.saldo += pengar_in
        return self.saldo

    def uttag(self, pengar_ut: int):
        self.saldo -= pengar_ut
        return self.saldo


konto = BankAccount(12345, 100)
print('Före:', konto.saldo)
konto.insattning(50)
print('Efter insättning:', konto.saldo)
konto.uttag(30)
print('Efter uttag:', konto.saldo)




