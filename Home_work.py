from datetime import date

group_members = {
    'Luke':{
        'role':'вокалист', 
        'dob':date(1991, 8, 16)
        },
    'Dante':{
        'role':'гитарист', 
        'dob':date(1986, 3, 12)
        },
    'Derrick':{
        'role':'барабанщик', 
        'dob':date(1989, 3, 23)
        }
    }
def remove_member(name):
    del group_members[name]
    return group_members
def add_member(name, role, year, month, day):
    group_members[name] = dict(role = role, dob = date(year, month, day))
    return group_members

concerts = {
    'Киев':{
        'затраты':{
            'отель': 23411 ,
            'питание': 12341,
            'проезд': 1234,
            'другое': 7654 
        },
        'сумма_контракта':657477,
        'дата': date(2021, 7, 11)
    },
    'Москва':{
        'затраты':{
            'отель': 8754 ,
            'питание': 48975,
            'проезд': 5683,
            'другое': 3463 
        },
        'сумма_контракта':548357,
        'дата':date(2021, 6, 14)
    },
    'Новосибирск':{
        'затраты':{
            'отель': 3463,
            'питание': 3345,
            'проезд': 7664,
            'другое':4654 
        },
        'сумма_контракта':533316,
        'дата':date(2021, 3, 21)
    },
    'Санкт-Петерсбург':{
        'затраты':{
            'отель': 64564,
            'питание': 3477,
            'проезд': 5644,
            'другое': 3565 
        },
        'сумма_контракта':571824,
        'дата':date(2021, 4, 15)
    },
    'Бишкек':{
        'затраты':{
            'отель': 9876,
            'питание': 5675,
            'проезд': 4674,
            'другое': 5786 
        },
        'сумма_контракта':426802,
        'дата':date(2021, 5, 26)
    }
}
def add_concert(sity, hotel, food, way, other, income, year, month, day):
    concerts[sity] = dict(затраты = dict(отель = hotel, питание = food, проезд = way, другое = other), сумма_контракта = income, дата = date(year, month, day))
    return concerts
def sum_expenses(sity):
    x = concerts[sity]['затраты']['отель'] + concerts[sity]['затраты']['питание'] + concerts[sity]['затраты']['проезд'] + concerts[sity]['затраты']['другое']
    return x
def profit(sity):
    x = concerts[sity]['сумма_контракта'] - sum_expenses(sity) 
    return x
print('Чистая прибыль за все концерты:', profit('Бишкек') + profit('Киев') + profit('Москва') + profit('Новосибирск') + profit('Санкт-Петерсбург'))
