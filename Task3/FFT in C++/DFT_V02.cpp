/* includes */
#include <iostream>
#include <vector>
#include <complex.h>
#include <cmath>
#include <iterator>

using namespace std;
#define PI 3.1415926536
typedef complex<double> Complex;
    
vector<Complex> dft2(vector<Complex> real_input)
{
    // container to store complex result
    vector<Complex> complex_output(0);

    // real, imaginary part of k-th complex element
    double real = 0;
    double imgn = 0;

    // temperary variable to combine real, imaginary pairs inside
    Complex temp = 0;

    // number of elements in array
    int N = real_input.size();

    double phase, sine, cosine;

    for(int k = 0; k < N; k++){
        real = 0;
        imgn = 0;
        // produce one element "S(k)" of complex output
        for(int n = 0; n < N; n++)
        {
            phase = (-2 * PI * k * n) / N;
            cosine = cos(phase);
            sine = sin(phase);
            std::cout<< "cos: " <<cosine<< '\n';
            real += real_input[n].real() * cosine - real_input[n].imag() * sine;

            imgn += real_input[n].real() * sine + real_input[n].imag() * cosine ;
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
    vector<Complex>complex_out = dft2({13251,12,15});
    vector<Complex>::iterator i = complex_out.begin();
    /* print the output */
    cout<<'[';
    for (; i != complex_out.end(); ++i)
        cout << *i << ' ';
    cout<<']';
    return 0;
}