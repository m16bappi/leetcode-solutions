class TreeNode {
  val: number
  left: TreeNode | null | undefined
  right: TreeNode | null | undefined

  heads: TreeNode[] = []

  constructor(val: number, left?: TreeNode | null, right?: TreeNode | null) {
    this.val = val
    this.left = left
    this.right = right
  }

  buildTree(n: number) {
    if (n === 1) {
      this.heads.push(new TreeNode(n))
    }
    return this.heads
  }
}

const tree = new TreeNode(10)
console.log(tree.buildTree(1))
