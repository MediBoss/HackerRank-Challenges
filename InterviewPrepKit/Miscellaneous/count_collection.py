from collections import Counter
from collections import defaultdict
import heapq


# Approach one : Use Histogram
# Approach two : Use Histogram + OrderedDict
# Approach three : Use HeapQueue

def create_histogram(arr):
    ''' Creates a key-value pair for an element and its frequency'''
    histogram = {}
    for elem in arr:
        if elem in histogram:
            histogram[elem] += 1
        else:
            histogram[elem] = 1
    return histogram


def get_most_frequent(arr, n):

    histogram = create_histogram(arr) # Key-value pair of element and their frequency
    result = [] # Holds n frequent elements
    max_value = 0 # Keeps track of the current highest element
    count = 0 # Keeps track of only returning n elements

    for key,value in histogram.items():
        if count == n:
            break

        if value > max_value:
            max_value = value
            count += 1
            result.append(key)
    return result

def get_most_frequent_improved(arr, n):

    d = create_histogram(arr)
    result = []
    count = 0

    for w in sorted(d, key=d.get, reverse=True):

        if count == n:
            break
        count += 1
        result.append(w)

    return result

def get_most_frequent_heapq(arr):
    pass
    
def main():
    
    freq = Counter()
    colors = ["red", "blue", "red", "yellow", "purple", "blue", "red", "orange"]

    #print(get_most_frequent(colors, 1))
    print(get_most_frequent_improved(colors, 2))


if __name__ == "__main__":
    main()