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

class Array
  def <(other)
    (self <=> other) == -1
  end

  def >(other)
    (self <=> other) == 1
  end
end

def get_order(tasks)
  i = 0
  n = tasks.size
  current_time = 0
  pq = PriorityQueue.new
  ret = []
  tasks = tasks.map.with_index { |(enq_time, process_time), id| [enq_time, process_time, id] }.sort

  while i < n || !pq.empty?
    while i < n && tasks[i][0] <= current_time
      _, process_time, id = tasks[i]
      pq.push([process_time, id])
      i += 1
    end
    if !pq.empty?
      process_time, id = pq.pop
      current_time += process_time
      ret << id
    else
      current_time = tasks[i][0]
    end
  end

  ret
end
