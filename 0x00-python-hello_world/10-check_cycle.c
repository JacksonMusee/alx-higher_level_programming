#include "lists.h"

/**
 *check_cycle - Check is a list has a cycle
 *
 *@list: The list
 *
 *Return: 1 if there is a cyle 0 if not
 */

int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	while (fast->next->next)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
			return (1);
	}

	return (0);
}
