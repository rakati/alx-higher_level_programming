#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - check if circle in a linked list.
 * @list: A pointer to the head of the list
 *
 * Return: 0 if acyclic otherwise 0
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (!list)
		return (0);
	slow = (listint_t *)list;
	fast = slow;
	while (slow)
	{
		slow = slow->next;
		if (fast)
			fast = fast->next ? fast->next->next : NULL;
		if (slow == fast)
			break;
	}
	if (slow == NULL || slow != fast)
		return (0);
	return (1);
}
