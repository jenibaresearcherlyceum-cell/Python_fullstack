function EmployeeTable({ employees, onDelete, onEdit, role = "admin" }) {
  return (
    <div className="table-card">
      <table className="employee-table">
        <thead>
          <tr>
            <th>Emp ID</th>
            <th>Name</th>
            <th>Department</th>
            <th>Designation</th>
            <th>Status</th>
            {role === "admin" && <th>Action</th>}
          </tr>
        </thead>
        <tbody>
          {employees.map((emp, index) => (
            <tr key={index}>
              <td>{emp[0]}</td>
              <td>{emp[1]}</td>
              <td>{emp[2]}</td>
              <td>{emp[3]}</td>
              <td className={emp[4] === 1 ? "status-active" : "status-inactive"}>
                {emp[4] === 1 ? "Active" : "Inactive"}
              </td>
              {role === "admin" && (
                <td>
                  <button className="add-btn" style={{padding: '8px 12px', fontSize: '14px', marginRight: '10px'}} onClick={() => onEdit(emp)}>
                    Edit
                  </button>
                  <button className="delete-btn" onClick={() => onDelete(emp[0], emp[1])}>
                    Delete
                  </button>
                </td>
              )}
            </tr>
          ))}
          {employees.length === 0 && (
            <tr>
               <td colSpan="6" style={{textAlign: 'center', padding: '20px'}}>No Employees Found.</td>
            </tr>
          )}
        </tbody>
      </table>
    </div>
  );
}

export default EmployeeTable;
