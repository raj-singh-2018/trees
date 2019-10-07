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
        node(int t){
            data = t;
            left = right = null;
        }
    }
    
    static int treesize(node root){
        if(root == null)
            return 0;
        return 1 + treesize(root.left) + treesize(root.right);
    }
    
	public static void main (String[] args) throws java.lang.Exception
	{
		// your code goes here
		node root = new node(1);
		root.left = new node(2);
		root.right = new node(3);
		root.left.left = new node(4);
		root.left.right = new node(5);
		System.out.println(treesize(root));
	}
}
