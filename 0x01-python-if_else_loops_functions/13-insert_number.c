#include "lists.h"

/**
 * *insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to the pointer to the head node of the list.
 * @number: int value of the node to be added.
 *
 * Return: the address of the new node, or NULL if it failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newnode, *nude = *head;
	int firstNode = 1;

	newnode = malloc(sizeof(listint_t));
	if (!newnode)
		return (NULL);

	newnode->n = number;
	newnode->next = NULL;

	/* if there's no list, add a head node */
	if (!*head)
	{
		*head = newnode;
		return (*head);
	}

	/* only one node in the list */
	if (!nude->next)
	{
		if (nude->n >= number)
		{
			newnode->next = nude;
			*head = newnode;
		}
		else
			nude->next = newnode;
		return (*head);
	}

	while (nude && nude->next)
	{
		if (firstNode)
		{
			if (nude->n > number)
			{
				newnode->next = nude;
				*head = newnode;
				return (*head);
			}
			firstNode = 0;
		}

		if (nude->next->n > number)
		{
			newnode->next = nude->next;
			nude->next = newnode;
			return (*head);
		}
		nude = nude->next;
	}
	nude->next = newnode;
	return (*head);
}
