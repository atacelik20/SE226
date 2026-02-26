#include <iostream>
#include <string>
using namespace std;
int main() {
    string name;
    cout << "What is your name?" << endl;
    getline(cin, name);
    cout << "Hello " << name << endl;

    string StudentId;
    cout << "What is your Student ID?" << endl;
    getline(cin, StudentId);
    cout << "Your ID is " << StudentId << endl;
    return 0;
}