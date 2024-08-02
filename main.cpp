// Grayson Zhu textbased game
// main.cpp

#include <iostream>
#include <string>
using namespace std;

int main() {
//variables
    string name;
    
    int techp = 0;
    int medp = 10;
    int psychp = 50;
    int combp = 75;
    int stamp = 100;
    
//intro text
    cout << "Hello, Battlers and Broads!"; endl;
    cout << "You all are now purveyors of the new text-based game which will determine; endl;
    cout << "the fate of the entire world! Bahahahahaha!!!!!"; endl;
    cout << "Choose your player name now: "; endl;
    getline (cin, name);
    cout << "Welcome, " << name  << ", " << "your destiny awaits...";
    
  
    return 0;
}
