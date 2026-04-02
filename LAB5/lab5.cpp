#include <iostream>
using namespace std;

double alternatingSeries(int n) {
    if (n == 1) {
        return 1.0;
    }

    if (n % 2 == 0) {
        return alternatingSeries(n - 1) - (1.0 / n);
    }
        return alternatingSeries(n - 1) + (1.0 / n);

}

int main() {
    int n;
    cout << "Enter n value: ";
    cin >> n;

    cout << "Result of alternating series = " << alternatingSeries(n) << endl;

    return 0;
}