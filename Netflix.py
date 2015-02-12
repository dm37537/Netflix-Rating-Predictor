import sys
import json 

def netflix_read (s) :
    """
    """

    if len(s) < 7:
    	a = s.split(':')
    	return [str(a[0]), str(a[1]), ""]
    else:
	    a = s.split(',')
	    return [str(a[0]), str(a[1]), str(a[2])]

def probe_read(f):
    
    l = {}
    movie_id = ''
    #users = []

    for s in f:
        #print (s[-2])
        if s[-2] == ':':
            movie_id = s[0:-2]
            users =[]
            l[movie_id] = users
        else:
            u = l[movie_id] 
            u.append(s[:-1])
            l[movie_id] = u
    return l

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
    usr_avg_cache = json.load(open('/u/dameng/CS373-test/netflix-tests/pma459-usrAvgCache.json', 'r'))
    mov_avg_cache = json.load(open('/u/dameng/CS373-test/netflix-tests/pma459-mvAvgCache.json', 'r'))
    probe_dict = probe_read(open('/u/dameng/CS373/probe.txt', 'r'))
    print(usr_avg_cache['7'])
    print(mov_avg_cache[2])
    print(probe_dict['10001'])
    
    """
    for s in r :
        i, j, k = netflix_read(s)
        netflix_print(w, i, j, k)
    """


if __name__ == "__main__" :
	netflix_solve(sys.stdin, sys.stdout)