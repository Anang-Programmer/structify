class PointerMemoryOperations:
    def __init__(self):
        self.memory = {}
        self.next_address = 1000
        self.selected_address = None
    
    def show_result(self, message, is_error=False):
        """Menampilkan hasil operasi"""
        if is_error:
            print(f"❌ ERROR: {message}")
        else:
            print(f"✅ SUCCESS: {message}")
    
    def display_memory(self):
        """Menampilkan memory layout saat ini"""
        print("\n" + "="*80)
        print("                      MEMORY LAYOUT")
        print("="*80)
        
        if not self.memory:
            print("[ MEMORY IS EMPTY ]")
        else:
            print(f"{'Address':<10} {'Variable':<15} {'Type':<10} {'Value':<15} {'Selected':<10}")
            print("-" * 80)
            
            for address in sorted(self.memory.keys()):
                data = self.memory[address]
                selected_mark = "<<<" if address == self.selected_address else ""
                
                # Format value display
                if data['is_pointer']:
                    if data['value'] in self.memory:
                        target_var = self.memory[data['value']]['variable_name']
                        value_display = f"→ {target_var}({data['value']})"
                    else:
                        value_display = f"→ INVALID({data['value']})"
                else:
                    value_display = str(data['value'])
                
                print(f"{address:<10} {data['variable_name']:<15} {data['type']:<10} {value_display:<15} {selected_mark:<10}")
        
        print("="*80)
        if self.selected_address is not None:
            selected_var = self.memory[self.selected_address]['variable_name']
            print(f"Currently Selected: {selected_var} at address {self.selected_address}")
        print(f"Next Available Address: {self.next_address}")
        print("="*80)
    
    def select_address(self):
        """Select address untuk operasi pointer"""
        if not self.memory:
            self.show_result("Memory is empty! No addresses to select", True)
            return
        
        print("\nAvailable addresses:")
        for address in sorted(self.memory.keys()):
            data = self.memory[address]
            print(f"  {address}: {data['variable_name']} ({data['type']})")
        
        try:
            address_input = input("Enter address to select (or 'none' to deselect): ").strip()
            
            if address_input.lower() == 'none':
                self.selected_address = None
                self.show_result("Address selection cleared")
                return
            
            address = int(address_input)
            if address not in self.memory:
                self.show_result("Invalid address", True)
                return
            
            # Toggle selection
            if self.selected_address == address:
                self.selected_address = None
                self.show_result("Address deselected")
            else:
                self.selected_address = address
                var_name = self.memory[address]['variable_name']
                self.show_result(f"Selected {var_name} at address {address}")
            
            self.display_memory()
            
        except ValueError:
            self.show_result("Please enter a valid address number", True)
    
    def allocate_memory(self):
        """Allocate memory untuk variable baru"""
        value = input("Enter value to allocate: ").strip()
        if not value:
            self.show_result("Please enter a value to allocate memory", True)
            return
        
        var_name = input("Enter variable name (optional): ").strip()
        
        address = self.next_address
        final_var_name = var_name if var_name else f"var_{address}"
        
        # Try to parse as number, otherwise keep as string
        parsed_value = value
        value_type = 'string'
        
        # Check if it's a number
        try:
            if '.' in value:
                parsed_value = float(value)
                value_type = 'float'
            else:
                parsed_value = int(value)
                value_type = 'integer'
        except ValueError:
            # Keep as string
            pass
        
        self.memory[address] = {
            'value': parsed_value,
            'type': value_type,
            'variable_name': final_var_name,
            'is_pointer': False
        }
        
        self.next_address += 1
        self.display_memory()
        self.show_result(f"Allocated memory: {final_var_name} = {parsed_value} at address {address}")
    
    def create_pointer(self):
        """Create pointer ke address yang dipilih"""
        if self.selected_address is None:
            self.show_result("Please select a memory block first", True)
            return
        
        var_name = input("Enter pointer variable name (optional): ").strip()
        final_var_name = var_name if var_name else f"ptr_{self.next_address}"
        
        address = self.next_address
        
        self.memory[address] = {
            'value': self.selected_address,  # Points to selected address
            'type': 'pointer',
            'variable_name': final_var_name,
            'is_pointer': True
        }
        
        self.next_address += 1
        target_var = self.memory[self.selected_address]['variable_name']
        self.display_memory()
        self.show_result(f"🔗 Created pointer: {final_var_name} → {target_var} ({self.selected_address})")
        
        self.selected_address = None  # Clear selection
    
    def dereference_pointer(self):
        """Dereference pointer yang dipilih"""
        if self.selected_address is None:
            self.show_result("Please select a pointer to dereference", True)
            return
        
        selected_data = self.memory[self.selected_address]
        if not selected_data['is_pointer']:
            self.show_result("Selected memory block is not a pointer", True)
            return
        
        target_address = selected_data['value']
        if target_address in self.memory:
            target_value = self.memory[target_address]['value']
            target_var = self.memory[target_address]['variable_name']
            self.show_result(f"🎯 Dereferenced {selected_data['variable_name']}: *{selected_data['variable_name']} = {target_value} (from {target_var})")
            
            # Show dereferencing visualization
            print(f"\nDereferencing Visualization:")
            print(f"  {selected_data['variable_name']} (address {self.selected_address}) contains → {target_address}")
            print(f"  Address {target_address} contains → {target_value}")
            print(f"  Therefore: *{selected_data['variable_name']} = {target_value}")
        else:
            self.show_result("Pointer points to invalid or deallocated address", True)
    
    def deallocate_memory(self):
        """Deallocate memory di address tertentu"""
        if self.selected_address is None:
            self.show_result("Please select a memory block to deallocate", True)
            return
        
        var_name = self.memory[self.selected_address]['variable_name']
        
        # Check if any pointers point to this address
        pointing_pointers = []
        for addr, data in self.memory.items():
            if data['is_pointer'] and data['value'] == self.selected_address:
                pointing_pointers.append((addr, data['variable_name']))
        
        if pointing_pointers:
            print(f"\nWarning: The following pointers will become invalid:")
            for addr, ptr_name in pointing_pointers:
                print(f"  - {ptr_name} (address {addr})")
            
            confirm = input("Continue with deallocation? (y/N): ").strip().lower()
            if confirm != 'y' and confirm != 'yes':
                print("Deallocation cancelled.")
                return
        
        del self.memory[self.selected_address]
        self.show_result(f"🗑️ Deallocated {var_name} from address {self.selected_address}")
        self.selected_address = None
        self.display_memory()
    
    def show_pointer_chain(self):
        """Tampilkan chain of pointers"""
        if not self.memory:
            self.show_result("Memory is empty", True)
            return
        
        print("\n" + "="*60)
        print("                   POINTER CHAINS")
        print("="*60)
        
        # Find all pointer chains
        chains_found = False
        for address, data in self.memory.items():
            if data['is_pointer']:
                chains_found = True
                chain = []
                current_addr = address
                visited = set()
                
                while current_addr is not None and current_addr not in visited:
                    visited.add(current_addr)
                    if current_addr in self.memory:
                        current_data = self.memory[current_addr]
                        chain.append((current_addr, current_data['variable_name'], current_data['value']))
                        
                        if current_data['is_pointer']:
                            current_addr = current_data['value']
                        else:
                            break
                    else:
                        chain.append((current_addr, "INVALID", None))
                        break
                
                # Display chain
                print(f"\nChain starting from {data['variable_name']}:")
                chain_str = ""
                for i, (addr, var_name, value) in enumerate(chain):
                    if i == 0:
                        chain_str += f"{var_name}({addr})"
                    else:
                        chain_str += f" → {var_name}({addr})"
                    
                    if i < len(chain) - 1:
                        chain_str += ""
                    elif not self.memory.get(addr, {}).get('is_pointer', False):
                        chain_str += f" = {value}"
                
                print(f"  {chain_str}")
        
        if not chains_found:
            print("No pointers found in memory")
        
        print("="*60)
    
    def clear_memory(self):
        """Clear semua memory"""
        if not self.memory:
            self.show_result("Memory is already empty", True)
            return
        
        confirm = input("Are you sure you want to clear all memory? This action cannot be undone. (y/N): ").strip().lower()
        if confirm != 'y' and confirm != 'yes':
            print("Operation cancelled.")
            return
        
        self.memory = {}
        self.next_address = 1000
        self.selected_address = None
        self.display_memory()
        self.show_result("🗑️ All memory has been cleared")
    
    def show_menu(self):
        """Menampilkan menu operasi"""
        print("\n" + "="*80)
        print("                   POINTER & MEMORY OPERATIONS MENU")
        print("="*80)
        print("1. Allocate Memory")
        print("2. Select Address")
        print("3. Create Pointer")
        print("4. Dereference Pointer")
        print("5. Deallocate Memory")
        print("6. Show Memory Layout")
        print("7. Show Pointer Chains")
        print("8. Clear All Memory")
        print("9. Exit")
        print("="*80)
    
    def run(self):
        """Main program loop"""
        print("🚀 Welcome to Pointer & Memory Operations Console App!")
        print("This simulator demonstrates memory allocation, pointers, and dereferencing.")
        self.display_memory()
        
        while True:
            self.show_menu()
            choice = input("Choose operation (1-9): ").strip()
            
            if choice == '1':
                self.allocate_memory()
            elif choice == '2':
                self.select_address()
            elif choice == '3':
                self.create_pointer()
            elif choice == '4':
                self.dereference_pointer()
            elif choice == '5':
                self.deallocate_memory()
            elif choice == '6':
                self.display_memory()
            elif choice == '7':
                self.show_pointer_chain()
            elif choice == '8':
                self.clear_memory()
            elif choice == '9':
                print("\n👋 Thank you for using Pointer & Memory Operations App!")
                break
            else:
                self.show_result("Invalid choice! Please choose 1-9", True)
            
            input("\nPress Enter to continue...")

# Jalankan program
if __name__ == "__main__":
    memory_app = PointerMemoryOperations()
    memory_app.run()