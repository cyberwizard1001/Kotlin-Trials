#include <iostream>
#include<string>
using namespace std;

template<class T>
class SLList {
protected:
	class Node {
	public:
		T element;
		Node *next;
		Node(T x) {
		    //@start-editable@
            element = x;
            next = NULL;
			//@end-editable@
		}
		
	};
	Node *head;


public:
	SLList() {
	
		head =  NULL;
	}

	bool isEmpty(){
		//@start-editable@
        
		if(head==NULL)
        {
            return true;
        }

        else
            return false;
		//@end-editable@
	}

	int size() {
	    //@start-editable@

        if(head==NULL)
        {
            return 0;
        }
        int n = 1;
        Node *temp = head;
        while(temp->next!=NULL)
        {
            temp = temp->next;
            n++;
        }

        return n;
	    //@end-editable@
	}

	void insertFirst(T x) {
	    //@start-editable@

        Node *ins = new Node(x);

		if(head==NULL)
        {
            head = ins;
        }

        else
        {
            ins->next = head;
            head = ins;
        }

		//@end-editable@
		return;
	}

	T removeBefore(T val) {
	    //@start-editable@
            T x = val;
            if(head==NULL)
            {
                cout << "List is empty!" << endl;
                return x;
            }

            else if(head->element==val)
            {
                cout << "Deletion not possible" << endl;
                return x;
            }

            else
            {
                Node* temp = head;
                int pos = 0;
                bool flag = false;                
                

                while((temp->next!=NULL) && (flag==false))
                {
                    if(temp->element!=val)
                    {
                        temp = temp->next;
                        pos++;
                    }

                    else
                        flag = true;
                    
                }

                if(flag==false)
                {
                    cout << "Node not found" << endl;
                    return x;
                }


                pos-=1;
                temp = head;

                for(int i=0;i<pos;i++)
                {
                    temp = temp->next;    
                }

                x = temp->element;

                if(temp->next->next!=NULL && temp->next!=NULL)
                {
                    temp->next = temp->next->next;
                }

                else
                {
                    cout << "Deletion not possible" << endl;
                }
            
            }
		
		
		
			//@end-editable@
			return x;
		
		
	}

	bool swap(int sp, int ep) {
	    //@start-editable@

		if(sp>size() || (ep>size()))
        {
            cout << "Invalid Swap range" << endl;
            return false;
        }

        //find node sp
        int pos = 1;
        Node* temp = head;

        while((temp->next!=NULL) && (pos<sp))
        {
            temp = temp->next;
            pos++;
        }


        while(pos<ep && temp!=NULL && temp->next!=NULL)
        {
            printlist();
            T tmp = temp->element;
            temp->element = temp->next->element; 
            temp->next->element = tmp; 
            

            pos++;
            temp = temp->next; 
        } 

        printlist();

        //@end-editable@
		return false;
	}
//Prints the list
	void printlist(){
		if (!isEmpty()) {
			Node *temp = head;
			while (temp != NULL) {
				cout << temp->element << " ";
				temp = temp->next;
			}
			cout << endl;
			return;
		}
		cout << ("List is empty!")<<endl;
	}

};

//Driver Code
int main(){
	SLList<int> slist1;
 	string noOfInputs,str;
 	getline(cin, noOfInputs);
 	for(int i=0;i<stoi(noOfInputs);i++){
 	    getline(cin, str); 
 	    
 	    if (str.substr(0, 2) == "IF"){
 	        int value = stoi(str.substr(3, 5));
 	        slist1.insertFirst(value);
 	        slist1.printlist();
 	    }
 	    else if (str.substr(0, 2) == "DB"){
 	        int value = stoi(str.substr(3, 5));
 	        int rt=slist1.removeBefore(value);
 	        if (rt!=0)
 	        {
 	            cout<< rt<<endl;
 	        slist1.printlist();
 	        }
 	    }
 	    else if (str.substr(0, 2) == "SW"){
 	        
 	        int s = stoi(str.substr(3, 5));
 	        int e = stoi(str.substr(5, 7));
 	        slist1.swap(s,e);
 	       // slist1.printlist();
 	    }
 	    else if (str.substr(0, 1) == "S"){
 	       cout<< slist1.size()<<endl;
 	    }
 	    else if (str.substr(0,1) == "I"){
 	        
 	        if(slist1.isEmpty()){
 	            cout<<"True"<<endl;
 	        }
 	        else{
 	            cout<<"False"<<endl;
 	        }
 	    }
 	}
}