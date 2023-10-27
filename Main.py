def main():
  n = input("Please enter value of N:")
  if n < 0:
    raise Exception("Please provide positive value of N")
  # We will use Dynamic programming here
  cols = 4
  rows = n
  attendance = [[0]*cols]*(rows+1)
  attendance[0][0] = 1
  for i in range(1,n+1):
    attendance[i][0] = sum(attendance[i-1][:4])
    for j in range(1, cols+1):
      attendance[i][j] = attendance[i-1][j-1]
  
      
  
  

def __name__ == "__main__":
  main()
