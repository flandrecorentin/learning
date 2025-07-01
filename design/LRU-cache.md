`````java

class LRUCache {

    Map<Integer, Node> map; // we can access current capacity .size()
    Node head;
    Node tail;
    int maxCapacity;
    final boolean debug = true;

    public LRUCache(int capacity) {
        if (debug) System.out.println("capacity is "+capacity);
        map = new HashMap<>();
        maxCapacity = capacity;
        head = new Node();
        head.isDummy = true;
        tail = head;
    }
    
    // O(1) 
    public int get(int key) {
        if (debug) System.out.println("get(" + key+"): " + (map.containsKey(key) ? map.get(key).val : -1));
        return map.containsKey(key) ? map.get(key).val : -1;
    }
    
    // O(1) 
    public void put(int key, int value) {
        if (debug) System.out.println("put("+key+","+value+"): ");

        if (map.containsKey(key)) {
            // Update value
            Node node = map.get(key);
            node.val = value;
            map.put(key, node);  // Do I need to reput ?

            // Remove node from order
            Node prevNode = node.prev;
            Node nextNode = node.next;
            if (node == head) return;
            if (node == tail) tail = prevNode;
            prevNode.next = nextNode;
            nextNode.prev = prevNode;

            // Add node as head
            Node copyHead = head;
            head = node;
            node.next = copyHead;
            copyHead.prev = node;

            map.put(key, node); // Do I need to reput ?
        } else {
            if (map.size() == maxCapacity) {
                if(debug)System.out.println("Removing tail "+tail.key+"...");
                // Remove tail
                map.remove(tail.key);
                tail = tail.prev;
                tail.next = null;
            }
            // Add node as head
            Node node = new Node();
            node.val = value;
            node.key = key;
            Node copyHead = head;
            head = node;
            node.next = copyHead;
            copyHead.prev = node;

            // first add, need to remove dummy
            if (map.size() == 0 && tail.isDummy) {
                tail = node;
                node.next = null;
            }
            map.put(key, node);
        }

        if (debug) {
            System.out.print("List is ");
            Node printedNode = head;
            while (printedNode != null) {
                System.out.print(printedNode.val+", ");
                printedNode = printedNode.next;
            }
            System.out.print("  (tail is "+ tail.val+")");
            System.out.println("");
        }
    }

    public class Node{
        public Node next;
        public Node prev;
        public int val;
        public int key;
        public boolean isDummy;

        public Node() {
            next = null;
            prev = null;   
            isDummy = false;     
        }
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */
 `````