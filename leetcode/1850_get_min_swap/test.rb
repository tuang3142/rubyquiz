require "minitest/autorun"
require_relative "solution"

class Test < Minitest::Test
  def test_general_cases
    assert_equal 2, Solution.new("5489355142", 4).solve
    assert_equal 4, Solution.new("11112", 4).solve
    assert_equal 1, Solution.new("00123", 1).solve
  end
end
