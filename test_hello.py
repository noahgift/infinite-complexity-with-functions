from click.testing import CliRunner
from hello import one, two, three, main


def test_one():
    assert 2 == one(1)
    
def test_two():
    assert 3 == two(1)

def test_three():
    assert 4 == three(1)

def test_hello_world():
  runner = CliRunner()
  result = runner.invoke(main, ['--myinput', '1'])
  assert result.exit_code == 0
  assert 'Click CLI' in result.output
