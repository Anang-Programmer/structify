import time
from datetime import datetime

class RecordManager:
    def __init__(self):
        self.record_data = {}
    
    def add_field(self):
        """Menambahkan field baru ke record"""
        try:
            field_name = input("Masukkan nama field: ").strip()
            field_value = input("Masukkan nilai field: ").strip()
            
            if field_name == '' or field_value == '':
                self.show_result('Silakan masukkan nama field dan nilai', is_error=True)
                return
            
            if field_name in self.record_data:
                self.show_result(f"Field '{field_name}' sudah ada. Gunakan update untuk mengubah.", is_error=True)
                return
            
            # Pilih tipe data
            print("\nTipe data yang tersedia:")
            print("1. String (text)")
            print("2. Number (angka)")
            print("3. Boolean (true/false)")
            print("4. Date (tanggal)")
            
            field_type_choice = input("Pilih tipe data (1-4): ").strip()
            
            # Mapping pilihan ke tipe
            type_mapping = {
                '1': 'string',
                '2': 'number', 
                '3': 'boolean',
                '4': 'date'
            }
            
            if field_type_choice not in type_mapping:
                self.show_result('Pilihan tipe data tidak valid', is_error=True)
                return
                
            field_type = type_mapping[field_type_choice]
            
            # Konversi nilai berdasarkan tipe
            converted_value = self.convert_value(field_value, field_type)
            if converted_value is None:
                return  # Error sudah ditangani di convert_value
            
            self.record_data[field_name] = {
                'value': converted_value,
                'type': field_type
            }
            
            self.update_display()
            self.show_result(f"Berhasil menambahkan field '{field_name}' dengan nilai '{converted_value}'")
            
        except Exception as e:
            self.show_result(f'Terjadi error: {e}', is_error=True)
    
    def convert_value(self, field_value, field_type):
        """Mengkonversi nilai berdasarkan tipe data"""
        try:
            if field_type == 'number':
                converted_value = float(field_value)
                if str(converted_value).endswith('.0'):
                    converted_value = int(converted_value)
                return converted_value
                
            elif field_type == 'boolean':
                return field_value.lower() == 'true'
                
            elif field_type == 'date':
                try:
                    # Coba parse berbagai format tanggal
                    date_obj = datetime.strptime(field_value, '%Y-%m-%d')
                    return date_obj.strftime('%Y-%m-%d')
                except ValueError:
                    try:
                        date_obj = datetime.strptime(field_value, '%d/%m/%Y')
                        return date_obj.strftime('%Y-%m-%d')
                    except ValueError:
                        try:
                            date_obj = datetime.strptime(field_value, '%d-%m-%Y')
                            return date_obj.strftime('%Y-%m-%d')
                        except ValueError:
                            self.show_result('Format tanggal tidak valid. Gunakan: YYYY-MM-DD, DD/MM/YYYY, atau DD-MM-YYYY', is_error=True)
                            return None
                            
            else:  # string
                return field_value
                
        except ValueError:
            if field_type == 'number':
                self.show_result('Nilai angka tidak valid', is_error=True)
            else:
                self.show_result(f'Nilai tidak valid untuk tipe {field_type}', is_error=True)
            return None
    
    def delete_field(self):
        """Menghapus field dari record"""
        if not self.record_data:
            self.show_result('Record kosong, tidak ada field untuk dihapus', is_error=True)
            return
        
        print("\nField yang tersedia:")
        for i, field_name in enumerate(self.record_data.keys(), 1):
            field_info = self.record_data[field_name]
            print(f"{i}. {field_name} ({field_info['type']}) = {field_info['value']}")
        
        try:
            choice = input("\nMasukkan nama field yang ingin dihapus: ").strip()
            
            if choice in self.record_data:
                deleted_value = self.record_data[choice]['value']
                del self.record_data[choice]
                self.update_display()
                self.show_result(f"Berhasil menghapus field '{choice}' dengan nilai '{deleted_value}'")
            else:
                self.show_result(f"Field '{choice}' tidak ditemukan", is_error=True)
                
        except Exception as e:
            self.show_result(f'Terjadi error: {e}', is_error=True)
    
    def update_field(self):
        """Mengupdate field yang sudah ada"""
        if not self.record_data:
            self.show_result('Record kosong, tidak ada field untuk diupdate', is_error=True)
            return
        
        print("\nField yang tersedia:")
        for i, field_name in enumerate(self.record_data.keys(), 1):
            field_info = self.record_data[field_name]
            print(f"{i}. {field_name} ({field_info['type']}) = {field_info['value']}")
        
        try:
            field_name = input("\nMasukkan nama field yang ingin diupdate: ").strip()
            
            if field_name not in self.record_data:
                self.show_result(f"Field '{field_name}' tidak ditemukan", is_error=True)
                return
            
            current_type = self.record_data[field_name]['type']
            current_value = self.record_data[field_name]['value']
            
            print(f"Field '{field_name}' saat ini: {current_value} (tipe: {current_type})")
            new_value = input("Masukkan nilai baru: ").strip()
            
            if new_value == '':
                self.show_result('Nilai tidak boleh kosong', is_error=True)
                return
            
            # Konversi dengan tipe yang sama
            converted_value = self.convert_value(new_value, current_type)
            if converted_value is None:
                return
            
            old_value = self.record_data[field_name]['value']
            self.record_data[field_name]['value'] = converted_value
            
            self.update_display()
            self.show_result(f"Berhasil mengupdate field '{field_name}' dari '{old_value}' ke '{converted_value}'")
            
        except Exception as e:
            self.show_result(f'Terjadi error: {e}', is_error=True)
    
    def clear_record(self):
        """Mengosongkan semua record"""
        if len(self.record_data) == 0:
            self.show_result('Record sudah kosong', is_error=True)
            return
        
        confirm = input("Yakin ingin menghapus semua record? (y/n): ").strip().lower()
        if confirm == 'y' or confirm == 'yes':
            self.record_data = {}
            self.update_display()
            self.show_result('Record berhasil dikosongkan')
        else:
            self.show_result('Pembersihan record dibatalkan')
    
    def search_field(self):
        """Mencari field berdasarkan nama atau nilai"""
        if not self.record_data:
            self.show_result('Record kosong', is_error=True)
            return
        
        search_term = input("Masukkan kata kunci pencarian: ").strip().lower()
        
        found_fields = []
        for field_name, field_info in self.record_data.items():
            if (search_term in field_name.lower() or 
                search_term in str(field_info['value']).lower()):
                found_fields.append((field_name, field_info))
        
        if found_fields:
            print(f"\n🔍 Ditemukan {len(found_fields)} field:")
            print("-" * 50)
            for field_name, field_info in found_fields:
                print(f"• {field_name} ({field_info['type']}) = {field_info['value']}")
        else:
            self.show_result('Tidak ada field yang ditemukan', is_error=True)
    
    def update_display(self):
        """Menampilkan status record saat ini"""
        print(f"\n{'='*60}")
        print(f"                    RECORD STATUS")
        print(f"{'='*60}")
        
        if not self.record_data:
            print("Record kosong")
        else:
            print(f"Total fields: {len(self.record_data)}")
            print("-" * 60)
            
            for field_name, field_info in self.record_data.items():
                type_icon = {
                    'string': '📝',
                    'number': '🔢', 
                    'boolean': '✅',
                    'date': '📅'
                }.get(field_info['type'], '❓')
                
                print(f"{type_icon} {field_name:<20} ({field_info['type']:<8}) = {field_info['value']}")
        
        print(f"{'='*60}")
    
    def show_result(self, message, is_error=False):
        """Menampilkan pesan hasil operasi"""
        if is_error:
            print(f"❌ ERROR: {message}")
        else:
            print(f"✅ {message}")
    
    def show_menu(self):
        """Menampilkan menu pilihan"""
        print("\n" + "="*60)
        print("              RECORD MANAGEMENT SYSTEM")
        print("="*60)
        print("1. Add Field (Tambah field baru)")
        print("2. Update Field (Update field yang ada)")
        print("3. Delete Field (Hapus field)")
        print("4. Search Field (Cari field)")
        print("5. Clear Record (Kosongkan semua record)")
        print("6. Display Record (Tampilkan record)")
        print("7. Export Record (Export ke file)")
        print("8. Import Record (Import dari file)")
        print("0. Exit")
        print("="*60)
    
    def export_record(self):
        """Export record ke file"""
        if not self.record_data:
            self.show_result('Record kosong, tidak ada yang di-export', is_error=True)
            return
        
        try:
            filename = input("Masukkan nama file (tanpa ekstensi): ").strip()
            if not filename:
                filename = f"record_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
            
            filename += ".txt"
            
            with open(filename, 'w', encoding='utf-8') as f:
                f.write("RECORD DATA EXPORT\n")
                f.write("=" * 50 + "\n")
                f.write(f"Export Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f"Total Fields: {len(self.record_data)}\n\n")
                
                for field_name, field_info in self.record_data.items():
                    f.write(f"Field: {field_name}\n")
                    f.write(f"Type: {field_info['type']}\n")
                    f.write(f"Value: {field_info['value']}\n")
                    f.write("-" * 30 + "\n")
            
            self.show_result(f"Record berhasil di-export ke '{filename}'")
            
        except Exception as e:
            self.show_result(f'Error saat export: {e}', is_error=True)
    
    def import_record(self):
        """Import record dari file (format sederhana)"""
        try:
            filename = input("Masukkan nama file untuk import: ").strip()
            
            # Contoh format import sederhana
            print("\nContoh format file import:")
            print("nama_field1:string:nilai1")
            print("nama_field2:number:123")
            print("nama_field3:boolean:true")
            print("nama_field4:date:2024-01-01")
            
            confirm = input("\nFile sudah dalam format yang benar? (y/n): ").strip().lower()
            if confirm != 'y' and confirm != 'yes':
                return
            
            with open(filename, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            imported_count = 0
            for line in lines:
                line = line.strip()
                if ':' in line and not line.startswith('#'):
                    parts = line.split(':', 2)
                    if len(parts) == 3:
                        field_name, field_type, field_value = parts
                        
                        if field_name not in self.record_data:
                            converted_value = self.convert_value(field_value, field_type)
                            if converted_value is not None:
                                self.record_data[field_name] = {
                                    'value': converted_value,
                                    'type': field_type
                                }
                                imported_count += 1
            
            self.update_display()
            self.show_result(f"Berhasil import {imported_count} field dari '{filename}'")
            
        except FileNotFoundError:
            self.show_result(f"File '{filename}' tidak ditemukan", is_error=True)
        except Exception as e:
            self.show_result(f'Error saat import: {e}', is_error=True)
    
    def run(self):
        """Menjalankan program record manager"""
        print("🗂️  Record Management System Python")
        self.update_display()
        
        while True:
            self.show_menu()
            
            try:
                choice = input("\nPilih operasi (0-8): ").strip()
                
                if choice == '1':
                    self.add_field()
                elif choice == '2':
                    self.update_field()
                elif choice == '3':
                    self.delete_field()
                elif choice == '4':
                    self.search_field()
                elif choice == '5':
                    self.clear_record()
                elif choice == '6':
                    self.update_display()
                elif choice == '7':
                    self.export_record()
                elif choice == '8':
                    self.import_record()
                elif choice == '0':
                    print("👋 Terima kasih! Program selesai.")
                    break
                else:
                    print("❌ Pilihan tidak valid! Silakan pilih 0-8.")
                    
            except KeyboardInterrupt:
                print("\n\n👋 Program dihentikan oleh user.")
                break
            except Exception as e:
                print(f"❌ Terjadi error: {e}")

# Cara menjalankan program
if __name__ == "__main__":
    record_manager = RecordManager()
    record_manager.run()
