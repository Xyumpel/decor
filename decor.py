from datetime import datetime
import os

path = 'C:\\VSCode\\Netology\\Decoration'
def parametrized_decor(parameter):
    def decor(foo):
        def new_foo(*args, **kwars):
            with open(os.path.join(parameter, 'data.txt'), "w") as file:
                t = str(datetime.now())
                result = foo(*args, **kwars)
                name = foo.__name__
                string = f'{t}, {name}, {args}, {result}, {parameter}'
                file.write(string)
                result = foo(*args, **kwars)
                return result 
        return new_foo
    return decor
 
@parametrized_decor(parameter=path)
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
