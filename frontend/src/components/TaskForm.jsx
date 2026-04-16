import { useState, useEffect } from "react";

function TaskForm({ onAdd, selectedTask, isSubmitting, role = "admin" }) {
  const isUser = role === "user";

  const [form, setForm] = useState({
    task_id: "",
    title: "",
    description: "",
    assigned_to: "",
    status: "Pending"
  });

  const [errors, setErrors] = useState({});

  useEffect(() => {
    if (selectedTask) {
      setForm({
        task_id: selectedTask[0] || "",
        title: selectedTask[1] || "",
        description: selectedTask[2] || "",
        assigned_to: selectedTask[3] || "",
        status: selectedTask[4] || "Pending"
      });
      setErrors({});
    } else {
      setForm({
        task_id: "",
        title: "",
        description: "",
        assigned_to: "",
        status: "Pending"
      });
    }
  }, [selectedTask]);

  const handleChange = (e) => {
    setForm({
      ...form,
      [e.target.name]: e.target.value,
    });
    if (errors[e.target.name]) {
      setErrors({ ...errors, [e.target.name]: null });
    }
  };

  const validate = () => {
    let newErrors = {};
    if (!form.task_id || form.task_id.trim() === "") {
      newErrors.task_id = "Task ID is required";
    }
    if (!form.title || form.title.trim().length < 2) {
      newErrors.title = "Title must be at least 2 characters";
    }
    if (!form.description || form.description.trim() === "") {
      newErrors.description = "Description is required";
    }
    if (!form.assigned_to || form.assigned_to.toString().trim() === "") {
      newErrors.assigned_to = "Assignee Employee ID is required";
    }
    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    if (validate()) {
      onAdd({
        ...form,
        assigned_to: isNaN(form.assigned_to) ? form.assigned_to : Number(form.assigned_to),
      });

      if (!selectedTask) {
        setForm({
          task_id: "",
          title: "",
          description: "",
          assigned_to: "",
          status: "Pending"
        });
      }
      setErrors({});
    }
  };

  return (
    <div className="form-card">
      <h2 className="form-title">{selectedTask ? "Edit Task" : "Assign New Task"}</h2>
      <form onSubmit={handleSubmit}>
        <div className="form-fields">
          <div className="field-group">
            <label className="field-label">Task ID</label>
            <input
              className={`form-input ${errors.task_id ? "input-error" : ""}`}
              name="task_id"
              placeholder="e.g. T-101"
              value={form.task_id}
              onChange={handleChange}
              disabled={!!selectedTask || isUser}
            />
            {errors.task_id && <span className="error-text">{errors.task_id}</span>}
          </div>

          <div className="field-group">
            <label className="field-label">Title</label>
            <input
              className={`form-input ${errors.title ? "input-error" : ""}`}
              name="title"
              placeholder="e.g. Fix Login Bug"
              value={form.title}
              onChange={handleChange}
              disabled={isUser}
            />
            {errors.title && <span className="error-text">{errors.title}</span>}
          </div>

          <div className="field-group">
            <label className="field-label">Description</label>
            <input
              className={`form-input ${errors.description ? "input-error" : ""}`}
              name="description"
              placeholder="e.g. Resolve 500 error on /login"
              value={form.description}
              onChange={handleChange}
              disabled={isUser}
            />
            {errors.description && <span className="error-text">{errors.description}</span>}
          </div>

          <div className="field-group">
            <label className="field-label">Assign To (Emp ID)</label>
            <input
              className={`form-input ${errors.assigned_to ? "input-error" : ""}`}
              name="assigned_to"
              placeholder="e.g. 101"
              value={form.assigned_to}
              onChange={handleChange}
              disabled={isUser}
            />
            {errors.assigned_to && <span className="error-text">{errors.assigned_to}</span>}
          </div>
          
          {selectedTask && (
            <div className="field-group">
              <label className="field-label">Status</label>
              <select
                className="form-input"
                name="status"
                value={form.status}
                onChange={handleChange}
              >
                <option value="Pending">Pending</option>
                <option value="Completed">Completed</option>
              </select>
            </div>
          )}
        </div>

        <button className="add-btn" type="submit" disabled={isSubmitting}>
          {isSubmitting ? "Processing..." : (selectedTask ? "Update Task" : "+ Add Task")}
        </button>
        {selectedTask && (
          <button 
            type="button" 
            className="add-btn modal-cancel" 
            style={{marginLeft: "10px", background: "#f1f5f9", color: "#475569"}} 
            onClick={() => onAdd(null)}
          >
            Cancel Edit
          </button>
        )}
      </form>
    </div>
  );
}

export default TaskForm;
