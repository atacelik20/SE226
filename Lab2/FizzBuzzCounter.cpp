#include <iostream>
using namespace std;
int main() {
    int n;
    cout << "Please enter a number between 10 and 100:";
    cin >> n;

    while (n <=10||n>=100) {
        cout << "Please enter a number between 10 and 100:";
        cin >> n;
    }
    int fizz=0, buzz=0, fizzbuzz=0;
    for (int i = 1; i <= n; i++) {
        if (i%7==0) {
            continue;
        }
        if (i%3==0&&i%5==0) {
            cout << "Fizzbuzz" << endl;
            fizzbuzz++;
        }
        else if (i%3==0) {
            cout << "Fizz" << endl;
            fizz++;
        }
        else if (i%5==0) {
            cout << "Buzz" << endl;
            buzz++;
        }
        else {
            cout << i << endl;
        }

    }
    cout <<"--- Summary ---"<< endl;
    cout << "Fizz Count: " << fizz << endl;
    cout << "Buzz Count: " << buzz << endl;
    cout << "Fizz Buzz Count: " << fizzbuzz << endl;

}