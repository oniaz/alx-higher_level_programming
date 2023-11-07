#include "lists.h"

listint_t *reverser(listint_t *mid)
{
    listint_t *prev, *current, *mynext;

    prev = mid;
    mynext = prev->next;

    while (mynext)
    {
        current = mynext;
        mynext = current->next;
        current->next = prev;
        prev = current;
    }
    return (current);
}
/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: double pointer to the head node.
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
 */
int is_palindrome(listint_t **head)
{
    int size = 1, i;
    listint_t *ptr1 = *head, *end;

    if (!*head)
        return (1);

    /* get the list size*/
    while (ptr1->next)
    {
        size++;
        ptr1 = ptr1->next;
    }

    /* get the mid index*/
    ptr1 = *head;

    /* traverse to the mid */
    for (i = 0; i < size / 2; i++)
        ptr1 = ptr1->next;
    end = reverser(ptr1);

ptr1 = *head;

for (i = 0; i < size / 2; i++)
{
    if (end->n != ptr1->n)
        return 0;
    end = end->next;
    ptr1 = ptr1->next;
}
return (1);
}