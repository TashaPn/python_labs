#number_1
nums = [1, 3, 2, 3]
def min_max(nums):
    nums_cell = []
    if len(nums) > 0:
        mini = nums_cell.append(min(nums))
        maxi = nums_cell.append(max(nums))
        print(tuple(nums_cell))
    else:
        raise ValueError
min_max(nums)
#number_2
nums = [3, 1, 2, 1, 3]
def n_sorted(nums):
    new_nums = sorted(set(nums))
    print(new_nums)
n_sorted(nums)
#number_3
mat = [[1, 2], [3, 4]]
def flatten(mat):
    new_mat = []
    for num in mat:
        if type(num) == tuple or type(num) == list:
            for i in range(len(num)):
                if num[i] != '':
                    new_mat.append(num[i])
        else:
            raise ValueError
    print(new_mat)
flatten(mat)