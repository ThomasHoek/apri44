#include <iostream>

// basic function
int add(int a, int b){          
    return (a + b);
}

//  main to call function
int main(){
    int a = 5;
    int b = 3;
    int c =  add(a,b);
    std::cout << c << std::endl;
    return 0;
}

//  main  returns 0 -> run succesful