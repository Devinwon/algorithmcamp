#include <bits/stdc++.h>
using namespace std;

// ================= 代码实现开始 =================

const int M = 505, L = 1000005;

// c：trie树上的边，c[x][y]表示从节点x出发（x从1开始），字符为y的边（y范围是0到25）
// sz：sz[x]表示x节点的子树中终止节点的数量（子树包括x自身）
// cnt：trie树上节点的数目
int c[L][26], sz[L], cnt;

// 将字符串s加入到trie树中
// s：所要插入的字符串
void add(char *s) {
    /* 请在这里设计你的算法 */
    int x=0;
    for(;*s;++s){
        int y=*s-'a';   //将字符的范围变成0-25,分别对应a-z
        if(!c[x][y])    //若这个字符对应的边不存在,则需要新建一个节点
            c[x][y]=++cnt;
        x=c[x][y];  //接着沿着边往下走
    ++sz[x];  //此时x是中止节点
    }
    // ++sz[x];  //此时x是中止节点
}

// 用于计算sz数组
// x：当前节点

/*void dfs(int x) {

    for(int y=0;y<26;++y)
        int z = c[x][y];
        if(z!=0){
            dfs(z);         //递归下去
            sz[x]+=sz[z];       //怎么计算sz数组?
        }
}

//no dfs(),25行直接放在23for循环中 74,75delete

*/




// 用字符串s沿着trie树上走，找到相应的节点
// s：所给字符串
// 返回值：走到的节点
int walk(char *s) {
    /* 请在这里设计你的算法 */
    int x=0;
    for(;*s;++s){
        int y=*s-'a';
        if(!c[x][y])
            return 0;
        //x该如何变化?
        x=c[x][y];
    }
    return x;

}

// ================= 代码实现结束 =================

char s[M];

int main() {
    int n, m;
    scanf("%d%d", &n, &m);
    for (; n--;) {
        scanf("%s", s);
        add(s);
    }
/*    dfs(0);
    sz[0] = 0;*/
    for (; m--;) {
        scanf("%s", s);
        printf("%d\n", sz[walk(s)]);
    }
    return 0;
}
