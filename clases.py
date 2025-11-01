
class MatrixGraph:
    def __init__(self, matrix):
        self.matrix = matrix
        self.size = len(matrix)

    def cartesian_product(self, other):
        """
        Строит декартово произведение текущего графа (self) и графа other.
        
        Параметры:
            other (MatrixGraph): второй граф для произведения
        
        Возвращает:
            MatrixGraph: новый граф — декартово произведение
        """
        A = self.matrix
        B = other.matrix
        n = self.size      # Размер первого графа
        m = other.size     # Размер второго графа


        # Размер результирующей матрицы: n*m × n*m
        result_size = n * m
        result = [[0] * result_size for _ in range(result_size)]


        # Проходим по всем вершинам произведения (i, j)
        for i in range(n):
            for j in range(m):
                # Глобальный индекс вершины (i, j) в новой матрице
                idx1 = i * m + j


                # Рёбра по первому графу: (i,j) ↔ (k,j) если A[i][k] == 1
                for k in range(n):
                    if A[i][k]:
                        idx2 = k * m + j
                        result[idx1][idx2] = 1
                        result[idx2][idx1] = 1  # Симметрия для неориентированного графа


                # Рёбра по второму графу: (i,j) ↔ (i,l) если B[j][l] == 1
                for l in range(m):
                    if B[j][l]:
                        idx2 = i * m + l
                        result[idx1][idx2] = 1
                        result[idx2][idx1] = 1  # Симметрия


        return MatrixGraph(result)
    
    def __str__(self):
        return "\n".join(" ".join(map(str, row)) for row in self.matrix)
    
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
        if v1 == v2 or v1 >= self.size or v2 >= self.size:
            print("Ошибка: неверные номера вершин")
            return None
        
        if self.matrix[v1][v2] == 0:
            print("Ошибка: между вершинами нет ребра")
            return None
        
        # Создаем новую матрицу без вершины v2
        new_size = self.size - 1
        new_matrix = [[0] * new_size for _ in range(new_size)]
        
        # Индексы для новой матрицы
        new_i = 0
        for i in range(self.size):
            if i == v2:  # Пропускаем вершину v2
                continue
                
            new_j = 0
            for j in range(self.size):
                if j == v2:  # Пропускаем вершину v2
                    continue
                
                # Определяем индексы в новом графе
                current_i = new_i
                current_j = new_j
                
                # Если это объединяемая вершина v1 в новой матрице
                if i == v1:
                    # Объединяем связи: берем ИЛИ связей v1 и v2
                    value = self.matrix[v1][j] or self.matrix[v2][j]
                elif j == v1:
                    # Объединяем связи: берем ИЛИ связей i с v1 и i с v2
                    value = self.matrix[i][v1] or self.matrix[i][v2]
                else:
                    # Просто копируем значение
                    value = self.matrix[i][j]
                
                # Убираем петлю (связь вершины с самой собой)
                if current_i == current_j:
                    value = 0
                
                new_matrix[new_i][new_j] = value
                new_j += 1
                
            new_i += 1
        
        return MatrixGraph(new_matrix)
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
    
    def union(self, other):
        """
        Объединение графов G1 ∪ G2
        Вершины нумеруются последовательно, сохраняются все ребра из обоих графов
        """
        if not isinstance(other, MatrixGraph):
            raise ValueError("Можно объединять только с MatrixGraph")
        
        new_size = self.size + other.size
        new_matrix = [[0] * new_size for _ in range(new_size)]
        
        # Копируем первый граф в левый верхний угол
        for i in range(self.size):
            for j in range(self.size):
                new_matrix[i][j] = self.matrix[i][j]
        
        # Копируем второй граф в правый нижний угол со смещением
        for i in range(other.size):
            for j in range(other.size):
                new_matrix[self.size + i][self.size + j] = other.matrix[i][j]
        
        return MatrixGraph(new_matrix)
    


    def intersection(self, other):
        """
        Пересечение графов G1 ∩ G2
        Только общие ребра, которые есть в обоих графах
        Графы должны быть одинакового размера
        """
        if not isinstance(other, MatrixGraph):
            raise ValueError("Можно пересекать только с MatrixGraph")
        
        if self.size != other.size:
            raise ValueError("Графы должны быть одинакового размера для пересечения")
        
        new_matrix = [[0] * self.size for _ in range(self.size)]
        
        for i in range(self.size):
            for j in range(self.size):
                # Ребро есть только если оно есть в обоих графах
                new_matrix[i][j] = 1 if self.matrix[i][j] == 1 and other.matrix[i][j] == 1 else 0
        
        return MatrixGraph(new_matrix)
    

    def ring_sum(self, other):
        """
        Кольцевая сумма G1 ⊕ G2
        Объединение графов без общих ребер (исключающее ИЛИ)
        """
        if not isinstance(other, MatrixGraph):
            raise ValueError("Можно выполнять кольцевую сумму только с MatrixGraph")
        
        if self.size != other.size:
            raise ValueError("Графы должны быть одинакового размера для кольцевой суммы")
        
        new_matrix = [[0] * self.size for _ in range(self.size)]
        
        for i in range(self.size):
            for j in range(self.size):
                # Ребро есть если оно есть только в одном из графов (XOR)
                new_matrix[i][j] = 1 if self.matrix[i][j] != other.matrix[i][j] else 0
        
        return MatrixGraph(new_matrix)
    




class AdjacencyGraph:
    def __init__(self, adj_list):
        self.adj_list = adj_list
        self.size = len(adj_list)

    def __str__(self):
        """Строковое представление графа в виде списков смежности"""
        result = "Граф (списки смежности):\n"
        for i, neighbors in enumerate(self.adj_list):
            result += f"Вершина {i}: {neighbors}\n"
        return result
    
    def identify_vertices(self, v1, v2):
        """Отождествление вершин v1 и v2"""
        if v1 == v2 or v1 >= self.size or v2 >= self.size:
            print("Ошибка: неверные номера вершин")
            return None
        
        new_adj_list = []
        
        for i in range(self.size):
            if i == v2:
                continue
                
            neighbors = []
            for neighbor in self.adj_list[i]:
                if neighbor == v2:
                    neighbors.append(v1)
                elif neighbor > v2:
                    neighbors.append(neighbor - 1)
                else:
                    neighbors.append(neighbor)
            
            # Убираем дубликаты и сортируем
            neighbors = sorted(list(set(neighbors)))
            new_adj_list.append(neighbors)
        
        # Объединяем списки смежности для v1
        v1_neighbors = set(new_adj_list[v1])
        for neighbor in self.adj_list[v2]:
            if neighbor != v2:
                adjusted_neighbor = neighbor if neighbor < v2 else neighbor - 1
                if adjusted_neighbor != v1:
                    v1_neighbors.add(adjusted_neighbor)
        
        new_adj_list[v1] = sorted(list(v1_neighbors))
        
        return AdjacencyGraph(new_adj_list)
    
    # def contract_edge(self, v1, v2):
    #     """Стягивание ребра между v1 и v2"""
    #     if v1 == v2 or v1 >= self.size or v2 >= self.size or v2 not in self.adj_list[v1]:
    #         print("Ошибка: между вершинами нет ребра или неверные номера")
    #         return None
        
    #     new_adj_list = []
        
    #     for i in range(self.size):
    #         if i == v2:
    #             continue
                
    #         neighbors = []
    #         for neighbor in self.adj_list[i]:
    #             if neighbor == v2:
    #                 neighbors.append(v1)
    #             elif neighbor > v2:
    #                 neighbors.append(neighbor - 1)
    #             else:
    #                 neighbors.append(neighbor)
            
    #         # Убираем дубликаты и сортируем
    #         neighbors = sorted(list(set(neighbors)))
    #         new_adj_list.append(neighbors)
        
    #     # Объединяем списки смежности для v1
    #     v1_neighbors = set(new_adj_list[v1])
    #     for neighbor in self.adj_list[v2]:
    #         if neighbor != v2 and neighbor != v1:
    #             adjusted_neighbor = neighbor if neighbor < v2 else neighbor - 1
    #             v1_neighbors.add(adjusted_neighbor)
        
    #     new_adj_list[v1] = sorted(list(v1_neighbors))
        
    #     return AdjacencyGraph(new_adj_list)


    # 
    

    def contract_edge(self, v1, v2):
        """Стягивание ребра между v1 и v2"""
        if v1 == v2 or v1 >= self.size or v2 >= self.size:
            print("Ошибка: неверные номера вершин")
            return None
        
        if v2 not in self.adj_list[v1]:
            print("Ошибка: между вершинами нет ребра")
            return None
        
        # Создаем копию для безопасной модификации
        temp_graph = self.copy()
        
        # Определяем, какую вершину сохраняем (v1), какую удаляем (v2)
        keep_vertex = min(v1, v2)
        remove_vertex = max(v1, v2)
        
        new_adj_list = []
        
        # Строим новый список смежности
        for i in range(temp_graph.size):
            if i == remove_vertex:  # Пропускаем удаляемую вершину
                continue
                
            new_neighbors = []
            for neighbor in temp_graph.adj_list[i]:
                if neighbor == remove_vertex:
                    # Заменяем ссылку на удаляемую вершину ссылкой на сохраняемую
                    if keep_vertex not in new_neighbors and keep_vertex != i:
                        new_neighbors.append(keep_vertex)
                elif neighbor > remove_vertex:
                    # Корректируем индексы вершин, которые были после удаляемой
                    new_neighbors.append(neighbor - 1)
                else:
                    # Сохраняем без изменений
                    new_neighbors.append(neighbor)
            
            new_adj_list.append(sorted(list(set(new_neighbors))))  # Убираем дубликаты и сортируем
        
        # Объединяем списки смежности для сохраняемой вершины
        # Добавляем всех соседей удаляемой вершины (кроме самой себя и сохраняемой)
        keep_index = keep_vertex if keep_vertex < remove_vertex else keep_vertex - 1
        
        additional_neighbors = []
        for neighbor in temp_graph.adj_list[remove_vertex]:
            if neighbor != remove_vertex and neighbor != keep_vertex:
                if neighbor > remove_vertex:
                    adjusted_neighbor = neighbor - 1
                else:
                    adjusted_neighbor = neighbor
                if adjusted_neighbor not in new_adj_list[keep_index]:
                    additional_neighbors.append(adjusted_neighbor)
        
        # Объединяем и убираем дубликаты
        if additional_neighbors:
            new_adj_list[keep_index] = sorted(list(set(new_adj_list[keep_index] + additional_neighbors)))
        
        return AdjacencyGraph(new_adj_list)



    
    def split_vertex(self, v):
        """Расщепление вершины v"""
        if v >= self.size:
            print("Ошибка: неверный номер вершины")
            return None
        
        new_adj_list = [neighbors.copy() for neighbors in self.adj_list]
        
        # Добавляем новую вершину
        new_vertex = self.size
        new_adj_list.append([])
        
        # Связываем новую вершину с исходной
        new_adj_list[v].append(new_vertex)
        new_adj_list[new_vertex].append(v)
        
        # Переносим часть связей на новую вершину
        connections_to_move = self.adj_list[v][:len(self.adj_list[v]) // 2]
        
        for neighbor in connections_to_move:
            if neighbor != v:
                # Убираем связь у исходной вершины
                if neighbor in new_adj_list[v]:
                    new_adj_list[v].remove(neighbor)
                if v in new_adj_list[neighbor]:
                    new_adj_list[neighbor].remove(v)
                
                # Добавляем связь к новой вершине
                new_adj_list[new_vertex].append(neighbor)
                new_adj_list[neighbor].append(new_vertex)
        
        # Сортируем все списки
        for i in range(len(new_adj_list)):
            new_adj_list[i] = sorted(new_adj_list[i])
        
        return AdjacencyGraph(new_adj_list)