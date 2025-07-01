# Problem 

Given an array of integers, where all elements but one occur twice, find the unique element.

# Example

From [1, 2, 4, 3, 3, 2, 1]
, the unique element is 4

# Incremental resolution

### 1. Double iteration 

O(n^2) time and O(1) memory

### 2. Sort property

- Sort
- Iterate every two, compare i and i+1

O(nlog(n)) time and O(1) memory

### 3. Set

- Add if does not contains. Remove if contains
- Last element in the set is the only one occured number

O(n) time and O(n) memory

### 4. Bit manipulation xor

- xor operator all res ^= i
- res should be the only occurenced number

O(n) time and O(1) memory

# Resources

[Hackerank problem](https://www.hackerrank.com/challenges/one-week-preparation-kit-lonely-integer/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-two)