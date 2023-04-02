result = []
data = []
def divider(a, b):
    if a < b:
        raise ValueError
    if b > 100:
        raise IndexError

    return a/b

try:
    data = {300: 200, 2: 5, 123: 4, 18: 0, 45: 15, 8 : 4}
except TypeError:
    print('Возникло исключения TypeError')
for key in data:
    try:
        res = divider(key, data[key])
        result.append(res)
    except ZeroDivisionError:
        print(f'Возникло исключения ZeroDivisionError! a = {key}, b = {data[key]}')
    except ValueError:
        print(f'Возникло исключения ValueError! a = {key}, b = {data[key]}')
        print(data[key])
    except IndexError:
        print(f'Возникло исключения IndexError! a = {key}, b = {data[key]}')
        print(data[key])
print(result)