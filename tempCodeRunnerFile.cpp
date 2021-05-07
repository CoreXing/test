#include <iostream>
#include <string>
using namespace std;
#define ac                            \
    ios_base::sync_with_stdio(false); \
    cin.tie(NULL);
int main()
{
    //ac
    int number;
    while (cin >> number)
    {
        int X=1;
        while (X < number)
        {
            cout << X << " ";
            X++;
        }
        cout << "\n";
    }
}