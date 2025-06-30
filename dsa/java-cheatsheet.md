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
PriorityQueue<Integer> minHeap = new PriorityQueue<>(); // minimum by default
minHeap.peek()
minHeap.poll();
minHeap.offer(newSweetness);
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
````