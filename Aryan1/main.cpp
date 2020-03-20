#include <iostream>
using namespace std;

int isPrimeNumber(int);

int main()
{
   bool isPrime;
   int count;
   cout<<"Enter the value of i:";
   cin>>count;
   for(int i = 2; i < count; i++)
   {
       // isPrime will be true for prime numbers
       isPrime = isPrimeNumber(i);

       if(isPrime == true)
          cout<<i<<" ";
   }
   return 0;
}

// Function that checks whether n is prime or not
int isPrimeNumber(int i) {
   bool isPrime = true;

   for(int n = 2; n <= i/2; n++) {
      if (i%n == 0)
      {
         isPrime = false;
         break;
      }
   }
   return isPrime;
}
