#include "lists.h"

/**
 * check_cycle - check if the list has a cycle or not
 * @list: list to check
 * Return: 1 if there is a cycle, else 0
 */

int check_cycle(listint_t *list)
{
	listint_t *normal, *fast;

	if (list == NULL || list->next == NULL)
		return (0);

	normal = list->next;
	fast = list->next->next;

	while (normal && fast && fast->next)
	{
		if (normal == fast)
			return (1);

		normal = normal->next;
		fast = fast->next->next;
	}
	return (0);
}