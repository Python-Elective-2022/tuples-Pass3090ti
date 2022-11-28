'''
The function tuples_skip will receive the input tuples 
the function will then skip each element and return back the tuple

Main function
    the tuples will be define as variable x 
    print out the function tuples_skip
'''

def tuples_skip(Tuples):
    '''
    The tuple will be inputted into the function 
    The function will return back the skipped tupples
    '''
    return Tuples[::2]

def main():
    x = ('I', 'am', 'a', 'test', 'tuple')
    print(tuples_skip(x))

if __name__ == "__main__":
    main()

