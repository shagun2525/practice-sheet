#def is the function key 


def hello_func():
    print('hello function')
hello_func()


def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

student_info('math', 'art', name ='john', age=22)







