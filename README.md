# Astable 555 Timer Generated CLK Signal
Ever since I learned about SPI and other communication interfaces in hardware I've been wanting to experiment with CLKs and CLK Signals. In this project I used a 555 timer in astable mode to help me produce a CLK like signal (highs and lows at a set frequency). I hooked up the output pin of the timer IC to my raspberry pi and wrote a mini python script to serve as my oscilloscope (because the real thing is very expensive) 😅.

## The Timer Circuit
  <p align='center'>
  <img src="https://user-images.githubusercontent.com/70349501/175654461-2b511101-4a44-4589-b283-a6cc8903f180.gif"/>
</p>
  
## The Process 

I simply monitored the GPIO input on pin 27 (BMC) to monitor for highs and lows and essentially the on and off states of the output. 

Mathematically you can calculate the frequency of an Astable 555 circuit as such,

$$ f = \frac{1.44}{(R_{1} + 2R_{2})\cdot C} $$

For our case, 

$$ R_{1} = R_{2} = 51K$$

And, 

$$ C = 4.7 \mu F$$

so our $$ f\approx 2.0 Hz $$


## Sample Output Signal

<p align='center'>
  <img src="https://user-images.githubusercontent.com/70349501/175653509-bfb38ea2-1d71-4e9b-873c-24db260425af.gif"/>
</p>

## Script In Action

<p align='center'>
  <a href="https://www.youtube.com/watch?v=2cakMXzuBgw"><img src="https://img.youtube.com/vi/2cakMXzuBgw/0.jpg"/></a>
</p>

