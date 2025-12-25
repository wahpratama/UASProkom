"""
Program Pemesanan Tiket Bioskop Sederhana
Fitur: lihat daftar film => pilih film => pilih seat => bayar tiket => cetak tiket
"""
# kumpulan fungsi
def movslct(lsMovies):
    global selectedMovie, studio, judul, durasi, harga, genre
    for i, movie in enumerate(lsMovies):
        if len(movie) == 5:
            studio, judul, durasi, harga, genre = movie
            print(f"{i+1}. {judul} ({', '.join(genre)}). Durasi: {durasi} menit. Harga tiket: Rp{harga}")         
    inputMovie = int(input("Pilih film yang ingin ditonton:"))
    print(f"Anda memilih film: {judul}")
    global selectedMovie
    return lsMovies[inputMovie - 1]

def seatpdt(lsSeats, row, col):
    if 0 <= row < len(lsSeats) and 0 <= col < len(lsSeats[0]):
        if lsSeats[row][col]:
            lsSeats[row][col] = False
            print(f"Kursi di baris {row + 1}, kolom {col + 1} berhasil dipilih.")
        else:
            print(f"Kursi di baris {row + 1}, kolom {col + 1} sudah terisi. Silakan pilih kursi lain.")
    else:
        print("Input kursi tidak valid. Silakan coba lagi.")

def seatslct(lsSeats):
    global selectedMovie, studio, judul, durasi, harga, genre
    selectedSeats=[]
    print("Ketersediaan kursi (O: Tersedia, X: Terisi):")
    for i, row in enumerate(lsSeats[1:]):
        print(f"Baris {i+1}: " + " ".join(['O' if seat else 'X' for seat in row]))
    if stdfull(lsSeats[1:]):
        selectedMovie = lsMovies[movslct(lsMovies)]
        studio, judul, durasi, harga, genre = selectedMovie
        print("Maaf, semua kursi sudah penuh. pilih film atau jam lain.")
        return 
    else:
        while not stdfull(lsSeats[1:]):
            print("Masukkan kursi yang ingin dipilih (format: baris,kolom) atau 'selesai' untuk mengakhiri:")
            selectedSeats.append(inputSeatInput := input())
            seatInput = inputSeatInput.strip()
            if seatInput.lower() == 'selesai':
                break

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

# data 
data=[]

lsMovies = [(1, "Avengers: Doomsday", 158, 75000, {"Aksi", "Fiksi Ilmiah", "Pahlawan Super"})
            ,(2, "The Batman: Part II", 100, 50000, {"Aksi", "Drama", "Kejahatan"})]

seats = [[1,[False, True, True, True, True],
              [True, True, False, True, True],
              [True, True, True, True, False],
              [True, False, True, True, True]],
            [2,[False, False, False, False, False],
            [False, False, False, False, False],
            [False, False, False, False, False],
            [False, False, False, False, False]]]

#pemrosesan utama
def main():
    print("Daftar film yang tersedia:")
    selectedMovie = movslct(lsMovies)
    print(f"baik kamu akan menonton film {judul}\n")
    selectedSeats = seatslct(seats[studio-1][0:])


if __name__ == "__main__":
    main()

