import time

class RecursiveCalculator:
    def __init__(self):
        self.call_count = 0
        self.show_steps = False
    
    def fibonacci(self, n, depth=0):
        """
        Menghitung bilangan Fibonacci ke-n menggunakan rekursi
        F(n) = F(n-1) + F(n-2), dengan F(0) = 0, F(1) = 1
        """
        self.call_count += 1
        
        if self.show_steps:
            print("  " * depth + f"fibonacci({n})")
        
        # Base case
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        
        # Recursive case
        return self.fibonacci(n-1, depth+1) + self.fibonacci(n-2, depth+1)
    
    def factorial(self, n, depth=0):
        """
        Menghitung faktorial n menggunakan rekursi
        n! = n × (n-1)!, dengan 0! = 1
        """
        self.call_count += 1
        
        if self.show_steps:
            print("  " * depth + f"factorial({n})")
        
        # Base case
        if n <= 1:
            return 1
        
        # Recursive case
        return n * self.factorial(n-1, depth+1)
    
    def power(self, base, exp, depth=0):
        """
        Menghitung perpangkatan base^exp menggunakan rekursi
        base^exp = base × base^(exp-1), dengan base^0 = 1
        """
        self.call_count += 1
        
        if self.show_steps:
            print("  " * depth + f"power({base}, {exp})")
        
        # Base case
        if exp == 0:
            return 1
        elif exp == 1:
            return base
        
        # Recursive case
        if exp > 0:
            return base * self.power(base, exp-1, depth+1)
        else:
            # Untuk eksponen negatif
            return 1 / self.power(base, -exp, depth+1)
    
    def fibonacci_optimized(self, n, memo=None):
        """
        Fibonacci dengan memoization untuk optimasi
        """
        if memo is None:
            memo = {}
        
        self.call_count += 1
        
        if n in memo:
            return memo[n]
        
        if n <= 0:
            result = 0
        elif n == 1:
            result = 1
        else:
            result = self.fibonacci_optimized(n-1, memo) + self.fibonacci_optimized(n-2, memo)
        
        memo[n] = result
        return result
    
    def power_optimized(self, base, exp):
        """
        Perpangkatan dengan optimasi (fast exponentiation)
        """
        self.call_count += 1
        
        if exp == 0:
            return 1
        elif exp == 1:
            return base
        elif exp % 2 == 0:
            # Jika eksponen genap: base^exp = (base^(exp/2))^2
            half_power = self.power_optimized(base, exp // 2)
            return half_power * half_power
        else:
            # Jika eksponen ganjil: base^exp = base × base^(exp-1)
            return base * self.power_optimized(base, exp - 1)
    
    def reset_counter(self):
        """Reset counter untuk menghitung panggilan fungsi"""
        self.call_count = 0
    
    def calculate_fibonacci(self):
        """Menu untuk menghitung Fibonacci"""
        print("\n🔢 FIBONACCI CALCULATOR")
        print("=" * 40)
        
        try:
            n = int(input("Masukkan nilai n untuk Fibonacci ke-n: "))
            
            if n < 0:
                print("❌ Nilai n harus >= 0")
                return
            
            show_steps = input("Tampilkan langkah-langkah? (y/n): ").lower() == 'y'
            self.show_steps = show_steps
            
            print(f"\n📊 Menghitung Fibonacci({n})...")
            
            # Fibonacci biasa
            self.reset_counter()
            start_time = time.time()
            
            if show_steps:
                print("\nLangkah-langkah rekursi:")
            
            result = self.fibonacci(n)
            end_time = time.time()
            
            print(f"\n✅ Hasil: Fibonacci({n}) = {result}")
            print(f"⏱️  Waktu eksekusi: {end_time - start_time:.4f} detik")
            print(f"🔄 Jumlah panggilan rekursi: {self.call_count}")
            
            # Jika n cukup besar, tawarkan versi optimized
            if n > 10:
                use_optimized = input("\nGunakan versi optimized? (y/n): ").lower() == 'y'
                if use_optimized:
                    self.reset_counter()
                    start_time = time.time()
                    result_opt = self.fibonacci_optimized(n)
                    end_time = time.time()
                    
                    print(f"\n✅ Hasil (Optimized): Fibonacci({n}) = {result_opt}")
                    print(f"⏱️  Waktu eksekusi: {end_time - start_time:.4f} detik")
                    print(f"🔄 Jumlah panggilan rekursi: {self.call_count}")
                    
        except ValueError:
            print("❌ Masukkan angka yang valid!")
    
    def calculate_factorial(self):
        """Menu untuk menghitung Faktorial"""
        print("\n🔢 FACTORIAL CALCULATOR")
        print("=" * 40)
        
        try:
            n = int(input("Masukkan nilai n untuk n!: "))
            
            if n < 0:
                print("❌ Faktorial tidak terdefinisi untuk bilangan negatif")
                return
            
            show_steps = input("Tampilkan langkah-langkah? (y/n): ").lower() == 'y'
            self.show_steps = show_steps
            
            print(f"\n📊 Menghitung {n}!...")
            
            self.reset_counter()
            start_time = time.time()
            
            if show_steps:
                print("\nLangkah-langkah rekursi:")
            
            result = self.factorial(n)
            end_time = time.time()
            
            print(f"\n✅ Hasil: {n}! = {result}")
            print(f"⏱️  Waktu eksekusi: {end_time - start_time:.4f} detik")
            print(f"🔄 Jumlah panggilan rekursi: {self.call_count}")
            
            # Tampilkan penjelasan matematis
            if n <= 10:
                explanation = " × ".join(str(i) for i in range(n, 0, -1))
                print(f"📝 Penjelasan: {n}! = {explanation} = {result}")
                
        except ValueError:
            print("❌ Masukkan angka yang valid!")
    
    def calculate_power(self):
        """Menu untuk menghitung Perpangkatan"""
        print("\n🔢 POWER CALCULATOR")
        print("=" * 40)
        
        try:
            base = float(input("Masukkan bilangan dasar (base): "))
            exp = int(input("Masukkan eksponen (pangkat): "))
            
            show_steps = input("Tampilkan langkah-langkah? (y/n): ").lower() == 'y'
            self.show_steps = show_steps
            
            print(f"\n📊 Menghitung {base}^{exp}...")
            
            # Perpangkatan biasa
            self.reset_counter()
            start_time = time.time()
            
            if show_steps:
                print("\nLangkah-langkah rekursi:")
            
            result = self.power(base, exp)
            end_time = time.time()
            
            print(f"\n✅ Hasil: {base}^{exp} = {result}")
            print(f"⏱️  Waktu eksekusi: {end_time - start_time:.4f} detik")
            print(f"🔄 Jumlah panggilan rekursi: {self.call_count}")
            
            # Jika eksponen cukup besar, tawarkan versi optimized
            if abs(exp) > 5:
                use_optimized = input("\nGunakan versi optimized? (y/n): ").lower() == 'y'
                if use_optimized:
                    self.reset_counter()
                    start_time = time.time()
                    result_opt = self.power_optimized(base, abs(exp))
                    if exp < 0:
                        result_opt = 1 / result_opt
                    end_time = time.time()
                    
                    print(f"\n✅ Hasil (Optimized): {base}^{exp} = {result_opt}")
                    print(f"⏱️  Waktu eksekusi: {end_time - start_time:.4f} detik")
                    print(f"🔄 Jumlah panggilan rekursi: {self.call_count}")
                    
        except ValueError:
            print("❌ Masukkan angka yang valid!")
    
    def show_theory(self):
        """Menampilkan teori rekursi"""
        print("\n📚 TEORI REKURSI")
        print("=" * 50)
        
        print("🔄 Rekursi adalah teknik pemrograman dimana fungsi memanggil dirinya sendiri.")
        print("\n📋 Komponen utama rekursi:")
        print("1. Base Case: Kondisi yang menghentikan rekursi")
        print("2. Recursive Case: Fungsi memanggil dirinya sendiri")
        
        print("\n🔢 Contoh implementasi:")
        
        print("\n1. FIBONACCI:")
        print("   F(n) = F(n-1) + F(n-2)")
        print("   Base case: F(0) = 0, F(1) = 1")
        print("   Contoh: F(5) = F(4) + F(3) = 5 + 3 = 8")
        
        print("\n2. FAKTORIAL:")
        print("   n! = n × (n-1)!")
        print("   Base case: 0! = 1, 1! = 1")
        print("   Contoh: 5! = 5 × 4! = 5 × 24 = 120")
        
        print("\n3. PERPANGKATAN:")
        print("   base^exp = base × base^(exp-1)")
        print("   Base case: base^0 = 1, base^1 = base")
        print("   Contoh: 2^5 = 2 × 2^4 = 2 × 16 = 32")
        
        print("\n⚠️  Catatan:")
        print("- Rekursi dapat menyebabkan stack overflow jika terlalu dalam")
        print("- Optimasi seperti memoization dapat meningkatkan performa")
        print("- Kompleksitas waktu berbeda untuk setiap jenis rekursi")
    
    def compare_algorithms(self):
        """Membandingkan performa algoritma"""
        print("\n📊 PERBANDINGAN ALGORITMA")
        print("=" * 50)
        
        try:
            n = int(input("Masukkan nilai untuk perbandingan (disarankan 5-15): "))
            
            if n < 0:
                print("❌ Nilai harus >= 0")
                return
            
            print(f"\n🔍 Membandingkan algoritma untuk n = {n}:")
            print("-" * 50)
            
            # Fibonacci
            print("\n1. FIBONACCI:")
            self.reset_counter()
            start = time.time()
            fib_result = self.fibonacci(n)
            fib_time = time.time() - start
            fib_calls = self.call_count
            
            self.reset_counter()
            start = time.time()
            fib_opt_result = self.fibonacci_optimized(n)
            fib_opt_time = time.time() - start
            fib_opt_calls = self.call_count
            
            print(f"   Biasa:     {fib_result} ({fib_time:.4f}s, {fib_calls} calls)")
            print(f"   Optimized: {fib_opt_result} ({fib_opt_time:.4f}s, {fib_opt_calls} calls)")
            
            # Faktorial
            print("\n2. FAKTORIAL:")
            self.reset_counter()
            start = time.time()
            fact_result = self.factorial(n)
            fact_time = time.time() - start
            fact_calls = self.call_count
            
            print(f"   Hasil: {fact_result} ({fact_time:.4f}s, {fact_calls} calls)")
            
            # Perpangkatan
            base = 2
            print(f"\n3. PERPANGKATAN ({base}^{n}):")
            self.reset_counter()
            start = time.time()
            pow_result = self.power(base, n)
            pow_time = time.time() - start
            pow_calls = self.call_count
            
            self.reset_counter()
            start = time.time()
            pow_opt_result = self.power_optimized(base, n)
            pow_opt_time = time.time() - start
            pow_opt_calls = self.call_count
            
            print(f"   Biasa:     {pow_result} ({pow_time:.4f}s, {pow_calls} calls)")
            print(f"   Optimized: {pow_opt_result} ({pow_opt_time:.4f}s, {pow_opt_calls} calls)")
            
            print(f"\n📈 Kesimpulan:")
            print(f"- Fibonacci optimized {fib_calls/fib_opt_calls:.1f}x lebih efisien")
            print(f"- Power optimized {pow_calls/pow_opt_calls:.1f}x lebih efisien")
            print(f"- Faktorial linear O(n) - tidak perlu optimasi")
            
        except ValueError:
            print("❌ Masukkan angka yang valid!")
    
    def show_menu(self):
        """Menampilkan menu utama"""
        print("\n" + "="*60)
        print("           🔄 PROGRAM REKURSI PYTHON 🔄")
        print("="*60)
        print("1. 📈 Fibonacci Calculator")
        print("2. 📊 Factorial Calculator") 
        print("3. ⚡ Power Calculator")
        print("4. 📚 Teori Rekursi")
        print("5. 📊 Perbandingan Algoritma")
        print("6. 🧮 Kalkulator Gabungan")
        print("0. 🚪 Exit")
        print("="*60)
    
    def combined_calculator(self):
        """Kalkulator yang menggabungkan semua fungsi"""
        print("\n🧮 KALKULATOR GABUNGAN")
        print("=" * 40)
        
        try:
            n = int(input("Masukkan nilai n: "))
            
            if n < 0:
                print("❌ Nilai harus >= 0")
                return
            
            print(f"\n📊 Hasil untuk n = {n}:")
            print("-" * 30)
            
            # Fibonacci
            self.reset_counter()
            fib_result = self.fibonacci_optimized(n) if n > 10 else self.fibonacci(n)
            print(f"📈 Fibonacci({n}) = {fib_result}")
            
            # Faktorial
            self.reset_counter()
            fact_result = self.factorial(n)
            print(f"📊 {n}! = {fact_result}")
            
            # Perpangkatan (base = 2)
            self.reset_counter()
            pow_result = self.power_optimized(2, n) if n > 5 else self.power(2, n)
            print(f"⚡ 2^{n} = {pow_result}")
            
            # Perpangkatan (base = n)
            if n > 0:
                self.reset_counter()
                pow_n_result = self.power_optimized(n, n) if n > 3 else self.power(n, n)
                print(f"🔥 {n}^{n} = {pow_n_result}")
            
        except ValueError:
            print("❌ Masukkan angka yang valid!")
    
    def run(self):
        """Menjalankan program utama"""
        print("🚀 Selamat datang di Program Rekursi Python!")
        print("Program ini mendemonstrasikan 3 algoritma rekursi klasik:")
        print("📈 Fibonacci, 📊 Faktorial, dan ⚡ Perpangkatan")
        
        while True:
            self.show_menu()
            
            try:
                choice = input("\nPilih menu (0-6): ").strip()
                
                if choice == '1':
                    self.calculate_fibonacci()
                elif choice == '2':
                    self.calculate_factorial()
                elif choice == '3':
                    self.calculate_power()
                elif choice == '4':
                    self.show_theory()
                elif choice == '5':
                    self.compare_algorithms()
                elif choice == '6':
                    self.combined_calculator()
                elif choice == '0':
                    print("\n👋 Terima kasih telah menggunakan Program Rekursi!")
                    print("🎓 Semoga membantu dalam memahami konsep rekursi!")
                    break
                else:
                    print("❌ Pilihan tidak valid! Silakan pilih 0-6.")
                    
            except KeyboardInterrupt:
                print("\n\n👋 Program dihentikan oleh user.")
                break
            except Exception as e:
                print(f"❌ Terjadi error: {e}")

# Cara menjalankan program
if __name__ == "__main__":
    calculator = RecursiveCalculator()
    calculator.run()
    
    # Contoh penggunaan langsung:
    # calc = RecursiveCalculator()
    # print(f"Fibonacci(10) = {calc.fibonacci(10)}")
    # print(f"10! = {calc.factorial(10)}")
    # print(f"2^10 = {calc.power(2, 10)}")