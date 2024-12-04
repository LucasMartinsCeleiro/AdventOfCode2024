# Day 4: Ceres Search : Part 1

## Puzzle instructions

"Looks like the Chief's not here. Next!" One of The Historians pulls out a device and pushes the only button on it. After a brief flash, you recognize the interior of the Ceres monitoring station!

As the search for the Chief continues, a small Elf who lives on the station tugs on your shirt; she'd like to know if you could help her with her word search (your puzzle input). She only has to find one word: XMAS.

This word search allows words to be horizontal, vertical, diagonal, written backwards, or even overlapping other words. It's a little unusual, though, as you don't merely need to find one instance of XMAS - you need to find all of them. Here are a few ways XMAS might appear, where irrelevant characters have been replaced with .:

```	
..X...
.SAMX.
.A..A.
XMAS.S
.X....
```
The actual word search will be full of letters instead. For example:
```	
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
```	
In this word search, XMAS occurs a total of 18 times; here's the same word search again, but where letters not involved in any XMAS have been replaced with .:
```	
....XXMAS.
.SAMXMS...
...S..A...
..A.A.MS.X
XMASAMX.MM
X.....XA.A
S.S.S.S.SS
.A.A.A.A.A
..M.M.M.MM
.X.X.XMASX
```	
Take a look at the little Elf's word search. How many times does XMAS appear?

## Step to complete the puzzle

1. **Step 1**: Read the input data and load it as a list of strings.
2. **Step 2**: Implement a function to search for the word `XMAS` in all possible directions.
3. **Step 3**: Count the number of times the word `XMAS` appears in the word search.
4. **Step 4**: Return the total count of the word `XMAS` in the word search.

# Day 4 : Ceres Search : Part 2

## Puzzle instructions

The Elf looks quizzically at you. Did you misunderstand the assignment?

Looking for the instructions, you flip over the word search to find that this isn't actually an XMAS puzzle; it's an X-MAS puzzle in which you're supposed to find two MAS in the shape of an X. One way to achieve that is like this:

M.S
.A.
M.S
Irrelevant characters have again been replaced with . in the above diagram. Within the X, each MAS can be written forwards or backwards.

Here's the same example from before, but this time all of the X-MASes have been kept instead:

```	
.M.S......
..A..MSMS.
.M.S.MAA..
..A.ASMSM.
.M.S.M....
..........
S.S.S.S.S.
.A.A.A.A..
M.M.M.M.M.
..........
```	

In this example, an X-MAS appears 9 times.

Flip the word search from the instructions back over to the word search side and try again. How many times does an X-MAS appear?

## Step to complete the puzzle

1. **Step 1**: Read the input data and load it as a list of strings.
2. **Step 2**: Implement a function to search for the word `MAS` in all possible directions.
3. **Step 3**: Count the number of times the word `MAS` appears in the word search.
4. **Step 4**: Return the total count of the word `MAS` in the word search.
