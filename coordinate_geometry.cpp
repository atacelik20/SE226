#include <iostream>
#include <cmath>
using namespace std;
int main() {
    double x1, y1, x2, y2;
    cout << "Enter the value of x1" << endl;
    cin >> x1;
    cout << "Enter the value of x2" << endl;
    cin >> x2;
    cout << "Enter the value of y1" << endl;
    cin >> y1;
    cout << "Enter the value of y2" << endl;
    cin >> y2;
    double distance = sqrt(pow(x2-x1,2)+pow(y2-y1,2));
    cout << "The distance between two points is " << distance << endl;
    return 0;
}
