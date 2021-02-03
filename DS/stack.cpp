template<typename Object>

class Stack
{
 public:
 int size();
 bool isEmpty();
 Object& top()
     throw(StackEmptyException);
 void push(Object o);
 Object pop()
     throw(StackFullException);
