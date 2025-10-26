import random as rd
import numpy as np

import clases as cl


def generator_smezh(razm):
    matr_sm = np.array([abs(rd.randint(-1000, 1000))%2 for _ in range(razm) for _ in range(razm)]).reshape(razm, razm)

    for i in range(razm):
        # matr_sm[i, i] = 0
        for j in range(razm):
            if i<=j:
                matr_sm[i, j] = matr_sm[j, i]


    return matr_sm.tolist()


def matrix_to_adj_list_functional(matrix):
    """Функциональный стиль преобразования"""
    return [
        [j for j in range(len(matrix)) if matrix[i][j] != 0]
        for i in range(len(matrix))
    ]

def matrix(G1, G2):
   
    G1 = cl.MatrixGraph(matrix=G1)
    G2 = cl.MatrixGraph(matrix=G2)




#для 1 матрицы
    print(f"{G1}\n")

    v1_1 = int(input("введите первую вершину для слияния:"))
    v1_2 = int(input("введите вторую вершину для слияния:"))
    G1 = G1.identify_vertices(v1_1, v1_2)
    print(f"{G1}\n")

    v1_3 = int(input("введите вершину для разрыва:"))
    G1 = G1.split_vertex(v1_3)
    print(f"{G1}\n")
   
    v1_4 = int(input("введите первую вершину для cтягивания ребра:"))
    v1_5 = int(input("введите вторую вершину для стягивания ребра:"))
    G1 = G1.contract_edge(v1_4, v1_5)
    print(f"{G1}\n")
    
    # print(f"{G1}\n")
    
#для 2 матрицы
    print(G2)

    v2_1 = int(input("введите первую вершину для слияния:"))
    v2_2 = int(input("введите вторую вершину для слияния:"))
    G2 = G2.identify_vertices(v2_1, v2_2)
    print(G2)

    v2_3 = int(input("введите вершину для разрыва:"))
    G2 = G2.split_vertex(v2_3)
    print(G2)

    v2_4 = int(input("введите первую вершину для cтягивания ребра:"))
    v2_5 = int(input("введите вторую вершину для стягивания ребра:"))
    G2 = G2.contract_edge(v2_4, v2_5)
    print(G2)

    # print(G2)

def lists(spisok):
    spisok = cl.AdjacencyGraph(spisok)
    print(spisok)



    v1 = int(input("введите первую вершину для слияния:"))
    v2 = int(input("введите вторую вершину для слияния:"))
    spisok = spisok.identify_vertices(v1, v2)
    print(spisok)



    v3 = int(input("Введите вершину для разрыва:"))
    spisok = spisok.split_vertex(v3)
    print(spisok)


    v4 = int(input("Введите первую вершину для стягивания ребра:"))
    v5 = int(input("Введите вторую вершину для стягивания ребра:"))
    spisok = spisok.contract_edge(v4, v5)
    print(spisok)
     
    

if __name__ == "__main__":
    G1 = generator_smezh(3)#int(input("Введите размер первой матрицы:\n")))
    G2 = generator_smezh(4)#int(input("Введите размер второй матрицы:\n")))
    matrix(G1, G2)
    adj_list = matrix_to_adj_list_functional(G1)
    lists(adj_list)