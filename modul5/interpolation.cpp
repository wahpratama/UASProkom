#include <iostream>
using namespace std;

//sortir data
void bubbleSort(int data[], int n) {
    int temp;
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - 1 - i; j++) {
            if (data[j] > data[j + 1]) {
                temp = data[j];
                data[j] = data[j + 1];
                data[j + 1] = temp;
            }
        }
    }
}


int main() {
    int i, n, caridata, posisi, awal, akhir, proses;
    bool berhenti = false;
    int data[10]  = {20, 21, 50, 63, 54, 84, 11, 10, 7, 99};
    cout << "Data awal: ";
    for (i = 0; i < n; i++) {
        cout << data[i] << " ";
    }
    n = sizeof(data) / sizeof(data[0]);
    bubbleSort(data, n);
    cout << "Data yang telah diurutkan: ";
    for (i = 0; i < n; i++) {
        cout << data[i] << " ";
    }
    cout << endl;
    awal = 0;
    akhir = n - 1;
    proses = 0;
    cout << "data yang dicari: ";
    cin >> caridata;
    while (awal <= akhir && !berhenti) {
        proses++;
        posisi = awal + ((caridata - data[awal]) * (akhir - awal)) / (data[akhir] - data[awal]);
        if (posisi < awal || posisi > akhir) {
            berhenti = true;
            break;
        }
        if (data[posisi] == caridata) {
            cout << "Data " << caridata << " pada posisi indeks ke " << posisi + 1 << endl;
            berhenti = true;
        } else if (data[posisi] < caridata) {
            awal = posisi + 1;
        } else {
            akhir = posisi - 1;
        }
    }
    if (!berhenti) {
        cout << "Data " << caridata << " tidak ditemukan." << endl;
    }

    return 0;
}