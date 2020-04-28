#!/usr/bin/python
import numpy as np
import ctypes

def totalPython(arr):
	resposta = 0
	for i in range(len(arr)):
		resposta += arr[i]
	return resposta

def totalNumpy(arr):
	return np.sum(arr)

_totalLib=ctypes.CDLL('./_fib.so')

def totalCtypes(arr, n):
	return _totalLib.total(arr.ctypes.data_as(ctypes.c_void_p), n)
