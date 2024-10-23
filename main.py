import matplotlib.pyplot as plt

def dda(x1, y1, x2, y2):
    # Untuk menentukan deltax dan deltay
    dx = x2 - x1
    dy = y2 - y1
    
    # Menentukan langkah yang diperlukan
    steps = int(max(abs(dx), abs(dy)))
    
    # increment untuk x dan y
    x_increment = dx / steps
    y_increment = dy / steps
    
    # Menyimpan titik-titik garis
    x = x1
    y = y1
    
    # List untuk menyimpan koordinat titik
    points = [(x, y)]
    
    for _ in range(steps):
        x += x_increment
        y += y_increment
        points.append((round(x), round(y)))  # Membulatkan nilai x dan y
    
    return points

# Titik awal dan akhir
x1, y1 = 30, 4
x2, y2 = 4, 30

# Menggambar garis
points = dda(x1, y1, x2, y2)

# Menyiapkan data untuk grafik
x_values, y_values = zip(*points)

# Membuat plot
plt.plot(x_values, y_values, marker='o')
plt.title('Garis antara titik (30, 4) dan (4, 30) dengan Algoritma DDA')
plt.xlim(0, 35)
plt.ylim(0, 35)
plt.grid()
plt.xlabel('X')
plt.ylabel('Y')
plt.show()