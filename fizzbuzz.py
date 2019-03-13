def replace(n):
  A = [i+1 for i in range(n)]
  for i in range(2, len(A), 3):
    A[i] = 'fizz'
  for i in range(4, len(A), 5):
    if A[i] != 'fizz':
      A[i] = 'buzz'
    else:
      A[i] = 'fizzbuzz'
  return A
