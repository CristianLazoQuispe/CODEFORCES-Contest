#include<bits/stdc++.h>

using namespace std;


int main(){
    int t;
    string a,b,c;

    cin>>t;
    while(t--){
        cin>>a>>b;
        bool init = false;
        int j = 0;

        if (a.length() > b.length()){
            swap(a, b); 
        }

        for(int i =0;i<a.length();i++){
            if (a[i]==b[j] & (!init)){
                init = true;
            }
        } 
        cout<< <<"\n";
    }
}