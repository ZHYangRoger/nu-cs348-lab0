def quick_sort(lst):
    if len(lst) < 2:
        return lst
    smaller, same, larger = [], [], []
    pv = lst[len(lst)//2]
    for n in lst:
        if n > pv:
            larger.append(n)
        elif n < pv:
            smaller.append(n)
        else:
            same.append(n)
    return quick_sort(smaller) + same + quick_sort(larger)

def order(data, stats):
#your code goes here
	data_len = len(data)
	if data_len == 1:
		stats[0], stats[1], stats[2] = data[0], data[0], data[0]
  
	sorted_data = quick_sort(data)
	for i in range(len(sorted_data)):
		data[i] = sorted_data[i]
	stats[0] = sum(data)//data_len
	if data_len%2 == 0:
		stats[1] = data[data_len//2 - 1]
	else:
		stats[1] = data[data_len//2]
	occurrence = {}
	for n in data:
		if n not in occurrence:
			occurrence[n] = 0
		else:
			occurrence[n] += 1
	max_n = []
	for k, v in occurrence.items():
		if v == max(occurrence.values()):
			max_n.append(k)
	stats[2] = min(max_n)
	return 0