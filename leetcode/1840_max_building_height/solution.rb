def get_max_height(cap, i, j)
  i1, h1 = cap[i]
  i2, h2 = cap[j]

  h = h1 + (i2 - i1).abs

  h <= h2 ? cap[j][1] = h : (h + h2) / 2
end

def max_building(n, cap)
  cap.concat [[1, 0], [n, n - 1]]
  cap.sort!
  size = cap.size

  0.upto(size - 2).map { |i| get_max_height(cap, i, i + 1) }
  (size - 1).downto(1).map { |i| get_max_height(cap, i, i - 1) }.max
end
