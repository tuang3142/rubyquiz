def longest_zig_zag(root)
  left, right = ["left", "right"]
  ret = 0
  def visit(dir, node, step)
    return if node.nil?
    ret = [step, ret].max

    if dir == left
      visit(left, node.left, step + 1)
      visit(right, node.right, 1)
    else
      visit(left, node.right, step + 1)
      visit(right, node.left, 1)
    end
  end

  visit(left, root, 0), visit(right, root, 0)
  ret
end
