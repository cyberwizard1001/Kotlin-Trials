#include <iostream>
#include<string>
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
			T element;
			next=NULL;
			prev=NULL;

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
		if(n==0)
			return true;

		else
			return false;
		//@end-editable@
	}

	int size() {
	    //@start-editable@
	    return n;
	    //@end-editable@
	}

	bool insertLast(T x) {
	    //@start-editable@

		Node nnode = new Node(x);

		//empty list - add element at head and tail
		head = tail = nnode;

		//if it's not empty,
		tail.next->nnode;
		nnode.prev->tail;
		tail=nnode;

		n++;

		//@end-editable@
		return true;
	}

	T insertFirst(T x) {
	    //@start-editable@

		Node nnode = new Node(x);

		//empty list
		if(n==0)
		{
			head = nnode;
			tail = head;
		}

		//list is not empty - make new node
		//as head and move the rest

		head->prev=nnode;
		nnode->next=head;
		head = nnode;

		n++;

		//@end-editable@
		return x;
	}

	T deleteLast() {
	    //@start-editable@

		//empty list - print error
		if(head == NULL){
            cout << "Linked List Empty Exception";
        }

		//single element - make everything null
		else if(head->next==NULL)
		{
			head = tail = NULL;
			n--;
		}

		//else, remove appropriate connects and replace tail with tail->prev
		else {
			
			Node del = tail;
			tail->prev->next=NULL;
			tail=tail->prev;
			tail->next=NULL;
			delete del;
			n--;
		}

		//@end-editable@
		return x;


	}

	T deleteFirst() {
	    //@start-editable@

		//empty list - print error
		if(head == NULL){
            cout << "Linked List Empty Exception";
        }

		//single element
		else if(n==1)
		{
			head = tail = NULL;
			n--;
		}

		else{

			Node del = head;
			head->next->prev=NULL;
			head = head->next;
			delete del;
			n--;
		}



		//@end-editable@
		return x;
	}

	//insert a node with value u after the node containing value v
    T insertAfter(T u,T v){

		Node nnode = new Node(x);

		bool flag = false;
		Node tnode = head;
		
		while((flag==true)&&(tnode->next!= NULL))
		{
			if(tnode.element!=u)
				tnode=tnode->next;

			else
				flag=true;
		}

		if(flag==true)
		{
			nnode->next=tnode->next;
			nnode->prev=tnode;
			tnode->next->prev=nnode;
			tnode->next=nnode;
			n++;
		}

		else
		{
			cout << "Find exact error statement";
		}

    	return true;
    }


    //insert a node with value u before the node containing value v

    T insertBefore(T u,T v){

		Node nnode = new Node(x);

		bool flag = false;
		Node tnode = head;
		
		while((flag==true)&&(tnode->next!= NULL))
		{
			if(tnode.element!=u)
				tnode=tnode->next;

			else
				flag=true;
		}

		if(flag==true)
		{
			tnode=tnode->prev;

			nnode->next=tnode->next;
			nnode->prev=tnode;
			tnode->next->prev=nnode;
			tnode->next=nnode;
			n++;
		}

		else
		{
			cout << "Find exact error statement";
		}

    	return true;
    }

    //delete the node after the node containting value u
    T deleteAfter(T u){

		Node tnode = head;

		flag = false;

		while((!flag)&&(tnode->next!=NULL))
		{
			
		}

    }

	//delete the node before the node containting value u
    T deleteBefore(T u){

    }

    T getHead() {

    }

    T getTail() {

    }

    Node* findNode(T val){
    	return temp;
    }

    //swap the nodes containing u and v
    void swap(T u,T v){

    	return true;
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
			*temp = tail;
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

//Driver Code
int main(){
	DLList<int> dlist1;
 	string noOfInputs,str;
 	getline(cin, noOfInputs);
 	for(int i=0;i<stoi(noOfInputs);i++){
 	    getline(cin, str);

 	    if (str.substr(0, 2) == "IF"){
 	        int value = stoi(str.substr(3, 5));
 	        dlist1.insertFirst(value);
 	        dlist1.printlist();
 	    }
 	    else if (str.substr(0, 2) == "IL"){
 	        int value = stoi(str.substr(3, 5));
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
 	    if (str.substr(0, 2) == "IA"){
 	        int value1 = stoi(str.substr(3, 5));
 	        int value2 = stoi(str.substr(6, 8));
 	        dlist1.insertAfter(value1,value2);
 	        dlist1.printlist();
 	    }
 	    else if (str.substr(0, 2) == "IB"){
 	        int value1 = stoi(str.substr(3, 5));
 	        int value2 = stoi(str.substr(6, 8));
 	        dlist1.insertBefore(value1,value2);
 	        dlist1.printlist();
 	    }
		if (str.substr(0, 2) == "DA"){
 	        int value = stoi(str.substr(3, 5));
 	        dlist1.deleteAfter(value);
 	        dlist1.printlist();
 	    }
 	    else if (str.substr(0, 2) == "DB"){
 	        int value = stoi(str.substr(3, 5));
 	        dlist1.deleteBefore(value);
 	        dlist1.printlist();
 	    }
 	    else if (str.substr(0, 1) == "S"){
 	       cout<< dlist1.size()<<endl;
 	    }
 	    else if (str.substr(0, 1) == "F"){
 	       cout<< dlist1.getHead()<<endl;
 	    }
 	    else if (str.substr(0, 1) == "L"){
 	       cout<< dlist1.getTail()<<endl;
 	    }
 	    else if (str.substr(0, 4) == "FIND"){
 	       int value1 = stoi(str.substr(5, 7));
 	       DLList<int> :: Node *temp = dlist1.findNode(value1);
 	       cout<<temp->element<<endl;
 	    }
 	    else if (str.substr(0, 2) == "SW"){
 	       int value1 = stoi(str.substr(3, 5));
 	       int value2 = stoi(str.substr(6, 8));
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
