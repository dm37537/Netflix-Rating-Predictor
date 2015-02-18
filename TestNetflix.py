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


# ----
# main
# ----

if __name__ == "__main__" :
    main()
