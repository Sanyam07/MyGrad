from .multivar_operations import Operation
import numpy as np

__all__ = ["Sinh",
           "Cosh",
           "Tanh",
           "Csch",
           "Sech",
           "Coth"]


class Sinh(Operation):
    def __call__(self, a):
        self.variables = (a,)
        return np.sinh(a.data)

    def backward_var(self, grad, index, **kwargs):
        a = self.variables[index]
        a.backward(grad * np.cosh(a.data), **kwargs)


class Cosh(Operation):
    def __call__(self, a):
        self.variables = (a,)
        return np.cosh(a.data)

    def backward_var(self, grad, index, **kwargs):
        a = self.variables[index]
        a.backward(grad * np.sinh(a.data), **kwargs)


class Tanh(Operation):
    def __call__(self, a):
        self.variables = (a,)
        return np.tanh(a.data)

    def backward_var(self, grad, index, **kwargs):
        a = self.variables[index]
        a.backward(grad * (1 - np.tanh(a.data) ** 2), **kwargs)


class Csch(Operation):
    def __call__(self, a):
        self.variables = (a,)
        return 1 / np.sinh(a.data)

    def backward_var(self, grad, index, **kwargs):
        a = self.variables[index]
        a.backward(grad * -np.cosh(a.data) / np.sinh(a.data)**2)


class Sech(Operation):
    def __call__(self, a):
        self.variables = (a,)
        return 1 / np.cosh(a.data)

    def backward_var(self, grad, index, **kwargs):
        a = self.variables[index]
        a.backward(grad * -np.sinh(a.data) / np.cosh(a.data)**2, **kwargs)


class Coth(Operation):
    def __call__(self, a):
        self.variables = (a,)
        return 1 / np.tanh(a.data)

    def backward_var(self, grad, index, **kwargs):
        a = self.variables[index]
        a.backward(grad * -1 / np.sinh(a.data)**2, **kwargs)