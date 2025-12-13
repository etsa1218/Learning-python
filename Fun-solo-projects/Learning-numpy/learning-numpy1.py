import numpy as np

# This is how users will create the amount of rows and colomns

rows = int(input("how many columns in your matrix do you want"))

cols = int(input("how many columns in your matrix do you want"))

matrix = []

# this is the for loop
for i in range(rows):
    row = input(f"input row {i+1} ({cols} numbers): ")
    matrix.append(list(map(float, row.split())))

matrix = np.array(matrix)
print(matrix)

# this will ask if they whant the matrix to have the eigenvectors and eigenvalues output
eigein_funct = input(
    "Do you want to calculate eigenvectors and eigenvalues?(Y/N)")
if eigein_funct == "Y":
    w, v = np.linalg.eig(matrix)

    print("the eigenvalues are \n", w, "\n and the eigenvectors are \n")
if eigein_funct == "N":
    print("thats it")
