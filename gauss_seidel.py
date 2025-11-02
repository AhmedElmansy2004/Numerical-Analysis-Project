from Matrix import *
from Vector import *

def is_diagonally_dominant(matrix):
    condition_2 = False

    for i in range(matrix.rows):
        sum = 0
        for j in range(matrix.cols):
            if(i != j): sum += abs(matrix.values[i][j])
        if(abs(matrix.values[i][i]) >= sum):
            if(abs(matrix.values[i][i]) > sum): condition_2 = True
        else: return False
    
    return (condition_2)
           
def gauss_seidel_by_iteration(matrix, ans_vector, initial_guess, iterations):
    for k in range(iterations):
        for i in range(matrix.rows):
            b_i = ans_vector.values[i]

            pivot_i = matrix.values[i][i]
            if abs(pivot_i) < 1e-12:        #what if the pivot is zero
                return f"Zero pivot detected at row {i}. Cannot proceed."            
            row_sum = 0
            for j in range(matrix.cols):
                if(j != i): 
                    row_sum += matrix.values[i][j] * initial_guess.values[j]
            initial_guess.values[i] = (b_i - row_sum) / (pivot_i)

    return initial_guess

def gauss_seidel_by_error(matrix, ans_vector, initial_guess, abs_rel_err):       #abs_rel_err is not in percentage, this will be fixed in GUI
    it = 1000   #wait 1000 iteration other than that the system diverges
    while(it):
        mx_epsilon = 0

        for i in range(matrix.rows):
            previous_approximation = initial_guess.values[i]

            b_i = ans_vector.values[i]
            pivot_i = matrix.values[i][i]
            if abs(pivot_i) < 1e-12:        #what if the pivot is zero
                return f"Zero pivot detected at row {i}. Cannot proceed."

            sum = 0
            for j in range(matrix.cols):
                if(j != i): 
                    sum += matrix.values[i][j] * initial_guess.values[j]
            initial_guess.values[i] = (b_i - sum) / (pivot_i)   

            if(abs(previous_approximation) > 1e-12):
                epsilon = (initial_guess.values[i] - previous_approximation) / (previous_approximation)
            else: 
                epsilon = (initial_guess.values[i] - previous_approximation)

            mx_epsilon = max(mx_epsilon, abs(epsilon))
        
        if(mx_epsilon <= abs_rel_err and mx_epsilon != 0):
            break
        if(not is_diagonally_dominant(matrix)): it -= 1

    if(it): return initial_guess
    else: return "The system diverges!!!"


def gauss_seidel(matrix, ans_vector, initial_guess, iterations=0, abs_rel_err=-1):

    if(iterations > 0):
        return gauss_seidel_by_iteration(matrix, ans_vector, initial_guess, iterations)
    
    elif(abs_rel_err != -1):
        return gauss_seidel_by_error(matrix, ans_vector, initial_guess, abs_rel_err)
    else:
        raise ValueError("stopping condition is not defined")
    
