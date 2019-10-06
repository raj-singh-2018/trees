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
    
    static void inorder(node root){
        if(root == null)
            return;
        inorder(root.left);
        System.out.print(root.data + " ");
        inorder(root.right);
    }
    
    static void preorder(node root){
        if(root == null)
            return;
        System.out.print(root.data + " ");
        preorder(root.left);
        preorder(root.right);
    }
    
    static void postorder(node root){
        if(root == null)
            return;
        postorder(root.left);
        postorder(root.right);
        System.out.print(root.data + " ");
    }
    
    public static void main (String[] args) throws java.lang.Exception
	{
		// your code goes here
	    node root = new node(1);
	    root.left = new node(2);
	    root.right = new node(3);
	    root.left.left = new node(4);
	    root.left.right = new node(5);
	    inorder(root);
	    System.out.println();
	    preorder(root);
	    System.out.println();
	    postorder(root);
	}
}
