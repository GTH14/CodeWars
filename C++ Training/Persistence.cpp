#include <string>
#include <iostream>
#include <cmath>

unsigned long decimal2binary(unsigned long ip){
  unsigned long counter = 0;
  unsigned long res = ip/2, bin_res = ip%2*pow(10, counter);
  while(res>0){
    counter += 1;
    bin_res += res%2*pow(10, counter);
    res = floor(res/2);
  }
  return bin_res;
}

int main(){
    unsigned long x=2149583361;
    unsigned long res = decimal2binary(x);
    std::cout << res;
}
