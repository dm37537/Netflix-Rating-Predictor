import sys
import json 

from functools import reduce
from math import sqrt
from sys import version
from timeit import timeit
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

    for s in f:
        if s[-2] == ':':
            movie_id = s[0:-2]
            users =[]
            l[movie_id] = users
        else:
            u = l[movie_id] 
            u.append(s[:-1])
            l[movie_id] = u
    return l

def netflix_solve (r, w) :
    """
    r a reader
    w a writer
    """
    usr_avg_cache = json.load(open('/u/mck782/netflix-tests/pma459-usrAvgCache.json', 'r'))
    mov_avg_cache = json.load(open('/u/mck782/netflix-tests/pma459-mvAvgCache.json', 'r'))
    rating_cache = json.load(open('/u/mck782/netflix-tests/pma459-answersCache.json', 'r'))
    cache = json.load(open('/u/mck782/netflix-tests/jab5948-movie-stats.json', 'r'))
    cache_users = json.load(open('/u/mck782/netflix-tests/jab5948-user-stats.json', 'r'))
    #probe_dict = probe_read(open('./probe.txt', 'r'))
    probe_dict = probe_read(r)
    movie_date_cache = json.load(open('/u/mck782/netflix-tests/af22574-movieDates.json', 'r'))
    user_decade_cache = json.load(open('/u/mck782/netflix-tests/cdm2697-userRatingsAveragedOver10yInterval.json', 'r'))
    Stats = namedtuple('Stats', 'mean, stdev, min_rating, q1, median, q3, max_rating, skew, size')

    #print(len(cache))
    #print(usr_avg_cache['7'])
    #print(mov_avg_cache[2])
    #print(probe_dict['10001'])

    total = 0
    count = 0

    for k in mov_avg_cache:
        if k > 0 :
            total += k  
            count += 1
    overall_mov_avg = total / count

    total = 0
    count = 0

    for k in usr_avg_cache:
        total += usr_avg_cache[k]
        count += 1

    overall_usr_avg = total/count

    predict_ratings = []
    actual_ratings = []
    for k,v in probe_dict.items():
        #w.write(k + ":" + "\n")
        mov_year = movie_date_cache[k]
        mov_year = list(mov_year)
        mov_year[-1] = '0'
        mov_avg = cache[int(k)][0]
        movie_stats = Stats(*cache[int(k)])
        l = []
        for u in v:
            usr_decade_avg = user_decade_cache[u]
            mov_d_avg = 0
            for y, a, n in usr_decade_avg:
                y = list(y)
                y = y[0:4]
                if mov_year == list(y) :
                    mov_d_avg = float(a)
            usr_avg = cache_users[u][0]
            user_stats = Stats(*cache_users[u])

            # get trend by compare current average with overall average
            mov_trend = (mov_avg - overall_mov_avg)
            usr_trend = (usr_avg - overall_usr_avg)

            actual_mov_avg = mov_avg + mov_trend
            actual_usr_avg = usr_avg + usr_trend    
            
            if mov_trend > 0:
                actual_mov_avg += 0.06
            else:
                actual_mov_avg -= 1.4

            if usr_trend > 0:
                actual_usr_avg += 0.02
            else:
                actual_usr_avg -= 0.7

            
            if (mov_d_avg == 0):
                p_v = round(((user_stats.median + movie_stats.median + mov_avg + usr_avg + actual_mov_avg + actual_usr_avg)/6), 10)
            else:
                #modify according to decade rating value
                if mov_avg - mov_d_avg < 0 :
                    mov_d_avg += 0.26
                else:
                    mov_d_avg -= 0.26
                p_v = round(((user_stats.median + movie_stats.median + mov_avg + usr_avg + mov_d_avg + actual_mov_avg + actual_usr_avg)/7), 10)
            l.append(p_v)
            l.append(u)
            predict_ratings.append(p_v)
            actual_ratings.append(rating_cache[k][u])
            #w.write(str(p_v) + "\n")   
 
    assert(len(predict_ratings) == len(actual_ratings))
    print (str(rmse_zip_list_sum(predict_ratings, actual_ratings)))



