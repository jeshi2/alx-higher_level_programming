#include <Python.h>
#include <stdio.h>
#include <string.h>

/**
 * print_python_string - Prints info about python str
 * @p: pointer to PyObject
 * Return: error message if p is not valid
 **/
void print_python_string(PyObject *p)
{
    PyUnicodeObject *str = (PyUnicodeObject *)p;

    if (!PyUnicode_Check(str))
    {
        fprintf(stderr, "[ERROR] Invalid String Object\n");
        return;
    }

    Py_ssize_t length = PyUnicode_GET_LENGTH(str);
    Py_UCS4 *value = PyUnicode_AsUCS4Copy(str);

    if (!value)
    {
        fprintf(stderr, "[ERROR] Invalid String Object\n");
        return;
    }

    printf("[.] string object info\n");
    printf("  type: %s\n", PyUnicode_IS_COMPACT_ASCII(str) ? "compact ascii" : "compact unicode object");
    printf("  length: %zd\n", length);
    printf("  value: %ls\n", value);

    PyMem_Free(value);
}
