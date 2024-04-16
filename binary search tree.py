def binary_search(arr, target):
    """
    Perform binary search on a sorted array.

    Parameters:
    - arr: A sorted list of elements.
    - target: The element to search for.

    Returns:
    - index: The index of the target element if found, otherwise -1.
    """
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1

if __name__ == "__main__":
    # User input for the array
    arr = input("Enter a sorted list of numbers separated by spaces: ").split()
    arr = [int(x) for x in arr]  # Convert input strings to integers
    target = int(input("Enter the target element to search for: "))

    # Perform binary search
    index = binary_search(arr, target)

    # Output the result
    if index != -1:
        print(f"Element {target} found at index {index}.")
    else:
        print(f"Element {target} not found in the array.")