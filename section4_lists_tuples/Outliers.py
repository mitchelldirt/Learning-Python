data = [4, 5, 104, 105, 110, 120, 130, 130, 150,
        160, 170, 183, 185, 187, 188, 191, 350, 360]
# data = [104, 105, 110, 120, 130, 130, 150,
#          160, 170, 183, 185, 187, 188, 191, 350, 360]
# data = [4, 5, 104, 105, 110, 120, 130, 130, 150,
#          160, 170, 183, 185, 187, 188, 191, 350, 360]
# data = [104, 105, 110, 120, 130, 130, 150,
#          160, 170, 183, 185, 187, 188, 191]
# data = [4111, 5111, 1014, 1051, 1110, 1201, 1310, 1130, 1510,
#          1160, 1170, 1183, 1851, 1817, 1188, 1911, 3501, 3601]
# data = []
min_valid = 100
max_valid = 200

stop = 0
for index, value in enumerate(data):
    if value >= min_valid:
        stop = index
        break

print(stop)
del data[:stop]
print(data)

start = 0
for index in range(len(data) - 1, -1, -1):  #Start, Stop, Step
    if data[index] <= max_valid:
        #We have the index of the last item to keep.
        #Set 'start' to the position of the first.
        #item to delete, which is 1 after the 'index'
        start = index + 1
        break

print(start)
del data[start:]
print(data)