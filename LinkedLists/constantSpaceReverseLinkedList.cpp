#include <iostream>

struct Node {
	int val;
	Node* next;
};

//turns the passed array into a linked list returning pointer to head
Node* createAList(int* arr, int length) {
	if (length <= 0) {
		return NULL;
	}

	Node* head = new Node;
	head->val = arr[0];

	Node* iterator = head;
	for (int i = 1; i < length; i++) {
		Node* nextOne = new Node;
		iterator->next = nextOne;
		iterator = nextOne;
		iterator->val = arr[i];
	}

	iterator->next = NULL;

	return head;

}

//function to a reverse a linked list in O(n) time and O(1) space
Node* reverseList(Node* head) {

	//check the list is valid
	if (head == NULL || head->next == NULL) {
		return head;
	}

	//set up the 3 needed variables
	Node* prev = head;
	Node* cur = head->next;
	Node* nextOne = head->next->next;
	prev->next = NULL;

	//iterate through the list making current point to previous
	while (nextOne != NULL) {
		cur->next = prev;
		prev = cur;
		cur = nextOne;
		nextOne = cur->next;
	}

	//link in the last value
	cur->next = prev;

	return cur;
}

//quick helper function to print all the values of the linked list
void printList(Node* head) {
	while (head != NULL) {
		std::cout << " " << head->val;
		head = head->next;
	}
	std::cout << std::endl;
}

int main () {
	//array to make into the linked list
	int testVals[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

	//create the linked list
	Node* list = createAList(testVals, 10);

	//print initial list ordering
	std::cout << "The list initially was:";
	printList(list);

	//Reverse the linked list in constant space
	list = reverseList(list);

	//print the reversed list
	std::cout << "The reversed list is:";
	printList(list);

}