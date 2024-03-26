import java.util.Scanner;

class Node {
    int data;
    Node next;

    Node(int data) {
        this.data = data;
        this.next = null;
    }
}

public class LinkedList {
    static Node head;

    static void insert(int data) {
        Node new_node = new Node(data);
        if (head == null) {
            head = new_node;
            return;
        }
        Node current = head;
        while (current.next != null) {
            current = current.next;
        }
        current.next = new_node;
    }

    static void show() {
        Node current = head;
        while (current != null) {
            System.out.print(current.data + " ");
            current = current.next;
        }
        System.out.println();
    }

    static Node reverseKBlock(Node head, int k) {
        Node current = head;
        Node prev = null;
        Node nextNode = null;
        int count = 0;

        // Reverse the first K nodes of the linked list
        while (count < k && current != null) {
            nextNode = current.next;
            current.next = prev;
            prev = current;
            current = nextNode;
            count++;
        }

        // Recursive call for the remaining nodes
        if (nextNode != null) {
            head.next = reverseKBlock(nextNode, k);
        }

        return prev; // New head of the reversed sublist
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Input the elements of the linked list
        System.out.print("Enter the number of elements in the linked list: ");
        int n = scanner.nextInt();
        System.out.println("Enter the elements:");
        for (int i = 0; i < n; i++) {
            int data = scanner.nextInt();
            insert(data);
        }

        // Input the block size K
        System.out.print("Enter the block size (K): ");
        int k = scanner.nextInt();

        // Display the original linked list
        System.out.println("Original linked list:\n");
        show();

        // Reverse the linked list in blocks of size K
        head = reverseKBlock(head, k);

        // Display the reversed linked list
        System.out.println("Linked list after reversing in blocks of size " + k + ":");
        show();

        scanner.close();
    }
}
