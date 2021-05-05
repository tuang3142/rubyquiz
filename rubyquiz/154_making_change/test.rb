require "minitest/autorun"
require_relative "solution"

class Test < Minitest::Test
  def test_regular_case
    assert_equal Solution.new(14, [10, 7, 1]).solve, [7, 7]
    assert_equal Solution.new(39).solve, [25, 10, 1, 1, 1, 1]
  end
end
