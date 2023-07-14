#include <iostream>

using namespace std;

int main()
{
    int N1 = 0;
    int N2 = 0;
    int R = 0;
    int operation;
    
    cout << "***CALCULATOR :)***" << endl;
    cout << "1.Add"<< endl;
    cout << "2.Subtract"<< endl;
    cout << "3.Multiply"<< endl;
    cout << "4.Divide"<< endl;
    cout << "Enter the operation you want to perform"<< endl;
    cin >> operation;
    switch (operation)
    {
        case 1: cout << "Your election is Add" << endl;
        cout << "Enter the first number"<<endl;
        cin >> N1;
        cout << "Enter the second number"<<endl;
        cin >> N2;
        R = N1 + N2;
        cout << "The result of the add is:" << R << endl;
        break;
        
        case 2: cout << "Your election is subtract" << endl;
        cout << "Enter the first number"<<endl;
        cin >> N1;
        cout << "Enter the second number"<<endl;
        cin >> N2;
        R = N1 - N2;
        cout << "The result of the subtract is:" << R << endl;
        break;
        
        case 3: cout << "Your election is Multiply" << endl;
        cout << "Enter the first number"<<endl;
        cin >> N1;
        cout << "Enter the second number"<<endl;
        cin >> N2;
        R = N1 * N2;
        cout << "The result of the Multiply is:" << R << endl;
        break;
        
        case 4: cout << "Your election is Divide" << endl;
        cout << "Enter the first number"<<endl;
        cin >> N1;
        cout << "Enter the second number"<<endl;
        cin >> N2;
        R = N1/N2;
        cout << "The result of the Divide is:" << R << endl;
        break;
        
        default:cout << "***ERROR IN CALCULATOR :(***";
        
    }
    
    
    
    
}