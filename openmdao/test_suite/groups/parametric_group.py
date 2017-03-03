"""Define the test group classes."""
from __future__ import division, print_function

from openmdao.core.group import Group


class ParametericTestGroup(Group):
    """
    Test Group expected by `ParametricInstance`. Groups inheriting from this should extend
    `default_params` to include valid parametric options for that model.

    Attributes
    ----------
    expected_totals : dict or None
        Dictionary mapping (out, in) pairs to the associated total derivative. Optional
    total_of : iterable
        Iterable containing which outputs to take the derivative of.
    total_wrt : iterable
        Iterable containing which variables with which to take the derivative of the above.
    expected_values : dict or None
        Dictionary mapping variable names to expected values. Optional.
    default_params : dict
        Dictionary containing the available options and default values for parametric sweeps.
    """
    def __init__(self, **kwargs):

        self.expected_totals = None
        self.total_of = None
        self.total_wrt = None
        self.expected_values = None
        self.default_params = {
            'vector_class': ['default', 'petsc'],
            'global_jac': [True, False],
            'jacobian_type': ['matvec', 'dense', 'sparse-coo', 'sparse-csr'],
        }

        super(ParametericTestGroup, self).__init__(**kwargs)
