def any7(nums):
    """Are any of these numbers a 7? (True/False)"""

    # YOUR CODE HERE 
    for num in nums:
        num = int(num)
        print(num)
        if num == 7:
            return(f"should be true, any7{nums}")
        
    return(f"should be false, any7{nums}")


print("should be true", any7([1, 2, 7, 4, 5]))
print("should be false", any7([1, 2, 4, 5]))
