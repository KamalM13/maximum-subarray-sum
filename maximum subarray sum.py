def max_subarray(A):
    max_so_far = max_ending_here = A[0]
    print(max_so_far, max_ending_here)
    for i in range(1, len(A)):
        max_ending_here = max(A[i], max_ending_here + A[i])
        max_so_far = max(max_so_far, max_ending_here)
        print(max_so_far, max_ending_here)
    return max_so_far


def main():
    A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(max_subarray(A))
    A = [-2, -3, 4, -1, -2, 1, 5, -3]
    print(max_subarray(A))


if __name__ == "__main__":
    main()
