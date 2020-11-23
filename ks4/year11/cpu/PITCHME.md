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

##Clock Speed
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

##Von Neumann

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
- MAR, Memory Address Register
- MDR - Memory Data Register
@ol
## Never forget the ALU
@ol
- Its the only one not a register
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

## Task

Complete the supplied example exam question

---
[drag=100, drop=center, flow=col]

##Plenary

Think about the following questions for 3 minutes, then be prepared to feedback to the class:

- How do more cores  improve performance?
- What is faster, RAM or Cache?
- Name two registers in the Von Neumann architecture
- Name a part of the Von Neumann architecture that is not a register?
-