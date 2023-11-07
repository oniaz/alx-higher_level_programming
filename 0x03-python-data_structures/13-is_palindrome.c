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
    listint_t *start = *head, *end;

    if (!*head)
        return (1);

    /* get the list size*/
    while (start->next)
    {
        size++;
        start = start->next;
    }

    /* get the mid index*/
    start = *head;

    /* traverse to the mid */
    for (i = 0; i < size / 2; i++)
        start = start->next;
    /* reversing*/
    listint_t *prev, *current, *mynext;

    prev = start;
    mynext = prev->next;

    while (mynext)
    {
        current = mynext;
        mynext = current->next;
        current->next = prev;
        prev = current;
    }

    end = current;
    start = *head;

    for (i = 0; i < size / 2; i++)
    {
        if (end->n != start->n)
            return 0;
        end = end->next;
        start = start->next;
    }

    return (1);
}