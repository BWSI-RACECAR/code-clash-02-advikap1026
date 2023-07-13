class Solution:    
    def digitdecrypt(self, num):
            #type num: int
            #return type: int
            
            #TODO: Write code below to returnn an int with the solution to the prompt.
            tens = 10 
            sum = 0
            arr = [char for char in nums]
            for i in range(9):
                while arr.len != 1:
                     for i in range(arr.len):
                        
                        sum += arr[i]
                        
                return sum 
            pass
 
def main():
    input1= input()
    input2 = int(input1)

    
    tc1 = Solution()
    ans = tc1.digitdecrypt(input2)
    print(ans)
    
if __name__ == "__main__":
    main()