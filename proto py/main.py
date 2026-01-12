"""
Program Pemesanan Tiket Bioskop Sederhana
Fitur: lihat daftar film => pilih film => pilih seat => bayar tiket => cetak tiket
"""
from payment import createPaymentProcessor
# data 
payment = createPaymentProcessor(1000000)
data=[]

debitsaldo=1000000

lsMovies = [(1, "Avengers: Doomsday", 158, 75000, {"Aksi", "Fiksi Ilmiah", "Pahlawan Super"})
            ,(2, "The Batman: Part II", 100, 50000, {"Aksi", "Drama", "Kejahatan"})]

seats = {
    1: [
        [False, True, True, True, True],
        [True, True, False, True, True],
        [True, True, True, True, False],
        [True, False, True, True, True]
    ],
    2: [
        [False, False, False, False, False],
        [False, False, False, False, False],
        [False, False, False, False, False],
        [False, False, False, False, False]
    ]
}
# kumpulan fungsi
def movslct(lsMovies):
    global selectedMovie
    for i, movie in enumerate(lsMovies):
        if len(movie) == 5:
            studio, judul, durasi, harga, genre = movie
            print(f"{i+1}. {judul} ({', '.join(genre)}). Durasi: {durasi} menit. Harga tiket: Rp{harga}. Studio: {studio}")         
    inputMovie = int(input("Pilih film yang ingin ditonton:"))
    selectedMovie = lsMovies[inputMovie-1]
    studio, judul, durasi, harga, genre = selectedMovie
    print(f"Anda memilih film: {judul}")
    return selectedMovie

def seatslct(lsSeats):
    global seatsStudio, lsMovies, selectedMovie
    seatsStudio = lsSeats
    selectedSeats = []
    print("Ketersediaan kursi (O: Tersedia, X: Terisi):")
    for i, row in enumerate(lsSeats):
        print(f"Baris {i+1}: " + " ".join(['O' if seat else 'X' for seat in row]))
    while not stdfull(seatsStudio):
        seatInput = input("Pilih kursi (baris,kolom) atau 'selesai': ").strip()

        if seatInput.lower() == 'selesai':
            break
        try:
            row, col = map(int, seatInput.split(','))
            row -= 1
            col -= 1

            if 0 <= row < len(lsSeats) and 0 <= col < len(lsSeats[0]):
                if lsSeats[row][col]:
                    lsSeats[row][col] = False
                    selectedSeats.append((row+1, col+1))
                    print("Kursi berhasil dipilih.")
                else:
                    print("Kursi sudah terisi.")
            else:
                print("Nomor kursi tidak valid.")
        except:
            print("Format salah! Contoh: 2,3")
    if stdfull(seatsStudio):
        print("Maaf, semua kursi sudah terisi.")
        print("Anda dapat memilih film lain atau jadwal lain.")
        selectedMovie = movslct(lsMovies)
        studio, judul, durasi, harga, genre = selectedMovie
        selectedSeats = seatslct(seats[studio])
    
    return selectedSeats
# validator kursi penuh
def stdfull(seatsStudio):
    return all(not seat for row in seatsStudio for seat in row)

def printTicket(judul, durasi, harga, selectedSeats):
    print("\n--- Tiket Bioskop ---")
    print(f"Film: {judul}")
    print(f"Durasi: {durasi} menit")
    print(f"Harga per tiket: Rp{harga}")
    print("Kursi yang dipilih:")
    for seat in selectedSeats:
        print(f"- Baris {seat[0]}, Kolom {seat[1]}")
    totalHarga = harga * len(selectedSeats)
    print(f"Total Harga: Rp{totalHarga}")
    print("---------------------\n")


#main program
def main():
    print("Daftar film yang tersedia:")
    selectedMovie = movslct(lsMovies)
    studio, judul, durasi, harga, genre = selectedMovie
    print(f"\nAnda akan menonton: {judul}")
    print(f"Studio: {studio}")
    selectedSeats = seatslct(seats[studio])
    if not selectedSeats:
        print("Trimakasih telah berkunjung :).")
        return
    totalHarga = harga * len(selectedSeats)
    if payment(totalHarga):
        printTicket(judul, durasi, harga, selectedSeats)
    if input("Ingin memesan tiket lagi? (y/n): ").lower() == 'y':
        main()
    else :
        print("Terima kasih telah menggunakan layanan kami!")


if __name__ == "__main__":
    main()

