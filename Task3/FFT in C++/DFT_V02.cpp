/* includes */
#include <iostream>
#include <vector>
#include <complex.h>
#include <cmath>
#include <iterator>

using namespace std;
#define M_PI 3.14159265359

    
vector<complex<double>> dft(vector<double> real_input)
{
    // container to store complex result
    vector<complex<double>> complex_output;

    // real, imaginary part of k-th complex element
    double real = 0;
    double imgn = 0;

    // temperary variable to combine real, imaginary pairs inside
    complex<double> temp;

    // number of elements in array
    int N = real_input.size();

    for(int k = 0; k < N; k++){

        // produce one element "S(k)" of complex output
        for(int n = 0; n < N; n++)
        {
            real += cos((2 * M_PI * k * n) / N) * real_input[n];
            imgn += -sin((2 * M_PI * k * n) / N) * real_input[n];
        }

        temp.real(real);
        temp.imag(imgn);

        // push the complex element in the output container
        complex_output.push_back(temp);
    }
    return complex_output;   // O(n2)
}


int main()
{
    vector<complex<double>>complex_out = dft({1564.0,4654.0,46.0,64.0,657.0,897198.0,7897.0,98786
                                                    ,7186,176,716,71,16871867,876});
    vector<complex<double>>::iterator i = complex_out.begin();
    /* print the output */
    cout<<'[';
    for (; i != complex_out.end(); ++i)
        cout << *i << ' ';
    cout<<']';
    return 0;
}