import json

with open('/home/sherlock/Documents/GitHub/data-quran/surah/surah.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Get only the nAyah values
n_ayahs = [entry['nAyah'] for entry in data.values()]


T = []

for i in range(len(n_ayahs)):
    T.append([i+1, n_ayahs[i], i +1 + n_ayahs[i]])

print(T)

print(f"Total number of ayahs in the Quran: {sum(n_ayahs)}")
print(f"Sum of the surah numbers : {sum([i+1 for i in range(114)])}")

E = 0
O = 0

for i in T:
    if i[2] % 2 == 0:
        E += i[2]
    else:
        O += i[2]

print(f"Sum of the even surahs: {E}")
print(f"Sum of the odd surahs: {O}")