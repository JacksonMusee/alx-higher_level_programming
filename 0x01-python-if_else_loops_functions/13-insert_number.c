#include "lists.h"

/**
 *insert_node - inserts a node into a sorted list
 *
 *@head: The list
 *@number: Data value of the new node
 *
 *Return: The new node
 *
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_nod;
	listint_t *prev_nod = NULL;
	listint_t *curr_nod = NULL;

	new_nod = malloc(sizeof(listint_t));
	if (new_nod == NULL)
		return (NULL);

	new_nod->n = number;
	new_nod->next = NULL;

	if (*head == NULL)
	{
		*head = new_nod;
		return (new_nod);
	}

	curr_nod = *head;
	while ((curr_nod->n <= number) && curr_nod->next)
	{
		prev_nod = curr_nod;
		curr_nod = curr_nod->next;
	}

	if (curr_nod->n > number)
	{
		prev_nod->next = new_nod;
		new_nod->next = curr_nod;
	}
	else
	{
		curr_nod->next = new_nod;
	}

	return (new_nod);
}
