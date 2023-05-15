#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * reverse_list - reverses a linked list
 * @head: double pointer to the head of the list
 */
void reverse_list(listint_t **head)
{
    listint_t *prev = NULL;
    listint_t *current = *head;
    listint_t *next = NULL;

    while (current != NULL)
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }

    *head = prev;
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: double pointer to the head of the list
 * Return: 1 if palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
    if (*head == NULL || (*head)->next == NULL)
        return 1;

    listint_t *slow_ptr = *head;
    listint_t *fast_ptr = *head;
    listint_t *prev_slow_ptr = *head;
    listint_t *second_half = NULL;
    int is_palindrome = 1;

    while (fast_ptr != NULL && fast_ptr->next != NULL)
    {
        fast_ptr = fast_ptr->next->next;
        prev_slow_ptr = slow_ptr;
        slow_ptr = slow_ptr->next;
    }

    if (fast_ptr != NULL)
    {
        second_half = slow_ptr->next;
    }
    else
    {
        second_half = slow_ptr;
    }

    prev_slow_ptr->next = NULL;
    reverse_list(&second_half);

    listint_t *list1 = *head;
    listint_t *list2 = second_half;

    while (list1 != NULL && list2 != NULL)
    {
        if (list1->n != list2->n)
        {
            is_palindrome = 0;
            break;
        }
        list1 = list1->next;
        list2 = list2->next;
    }

    reverse_list(&second_half);

    if (fast_ptr != NULL)
    {
        prev_slow_ptr->next = slow_ptr;
        slow_ptr->next = second_half;
    }
    else
    {
        prev_slow_ptr->next = second_half;
    }

    return is_palindrome;
}
