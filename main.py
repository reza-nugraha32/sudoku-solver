
# Grid sudoku yang menjadi input
grid = [
  [1, 0, 0,   5, 0, 0,   0, 4, 3],
  [4, 7, 0,   1, 0, 2,   0, 5, 0],
  [0, 0, 0,   0, 0, 0,   2, 9, 1],

  [9, 0, 3,   4, 0, 0,   5, 8, 6],
  [6, 0, 0,   0, 0, 5,   0, 2, 0],
  [0, 5, 0,   0, 0, 0,   1, 7, 0],

  [3, 0, 5,   8, 0, 0,   9, 6, 2],
  [0, 2, 6,   3, 0, 9,   8, 0, 5],
  [8, 0, 0,   0, 5, 0,   0, 0, 0]
  ]


# Fungsi untuk print grid
# i = baris
# j = kolom

def print_grid(sudoku):
  for i in range(0,3):

    for j in range(0,3):
      print(sudoku[i][j], end=" ")
    print("|", end=" ")

    for j in range(3, 6):
      print(sudoku[i][j], end=" ")
    print("|", end=" ")

    for j in range(6, 9):
      print(sudoku[i][j], end=" ")
    print(" ")

  print("---------------------")

  for i in range(3,6):

    for j in range(0,3):
      print(sudoku[i][j], end=" ")
    print("|", end=" ")

    for j in range(3, 6):
      print(sudoku[i][j], end=" ")
    print("|", end=" ")
  
    for j in range(6, 9):
      print(sudoku[i][j], end=" ")
    print(" ")

  print("---------------------")

  for i in range(6,9):

    for j in range(0,3):
      print(sudoku[i][j], end=" ")
    print("|", end=" ")

    for j in range(3, 6):
      print(sudoku[i][j], end=" ")
    print("|", end=" ")
  
    for j in range(6, 9):
      print(sudoku[i][j], end=" ")
    print(" ")

# Langkah 1 : Mencari grid yang kosong
def empty_grid(sudoku) :

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
      if sudoku[i][j] == iterasi:
        return False
  
  return True # Input tervalidasi sebagai solusi

# Langkah 3 : Solusi
def sudoku_solver(sudoku):

  # Memasukkkan input untuk menyelesaikan grid sudoku yang kosong
  baris, kolom = empty_grid(sudoku)

  # Apabila sudoku selesai, logika di bawah akan True saat empty_grid me-return None
  if kolom is None:
    return True
  
  # Apabila masih ada grid yang kosong, maka dilakukan iterasi untuk menebak setiap solusi sudoku yang mungkin
  for iterasi in range(1,10):
    
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

print(sudoku_solver(grid))
print(print_grid(grid))
