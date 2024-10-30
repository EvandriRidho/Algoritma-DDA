import matplotlib.pyplot as plt

def dda(x1, y1, x2, y2):
    # Menghitung delta x dan delta y
    dx = x2 - x1
    dy = y2 - y1
    
    # Menentukan jumlah langkah yang diperlukan
    steps = int(max(abs(dx), abs(dy)))
    
    # Increment untuk setiap langkah
    x_increment = dx / steps
    y_increment = dy / steps
    
    # Titik awal
    x = x1
    y = y1
    
    # List untuk menyimpan koordinat titik
    points = [(x, y)]
    
    for _ in range(steps):
        x += x_increment
        y += y_increment
        points.append((round(x), round(y)))  # Membulatkan koordinat
    
    return points

# Titik awal dan akhir yang benar
x1, y1 = 30, 20
x2, y2 = 37, 27

# Menghitung titik-titik garis menggunakan DDA
points = dda(x1, y1, x2, y2)

# Ekstrak nilai x dan y untuk plotting
x_values, y_values = zip(*points)

# Membuat plot
plt.plot(x_values, y_values, marker='o')
plt.title('Garis antara titik (30, 20) dan (37, 27) dengan Algoritma DDA')
plt.xlim(0, 40)
plt.ylim(0, 40)
plt.grid()
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
