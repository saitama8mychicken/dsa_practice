"""

"""


def graphColoring(graph, k, V):
    def check_if_colors_possible(colors):
        return False

    color_combinations_possible = []

    def backtrack(nums, path):

        if len(nums) == 0:
            color_combinations_possible.append(path)

        for i in range(len(nums)):
            backtrack(nums[:i] + nums[i:], path + [nums[i]])

    # your code here
    colors = [i for i in range(1, k + 1)]
    # color_combinations_possible = backtrack(colors, [])
    print(graph, k, V)
    if color_combinations_possible:
        return 1
    else:
        return 0


if __name__ == "__main__":
    res = graphColoring([[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6]], 3, 6)
    print(res)
