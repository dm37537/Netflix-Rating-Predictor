import sys

def netflix_read (s) :
    """
    read two ints
    s a string
    return a list of two ints, representing the beginning and end of a range, [i, j]
    """
    if len(s) < 7:
    	a = s.split(':')
    	return [str(a[0]), str(a[1]), ""]
    else:
	    a = s.split(',')
	    return [str(a[0]), str(a[1]), str(a[2])]

def netflix_print (w, i, j, k) :
    """
    print three ints
    w a writer
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    v the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(k) + "\n")



def netflix_solve (r, w) :
    """
    r a reader
    w a writer
    """
    for s in r :
        i, j, k = netflix_read(s)
        netflix_print(w, i, j, k)



if __name__ == "__main__" :
	netflix_solve(sys.stdin, sys.stdout)