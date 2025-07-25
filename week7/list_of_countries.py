countries = []
'''
#Learn dimensions of arrays of strings
1. One dimension array or vector (#One list)
2. Two dimension array or matrix( #Two lists (list within a list)]
3. Three dimensional array or Tensor ( #Three lists within a list)
4. N-dimensional (ND) Array: NumPy arrays can have an arbitrary number of dimensions. The ndim attribute of a NumPy array returns the number of dimensions, and the shape attribute returns a tuple indicating the size of e dimension
countries[0] = "Spain"

slice must always come from something
'''
countries =["Spain", "Malawi", 'Iran', "USA"]
details = countries[0:3] # slicing an array always returns the same datatype as the original place the slice is coming from as slice must always come from something
country1, country2 = countries[0:2] # unpacking using a slice
#print(details)
#print(country1)
#print(country2)

country1, *country2 = countries[0:3]
#print(country1)
#print(country2)
country1, *country2 = countries[:]
#print(country1)
#print(country2)
country1, *country2 = countries[::-2]
#print(country1)
#print(country2)
#args and kwags (read on this)
#variadic function
countries.remove(countries[0])
#print(countries)


accounts = [
	["1001", "Joy", "Savings", 1500],
	["1002", "David", "Current", 2000],
	 ["1003", "Ruth", "Savings", 1800]]
#1. Remove the account of David
'''
#Method 1
davids_accounts = accounts[1]
accounts.remove(davids_accounts)
print(accounts)
'''
#learn DSA(deta structure) learn logic to use remove,sort,etc
#learn how to create a function that will do sort and remove.
#practice array this nights
#learn how to create a matrix

#Method 2
accounts.remove(accounts[1])
print(accounts) 

#2. Assign the name and account type of Ruth to two variables using multiple assignment
'''
#Method 1
ruths_account = accounts[1]
account_name, account_type = ruths_account[1:3]
print(account_name, account_type)
'''

#Method 2
name, type_account = accounts[1][1:3]
print(name, type_account)

#3. Use slicing to get only the name and account type of "Joy"
'''
#Method 1
joys_account = accounts[0]
name, account_type = joys_account[1:3]
print(name, account_type)
'''
#Method 2
joy_name, joy_account_type = accounts[0][1:3]
print(joy_name, joy_account_type)



