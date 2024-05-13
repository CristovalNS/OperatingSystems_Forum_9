def read_requests(file_path):
    with open(file_path, 'r') as file:
        return [int(line.strip()) for line in file if line.strip().isdigit()]
    
def SCAN(requests, start):
    head_moves = 0
    current_position = start
    idx = 0
    
    while idx < len(requests) and requests[idx] < start:
        idx += 1

    right_part = sorted(requests[idx:])
    left_part = sorted(requests[:idx], reverse=True)

    for request in left_part:
        head_moves += abs(current_position - request)
        current_position = request
    current_position = start
    for request in right_part:
        head_moves += abs(current_position - request)
        current_position = request
    return head_moves

def main():
    head = 1234  
    file_path = 'random_numbers.txt'  
    requests = read_requests(file_path)
    requests_sorted = sorted(requests)
    
    scan_moves = SCAN(requests, head)
    sorted_scan_moves = SCAN(requests_sorted, head)

    print(f"Total head movements for original SCAN: {scan_moves}")
    print(f"Total head movements for sorted SCAN: {sorted_scan_moves}")

if __name__ == "__main__":
    main()