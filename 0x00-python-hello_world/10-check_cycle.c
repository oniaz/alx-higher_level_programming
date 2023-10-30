#include "lists.h"

/**
 * check_cycle - checks whether a linked list has a cycle in it
 * using Floyd’s cycle finding algorithm
 * @list: pointer to the head of the linked list
 *
 * Return: 0 if the linked list is linear, 1 if it has a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *tortoise = list, *hare = list;

	if (!list)
		return (0);

	while (hare->next && hare->next->next)
	{
		tortoise = tortoise->next;
		hare = hare->next->next;
		if (tortoise == hare)
			return (1);
	}
	return (0);
}
