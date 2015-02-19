#!/usr/bin/env python3

# -------------------------------
# projects/netflix/TestNetflix.py
# -------------------------------

# -------
# imports
# -------

from io       import StringIO
from unittest import main, TestCase

from Netflix import probe_read, rmse_zip_list_sum, netflix_solve

import warnings

def fxn():
    warnings.warn("deprecated", DeprecationWarning)



# -----------
# TestCollatz
# -----------

class TestNetflix (TestCase) :
   
    # ----------
    # probe_read
    # ----------

    def test_probe_read_1 (self) :
        f = StringIO("2048:\n10101\n3456\n1001\n")
        s = probe_read(f)
        self.assertEqual(type(s), dict)
        self.assertEqual(s['2048'], ['10101', '3456', '1001'])

    def test_probe_read_2 (self) :
        f = StringIO("500:\n10190\n3756\n11256\n")
        s = probe_read(f)
        self.assertEqual(type(s), dict)
        self.assertEqual(s['500'], ['10190', '3756', '11256'])

    def test_probe_read_3 (self) :
        f = StringIO("2049:\n10111\n3451\n101\n")
        s = probe_read(f)
        self.assertEqual(type(s), dict)
        self.assertEqual(s['2049'], ['10111', '3451', '101'])

    def test_probe_read_4 (self) :
        f = StringIO("2045:\n101\n31\n10")
        s = probe_read(f)
        self.assertEqual(type(s), dict)
        self.assertEqual(s['2045'], ['101', '31', '10'])

    # ----
    # rmse
    # ----

    def test_rmse_zip_list_sum_1 (self):
        a = [1, 3, 5]
        b = [3, 5, 3]
        v = rmse_zip_list_sum(a,b)
        self.assertEqual(v, 2.0)

    def test_rmse_zip_list_sum_2 (self):
        a = [1, 4, 5, 4]
        b = [4, 5, 3, 2]
        v = round(rmse_zip_list_sum(a,b), 2)
        self.assertEqual(v, 2.12)

    def test_rmse_zip_list_sum_3 (self):
        a = [1, 3, 5, 5]
        b = [3, 3, 4, 1]
        v = round(rmse_zip_list_sum(a,b), 2)
        self.assertEqual(v, 2.29)

    # -----
    # solve
    # -----

    def test_netflix_solve_1 (self):
        r = StringIO("15581:\n1786736\n15582:\n554807\n1530342\n")
        w = StringIO()
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            fxn()
            netflix_solve(r, w)
        self.assertEqual(w.getvalue(), "15581:\n3.4\n15582:\n3.9\n4.3\nRMSE: 0.74")

    def test_netflix_solve_2 (self):
        r = StringIO("10002:\n1450941\n1213181\n308502\n2581993\n10003:\n1515111\n")
        w = StringIO()
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            fxn()
            netflix_solve(r, w)
        self.assertEqual(w.getvalue(), "10002:\n4.5\n3.7\n4.7\n4.2\n10003:\n2.7\nRMSE: 0.48")

    def test_netflix_solve_null_year (self):
        r = StringIO("4388:\n2493000\n1670719\n1359762")
        w = StringIO()
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            fxn()
            netflix_solve(r, w)
        self.assertEqual(w.getvalue(), "4388:\n3.2\n3.1\n2.7\nRMSE: 0.88")

    def test_netflix_4 (self):
        r = StringIO("10014:\n1626179\n1359761\n430376")
        w = StringIO()
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            fxn()
            netflix_solve(r, w)
        self.assertEqual(w.getvalue(), "10014:\n3.0\n3.9\n2.7\nRMSE: 0.88")


# ----
# main
# ----

if __name__ == "__main__" :
    main()
