import random  # Mengimpor modul random untuk menghasilkan angka acak

number = random.randint(1, 10)  # Menghasilkan angka acak antara 1 sampai 10 dan menyimpannya ke variabel 'number'
isGuessRight = False  # Variabel boolean untuk menandai apakah tebakan sudah benar atau belum

# Loop akan terus berjalan selama tebakan belum benar
while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")  # Meminta input tebakan dari pengguna
    
    if int(guess) == number:  # Mengecek apakah tebakan (setelah diubah ke integer) sama dengan angka acak
        print("You guessed {}. That is correct! You win!".format(guess))  # Jika benar, tampilkan pesan menang
        isGuessRight = True  # Ubah nilai menjadi True agar loop berhenti
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))  # Jika salah, minta coba lagi
