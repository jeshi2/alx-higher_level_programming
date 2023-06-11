#include <Python.h>

void print_python_string(PyObject *p)
{
    const cahr *value;
    if (!PyUnicode_Check(p))
    {
        fprintf(stderr, "[ERROR] Invalid String Object\n");
        return;
    }

    Py_ssize_t length = PyUnicode_GET_LENGTH(p);
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
