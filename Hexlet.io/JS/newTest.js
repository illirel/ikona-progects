class User {
  constructor(name, id) {
    this.name = name;
    this.id = id;
  }
  jopa = 0;
  zp = 300;
  zpplusId() {
    jopa = this.id + this.zp;
  }
}
const admin = new User('Ilya', 9);
admin.age = 29;
admin.zp = 500;
admin.zpplusId;

const RO = new User('Viktor', 8);
RO.age = 33;

console.log(admin);
console.log(RO);
