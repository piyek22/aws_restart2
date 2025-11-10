import csv  # Mengimpor modul csv untuk membaca file CSV
import copy  # Mengimpor modul copy agar bisa membuat salinan objek (deep copy)

# Membuat dictionary template kendaraan dengan nilai awal kosong
myVehicle = {
    "vin" : "<empty>",       # Nomor identifikasi kendaraan
    "make" : "<empty>",      # Merek kendaraan
    "model" : "<empty>",     # Model kendaraan
    "year" : 0,              # Tahun produksi
    "range" : 0,             # Jarak tempuh (range)
    "topSpeed" : 0,          # Kecepatan maksimum
    "zeroSixty" : 0.0,       # Waktu akselerasi 0-60 mph
    "mileage" : 0            # Jarak yang sudah ditempuh (km atau mil)
}

# Menampilkan isi awal dari dictionary myVehicle
for key, value in myVehicle.items():
    print("{} : {}".format(key, value))  # Cetak key dan value tiap item

myInventoryList = []  # List kosong untuk menyimpan data kendaraan yang sudah dibaca dari file

# Membuka file CSV berisi data kendaraan
with open('car_fleet.csv') as csvFile:  # Membuka file car_fleet.csv dalam mode baca
    csvReader = csv.reader(csvFile, delimiter=',')  # Membuat pembaca CSV dengan pemisah koma
    lineCount = 0  # Inisialisasi penghitung baris

    # Membaca setiap baris dari file CSV
    for row in csvReader:
        if lineCount == 0:  # Baris pertama biasanya header (nama kolom)
            print(f'Column names are: {", ".join(row)}')  # Tampilkan nama kolom
            lineCount += 1  # Tambah hitungan baris
        else:  # Untuk baris data berikutnya
            # Cetak data kendaraan dari baris CSV
            print(f'vin: {row[0]} make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}')
            
            currentVehicle = copy.deepcopy(myVehicle)  # Membuat salinan baru dari template myVehicle
            
            # Mengisi data kendaraan berdasarkan isi baris CSV
            currentVehicle["vin"] = row[0]
            currentVehicle["make"] = row[1]
            currentVehicle["model"] = row[2]
            currentVehicle["year"] = row[3]
            currentVehicle["range"] = row[4]
            currentVehicle["topSpeed"] = row[5]
            currentVehicle["zeroSixty"] = row[6]
            currentVehicle["mileage"] = row[7]

            myInventoryList.append(currentVehicle)  # Menambahkan dictionary kendaraan ke list inventory
            lineCount += 1  # Tambah hitungan baris
    
    print(f'Processed {lineCount} lines.')  # Menampilkan jumlah total baris yang sudah diproses

# (Kemungkinan ada indentasi salah di bawah ini)
currentVehicle = copy.deepcopy(myVehicle)  # Membuat salinan baru dari template kendaraan

# Menampilkan semua kendaraan yang sudah ada di myInventoryList
for myCarProperties in myInventoryList:
    for key, value in myCarProperties.items():
        print("{} : {}".format(key, value))  # Cetak semua properti kendaraan
    print("-----")  # Pemisah antar kendaraan
