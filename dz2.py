class UserErr(Exception):
    pass


class User:


    def division(self):
        num = int(input('Ведите число! \n'))
        while num == 0:
            try:
                raise UserErr(f'Делить на 0 нельзя!')
            except UserErr as err:
                print(err)
            num = int(input('Введите другое число! \n'))
        else:
            num != 0
            result = 100 / num
            print(round(result, 2))
            # if num == 0:
            #     # raise UserErr(f'Делить на 0 нельзя!')
            #     input('Введите другое число! \n')
            # else:
            #     result = 100 / num
            #     return round(result, 2)


u = User
u.division(User)
