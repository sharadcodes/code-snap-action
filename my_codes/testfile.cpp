// CPP program to illustrate 
// working of erase() function 
#include <iostream> 
#include <vector> 
using namespace std; 

int main() 
{ 
	vector<int> myvector{ 1, 2, 3, 4, 5 }; 
	vector<int>::iterator it; 

	it = myvector.begin(); 
	myvector.erase(it); 

	// Printing the Vector 
	for (auto it = myvector.begin(); it != myvector.end(); ++it) 
		cout << ' ' << *it; 
	return 0; 
} 
