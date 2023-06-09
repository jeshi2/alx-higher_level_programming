#include <Python.h>
#include <stdio.h>
#include <string.h>

/**
 * print_python_string - Prints info about python str
 * @p: pointer to PyObject
 * Return: error messages
 **/
void print_python_string(PyObject *p)
{
    Py_ssize_t length = PyUnicode_GET_LENGTH(p);
    const char *value;
    if (!PyUnicode_Check(p))
    {
        fprintf(stderr, "[ERROR] Invalid String Object\n");
        return;
    }
    value = PyUnicode_AsUTF8(p);
    
    if (!value)
    {
        fprintf(stderr, "[ERROR] Invalid String Object\n");
        return;
    }

    printf("[.] string object info\n");
    printf("  type: compact %s\n", PyUnicode_IS_COMPACT_ASCII(p) ? "ascii" : "unicode object");
    printf("  length: %zd\n", length);
    printf("  value: %s\n", value);
}
