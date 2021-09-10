# Step 1 receive input as s
s = input()

# Step 2 Amount of 'e's is equal to length of string - 2, and we need double that number.
eQty = len(s) - 2
eNeeded = eQty * 2

# Step 3 print h, e * Eneeded, and y
print('h' + ('e' * eNeeded) + 'y')

