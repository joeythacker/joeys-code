//  jtrestrauntbill.cpp
//  Created by Josiah Thacker
//3/31/23.
//Purpose is to show user their meal charge while computing the tax, and tip on the bill

#include <iostream>
using namespace std;

int main() {
    double meal_charge = 32.95;
    double tax_rate = 0.0675;
    double tip_rate = 0.20;
    
    // Calculate the tax and tip
    double tax_amount = meal_charge * tax_rate;
    double total_with_tax = meal_charge + tax_amount;
    double tip_amount = total_with_tax * tip_rate;
    
    // Calculate the total cost
    double total_cost = meal_charge + tax_amount + tip_amount;
    
    // Print the results
    cout << "Meal Charge: $" << meal_charge << endl;
    cout << "Tax: $" << tax_amount << endl;
    cout << "Tip: $" << tip_amount << endl;
    cout << "Total Cost: $" << total_cost << endl;
    
    return 0;
}


