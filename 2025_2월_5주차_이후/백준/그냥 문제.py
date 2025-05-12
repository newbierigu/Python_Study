# Target : 11
# nums: [2,5,7,9]
# Target: 11
# nums배열에서 target숫자를 만들 수 있는 nums의 index찾기


nums = [2, 5, 7, 9]
Target = 11

for i in range(len(nums)):
    for j in range(i +1, len(nums)):
        if nums[i] + nums[j] == Target:
            print(i, j)






    
        