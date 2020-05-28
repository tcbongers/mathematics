memo = {}

def count_ways(target, coins):
	memo_string = str(target) + ' ' + str(len(coins))
	if memo_string in memo:
		return memo[memo_string]
		
	if target < 0:
		memo[memo_string] = 0
		return 0
	
	if target == 0:
		memo[memo_string] = 1
		return 1
	
	ways = 0
	for coin_index in range(len(coins)):
		ways += count_ways(target - coins[coin_index], coins[0:coin_index + 1])
		
	memo[memo_string] = ways
	return ways
	
#coin_list = range(1, 100)
#for k in range(100, 101):
#	print(f'Target {k}, number of ways = {count_ways(k, coin_list)}')

#coin_list = [2, 3, 5, 6]
#target = 10
coin_list = [1, 2, 3]
target = 4
print(count_ways(target, coin_list))