require "minitest/autorun"
require_relative "solution"

class Test < Minitest::Test
  def test_grid_has_some_islands
    grid = [
      ["1","1","1","1","0"],
      ["1","1","0","1","0"],
      ["1","1","0","0","0"],
      ["0","0","0","0","0"]
    ]
    assert_equal Solution.new(grid).solve, 1

    grid = [
      ["1","1","0","0"],
      ["1","1","0","0"],
      ["0","0","1","0"],
      ["0","0","0","1"]
    ]
    assert_equal Solution.new(grid).solve, 3

    grid = [
      ["1","1"],
      ["1","1"],
    ]
    assert_equal Solution.new(grid).solve, 1
  end


  def test_grid_has_no_islands
    grid = [
      ["0","0"],
      ["0","0"],
      ["0","0"],
      ["0","0"]
    ]
    assert_equal Solution.new(grid).solve, 0
  end

  def test_really_small_grid
    grid = [["1"]]
    assert_equal Solution.new(grid).solve, 1

    grid = [["0"]]
    assert_equal Solution.new(grid).solve, 0
  end
end
