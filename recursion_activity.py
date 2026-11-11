def sum_array(arr):
    if len(arr) == 0:
        return 0
    return arr[0] + sum_array(arr[1:])


def find_largest(arr):
    if len(arr) == 0:
        raise ValueError("Input array must not be empty.")
    if len(arr) == 1:
        return arr[0]
    
    largest_in_rest = find_largest(arr[1:])
    return arr[0] if arr[0] > largest_in_rest else largest_in_rest


def count_number(arr, target):
    if len(arr) == 0:
        return 0
    
    match = 1 if arr[0] == target else 0
    return match + count_number(arr[1:], target)


if __name__ == "__main__":
    print("=== 1. Testing sum_array ===")
    print("Empty array []:", sum_array([]))                     
    print("One number [10]:", sum_array([10]))                  
    print("Mixed numbers [5, -2, 8, -1]:", sum_array([5, -2, 8, -1])) 

    print("\n=== 2. Testing find_largest ===")
    print("One number [7]:", find_largest([7]))               
    print("Largest at start [99, 4, 12]:", find_largest([99, 4, 12])) 
    print("Largest at end [3, 15, 42]:", find_largest([3, 15, 42]))   
    print("Negative numbers [-10, -3, -25]:", find_largest([-10, -3, -25])) 

    print("\n=== 3. Testing count_number ===")
    print("Empty array ([], 5):", count_number([], 5))          
    print("Appears multiple times ([2, 4, 2, 2, 9], 2):", count_number([2, 4, 2, 2, 9], 2)) 
    print("Does not appear ([1, 3, 5], 8):", count_number([1, 3, 5], 8)) 

