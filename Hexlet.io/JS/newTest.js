const array = [1, 1, [1, [1, 2], 1], [1]];

const sum = arr => {
  return arr.reduce((total, item) => {
    if (Array.isArray(item)) {
      return total + sum(item);
    } else {
      return total + item;
    }
  }, 0);
};
console.log(sum(array));
