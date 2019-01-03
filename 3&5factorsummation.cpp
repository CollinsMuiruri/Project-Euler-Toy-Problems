#include <iostream>
using namespace std;

int main()
{
    int a;
    int b[] = {a};
    int result=0;

    for(a=0;a<1000;a++ ){
        if(a%3==0 || a%5==0)
        result += a;
        }
        cout<<result<<endl;

    return 0;
}