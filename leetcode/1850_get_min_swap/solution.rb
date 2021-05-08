class Solution
  def initialize(arr, k)
    @arr = arr.split("").reverse
    @k = k
  end

  def solve
    brr = @arr.map(&:clone)
    @k.times { brr = gen_next_permuation(brr) }

    calc_diff(brr, @arr)
  end

  def gen_next_permuation(a)
    n = a.length
    i = (0..n-2).find { |x| a[x] > a[x + 1] } + 1
    j = a[0, i].bsearch_index { |x| x > a[i] }
    a[i], a[j] = a[j], a[i]
    a[0, i].reverse + a[i, n]
  end

  def calc_diff(a, b)
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
