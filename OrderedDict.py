from collections import OrderedDict

od = OrderedDict()
od["apple"] = 100
od["banana"] = 200
od["grape"] = 300

print(od)

del od["banana"]

print(od)

od.move_to_end("apple")

print(od)

od.move_to_end("apple", False)

print(od)

