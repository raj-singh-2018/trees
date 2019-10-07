/* package codechef; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class Codechef
{   
    static class node{
        int data;
        node left, right;
        node(int tdata){
            data = tdata;
            left = right = null;
        }
    }
    
    static void levelOrder(node root){
        Queue<node> Q = new LinkedList<>();
        Q.add(root);
        while(Q.size() > 0){
            node temp = Q.poll();
            System.out.print(temp.data + " ");
            if(temp.left != null)
                Q.add(temp.left);
            if(temp.right != null)
                Q.add(temp.right);
        }
    }
    
	public static void main (String[] args) throws java.lang.Exception
	{
	   	// your code goes here
	   	node root = new node(1);
	   	root.left = new node(2);
	   	root.right = new node(3);
	   	root.left.left = new node(4);
	   	root.left.right = new node(5);
	   	levelOrder(root);
	}
}
