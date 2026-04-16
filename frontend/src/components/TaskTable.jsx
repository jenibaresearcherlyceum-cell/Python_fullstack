function TaskTable({ tasks, onDelete, onEdit, role = "admin" }) {
  return (
    <div className="table-card">
      <table className="employee-table">
        <thead>
          <tr>
            <th>Task ID</th>
            <th>Title</th>
            <th>Description</th>
            <th>Assigned To</th>
            <th>Status</th>
            <th>Action</th>
          </tr>
        </thead>
        <tbody>
          {tasks.map((task, index) => (
            <tr key={index}>
              <td>{task[0]}</td>
              <td>{task[1]}</td>
              <td>{task[2]}</td>
              <td>{task[3]}</td>
              <td className={task[4] === 'Pending' ? "status-inactive" : "status-active"}>
                {task[4]}
              </td>
              <td>
                <button className="add-btn" style={{padding: '8px 12px', fontSize: '14px', marginRight: '10px'}} onClick={() => onEdit(task)}>
                  Edit
                </button>
                {role === "admin" && (
                  <button className="delete-btn" onClick={() => onDelete(task[0], task[1])}>
                    Delete
                  </button>
                )}
              </td>
            </tr>
          ))}
          {tasks.length === 0 && (
            <tr>
              <td colSpan="6" style={{textAlign: 'center', padding: '20px'}}>No Tasks Found.</td>
            </tr>
          )}
        </tbody>
      </table>
    </div>
  );
}

export default TaskTable;
