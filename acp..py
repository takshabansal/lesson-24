set1 = set(map(int, input("Enter elements of the first set separated by spaces: ").split()))
set2 = set(map(int, input("Enter elements of the second set separated by spaces: ").split()))
symmetric_diff = set1.symmetric_difference(set2)
print("Symmetric difference between the two sets:", symmetric_diff)
