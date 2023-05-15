import os
import unittest

from sync_list import SyncList


class TestSyncList(unittest.TestCase):
    def setUp(self):
        self.filename = 'test_sync_list.json'

    def tearDown(self):
        os.remove(self.filename)

    def test_init(self):
        lst = SyncList([1, 2, 3], self.filename)
        self.assertEqual(len(lst), 3)

    def test_append(self):
        lst = SyncList(filename=self.filename)
        lst.append(1)
        lst.append(2)
        self.assertEqual(len(lst), 2)
        self.assertEqual(lst[0], 1)
        self.assertEqual(lst[1], 2)

    def test_extend(self):
        lst = SyncList(filename=self.filename)
        lst.extend([1, 2, 3])
        self.assertEqual(len(lst), 3)
        self.assertEqual(lst[0], 1)
        self.assertEqual(lst[1], 2)
        self.assertEqual(lst[2], 3)

    def test_insert(self):
        lst = SyncList([1, 3], self.filename)
        lst.insert(1, 2)
        self.assertEqual(len(lst), 3)
        self.assertEqual(lst[0], 1)
        self.assertEqual(lst[1], 2)
        self.assertEqual(lst[2], 3)

    def test_remove(self):
        lst = SyncList([1, 2, 3], self.filename)
        lst.remove(2)
        self.assertEqual(len(lst), 2)
        self.assertEqual(lst[0], 1)
        self.assertEqual(lst[1], 3)

    def test_pop(self):
        lst = SyncList([1, 2, 3], self.filename)
        item = lst.pop()
        self.assertEqual(len(lst), 2)
        self.assertEqual(item, 3)

    def test_clear(self):
        lst = SyncList([1, 2, 3], self.filename)
        lst.clear()
        self.assertEqual(len(lst), 0)

    def test_index(self):
        lst = SyncList([1, 2, 3], self.filename)
        index = lst.index(2)
        self.assertEqual(index, 1)

    def test_count(self):
        lst = SyncList([1, 2, 2, 3], self.filename)
        count = lst.count(2)
        self.assertEqual(count, 2)

    def test_sort(self):
        lst = SyncList([3, 2, 1], self.filename)
        lst.sort()
        self.assertEqual(len(lst), 3)
        self.assertEqual(lst[0], 1)
        self.assertEqual(lst[1], 2)
        self.assertEqual(lst[2], 3)

    def test_reverse(self):
        lst = SyncList([1, 2, 3], self.filename)
        lst.reverse()
        self.assertEqual(len(lst), 3)
        self.assertEqual(lst[0], 3)
        self.assertEqual(lst[1], 2)
        self.assertEqual(lst[2], 1)
