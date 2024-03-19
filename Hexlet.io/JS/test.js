function get(data, keys) {
  let result = data;
  for (const key of keys) {
    if (!Object.hasOwn(result, key)) {
      return null;
    }
    result = result[key];
  }
  return result;
}

const data = {
  user: 'ubuntu',
  hosts: {
    0: {
      name: 'web1',
    },
    1: {
      name: 'web2',
      null: 3,
      active: false,
    },
  },
};

console.log(get(data, ['hosts', 1, 'name']));
