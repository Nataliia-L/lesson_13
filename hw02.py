def parse_file (file_name='weather.txt'):
    weather = {}
    with open (file_name) as f:
        for line in f:
            d, t = parse_line(line)
            if t in weather:
                weather[t].append (d)
            else:
                weather[t] = [d]
    return weather


def parse_line (line):
    date, temp = line.strip ().split (';')
    return date, int(temp)
    

weather = parse_file ()
min_temp = min(weather.keys())
max_temp = max(weather.keys())
print ('Данные в виде словаря: ', weather)
print ('Минимальные значения: ', min_temp, weather[min_temp])
print ('Максимальные значения: ', max_temp,weather[max_temp])
