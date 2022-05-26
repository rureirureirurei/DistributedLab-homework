## Large numbers
1. It's obvious that the number of unique n-byte keys is $2^n$ as for each byte we have only two options: 1, 0. For calculating 2 raised to the power of n we will use the "Binary Exponentiation" algorithm which allows us to compute the answer in O(log n). 

2. For choosing a random key we will use python's built-in random package. Even though it is a pseudorandom generation, that will satisfy us for now.

3. The implemented solution gives us the following results: 

      $ $ $ $ $ $ $ \\approx $ 0.000031 s. for 8 bytes   
      $ $ $ $ $ $ $ \\approx $ 0.000663 s. for 16 bytes  
      $ $ $ $ $ $ $ \\approx $ 682 s. for 32 bytes  
   
   For the bigger numbers waiting time is ... pretty large. Let's estimate it. We can get the results for some smaller size values, fit them into some exponential model and then extrapolate it.  
   Here you can see our initial data (green points) and approximation curve.
   
   ![Alt text](https://github.com/rureirureirurei/DistributedLab-homework/blob/main/hw1/graph.png?raw=true)
   
   It turns out, that $t = 0.0000003⋅1.97^{size - 0.45}$ fits our dataset pretty well. Even though further research can be done and the quality can be improved, we can dare to roughly estimate the time needed for brute-forcing keys with the larger sizes. 
   
      $ $ $ $ $ $ $ \\approx $ 49163 years for 64 bytes   
      $ $ $ $ $ $ $ \\approx $ $10^{61}$ years for 256 bytes  
      $ $ $ $ $ $ $ \\approx $ $10^{1200}$ years for 4096 bytes  

   Now it's clear, that brute-forcing is practically unacceptable for such problem.
