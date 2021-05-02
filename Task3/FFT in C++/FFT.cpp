#include <iostream>
#include <valarray> // A class that allows me to do mathematical operations on arrays
#include <complex>  //to contain complex values

const double PI = 3.14159265359;


typedef std::complex<double> Complex;
typedef std::valarray<Complex> ComplexArray;
/* NOTE: THIS FUNCTION IS NOT WORKING PROPERLY!
 * NOTE: THIS FUNCTION IS NOT WORKING PROPERLY! 
 * NOTE: THIS FUNCTION IS NOT WORKING PROPERLY! 
 * NOTE: THIS FUNCTION IS NOT WORKING PROPERLY! 
 * NOTE: THIS FUNCTION IS NOT WORKING PROPERLY! 
 * NOTE: THIS FUNCTION IS NOT WORKING PROPERLY! 
 * NOTE: SEE THE VIDEO AND MIMIC HIS LOGIC
 */
void FFT(ComplexArray& data){
    const size_t  size = data.size();
    if (size == 1 ) return;
    //devide the array into even and odd based on indecies
    ComplexArray Even = data[std::slice(0,size/2,2)];
    
    ComplexArray Odd = data[std::slice(1,size/2,2)]; 
    //repeat the division till array size is 1
    FFT(Even);
    FFT(Odd);
    
    //calculate the complex values 
    // this part is taken from a website and i didnt get it very much

    for (size_t i = 0 ; i < size ; i++)
    {
		// polar is a complex representation (mag.=1,phase=-2*PI*i/size)
		// this for loop collect complex data(after FFT application) 
		// "std::polar(1.0,-2*PI*i/size)" is a constatnt factor that should be multiplied by odd "see the video that you told me to see :)"
        Complex T = std::polar(1.0,-2*PI*i/size)*Odd[i];
        data[i] = Even[i]+T;
        // the sin wave is periodic so F(k) equals F((N/2)-1 +k) and that what he did in the last line of code
		// and the sign of T is changed each time so he adds '-' before T
		data[i+(size/2)] = Even[i]-T;

    }
   
}
