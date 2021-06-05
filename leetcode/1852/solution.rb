def distinct_numbers(nums, k)
  n = nums.size
  dist = [0]
  counter = nums[0, k].each_with_object({}) do |v, counter|
    counter[v] = counter[v].to_i + 1
    dist[0] += 1 if counter[v] == 1
  end

  k.upto(n-1) do |i|
    first = nums[i - k]
    last = nums[i]
    dist << dist[-1]
    dist[-1] += 1 if (counter[last] = counter[last].to_i + 1) == 1
    dist[-1] -= 1 if (counter[first] -= 1) == 0
  end

  dist
end
