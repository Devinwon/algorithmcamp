#include <bits/stdc++.h>
using namespace std;

stack<int> sorting(stack<int>);

int main() {
    int n;
    cin >> n;
    stack<int> myStack;
    for (int i = 0; i < n; ++i) {
        int tmp;
        cin >> tmp;
        myStack.push(tmp);
    }
    stack<int> result = sorting(myStack);
    vector<int> answer;
    while (!result.empty()) {
        answer.push_back(result.top());
        result.pop();
    }
    for (auto i = answer.rbegin(); i != answer.rend(); ++i)
        cout << *i << endl;
    return 0;
}

// myStack：输入栈，栈中的所有元素即是待排序的元素
// 返回值：输出栈，即排序后的序列，满足从栈底至栈顶为升序
stack<int> sorting(stack<int> myStack) {
    /* 请在这里设计你的算法！ */
}