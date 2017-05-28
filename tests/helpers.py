import io
from unittest.mock import patch


@patch('builtins.input')
@patch('sys.stdout', new_callable=io.StringIO)
def call(task, solution, mock_stdout, mock_input):
    """Run solution function with given task and grab standard output."""
    input_chunks = task.split('\n')
    mock_input.side_effect = input_chunks
    try:
        solution()
    except StopIteration:
        raise ValueError('Solution expects more input data')
    if mock_input.call_count != len(input_chunks):
        raise ValueError('Solution does not expect so much data')
    return mock_stdout.getvalue().strip()
