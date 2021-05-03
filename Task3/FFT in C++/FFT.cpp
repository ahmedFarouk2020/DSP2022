#include <iostream>
#include <valarray> // A class that allows me to do mathematical operations on arrays
#include <complex>  //to contain complex values

const double PI = 3.14159265359;

typedef std::complex<double> Complex;
typedef std::valarray<Complex> ComplexArray;


void FFT(ComplexArray& data){
    const size_t  size = data.size();
    if (size <= 1 ) return;
    //devide the array into even and odd based on indecies
    ComplexArray Even = data[std::slice(0,size/2,2)];
    
    ComplexArray Odd = data[std::slice(1,size/2,2)]; 
    //repeat the division till array size is 1
    FFT(Even);
    FFT(Odd);
    
    //calculate the complex values and put it back in the same array called data
    for (size_t k = 0 ; k < size/2 ; ++k)
    {
        Complex T = std::polar(1.0,-2 * PI * k/size) * Odd[k];
        data[k] = Even[k]+T;
        data[k+(size/2)] = Even[k]-T;

    }
    

}
