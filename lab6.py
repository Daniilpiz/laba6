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

def main():
    G1 = generator_smezh(3)#int(input("Введите размер первой матрицы:\n")))
    G2 = generator_smezh(4)#int(input("Введите размер второй матрицы:\n")))
    G1 = cl.MatrixGraph(matrix=G1)
    G2 = cl.MatrixGraph(matrix=G2)
#для 1 матрицы


    G1.display()

    v1_1 = int(input("введите первую вершину для слияния:"))
    v1_2 = int(input("введите вторую вершину для слияния:"))



    G1.identify_vertices(v1_1, v1_2 )

    print()
    v1_3 = int(input("введите вершину для разрыва:"))
    G1.split_vertex( v1_3)
   
    print(G1)


    G1.contract_edge()
#для 2 матрицы
    G2.display()

    v2_1 = int(input("введите первую вершину для слияния:"))
    v2_2 = int(input("введите вторую вершину для слияния:"))
    G2.identify_vertices_edge(v2_1, v2_2)
    print(G2.get_matrix())

    print(G2.get_matrix())

    v2_3 = int(input("введите вершину для разрыва:"))
    G1.split_vertex(v2_3)

    print(G2.get_matrix())

if __name__ == "__main__":
    main()