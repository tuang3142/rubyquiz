class Solution
  def self.max_sum_min_product(nums)
    n = nums.length

    # calc left bound
    left_bound = [0] * n
    st = []
    0.upto n-1 do |i|
      st.pop while !st.empty? && nums[st[-1]] >= nums[i]
      left_bound[i] = st.empty? ? 0 : st[-1] + 1
      st.append i
    end

    # calc right bound
    right_bound = [0] * nums.length
    st = []
    (n-1).downto 0 do |i|
      st.pop while !st.empty? && nums[st[-1]] >= nums[i]
      right_bound[i] = st.empty? ? n-1 : st[-1] - 1
      st.append i
    end

    # calc accumulated sum
    acc_sum = []
    nums.each_with_index do |val, i|
      if i == 0
        acc_sum.append(val)
      else
        acc_sum.append(acc_sum[-1] + val)
      end
    end

    nums.each_with_index.map do |val, i|
      val * self.get_sum_range(left_bound[i], right_bound[i], acc_sum)
    end.max
  end

  def self.get_sum_range(i, j, sum)
    return sum[j] if i == 0

    sum[j] - sum[i - 1]
  end
end

require "minitest/autorun"

class Test < Minitest::Test
  def test_general_cases
    assert_equal 14, Solution.max_sum_min_product([1, 2, 3, 2])
    assert_equal 10000, Solution.max_sum_min_product([100, 1, 2, 1, 1])
  end

  def test_edge_cases
    assert_equal 4, Solution.max_sum_min_product([1, 1, 1, 1])
    assert_equal 9, Solution.max_sum_min_product([3])
  end
end
