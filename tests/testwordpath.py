#! /usr/bin/python
import unittest
import os
import sys
from wordpath.wp_engine import WordPath
from wordpath.wp_engine import WordPathTools
sys.setrecursionlimit(50000)

class TestUtils(unittest.TestCase):

    def test_diff_1_letter(self):
        wt = WordPathTools()
        self.assertTrue(wt.diff_1_letter("aaaa", "aaba"))
        self.assertTrue(wt.diff_1_letter("aaaabbbb", "aaaacbbb"))
        self.assertFalse(wt.diff_1_letter("aaaa", "aaaa"))  #no diff
        self.assertFalse(wt.diff_1_letter("aaaa", "aabb"))  #diff 2
        self.assertFalse(wt.diff_1_letter("aaaa", "aabaa"))  #len + 1

    def test_read_words(self):
        wt = WordPathTools()
        file = open(os.path.dirname(os.path.abspath(__file__))+os.path.sep+"words", 'r')
        c = wt.read_words(file.name, 3)
        self.assertTrue(len(c) == 1294)

    def test_find_children(self):
        wt = WordPathTools()
        children = wt.find_children("aaa", ["aba", "ccc", "ddd", "abb", "aac"])
        self.assertTrue(len(children) == 2)
        self.assertListEqual(children, ["aba", "aac"])

        children = wt.find_children("aaa", ["abb", "ccc", "ddd", "aaa", "fff"])
        self.assertTrue(len(children) == 0)

    def test_build_graph(self):
        wt = WordPathTools()
        d = {'real': ['feal', 'rial'], 'feal': ['real', 'foal'], 'foud': ['foul'], 'foal': ['feal', 'foul'], 'foul': ['foal', 'foud'], 'rial': ['real']}
        g = {}
        wt.build_graph("rial", "foud", g, ["real", "feal", "foal", "foul"])
        self.assertDictEqual(g, d)

    def test_build_graph_file(self):
        wt = WordPathTools()
        file = open(os.path.dirname(os.path.abspath(__file__))+os.path.sep+"words", "r")
        c = wt.read_words(file.name, 4)
        g = {}
        wt.build_graph("rial", "foud", g, c)
        self.assertEquals(len(g.keys()), 4994)

    def test_find_path(self):
        wt = WordPathTools()
        d = {'real': ['feal', 'rial'], 'feal': ['real', 'foal'], 'foud': ['foul'], 'foal': ['feal', 'foul'], 'foul': ['foal', 'foud'], 'rial': ['real']}
        l = wt.find_path(d, "rial", "foud")
        self.assertListEqual(l, ['rial', 'real', 'feal', 'foal', 'foul', 'foud'])

class TestWordPath(unittest.TestCase):

    def test_process_real_file1(self):
        file = open(os.path.dirname(os.path.abspath(__file__))+os.path.sep+"words", 'r')
        wproc = WordPath(file.name, "rial", "foud")
        p = wproc.process()
        self.assertTrue(p[0], "rial")
        self.assertTrue(p[-1], "foud")

    def test_process_real_file2(self):
        file = open(os.path.dirname(os.path.abspath(__file__))+os.path.sep+"words", 'r')
        wproc = WordPath(file.name, "dung", "geez")
        p = wproc.process()
        self.assertTrue(p[0], "dung")
        self.assertTrue(p[-1], "geez")

    def test_process_real_file3(self):
        file = open(os.path.dirname(os.path.abspath(__file__))+os.path.sep+"words", 'r')
        wproc = WordPath(file.name, "jehu", "guha")
        p = wproc.process()
        self.assertTrue(p[0], "jehu")
        self.assertTrue(p[-1], "guha")

    def test_process_real_no_path(self):
        file = open(os.path.dirname(os.path.abspath(__file__))+os.path.sep+"words", 'r')
        wproc = WordPath(file.name, "aaaa", "zzzz")
        p = wproc.process()
        self.assertIsNone(p)

if __name__ == '__main__':
    unittest.main()
