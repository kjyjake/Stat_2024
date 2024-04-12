while True :
    height=list(map(int,input('Enter non-negative integers : ').split()))
    if min(height)<0:
        print("Please enter non-negative integers.")
    else:
        def water_trap(height:list[int]) -> int:
            if height == []:
                return 0
            else:
                water = 0
                l_index=0
                r_index=len(height)-1
                l_max=height[l_index]
                r_max=height[r_index]
                while l_index <= r_index:
                    if l_max <= r_max:
                        if height[l_index] > l_max:
                            l_max = height[l_index]
                        else:
                            water += (l_max - height[l_index])
                        l_index += 1
                    else:
                        if height[r_index] > r_max:
                            r_max = height[r_index]
                        else:
                            water += (r_max - height[r_index])
                        r_index -= 1
                return water
        print("Trapped water is", water_trap(height))
        break
