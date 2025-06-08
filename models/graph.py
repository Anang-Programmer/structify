class GraphOperations:
    def __init__(self):
        self.vertices = set()
        self.edges = {}  # Dictionary of sets untuk adjacency list
        self.positions = {}  # Untuk menyimpan posisi vertex (opsional)
    
    def show_result(self, message, is_error=False):
        """Menampilkan hasil operasi"""
        if is_error:
            print(f"⚠️ ERROR: {message}")
        else:
            print(f"✅ SUCCESS: {message}")
    
    def display_graph(self):
        """Menampilkan graph saat ini"""
        print("\n" + "="*60)
        print("                   CURRENT GRAPH")
        print("="*60)
        
        if not self.vertices:
            print("Graph is empty - no vertices or edges")
        else:
            print("VERTICES:")
            vertices_list = sorted(list(self.vertices))
            print(f"  {vertices_list}")
            
            print("\nEDGES (Adjacency List):")
            for vertex in sorted(self.vertices):
                neighbors = sorted(list(self.edges.get(vertex, set())))
                if neighbors:
                    print(f"  {vertex} → {neighbors}")
                else:
                    print(f"  {vertex} → []")
            
            print(f"\nSTATISTICS:")
            print(f"  Total Vertices: {len(self.vertices)}")
            print(f"  Total Edges: {self.count_edges()}")
        
        print("="*60)
    
    def count_edges(self):
        """Menghitung total edges (undirected graph)"""
        total = 0
        for neighbors in self.edges.values():
            total += len(neighbors)
        return total // 2  # Dibagi 2 karena undirected graph
    
    def add_vertex(self):
        """Menambah vertex baru"""
        vertex = input("Enter vertex name: ").strip().upper()
        
        if not vertex:
            self.show_result("Vertex name is required!", True)
            return
        
        if vertex in self.vertices:
            self.show_result("Vertex already exists!", True)
            return
        
        self.vertices.add(vertex)
        self.edges[vertex] = set()
        self.positions[vertex] = self.generate_position(vertex)
        
        self.show_result(f'Vertex "{vertex}" added successfully!')
        self.display_graph()
    
    def add_edge(self):
        """Menambah edge antara dua vertex"""
        from_vertex = input("Enter 'From' vertex: ").strip().upper()
        to_vertex = input("Enter 'To' vertex: ").strip().upper()
        
        if not from_vertex or not to_vertex:
            self.show_result("Both 'From' and 'To' vertices are required!", True)
            return
        
        if from_vertex not in self.vertices or to_vertex not in self.vertices:
            self.show_result("Both vertices must exist first!", True)
            return
        
        if from_vertex == to_vertex:
            self.show_result("Cannot create self-loop!", True)
            return
        
        if to_vertex in self.edges[from_vertex]:
            self.show_result("Edge already exists!", True)
            return
        
        # Add edge (undirected graph)
        self.edges[from_vertex].add(to_vertex)
        self.edges[to_vertex].add(from_vertex)
        
        self.show_result(f'Edge added between "{from_vertex}" and "{to_vertex}"!')
        self.display_graph()
    
    def remove_vertex(self):
        """Menghapus vertex dan semua edge yang terhubung"""
        vertex = input("Enter vertex to remove: ").strip().upper()
        
        if vertex not in self.vertices:
            self.show_result("Vertex doesn't exist!", True)
            return
        
        # Remove all edges connected to this vertex
        for neighbors in self.edges.values():
            neighbors.discard(vertex)
        
        # Remove vertex
        del self.edges[vertex]
        self.vertices.remove(vertex)
        if vertex in self.positions:
            del self.positions[vertex]
        
        self.show_result(f'Vertex "{vertex}" and all its connections removed!')
        self.display_graph()
    
    def remove_edge(self):
        """Menghapus edge antara dua vertex"""
        from_vertex = input("Enter 'From' vertex: ").strip().upper()
        to_vertex = input("Enter 'To' vertex: ").strip().upper()
        
        if not from_vertex or not to_vertex:
            self.show_result("Both 'From' and 'To' vertices are required!", True)
            return
        
        if from_vertex not in self.vertices or to_vertex not in self.vertices:
            self.show_result("Both vertices must exist!", True)
            return
        
        if to_vertex not in self.edges[from_vertex]:
            self.show_result("Edge doesn't exist!", True)
            return
        
        # Remove edge (undirected graph)
        self.edges[from_vertex].remove(to_vertex)
        self.edges[to_vertex].remove(from_vertex)
        
        self.show_result(f'Edge between "{from_vertex}" and "{to_vertex}" removed!')
        self.display_graph()
    
    def clear_graph(self):
        """Menghapus seluruh graph"""
        if not self.vertices:
            self.show_result("Graph is already empty!", True)
            return
        
        confirm = input("🗑️ Are you sure you want to clear the entire graph? (y/N): ").strip().lower()
        if confirm != 'y' and confirm != 'yes':
            print("Operation cancelled.")
            return
        
        self.vertices.clear()
        self.edges.clear()
        self.positions.clear()
        
        self.show_result("Graph cleared successfully!")
        self.display_graph()
    
    def generate_position(self, vertex):
        """Generate posisi untuk vertex (placeholder)"""
        # Ini bisa dikembangkan untuk visualisasi yang lebih kompleks
        return {"x": hash(vertex) % 100, "y": hash(vertex) % 50}
    
    def show_adjacency_matrix(self):
        """Menampilkan adjacency matrix"""
        if not self.vertices:
            self.show_result("Graph is empty!", True)
            return
        
        vertices_list = sorted(list(self.vertices))
        n = len(vertices_list)
        
        print("\n" + "="*60)
        print("                ADJACENCY MATRIX")
        print("="*60)
        
        # Header
        print("    ", end="")
        for v in vertices_list:
            print(f"{v:>3}", end="")
        print()
        
        # Matrix
        for i, v1 in enumerate(vertices_list):
            print(f"{v1:>3} ", end="")
            for j, v2 in enumerate(vertices_list):
                if v2 in self.edges[v1]:
                    print("  1", end="")
                else:
                    print("  0", end="")
            print()
        print("="*60)
    
    def find_path_bfs(self, start, end):
        """Mencari path menggunakan BFS"""
        if start not in self.vertices or end not in self.vertices:
            self.show_result("Both vertices must exist!", True)
            return
        
        if start == end:
            print(f"Path from {start} to {end}: [{start}]")
            return
        
        from collections import deque
        
        queue = deque([(start, [start])])
        visited = set([start])
        
        while queue:
            current, path = queue.popleft()
            
            for neighbor in self.edges[current]:
                if neighbor == end:
                    final_path = path + [neighbor]
                    print(f"✅ Path found from {start} to {end}: {' → '.join(final_path)}")
                    return
                
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))
        
        print(f"❌ No path found from {start} to {end}")
    
    def show_menu(self):
        """Menampilkan menu operasi"""
        print("\n" + "="*60)
        print("                GRAPH OPERATIONS MENU")
        print("="*60)
        print("1. Add Vertex")
        print("2. Add Edge")
        print("3. Remove Vertex")  
        print("4. Remove Edge")
        print("5. Clear Graph")
        print("6. Display Graph")
        print("7. Show Adjacency Matrix")
        print("8. Find Path (BFS)")
        print("9. Exit")
        print("="*60)
    
    def run(self):
        """Main program loop"""
        print("🚀 Welcome to Graph Operations Console App!")
        print("This is an undirected graph implementation.")
        self.display_graph()
        
        while True:
            self.show_menu()
            choice = input("Choose operation (1-9): ").strip()
            
            if choice == '1':
                self.add_vertex()
            elif choice == '2':
                self.add_edge()
            elif choice == '3':
                self.remove_vertex()
            elif choice == '4':
                self.remove_edge()
            elif choice == '5':
                self.clear_graph()
            elif choice == '6':
                self.display_graph()
            elif choice == '7':
                self.show_adjacency_matrix()
            elif choice == '8':
                start = input("Enter start vertex: ").strip().upper()
                end = input("Enter end vertex: ").strip().upper()
                self.find_path_bfs(start, end)
            elif choice == '9':
                print("\n👋 Thank you for using Graph Operations App!")
                break
            else:
                self.show_result("Invalid choice! Please choose 1-9", True)
            
            input("\nPress Enter to continue...")

# Jalankan program
if __name__ == "__main__":
    graph_app = GraphOperations()
    graph_app.run()