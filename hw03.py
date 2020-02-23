def parse_file (file_name='date.txt'):
    with open ('date.txt') as f:
        lines = f.readlines()
        print (lines)
        return lines

parse_file ()

def parse_line (lines):
    payments = {}
    for line in parse_file(file_name='date.txt'):
        splitted = line.split(';')
        if len(splitted)<5:
            continue
        name, amount, date, p_type, *others = splitted
        if p_type!='out':
            continue
        amount = float(amount.split()[0].replace(',', '.'))
        if name in parse_file():
            payments[name].append (amount)
        else:
            payments[name] = [amount]
    return payments   

print (parse_line(payments))

def max_count_of_perch (count, person):
    person = ''
    count = 0
for name, sums in parse_line(payments).items:
    if len (sums)>count:
        count = len (sums)
        person = name
max_count_of_perch (count, person)
print (person)
print ('Количество покупок: ' , count)
