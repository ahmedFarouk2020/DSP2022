#include <vector>
#include <complex>
#include <iostream>

const double PI = 3.14159265359;

typedef std::complex<double> Complex;
typedef std::vector<Complex> ComplexVector;

ComplexVector FFT (ComplexVector Data){
    int Size = Data.size(); //get the size of the data vector

    if (Size == 1){return Data;}//checks if the data vector has reached only 1 sample or not,

    ComplexVector EvenDataSamples(Size/2), OddDataSamples(Size/2);// created 2 complex vectors for even and odd vector of a size equal to that of the data vector and has initial values of 0 (all elements in it is 0).
    for (int i = 0; i != Size/2 ; i++) // here we fill the new vectors with even and odd sample data
    {
        EvenDataSamples[i] = Data[2*i];
        OddDataSamples[i] = Data[(2*i)+1];
    }

    ComplexVector Even(Size/2), Odd(Size/2) , FinalFrequencies(Size); // 3 new vectors to contain the new  even,odd, and final frequencies.


    Even = FFT(EvenDataSamples), Odd = FFT(OddDataSamples); // recursively spliting the data to even and odd  till we have a vector with 1 data sample

    for (int k; k != Size; k++) // combine the results of all the even and odd summations
    {
        Complex CommonComplexEXP = std::polar(1.0,-2*PI*k/Size)* Odd[k]; // calculating the common exponential and multiplying it by the odd 

        FinalFrequencies[k] = Even[k] + CommonComplexEXP; 

        FinalFrequencies[k+(Size/2)] = Even[k] - CommonComplexEXP;
    }
    

    return FinalFrequencies;
}
