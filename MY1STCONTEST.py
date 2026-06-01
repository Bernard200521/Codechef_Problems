# Input values
N, A, B = map(int, input().split())

# Users who get rating
rated_users = N - A

# Users with rating greater than 1000
high_rating = rated_users - B

# Print results
print(rated_users, high_rating)