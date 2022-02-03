import re


class Date:
    date = ''
    def __init__(self, date):
        self.date = date

    @classmethod
    def num_date(cls, param):
        patern = re.compile(r'(\d+)')
        result = patern.findall(param)
        day = int(result[0])
        month = int(result[1])
        year = int(result[2])
        return f'{day} {month} {year}'


    @staticmethod
    def valid_date(obj):
        patern = re.compile(r'(\d+)')
        result = patern.findall(obj)
        day = int(result[0])
        month = int(result[1])
        year = int(result[2])
        if month < 1 or month > 12 or year < 2000 or year > 2022:
            print('Неверный месяц или год!')
            raise ValueError
        else:
            print(f'{day} {month} {year}')



val = Date.valid_date('12-12-2021')
print(Date.num_date('12-10-2021'))

# date = '12-01-2015'
# patern = re.compile(r'(?P<day>\d{1,2})\-(?P<month>\d{1,2})\-(?P<year>\d{,4})')
# result = patern.findall(date)
# n_1 = result[0]
# print(result)
# print(*n_1)