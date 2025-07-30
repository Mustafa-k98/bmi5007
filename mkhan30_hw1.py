import time

def find_majority_element(votes):
    """
     Parameters:
    - votes (list): A list of votes, where each vote is represented as a string.

    Returns:
    - str: The majority element in the list. If no majority element exists, returns None.

    Example:
    >>> find_majority_element(["Alice", "Bob", "Alice", "Alice"])
    'Alice'
    >>> find_majority_element(["Alice", "Bob", "Charlie"])
    None

    Time Complexity:

    The time complexity for this algorithm O(n). 

    The initialization of both the vote_counts dictionary and number_of_votes is O(1).

    The first for loop iterates through each of the (n) votes once in the votes list. 
    Inside the first for loop, the "if not in votes_counts" takes O(1) time on average, and 
    the vote_counts[name] = 1/vote_counts[name] += 1 also takes O(1) time on average. This means
    the first for loop takes n*O(1) time on average which can be reduced to O(n).

    The second for loop iterates through the vote_counts dictionary, which has k enteries2. In the worst case the loop 
    will have to go through the entire dictionary (all values would have to be unique), in the best
    case the loop will have to only go through the first value of the dictionary, making this loops
    time complexity O(k) in most cases, and O(n) in only the worst case. 
    Inside the second for loop, all operations are O(1). This means that this loops time complexity
    can be summized as k*O(1) which can be reduced to O(k).

    To sum the total time complexity, we have O(1) + O(n) + O(k). However, since O(n) is the more
    dominant term, since k always has to be less than n, we can state the overall time complexity as
    O(n).

    """
    # Initializes an empty dictionary
    vote_counts={} 
    # Counts the total number of votes
    number_of_votes = len(votes) 

    # Iterates through each vote to count number of votes per name
    for name in votes: 
        # If the name is new, its count is initialized to one in the entry
        if name not in vote_counts:
            vote_counts[name] = 1
        # If the name already exists, the count is incrimented for the name.
        else:
            vote_counts[name] += 1

    # Checks each candidate to see if they have the majority of votes
    for name, count in vote_counts.items():
        # A candidate can be considered the majority if they have more than half of the votes
        if count > number_of_votes / 2:
            return name 
        
    return None 
    
    
test_cases = [
    ["Alice", "Bob", "Alice", "Alice", "Bob", "Alice"],
    ["Bob", "Bob", "Bob", "Alice", "Alice"],
    ["John", "John", "John", "John", "Mike", "Mike", "Mike", "Mike", "Mike"],
    ["Steve", "Steve", "Alex", "Steve"] * 1000000,  # Large dataset
    ["John", "John", "Mike", "Mike"],  # No majority element
     ["Alice"] * 500000 + ["Bob"] * 499999,  # Majority by 1
    ["Alice", "Bob"] * 250000 + ["Alice"],  # Alternating with Alice as majority by 1
    ["Candidate_" + str(i) for i in range(1, 1000000)],  # No majority, all unique
    ["Even"] * 500000 + ["Odd"] * 500000,  # Equal distribution, no majority
    ["Repeat"] * 1000000,  # Single candidate repeated, clear majority
    ["First"] * 500001 + ["Second"] * 499999,  # Majority at the beginning
    ["Start"] + ["Middle"] * 999998 + ["End"],  # Majority in the middle
]

for i, votes in enumerate(test_cases, 1):
    start_time = time.time()
    majority = find_majority_element(votes)
    elapsed_time = time.time() - start_time
    print(f"Test Case {i}: Majority Element = {majority}, Elapsed Time = {elapsed_time:.6f} seconds")
