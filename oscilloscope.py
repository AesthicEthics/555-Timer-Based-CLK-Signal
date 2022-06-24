import RPi.GPIO as GPIO
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import time
import datetime as dt
import os

#Hardware Setup
pin = 27
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN)

#Plotting Setup
style.use('fivethirtyeight')
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
xs = []
ys = []

#Animation Run

def animate(i,xs,ys):
	value = GPIO.input(pin)
	xs.append(dt.datetime.now())
	ys.append(value)

	xs = xs[-20:]
	ys = ys[-20:]

	ax1.clear()
	ax1.plot(xs,ys)

	plt.xticks(rotation=45, ha='right')
	plt.subplots_adjust(bottom=0.30)
	plt.title('IC Generated CLK Signal')
	plt.ylabel("State")

#function main loop
try:
	#system Checks
	os.system("rm -rf CLK.mp4")

	print('[+] Parsing CLK Signal')
	anim = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=2000)
	writerMp4 = animation.FFMpegWriter(fps=3)
	anim.save("CLK.mp4",writer=writerMp4)

finally:
	print('[+] Save Successful')
	GPIO.cleanup()
