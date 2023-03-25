#!/usr/bin/env python

############################################
# this EMPTY python fifo class was written by dr fred depiero at cal poly
# distribution is unrestricted provided it is without charge and includes attribution

import sys
import json

class my_fifo:
	
	
	############################################
	# constructor for signal history object
	def __init__(self,buff_len):
			
		self.buff_len = buff_len
		self.buff = []
		self.temp = []
		for k in range(buff_len): self.buff.append(0)
		for k in range(buff_len): self.temp.append(0)
		
		# initialize more stuff, as needed	
	
	 
	############################################
	# update history with newest input and advance head / tail
	def update(self,current_in):
		"""
		:current_in: a new input value to add to recent history
		:return: T/F with any error message
		"""

		# students - need to make space for newest sample and include it in history
		
		# students - this is not the correct implementation!
		for x in range(1, self.buff_len):
			self.temp[x] = self.buff[x-1]

		for y in range(self.buff_len):
			self.buff[y] = self.temp[y]
		
		self.buff[0] = current_in

		return True

	

	############################################
	# get value from the recent history, specified by age_indx
	def get(self,age_indx):
		"""
		:indx: an index in the history
			age_indx == 0    ->  most recent historical value
			age_indx == 1    ->  next most recent historical value
			age_indx == M-1  ->  oldest historical value
		:return: value stored in the list of historical values, as requested by indx 
		"""
		
		# students - this is not the correct implementation!
		val = self.buff[age_indx]
		return val


