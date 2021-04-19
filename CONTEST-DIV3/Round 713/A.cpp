#include<bits/stdc++.h>

using namespace std;

int main(){
    int t,n,a,b=0,index;

    cin>>t;
    for(int i =0;i<t;i++){
        cin>>n;
        b = 0;
        int cnt=0;
        cin>>b;
        for(int j =0;j<(n-1);j++){
            cin>>a;
            if (b!=a){
                index = j+1;
                cnt +=1;
            }
            else{
                cnt = 0;
            }
            b=a;
        }
        if (cnt==1) index+=1;
        cout<<index<<endl;
    }

}