require "minitest/autorun"
require_relative "topo_sort"

class TopoSortTest < Minitest::Test
  def validate_topo_sort(graph)
    arr = graph.topo_sort
    0.upto(graph.size - 1).all? do |u|
      gp = graph.graph[u]
      gp.all? { |v| arr.index(v) > arr.index(u) }
    end
  end

  def test_add_edges_to_graph_and_topo_sort
    graph = Graph.new(6)
    graph.add_edge(5, 2)
    graph.add_edge(5, 0)
    graph.add_edge(4, 0)
    graph.add_edge(4, 1)
    graph.add_edge(2, 3)
    graph.add_edge(3, 1)

    assert_equal true, validate_topo_sort(graph)
  end
end
