// passed 60%
#include <stdio.h>
#include <math.h>
typedef struct point{
    int x;
    int y;
    int id;
} Point;

Point ps[100005];

void swap(Point* p1, Point* p2){
    Point temp = {p1->x, p1->y, p1->id};
    p1->x = p2->x; p1->y = p2->y; p1->id = p2->id;
    p2->x = temp.x; p2->y = temp.y; p2->id = temp.id;
}

int Where(Point P, Point Q, Point S){
    return P.x * Q.y - P.y * Q.x
        + Q.x * S.y - Q.y * S.x
        + S.x * P.y - S.y * P.x;
}

int main(void){
    int n;
    scanf("%d", &n);
    int nodes = 0;
    for(int i = 0; i < n; i++){
        scanf("%d %d", &ps[i].x, &ps[i].y);
        ps[i].id = i+1;                    //由于i从0开始，序号比在数组中存储的位置要大1
    }

    Point ltl;
    ltl.id = ps[0].id, ltl.x = ps[0].x, ltl.y = ps[0].y;
    for(int i = 0; i < n; i++){            //找出ltl
        if(ps[i].y < ltl.y || (ltl.y == ps[i].y && ps[i].x < ltl.x))
            {ltl.x = ps[i].x, ltl.y = ps[i].y, ltl.id = ps[i].id;}
    }
    swap(&ps[0], &ps[ltl.id - 1]);
//    printf("%d %d\n", ps[0].id, ltl.id);
    int i;
    for(i = 0; i + 1< n; i++){        //类似于选择排序，每次选择后ps[i] ps[i+1]构成的边都是极边
        for(int j = 2; j + i < n; j++){
            if(Where(ps[i], ps[i + 1], ps[i + j]) < 0 ||        //如果在ps[i + j] 在右边
                (Where(ps[i], ps[i + 1], ps[i + j]) == 0        //如果ps[i], ps[i + 1] ps[i + j] 三点共线
                  && abs(ps[i + 1].x - ps[i].x) + abs(ps[i + 1].y - ps[i].y) >  //且ps[i+j]比较近
                  abs(ps[i + j].x - ps[i].x) + abs(ps[i + j].y - ps[i].y)))
                  swap(&ps[i + 1], &ps[i + j]);
        }
        if(Where(ps[i], ps[i+1], ps[0])<0)                    //出口，这时类似于蚊香一样往中间转去，但是发现第一个点在外面，跳出
            break;
    }
    int ret = i+1;
    n++;
    for(int j = 0; j <= i; j++)
        ret = ret * ps[j].id % n;
//        printf("%d ", ps[j].id);
    printf("%d", ret);
}
