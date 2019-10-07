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
            data =  t;
            left = right = null;
        }
    }
    
    static node add(int data){
        node newnode = new node(data);
        return newnode;
    }
    
    static void inorder(node root){
        if(root == null)
            return;
        inorder(root.left);
        System.out.print(root.data + " ");
        inorder(root.right);
    }
    
    static node removenode(node root, int data){
        node rightmost = root, prev = root, target = root;
        if(root.data == data && root.left == null && root.right == null)
            return null;
        Queue<node> Q = new LinkedList<> ();
        int cnt = 0;
        Q.add(root);
        while(Q.size() > 0){
            node temp = Q.poll();
            if(temp.data == data)
                target = temp;
            if(temp.left != null){
                Q.add(temp.left);
                prev = temp;
                rightmost = temp.left;
                cnt = 1;
            }
            if(temp.right != null){
                Q.add(temp.right);
                prev = temp;
                rightmost = temp.right;
                cnt = 2;
            }
        }
        if(cnt == 1)
            prev.left = null;
        else
            prev.right = null;
        int t = target.data;
        target.data = rightmost.data;
        rightmost.data = t;
        return root;
    }
    
	public static void main (String[] args) throws java.lang.Exception
	{
		// your code goes here
		node root = add(1);
		root.left = add(2);
		root.right = add(3);
		root.left.left = add(4);
		root.left.right = add(5);
		inorder(root);
		root = removenode(root, 4);
		System.out.println();
		inorder(root);
	}
}
