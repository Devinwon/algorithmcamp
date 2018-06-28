#include <bits/stdc++.h>
using namespace std;

// ================= 代码实现开始 =================

/* 请在这里定义你需要的全局变量 */
const int N=500005;
vector<int> Set[N];

// 给定n个变量以及m个约束，判定是否能找出一种赋值方案满足这m个约束条件
// n：如题意
// m：如题意
// A：大小为m的数组，表示m条约束中的a
// B：大小为m的数组，表示m条约束中的b
// E：大小为m的数组，表示m条约束中的e
// 返回值：若能找出一种方案，返回"Yes"；否则返回"No"（不包括引号）。
string getAnswer(int n, int m, vector<int> A, vector<int> B, vector<int> E) {
    /* 请在这里设计你的算法 */
    //初始化

    int cnt=0;
    for (int i=0;i<m;++i)
        if(E[i]==1){
            swap(A[i],A[cnt]);
            swap(B[i],B[cnt]);
            swap(E[i],E[cnt]);
            ++cnt;
        }
    for (int i=0;i<m;++i)
    {
        if (E[i]==1){
            int ida=ID[a];
            int idb=ID[b];
            if(Set[ida].size()>Set[idb].size())
                swap(ida,idb);
            for(int j=0;j<int(set[ida].size()),++j){
                int c=Set[ida][j];
                Set[idb].push_back(c);
                ID[c]=idb;
            }
        Set[ida].clear();
        }
    }
    return "Yes";

}

// ================= 代码实现结束 =================

int main() {
    int T;
    for (scanf("%d", &T); T--; ) {
        int n, m;
        scanf("%d%d", &n, &m);
        vector<int> A, B, E;
        for (int i = 0; i < m; ++i) {
            int a, b, e;
            scanf("%d%d%d", &a, &b, &e);
            A.push_back(a);
            B.push_back(b);
            E.push_back(e);
        }
        printf("%s\n", getAnswer(n, m, A, B, E).c_str());
    }
    return 0;
}
