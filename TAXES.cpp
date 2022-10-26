#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int n,j;
	cin>>n;
	for(int i=0;i<n;i++)
	{ 
	    cin>>j;
	    if(j>100)
	      j=j-10;
	    cout<<j<<"\n";
	    
	}
	return 0;
}
