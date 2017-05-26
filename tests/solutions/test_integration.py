import importlib
import os
import warnings

import pytest

from tests.helpers import call

BASE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
TEST_DATA_PATH = os.path.join(BASE_PATH, 'tests', 'data')


def get_test_parameters():
    """Get input, output and main solution function."""
    parameters = []
    solutions = os.listdir(os.path.join(BASE_PATH, 'solutions'))
    solutions = [file[:-3] for file in solutions if not file.startswith('__')]
    for solution in solutions:
        try:
            with open(os.path.join(TEST_DATA_PATH, solution, 'in')) as file:
                task = file.read()
            main = importlib.import_module('solutions.%s' % solution).main
            with open(os.path.join(TEST_DATA_PATH, solution, 'out')) as file:
                expected_result = file.read()
            parameters.append((task, main, expected_result))
        except FileNotFoundError:
            warnings.warn('Test data for solution %s was not found' % solution)
        except (ImportError, AttributeError):
            warnings.warn('Solution %s does not implement main()' % solution)
    return parameters


@pytest.mark.parametrize('task,solution,expected_result', get_test_parameters())
def test_input_output(task, solution, expected_result):
    assert call(task, solution) == expected_result
