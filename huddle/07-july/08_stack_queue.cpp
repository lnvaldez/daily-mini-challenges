// 08. Pilas y colas: Implementa las operaciones básicas de una pila y/o una cola para 5 elementos.

#include <iostream>
#include <queue>
#include <stack>

using namespace std;

int main(){
	
	cout << "*** Queue ***" << endl;
	
	// Create priority queue
	priority_queue<int> q;
	
	// Add elements to queue
	q.push(55);
	q.push(40);
	q.push(35);
	q.push(20);
	q.push(60);
	
	// Print the top element of queue
	while (!q.empty()){
		cout << "Top: " << q.top() << endl;
		q.pop();
	}
	
	cout << "*** Stack ***" << endl;
	
	// Stack (pila)
	
	stack<int> s;
	
	s.push(36); 
	s.push(12);
	s.push(24);
	s.push(40);
	s.push(52);
	
	while(!s.empty()){
		cout << "Top: " << s.top() << endl;
		s.pop();
	}
	
	return 0;
}
