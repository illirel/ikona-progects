function getSortNames(users) {
  const names = [];
  for (const user of users) {
    names.push(user['name']);
  }
  return names.sort();
}

const users = [
  { name: 'Bronn', gender: 'male', birthday: '1973-03-23' },
  { name: 'Reigar', gender: 'male', birthday: '1973-11-03' },
  { name: 'Eiegon', gender: 'male', birthday: '1963-11-03' },
  { name: 'Sansa', gender: 'female', birthday: '2012-11-03' },
];

console.log(getSortNames(users));
