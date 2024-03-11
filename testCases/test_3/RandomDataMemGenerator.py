import random
import sys


random_numbers = [random.randint(0, 255) for _ in range(int(sys.argv[1]))]
formatted_strings = [f"{i}: {random_numbers[i]};" for i in range(len(random_numbers))]
formatted_string = "\n".join(formatted_strings)

with open('data_mem_3.txt', 'w') as f:
    f.write('''# The initial content of the data memory
# The format is: <data mem. address>: <memory value>;
# All numbers are decimal''')
    f.write('\n\n')
    f.write(formatted_string)

print(formatted_string)
