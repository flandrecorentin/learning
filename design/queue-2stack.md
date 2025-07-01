````java
import java.io.*;
import java.util.*;

public class Solution {


    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */

        // queue // FIFO using two stack
        // enqueue : add new element at end of queue
        // dequeue : remove 

        // 1 x : add to queeu
        // 2   : dequee
        // 3   : print element at front of queue

        Scanner scanner = new Scanner(System.in);
        int nbQueries =Integer.parseInt(scanner.nextLine());

        Queue2Stacks queue = new Queue2Stacks();
        for (int i=0; i<nbQueries; i++) {
            String[] query = scanner.nextLine().split(" ");
            if (query.length == 0)
                throw new RuntimeException();
            if (query[0].equals("1")) {
                if (query.length == 1)
                    throw new RuntimeException();
                queue.offer(Integer.parseInt(query[1]));
            } else if (query[0].equals("2")) {
                queue.poll();
            } else if (query[0].equals("3")) {
                System.out.println(queue.peek());
            } else {
                throw new RuntimeException();
            }
        }
    }

    public static class Queue2Stacks {

        private Stack<Integer> temp;  // 
        private Stack<Integer> stack; // 28 14

        public Queue2Stacks() {
            this.temp = new Stack<>();
            this.stack = new Stack<>();
        }

        // O(1)
        public void offer(int val) {
            stack.push(val);
        }

        // worst O(N) // amortized O(1) 
        public void poll() {
            if (temp.isEmpty()) {
                while (!stack.isEmpty()) {
                    temp.push(stack.pop());
                }
            }
            temp.pop();
        }

        // worst O(N) // amortized O(1) 
        public int peek() {
            if (temp.isEmpty()) {
                while (!stack.isEmpty()) {
                    temp.push(stack.pop());
                }
            }
            return temp.peek();
        }
    }
}

````