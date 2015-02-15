import sys
import json 

from functools import reduce
from math import sqrt
import math
from collections import namedtuple

def rmse_zip_list_sum (a, p) :
    """
    O(n) in space
    O(n) in time
    """
    assert(hasattr(a, "__len__"))
    assert(hasattr(p, "__len__"))
    assert(hasattr(a, "__iter__"))
    assert(hasattr(p, "__iter__"))
    z = zip(a, p)
    v = sum([(x - y) ** 2 for x, y in z])
    return sqrt(v / len(a))


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
    rating_cache = json.load(open('/u/dameng/CS373-test/netflix-tests/pma459-answersCache.json', 'r'))
    probe_dict = probe_read(open('/u/dameng/CS373/probe.txt', 'r'))
    Stats = namedtuple('Stats', 'mean, stdev, min_rating, q1, median, q3, max_rating, skew, size')
    cache = json.load(open('/u/dameng/CS373-test/netflix-tests/jab5948-movie-stats.json', 'r'))
    

    #print(usr_avg_cache['7'])
    #print(mov_avg_cache[2])
    #print(probe_dict['10001'])

    predict = {}
    predict_ratings = []
    actual_ratings = []

    for k,v in probe_dict.items():
        movie_stats = Stats(*cache[int(k)])
        mov_avg = movie_stats.mean
        mov_med = movie_stats.median
        mov_q3 = movie_stats.q3
        mov_q1 = movie_stats.q1
        #mov_avg = mov_avg_cache[int(k)]
        l = []
        for u in v:
            usr_avg = usr_avg_cache[u]
            p_dv = (mov_avg + usr_avg) // 2
            if abs(p_dv - usr_avg) > 0.5 :
                p_v = p_dv + 1
            else :
                p_v = p_dv        
            l.append(p_v)
            l.append(u)
            predict_ratings.append(p_v)
            actual_ratings.append(rating_cache[k][u])
            predict[k] = l


    print (len(predict_ratings))
    print (len(actual_ratings))
    print (rmse_zip_list_sum(predict_ratings, actual_ratings))
    print (predict['1'])

    """
    for s in r :
        i, j, k = netflix_read(s)
        netflix_print(w, i, j, k)
    """


if __name__ == "__main__" :
	netflix_solve(sys.stdin, sys.stdout)
