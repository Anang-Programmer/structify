import time

class Queue:
    def __init__(self, max_capacity=10):
        self.queue_data = []
        self.max_capacity = max_capacity
    
    def enqueue_value(self):
        """Menambahkan nilai ke dalam queue"""
        try:
            value = input("Masukkan nilai untuk enqueue: ").strip()
            
            if value == '':
                self.show_result('Silakan masukkan nilai untuk enqueue', is_error=True)
                return
            
            if len(self.queue_data) >= self.max_capacity:
                self.show_result('Queue penuh!', is_error=True)
                return
            
            # Simulasi loading effect
            print("Processing...")
            time.sleep(0.3)
            
            self.queue_data.append(int(value))
            self.update_display()
            self.show_result(f'Enqueued {value} ke queue')
            
        except ValueError:
            self.show_result('Masukkan angka yang valid!', is_error=True)
    
    def dequeue_value(self):
        """Menghapus dan mengembalikan nilai dari depan queue"""
        if len(self.queue_data) == 0:
            self.show_result('Queue kosong! Tidak bisa dequeue', is_error=True)
            return
        
        # Simulasi loading effect
        print("Processing...")
        time.sleep(0.3)
        
        dequeued_value = self.queue_data.pop(0)
        self.update_display()
        self.show_result(f'Dequeued {dequeued_value} dari queue')
        return dequeued_value
    
    def front_value(self):
        """Menampilkan nilai di depan queue tanpa menghapusnya"""
        if len(self.queue_data) == 0:
            self.show_result('Queue kosong! Tidak ada elemen depan', is_error=True)
            return
        
        # Simulasi loading effect
        print("Processing...")
        time.sleep(0.3)
        
        front_element = self.queue_data[0]
        self.show_result(f'Elemen depan adalah: {front_element}')
        return front_element
    
    def rear_value(self):
        """Menampilkan nilai di belakang queue tanpa menghapusnya"""
        if len(self.queue_data) == 0:
            self.show_result('Queue kosong! Tidak ada elemen belakang', is_error=True)
            return
        
        # Simulasi loading effect
        print("Processing...")
        time.sleep(0.3)
        
        rear_element = self.queue_data[-1]
        self.show_result(f'Elemen belakang adalah: {rear_element}')
        return rear_element
    
    def clear_queue(self):
        """Mengosongkan semua elemen dalam queue"""
        print("Processing...")
        time.sleep(0.3)
        
        self.queue_data = []
        self.update_display()
        self.show_result('Queue dikosongkan')
    
    def update_display(self):
        """Menampilkan status queue saat ini"""
        print(f"\n{'='*40}")
        print(f"Status Queue: {self.queue_data}")
        print(f"Ukuran: {len(self.queue_data)}/{self.max_capacity}")
        print(f"{'='*40}")
    
    def show_result(self, message, is_error=False):
        """Menampilkan pesan hasil operasi"""
        if is_error:
            print(f"❌ ERROR: {message}")
        else:
            print(f"✅ {message}")
    
    def show_menu(self):
        """Menampilkan menu pilihan"""
        print("\n" + "="*50)
        print("           QUEUE OPERATIONS MENU")
        print("="*50)
        print("1. Enqueue (Tambah nilai)")
        print("2. Dequeue (Hapus nilai depan)")
        print("3. Front (Lihat nilai depan)")
        print("4. Rear (Lihat nilai belakang)")
        print("5. Clear (Kosongkan queue)")
        print("6. Display (Tampilkan queue)")
        print("0. Exit")
        print("="*50)
    
    def run(self):
        """Menjalankan program queue interaktif"""
        print("🚀 Program Queue Python")
        print(f"Kapasitas maksimum: {self.max_capacity}")
        self.update_display()
        
        while True:
            self.show_menu()
            
            try:
                choice = input("\nPilih operasi (0-6): ").strip()
                
                if choice == '1':
                    self.enqueue_value()
                elif choice == '2':
                    self.dequeue_value()
                elif choice == '3':
                    self.front_value()
                elif choice == '4':
                    self.rear_value()
                elif choice == '5':
                    self.clear_queue()
                elif choice == '6':
                    self.update_display()
                elif choice == '0':
                    print("👋 Terima kasih! Program selesai.")
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
    queue = Queue(max_capacity=10)
    queue.run()
    