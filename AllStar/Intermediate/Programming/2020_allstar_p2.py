

line = input()
sline= sorted(line)
line = list(line)

begin = 0
end   =len(line)
end_pos = end
swap_cnt =0

while True:
    #find min
    is_sorted = True
    for index in range(begin,end):
        if sline[index] != line[index]:
            begin = index
            is_sorted = False
            break

    if not is_sorted:
        min_v  = line[begin]
        min_pos= begin
        for index in range(begin+1,end):
            if sline[index] != line[index]:        
                if line[index]< min_v:
                    min_v= line[index]
                    min_pos = index

        if begin!=min_pos:
            swap_cnt += 1
            line[begin],line[min_pos] = line[min_pos],line[begin]                
            print("min: swap ", line[begin], line[min_pos],begin,min_pos,"result:",line, " cnt=", swap_cnt)        
    else:
        break

    #find max
    is_sorted = True
    begin_pos = begin +1

    #  for index in range(begin_pos,end_pos):
    #     if sline[index] != line[index]:
    #         begin_pos = index
    #         is_sorted = False
    #         break 

    for end_pos in range(end_pos-1,begin_pos,-1):
         if sline[end_pos] != line[end_pos]:
             is_sorted = False
             break
    end_pos +=1          
             

    if not is_sorted:
        max_v  = line[begin_pos]
        max_pos= begin_pos
        for index in range(begin_pos+1,end_pos):
                if line[index] >= max_v:
                    max_v= line[index]
                    max_pos = index
        if  line[end_pos-1] != line[max_pos]:          
            swap_cnt += 1
            line[end_pos-1],line[max_pos] = line[max_pos],line[end_pos-1]                
            print("max: swap ", line[max_pos], line[end_pos-1], max_pos,end_pos-1,"result:",line, " cnt=", swap_cnt)   
            print()
        else:
            continue     
        end_pos -=1        
    else:
        break        

print(swap_cnt)