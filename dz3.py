import time


class UserErrValue(Exception):
    def __init__(self, mesage):
        super().__init__(mesage)


# def add_list():
#     num_list = []
#     num = input('Введтье число! \n')
#     while num != 'stop':
#         if num.isdigit():
#             num_list.append(num)
#             num = input('Введите следующее число! \n')
#         else:
#             raise UserErrValue('не число!')
#         if num == 'stop':
#             print(num_list)
#             break

# add_list()


def add_list():
    list2 = []
    num_list = []
    num = input('Введтье число! \n')
    while num != 'stop':
        if num.isdigit() == True:
            num_list.append(num)
        num = input('Введите следующее число! \n')
        try:
            if num.isdigit() == False:
                raise UserErrValue('Не число!')
        except UserErrValue as err:
            list2.append(num)
            print(err)
    if num == 'stop':
        print(num_list)
        # print(list2)


add_list()
