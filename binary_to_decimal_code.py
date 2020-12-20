binary_num = input("ENTER YOUR BINARY NUMBER : ")
parts = binary_num.split('.')

point = 2**(len(parts[0])-1)
part1 = []
for bit in parts[0]:
        part1.append(int(bit)*point)
        point=int(point*(1/2))
        
point = 1/2
part2 = []
for bit in parts[1]:
	part2.append(int(bit)*point)
	point = point*(1/2)



print(f"YOUR DECIMAL NUMBER IS: \n\t{sum(part1)+sum(part2)}")
