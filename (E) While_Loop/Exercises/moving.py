free_space_width = int(input())
free_space_length = int(input())
free_space_height = int(input())
total_space = free_space_length * free_space_height * free_space_width
boxes_spaces = 0
while True:
    num_of_boxes = input()
    diff = abs(total_space - boxes_spaces)
    if num_of_boxes == 'Done':
        print(f'{diff} Cubic meters left.')
        break
    boxes = int(num_of_boxes)
    boxes_spaces += boxes
    if boxes_spaces > total_space:
        print(f'No more free space! You need {diff} Cubic meters more.')
        break
