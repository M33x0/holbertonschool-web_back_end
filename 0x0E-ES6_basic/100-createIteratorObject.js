export default function createIteratorObject(report) {
  const arrEmp = [];
  for (const element of Object.keys(report.allEmployees)) {
    arrEmp.push(...report.allEmployees[element]);
  }
  return arrEmp;
}

