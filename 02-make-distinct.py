import sys

def main():
    # Read the input data
    input = sys.stdin.read()
    data = input.split()
    
    # Extract N from the first line and convert to integer
    N = int(data[0])
    
    # Validate N
    if not (1 <= N <= 2 * 10**5):
        print("N is out of bounds.")
        sys.exit()
    
    # Extract A from the second line, convert each element to integer, and store in a list
    A = list(map(int, data[1:]))
    
    # Validate list items
    if any(x < 1 or x > N for x in A):
        print("Elements out of bounds.")
        sys.exit()
    
    # Define variables
    operations = 0
    processed = set()
    
    # Iterate A
    for i in range(len(A)):
        number = A[i]
        
        # Determine if number exists in list processed
        if number in processed:
            
            # Define variables
            prev_number = number
            next_number = number
            cost_of_reducing = 0
            cost_of_increasing = 0
            
            # Determine the prev number and cost of reducing
            while prev_number in processed:
                prev_number -= 1
                cost_of_reducing += 1
            
            # Determine the next number and cost of increasing    
            while next_number in processed:
                next_number += 1
                cost_of_increasing += 1
                
            # Determine the minimum cost and the new number.
            min_cost, new_number = (cost_of_reducing, prev_number) if cost_of_reducing <= cost_of_increasing else (cost_of_increasing, next_number)
            
            operations += min_cost
            processed.add(new_number)
        else:
            processed.add(number)
            
    print(operations)

if _name_ == "_main_":
    main()