from datetime import datetime
import os


def writer(func):
    def info(*args, **kwargs):
        with open ('file.txt', 'w', encoding= 'utf-8' ) as file:
            t = str(datetime.now())
            result = func(*args, **kwargs)
            name = func.__name__
            string = f'{t}, {name}, {args}, {result}, {os.path.abspath("file.txt")}'
            file.write(string)
        return result
    return info    


@writer
def flat_generator(nested_list): 
    for a in sum(nested_list,[]):
        yield a

nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f'],
	['g', 'h', 'i'],
]
for item in  flat_generator(nested_list):
	print(item)


