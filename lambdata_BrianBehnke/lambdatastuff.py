def mean(nums):
  return sum(nums) / len(nums)

def sqrt(n):
  return n ** 0.5

def variance(nums):
  return sum((x - mean(nums)) ** 2 for x in nums) / (len(nums) - 1)   # change n to n-1 here

def stdev(nums):
  return sqrt(variance(nums))
  
def corrcoef(x, y):
  # r = 1/(n-1) * sum( ((x_i - x_)/S_x)((y_i - x_)/S_y)
  X, Y = mean(x), mean(y)
  return (1/(len(x)-1)) * sum( ((x[i] - X) / stdev(x)) * ((y[i] - Y) / stdev(y)) for i in range(int(len(x))) )
  
def lr_least_squares(d):
  # return in as "m, b" format
  x = [n[0] for n in d]
  y = [n[1] for n in d]
  x_sd, y_sd = stdev(x), stdev(y)
  r = corrcoef(x, y)
  m = r * (y_sd / x_sd)
  # for b:  mean(y) = m * mean(x) + b
  b = mean(y) - m * mean(x)
  return round(m, 2), round(b, 2)