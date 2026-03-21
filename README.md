# Data Structures Java
________________________________________
## 1. Array
-	Type: Fixed-size sequence
-	Access: arr[i]
-	Time Complexity:
  -	Access: O(1)
  -	Search: O(n)
  -	Insert/Delete (middle): O(n)
-	Use Cases: Prefix sums, sliding window, in-place rearrangement, sorting, two pointers.
________________________________________
## 2. List
#### ArrayList
-	Type: Dynamic array
-	Key Methods: add(), get(), set(), remove(), size()
-	Time Complexity:
  -	Access by index: O(1)
	- Add at end: O(1) amortized
  -	Remove/Insert in middle: O(n)
-	Use Cases: Random access, storing results, dynamic resizing.

#### LinkedList
-	Type: Doubly-linked list
-	Key Methods: addFirst(), addLast(), removeFirst(), removeLast(), get()
-	Time Complexity:
  -	Access by index: O(n)
  -	Insert/Delete at ends: O(1)
-	Use Cases: Queue, Deque, frequent insertions/deletions.
________________________________________
## 3. Set
#### HashSet
-	Type: Unordered, unique elements
-	Key Methods: add(), contains(), remove()
-	Time Complexity: O(1) average
-	Use Cases: Remove duplicates, check existence, fast membership.
#### TreeSet
-	Type: Sorted set
-	Key Methods: first(), last(), ceiling(), floor()
-	Time Complexity: O(log n)
-	Use Cases: Range queries, ordered traversal.
#### LinkedHashSet
-	Type: Ordered insertion set
-	Key Methods: same as HashSet
-	Time Complexity: O(1)
-	Use Cases: Maintain order while keeping uniqueness.
________________________________________
## 4. Map
#### HashMap
-	Type: Unordered key-value
-	Key Methods: put(), get(), containsKey(), remove()
-	Time Complexity: O(1) average
-	Use Cases: Counting frequencies, memoization, mapping relationships.
#### TreeMap
-	Type: Sorted map
-	Key Methods: firstKey(), lastKey(), ceilingKey(), floorKey()
-	Time Complexity: O(log n)
-	Use Cases: Ordered queries, range queries.
#### LinkedHashMap
-	Type: Maintains insertion order
-	Key Methods: Same as HashMap
-	Use Cases: LRU cache, maintain order of insertion.
________________________________________
## 5. Queue / Deque
#### Queue (LinkedList or ArrayDeque)
-	Type: FIFO
-	Key Methods: offer(), poll(), peek()
-	Time Complexity: O(1)
-	Use Cases: BFS, level order traversal.
#### Deque (ArrayDeque)
-	Type: Double-ended queue
-	Key Methods: addFirst(), addLast(), pollFirst(), pollLast(), peekFirst(), peekLast()
-	Time Complexity: O(1)
-	Use Cases: Sliding window max/min, monotonic queue, BFS with level tracking.
________________________________________
## 6. PriorityQueue (Min/Max Heap)
-	Type: Min-heap (default) or Max-heap (via comparator)
-	Key Methods: offer(), poll(), peek()
-	Time Complexity: O(log n) for insert/remove
-	Use Cases: Top-K problems, Dijkstra’s algorithm, interval scheduling.
________________________________________
## 7. Stack
-	Type: LIFO (can use Deque)
-	Key Methods: push(), pop(), peek()
-	Time Complexity: O(1)
-	Use Cases: DFS, balanced parentheses, monotonic stack problems.
________________________________________
## 8. Utilities
-	Arrays class: sort(), binarySearch(), fill(), copyOf()
-	Collections class: sort(), reverse(), swap(), max(), min()
-	Use Cases: Sorting, reversing, swapping elements in arrays/lists, binary search.
________________________________________
### Tips for LeetCode
1.	HashMap + HashSet cover 70–80% of problems needing frequency/count/existence checks.
2.	ArrayDeque > LinkedList for queue/stack operations; faster and cleaner.
3.	TreeMap / TreeSet only when you need sorted order or floor/ceiling operations.
4.	PriorityQueue is essential for top-k or interval problems.
________________________________________

