def hanoi(n, source, auxiliary, target):
    if n == 1:  # Base case: only 1 disk, move it directly
        print(f"Move disk 1 from {source} to {target}")
        return
    
    # Step 1: Move n-1 disks from source to auxiliary, using target as a helper
    hanoi(n-1, source, target, auxiliary)
    
    # Step 2: Move the largest disk from source to target
    print(f"Move disk {n} from {source} to {target}")
    
    # Step 3: Move n-1 disks from auxiliary to target, using source as a helper
    hanoi(n-1, auxiliary, source, target)

# Example: Solve for 3 disks
hanoi(3, 'A', 'B', 'C')
