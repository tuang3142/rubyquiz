class Solution
  def self.get_min_swap(a, k)
    a = a.split("").reverse
    b = a.map(&:clone)
    k.times { b = gen_next_permuation(b) }
    calc_diff(b, a)
  end

  def self.gen_next_permuation(a)
    n = a.length
    i = (0..n-2).find { |x| a[x] > a[x + 1] } + 1
    j = a[0, i].bsearch_index { |x| x > a[i] }
    a[i], a[j] = a[j], a[i]
    a[0, i].reverse + a[i, n]
  end

  def self.calc_diff(a, b)
    ans = 0
    n = a.length
    n.times do |i|
      if a[i] != b[i]
        j = i
        j += 1 while j < n && b[j] != a[i]
        ans += j - i
        while j > i
          b[j], b[j - 1] = b[j - 1], b[i]
          j -= 1
        end
      end
    end

    ans
  end
end

require "minitest/autorun"

class Test < Minitest::Test
  def test_general_cases
    assert_equal 2, Solution.get_min_swap("5489355142", 4)
    assert_equal 4, Solution.get_min_swap("11112", 4)
    assert_equal 1, Solution.get_min_swap("00123", 1)
  end
end
