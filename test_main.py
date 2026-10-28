  import pytest
  from main import fibonacci

  def test_fib_zero():
      assert fibonacci(0) == 0

  def test_fib_one():
      assert fibonacci(1) == 1

  def test_fib_two():
      assert fibonacci(2) == 1

  def test_fib_five():
      assert fibonacci(5) == 5

  def test_fib_seven():
      assert fibonacci(7) == 13

  def test_fib_negative():
      with pytest.raises(ValueError):
          fibonacci(-5)
