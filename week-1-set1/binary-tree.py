# -*- coding: UTF-8 -*-

"""
描述
给定一个1到n的排列，按顺序依次插入到一棵二叉排序树中，请你将这棵二叉树前序遍历和后序遍历输出。

前序遍历的定义

后序遍历的定义

输入
第一行一个整数n。

接下来一行表示为n个整数，代表1到n的一个排列。

输出
输出所建成的二叉树的前序遍历和后序遍历。

输入样例
10
2 6 9 3 5 7 10 8 4 1

输出样例
2 1 6 3 5 4 9 7 8 10
1 4 5 3 8 7 10 9 6 2

"""
# count=int(raw_input())
# lst=list(map(int,raw_input().strip().split(' ')))

class Node:
  def __init__(self, data):
    self.data = data
    self.lchild = None
    self.rchild = None

class BST:
  def __init__(self, node_list):
    self.root = Node(node_list[0])
    for data in node_list[1:]:
        self.insert(data)

    # 搜索
  def search(self, node, parent, data):
    if node is None:
      return False, node, parent
    if node.data == data:
      return True, node, parent
    if node.data > data:
      return self.search(node.lchild, node, data)
    else:
      return self.search(node.rchild, node, data)

    # 插入
  def insert(self, data):
    flag, n, p = self.search(self.root, self.root, data)
    if not flag:
      new_node = Node(data)
      if data > p.data:
        p.rchild = new_node
      else:
        p.lchild = new_node

    # 删除
  def delete(self, root, data):
      flag, n, p = self.search(root, root, data)
      if flag is False:
        print "无该关键字，删除失败"
      else:
        if n.lchild is None:
          if n == p.lchild:
            p.lchild = n.rchild
          else:
            p.rchild = n.rchild
          del p
        elif n.rchild is None:
          if n == p.lchild:
            p.lchild = n.lchild
          else:
            p.rchild = n.lchild
          del p
        else:  # 左右子树均不为空
          pre = n.rchild
          if pre.lchild is None:
            n.data = pre.data
            n.rchild = pre.rchild
            del pre
          else:
            next = pre.lchild
            while next.lchild is not None:
              pre = next
              next = next.lchild
            n.data = next.data
            pre.lchild = next.rchild
            del p


    # 先序遍历
  def preOrderTraverse(self, node):
    if node is not None:
      print node.data,
      self.preOrderTraverse(node.lchild)
      self.preOrderTraverse(node.rchild)

  # 中序遍历
  def inOrderTraverse(self, node):
    if node is not None:
      self.inOrderTraverse(node.lchild)
      print node.data,
      self.inOrderTraverse(node.rchild)

  # 后序遍历
  def postOrderTraverse(self, node):
    if node is not None:
      self.postOrderTraverse(node.lchild)
      self.postOrderTraverse(node.rchild)
      print node.data,


# a = [49, 38, 65, 97, 60, 76, 13, 27, 5, 1]
a=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# lst.sort()
# print lst
bst = BST(a)  							# 创建二叉查找树
bst.preOrderTraverse(bst.root)
print
bst.postOrderTraverse(bst.root)

# bst.delete(bst.root, 49)
