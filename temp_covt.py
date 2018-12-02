print('\n\nWELCOME TO TEMPERATURE CONVERTER')
print('Presented by Abhay Adil Enterprises\n')

def fah2cel(fah):
    cel = (fah -32)*5/9
    return cel

def cel2fah(cel):
    fah = cel*9/5+32
    return fah

def kelvin(cel):
    kel = cel+273.15
    return kel

ent = input()

print('\nInstructions:')
print('\n -type f2c to convert Fahrenheit to Celcius')
print(' -type c2f to convert Celcius to Fahrenheit')
print(' -type done to close program\n')

while str(ent) != 'done':

    ent = input('Type option >>>  ')
    if ent == 'f2c':
        inp1 = input('\nEnter Fahrenheit: ')
        try:
            fah = float(inp1)
        except:
            fah = 0
        cel = fah2cel(fah)
        kel = kelvin(cel)
        print('\n')
        print('Fahrenheit', fah, 'is: ', cel, 'Celcius')
        print('And', kel, 'Kelvin')
        print('\nNext instruction-')
        print('\n -type f2c to convert Fahrenheit to Celcius')
        print(' -type c2f to convert Celcius to Fahrenheit')
        print(' -type done to close program\n')


    if ent == 'c2f':
        inp1 = input('\nEnter Celcius: ')
        try:
            cel = float(inp1)
        except:
            cel = 0
        fah = cel2fah(cel)
        kel = kelvin(cel)
        print('\n')
        print(cel, 'Celcius is:', 'Fahrenheit', fah)
        print('And', kel, 'Kelvin')
        print('\nNext instruction-')
        print('\n -type f2c to convert Fahrenheit to Celcius')
        print(' -type c2f to convert Celcius to Fahrenheit')
        print(' -type done to close program\n')
