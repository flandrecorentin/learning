# Java List

````java
Collections.sort(list);
list.add(val); 
list.add(index, newVal);
list.set(index, replaceElement));

// Transform a int[] to a List<Integer> quickly
List<Integer> list  = Arrays.stream(res)
                             .boxed() // wrapper int => Integer
                             .collect(Collectors.toList());
````

# Java String

````java
str.length();
str.charAt(i);

String str = new String(charArray);
char[] charArray = str.toCharArray();
Character.isUpperCase(c);
Character.isLowerCase(c);
````

# Java Map

````java

containsKey(key)
containsValue(value)
values()
entrySet()
values() // return Set<Map<K,V>> // for (entrySet : map.entrySet()) getKey(), getValue
put(key, value)
remvve(key) // remove(key, value) // remove only if the key mapped with value
getOrDefault(key, val)
````

# Java Set

`````java
Set<Integer> set = new HashSet<Integer>();
set.add(i);
set.remove(i);
set.contains(i);
set.iterator().next(); // to get the first value
`````

# Java stack and queue

````java
// implementation can be Stack and LinkedList

Stack<Integer> lifo = new Stack<>(); // push pop peek
Queue<Integer> fifo = new LinkedList<>(); // offer poll peek
````

# Java Integer/Double

````java
int i = Integer.parseInt(str);
String str = Integer.toString(number);
````

# Java Arrays

`````java
int[] numbers
Arrays.fill(numbers, val);
Arrays.sort(numbers)
`````

# Java read from input standard

````java
Scanner scanner = new Scanner(System.in);
String inputLine = scanner.nextLine(); // Integer.parseInt(scanner.nextLine()) if int
String[] numbers = inputLine.split(" "); // if contains space or space

scanner.nextInt();
scannner.nextLine();

scanner.close();
````

# PriorityQueue 

````java
// binary heaps
PriorityQueue<Integer> minHeap = new PriorityQueue<>(); // minimum by default
minHeap.peek()
minHeap.poll();
minHeap.offer(newSweetness);

// can be represented as array using traversal method
// children 2i+1 and 2i+2
// parent (i-1)/2

// insertion O(logN)
// deletion O(logN)
// peek O(1)
// heapify O(N) 

````

# BFS/DFS recusirve/fifo/lifo

````java

````

# Backtracking

````java
// return all combinations of size k numbers between 1<=n([1, 2, 10.., n])
public static void main(String[] args) {
    List<List<Integer>> ans = new ArrayList<>();
    backTrack(ans, new ArrayList<>(), 1, n, k);
    return ans;
}

public void backTrac(List<List<Integer>> ans, List<Integer> tmp, int start, int n, int k) {
    if (temp.size()==k) ans.add(new ArrayList<>(temp)); // condition to stop backtrack
    else {
        for (int i=start; i<n; i++) { // Cover other possibilities from start
            tmp.add(i);
            backTrac(ans, tmp, start+(1), n, k);
            tmp.remove(i);  
        }
    }
}

````

# Binary search

````java
public static int binarySearch(int[] array, int target) {
    int left = 0;
    int right = array.length - 1;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        // Check if the target is present at mid
        if (array[mid] == target) {
            return mid;
        }
        if (array[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }

    // Target is not present in the array
    return -1;
}
````

# Java basics / bit manipulation

````java
// from int, long, short, char and byte
and &
or |
xor ^
not ~
<< 1 shift-left // *2
>> 1 shift-right // /2
>>> 1 // comp 2???

switch (day) {
    case 1:
        dayName = "Monday";
        break;
    case 2:
        dayName = "Tuesday";
        break;
    default:
        dayName = "Invalid day";
}
````

# Java Math

````java
logA(X)=logB(X)/logB(A);

// Find all prime number until n (not best best way)
// O(n*sqrt(n)) // 2,3,5,7
for (int n = 2; n<N; n++) {
    boolean isPrime = true;
    for (int i = 2; i <= Math.sqrt(n); i++) {
        if (n % i == 0) { isPrime = false;}
    }
    if (isPrime) primeSet.add(n);
}
````