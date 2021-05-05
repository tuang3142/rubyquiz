require "minitest/autorun"
require_relative "solution"

class Test < Minitest::Test
  def test_regular_array
    assert_equal Solution.new([1, 1, 1], 2), 2
  end

  def test_small_array

  end

  def test_no_subarray_whose_sum_equal_k

  end
end
