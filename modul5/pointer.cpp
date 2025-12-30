#include <iostream>
using namespace std;

int main() {
    int x = 10, y = 20;
    int *px = &x, *py = &y;
    cout << "Sebelum: x = " << x << ", y = " << y << endl;
    int temp = *px;
    *px = *py;
    *py = temp;
    cout << "Sesudah: x = " << x << ", y = " << y << endl;
    return 0;
}
