class PriorityQueue
  def initialize
    @q = [nil]
  end

  def push(e)
    @q << e
    go_up(size - 1)
  end

  def pop
    swap(1, size - 1)
    top = @q.pop
    go_down(1)
    top
  end

  def size
    @q.size
  end

  def empty?
    @q[size - 1].nil?
  end

  private

  def go_up(id)
    parent_id = id / 2
    return if id <= 1
    return if @q[parent_id] < @q[id]

    swap(id, parent_id) if @q[id] < @q[parent_id]
    go_up(parent_id)
  end

  def go_down(id)
    left_id, right_id = id * 2, id * 2 + 1
    return if left_id >= size

    next_id = left_id
    next_id = right_id if right_id < size && @q[right_id] < @q[left_id]
    return if @q[id] < @q[next_id]

    swap(id, next_id)
    go_down(next_id)
  end

  def swap(i, j)
    @q[i], @q[j] = @q[j], @q[i]
  end
end
