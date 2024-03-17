# Instruction Set Architecture 
This is an Instruction Set Architecture simulator project that was created for 'Cyber Systems' course for Bsc. in General Engineering at Technical University of Denmark.

It includes 3 test cases, the third one was created by us. Run ```.\isa-sim.py``` file to use the project.

You can use ```.\testCases\test_3\MergeSort.py``` to compare the result from third test case.

## Authors (Group 25)

- Adrian Maciejewski
- Vebika Boulos 
- Jázmin Seregi

## Running test cases

To run the 1st test case run the following from the root of the project:

```bash
  python .\isa-sim.py 1000 .\testCases\test_1\program_1.txt .\testCases\test_1\data_mem_1.txt

```
The output should be:
```
Welcome to the ISA simulator! - Designed by <YOUR NAMES HERE>

Initializing data memory content from file.
Data memory initialized.

Initializing instruction memory content from file.
Instruction memory initialized.

---Start of simulation---


Register file content:
R0 = 0
R1 = 26
R2 = 9
R3 = 20
R4 = 2
R5 = 11
R6 = 9
R7 = 244
R8 = 0
R9 = 0
R10 = 0
R11 = 0
R12 = 0
R13 = 255
R14 = 255
R15 = 0

Data memory content (used locations only):
Address 0 = 11
Address 1 = 9
Address 2 = 20

Executes in 24 cycles.

---End of simulation---
```

To run the 2nd test case run the following from the root of the project:

```bash
  python .\isa-sim.py 1000 .\testCases\test_2\program_2.txt .\testCases\test_2\data_mem_2.txt
```
The output should be:
```
Welcome to the ISA simulator! - Designed by <YOUR NAMES HERE>

Initializing data memory content from file.
Data memory initialized.

Initializing instruction memory content from file.
Instruction memory initialized.

---Start of simulation---


Register file content:
R0 = 0
R1 = 19
R2 = 20
R3 = 1
R4 = 1
R5 = 8
R6 = 9
R7 = 20
R8 = 17
R9 = 20
R10 = 26
R11 = 0
R12 = 0
R13 = 0
R14 = 0
R15 = 0

Data memory content (used locations only):
Address 0 = 8
Address 1 = 9
Address 2 = 1
Address 3 = 2
Address 4 = 7
Address 5 = 6
Address 6 = 5
Address 7 = 3
Address 8 = 4
Address 9 = 0
Address 10 = 0
Address 11 = 1
Address 12 = 2
Address 13 = 3
Address 14 = 4
Address 15 = 5
Address 16 = 6
Address 17 = 7
Address 18 = 8
Address 19 = 9

Executes in 752 cycles.

---End of simulation---
```

To run the 3rd test case run the following from the root of the project:

```bash
  python .\isa-sim.py 1000000 .\testCases\test_3\program_3.txt .\testCases\test_3\data_mem_3.txt

```
The output should be:
```
Welcome to the ISA simulator! - Designed by <YOUR NAMES HERE>

Initializing data memory content from file.
Data memory initialized.

Initializing instruction memory content from file.
Instruction memory initialized.

---Start of simulation---


Register file content:
R0 = 0
R1 = 0
R2 = 100
R3 = 100
R4 = 99
R5 = 100
R6 = 0
R7 = 0
R8 = 0
R9 = 0
R10 = 29
R11 = 237
R12 = 17
R13 = 0
R14 = 0
R15 = 0

Data memory content (used locations only):
Address 0 = 3
Address 1 = 4
Address 2 = 19
Address 3 = 20
Address 4 = 31
Address 5 = 31
Address 6 = 34
Address 7 = 38
Address 8 = 40
Address 9 = 41
Address 10 = 41
Address 11 = 42
Address 12 = 43
Address 13 = 47
Address 14 = 51
Address 15 = 54
Address 16 = 55
Address 17 = 55
Address 18 = 58
Address 19 = 60
Address 20 = 63
Address 21 = 63
Address 22 = 63
Address 23 = 64
Address 24 = 65
Address 25 = 68
Address 26 = 72
Address 27 = 74
Address 28 = 81
Address 29 = 84
Address 30 = 86
Address 31 = 98
Address 32 = 104
Address 33 = 105
Address 34 = 106
Address 35 = 111
Address 36 = 114
Address 37 = 120
Address 38 = 120
Address 39 = 120
Address 40 = 120
Address 41 = 125
Address 42 = 126
Address 43 = 128
Address 44 = 128
Address 45 = 129
Address 46 = 134
Address 47 = 137
Address 48 = 141
Address 49 = 144
Address 50 = 144
Address 51 = 145
Address 52 = 149
Address 53 = 149
Address 54 = 152
Address 55 = 153
Address 56 = 157
Address 57 = 158
Address 58 = 159
Address 59 = 159
Address 60 = 159
Address 61 = 167
Address 62 = 168
Address 63 = 172
Address 64 = 175
Address 65 = 181
Address 66 = 185
Address 67 = 189
Address 68 = 190
Address 69 = 190
Address 70 = 191
Address 71 = 191
Address 72 = 192
Address 73 = 195
Address 74 = 196
Address 75 = 197
Address 76 = 206
Address 77 = 207
Address 78 = 209
Address 79 = 210
Address 80 = 210
Address 81 = 211
Address 82 = 212
Address 83 = 214
Address 84 = 216
Address 85 = 220
Address 86 = 220
Address 87 = 220
Address 88 = 220
Address 89 = 221
Address 90 = 221
Address 91 = 226
Address 92 = 227
Address 93 = 228
Address 94 = 230
Address 95 = 231
Address 96 = 231
Address 97 = 232
Address 98 = 235
Address 99 = 237

Executes in 51342 cycles.

---End of simulation---
```


You can generate new number to sort. The following script will replace data_mem_3.txt file with new numbers. 

```bash
  cd ..\..\
  python .\RandomDataMemGenerator.py 100
  cd .\testCases\test_3\
```