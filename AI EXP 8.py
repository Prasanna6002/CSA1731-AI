rooms = {
    'A': 'Dirty',
    'B': 'Dirty'
}
position = 'A'
while 'Dirty' in rooms.values():
    print("Vacuum at", position)
    if rooms[position] == 'Dirty':
        rooms[position] = 'Clean'
        print(position, "cleaned")
    if position == 'A':
        position = 'B'
    else:
        position = 'A'
print("All rooms are clean")
print(rooms)