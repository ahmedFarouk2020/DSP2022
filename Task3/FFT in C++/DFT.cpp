/* includes */
#include <iostream>
#include <vector>
#include <complex.h>
#include <cmath>
#include <iterator>

using namespace std;


#define PI 3.1415926536
typedef complex<double> Complex;
    
extern "C"
{
   void dft2(double* real_input, int N, double* real_out,double* img_out);
}


void dft2(double* real_input, int N, double* real_out,double* img_out)
{
    // container to store complex result
    // vector<double> real_output(0);
    // vector<double> complex_output(0);

    // real, imaginary part of k-th complex element
    double real = 0;
    double imgn = 0;

    // temperary variable to combine real, imaginary pairs inside
    //Complex temp = 0;

    // number of elements in array
    // int N = real_input.size();

    double phase, sine, cosine;

    for(int k = 0; k < N; k++){
        real_out[k] = 0;
        img_out[k] = 0;
        // produce one element "S(k)" of complex output
        for(int n = 0; n < N; n++)
        {
            phase = (-2 * PI * k * n) / N;
            cosine = cos(phase);
            sine = sin(phase);
            
            real_out[k] += real_input[n] * cosine ;
            img_out[k] += real_input[n] * sine ;

        }
        
    }
   // O(n2)
}




int main()
{
    double real_out[3], complex_out[3], input[3];
    input[0] = {112.0};
   int N = 3;
    dft2(input, N, real_out, complex_out);
    cout<< '[';
    for(int i=0; i<N; i++)
        cout<< '(' <<real_out[i]<< ' '<<complex_out[i] << ')' << ',';
    cout<< ']';
    // vector<double>::iterator i = complex_out.begin();
    // vector<double>::iterator a = real_out.begin();
    /* print the output */
    // cout<<'[';
    // for (; i != complex_out.end(); ++i)
    //     cout << *a++ << ' '<< *i << ", ";
    // cout<<']';
    return 0;
}