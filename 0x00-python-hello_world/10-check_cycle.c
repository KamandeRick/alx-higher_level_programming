#include "lists.h"
/**
 * check_cycle - function to check if cycle present in singly linked list
 * @list: pointer to head
 * Return: 0 if there is no cycle else returns 1
 */
int check_cycle(listint_t *list)
{
        listint_t *fast, *slow;

        if (list == NULL)
                return (0);

        slow = list;
        fast = list->next;

        if (fast == NULL)
                return (0);

        while (slow != fast)
        {
                if (fast->next == NULL || fast->next->next == NULL)
                        return (0);
                slow = slow->next;
                fast = fast->next->next;
        }
        return (1);
}
