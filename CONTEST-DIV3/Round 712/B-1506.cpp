#include<bits/stdc++.h>

using namespace std;



int main(){
    int t,n,k,back,ans,last,ant;
    string s;
    bool init;
    cin>>t;
    while(t--){
        cin>>n>>k;
        cin>>s;
        init = false;
        back=0,ans=0,ant=0;
        last = 0;
        for (int i=0;i<n;i++){
            if(s[i]=='*'){
                last = i;
                if (!init){
                    back = i;
                    init = true;
                    ans+=1;
                }
                else{
                    if((i-back)>k){
                        ans+=1;
                        back=ant;// get the maximun j-i<=k
                    }
                }
                ant = i;
            }
        }
        if (last>back) ans+=1;

        cout<<ans<<"\n";
    }
}