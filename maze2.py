def print_maze(player_position):
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if (i, j) == player_position:
                print("P", end=" ")
            elif maze[i][j] == "#":
                print("#", end=" ")
            else:
                print(maze[i][j], end=" ")
        print()
def move_player(direction):
    global player_position
    new_position = player_position
    if direction == "up" and player_position[0] > 0:
          new_position = (player_position[0] - 1, player_position[1])
    elif direction == "down" and player_position[0] < len(maze) - 1:
        new_position = (player_position[0] + 1, player_position[1])
    elif direction == "left" and player_position[1] > 0:
        new_position = (player_position[0], player_position[1] - 1)
    elif direction == "right" and player_position[1] < len(maze[0]) - 1:
        new_position = (player_position[0], player_position[1] + 1)
    if maze[new_position[0]][new_position[1]] != "#":
        player_position = new_position
    else:
        print("You hit a wall. Change your direction.")
def is_game_over():
    return player_position == exit_position
maze = [
    "##########",
    "#        #",
    "#   ##   #",
    "#   ##   #",
    "#        #",
    "#   ##   #",
    "#   ##   #",
    "#   ##   #",
    "#   ##   #",
    "##########"
]
player_position = (1, 1)
exit_position = (len(maze) - 2, len(maze[0]) - 2)
while not is_game_over():
    print_maze(player_position)
    direction = input("Enter your move (up/down/left/right): ").lower()
    move_player(direction)
print("Congratulations! You reached the exit!")