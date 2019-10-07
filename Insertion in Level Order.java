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
    
    static node addlevel(node root, int data){
        if(root == null){
            root = new node(data);
            return root;
        }
        Queue<node> Q = new LinkedList<> ();
        Q.add(root);
        while(Q.size() > 0){
            node temp = Q.poll();
            if(temp.left != null)
                Q.add(temp.left);
            else{
                temp.left = new node(data);
                break;
            }
            if(temp.right != null)
                Q.add(temp.right);
            else{
                temp.right = new node(data);
                break;
            }
        }
        return root;
    }
    
    static void inorder(node root){
        if(root == null)
            return;
        inorder(root.left);
        System.out.print(root.data + " ");
        inorder(root.right);
    }
    
	public static void main (String[] args) throws java.lang.Exception
	{
	   	// your code goes here
	   	node root = new node(1);
	   	root.left = new node(2);
	   	root.right = new node(3);
	   	root.right.left = new node(5);
	   	root.left.right = new node(4);
	   	root.right.right = new node(6);
	   	inorder(root);
	   	root = addlevel(root, 100);
	   	System.out.println("\nNOW:");
	   	inorder(root);
	}
}
