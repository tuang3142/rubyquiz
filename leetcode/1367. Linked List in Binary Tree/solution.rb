def check_down_path(list, tree)
  return true if list.nil?
  return false if tree.nil? || list.val != tree.val

  check_down_path(list.next, tree.left) ||
  check_down_path(list.next, tree.right)
end

def is_sub_path(head, root)
  return true if check_down_path(head, root)

  is_sub_path(head, root.left) ||
  is_sub_path(head, root.right)
end
