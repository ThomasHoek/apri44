#include <iostream>
#include <string>

// Function to count the amount of times a letter occures in a string.
int countingLetters(std::string input,char c){
    int total = 0;
    for (int i = 0; i < input.size(); i++){
        
        if (input[i] == c){
            total = total + 1;
        }
    }
    return total;
}

// main
int main(){

    std::string sentence("Always an airplane heading towards Arizona");
    char c  = 'a';

    int amount = countingLetters(sentence, c);
    std::cout << "The sentence is: " << sentence << std::endl;
    std::cout << "It has: " << amount << " times the letter: " << c << std::endl;

    return 0;
}