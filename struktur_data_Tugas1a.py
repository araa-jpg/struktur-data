"""Tugas Mandiri 1a - Struktur Data
Studi kasus: sistem akademik yang mengelola data mahasiswa.
a. Penyimpanan data berurutan -> Array (list Python)
b. Fitur Undo                 -> Stack (LIFO), list Python
c. Antrean pengolahan data    -> Queue (FIFO), collections.deque
d. Pencarian berdasarkan key  -> Hash Table, dict Python
"""
from collections import deque

# ---------------------------------------------------------------
# a. ARRAY (list) : data tersimpan berurutan, akses indeks O(1)
# ---------------------------------------------------------------
print("=== a. ARRAY (list): penyimpanan data berurutan ===")
array_mhs = ["Andi", "Budi", "Citra", "Dewi", "Eka"]
print("Seluruh data   :", array_mhs)
print("Indeks ke-2    :", array_mhs[2], "-> akses langsung O(1)")
array_mhs.append("Fani")                 # penyisipan di akhir O(1)
print("Setelah append :", array_mhs)

# ---------------------------------------------------------------
# b. STACK : Last In First Out untuk fitur Undo
# ---------------------------------------------------------------
print("\n=== b. STACK: fitur Undo (LIFO) ===")
stack_undo = []                          # struktur data stack
for aktivitas in ["Tambah data Andi", "Ubah data Budi", "Hapus data Citra"]:
    stack_undo.append(aktivitas)         # push O(1)
    print("push :", aktivitas, "->", stack_undo)
print("Undo (pop)    :", stack_undo.pop(), "->", stack_undo)   # pop O(1)
print("Undo (pop)    :", stack_undo.pop(), "->", stack_undo)

# ---------------------------------------------------------------
# c. QUEUE : First In First Out untuk antrean pengolahan data
# ---------------------------------------------------------------
print("\n=== c. QUEUE: antrean pengolahan data (FIFO) ===")
queue_proses = deque()                   # struktur data queue
for tugas in ["Proses KRS Andi", "Proses KRS Budi", "Proses KRS Citra"]:
    queue_proses.append(tugas)           # enqueue O(1)
    print("enqueue :", tugas, "->", list(queue_proses))
print("Dilayani (dequeue):", queue_proses.popleft(), "->", list(queue_proses))  # O(1)
print("Dilayani (dequeue):", queue_proses.popleft(), "->", list(queue_proses))

# ---------------------------------------------------------------
# d. HASH TABLE (dict) : pencarian berdasarkan key (NIM) O(1) rata-rata
# ---------------------------------------------------------------
print("\n=== d. HASH TABLE (dict): pencarian berdasarkan key ===")
hash_mhs = {
    "12550120001": "Andi",
    "12550120002": "Budi",
    "12550120003": "Citra",
}
nim_dicari = "12550120002"
print("Cari NIM", nim_dicari, "->", hash_mhs.get(nim_dicari, "tidak ditemukan"))
print("Cari NIM 12550129999 ->", hash_mhs.get("12550129999", "tidak ditemukan"))
