def towerofhanoi(n, source, helper, destination):
    if n == 0:
        return 0
    
    # Move n-1 disks from source to helper using destination as temporary
    moves = towerofhanoi(n-1, source, destination, helper)
    
    # Move the largest disk from source to destination
    print(f"Move disk from {source} to {destination}")
    moves += 1
    
    # Move n-1 disks from helper to destination using source as temporary
    moves += towerofhanoi(n-1, helper, source, destination)
    
    return moves

total_moves = towerofhanoi(3, "A", "B", "C")

print(f"Total number of moves: {total_moves}")