import numpy as np

# Input-Output matrix (IOM) - Leontief model
A = np.array([[0.3, 0.2, 0.1], [0, 0.2, 0.2], [0.1, 0.3, 1]])

# Expected demand (External Demand)
D = np.array([300, 300, 300])

# Calculate total producgtion required
try: 
    
    # Calulate inverse of (I-A)
    B = np.linalg.inv(np.eye(3) - A)
    X = np.dot(B, D)

    # Check is the internal demand is met
    flag = 0
    for num in X:
        if num<0:
            flag = -1

    if(flag!=-1):
        print('It is possible to achieve the demand!!')
        print("Total production required:\n", X)
    else:
        print(X)
        print("The external demand cannot be satisfied because internal demand is not satisfied.")
        print("The economy is lost")

# If the input output matrix is a Markov Matrix
except np.linalg.LinAlgError:
    print("The given matrix is a Markov matrix and the economy is at equillibrium.")