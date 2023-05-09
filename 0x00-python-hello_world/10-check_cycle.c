#include "lists.h"

int check_cycle(listint_t *list) {
    listint_t *slow = list;
    listint_t *fast = list;

    while (fast != NULL && fast->next != NULL) {
        slow = slow->next;
        fast = fast->next->next;

        if (slow == fast) {
            return 1;  /* Cycle found */
        }
    }

    return 0;  /* No cycle found */
}

