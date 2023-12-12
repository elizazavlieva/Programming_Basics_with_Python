width = int(input())
length = int(input())
total_pieces = width * length

while True:
    pieces = input()
    if pieces == 'STOP':
        print(f"{abs(total_pieces)} pieces are left.")
        break
    pieces_cake = int(pieces)
    total_pieces -= pieces_cake
    if total_pieces < 0:
        print(f'No more cake left! You need {abs(total_pieces)} pieces more.')
        break
        