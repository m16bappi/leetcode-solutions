const bestClosingTime = (customers: string): number => {
  let result = 0,
    current = 0
  for (let i = 0; i < customers.length; i++) {
    if (customers[i] === 'Y') {
      current++
      if (current > 0) {
        result = i + 1
        current = 0
      }
    } else {
      current--
    }
  }
  return result
}

console.log(bestClosingTime('YYNY'))
console.log(bestClosingTime('NNNN'))
console.log(bestClosingTime('YYYY'))
