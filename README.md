# Cross-Correlation-calculation
This repository for my assignment. These code perform two very standard way to calculate the correlation of one image to another bigger image.
## What-is-Cross-correlation?
This is a value tells us how similar two input is. For example in this repository is calculate which part (m x m pixels) is similar with the template (e.g e_letter or o_letter).
## Cross-Correlation-calculation
There is many way to calculate the Cross-correlation value. In my code I have used two techniques are convolution and using FFT (Fast Fourier Transform).
### Convolution
Convolution is a mathematical operation used to combine two function. The intuiton way to think about convolution is take a function's graph then slide it above another function then combine them.
### FFT
Fourier Transform is a way to analyze a complex signal to many of signals that create it.
In Cross Correlation calculation if we use convolution the Time Complexity is O(n^2) but when we apply Fourier Transform (or in this case is Fast Fourier Transform) we can calculate the convolution of two function at only O(nlogn).
# Conclusion
Cross correlation is a small step to create a Convolutional Networks by taking a correlation's matrix then feed it into a neural. In my project now is just for calculating this small step.

I just start to really study about this topic recent and maybe some of my explanition are not correct and my english is horrible then hope you will help me to fix. Thank you for reading.
