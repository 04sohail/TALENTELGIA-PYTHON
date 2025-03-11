# starPattern_10.py

# ******
# *    *
# *    *
# ******

# nr = 4  
# nc = 6  

# for i in range(1, nr + 1):  # Loop through rows
#     for j in range(1, nc + 1):  # Loop through columns
#         # Print '*' for the top and bottom rows, or the first and last columns
#         if i == 1 or i == nr or j == 1 or j == nc:
#             print("*", end="")
#         else:
#             print(" ", end="")  # Print space for inner cells
#     print("")  # Move to the next line after each row


nr = 4
nc = 6

for i in range(1, nr+1):
    for j in  range(1, nc+1):
        if i == 1 and j == 1 or i == nr and j == nr:
            print("*", end="")
        else:
            print(" ", end="")
    print("")
