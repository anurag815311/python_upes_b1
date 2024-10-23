#write a program using dictionary comprehension to create a dictionary 
n=10
res={x:x**2 for x in range(0,n) if x % 2==0}
print(res)
#waf that takes an argument i.e. dictionary and returns a dictionary where keys are values and values are key..
def swap_dict(input_dict):
    # Create an empty dictionary to store swapped key-value pairs
    swapped_dict = {}
    
    # Iterate through the original dictionary
    for key, value in input_dict.items():
        # Swap keys and values
        swapped_dict[value] = key
    
    return swapped_dict

# Example usage
original_dict = {'a': 1, 'b': 2, 'c': 3}
swapped = swap_dict(original_dict)
print(swapped)  # Output: {1: 'a', 2: 'b', 3: 'c'}


#using dictionary comprehension

def flip_dict(d1):
    assert isinstance(d1,dict),"Input is not a dictionary"
    flipped={val:key for key,val in d1.items()}
    return flipped

print(f"flipped dictionary is \n{flip_dict(res)}")