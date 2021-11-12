# This is a sample Python script.
import numpy as np


dim = 100


def initiate_implementation():
    print("It is happening!")


def lagrangian_relaxation():
    def get_ub_NNH() -> float:
        pass

    def get_ub_custom() -> float:
        pass

    def lagrangian(multipliers) -> float:
        pass

    def get_subgradient() -> float:
        pass

    def get_l(u) -> float:
        return lagrangian(u) + alpha * (ub - lagrangian(u))

    # initialize the params
    u, delta, rho, alpha, eeta = np.zeros([dim, ]), 2, .95, 1/3, dim/2
    # get the ub using Nearest neighbor heuristic
    ub = get_ub_NNH()
    # initialize the L-bar var
    l = get_l(u)

    for k in range(1000):
        gamma = get_subgradient()
        if gamma**2 == 0:
            return
        if gamma**2 < eeta:
            ub = get_ub_custom()

        l = get_l(u)
        if l > ub:
            l = ub

        lambda_k = get_step_size()


if __name__ == '__main__':
    initiate_implementation()
    lagrangian_relaxation()