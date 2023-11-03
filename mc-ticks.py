def calculate(input, multiplier):
    result = int(input)*int(multiplier)
    if len(str(result)) >= 12:
        print(f'{result} Ticks.')
        enter()
    else:
        print('\n{:,} Ticks\n'.format(result))
        enter()

def validate(input, measurement):
    if measurement.lower() not in ['s', 'm', 'h', 'seconds', 'second', 'minutes', 'minute', 'hours', 'hour']:
        print('Valid units of measurement are seconds(s), minutes(m), or hours(h)')
        enter()
    else:
        if measurement.lower() == 's' or measurement.lower() == 'seconds' or measurement.lower() == 'second':
            calculate(input, multiplier=20)
        elif measurement.lower() == 'm' or measurement.lower() == 'minutes' or measurement.lower() == 'minute':
            calculate(input, multiplier=20*40)
        elif measurement.lower() == 'h' or measurement.lower() == 'hours' or measurement.lower() == 'hour':
            calculate(input, multiplier=20*60)

def enter():
    print('MC-TICKS.py - Enter amount of time. (num)')
    uim = input('> ')
    if uim.isnumeric():
        print('MC-TICKS.py - Enter unit of measurement. (s/m/h)')
        uit = input('> ')
        validate(uim, uit)
    else:
        print('MC-TICKS.py - Input must be numeric.\n')
        enter()

enter()

# https://www.mc-ticks.pro/