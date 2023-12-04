#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <listobject.h>
#include <object.h>

/**
 * print_python_list_info - prints information about Python lists
 * Description: func to  print information  about Python lists
 * @p: Pointer to pyobject
 * Return: void
 */

void print_python_list_info(PyObject *p)
{
        long int listSize = Py_SIZE(p), indexList;
        PyListObject *list_object = (PyListObject *) p;

        printf("[*] Size of the Python List = %ld\n", listSize);
        printf("[*] Allocated = %ld\n", list_object->allocated);

        for (indexList = 0; indexList < listSize; indexList++)
                printf("Element %ld: %s\n", indexList,
                                Py_TYPE(PyList_GetItem(p, indexList))->tp_name);
}

