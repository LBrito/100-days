
class Matrix(object):
    def __init__(self, matrix_string):
        self.matrix = [[int(num) for num in col.split(' ')] for col in [row for row in matrix_string.split("\n")]]

    def row(self, index):
        return self.matrix[index - 1]

    def column(self, index):
        return [self.row(i + 1)[index - 1] for i in range(len(self.matrix))]
