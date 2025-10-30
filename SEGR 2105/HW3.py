
# ----- IMPORTANT -----
# question 3 I wrote it so that the computation would take way too long to compute. If you are reading this I ran out of time
#for question 4 I found the matrix multiplication after so I made a new one lol

def q1_2():
    # Q1: approximation alg for Knapsack using 'value/weight ratio' method. 
    # This will prioritize items with largest value/weight ratio (value of item divded by of item)
    #      a. compute value of each item
    #      b. sort items by value/weight ratios in descending order (largest to smallest)
    #      c. add items into knapsack using sorted order until knapsack constraint is no longer satisfied
    #      d. all units that were added to knapsack without violating constraint are included in approximated solution

    import random
    random.seed(100)

    #problem parameters
    knapsack_weight = 50
    num_items = 25

    #problem instance data
    items = [i for i in range(1, num_items + 1)]
    item_properties = {}
    for i in items:
        item_properties[i] = {
            'weight': random.randint(5,15),
            'value': random.randint(1,10)
        }

    # a. find value of each item/weight ratio
    ratio_list = []
    for item_id, property in item_properties.items():
        # Calculates the ratio inside this loop
        current_ratio = property['value'] / property['weight']
        
        # Adds the ratio and the item's ID to the list as tuple
        ratio_list.append((current_ratio, item_id))

    # b. Sorts the list. 
    sorted_ratio_list = sorted(ratio_list, reverse=True)

    # c&d. add to knapsack, shows units added
    knapsack = []       #where units go

    current_weight = 0
    current_value = 0
    # Loops through sorted list
    for ratio, item_id in sorted_ratio_list:
        # Using the item_id to find the item's properties
        item_weight = item_properties[item_id]['weight']
        item_value = item_properties[item_id]['value']
        
        # Check if the item fits
        if current_weight + item_weight <= knapsack_weight:
            knapsack.append(item_id)
            current_weight += item_weight
            current_value += item_value

    # Final Solutions
    print("Greedy Algorithm Solution:",
        f"\nSelected Item ID's: {knapsack}",
        f"\nCurrent Weight: {current_weight}, Knapsack Weight: {knapsack_weight}, did not go over",
        f"\nKnapsack Total Value: {current_value}")

    # To compare the greedy solution and the brute-force method, the greedy solution is quicker but less efficient, and brute-force is exact, but longer
    # So the greedy solution would be good for a quick answer that does not need to be perfect
    # However the brute-force method would be better for answers that must be exact, and don't mind taking longer


    # Q2: Implement a random-search algorithm for the Knapsack problem
    #write a program that randomly generates different combinations of items and evaluate their respective solution qualities. Output the
    # best-found solution from your algorithm after meeting either of the below terminating conditions:
    # 1. No improvement in the best solution for 100 consecutive iterations;
    # 2. Performing at most 10,000 iterations

    # random variables
    no_improvement = 100
    current_no_improvement = 0
    max_iterations = 10000

    # variables for best solution
    best_value = 0
    best_weight = 0
    best_id_solution = []

    #keeps within max iterations
    for i in range(max_iterations):
        
        # temporary variables
        current_combination = []
        current_value = 0
        current_weight = 0
        
        # Loop that goes through all possible items
        for item_id in items:
            # Give it a 50% change
            if random.random() < 0.5:
                property = item_properties[item_id]
                current_combination.append(item_id)
                current_weight += property['weight']
                current_value += property['value']

        # Check if it's a valid solution (under or at weight limit)
        if current_weight <= knapsack_weight:
            
            # valid, check if better
            if current_value > best_value:
                # new best solution
                best_value = current_value
                best_weight = current_weight
                best_combination = current_combination
                
            else:
                # valid, not better.
                current_no_improvement += 1
        else:
            # over the weight
            no_improvement += 1

        # Check how many times there's no improvement
        if current_no_improvement >= no_improvement:
            break

    # Final Solution
    print("\nRandom Search Algorithm Solution:",
        f"\nSelected Item ID's: {best_combination}",
        f"\nCurrent Weight: {best_weight} Knapsack Weight: {knapsack_weight}, did not go over",
        f"\nKnapsack Total Value: {best_value}")


def part_q3(number_of_tasks):
    # Q3: Workers need to be assigned tasks, each worker must get 1 task each

    from itertools import permutations
    import random

    random.seed(100)
    num_tasks = number_of_tasks

    global_best_benefit = 0
    best_solution = None

    tasks = [i for i in range(1, num_tasks+1)]   #[1,2,3,...,10]
    task_properties = {}
    for task in tasks:
        workers_benefit = {}     #give keys: 1,2,3..., to number_of_tasks

        for worker in range(1, num_tasks+1):
            workers_benefit[worker] = random.randint(1,10)        # for each key, give random integer
            
        # Assigns current task dictionary of worker benefits
        task_properties[task] = dict(workers_benefit)

    for subset in permutations(sorted(tasks), num_tasks):    #subset will be a tuple of task, value is worker
        current_benefit = 0
        
        # enumerate("subset", 1) to start task_id at 1
        for task_id, worker_id in enumerate(subset, 1):
            # Find benefit, add to current
            benefit = task_properties[task_id][worker_id]
            current_benefit += benefit
            
        # Check if this combination is the new best
        if current_benefit > global_best_benefit:
            global_best_benefit = current_benefit
            best_solution = subset

    # Prints the results
    print(f"Solution for num_tasks = {num_tasks}")
    print(f"Best Solution for Workers for Tasks 1-{num_tasks}: {best_solution}")
    print(f"Max Total Benefit: {global_best_benefit}")

def q3():
    part_q3(number_of_tasks=10)
    # part_q3(number_of_tasks=20)
    # part_q3(number_of_tasks=30)



def q4():
    matrix_dim = input("What dimensions would you like your matrices 1 and 2? (positive integers)"
                       "\nSplit the dimensions with a comma: (row),(column). EX: 3,2 --> 3x2 matrix\n").split(',')

    matrix_dim = [int(i) for i in matrix_dim]      #convert to int

    matrix1 = []
    print(f"Next insert the numeric values of your {matrix_dim[0]} x {matrix_dim[1]} matrix (again, with a comma)")
    for row in range(matrix_dim[0]):
        print("next row")
        temp_row = []
        for col in range(matrix_dim[1]):
            val = float(input("input value: "))
            temp_row.append(val)
        matrix1.append(temp_row)

    matrix2 = []
    print("Do it again for matrix 2:")
    for row in range(matrix_dim[0]):
        print("next row")
        temp_row = []
        for col in range(matrix_dim[1]):
            val = float(input("input value: "))
            temp_row.append(val)
        matrix2.append(temp_row)

    final_matrix = []
    operation = input("Do you want to add or subtract matrix 2 to matrix 1?")

    if operation.lower() == 'add':
        # Go through each row
        for i in range(matrix_dim[0]):
            new_row = []
            # Go through each column in row
            for j in range(matrix_dim[1]):
                # Add
                sum_val = matrix1[i][j] + matrix2[i][j]
                new_row.append(sum_val)
            # Add the completed row to the final matrix
            final_matrix.append(new_row)

    elif operation.lower() == 'subtract':
        # Go through each row
        for i in range(matrix_dim[0]):
            new_row = []
            # Go through each column in row
            for j in range(matrix_dim[1]):
                # Subtract
                diff_val = matrix1[i][j] - matrix2[i][j]
                new_row.append(diff_val)
            # Add the completed row to the final matrix
            final_matrix.append(new_row)

    else:
        print("Invalid operation. Please run again and type 'add' or 'subtract'.")

    # print final
    if final_matrix:
        print("\nResulting Matrix:")
        for row in final_matrix:
            print(row)



def q7():


    import random
    def linear_search(L, e):

        # L is the data structure we are going to search over,
        # e is the item we are interested in looking for.

        idx = 0
        for i in L:
            if i == e:
                print(f'item was found at index {idx}')
                print(f"Runs: {idx}")
                return True
            if i > e:
                print(f'all items in L will be strictly greater than {e}, so terminating the search early...')
                print(f"Runs: {idx}")
                return False
            idx += 1
        print('item was not found')
        return False

    runs = 0
    num_dataset = 10000
    num_find = 50
    lst = [random.randint(1,num_dataset) for i in range(num_dataset)]
    lst.sort()
    print("Linear Search")
    linear_search(L = lst, e = num_find)

    print("\nBinary Search")
    low = 0
    high = len(lst) - 1
    x = num_find
    while low <= high:
        mid = (low + high) // 2
        # if x is greater than lst[mid], that means lst[mid] is an under-approximation
        # so we want to chop off the left side of the list
        if lst[mid] < x:
            low = mid + 1
            runs += 1
            # if x is lesser than lst[mid], that means lst[mid] is an over-approximation
            # so we want to chop off the right side of the list
        elif lst[mid] > x:
            high = mid - 1
            runs += 1
            # if x is equal to lst[mid], that means we found the value we were looking for
        elif lst[mid] == x:
            print(f"value {x} was found at index {mid}")
            print(f"low: {low}, high: {high}")
            print(f"Runs: {runs}")
            break





while True:
    qOption = input("Select which question you would like to review: (1&2),(3),(4),(7),(stop): ")
    match qOption.lower():
        case '1&2':
            q1_2()
        case '3':
            q3()
        case '4':
            q4()
        case '7':
            q7()
        case 'stop':
            break
        case _:
            print("try again")