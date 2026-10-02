"""Tugas Mandiri 1b - Struktur Data
Antrean layanan mahasiswa  -> Queue (FIFO) memakai collections.deque
Fitur Undo                 -> Stack (LIFO) memakai list Python
"""
from collections import deque


class AntreanMahasiswa:
    """Queue (FIFO): yang datang lebih dulu dilayani lebih dulu."""

    def __init__(self):
        self._data = deque()

    def enqueue(self, nama):          # penambahan data  -> O(1)
        self._data.append(nama)

    def dequeue(self):                # penghapusan data -> O(1)
        if self.is_empty():
            raise IndexError("Antrean kosong")
        return self._data.popleft()

    def front(self):                  # melihat data terdepan -> O(1)
        if self.is_empty():
            raise IndexError("Antrean kosong")
        return self._data[0]

    def is_empty(self):               # memeriksa kondisi kosong -> O(1)
        return len(self._data) == 0

    def __str__(self):
        return "Depan -> " + (" | ".join(self._data) if self._data else "(kosong)") + " <- Belakang"


class UndoStack:
    """Stack (LIFO): aktivitas terakhir dibatalkan lebih dulu."""

    def __init__(self):
        self._data = []

    def push(self, aktivitas):        # penambahan data -> O(1)
        self._data.append(aktivitas)

    def pop(self):                    # penghapusan data (undo) -> O(1)
        if self.is_empty():
            raise IndexError("Stack Undo kosong")
        return self._data.pop()

    def peek(self):                   # melihat data teratas -> O(1)
        if self.is_empty():
            raise IndexError("Stack Undo kosong")
        return self._data[-1]

    def is_empty(self):               # memeriksa kondisi kosong -> O(1)
        return len(self._data) == 0

    def __str__(self):
        return "Bawah -> " + (" | ".join(self._data) if self._data else "(kosong)") + " <- Atas (Top)"


if __name__ == "__main__":
    print("=== SIMULASI ANTREAN ===")
    q = AntreanMahasiswa()
    for nama in ["Andi", "Budi", "Citra", "Dewi", "Eka"]:
        q.enqueue(nama)
        print(f"enqueue({nama})  :", q)
    print("front()         :", q.front())
    print("dequeue()       :", q.dequeue(), "->", q)
    print("dequeue()       :", q.dequeue(), "->", q)
    print("is_empty()      :", q.is_empty())
    print("Hasil akhir     :", q)

    print("\n=== SIMULASI UNDO ===")
    u = UndoStack()
    for akt in ["Tambah antrean Andi", "Tambah antrean Budi", "Layani Andi",
                "Tambah antrean Citra", "Layani Budi"]:
        u.push(akt)
        print(f"push({akt})  :", u)
    print("peek()          :", u.peek())
    print("pop() / undo    :", u.pop(), "->", u)
    print("pop() / undo    :", u.pop(), "->", u)
    print("is_empty()      :", u.is_empty())
    print("Hasil akhir     :", u)
