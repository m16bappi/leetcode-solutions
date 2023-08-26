function findLongestChain(pairs: number[][]): number {
  pairs.sort((a: number[], b: number[]) => a[1] - b[1])
  let curr: number = Number.MIN_SAFE_INTEGER,
    count: number = 0

  for (const [start, end] of pairs) {
    if (curr < start) {
      curr = end
      count++
    }
  }
  return count
}

// output should be 2 here
const inputs = [
  [1, 2],
  [2, 3],
  [3, 4],
]

console.log(findLongestChain(inputs))
