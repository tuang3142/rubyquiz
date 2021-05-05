class Solution
  def initialize(grid)
    @grid = grid
    @n = @grid.length
    @m = @grid[0].length
  end

  def solve
    count = 0

    (0..@n-1).each do |i|
      (0..@m-1).each do |j|
        next if @grid[i][j] == "0"

        count += 1
        dfs(i, j)
      end
    end

    count
  end

  def dfs(i, j)
    return if out_of_bound(i, j) || @grid[i][j] == "0"

    @grid[i][j] = "0"
    dfs(i + 1, j)
    dfs(i - 1, j)
    dfs(i, j + 1)
    dfs(i, j - 1)
  end

  def out_of_bound(i, j)
    i < 0 || j < 0 || i >= @n || j >= @m
  end
end

