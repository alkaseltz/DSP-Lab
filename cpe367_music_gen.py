#!/usr/bin/python

import sys
import time

import base64
import random as random

import datetime
import time
import math

from cpe367_wav import cpe367_wav



############################################
############################################
# define function to add one note to list
# students - modify this function as needed!

def add_note(xlist,amp,w0,nstart,nlen,sigma):

	# this initial version of the function only includes a tone burst
	#  no harmonics and no decaying envelope are included
	for n in range(nstart,nstart+nlen):
			xlist[n] += amp * math.exp((nstart-n)/sigma)*math.sin(w0 * n)
	# note summed into signal
	return
	
		


############################################
############################################
# define routine for generating signal in WAV format
def gen_wav(fpath_wav_out):
	"""
	: this example generates a WAV file
	: output is accomplished via WAV files
	: return: True or False 
	"""
	
	# construct object for writing WAV file
	#  assign object a name, to facilitate status and error reporting
	wav_out = cpe367_wav('wav_out',fpath_wav_out)
		
	# setup configuration for output WAV
	num_channels = 1
	sample_width_8_16_bits = 16
	sample_rate_hz = 16000
	wav_out.set_wav_out_configuration(num_channels,sample_width_8_16_bits,sample_rate_hz)
		
	# open WAV output file
	ostat = wav_out.open_wav_out()
	if ostat == False:
		print('Cant open wav file for writing')
		return False
	
	
	
	###############################################################
	###############################################################
	# students - modify this section here

	# these parameters will need updating!
	#  you may also wish to add more parameters
	total_num_samples = 41040
	
	# allocate list of zeros to store an empty signal
	xlist = [0] * total_num_samples

	# setup one note
	#  this implementation does not include harmonics or a decay
	w1 = 2 * math.pi * 98 / sample_rate_hz
	w2 = 2 * math.pi * 392 / sample_rate_hz
	w3 = 2 * math.pi * 440 / sample_rate_hz
	w4 = 2 * math.pi * 493.9 / sample_rate_hz
	w5 = 2 * math.pi * 196 / sample_rate_hz
	w6 = 2 * math.pi * 587.3 / sample_rate_hz
	w7 = 2 * math.pi * 523.3 / sample_rate_hz
	w8 = 2 * math.pi * 523.3 / sample_rate_hz
	w9 = 2 * math.pi * 164.6 / sample_rate_hz
	w10 = 2 * math.pi * 659.2 / sample_rate_hz
	w11 = 2 * math.pi * 587.3 / sample_rate_hz

	frequency  =  [98,392,440,493.9,196,587.3,523.3,523.3,164.6,659.2,587.3]
	frequency3 = [i*3 for i in frequency]
	frequency5 = [i*5 for i in frequency]
	frequency7 = [i*7 for i in frequency]
	
	start = [0,4560,9120,13680,13680,18240,22800,27360,27360,31920,36480]
	for x in frequency3:
		amp = 3500
		sigma1 = 912
		sigma2 = 2736
		n_durr = 13680
		n_durr2 = 4560
		if(frequency3.index(x) == 0 or frequency3.index(x) == 4 or frequency3.index(x) == 8):
			add_note(xlist,amp/(frequency3.index(x)+1),x,start[(frequency3.index(x))],n_durr,sigma2)
		else: add_note(xlist,amp/(frequency3.index(x)+1),x,start[(frequency3.index(x))],n_durr2,sigma1)

	for x in frequency5:
		amp = 3500
		sigma1 = 912
		sigma2 = 2736
		n_durr = 13680
		n_durr2 = 4560
		if(frequency5.index(x) == 0 or frequency5.index(x) == 4 or frequency5.index(x) == 8):
			add_note(xlist,amp/(frequency5.index(x)+1),x,start[(frequency5.index(x))],n_durr,sigma2)
		else: add_note(xlist,amp/(frequency5.index(x)+1),x,start[(frequency5.index(x))],n_durr2,sigma1)

	for x in frequency7:
		amp = 3500
		sigma1 = 912
		sigma2 = 2736
		n_durr = 13680
		n_durr2 = 4560
		if(frequency7.index(x) == 0 or frequency7.index(x) == 4 or frequency7.index(x) == 8):
			add_note(xlist,amp/(frequency7.index(x)+1),x,start[(frequency7.index(x))],n_durr,sigma2)
		else: add_note(xlist,amp/(frequency7.index(x)+1),x,start[(frequency7.index(x))],n_durr2,sigma1)

	amp = 10500
	sigma1 = 912
	sigma2 = 2736
	
	n_start = 0
	n_durr = 13680
	n_start2 = 4560
	n_durr2 = 4560
	n_start3 = 9120
	n_durr3 = 4560
	n_start4 = 13680
	n_durr4 = 4560
	n_start5 = 13680
	n_durr5 = 13680
	n_start6 = 18240
	n_durr6 = 4560
	n_start7 = 22800
	n_durr7 = 4560
	n_start8 = 27360
	n_durr8 = 4560
	n_start9 = 27360
	n_durr9 = 13680
	n_start10 = 31920
	n_durr10 = 4560
	n_start11 = 36480
	n_durr11 = 4560
	
	add_note(xlist,amp,w1,n_start,n_durr,sigma2)
	add_note(xlist,amp,w2,n_start2,n_durr2,sigma1)
	add_note(xlist,amp,w3,n_start3,n_durr3,sigma1)
	add_note(xlist,amp,w4,n_start4,n_durr4,sigma1)
	add_note(xlist,amp,w5,n_start5,n_durr5,sigma2)
	add_note(xlist,amp,w6,n_start6,n_durr6,sigma1)
	add_note(xlist,amp,w7,n_start7,n_durr7,sigma1)
	add_note(xlist,amp,w8,n_start8,n_durr8,sigma1)
	add_note(xlist,amp,w8,n_start8,n_durr8,sigma1)
	add_note(xlist,amp,w9,n_start9,n_durr9,sigma2)
	add_note(xlist,amp,w10,n_start10,n_durr10,sigma1)
	add_note(xlist,amp,w11,n_start11,n_durr11,sigma1)

	
	
	# students - well done!
	###############################################################
	###############################################################



	# write samples to output file one at a time
	for n in range(total_num_samples):
	
		# convert to signed int
		yout = int(round(xlist[n]))
		
		# output current sample 
		ostat = wav_out.write_wav(yout)
		if ostat == False: break
	
	# close input and output files
	#  important to close output file - header is updated (with proper file size)
	wav_out.close_wav()
		
	return True





############################################
############################################
# define main program
def main():

	# check python version!
	major_version = int(sys.version[0])
	if major_version < 3:
		print('Sorry! must be run using python3.')
		print('Current version: ')
		print(sys.version)
		return False
		
	# grab file names
	# fpath_wav_out = sys.argv[1]
	fpath_wav_out = 'music_synth.wav'

	# let's do it!
	return gen_wav(fpath_wav_out)
	
			
	
	
############################################
############################################
# call main function
if __name__ == '__main__':
	
	main()
	quit()
