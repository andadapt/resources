[drag=100, drop=center, flow=col]

## Starter
Answer the following questions on your MWB:

- Name two network topologies
- What address does a switch use?
- What address does a router use?


---
[drag=100, drop=center, flow=col]

## CPU Performance
### Von Neumann

**Aspire to:**
Understand the complete Von Neumann FDE cycle
**Challenge to:**
Identify three performance metrics of the CPU and 2 registers of Von Neumann architecture
---

[drag=100, drop=center, flow=col]

## CPU Performance

@ol
- Clock speed
- Number of cores
- cache
@ol

---

[drag=100, drop=center, flow=col]

## Clock Speed
@ol
- Measured in Hz
- 1 Hz = 1 fetch, decode, execute (FDE) cycle a second
- 1Mhz = 1 Million (FDE) cycles a second
- 1 GHz = 1 billion f(FDE) cycles a second
@ol

---

[drag=100, drop=center, flow=col]

## Number of cores

@ol
- Increasing the core count increases the (FDE) cycles per second
- As FDE cycles can be run simultaneously
- 2 core at 1Hz, can do 2 (FDE) cycles per second
- 2 cores at 2 Hz, 4 (FDE) cycles per second
- Software needs to be written to take advantage of all cores
- Some software such as games are very single core dependant 
@ol


---

[drag=100, drop=center, flow =col]

## Cache

@ol
- Cacheform of memory, stores data and instructions
- cache is faster than RAM
- Cache 1ms Vs RAM 1000ms
@ol
---
[drag=100, drop=center, flow=col]

## Task

**Complete the CPU performance worksheet**


### Extension

What are the common CPU architectures?

---
[drag=100, drop=center, flow=col]

## Von Neumann

Von Neumann architecture is the design upon which many general purpose computers are based. 

The key elements of Von Neumann architecture are: 
@ol
- data and instructions are both stored as binary . 
- data and instructions are both stored in main memory.
@ol
---
[drag=100,drop=center flow=col]

## Fetch, Decode, Execute cycle

@ol
- Step 1 - the Program Counter (PC) is set to 0.
- Step 2 - the PC passes the address of the next instruction to be fetched to the Memory Address Register (MAR)
- Step 3 - the MAR sends a request for the data in the memory address it holds to be fetched and placed in the Memory Data Register (MDR).
- Step 4 - once the data has been fetched, the Program Counter (PC) is incremented by 1. This is the fetch stage complete.
- Step 5 - the Control Unit, now decodes the instruction in the MDR and works out what to do.
- Step 6 - the instruction is then executed. In this example, the instruction is to load the contents of memory address 4 to the ALU. This is the FDE cycle complete.
- The CPU now repeats the FDE cycle again. The first step is moving the contents of the PC to the MAR.
@ol

---
[drag=100, drop=center, flow=col]
## Refine & Revise

the important bit is remembering two registers..

## 2 registers to remember
@ol
- MAR // memory address register   Stores the address where data will be read
- MDR memory data register, stores the data that is read from memory
- PC -  Program counter, Stores the address of next instruction to be run
- AC -  Accumulator  , stores the result of calculations
- CIR - Current Instruction Register, , holds instructions current being executed
@ol

## Never forget the ALU
@ol
- Its not a register!
- ALE = Arithmetic Logic Unit, its where all the math happens!
- this often comes up
@ol

---
[drag=100, drop=center, flow=col]

## Learning brilliance

Together lets build a picture to remember

or

A fun mnemonic 

---
[drag=100, drop=center, flow=col]

### Von Neumann The counting robot!

@ol
- Von the shiny ALUminium bot.
- Likes counting, he keeps track  of his next instruction on his program counter.
-  and stores his results in his accumulator
@ol


---
[drag=100, drop=center, flow=col]

## Task
**Complete the following exam based questions**

---
[drag=100, drop=center, flow=col]

## Question 1:


Alicia has designed a computer using Von Neumann architecture. 

a -  Describe the purpose of two registers that are used by Von Neumann architecture. (4 marks)

@ol
- MAR // memory address register   Stores the address where data will be read
- MDR memory data register, stores the data that is read from memory
- PC -  Program counter, Stores the address of next instruction to be run
- AC -  Accumulator  , stores the result of calculations
-  CIR - Current Instruction Register, , holds instructions current being executed
@ol

---
[drag=100, drop=center, flow=col]

## Question 1

b -  The CPU has a clock speed of 3.8GHz. Describe what is meant by a clock speed of 3.8GHz. (2 marks)

@ol
- Number of FDE cycles per second
- 3.8 billion cycles per second
@ol

---
[drag=100,drop=center, flow=col]

## Question 1

c -  Alicia says: “My computer has a quad-core processor, so it will run twice as fast as a computer with a dual-core processor.” Explain why this statement is not always true. (3 marks)


@ol
- Software may be designed to run on 1 core and not multiple cores // depends on the task(s)  
- …some tasks cannot be split across cores  Clock speed also affects speed // dual core may have a faster clock speed // quad-core may have slower clock speed  
- ….so one task may be run faster/slower  
- RAM size also affects speed // Quad-core may have less RAM // amount of VM being used  
- Cache size also affects speed // Quad-core may have less cache
@ol
---
[drag=100, drop=center, flow=col]

## Plenary

Think about the following questions for 3 minutes, then be prepared to feedback to the class:

- How do more cores  improve performance?
- What is faster, RAM or Cache?
- Name two registers in the Von Neumann architecture

