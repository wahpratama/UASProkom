use std::io::{self, Write};
// luas
fn hitung_luas(sisi: f64) -> f64 {
    sisi * sisi
}
// keliling
fn hitung_keliling(sisi: f64) -> f64 {
    4.0 * sisi
}
fn main() {
    print!("Masukkan panjang sisi persegi: ");
    io::stdout().flush().unwrap(); 
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Gagal membaca input");
    let sisi: f64 = input.trim().parse().expect("Input harus berupa angka");
    let luas = hitung_luas(sisi);
    let keliling = hitung_keliling(sisi);
    println!("\n=== Hasil Perhitungan Persegi ===");
    println!("Panjang sisi     : {}", sisi);
    println!("Luas Persegi     : {}", luas);
    println!("Keliling Persegi : {}", keliling);
}
