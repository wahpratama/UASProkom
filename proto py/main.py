def movslct(lsMovies):
    for i, movie in enumerate(lsMovies):
        if len(movie) == 5:
            studio, judul, durasi, harga, genre = movie
            print(f"{i+1}. {judul} ({', '.join(genre)}). Durasi: {durasi} menit. Harga tiket: Rp{harga}")         
    inputMovie = int(input("Pilih film yang ingin ditonton:"))
    return inputMovie - 1
    
def seatslct(lsSeats):
    selectedSeats=[]
    print("Ketersediaan kursi (O: Tersedia, X: Terisi):")

    for i, row in enumerate(lsSeats[1:]):
        print(f"Baris {i+1}: " + " ".join(['O' if seat else 'X' for seat in row]))
    while True:
        print("Masukkan kursi yang ingin dipilih (format: baris,kolom) atau 'selesai' untuk mengakhiri:")
        selectedSeats.append(inputSeatInput := input())
        seatInput = inputSeatInput.strip()
        if seatInput.lower() == 'selesai':
            break
def stdfull(seatsStudio):
    return all(
        not seat
        for row in seatsStudio
        for seat in row
    )
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

print("Daftar film yang tersedia:")
selectedMovie = lsMovies[movslct(lsMovies)]
studio, judul, durasi, harga, genre = selectedMovie
print(f"Anda memilih film: {judul}")
selectedSeats = seatslct(seats[studio-1])