#include "lists.h"

listint_t *reverse(listint_t **head)
{
	listint_t *node = *head, *next, *bef = NULL;

	while (node)
	{
		next = node->next;
		node->next = bef;
		bef = node;
		node = next;
	}

	*head = bef;
	return (*head);
}

int is_palindrome(listint_t **head)
{
	listint_t rev = reverse(&head);
	if (*head == NULL || (*head)->next == NULL)
		return (1);
	

}
