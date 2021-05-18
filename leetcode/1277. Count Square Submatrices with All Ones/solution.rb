def count_squares(grid)
  row = grid.size - 1
  col = grid[0].size - 1

  res = 0
  0.upto row do |i|
    0.upto col do |j|
      next if grid[i][j].zero?

      unless i.zero? or j.zero?
        grid[i][j] += [grid[i-1][j-1], grid[i-1][j], grid[i][j-1]].min
      end
      res += grid[i][j]
    end
  end
  res
end

matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]

p count_squares(matrix)
