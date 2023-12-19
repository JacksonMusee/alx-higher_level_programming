#include <stdio.h>
#include <stdlib.h>
#include <Python.h>

/**
 *print_python_list - Print items of a python list
 *
 *@p: Pointer to a python object, list in this case
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size;
	Py_ssize_t i;
	PyObject *item;

	setbuf(stdout, NULL);

	if (PyList_Check(p))
	{
		size = PyObject_Length(p);
		
		printf("[");
		i = 0;
		while (i < size)
		{
			item = PyList_GetSlice(p, i, i + 1);
			PyObject_Print(item, stdout, 0);
			Py_XDECREF(item);

			if (i < size - 1)
			{
				printf(", ");
			}

			i++;
		}

		printf("]\n");
	}
	else
	{
		fprintf(stderr,"Invalid List Object\n");	
	}
}

/**
 *
 *
 *
 *
 *


void print_python_bytes(PyObject *p)
{
	
}*/
