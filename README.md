# Instruction Set Architecture 
This is an Instruction Set Architecture simulator project that was created for 'Cyber Systems' course for Bsc. in General Engineering at Technical University of Denmark.

It includes 3 test cases, the third one was created by us. Run ```.\isa-sim.py``` file to use the project.

You can use ```.\testCases\test_3\MergeSort.py``` to compare the result from third test case.

## Authors (Group 25)

- Adrian Maciejewski

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
