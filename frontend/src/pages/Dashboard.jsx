import { useEffect, useState } from "react";

function Dashboard() {
  const [employees, setEmployees] = useState([]);

  useEffect(() => {
    fetch("https://python-fullstack-q5hz.onrender.com/employees")
      .then((res) => res.json())
      .then((data) => {
        console.log(data);
        setEmployees(data.data);
      })
      .catch((err) => console.log(err));
  }, []);

  return (
    <div>
      <h2>Employees</h2>
      {employees.map((emp, index) => (
        <p key={index}>{emp[1]}</p>
      ))}
    </div>
  );
}

export default Dashboard;