# Binary-Search-Tree
This repository contains a simple implementation of the binary search algorithm in Python.

# Description

Binary search is an efficient algorithm for finding a target value within a sorted array. It works by repeatedly dividing the search interval in half until the target value is found or the interval becomes empty.

# What is Binary Search Tree?

Binary Search Tree (BST) is a special type of binary tree in which the left child of a node has a value less than the node’s value and the right child has a value greater than the node’s value. This property is called the BST property and it makes it possible to efficiently search, insert, and delete elements in the tree.

Operation:

1. Insertion in BST.
2. Deletion in BST.
3. Searching in BST.

Traversal:
1. In-order Traversal.
2. Pre-order Traversal.
3. Post-order Traversal.

   
# Properties of Binary Search Tree:

1. The left subtree of a node contains only nodes with keys lesser than the node’s key.
2. The right subtree of a node contains only nodes with keys greater than the node’s key.
3. This means everything to the left of the root is less than the value of the root and everything to the right of the root is greater than the value of the root. Due to this performing, a binary search is very easy.
4. The left and right subtree each must also be a binary search tree.  
5. There must be no duplicate nodes(BST may have duplicate values with different handling approaches)


# Applications of BST:

1. Graph algorithms: BSTs can be used to implement graph algorithms, such as in minimum spanning tree algorithms.
2. Priority Queues: BSTs can be used to implement priority queues, where the element with the highest priority is at the root of the tree, and elements with lower priority are stored in the subtrees.
3. Self-balancing binary search tree: BSTs can be used as a self-balancing data structures such as AVL tree and Red-black tree.
4. Data storage and retrieval: BSTs can be used to store and retrieve data quickly, such as in databases, where searching for a specific record can be done in logarithmic time.

   
# Advantages:
1. Fast search: Searching for a specific value in a BST has an average time complexity of O(log n), where n is the number of nodes in the tree. This is much faster than searching for an element in an array or 2. 2. linked list, which have a time complexity of O(n) in the worst case.
3. In-order traversal: BSTs can be traversed in-order, which visits the left subtree, the root, and the right subtree. This can be used to sort a dataset.
4. Space efficient: BSTs are space efficient as they do not store any redundant information, unlike arrays and linked lists.

   
# Disadvantages:
1. Skewed trees: If a tree becomes skewed, the time complexity of search, insertion, and deletion operations will be O(n) instead of O(log n), which can make the tree inefficient.
2. Additional time required: Self-balancing trees require additional time to maintain balance during insertion and deletion operations.
3. Efficiency: BSTs are not efficient for datasets with many duplicates as they will waste space.



# Example
Here's an example of how to use the binary search algorithm:

     Enter a sorted list of numbers separated by spaces: 1 3 5 7 9 11 13 15 17 19
     Enter the target element to search for: 11
     Element 11 found at index 5.

             9
           /   \
         3      15
        / \    /  \
       1   7  13   17
            \      \
             11     19



# Usage
To use the binary search algorithm, follow these steps:

1. Clone the Repository: Clone this repository to your local machine using Git.

        "git clone https://github.com/bhawana0504/binary-search.git"

   
2. Input: Follow the prompts to input a sorted list of numbers and the target element to search for.

3. Output: The program will output the index of the target element if found, or a message indicating that the element was not found.


    
# Contributing
If you'd like to contribute to this project, please follow these guidelines:

1. Fork the repository.
2. Create a new branch (git checkout -b feature/new-feature).
3. Commit your changes (git commit -am 'Add new feature').
4. Push to the branch (git push origin feature/new-feature).
5. Create a new Pull Request.

   
# License

This project is licensed under the MIT License - see the LICENSE file for details.
