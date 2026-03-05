#include <iostream>
using namespace std;
int main() {
    int x;
    cout << "Please enter a number between 3 and 9 ";
    cin >> x;

    while (x > 9 || x < 3) {
        cout << "Please enter a number between 3 and 9 ";
        cin >> x;
    }
    for (int i = 1; i <= 2*x; i++) {
        int y = x-abs(x-i);

        for (int j = 0; j < y; j++) {
            cout << "*";
        }
        cout << endl;
    }
}