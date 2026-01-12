def createPaymentProcessor(initial_saldo):
    saldo = initial_saldo

    def processPayment(totalHarga):
        nonlocal saldo
        if saldo >= totalHarga:
            saldo -= totalHarga
            print(f"Pembayaran berhasil! Sisa saldo Anda: Rp{saldo}")
            return True
        else:
            print("Saldo tidak mencukupi.")
            return False

    return processPayment
