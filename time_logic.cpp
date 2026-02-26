#include <iostream>
using namespace std;
int main() {
    long long totalSeconds;
    cout << "Please enter total seconds" << endl;
    cin>>totalSeconds;
    long long hours = totalSeconds / 3600;
    long long remainingSeconds = totalSeconds%3600;
    long long minutes = remainingSeconds/60;
    long long seconds = remainingSeconds%60;
    cout << totalSeconds << " Seconds "<< "is " << hours << " Hours, " << minutes << " Minutes, " << seconds << " Seconds." << endl;
    return 0;
}
