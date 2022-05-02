
def testKnapsack(W, wt, val, n):
  
    # Base Case
    if n == 0 or W == 0 :
        return 0
  
    # Check to see of the Weight of the nth Item Can Fit
    if (wt[n-1] > W):
        return testKnapsack(W, wt, val, n-1)
  
    # Return the Max of if the Item is or isn't Included
    else:
        return max(val[n-1] + testKnapsack(W-wt[n-1], wt, val, n-1),
                   testKnapsack(W, wt, val, n-1))
  

val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
print(testKnapsack(W, wt, val, n))