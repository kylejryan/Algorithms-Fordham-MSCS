import math
import numpy as np

def simplex(c, A, b):  

    # Converting the Equation Form to Tableau
    xb = [eq + [x] for eq, x in zip(A, b)]
    z = c + [0]
    tableau = xb + [z]
    
    # While Loop to See if Any Values Can be Increased
    # Will Only Increase if Objective Doesn't Get Smaller
    z = tableau[-1]
    while any(x > 0 for x in z[:-1]):

        # Searching for Pivot Position
        z = tableau[-1]
        try:
            # Returns Next Iterator
            column = next(i for i, x in enumerate(z[:-1]) if x > 0)
        # Using Try/Except so When Next Method Ends, Function Continues
        except StopIteration:
            pass
        
        # Retrieving Restrictions from Tableau
        # Appending to New Array for Ease of Use
        restrictions = []
        for eq in tableau[:-1]:
            el = eq[column]
            restrictions.append(math.inf if el <= 0 else eq[-1] / el)

        row = restrictions.index(min(restrictions))
        pivot_position = row, column

        # Creating New Tableau
        new_tableau = [[] for _ in tableau]

        # Pivot Step of Algorithm
        i, j = pivot_position
        pivot_value = tableau[i][j]
        new_tableau[i] = np.array(tableau[i]) / pivot_value
        
        for eq_i, eq in enumerate(tableau):
            if eq_i != i:
                multiplier = np.array(new_tableau[i]) * tableau[eq_i][j]
                new_tableau[eq_i] = np.array(tableau[eq_i]) - multiplier

        tableau = new_tableau
    
    # Once Done Optimizing, Create New Array Solution to Append Answer To
    columns = np.array(tableau).T
    solutions = []
    for column in columns:
        solution = 0
        if sum(column) == 1 and len([c for c in column if c == 0]) == len(column) - 1:
            one_index = column.tolist().index(1)
            solution = columns[-1][one_index]
        solutions.append(solution)
        
    return solutions

# Evaluating Algorithm on Test Case
c = [3, 2, 1]
A = [
    [2, 1, 1],
    [2, 2, 8],
    [2, 3, 1]
]
b = [150, 200, 320]

# Returning x, y, z and Max Profit
solution = simplex(c, A, b)
print('x, y, z: ', solution[:3])

# p = 3x + 2y + z
print('Max Value: ', (3*solution[0] + 2*solution[1] + 1*solution[2]))