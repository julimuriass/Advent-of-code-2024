FILE_NAME = "input.txt"

def count_word_occurrences(grid, word):
    rows, cols = len(grid), len(grid[0])
    word_len = len(word)
    directions = [
        (0, 1),  # Horizontal right
        (0, -1), # Horizontal left
        (1, 0),  # Vertical down
        (-1, 0), # Vertical up
        (1, 1),  # Diagonal down-right
        (-1, -1),# Diagonal up-left
        (1, -1), # Diagonal down-left
        (-1, 1)  # Diagonal up-right
    ]

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    def check_direction(x, y, dx, dy):
        for i in range(word_len):
            nx, ny = x + i * dx, y + i * dy
            if not is_valid(nx, ny) or grid[nx][ny] != word[i]:
                return False
        return True

    count = 0
    for r in range(rows):
        for c in range(cols):
            for dx, dy in directions:
                if check_direction(r, c, dx, dy):
                    count += 1
    return count


def restoring_file ():
     lines = []
     with open(FILE_NAME) as f:
         for line in f:
             lines.append(list(line)) # Creates a list of lists (the main list has as elements each line, and the elements are lists with each character).

     return lines

grid = restoring_file()
# Word to search
word = "XMAS"

# Count occurrences
total_occurrences = count_word_occurrences(grid, word)
print(f"Total occurrences of '{word}': {total_occurrences}")