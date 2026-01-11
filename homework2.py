import numpy as np
arr = np.array([[10, 20, 30],
                [40, 50, 60],
                [70, 80, 90]])
print("1:", arr[2, 0])
print("2:", arr[:, 1])
print("3:", arr.dtype)
arr_copy = arr.copy()
arr_copy[0, 0] = 999
print("4- النسخة:", arr_copy)
print("الأصل بعد copy:", arr)
arr_view = arr.view()
arr_view[0, 0] = 555
print("5- العرض view:", arr_view)
print("الأصل بعد view:", arr)
print("6:", arr.shape)
print("7:")
for i in range(arr.shape[0]):
    for j in range(arr.shape[1]):
        print(f"العنصر {arr[i,j]} في الصف {i} والعمود {j}")
new_arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
vertical = np.vstack((arr, new_arr))
horizontal = np.hstack((arr, new_arr))
print("8- دمج عمودي:\n", vertical)
print("دمج أفقي:\n", horizontal)
split_arrays = np.hsplit(arr, 3)
print("9:", split_arrays)
pos = np.where(arr == 60)
print("10: الصف:", pos[0][0], "العمود:", pos[1][0])
sorted_arr = np.sort(arr, axis=1)
print("11:\n", sorted_arr)
filtered = arr[arr > 50]
print("12:", filtered)
random_arr = np.random.randint(1, 101, (2,3))
print("13:\n", random_arr)
