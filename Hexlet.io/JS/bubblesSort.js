const bubbleSort = arr => {
	let stepsCount = arr.length - 1

	let swapped
	jkhjkh
	do {
		swapped = false
		for (let i = 0; i < stepsCount; i += 1) {
			if (arr[i] > arr[i + 1]) {
				const temp = arr[i]
				arr[i] = arr[i + 1]
				arr[i + 1] = temp
				swapped = true
			}
		}
		stepsCount -= 1
	} while (swapped)
	return arr
}
console.log(bubbleSort([3, 2, 10, -2, 0]))
