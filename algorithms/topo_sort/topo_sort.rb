class Graph
  attr_reader :graph, :size

  def initialize(size)
    @size = size
    @graph = 1.upto(@size).map { [] }
    @found = [false] * @size
    @stack = []
  end

  def add_edge(u, v)
    @graph[u].append(v)
  end

  def topo_sort
    0.upto(@size - 1).each { |u| visit(u) }

    @stack.reverse
  end

  private

  def visit(u)
    return if @found[u]

    @found[u] = true
    @graph[u].each { |v| visit(v) }
    @stack.append(u)
  end
end
