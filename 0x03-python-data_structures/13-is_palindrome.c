/**
 * is_palindrome - function to check if a singly linked list is  palindrome
 * Description: function to check if a singly linked list is a palindrome.
 * @head: Pointer to head
 * Return: 0 if it is not a palindrome, else return 1
 */
int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
        int i, tally;
        int arrayList[2048];

        if (current == NULL)
                return (1);
        for (tally = 0; current != NULL; tally++, current = current->next)
                ;
        if (tally == 1)
                return (1);
        current = *head;
        if (tally % 2 == 0)
        {
                for (i = 0; i < (tally / 2); i++, current = current->next)
                        arrayList[i] = current->n;
                for (i = i - 1; i >= 0; i--, current = current->next)
                        if (arrayList[i] != current->n)
                                return (0);
        }
        else
        {
                for (i = 0; i <= (tally / 2); i++, current = current->next)
                        arrayList[i] = current->n;
                for (i = i - 2; i >= 0; i--, current = current->next)
                        if (arrayList[i] != current->n)
                                return (0);
        }
        return (1);
}
