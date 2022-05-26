## Large numbers
1. It's pretty obvious that the number of unique n-byte keys is basically $2^n$ - for each byte we have two options - 1, 0. For calculating 2 raised to the power of n we will use the "Binary Exponentiation" algorythm which allows us to compute the answer in O(log n). 

2. For choosing a random key we will use python's built-in random package. Even though it is actually a pseudorandom generation, that will satisfy us for now.

3. The implemented solution gives us a following results: 

      $ $ $ $ $ $ $ \approx $ 0.000031 s. for 8 bytes   
      $ $ $ $ $ $ $ \approx $ 0.000663 s. for 16 bytes  
      $ $ $ $ $ $ $ \approx $ 682 s. for 32 bytes  
   
   For the bigger numbers waiting time is ... pretty large. Let's estimate it. We can easily get the results for some smaller key size values, fit them into some exponential model and then extrapolate it.
   
   ![Alt text](hw1/graph.jpg?raw=true "Given data and approximation function")
   
   It turns out, that $t = 0.0000003⋅1.97^{size - 0.45}$ fits our dataset pretty well. Even though further research can be done and the quality can be improved, we can dare to roughly estimate time needed for bruteforcing keys with the larger sizes. 
   
      $ $ $ $ $ $ $ \approx $ 49163 years for 64 bytes   
      $ $ $ $ $ $ $ \approx $ $10^{61}$ years for 256 bytes  
      $ $ $ $ $ $ $ \approx $ $10^{1200}$ years for 4096 bytes  

   Now it's obvious, that bruteforcing is practically unacceptable for such keys.
