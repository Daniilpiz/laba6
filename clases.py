
class MatrixGraph:
    def __init__(self, matrix):
        self.matrix = matrix
        self.size = len(matrix)

    def get_matrix(self):
        return self.matrix
    
    def __str__(self):
        return "\n".join(" ".join(map(str, row)) for row in self.matrix)

    def display(self, return_string=False):
        output = "Матрица смежности:\n"
        for row in self.matrix:
            output += " ".join(map(str, row)) + "\n"
    
        if return_string:
            return output
        else:
            print(output)
            return None

    def get_matrix(self):
        return self.matrix

    
    def identify_vertices(self, v1, v2):
        """Отождествление вершин v1 и v2"""
        if v1 == v2 or v1 >= self.size or v2 >= self.size:
            print("Ошибка: неверные номера вершин")
            return None
        
        # Создаем новую матрицу без вершины v2
        new_size = self.size - 1
        new_matrix = [[0] * new_size for _ in range(new_size)]
        
        # Копируем данные, пропуская строку и столбец v2
        new_i, new_j = 0, 0
        for i in range(self.size):
            if i == v2:
                continue
            new_j = 0
            for j in range(self.size):
                if j == v2:
                    continue
                
                if i == v1 or j == v1:
                    # Объединяем связи вершин v1 и v2
                    value = self.matrix[i][j] or self.matrix[i if i != v1 else v2][j if j != v1 else v2]
                else:
                    value = self.matrix[i][j]
                
                new_matrix[new_i][new_j] = value
                new_j += 1
            new_i += 1
        
        return MatrixGraph(new_matrix)
    
    def contract_edge(self, v1, v2):
        """Стягивание ребра между v1 и v2"""
        if v1 == v2 or v1 >= self.size or v2 >= self.size or self.matrix[v1][v2] == 0:
            print("Ошибка: между вершинами нет ребра или неверные номера")
            return None
        
        # Создаем новую матрицу без вершины v2
        new_size = self.size - 1
        new_matrix = [[0] * new_size for _ in range(new_size)]
        
        # Копируем данные, объединяя вершины v1 и v2
        new_i, new_j = 0, 0
        for i in range(self.size):
            if i == v2:
                continue
            new_j = 0
            for j in range(self.size):
                if j == v2:
                    continue
                
                if i == v1 or j == v1:
                    # Объединяем связи вершин v1 и v2
                    value = self.matrix[i][j] or self.matrix[i if i != v1 else v2][j if j != v1 else v2]
                else:
                    value = self.matrix[i][j]
                
                new_matrix[new_i][new_j] = value
                new_j += 1
            new_i += 1
        
        return MatrixGraph(new_matrix)
    
    def split_vertex(self, v):
        """Расщепление вершины v"""
        if v >= self.size:
            print("Ошибка: неверный номер вершины")
            return None
        
        # Создаем новую матрицу с дополнительной вершиной
        new_size = self.size + 1
        new_matrix = [[0] * new_size for _ in range(new_size)]
        
        # Копируем существующую матрицу
        for i in range(self.size):
            for j in range(self.size):
                new_matrix[i][j] = self.matrix[i][j]
        
        # Новая вершина будет иметь индекс self.size
        new_vertex = self.size
        
        # Связываем новую вершину с исходной
        new_matrix[v][new_vertex] = 1
        new_matrix[new_vertex][v] = 1
        
        # Часть связей переносим на новую вершину
        # В данном примере переносим половину связей
        connections = []
        for i in range(self.size):
            if self.matrix[v][i] == 1 and i != v:
                connections.append(i)
        
        # Переносим часть связей на новую вершину
        for i in range(len(connections) // 2):
            neighbor = connections[i]
            new_matrix[new_vertex][neighbor] = 1
            new_matrix[neighbor][new_vertex] = 1
            # Убираем связь у исходной вершины
            new_matrix[v][neighbor] = 0
            new_matrix[neighbor][v] = 0
        
        return MatrixGraph(new_matrix)