import numpy as np
# https://stackoverflow.com/questions/15638650/is-there-a-standard-solution-for-gauss-elimination-in-python
def gaussian_elimination(matrix, vector):
    """
    Solve a system of linear equations Ax = b using Gaussian elimination.
    
    Args:
        matrix: n×n coefficient matrix (A)
        vector: n×1 constant vector (b)
    
    Returns:
        Solution vector x
    """
    n = len(matrix)
    
    # Create augmented matrix [A|b]
    augmented = np.column_stack([matrix.astype(float), vector.astype(float)])
    
    # Forward elimination (create upper triangular matrix)
    for i in range(n):
        # Find pivot (optional but improves numerical stability)
        max_row = i
        for k in range(i + 1, n):
            if abs(augmented[k, i]) > abs(augmented[max_row, i]):
                max_row = k
        
        # Swap rows
        augmented[[i, max_row]] = augmented[[max_row, i]]
        
        # Make all rows below this one 0 in current column
        for k in range(i + 1, n):
            if augmented[i, i] == 0:
                raise ValueError("Matrix is singular and cannot be solved")
            
            factor = augmented[k, i] / augmented[i, i]
            augmented[k, i:] -= factor * augmented[i, i:]
    
    # Back substitution
    solution = np.zeros(n)
    for i in range(n - 1, -1, -1):
        solution[i] = augmented[i, n]
        for j in range(i + 1, n):
            solution[i] -= augmented[i, j] * solution[j]
        solution[i] /= augmented[i, i]
    
    return solution


# Example usage
if __name__ == "__main__":
    # System of equations:
    # 2x + y - z = 8
    # -3x - y + 2z = -11
    # -2x + y + 2z = -3
    
    A = np.array([
        [2123, 11221, -11213],
        [-3033, -11221, 212121],
        [-2678, 11345, 21212]
    ])
    
    b = np.array([8, -11, -3])
    
    solution = gaussian_elimination(A, b)
    print("Solution (x, y, z):", solution)
    print("Verification A @ x =", A @ solution)
    print("Expected b =", b)
