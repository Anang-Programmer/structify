import time
import os

class Stack:
    def __init__(self, max_capacity=10):
        self.stack_data = []
        self.max_capacity = max_capacity
    
    def highlight_element(self, message="Processing..."):
        """Simulasi highlight element dengan loading effect"""
        print(f"{message}")
        self.loading_animation()
    
    def loading_animation(self, duration=0.6):
        """Simulasi animasi loading"""
        animation_chars = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
        end_time = time.time() + duration
        
        while time.time() < end_time:
            for char in animation_chars:
                if time.time() >= end_time:
                    break
                print(f'\r{char} Processing...', end='', flush=True)
                time.sleep(0.05)
        
        print('\rDone!        ')
    
    def show_result(self, message, is_error=False, duration=3):
        """Menampilkan hasil operasi dengan delay"""
        if is_error:
            print(f"ERROR: {message}")
        else:
            print(f"{message}")
        
        # Simulasi auto-hide dengan countdown
        if duration > 0:
            for i in range(3, 0, -1):
                print(f"Message akan hilang dalam {i} detik...", end='\r', flush=True)
                time.sleep(1)
            print("                                            ", end='\r')  # Clear line
    
    def push_value(self):
        """Menambahkan nilai ke top of stack"""
        try:
            value = input("Masukkan nilai untuk push ke stack: ").strip()
            
            if value == '':
                self.show_result('Silakan masukkan nilai untuk push', is_error=True)
                return
            
            if len(self.stack_data) >= self.max_capacity:
                self.show_result('Stack overflow! Kapasitas maksimum tercapai.', is_error=True)
                return
            
            # Add push animation
            self.highlight_element("Pushing value to stack...")
            
            self.stack_data.append(int(value))
            self.update_display()
            self.show_result(f'Pushed {value} to top of stack')
            
        except ValueError:
            self.show_result('Masukkan angka yang valid!', is_error=True)
    
    def pop_value(self):
        """Menghapus dan mengembalikan nilai dari top of stack"""
        if len(self.stack_data) == 0:
            self.show_result('Stack underflow! Tidak bisa pop dari stack kosong.', is_error=True)
            return None
        
        # Add pop animation
        print("Animating pop operation...")
        top_value = self.stack_data[-1]
        
        # Simulate popping animation
        print(f"Popping element: {top_value}")
        for i in range(3):
            print(f"{'  ' * i} {top_value} {'↗️' * (i+1)}")
            time.sleep(0.15)
        
        popped_value = self.stack_data.pop()
        self.update_display()
        self.show_result(f'Popped {popped_value} from stack')
        return popped_value
    
    def peek_value(self):
        """Melihat nilai di top of stack tanpa menghapusnya"""
        if len(self.stack_data) == 0:
            self.show_result('Stack kosong! Tidak ada yang bisa di-peek.', is_error=True)
            return None
        
        top_value = self.stack_data[-1]
        self.show_result(f'Top element is: {top_value}')
        
        # Highlight the top element
        print("Highlighting top element...")
        self.highlight_top_element(top_value)
        
        return top_value
    
    def highlight_top_element(self, value):
        """Highlight elemen teratas dengan animasi"""
        print(f"\n{'='*30}")
        print(f"    TOP ELEMENT")
        print(f"{'='*30}")
        
        # Animasi berkedip
        for i in range(4):
            if i % 2 == 0:
                print(f"    {value}", end='\r', flush=True)
            else:
                print(f"    {value}", end='\r', flush=True)
            time.sleep(0.5)
        
        print(f"    {value}")
        print(f"{'='*30}\n")
    
    def clear_stack(self):
        """Mengosongkan semua elemen dalam stack"""
        if len(self.stack_data) == 0:
            self.show_result('Stack sudah kosong', is_error=True)
            return
        
        # Confirmation
        confirm = input("Yakin ingin menghapus semua elemen? (y/n): ").strip().lower()
        if confirm not in ['y', 'yes']:
            print("Pembersihan stack dibatalkan")
            return
        
        # Clear animation
        print("Clearing stack...")
        original_length = len(self.stack_data)
        
        while self.stack_data:
            removed = self.stack_data.pop()
            print(f"Removing: {removed} (Remaining: {len(self.stack_data)})")
            time.sleep(0.2)
        
        self.update_display()
        self.show_result(f'Stack cleared successfully! Removed {original_length} elements.')
    
    def update_display(self):
        """Menampilkan status stack saat ini dengan visualisasi"""
        os.system('clear' if os.name == 'posix' else 'cls')  # Clear screen
        
        print(f"\n{'='*50}")
        print(f"              STACK STATUS")
        print(f"{'='*50}")
        print(f"Capacity: {len(self.stack_data)}/{self.max_capacity}")
        print(f"{'='*50}")
        
        if not self.stack_data:
            print("│                                                │")
            print("│              STACK KOSONG                      │")
            print("│                                                │")
            print("│                                                │")
        else:
            # Tampilkan stack dari atas ke bawah (LIFO visualization)
            print("│              STACK CONTENTS                    │")
            print("├────────────────────────────────────────────────┤")
            
            # Tampilkan elemen dari index tertinggi (top) ke terendah (bottom)
            for i in range(len(self.stack_data) - 1, -1, -1):
                value = self.stack_data[i]
                
                if i == len(self.stack_data) - 1:  # Top element
                    print(f"│ TOP  ➤  [{value:^10}]                    │")
                    print("├────────────────────────────────────────────────┤")
                else:
                    print(f"│ [{i+1:2}]  ➤     [{value:^10}]                     │")
            
            print("│                                                │")
            print(f"│ BOTTOM ➤ [{self.stack_data[0]:^10}]                │")
        
        print(f"{'='*50}")
        
        # Stack operations info
        print("STACK OPERATIONS:")
        print("   • PUSH: Menambah elemen ke TOP")
        print("   • POP:  Menghapus elemen dari TOP") 
        print("   • PEEK: Melihat elemen TOP tanpa menghapus")
        print("   • CLEAR: Mengosongkan semua elemen")
        print(f"{'='*50}")
    
    def show_stack_info(self):
        """Menampilkan informasi detail tentang stack"""
        print(f"\n{'='*60}")
        print(f"                   STACK INFORMATION")
        print(f"{'='*60}")
        
        if not self.stack_data:
            print("Stack Status: EMPTY")
            print("Size: 0")
            print("Memory Usage: Minimal")
        else:
            print(f"Stack Status: ACTIVE")
            print(f"Size: {len(self.stack_data)}")
            print(f"Usage: {len(self.stack_data)}/{self.max_capacity} ({(len(self.stack_data)/self.max_capacity)*100:.1f}%)")
            print(f"Top Element: {self.stack_data[-1]}")
            print(f"Bottom Element: {self.stack_data[0]}")
            print(f"All Elements: {self.stack_data}")
            
            # Statistics
            if len(self.stack_data) > 1:
                avg_value = sum(self.stack_data) / len(self.stack_data)
                max_value = max(self.stack_data)
                min_value = min(self.stack_data)
                
                print(f"\nSTATISTICS:")
                print(f"   Average: {avg_value:.2f}")
                print(f"   Maximum: {max_value}")
                print(f"   Minimum: {min_value}")
                print(f"   Range: {max_value - min_value}")
        
        print(f"{'='*60}")
    
    def demonstrate_lifo(self):
        """Demonstrasi konsep LIFO (Last In, First Out)"""
        print("\nDEMONSTRASI LIFO (Last In, First Out)")
        print("="*50)
        
        demo_values = [10, 20, 30]
        original_stack = self.stack_data.copy()
        
        print("Mari kita push beberapa nilai untuk demo:")
        
        for value in demo_values:
            print(f"\nPushing {value}...")
            self.stack_data.append(value)
            time.sleep(1)
            
            # Show mini display
            print(f"   Stack sekarang: {self.stack_data}")
            print(f"   Top element: {self.stack_data[-1]}")
        
        print(f"\nStack setelah push: {self.stack_data}")
        
        print("\nSekarang mari kita pop satu per satu:")
        
        while len(self.stack_data) > len(original_stack):
            top_value = self.stack_data[-1]
            print(f"\nPopping: {top_value}")
            self.stack_data.pop()
            time.sleep(1)
            
            if len(self.stack_data) > len(original_stack):
                print(f"   Stack sekarang: {self.stack_data}")
                print(f"   New top: {self.stack_data[-1]}")
            else:
                print(f"   Stack sekarang: {self.stack_data if len(self.stack_data) > 0 else 'EMPTY'}")
        
        print("\nDemo LIFO selesai!")
        print("Perhatikan: Yang terakhir masuk (30) adalah yang pertama keluar!")
        
        # Restore original stack
        self.stack_data = original_stack
    
    def show_menu(self):
        """Menampilkan menu pilihan"""
        print("\n" + "="*60)
        print("                STACK OPERATIONS MENU")
        print("="*60)
        print("1. Push (Tambah elemen ke top)")
        print("2. Pop (Hapus elemen dari top)")
        print("3. Peek (Lihat elemen top)")
        print("4. Clear (Kosongkan stack)")
        print("5. Display (Tampilkan stack)")
        print("6. Stack Info (Info detail)")
        print("7. Demo LIFO (Demonstrasi)")
        print("8. Batch Operations (Operasi batch)")
        print("0. Exit")
        print("="*60)
    
    def batch_operations(self):
        """Operasi batch untuk multiple push/pop"""
        print("\nBATCH OPERATIONS")
        print("="*40)
        
        print("1. Batch Push")
        print("2. Batch Pop")
        choice = input("Pilih operasi (1-2): ").strip()
        
        if choice == '1':
            values_input = input("Masukkan nilai-nilai (pisahkan dengan koma): ").strip()
            if not values_input:
                print("Input kosong!")
                return
            
            try:
                values = [int(x.strip()) for x in values_input.split(',')]
                
                print(f"\nPushing {len(values)} values...")
                for i, value in enumerate(values, 1):
                    if len(self.stack_data) >= self.max_capacity:
                        print(f"Stack penuh! Hanya berhasil push {i-1} dari {len(values)} nilai.")
                        break
                    
                    self.stack_data.append(value)
                    print(f"   {i}. Pushed {value}")
                    time.sleep(0.3)
                
                self.update_display()
                print(f"Batch push selesai!")
                
            except ValueError:
                print("Format input salah! Gunakan angka yang dipisahkan koma.")
        
        elif choice == '2':
            if not self.stack_data:
                print("Stack kosong!")
                return
            
            try:
                count = int(input(f"Berapa elemen yang ingin di-pop? (max {len(self.stack_data)}): "))
                count = min(count, len(self.stack_data))
                
                print(f"\nPopping {count} values...")
                popped_values = []
                
                for i in range(count):
                    value = self.stack_data.pop()
                    popped_values.append(value)
                    print(f"   {i+1}. Popped {value}")
                    time.sleep(0.3)
                
                self.update_display()
                print(f"Batch pop selesai! Values: {popped_values}")
                
            except ValueError:
                print("Masukkan angka yang valid!")
    
    def run(self):
        """Menjalankan program stack interaktif"""
        print("Program Stack Python")
        print(f"Kapasitas maksimum: {self.max_capacity}")
        self.update_display()
        
        while True:
            self.show_menu()
            
            try:
                choice = input("\nPilih operasi (0-8): ").strip()
                
                if choice == '1':
                    self.push_value()
                elif choice == '2':
                    self.pop_value()
                elif choice == '3':
                    self.peek_value()
                elif choice == '4':
                    self.clear_stack()
                elif choice == '5':
                    self.update_display()
                elif choice == '6':
                    self.show_stack_info()
                elif choice == '7':
                    self.demonstrate_lifo()
                elif choice == '8':
                    self.batch_operations()
                elif choice == '0':
                    print("\nTerima kasih! Program selesai.")
                    print("Semoga membantu memahami konsep Stack!")
                    break
                else:
                    print("Pilihan tidak valid! Silakan pilih 0-8.")
                    
            except KeyboardInterrupt:
                print("\n\nProgram dihentikan oleh user.")
                break
            except Exception as e:
                print(f"Terjadi error: {e}")

# Cara menjalankan program
if __name__ == "__main__":
    stack = Stack(max_capacity=10)
    stack.run()

