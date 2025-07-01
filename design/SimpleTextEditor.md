````java
import java.io.*;
import java.util.*;

public class Solution {
    
    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner scanner = new Scanner(System.in);
        int nbQueries = Integer.parseInt(scanner.nextLine());
        
        SimpleTextEditor textEditor = new SimpleTextEditor();
        
        for (int iQuery = 0; iQuery<nbQueries; iQuery++) {
            String[] query = scanner.next().split(" ");
            for (String partQuery : query) 
                System.out.print(partQuery+" ");
            System.out.println();
            
            if (query.length < 1) throw new RuntimeException();
            switch(query[0]) {
                case "1":
                    verif2Parameters(query);
                    textEditor.append(query[1]);
                    break;
                case "2":
                    textEditor.delete(Integer.parseInt(query[1]));
                    verif2Parameters(query);
                    break;
                case "3":
                    System.out.println(textEditor.print(Integer.parseInt(query[1])));
                    verif2Parameters(query);
                    break;
                case "4":
                    if (textEditor.canUndo()) textEditor.undo();
                    else throw new RuntimeException();
                    break;
                default:
                    throw new RuntimeException();
            }
            
        }
    }
    
    private static void verif2Parameters(String[] s) {
        if (s.length < 2) throw new RuntimeException();
    }
    
    private static class SimpleTextEditor {
        
        private StringBuilder S;
        private Stack<String> undoStack;
        
        public SimpleTextEditor() {
            undoStack = new Stack<>();
            S = new StringBuilder();
        }
        
        public void append(String W) {
            undoStack.push(S.toString());
            S.append(W);
        }
        
        public void delete(int k) {
            undoStack.push(S.toString());
            if (S.length() - k < 0) S.delete(0, S.length()); // edge case
            S.delete(S.length() - k, S.length());
        }
        
        public char print(int k) {
            if (k > S.length() || k <= 0) throw new RuntimeException();
            return S.charAt(k-1);
        }
        
        public void undo() {
            S = new StringBuilder(undoStack.pop());
        }
        
        public boolean canUndo() {
            return undoStack.isEmpty() ? false : true;
        }
    }
    
    // empty String S
    // append(W) append String W at end
    // dekete(k) k last char            // What if delete too much (k>W.len())
    // print(k) print k-th char of S    // What if print too far (k > W.leng())
    // undo() of type 1/2 : reverting S to that state operation // what if nothing to undo 
}
````