#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 13:58:00 2021

@author: nirmalk
"""


class singly_linked_lists:
    class node:
        def __init__(self):
            self.element = None
            self.next = None

    def __init__(self):
        self.head = self.node()
        self.sz = 0

    def printList(self):
        tnode = self.head

        while tnode.next != None:
            print(tnode.element, end="-->")
            tnode = tnode.next
        return

    def size_of_list(self):
        return self.sz

    def isempty(self):
        return self.sz == 0

    def insertFirst(self, u):
        u.next = self.head
        self.head = u
        self.sz += 1
        return

    def delete_first(self):
        if self.size_of_list() == 0:
            return "List Empty"
        elif self.size_of_list() == 1:
            self.head.element = None
            self.sz -= 1
        else:
            temp = self.node()
            temp = self.head
            head = self.head.next
            temp.next = None
            self.sz -= 1

    def delete_last(self):
        if self.size_of_list() == 0:
            return "List Empty"
        elif self.size_of_list() == 1:
            self.head.element = None
            self.sz = -1
        else:
            curnode = self.node()
            while curnode.next.next != None:
                curnode = curnode.next
            curnode.next = None

    def delete_after(self,v):
        if self.size_of_list() == 0:
            return "List Empty"
        else:
            curnode = self.node()
            while curnode.element!=v.element:
                curnode = curnode.next
            curnode.next = None
        return

    def insert_after(self,v):

        return

    def find_node(self,n):

        return


list1 = singly_linked_lists()
print("size of the list : " + str(list1.size_of_list()))
print("is empty : " + str(list1.isempty()))

for i in range(5):
    curnode = list1.node()
    curnode.element = i
    list1.insertFirst(curnode)
print("*****")
list1.printList()
