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

def matrix():
    G1 = generator_smezh(3)#int(input("Введите размер первой матрицы:\n")))
    G2 = generator_smezh(4)#int(input("Введите размер второй матрицы:\n")))
    G1 = cl.MatrixGraph(matrix=G1)
    G2 = cl.MatrixGraph(matrix=G2)




#для 1 матрицы
    print(f"{G1}\n")

    v1_1 = int(input("введите первую вершину для слияния:"))
    v1_2 = int(input("введите вторую вершину для слияния:"))
    print(f"{G1.identify_vertices(v1_1, v1_2)}\n")

    v1_3 = int(input("введите вершину для разрыва:"))
    print(f"{G1.split_vertex(v1_3)}\n")
   
    v1_4 = int(input("введите первую вершину для cтягивания ребра:"))
    v1_5 = int(input("введите вторую вершину для стягивания ребра:"))
    print(f"{G1.contract_edge(v1_4, v1_5)}\n")
    
    print(f"{G1}\n")
    
#для 2 матрицы
    print(G2)

    v2_1 = int(input("введите первую вершину для слияния:"))
    v2_2 = int(input("введите вторую вершину для слияния:"))
    print(G2.identify_vertices(v2_1, v2_2))

    v2_3 = int(input("введите вершину для разрыва:"))
    print(G2.split_vertex(v2_3))

    v2_4 = int(input("введите первую вершину для cтягивания ребра:"))
    v2_5 = int(input("введите вторую вершину для стягивания ребра:"))
    print(G2.contract_edge(v2_4, v2_5))

    print(G2)

def lists(spisok):
    spisok = cl.AdjacencyGraph(spisok)
    print(spisok)


    
    v1 = int(input("введите первую вершину для слияния:"))
    v2 = int(input("введите вторую вершину для слияния:"))

    
    print(spisok.identify_vertices(v1, v2))



    v3 = int(input("Введите вершину для разрыва:"))

    
    print(spisok.split_vertex(v3))


    v4 = int(input("Введите первую вершину для разрыва:"))
    v5 = int(input("Введите вторую вершину для стягивания ребра:"))

    
    print(spisok.contract_edge(v4, v5))
     
    

if __name__ == "__main__":
    # matrix()
    adj_list = [
        [1, 2],
        [0, 2, 3],
        [0, 1, 3],
        [1, 2]
    ]
    lists(adj_list)