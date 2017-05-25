import io
import sys
from unittest.mock import patch


@patch('builtins.input')
@patch('sys.stdout', new=io.StringIO())
def controlled_call(task, solution, mock_input):
    """Run solution function with given task and grab standard output.

    Args:
        task: Task multi-line text.
        solution: Solution function.
        mock_input: Auto-provided patched input function.

    Returns:
        StdOut of the solution function call.

    Raises:
        ValueError: Input data doesn't match solution expectations.
    """
    input_chunks = task.split('\n')
    mock_input.side_effect = input_chunks
    try:
        solution()
    except StopIteration:
        raise ValueError('Solution expects more input data')
    if mock_input.call_count != len(input_chunks):
        raise ValueError('Solution does not expect so much data')
    return sys.stdout.getvalue().strip()
