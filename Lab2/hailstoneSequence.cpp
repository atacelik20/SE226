#include <iostream>
using namespace std;
int main() {
    int n;
    cout << "Please enter a number greater than 1:";
    cin >> n;

    while (n <=1) {
        cout << "Please enter a number greater than 1:";
        cin >> n;
    }
    int steps=0;
    cout <<n;
    while (n!=1) {
        if (n%2==0) {
            n = n/2;
        }
        else {
            n = n*3+1;
        }
        cout << n <<" -> ";
        steps++;
    }
    cout << "Total Steps: " << steps << endl;
}