# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

#def linear_interpolation(dict1):


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    dictionary = {}
    helper = {}
    size = int(input("enter how many point do u have: "))
    for i in range(size):
        print(i+1, ':\n')
        x = input("x = ")
        y = float(input("y = "))
        helper = {x: y}
        dictionary.update(helper)
    print(dictionary)
    x_f = float(input("Enter the point u want to calculate: "))
    print(dictionary[0])
    """יש פה בעייה להמשך כי נגיד בלינארית אני צריך שתי נקודות שהנקודה נמצאת בנייהם ואני צריך לבדוק נקודה נקודה כלומר לעבור על המילון שלי ואני לא יכול לעבור כמו שאת רואה 
    למעלה וזה בעיה




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
