#include <iostream>
#include<string>
#include <sstream>
using namespace std;

template<class T>
class DLList {
public:
	class Node {
	public:
		T element;
		Node *next;
		Node *prev;
		Node(T x) {
		    //@start-editable@
			element = x;
			next = NULL;
			prev = NULL;
			//@end-editable@
		}
	};
	Node *head;
	Node *tail;
	int n;
public:
	DLList() {
		n = 0;
		head = tail = NULL;
	}

	bool isEmpty(){
		//@start-editable@
		return (n==0);		
		//@end-editable@
	}

	int size() {
	    //@start-editable@
	    return n;	    
	    //@end-editable@
	}

	bool insertLast(T x) {
	    //@start-editable@
		Node * nnode = new Node(x);
		if (isEmpty())
		{
			head = tail = nnode;
		}
		else
		{
			tail->next = nnode;
			nnode->prev = tail;
			tail = nnode;	
		}
		n+=1;	
		//@end-editable@
		return true;
	}

	T insertFirst(T x) {
	    //@start-editable@
		Node * nnode = new Node(x);
		if(isEmpty()){
			head = tail = nnode;
		}
		else{
			nnode->next = head;
			head->prev = nnode;
			head = nnode;
		}
		n+=1;		
		//@end-editable@
		return x;
	}

	T deleteLast() {
	    //@start-editable@
		int x = 0;
		if (isEmpty())
		cout<<"List Empty"<<endl;
		else
		{
		     x = tail->element;
			if (n ==1)
			{
				Node* temp = head;
				head = tail = NULL;
				delete temp;
			}
			else
			{
			Node* temp = tail;
			tail->prev->next = NULL;
			tail = tail->prev;
			temp->prev = NULL;
			delete temp;
			}
			n -=1;			
		}		
		//@end-editable@
		return x;
		
		
	}

	T deleteFirst() {
	    //@start-editable@
		int x = 0;
		if (isEmpty())
		cout<<"List Empty"<<endl;
		if(!isEmpty()){
		    x = head->element;
			if(n==1){
				Node * temp = head;
				head = tail = NULL;
				delete temp;
			}
			else{
				Node * temp = head;
				head->next->prev = NULL;
				head = head->next;
				temp->next = NULL;
				delete temp;
			}
			n-=1;
		}		
		//@end-editable@
		return x;
	}

	//insert a node with value u after the node containing value v
    T insertAfter(T u,T v){
    	//@start-editable@
		if(!isEmpty()){
			if ((n == 1) &&(head->element == v )){
				insertLast(u);
				return true;
			}
			else{
				Node * curn = head;
				while(curn->next!=NULL)
				{
					if(curn->element == v)
					{
						Node*nnode = new Node(u);
						nnode->next = curn->next;
						nnode->prev = curn;
						curn->next->prev = curn->next= nnode;
						n+=1;
						return true;
					}
					curn = curn->next;
				}
				if (curn->element == v)
				{
					insertLast(u);
					return true;
				}
				else{
					cout<<"Node to insert after not found"<<endl;
					return true;
				}
				
			}
		}		
		//@end-editable@
    	return true;
    }
    

    //insert a node with value u before the node containing value v

    T insertBefore(T u,T v){
    	//@start-editable@
		if(!isEmpty()){
			if(head->element ==v){
				insertFirst(u);
				return true;
			}
			else{
				Node*curn = head->next;
				while(curn!=NULL){
					if(curn->element ==v){
						Node*nnode = new Node(u);
						nnode->next = curn;
						nnode->prev = curn->prev;
						curn->prev->next = nnode;
						curn->prev = nnode;
						n+=1;
						return true;
					}
					curn = curn->next;					
					}
				cout<<"Node to insert before not found"<<endl;
				}
		}		
		//@end-editable@
    	return true;
    }

    //delete the node after the node containting value u
    T deleteAfter(T u){
    	//@start-editable@
		Node*curn= head;
		if(n>1){
			while(curn->next->next!=NULL){
				if(curn->element==u){
					Node*temp = curn->next;
					curn->next = temp->next;
					temp->next->prev = curn;
					temp->next=temp->prev =NULL;
					int t = temp->element;
					delete temp;
					n-=1;
					return t;
				}
				curn=curn->next;
			}
			if (curn->element ==u){
				int t = curn->element;
				deleteLast();
				return t;
			}
		}
		return false;		
		//@end-editable@

    }
    
	//delete the node before the node containting value u
    T deleteBefore(T u){
    	//@start-editable@
		if(n>1){
			if(head ->next ->element==u)
			{	
				int t=head->element;
				deleteFirst();
				return t;
			}
			Node*curn = head->next->next;
			while(curn!=NULL){
				if(curn->element ==u){
					int t = curn->prev->element;
					Node*temp= curn->prev;
					curn->prev = temp->prev;
					temp->prev->next = curn;
					temp->next = temp->prev = NULL;
					delete temp;
					n-=1;
					return t;
				}
				curn=curn->next;
			}
		}
		return false;		
		//@end-editable@

    }

    T getHead() {
    	//@start-editable@
		return head->element;		
		//@end-editable@
    }

    T getTail() {
    	//@start-editable@
		return tail->element;
		//@end-editable@

    }

    Node* findNode(T val){
    	//@start-editable@
		cout<<"findnode";
		Node*curn = head;
		Node * temp;
		while(curn!=NULL)
		{
			if(curn->element==val){
				temp  = curn;
				//return curn;
			}
			curn = curn->next;
		}
    		//@end-editable@
    	return temp;
    }

    //swap the nodes containing u and v
    void swap(T u,T v){
    	//@start-editable@


		if(n>1){
		Node * curn = head;
		Node* a = NULL;
		Node* b = NULL;
		while(curn!=NULL){
			if(curn->element ==u){
				a = curn;
			}
			if(curn->element ==v){
				b = curn;
			}
			curn = curn->next;
		}
		if(a!=NULL && b!=NULL)
		{
			int temp = a->element;
			a->element = b->element;
			b->element = temp;
		}
		}
		
		//@end-editable
    }
     
	//Prints the list
	void printlist(){
		if (!isEmpty()) {
			Node *temp = head;
			while (temp != NULL) {
				cout << temp->element << "->";
				temp = temp->next;
			}
			cout << endl;
			temp = tail;
			while (temp != NULL) {
				cout << temp->element << "->";
				temp = temp->prev;
			}
			cout << endl;
			return;
		}
		cout << ("Linked List Empty Exception")<<endl;
	}

};

int getValue(string s, int pos) {
    istringstream iss(s);
    string temp;
    iss>>temp;
    iss>>temp;
    if(pos==1) {
        return stoi(temp);
    }
    else {
        iss>>temp;
        return stoi(temp);
    }
}
//Driver Code
int main(){
	DLList<int> dlist1;
 	string noOfInputs,str;
 	getline(cin, noOfInputs);
 	for(int i=0;i<stoi(noOfInputs);i++){
 	    getline(cin, str); 
 	    
 	    if (str.substr(0, 2) == "IF"){
 	        int value = getValue(str, 1);
 	        dlist1.insertFirst(value);
 	        dlist1.printlist();
 	    }
 	    else if (str.substr(0, 1) == "S"){
 	       cout<< dlist1.size()<<endl;
 	    }
 	    else if (str.substr(0, 2) == "IL"){
 	        int value = getValue(str, 1);
 	        dlist1.insertLast(value);
 	        dlist1.printlist();
 	    }
 	    else if (str.substr(0, 2) == "DF"){
 	        dlist1.deleteFirst();
 	        dlist1.printlist();
 	    }
 	    else if (str.substr(0, 2) == "DL"){
 	        dlist1.deleteLast();
 	        dlist1.printlist();
 	    }
 	    else if (str.substr(0, 2) == "IA"){
 	        int value1 = getValue(str, 1);
 	        int value2 = getValue(str, 2);
 	        dlist1.insertAfter(value1,value2);
 	        dlist1.printlist();
 	    }
 	    else if (str.substr(0, 2) == "IB"){
 	        int value1 = getValue(str, 1);
 	        int value2 = getValue(str, 2);
 	        dlist1.insertBefore(value1,value2);
 	        dlist1.printlist();
 	    }
		else if (str.substr(0, 2) == "DA"){
 	        int value = getValue(str, 1);
 	        dlist1.deleteAfter(value);
 	        dlist1.printlist();
 	    }
 	    else if (str.substr(0, 2) == "DB"){
 	        int value = getValue(str, 1);
 	        dlist1.deleteBefore(value);
 	        dlist1.printlist();
 	    }
 	    else if (str.substr(0, 1) == "F"){
 	       cout<< dlist1.getHead()<<endl;
 	    }
 	    else if (str.substr(0, 1) == "L"){
 	       cout<< dlist1.getTail()<<endl;
 	    }
 	    else if (str.substr(0, 4) == "FIND"){
 	       int value1 = getValue(str, 1);
 	       DLList<int> :: Node *temp = dlist1.findNode(value1);
 	       cout<<temp->element<<endl;
 	    }
 	    else if (str.substr(0, 2) == "SW"){
 	       int value1 = getValue(str, 1);
 	       int value2 = getValue(str, 2);
 	       dlist1.swap(value1,value2);
 	       dlist1.printlist();
 	    }
 	    else if (str.substr(0,1) == "I"){
 	        //cout<<slist1.isEmpty()<<endl;
 	        if(dlist1.isEmpty()){
 	            cout<<"True"<<endl;
 	        }
 	        else{
 	            cout<<"False"<<endl;
 	        }
 	    }
 	}
}