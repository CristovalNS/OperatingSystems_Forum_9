def read_requests(file_path):
    with open(file_path, 'r') as file:
        return [int(line.strip()) for line in file if line.strip().isdigit()]

def FCFS(requests, start):
    head_moves = 0
    current_position = start
    for request in requests:
        head_moves += abs(request - current_position)
        current_position = request
    return head_moves

def main():
    head = 1234  
    file_path = 'random_numbers.txt'  
    requests = read_requests(file_path)
    requests_sorted = sorted(requests)
    
    fcfs_moves = FCFS(requests, head)
    sorted_fcfs_moves = FCFS(requests_sorted, head)

    print(f"Total head movements for original FCFS: {fcfs_moves}")
    print(f"Total head movements for sorted FCFS: {sorted_fcfs_moves}")

if __name__ == "__main__":
    main()
