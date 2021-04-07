#include<bits/stdc++.h>

using namespace std;

long long  get_x(long long  n,long long  m, long long  x){
    //from_bycolumns
    long long  row,column;
    row = x%n== 0 ? n : x%n;
    column = (x+n-row)/n;
    //byrows
    return (row-1)*m+column;
};

int main(){
    long long  t,n,m,x;
    cin>>t;
    while(t--){
        cin>>n>>m>>x;
        cout<<get_x(n,m,x)<<"\n";
    }
}