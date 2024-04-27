# print(object(s), sep=separator, end=end, file=file, flush=flush)

# 1- object(s) Any object, and as many as you like. Will be converted to string before printed

# 2- sep='separator' Optional. Specify how to separate the objects, if there is more than one. Default is ' '

# 3- end='end' Optional. Specify what to print at the end. Default is '\n' (line feed)

# 4- file	Optional. An object with a write method. Default is sys.stdout

# 5- flush	Optional. A Boolean, specifying if the output is flushed (True) or buffered (False). Default is False

# print("Hello", "World", sep="&")
print("Hello", "World", end=" ")
print("Hello", "World")
print("Hello", "World")