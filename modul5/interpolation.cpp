#include <iostream>
#include <algorithm>
using namespace std;
int main() {
    int data[10] = {20, 21, 50, 63, 54, 84, 11, 10, 7, 99};
    int n = sizeof(data) / sizeof(data[0]);
    cout << "Data awal: "; for (int i = 0; i < n; i++) cout << data[i] << " ";cout << endl;
    sort(data, data + n);
    cout << "Data terurut: "; for (int i = 0; i < n; i++) cout << data[i] << " "; cout << endl;
    int caridata;
    cout << "Data yang dicari: ";cin >> caridata;
    int awal = 0, akhir = n - 1, proses = 0;
    bool ditemukan = false;
    while (awal <= akhir) {
        proses++;  
        if (data[awal] == data[akhir] && data[awal] == caridata) {
            cout << "Data ditemukan pada indeks ke " << awal + 1 << endl;
            ditemukan = true;
            break;
        }
        if (data[akhir] == data[awal]) {
            break;
        }
        int posisi = awal + ((caridata - data[awal]) * (akhir - awal)) / 
                    (data[akhir] - data[awal]);
        if (data[posisi] == caridata) {
            cout << "Data ditemukan pada indeks ke " << posisi + 1 << endl;
            ditemukan = true;
            break;
        }
        else if (data[posisi] < caridata) {
            awal = posisi + 1;
        }
        else {
            akhir = posisi - 1;
        }
    }
    if (!ditemukan) {
        cout << "Data tidak ditemukan" << endl;
    } return 0;
}