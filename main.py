import time
import os

# Grid sudoku yang menjadi input
grid = [
  [0, 0, 0,   0, 0, 0,   0, 0, 0],
  [0, 0, 0,   0, 0, 0,   0, 0, 0],
  [0, 0, 0,   0, 0, 0,   0, 0, 0],

  [0, 0, 0,   0, 0, 0,   0, 0, 0],
  [0, 0, 0,   0, 9, 0,   0, 0, 0],
  [0, 0, 0,   0, 0, 0,   0, 0, 0],

  [0, 0, 0,   0, 0, 0,   0, 0, 0],
  [0, 0, 0,   0, 0, 0,   0, 0, 0],
  [0, 0, 0,   0, 0, 0,   0, 0, 0]
  ]

# grid = [
#  [2, 1, 9,   0, 4, 6,   0, 3, 0],
#  [0, 0, 5,   1, 0, 0,   0, 0, 0],
#  [0, 3, 4,   0, 0, 0,   2, 6, 0],

#  [0, 2, 6,   0, 0, 7,   5, 0, 3],
#  [0, 0, 0,   0, 9, 0,   0, 0, 7],
#  [4, 7, 3,   0, 6, 5,   0, 0, 8],

#  [0, 6, 0,   4, 0, 2,   3, 1, 0],
#  [3, 4, 0,   0, 0, 0,   7, 8, 0],
#  [1, 0, 0,   0, 0, 0,   4, 5, 0]
#  ]

# Fungsi untuk print grid
# i = baris
# j = kolom

def print_grid(sudoku):
  for i in range(0,3):
   
    for j in range(0,3):
      print(sudoku[i][j], end=" ")
      time.sleep(0.002)
    print("|", end=" ")

    for j in range(3, 6):
      print(sudoku[i][j], end=" ")
      time.sleep(0.002)
    print("|", end=" ")

    for j in range(6, 9):
      print(sudoku[i][j], end=" ")
      time.sleep(0.002)
    print(" ")

  print("---------------------")

  for i in range(3,6):
   
    for j in range(0,3):
      print(sudoku[i][j], end=" ")
      time.sleep(0.002)
    print("|", end=" ")

    for j in range(3, 6):
      print(sudoku[i][j], end=" ")
      time.sleep(0.002)
    print("|", end=" ")
  
    for j in range(6, 9):
      print(sudoku[i][j], end=" ")
      time.sleep(0.002)
    print(" ")

  print("---------------------")

  for i in range(6,9):
    
    for j in range(0,3):
      print(sudoku[i][j], end=" ")
      time.sleep(0.002)
    print("|", end=" ")

    for j in range(3, 6):
      print(sudoku[i][j], end=" ")
      time.sleep(0.002)
    print("|", end=" ")
  
    for j in range(6, 9):
      print(sudoku[i][j], end=" ")
      time.sleep(0.002)
    print(" ")

# Langkah 1 : Mencari grid yang kosong
def cari_kosong(sudoku) :

  for i in range(9):
    for j in range(9):
      if sudoku[i][j] == 0:
        return i, j

  # Apabila tidak ada grid yang kosong, artinya sudoku sudah terpecahkan, dan return None, None
  return None, None

# Langkah 2 : Cek validasi input 
def cek_input(sudoku, iterasi, baris, kolom):
  
  # Validasi tingkat baris
  nilai_baris = sudoku[baris]

  if iterasi in nilai_baris:
    return False

  # Validasi tingkat kolom
  nilai_kolom = [sudoku[i][kolom] for i in range(9)]
  
  if iterasi in nilai_kolom:
    return False

  # Validasi tingkat kotak
  i_awal = (baris//3)*3 
  j_awal = (kolom//3)*3

  for i in range(i_awal, i_awal+3):
    for j in range(j_awal, j_awal+3):
      if iterasi == sudoku[i][j]:
        return False
  
  return True # Input tervalidasi sebagai solusi

# Langkah 3 : Solusi
def sudoku_solver(sudoku):

  # Memasukkkan input untuk menyelesaikan grid sudoku yang kosong
  baris, kolom = cari_kosong(sudoku) # f(x), x bisa apa saja, sudoku bisa apa saja

  # Apabila sudoku selesai, logika di bawah akan True saat cari_kosong me-return None
  if kolom is None:
    return True
  
  # Apabila masih ada grid yang kosong, maka dilakukan iterasi untuk menebak setiap solusi sudoku yang mungkin
  for iterasi in range(0,10):
    
    # Apabila iter nya merupakan solusi, grid diganti dengan nilai iter
    if cek_input(sudoku, iterasi, baris, kolom):
      sudoku[baris][kolom] = iterasi

      # Rekursi pada fungsi sudoku_solver
      if sudoku_solver(sudoku):
        return True
        
    # Apabila iter bukan solusi
    sudoku[baris][kolom]=0

  # Apabila tidak ada solusi
  return False


for i in range(9):
  for j in range(9):
    print("WELCOME TO SUDOKU SOLVER!")
    print("")
    print_grid(grid)
    grid[i][j] = int(input("Masukkan angka baris ke-"+str(i+1)+" kolom ke-"+str(j+1)+": "))
    os.system("cls")


def print_sol():
  input("Tekan Enter untuk mencetak solusi!")
  os.system("cls")
  sudoku_solver(grid)
  print("Solution:")
  print_grid(grid)

print_sol()
