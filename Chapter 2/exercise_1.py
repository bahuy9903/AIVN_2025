# Page 54
# Input: num_list = [3,4,5,1,-44,5,10,12,33,1] voi k=3
# Output: [5,5,5,5,10,12,33,33]
def max_over_kernel(num_list, k):
    if k <= 0 or k > len(num_list):
        raise ValueError("k must be between 1 and the length of the list")
    result = []
    for i in range(len(num_list)-k+1):
        window = num_list[i:i+k]
        max_in_window = max(window)
        result.append(max_in_window)
    
    return result   
if __name__ == "__main__":
    num_list = [3,4,5,1,-44,5,10,12,33,1]
    k = 3
    output = max_over_kernel(num_list, k)
    print(output)  # Output: [5, 5, 5, 5, 10, 12, 33, 33]