from requests import get

month = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
         'August', 'September', 'October', 'November', 'December']

def get_current():
    r = get('https://api.covidtracking.com/v1/us/current.json')
    return r.json()[0]

def get_historical(date):
    r = get(f'https://api.covidtracking.com/v1/us/{date}.json')
    return r.json()

def date_format(date_input):
    date = str(date_input)
    return f'{month[int(date[4:6]) - 1]} {int(date[6:8])}, {int(date[0:4])}'

def print_data(type):
    if int(type) == 1:
        data = get_current()
    else:
        date_input = input('Enter the date as mm/dd/yyyy : ')
        date_int = int(date_input[6:10] + date_input[0:2] + date_input[3:5])
        data = get_historical(date_int)

    date = data['date']

    infect = [data['positive'], data['positiveIncrease']]
    hospital = [data['hospitalizedCumulative'], data['hospitalizedCurrently'], data['hospitalizedIncrease']]
    death = [data['death'], data['deathIncrease']]

    print('date:', date_format(date), '\n')
    print('infected\n', '\ttoday:', f'+{infect[1]}', '\n\ttotal:', infect[0], '\n')
    print('hospitalized\n', '\ttoday:', f'+{hospital[2]}', '\n\tcurrent:', infect[1], '\n\ttotal:', infect[0], '\n')
    print('dead\n', '\ttoday:', f'+{death[1]}', '\n\ttotal:', death[0], '\n')

while 1:
    a = input('current (1) or historic (2) : ')
    print_data(a)