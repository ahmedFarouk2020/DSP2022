#include <iostream>
#include <iomanip>
#include <complex>
#include <cmath>
#include <valarray> /* val arrsy to easy making slice for the our arry */

using namespace std;

const double PI = 3.14159265359;
typedef complex<double> Complex;
typedef valarray<Complex> CArray;

typedef std::valarray<Complex> CArray;
extern "C"
{
    void calcfft(CArray &samples);
    void fft (double sample_num,double *input,double *real_output,double*img_output);
}

void calcfft(CArray &samples)
{
    const size_t N = samples.size();

    if (N <= 1) {return;}

    // divide
    CArray even = samples[std::slice(0, N/2, 2)];
    CArray  odd = samples[std::slice(1, N/2, 2)];

    // conquer
    calcfft(even);
    calcfft(odd);

    // combine
    for (size_t k = 0; k < N/2; ++k)
    {
        Complex t = std::polar(1.0, -2 * PI * k / N) * odd[k];
        samples[k    ] =(even[k] + t);
        samples[k+N/2] = (even[k] - t);
    }
}
extern "C"

void fft (double sample_num,double *input,double *real_output,double*img_output){


    long vOut = (long)sample_num; //convert sample number to long long 
    Complex test[vOut];

    for (int i = 0; i < sample_num; ++i)
    {
        std::complex<double>sample= input[i]; //for convert every sample to a complex 
        test[i]=sample;
        /* code */
    }

    CArray data(test, sample_num);
    // forward fft
    calcfft(data);

    for (int i = 0; i < sample_num; ++i)
    {
        real_output[i]=data[i].real();
        img_output[i]=data[i].imag();
    }

}
/*end  of  fast  fourer transform */
