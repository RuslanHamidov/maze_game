def move(position, direction):
    row, col = position
    if direction == 'up' and row > 0 and maze[row - 1][col] != 'X':
        row -= 1
    elif direction == 'down' and row < len(maze) - 1 and maze[row + 1][col] != 'X':
        row += 1
    elif direction == 'left' and col > 0 and maze[row][col - 1] != 'X':
        col -= 1
    elif direction == 'right' and col < len(maze[0]) - 1 and maze[row][col + 1] != 'X':
        col += 1
    else:
        print("You cannot move in that direction. There is a wall!")
    return row, col
def check_win(position):
    return maze[position[0]][position[1]] == 'E'
def display_maze(position):
    row, col = position
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if i == row and j == col:
                print("P", end="")  
            else:
                print(maze[i][j], end="")
        print()  
maze = [
    ['X', 'X', 'X', 'X', 'X'],
    ['.', '.', '.', '.', '.'],
    ['X', '.', 'X', '.', 'X'],
    ['.', '.', '.', '.', '.'],
    ['X', '.', 'X', 'E', 'X'],
]

player_position = (1, 0)
while True:
    display_maze(player_position)
    direction = input("Enter direction (up, down, left, right, or 'exit' to quit game): ").lower()
    if direction == 'exit':
        break 
    else:
        new_position = move(player_position, direction)
        player_position = new_position
    if check_win(player_position):
        print("Congratulations! You found the exit!")
        break  
print("Thanks for playing!")