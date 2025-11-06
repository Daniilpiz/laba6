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


def vvod():
    try:
        var = int(input("Выберите матричное представление графа(ввод 1) или списковое(ввод 2)"))
        return var
    except: print("Введите число")

def matrix_to_adj_list(matrix):
    """Функциональный стиль преобразования"""
    return [
        [j for j in range(len(matrix)) if matrix[i][j] != 0]
        for i in range(len(matrix))
    ]

def matrix(G1, G2):
   
    G1 = cl.MatrixGraph(matrix=G1)
    G2 = cl.MatrixGraph(matrix=G2)

    G1_2 = G1
    G2_2 = G2



#для 1 матрицы
    print(f"{G1}\n")
    print(f"{G2}\n")

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



    G = G1_2.cartesian_product(G2_2)
    print(f"декартово произведение графов:\n{G}\n\n")

    print(f"{G1}\n\n{G2}\n")
    print(f"{G1_2}\n\n{G2_2}\n")


def matrix_1(G3, G4):
    G3 = cl.MatrixGraph(G3)
    G4 = cl.MatrixGraph(G4)

    print(f"{G3}\n\n{G4}")
    
    var = int(input("Выберите объединение графов(1), пересечение графов(2), кольцевая сумма(3)"))
    


    if var ==1:
        G3 = G3.union(G4)
        print(f"{G3}")
    if var ==2:
        G3 = G3.intersection(G4)
        print(f"{G3}")
    if var == 3:
        G3 = G3.ring_sum(G3)
        print(f"{G3}")

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
    G1 = generator_smezh(int(input("Введите кол-во вершин первого графа:\n")))
    G2 = generator_smezh(int(input("Введите кол-во вершин второго графа:\n")))

    adj_list1 = matrix_to_adj_list(G1)
    adj_list2 = matrix_to_adj_list(G2)

    G3 = generator_smezh(int(input("Введите кол-во вершин третьего графа:\n")))
    G4 = generator_smezh(int(input("Введите кол-во вершин четвёртого графа:\n")))
    
    var = vvod()


    if var == 1:
        # matrix(G1, G2)
        matrix_1(G3, G4)
    if var == 2: 
        lists(adj_list1)
        lists(adj_list2)