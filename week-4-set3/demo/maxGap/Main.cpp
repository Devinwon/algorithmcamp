#include <bits/stdc++.h>
using namespace std;

// ================= 代码实现开始 =================

typedef unsigned int u32;

// 以下代码不需要解释，你只需要知道这是用于生成数据的就行了

u32 nextInt(u32 x) {
    x ^= x << 13;
    x ^= x >> 17;
    x ^= x << 5;
    return x;
}

void initData(u32* a, int n, int k, u32 seed) {
    for (int i = 0; i < n; ++i) {
        seed = nextInt(seed);
        a[i] = seed >> (32 - k);
    }
}

// 以上代码不需要解释，你只需要知道这是用于生成数据的就行了

/* 请在这里定义你需要的全局变量 */

const int N=67108864;

// a,输入中给定的数组
// l,每个桶中的最小值
// r,每个桶中的最大值
u32 a[N+1];
u32 l[N+1],r[N+1];

// 这是求解答案的函数，你需要对全局变量中的 a 数组求解 maxGap 问题
// n, k：意义与题目描述相符
// 返回值：即为答案（maxGap）
u32 maxGap(int n, int k) {
    /* 请在这里设计你的算法 */
    const int m=1<<26;      //桶的个数
    memset(l,-1,sizeof(int)*m);//将l中的所有位置赋值为-1
    memset(r,-1,sizeof(int)*m);//将r中的所有位置赋值为-1

    const int _k=max(k-26,0);//这是一个参数,辅助后续用位运算代替除法
    for(int i=0;i<n;++i){
        u32 b1=a[i]>>_k;    //(这个式子等价于a[i]除以2的_k次幂)求出a[i]所在的桶
        //更新对应桶的l,r;
        if( l[b1]==-1 )
           l[b1]=r[b1]=a[i] ;
        else if (a[i]<l[b1])
            l[b1]=a[i];
        else if (a[i]>r[b1])
            r[b1]=a[i];
    }
    //统计答案
    u32 last=a[0];
    u32 ans=0;
    for(int i=0;i<m;++i)
        if(l[i]!=-1   ){
            if(last>l[i])
                last=l[i];
            if ( l[i]-last >ans)
                ans= l[i]-last ;   //
            last=r[i];
        }
        return ans;
}

// ================= 代码实现结束 =================

int main() {
    int n, k;
    u32 seed;

    scanf("%d%d%u", &n, &k, &seed);
    initData(a, n, k, seed);

    u32 ans = maxGap(n, k);

    printf("%u\n", ans);
    return 0;
}
