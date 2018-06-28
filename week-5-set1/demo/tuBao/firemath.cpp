// passed 50%
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<iostream>
using namespace std;
typedef long long ll;
const int N = 300005;
struct ip {
    int x, y, i;
    ip(int x = 0, int y = 0) : x(x), y(y), i(0) { }
    void ri(int _i) {
        scanf("%d%d", &x, &y);
        i = _i;
    }
};
bool operator < (const ip &a, const ip &b) {
    return a.x == b.x ? a.y < b.y : a.x < b.x;
}
ip operator - (const ip &a, const ip &b) {
    return ip(a.x - b.x, a.y - b.y);
}
ll operator ^ (const ip &a, const ip &b) {
    return (ll)a.x * b.y - (ll)a.y * b.x;
}
ip a[N], b[N];
bool to_Left(ip a, ip b, ip c) {
    return 0 <= a.x * b.y - a.y * b.x
             + b.x * c.y - b.y * c.x
             + c.x * a.y - c.y * a.x;
}
bool cmp(const ip& p, const ip & q) {
    return to_Left(a[0], p, q);         //以 a[0] 为参考点， 求 p, q的相对位置 
}
int convex(int n) {                         //Graham scan 
  int index = 0, top1 = 0, top2 = 0;
  sort(a + 1, a + n, cmp);                  // 按极角排序 
  for(int j = 0; j < n; ++j) {
    //printf("-->点%d: %d %d\n",a[j].i, a[j].x, a[j].y );
  }
  while(top1 < n) {
    if(top2 < 2 || to_Left(b[top2 - 2], b[top2 - 1], a[top1])) {    //满足条件，入栈 
		//printf("\t入栈-->点%d: %d %d\n",a[top1].i, a[top1].x, a[top1].y );
		b[top2++] = a[top1++];
      } else {                          //不满足条件 ，出栈 
        //printf("\t  Out-->点%d: %d %d\n",b[top2 - 1].i, b[top2 - 1].x, b[top2 - 1].y );
		b[top2--];
      }
  }
 /* */
  for(int j = 0; j < top2; ++j) {
    //printf("-->点%d: %d %d\n", b[j].i, b[j].x, b[j].y );
  }
  
  return top2;
}
int main() {
    int n, index = 0;
    ip temp;
    //freopen("sample2_input.txt", "r", stdin);
    scanf("%d", &n);
    for (int i = 0; i < n; ++i) {
        a[i].ri(i + 1);
        if(a[i] < a[index]) {
            index = i;
        }
    }
    temp = a[0];
    a[0] = a[index];
    a[index] = temp;    //求得 a[0] 为 LTL 

    int m = convex(n), ans = m;  

    for (int i = 0; i < m; ++i)
        ans = ((ll)ans * b[i].i) % (n + 1);
    printf("%d\n", ans);
    return 0;
}