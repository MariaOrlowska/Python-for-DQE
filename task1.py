import random

# create list of 100 random numbers from 0 to 1000
random_numbers = [random.randint(0,1001) for _ in range(100)]

# sort list from min to max (without using sort())
def custom_sort(arr):
    for i in range(len(arr)):
        for j in range(i +1, len(arr)):
            if arr[i]> arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

sorted_numbers = custom_sort(random_numbers)


# creating lists for even and odd numbers
even_numbers = [num for num in sorted_numbers if num % 2 ==0]
odd_numbers = [num for num in sorted_numbers if num % 2 !=0]

# calculate average for even and odd numbers
even_avg = sum(even_numbers) / len(even_numbers)
odd_avg = sum(odd_numbers) / len(odd_numbers)

print(f'Average for even numbers: {even_avg}')
print(f'Average for odd numbers: {odd_avg}')





