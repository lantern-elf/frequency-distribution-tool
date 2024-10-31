data = [
    61, 72, 52, 73, 64, 78, 66, 56, 68, 76, 
    71, 71, 87, 48, 83, 94, 83, 68, 86, 96, 
    52, 74, 40, 68, 42, 75, 43, 48, 44, 82, 
    54, 62, 77, 45, 67, 66, 65, 66, 46, 35,
    72, 61, 76, 65, 56, 54, 58, 54, 76, 85, 
    25, 63, 64, 28, 52, 54, 23, 33, 48, 36 
]

data.sort()

kelas = [
    (23, 33),  
    (34, 44),  
    (45, 55),  
    (56, 66),  
    (67, 77),  
    (78, 88),  
    (89, 99) 
]

frekuensi = [0] * len(kelas)
data_kelas = [[] for _ in range(len(kelas))]

for value in data:
    for i, (bawah, atas) in enumerate(kelas):
        if bawah <= value <= atas: 
            frekuensi[i] += 1
            data_kelas[i].append(value)
            break 

banyak_kelas = sum(frekuensi)

print(f"Frequencies for each class:")
print(f"Data terbesar: {max(data)}")
print(f"Data terkecil: {min(data)}")
print(f"Banyak kelas (total frekuensi): {banyak_kelas}")
for i in range(len(kelas)):
    print(f"Kelas {i + 1} {data_kelas[i]}: {frekuensi[i]}")