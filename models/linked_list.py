import time

class LinkedListOperations:
    def __init__(self, max_size=10):
        self.list_data = []
        self.max_size = max_size
    
    def show_result(self, message, is_error=False):
        """Menampilkan hasil operasi"""
        if is_error:
            print(f"❌ ERROR: {message}")
        else:
            print(f"✅ SUCCESS: {message}")
    
    def display_list_visual(self):
        """Menampilkan list dalam format visual"""
        print("\n" + "="*60)
        print("                   CURRENT LIST")
        print("="*60)
        
        if not self.list_data:
            print("[ EMPTY LIST ]")
        else:
            # Visual representation
            list_str = ""
            for i, value in enumerate(self.list_data):
                list_str += f"[{value}]"
                if i < len(self.list_data) - 1:
                    list_str += " → "
            
            print(f"List: {list_str}")
            print(f"Size: {len(self.list_data)}/{self.max_size}")
            
            # Show positions
            pos_str = ""
            for i in range(len(self.list_data)):
                pos_str += f" {i} "
                if i < len(self.list_data) - 1:
                    pos_str += "   "
            print(f"Pos:  {pos_str}")
        
        print("="*60)
    
    def add_loading_effect(self, operation_name):
        """Simulasi loading effect"""
        print(f"\n⏳ Processing {operation_name}...", end="", flush=True)
        for _ in range(3):
            time.sleep(0.1)
            print(".", end="", flush=True)
        print(" Done!")
        time.sleep(0.2)
    
    def insert_at_beginning(self):
        """Insert value di awal list"""
        self.add_loading_effect("Insert at Beginning")
        
        try:
            value = input("Enter value to insert at beginning: ").strip()
            if not value:
                self.show_result("Please enter a value", True)
                return
            
            if len(self.list_data) >= self.max_size:
                self.show_result("List is full!", True)
                return
            
            self.list_data.insert(0, int(value))
            self.display_list_visual()
            self.show_result(f"Inserted {value} at beginning")
            
        except ValueError:
            self.show_result("Please enter a valid number", True)
    
    def insert_at_end(self):
        """Insert value di akhir list"""
        self.add_loading_effect("Insert at End")
        
        try:
            value = input("Enter value to insert at end: ").strip()
            if not value:
                self.show_result("Please enter a value", True)
                return
            
            if len(self.list_data) >= self.max_size:
                self.show_result("List is full!", True)
                return
            
            self.list_data.append(int(value))
            self.display_list_visual()
            self.show_result(f"Inserted {value} at end")
            
        except ValueError:
            self.show_result("Please enter a valid number", True)
    
    def insert_at_position(self):
        """Insert value di posisi tertentu"""
        self.add_loading_effect("Insert at Position")
        
        try:
            value = input("Enter value to insert: ").strip()
            position = input("Enter position (0 to {}): ".format(len(self.list_data))).strip()
            
            if not value or not position:
                self.show_result("Please enter both value and position", True)
                return
            
            pos = int(position)
            if pos < 0 or pos > len(self.list_data):
                self.show_result("Position out of bounds", True)
                return
            
            if len(self.list_data) >= self.max_size:
                self.show_result("List is full!", True)
                return
            
            self.list_data.insert(pos, int(value))
            self.display_list_visual()
            self.show_result(f"Inserted {value} at position {pos}")
            
        except ValueError:
            self.show_result("Please enter valid numbers", True)
    
    def delete_at_beginning(self):
        """Delete value di awal list"""
        self.add_loading_effect("Delete at Beginning")
        
        if len(self.list_data) == 0:
            self.show_result("List is empty! Cannot delete", True)
            return
        
        deleted_value = self.list_data.pop(0)
        self.display_list_visual()
        self.show_result(f"Deleted {deleted_value} from beginning")
    
    def delete_at_end(self):
        """Delete value di akhir list"""
        self.add_loading_effect("Delete at End")
        
        if len(self.list_data) == 0:
            self.show_result("List is empty! Cannot delete", True)
            return
        
        deleted_value = self.list_data.pop()
        self.display_list_visual()
        self.show_result(f"Deleted {deleted_value} from end")
    
    def delete_at_position(self):
        """Delete value di posisi tertentu"""
        self.add_loading_effect("Delete at Position")
        
        try:
            position = input("Enter position to delete: ").strip()
            
            if not position:
                self.show_result("Please enter position to delete", True)
                return
            
            pos = int(position)
            if pos < 0 or pos >= len(self.list_data):
                self.show_result("Position out of bounds", True)
                return
            
            deleted_value = self.list_data.pop(pos)
            self.display_list_visual()
            self.show_result(f"Deleted {deleted_value} from position {pos}")
            
        except ValueError:
            self.show_result("Please enter a valid number", True)
    
    def search_value(self):
        """Search value dalam list"""
        self.add_loading_effect("Search Value")
        
        try:
            value = input("Enter value to search: ").strip()
            if not value:
                self.show_result("Please enter value to search", True)
                return
            
            search_val = int(value)
            try:
                index = self.list_data.index(search_val)
                self.show_result(f"Value {value} found at position {index}")
                self.highlight_element(index)
            except ValueError:
                self.show_result(f"Value {value} not found in list", True)
                
        except ValueError:
            self.show_result("Please enter a valid number", True)
    
    def highlight_element(self, index):
        """Highlight element yang ditemukan"""
        print("\n🔍 Highlighting found element:")
        list_str = ""
        for i, value in enumerate(self.list_data):
            if i == index:
                list_str += f">>> [{value}] <<<"  # Highlight
            else:
                list_str += f"[{value}]"
            if i < len(self.list_data) - 1:
                list_str += " → "
        
        print(f"List: {list_str}")
        
        # Animation effect
        print("Found element is blinking...")
        for _ in range(3):
            time.sleep(0.5)
            print("✨", end=" ", flush=True)
        print("\n")
    
    def display_list_contents(self):
        """Display isi list lengkap"""
        self.add_loading_effect("Display List")
        
        if len(self.list_data) == 0:
            self.show_result("List is empty", True)
            return
        
        # Show in different formats
        print("\n📋 List Contents:")
        print(f"   Array format: {self.list_data}")
        print(f"   Arrow format: [{' → '.join(map(str, self.list_data))}]")
        print(f"   Total elements: {len(self.list_data)}")
        
        self.show_result(f"List contents: [{' → '.join(map(str, self.list_data))}]")
    
    def clear_list(self):
        """Clear semua element dari list"""
        self.add_loading_effect("Clear List")
        
        if len(self.list_data) == 0:
            self.show_result("List is already empty", True)
            return
        
        confirm = input("Are you sure you want to clear the entire list? (y/N): ").strip().lower()
        if confirm != 'y' and confirm != 'yes':
            print("Operation cancelled.")
            return
        
        self.list_data = []
        self.display_list_visual()
        self.show_result("List cleared")
    
    def reverse_list(self):
        """Reverse urutan list"""
        self.add_loading_effect("Reverse List")
        
        if len(self.list_data) == 0:
            self.show_result("List is empty! Cannot reverse", True)
            return
        
        original = self.list_data.copy()
        self.list_data.reverse()
        self.display_list_visual()
        self.show_result(f"List reversed: {original} → {self.list_data}")
    
    def show_menu(self):
        """Menampilkan menu operasi"""
        print("\n" + "="*60)
        print("              LINKED LIST OPERATIONS MENU")
        print("="*60)
        print("1. Insert at Beginning")
        print("2. Insert at End")
        print("3. Insert at Position")
        print("4. Delete at Beginning")
        print("5. Delete at End")
        print("6. Delete at Position")
        print("7. Search Value")
        print("8. Display List Contents")
        print("9. Clear List")
        print("10. Reverse List")
        print("11. Show Current List")
        print("12. Exit")
        print("="*60)
    
    def run(self):
        """Main program loop"""
        print("🚀 Welcome to Linked List Operations Console App!")
        print(f"Maximum list capacity: {self.max_size}")
        self.display_list_visual()
        
        while True:
            self.show_menu()
            choice = input("Choose operation (1-12): ").strip()
            
            if choice == '1':
                self.insert_at_beginning()
            elif choice == '2':
                self.insert_at_end()
            elif choice == '3':
                self.insert_at_position()
            elif choice == '4':
                self.delete_at_beginning()
            elif choice == '5':
                self.delete_at_end()
            elif choice == '6':
                self.delete_at_position()
            elif choice == '7':
                self.search_value()
            elif choice == '8':
                self.display_list_contents()
            elif choice == '9':
                self.clear_list()
            elif choice == '10':
                self.reverse_list()
            elif choice == '11':
                self.display_list_visual()
            elif choice == '12':
                print("\n👋 Thank you for using Linked List Operations App!")
                break
            else:
                self.show_result("Invalid choice! Please choose 1-12", True)
            
            input("\nPress Enter to continue...")

# Jalankan program
if __name__ == "__main__":
    # Buat instance dengan kapasitas maksimal 10 (bisa diubah)
    list_app = LinkedListOperations(max_size=10)
    list_app.run()