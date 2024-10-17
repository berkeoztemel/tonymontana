using namespace std;

int main()
{
    int counter = 5;
    bool AlwaysTrue = true;
    int Intvalue1 = 10;
    float FloatValue1 = 5.5;

    if (Intvalue1 < FloatValue1 || AlwaysTrue)
        counter++;
    else
        counter = 1;

    while (counter>0)

    {
        counter --;
        AlwaysTrue = !AlwaysTrue;
    }
    if (AlwaysTrue)
        cout << "It is always true";
    else
        cout << "It seems it is not always true after all";
    return 0
}