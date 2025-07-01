class MinStack {
// There is improvement to mix both and use ony stack and
// a int as getMin() will be faster
// - only push/pop twice when it's the new mini
// (update mini if new mini pushed)
// (update mini with a peek if min is poped)


    // O(N) -> O(2N) for the new minstack
    private Stack<Integer> stack;
    private Stack<Integer> minStack;
    private static final boolean DEBUG = true;

    public MinStack() {
        this.stack = new Stack();
        this.minStack = new Stack();
    }
    
    public void push(int val) {
        if (DEBUG) System.out.println("push("+val+")");

        this.stack.push(val);
        if (this.minStack.isEmpty() || this.minStack.peek() >= val)
            this.minStack.push(val);
    }
    
    public void pop() {
        if (DEBUG) System.out.println("pop("+")");

        int popedValue = this.stack.pop(); // pop before depending on order
        if (popedValue == this.minStack.peek())
            this.minStack.pop();
    }
    
    public int top() {
        if (DEBUG) System.out.println("top("+")");
        
        return this.stack.peek();
    }
    
    public int getMin() {
        if (DEBUG) System.out.println("getMin("+")");

        return this.minStack.peek();
    }
}

/**
* Your MinStack object will be instantiated and called as such:
* MinStack obj = new MinStack();
* obj.push(val);
* obj.pop();
* int param_3 = obj.top();
* int param_4 = obj.getMin();
  */