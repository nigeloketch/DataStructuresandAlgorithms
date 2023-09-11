def remove_duplicates(sequence):
    seen = set()  # Create a set to keep track of seen elements
    result = []   # Initialize an empty list to store unique elements
    
    for item in sequence:
        if item not in seen:
            # If the item is not in the set of seen elements, add it to the result
            seen.add(item)  # Mark the item as seen
            result.append(item)  # Add the unique item to the result list
    
    return result

input_sequence = [2, 3, 2, 4, 5, 3, 6, 7, 5]
result = remove_duplicates(input_sequence)
print(result)  # Output: [2, 3, 4, 5, 6, 7]
