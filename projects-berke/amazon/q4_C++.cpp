include <iostream>
using namespace std;
#define noop

int main()
{

    //basic math and types
    int a= 10;
    int b = 4;
    int c = 0;
    c = a / b;

    cout << "c=" << c << endl;

    //array and loop
    int IntArray[7];
    IntArray[0] = 1;
    IntArray[1] 1;

    for (int iter =2; iter < 7; iter++)
    {
        IntArray[iter] = IntArray[iter - 1] +IntArray[iter - 2];
    }
    cout << "IntArray[6]=" << IntArray[6] endl;

}
