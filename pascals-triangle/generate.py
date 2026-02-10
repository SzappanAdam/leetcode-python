def generate(numRows: int):
    """
    Generates the first numRows of Pascal's Triangle.
    Each row is constructed based on the previous row.
    """
    triangle = []

    for i in range(numRows):
        row = [1] * (i + 1)

        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        triangle.append(row)

    return triangle