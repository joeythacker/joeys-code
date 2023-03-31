//
//  main.cpp
//  jtingredientadjuster.cpp
///* Program name: jbtictactoe.cpp
//* Purpose: Adjusting ingredient amounts with user input influenced
//  Created by Josiah Thacker
//on 3/31/23.
//

#include <iostream>
#include <iomanip> //for rounding
using namespace std;

int main() {
    // amount of ingredients for the original recipe
    const double SUGAR_PER_COOKIE = 1.5 / 48;
    const double BUTTER_PER_COOKIE = 1.0 / 48;
    const double FLOUR_PER_COOKIE = 2.75 / 48;

    // number of cookies the user wants to make
    int numCookies;
    cout << "How many cookies do you want to make? ";
    cin >> numCookies;

    // Calculate the amount of ingredients needed for number of cookies
    double sugar = SUGAR_PER_COOKIE * numCookies;
    double butter = BUTTER_PER_COOKIE * numCookies;
    double flour = FLOUR_PER_COOKIE * numCookies;

    // Display the amount of ingredients needed
    cout << fixed << setprecision(2); //2 decimal points
    cout << "To make " << numCookies << " cookies, you will need:" << endl;
    cout << sugar << " cups of sugar" << endl;
    cout << butter << " cups of butter" << endl;
    cout << flour << " cups of flour" << endl;

    return 0;
}

