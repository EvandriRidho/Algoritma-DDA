import matplotlib.pyplot as plt
import numpy as np

class Lingkaran:
    def __init__(self, h, k, r):
        self.h = h  # Koordinat x pusat
        self.k = k  # Koordinat y pusat
        self.r = r  # Radius atau jari-jari

    def persamaan_lingkaran(self):
        # Mengembalikan string persamaan lingkaran
        return f"(x - {self.h})^2 + (y - {self.k})^2 = {self.r**2}"

    def plot_lingkaran(self):
        # Membuat titik-titik untuk lingkaran
        theta = np.linspace(0, 2 * np.pi, 100)
        x = self.h + self.r * np.cos(theta)
        y = self.k + self.r * np.sin(theta)

        # Plot lingkaran
        plt.figure(figsize=(6, 6))
        plt.plot(x, y, label=f"Lingkaran: (x - {self.h})² + (y - {self.k})² = {self.r**2}")

        # Plot pusat lingkaran
        plt.plot(self.h, self.k, 'ro', label="Pusat Lingkaran")

        # Menambah grid, legenda, dan label sumbu
        plt.grid(True)
        plt.axhline(0, color='black', lw=0.5)
        plt.axvline(0, color='black', lw=0.5)
        plt.xlabel("X-Axis")
        plt.ylabel("Y-Axis")
        plt.title("Grafik Lingkaran")
        plt.legend()
        plt.axis('equal')  # Memastikan skala sumbu X dan Y sama
        plt.show()

# Contoh penggunaan
if __name__ == "__main__":
    # Inisialisasi lingkaran dengan pusat (2, 3) dan radius 5
    lingkaran = Lingkaran(5,7,11)

    print("Persamaan Lingkaran:", lingkaran.persamaan_lingkaran())
    lingkaran.plot_lingkaran()