from Matrix import *
from Vector import *

def is_diagonally_dominant(matrix):
    condition_2 = False

    for i in range(matrix.rows):
        sum = 0
        for j in range(matrix.cols):
            if(i != j): sum += abs(matrix.value[i][j])
        if(abs(matrix.value[i][i]) >= sum):
            if(abs(matrix.values[i][i]) > sum): condition_2 = True
        else: return False
    
    return (condition_2)
           
def gauss_sidel_by_iteration(matrix, ans_vector, initial_guess, iterations):
    for k in range(iterations):
        for i in range(matrix.rows):
            b_i = ans_vector.values[i]
            pivot_i = matrix.values[i][i]
            sum = 0
            for j in range(matrix.cols):
                if(j != i): 
                    sum += matrix.values[i][j] * initial_guess.values[j]
            initial_guess.values[i] = (b_i - sum) / (pivot_i)

    return initial_guess

def gauss_sidel_by_error(matrix, ans_vector, initial_guess, abs_rel_err):
    return 0


def gauss_sidel(matrix, ans_vector, initial_guess, iterations=0, abs_rel_err=None):

    if(iterations > 0):
        return gauss_sidel_by_iteration(matrix, ans_vector, initial_guess, iterations)
    
    elif(abs_rel_err != None):
        return gauss_sidel_by_error(matrix, ans_vector, initial_guess, abs_rel_err)
    else:
        raise ValueError("stopping condition is not defined")
    
