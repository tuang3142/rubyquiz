require "minitest/autorun"
require_relative "priority_queue"

class PriorityQueueTest < Minitest::Test
  def setup
    @pq = PriorityQueue.new
  end

  def test_push_and_size
    @pq.push(1)
    @pq.push(2)

    assert_equal 3, @pq.size
  end

  def test_pop
    @pq.push(1)
    @pq.push(5)
    @pq.push(-1)

    assert_equal -1, @pq.pop
    assert_equal 3, @pq.size
  end

  def test_empty
    assert_equal true, @pq.empty?
    assert_equal nil, @pq.pop
  end
end
