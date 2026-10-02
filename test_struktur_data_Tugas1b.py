import unittest
from struktur_data_Tugas1b import AntreanMahasiswa, UndoStack


class TestAntrean(unittest.TestCase):
    def setUp(self):
        self.q = AntreanMahasiswa()

    def test_enqueue(self):
        for n in ["Andi", "Budi", "Citra"]:
            self.q.enqueue(n)
        self.assertEqual(self.q.front(), "Andi")
        self.assertFalse(self.q.is_empty())

    def test_dequeue_fifo(self):
        self.q.enqueue("Andi"); self.q.enqueue("Budi")
        self.assertEqual(self.q.dequeue(), "Andi")
        self.assertEqual(self.q.dequeue(), "Budi")
        self.assertTrue(self.q.is_empty())

    def test_dequeue_kosong(self):
        with self.assertRaises(IndexError):
            self.q.dequeue()

    def test_front(self):
        self.q.enqueue("Dewi"); self.q.enqueue("Eka")
        self.assertEqual(self.q.front(), "Dewi")
        self.assertEqual(self.q.front(), "Dewi")  # tidak menghapus

    def test_front_kosong(self):
        with self.assertRaises(IndexError):
            self.q.front()

    def test_is_empty(self):
        self.assertTrue(self.q.is_empty())
        self.q.enqueue("Andi")
        self.assertFalse(self.q.is_empty())


class TestUndo(unittest.TestCase):
    def setUp(self):
        self.s = UndoStack()

    def test_push(self):
        self.s.push("A1"); self.s.push("A2")
        self.assertEqual(self.s.peek(), "A2")

    def test_pop_lifo(self):
        self.s.push("A1"); self.s.push("A2"); self.s.push("A3")
        self.assertEqual(self.s.pop(), "A3")
        self.assertEqual(self.s.pop(), "A2")
        self.assertEqual(self.s.peek(), "A1")

    def test_pop_kosong(self):
        with self.assertRaises(IndexError):
            self.s.pop()

    def test_peek(self):
        self.s.push("A1")
        self.assertEqual(self.s.peek(), "A1")
        self.assertEqual(self.s.peek(), "A1")  # tidak menghapus

    def test_peek_kosong(self):
        with self.assertRaises(IndexError):
            self.s.peek()

    def test_is_empty(self):
        self.assertTrue(self.s.is_empty())
        self.s.push("A1")
        self.assertFalse(self.s.is_empty())


if __name__ == "__main__":
    unittest.main(verbosity=2)
