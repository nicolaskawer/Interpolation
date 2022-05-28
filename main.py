# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def linear_interpolation(arr, x_f1):
    for i in range(len(arr[0])):
        if arr[0][i] > x_f1:
            x_1 = arr[0][i - 1]
            x_2 = arr[0][i]
            function_x_f = (((arr[1][i-1] - arr[1][i]) * x_f1) / (x_1 - x_2)) + ((arr[1][i] * x_1 - arr[1][i-1] * x_2) / (x_1 - x_2))
            break
    return function_x_f




"""Matrix calculator methods:"""
def make_unit_matrix():
    unit_matrix = []
    for i in range(0, size):
        temp = []

        for j in range(0, size):
            if i == j:
                temp.append(1)
            else:
                temp.append(0)
        unit_matrix.append(temp)
    return unit_matrix

def make_elementary_matrix(pivot, num1, row, col):
    temp_elementary = make_unit_matrix()
    temp_elementary[row][col] = -1 * (num1 / pivot)
    return temp_elementary

def exchange(row, row_replace):
    unit_matrix = temp_elementary = make_unit_matrix()
    temp_elementary[row], temp_elementary[row_replace] = unit_matrix[row_replace], unit_matrix[row]
    return temp_elementary

def gauss_method(matrix):
    mul = make_unit_matrix()
    for r in range(size):
        maxi = abs(matrix[r][r])
        flag = 0
        for c in range(r, size):
            if abs(matrix[c][r]) > maxi:
                maxi = abs(matrix[c][r])
                flag = 1
                c_max = c
        if flag != 0:
            temp_matrix = exchange(r, c_max)
            mul = multiply_two_matrix(temp_matrix, mul)
            matrix = multiply_two_matrix(temp_matrix, matrix)
    for r in range(size):
        for c in range(r, size):
            if matrix[r][r] == 1 and r != c:
                temp_matrix = make_elementary_matrix(matrix[r][r], matrix[c][r], c, r)
                mul = multiply_two_matrix(temp_matrix, mul)
                matrix = multiply_two_matrix(temp_matrix, matrix)
            else:
                temp_matrix = make_unit_matrix()
                if matrix[r][r] < 0:
                    temp_matrix[r][r] = 1 / matrix[r][r]
                else:
                    temp_matrix[r][r] = 1 / matrix[r][r]
                mul = multiply_two_matrix(temp_matrix, mul)
                matrix = multiply_two_matrix(temp_matrix, matrix)
    for r in range(size-1, -1, -1):
        for c in range(r, -1, -1):
            if r != c:
                temp_matrix = make_elementary_matrix(matrix[r][r], matrix[c][r], c, r)
                mul = multiply_two_matrix(temp_matrix, mul)
                matrix = multiply_two_matrix(temp_matrix, matrix)
    return mul


def multiply_two_matrix(matrix1, matrix2):
    result = []
    for r in range(len(matrix1)):
        helper_res = []
        for c in range(len(matrix1)):
            helper_res.append(0)
        result.append(helper_res)
    for i in range(len(matrix1)):
        # iterating by column by B
        for j in range(len(matrix2[0])):
            # iterating by rows of B
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result


def Polynomial_interpolation(arr, x_f1):
    strong_matrix = []
    answer_matrix = arr[1]
    for i in range(len(arr[0])-1):
        helper = []
        for j in range(len(arr[0])-1):
            helper.append(arr[0][i] ** j)
        strong_matrix.append(helper)
    #print(strong_matrix)

    multiply_elementary_matrix = gauss_method(strong_matrix)
    for i in range(size):
        final_result.append(0)
    for r in range(len(multiply_elementary_matrix)):
        for c in range(len(multiply_elementary_matrix)):
            final_result[r] += multiply_elementary_matrix[r][c] * answer_matrix[c]
    total_amount = 0
    for i in range(len(final_result)):
        if i == 0:
            total_amount += final_result[i]
            continue
        total_amount += final_result[i] * (x_f1**i)
    return total_amount


def lagrange_interpolation(arr, x_f1):
    Pn = 0
    for i in range(len(arr[0])):
        Li = 1
        for j in range((len(arr[0]))):
            if i==j:
                continue
            Li *= (x_f1-arr[0][j])/(arr[0][i]-arr[0][j])
        Pn += Li*arr[1][i]
    return Pn


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    "לא לשכוח להוסיף הערות לבודק על הטבלת ערכים הזו מתחת"
    two_dimensional_array = tuple([[1, 2, 3, 4], [0.8415, 0.9093, 0.1411, 8]])
    x_f = 2.5
    #another example:
    #two_dimensional_array = tuple([[1, 2, 4], [1, 0, 1.5]])
    #x_f = 3
    final_result = []
    answer_matrix = []
    result = linear_interpolation(two_dimensional_array, x_f)
    print(result)
    size = len(two_dimensional_array[0]) - 1
    result = Polynomial_interpolation(two_dimensional_array, x_f)
    print(result)
    print(lagrange_interpolation(two_dimensional_array, x_f))
    """helper = {}
    size = int(input("enter how many point do u have: "))
    for i in range(size):
        print(i+1, ':\n')
        x = input("x = ")
        y = float(input("y = "))
        helper = {x: y}
        dictionary.update(helper)
    print(dictionary)
    x_f = float(input("Enter the point u want to calculate: "))
    print(dictionary[0])"""





# See PyCharm help at https://www.jetbrains.com/help/pycharm/
