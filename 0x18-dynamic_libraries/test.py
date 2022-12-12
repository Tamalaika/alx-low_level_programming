import ctypes
NUM = 16
fun = ctypes.CDLL("./100-operations.so")
fun.myFunction.argtypes = [ctypes.c_int]
returnVale = fun.myFunction(NUM)
