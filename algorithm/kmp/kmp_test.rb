require "minitest/autorun"
require_relative "topo_sort"

class KMPTest < Minitest::Test
  def test_lps
    kmp = KMP.new
    s = "ababcabab"
    assert_equal [0, 0, 1, 2, 0, 1, 2, 3, 4], kmp.buid_lps(s)
  end
end
