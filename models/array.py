class ArrayOperations:
    def __init__(self, max_capacity=10):
        self.array_data = []
        self.max_capacity = max_capacity
    
    #Menampilkan array saat ini
    def display_array(self):
        print("\n" + "="*50)
        print("Current Array:")
        if not self.array_data:
            print("[ EMPTY ]")
        else:
            array_str = "[ "
            for i, value in enumerate(self.array_data):
                array_str += f"{value}"
                if i < len(self.array_data) - 1:
                    array_str += ", "
            array_str += " ]"
            print(array_str)
        print(f"Size: {len(self.array_data)}/{self.max_capacity}")
        print("="*50)
    
    # Menampilkan hasil operasi
    def show_result(self, message, is_error=False):
        if is_error:
            print(f"❌ ERROR: {message}")
        else:
            print(f"✅ SUCCESS: {message}")
            
    #Insert value di akhir array
    def insert_value(self):
    
        try:
            value = input("Enter value to insert: ").strip()
            if not value:
                self.show_result("Please enter a value", True)
                return
            
            if len(self.array_data) >= self.max_capacity:
                self.show_result("Array is full! Cannot insert more elements.", True)
                return
            
            self.array_data.append(int(value))
            self.display_array()
            self.show_result(f"Inserted {value} at index {len(self.array_data) - 1}")
            
        except ValueError:
            self.show_result("Please enter a valid number", True)
    
    def insert_at_index(self):
        """Insert value di index tertentu"""
        try:
            value = input("Enter value to insert: ").strip()
            index = input("Enter index position: ").strip()
            
            if not value or not index:
                self.show_result("Please enter both value and index", True)
                return
            
            idx = int(index)
            if idx < 0 or idx > len(self.array_data):
                self.show_result("Index out of bounds", True)
                return
            
            if len(self.array_data) >= self.max_capacity:
                self.show_result("Array is full! Cannot insert more elements.", True)
                return
            
            self.array_data.insert(idx, int(value))
            self.display_array()
            self.show_result(f"Inserted {value} at index {idx}")
            
        except ValueError:
            self.show_result("Please enter valid numbers", True)
    
    def delete_at_index(self):
        """Delete value di index tertentu"""
        try:
            index = input("Enter index to delete: ").strip()
            
            if not index:
                self.show_result("Please enter index to delete", True)
                return
            
            idx = int(index)
            if idx < 0 or idx >= len(self.array_data):
                self.show_result("Index out of bounds", True)
                return
            
            deleted_value = self.array_data.pop(idx)
            self.display_array()
            self.show_result(f"Deleted value {deleted_value} from index {idx}")
            
        except ValueError:
            self.show_result("Please enter a valid number", True)
    
    def search_value(self):
        """Search value dalam array"""
        try:
            value = input("Enter value to search: ").strip()
            
            if not value:
                self.show_result("Please enter value to search", True)
                return
            
            search_val = int(value)
            try:
                index = self.array_data.index(search_val)
                self.show_result(f"Value {value} found at index {index}")
                # Highlight found element
                self.highlight_element(index)
            except ValueError:
                self.show_result(f"Value {value} not found in array", True)
                
        except ValueError:
            self.show_result("Please enter a valid number", True)
    
    def highlight_element(self, index):
        """Highlight element yang ditemukan"""
        print("\nHighlighted Array:")
        array_str = "[ "
        for i, value in enumerate(self.array_data):
            if i == index:
                array_str += f">>> {value} <<<"  # Highlight
            else:
                array_str += f"{value}"
            if i < len(self.array_data) - 1:
                array_str += ", "
        array_str += " ]"
        print(array_str)
    
    def clear_array(self):
        """Clear semua element dari array"""
        if len(self.array_data) == 0:
            self.show_result("Array is already empty", True)
            return
        
        self.array_data = []
        self.display_array()
        self.show_result("Array cleared successfully")
    
    def show_menu(self):
        """Menampilkan menu operasi"""
        print("\n" + "="*50)
        print("           ARRAY OPERATIONS MENU")
        print("="*50)
        print("1. Insert value (at end)")
        print("2. Insert at specific index")
        print("3. Delete at index")
        print("4. Search value")
        print("5. Clear array")
        print("6. Display array")
        print("7. Exit")
        print("="*50)
    
    def run(self):
        """Main program loop"""
        print("🚀 Welcome to Array Operations Console App!")
        print(f"Maximum array capacity: {self.max_capacity}")
        self.display_array()
        
        while True:
            self.show_menu()
            choice = input("Choose operation (1-7): ").strip()
            
            if choice == '1':
                self.insert_value()
            elif choice == '2':
                self.insert_at_index()
            elif choice == '3':
                self.delete_at_index()
            elif choice == '4':
                self.search_value()
            elif choice == '5':
                self.clear_array()
            elif choice == '6':
                self.display_array()
            elif choice == '7':
                print("\n👋 Thank you for using Array Operations App!")
                break
            else:
                self.show_result("Invalid choice! Please choose 1-7", True)
            
            input("\nPress Enter to continue...")

# Jalankan program
if __name__ == "__main__":
    # Buat instance dengan kapasitas maksimal 10 (bisa diubah)
    app = ArrayOperations(max_capacity=10)
    app.run()