import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.PrintWriter;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        InputReader in = new InputReader(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        Task solver = new Task();
        solver.solve(in, out);
        out.close();
    }

    static class Task {
        
        // myStack：输入栈，栈中的所有元素即是待排序的元素
        // 返回值：输出栈，即排序后的序列，满足从栈底至栈顶为升序
        Stack<Integer> sorting(Stack<Integer> myStack) {
            /* 请在这里设计你的算法！ */
        }

        void solve(InputReader in, PrintWriter out) {
            int n = in.nextInt();
            Stack<Integer> myStack = new Stack<>();
            while (!myStack.empty())
                myStack.pop();
            for (int i = 0; i < n; ++i) {
                int tmp = in.nextInt();
                myStack.push(tmp);
            }

            Stack<Integer> result = sorting(myStack);
            for (Integer x : result)
                out.println(x);
        }

    }

    static class InputReader {
        BufferedReader reader;
        StringTokenizer tokenizer;

        private InputReader(InputStream stream) {
            reader = new BufferedReader(new InputStreamReader(stream), 32768);
            tokenizer = null;
        }

        private String next() {
            while (tokenizer == null || !tokenizer.hasMoreTokens()) {
                try {
                    tokenizer = new StringTokenizer(reader.readLine());
                } catch (IOException e) {
                    throw new RuntimeException(e);
                }
            }
            return tokenizer.nextToken();
        }

        private short nextShort() {
            return Short.parseShort(next());
        }

        private int nextInt() {
            return Integer.parseInt(next());
        }

        private long nextLong() {
            return Long.parseLong(next());
        }

        private float nextFloat() {
            return Float.parseFloat(next());
        }

        private double nextDouble() {
            return Double.parseDouble(next());
        }
    }

}