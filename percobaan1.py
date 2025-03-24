import numpy as np
import matplotlib.pyplot as plt

def orbit_planet(planets):
    plt.figure(figsize=(6, 6))
    for planet in planets:
        t = np.linspace(0, 2*np.pi, 100)
        e = np.sqrt(1 - (planet["b"]**2 / planet["a"]**2))
        f = e * planet["a"]
        x = planet["a"] * np.cos(t) - f
        y = planet["b"] * np.sin(t)

        plt.plot(x, y, label=f"Orbit {planet['name']}")
    
    plt.scatter(-f, 0, color="yellow", label="Matahari")
    plt.legend()
    plt.xlabel("X (AU)")
    plt.ylabel("Y (AU)")
    plt.title("Simulasi Orbit Planet")
    plt.grid()
    plt.show()

planets = []

def input_planet():
    nama_planet = input("Masukkan nama planet: ")
    a = float(input("Masukkan panjang sumbu mayor (AU): "))
    b = float(input("Masukkan panjang sumbu minor (AU): "))
    
    planets.append({"name": nama_planet, "a": a, "b": b})


while True:
    print("=== Simulasi Orbit Planet ===")
    print("1. Tambah Planet")
    print("2. Tampilkan Orbit Planet")
    print("3. Keluar")
    pilihan = input("Pilih menu (1-3): ")

    if pilihan == "1":
        input_planet()
    elif pilihan == "2":
        if planets:
            orbit_planet(planets)
        else:
            print("Belum ada data planet! Tambahkan dulu.")
    elif pilihan == "3":
        print("Terima Kasih!\n")
        break
    else:
        print("Pilihan tidak valid, coba lagi\n")
