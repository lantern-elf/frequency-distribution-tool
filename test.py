data = [
    52, 65, 38, 39, 36, 27, 28, 23, 27, 13,
    53, 60, 37, 39, 35, 28, 29, 23, 24, 15,
    55, 49, 47, 31, 35, 27, 30, 24, 25, 17,
    56, 41, 46, 32, 34, 26, 26, 25, 26, 17,
    70, 42, 43, 32, 34, 25, 27, 24, 26, 21,
    53, 43, 43, 33, 33, 28, 25, 25, 14, 20
]

data.sort()

kelas = [
    (13, 20),  
    (21, 30),  
    (31, 39),  
    (40, 48),  
    (49, 57),  
    (58, 66),  
    (67, 75) 
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

# print(f"Frequencies for each class:")
# print(f"Data terbesar: {max(data)}")
# print(f"Data terkecil: {min(data)}")
# print(f"Banyak kelas (total frekuensi): {banyak_kelas}")
# for i in range(len(kelas)):
#     print(f"Kelas {i + 1} ({data_kelas[i]}): {frekuensi[i]}")

print(list(enumerate(kelas)))