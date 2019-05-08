import numpy as np

n = 4
k = 4
j = 2

# This part of code is for verifying the results obtained from calculation. Please comment it when n,k,j are large.
# Initial = np.expand_dims(np.array([1]), axis=1)
# Previous = Initial
# for length in range(1, n, 1):
#     for realization in range(0, Previous.shape[0], 1):
#         new_portion = np.expand_dims(np.arange(1, k+1, 1), axis=1)
#         Last = Previous[realization][-1:]
#         new_portion = np.expand_dims(np.delete(new_portion, Last-1), axis=1)
#         new = np.tile(Previous[realization], (new_portion.shape[0], 1))
#         new = np.hstack((new, new_portion))
#         if realization == 0:
#             new_stack = new
#         else:
#             new_stack = np.vstack((new_stack, new))
#     Previous = new_stack
#     row = Previous.shape[0]
#     Exclude = 0
# for row_count in range(0, row, 1):
#     if Previous[row_count][-1:] != j:
#         Exclude = Exclude + 1
#         Previous[row_count] = 0
# Num_Possible_Sequence = Previous.shape[0] - Exclude
# print(Previous)
# print(Num_Possible_Sequence)
# print(Previous.shape[0])

if j != 1:
    if np.remainder(n, 2) == 0:
        Num_Possible_Estimate = ((k-1)**(n-1)+1)//k
        Num_Possible_End = np.mod(Num_Possible_Estimate, 10000000007)
    elif np.remainder(n, 2) == 1:
        Num_Possible_Estimate = ((k-1)**(n-1)-1)//k
        Num_Possible_End = np.mod(Num_Possible_Estimate, 10000000007)
else:
    if np.remainder(n, 2) == 0:
        Num_Possible_Estimate = ((k-1)**(n-1)+1)//k-1
        Num_Possible_End = np.mod(Num_Possible_Estimate, 10000000007)
    elif np.remainder(n, 2) == 1:
        Num_Possible_Estimate = ((k-1)**(n-1)-1)//k+1
        Num_Possible_End = np.mod(Num_Possible_Estimate, 10000000007)

print(Num_Possible_End)

