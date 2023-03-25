#!/usr/bin/python

import sys
import time

import base64
import random as random

import datetime
import time
import math

import matplotlib.pyplot as plt
import numpy as np
import queue

#from cpe367_wav import cpe367_wav
from cpe367_sig_analyzer import cpe367_sig_analyzer
from scipy.fft import fft
from collections import deque





############################################
############################################
# define routine for detecting DTMF tones
def process_wav(fpath_sig_in):
	
		
	###############################
	# define list of signals to be displayed by and analyzer
	#  note that the signal analyzer already includes: 'symbol_val','symbol_det','error'
	more_sig_list = ['sig_1','sig_2']
	
	# sample rate is 4kHz
	fs = 4000
	
	# instantiate signal analyzer and load data
	s2 = cpe367_sig_analyzer(more_sig_list,fs)
	s2.load(fpath_sig_in)
	s2.print_desc()
	
	########################
	# students: setup filters
	def bandpass_filter(signal, f, r):
		C = 1024
		F = f/fs
		a1 = -(2 * r * np.cos(2 * np.pi * F))
		a2 = (r ** 2)
		b0 = 1 - r
		a1c = round(a1*C)
		a2c = round(a2*C)
		b0c = round(b0*C)
		print(b0c, a1c, a2c)
		# Initialize filter state variables
		x1 = 0
		x2 = 0
		y1 = 0
		y2 = 0
		
		# Apply the filter to the input signal
		filtered_signal = []
		for x in signal:
			y = (b0c * x + a1c * x1 + a2c * x2 - a1c * y1 - a2c * y2)/C
			filtered_signal.append(y)
			x2 = x1
			x1 = x
			y2 = y1
			y1 = y
		
		return filtered_signal
	
	def dft(samples, sample_rate):
		N = len(samples)
		freqs = np.arange(N) * (sample_rate / N)
		magnitudes = np.zeros(N)

		for k in range(N):
			for n in range(N):
				magnitudes[k] += samples[n] * np.exp(-2j * np.pi * k * n / (2*N))

		magnitudes = np.abs(magnitudes)

		return magnitudes, freqs
	
	def get_max_index(tup, samples):
		numsum = 0
		densum = 0
		T = max(tup[0])
		# print(T)
		for x in range(samples):
			if(tup[0][x]>(T/2)):
				numsum += tup[0][x]*tup[1][x]
				densum += tup[0][x]
		
		return max(tup[0])

	# process input	
	xin = 0
	num = 33   
	xinList = []
	fifo = deque([0] * num)
	symbol_val_det = 0
	for n_curr in range(s2.get_len()):
	
		# read next input sample from the signal analyzer
		xin = s2.get('xin',n_curr)
		
		vertFreq = [697, 770, 852, 941]
		horizFreq = [1209, 1336, 1477, 1633]

		
		xinList.append(xin)
		fifo.append(xin)
		fifo.popleft()

		f1 = bandpass_filter(fifo, vertFreq[0], 0.999)
		f2 = bandpass_filter(fifo, vertFreq[1], 0.999)
		f3 = bandpass_filter(fifo, vertFreq[2], 0.999)
		f4 = bandpass_filter(fifo, vertFreq[3], 0.999)

		f5 = bandpass_filter(fifo, horizFreq[0], 0.999)
		f6 = bandpass_filter(fifo, horizFreq[1], 0.999)
		f7 = bandpass_filter(fifo, horizFreq[2], 0.999)
		f8 = bandpass_filter(fifo, horizFreq[3], 0.999)
		
		########################
		# students: evaluate each filter and implement other processing blocks
		# dft1 = dft(f1,fs)
		# maxval1 = round(get_max_index(dft1, num))
		# print(maxval1)
		# dft2 = dft(f2,fs)
		# maxval2 = round(get_max_index(dft2, num))
		# dft3 = dft(f3,fs)
		# maxval3 = round(get_max_index(dft3, num))
		# dft4 = dft(f4,fs)
		# maxval4 = round(get_max_index(dft4, num))
		# dft5 = dft(f5,fs)
		# maxval5 = round(get_max_index(dft5, num))
		# dft6 = dft(f6,fs)
		# maxval6 = round(get_max_index(dft6, num))
		# dft7 = dft(f7,fs)
		# maxval7 = round(get_max_index(dft7, num))
		# dft8 = dft(f8,fs)
		# maxval8 = round(get_max_index(dft8, num))
		
		
		f1max = max(f1)
		f2max = max(f2)
		f3max = max(f3)
		f4max = max(f4)

		f5max = max(f5)
		f6max = max(f6)
		f7max = max(f7)
		f8max = max(f8)
		
		Rows = {}
		Col = {}
		Rows[697] = f1max
		Rows[770] = f2max
		Rows[852] = f3max
		Rows[941] = f4max

		Col[1209] = f5max
		Col[1336] = f6max
		Col[1477] = f7max
		Col[1633] = f8max

		rowmax = max(Rows.values())
		colmax = max(Col.values())
		rowkey = 0
		for k in Rows:
			if Rows[k] == rowmax:
				rowkey = k

		colkey = 0
		for k in Col:
			if Col[k] == colmax:
				colkey = k

		if rowkey == 697:
			if colkey == 1209:
				symbol_val_det = 1
			if colkey == 1336:
				symbol_val_det = 2
		if rowkey == 770:
			if colkey == 1209:
				symbol_val_det = 4
			if colkey == 1336:
				symbol_val_det = 5
		

		# save intermediate signals as needed, for plotting
		#  add signals, as desired!
		s2.set('sig_1',n_curr,xin)
		for x in range(num):
			s2.set('sig_2',n_curr,f1[x])

		# save detected symbol
		s2.set('symbol_det',n_curr,symbol_val_det)

		# get correct symbol (provided within the signal analyzer)
		symbol_val = s2.get('symbol_val',n_curr)

		# compare detected signal to correct signal
		symbol_val_err = 0
		if symbol_val != symbol_val_det: symbol_val_err = 1
		
		# save error signal
		s2.set('error',n_curr,symbol_val_err)

	# display mean of error signal
	err_mean = s2.get_mean('error')
	print('mean error = '+str( round(100 * err_mean,1) )+'%')
		
	# define which signals should be plotted
	plot_sig_list = ['sig_1','sig_2','symbol_val','symbol_det','error']
	
	# plot results
	s2.plot(plot_sig_list)
	
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
		
	# assign file name
	# fpath_sig_in = 'dtmf_signals_slow.txt'
	fpath_sig_in = 'dtmf_signals_fast.txt'
	
	
	# let's do it!
	return process_wav(fpath_sig_in)


	
	
############################################
############################################
# call main function
if __name__ == '__main__':
	
	main()
	quit()
