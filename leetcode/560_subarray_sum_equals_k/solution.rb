class Solution
  def initialize(nums, k)
    @nums = num
    @k = k
  end

  def solve
    cumulative_sum = 0
    counter = 0
    map_sum = {0 => 1}

    @nums.each do |n|
      cumulative_sum += n
      counter += map_sum[cumulative_sum - @k].to_i

      map_sum[cumulative_sum] = map_sum[cumulative_sum].to_i + 1
    end

    counter
  end
end
