#include<iostream>
#include<cstring>

using namespace std;


bool lapindrome(char str[])
{
    int length = strlen(str);

    if(length%2==0)
    {
        char left_str[length/2] = "\0";
        char right_str[length/2] = "\0";

        for(int i=0;i<length/2;i++)
        {
            left_str[i] = str[i];
            right_str[i] = str[length/2+i];
            cout << str[length/2+i];
        }

        cout << endl <<left_str << " | " <<  right_str << endl;
    }

    return true;
}

int main()
{
    char str[] = "string";
    lapindrome(str);
    return 0;
}