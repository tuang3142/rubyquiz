def min_interval(intervals, queries)
  queries = queries.map.with_index { |v, i| [v, i] }.sort
  intervals.sort!

  n = queries.size
  ret = [-1] * n
  i, j = 0, 0
  while i < n
    num, id = queries[i]
    while j < intervals.size
      l, r = intevals[j]
      if r < num
        j -= 1
        break
      end

      ret[id] = [ret[id], r - l + 1].min
      j += 1
    end
  end

  ret
end
