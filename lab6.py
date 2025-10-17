import numpy as np
import random as rd


def generator_smezh(razm):
    matr_sm = np.matrix(np.array([abs(rd.randint(-1000, 1000))%2 for _ in range(razm) for _ in range(razm)]).reshape(razm, razm))

    for i in range(razm):
        # matr_sm[i, i] = 0
        for j in range(razm):
            if i<=j:
                matr_sm[i,j] = matr_sm[j, i]


    return matr_sm



def main():
    G1 = generator_smezh(int(input("Введите размер первой матрицы:\n")))
    G2 = generator_smezh(int(input("Введите размер второй матрицы:\n")))
    print(f"{G1}\n\n")
    print(f"{G2}\n\n")



if __name__ == "__main__":
    main()