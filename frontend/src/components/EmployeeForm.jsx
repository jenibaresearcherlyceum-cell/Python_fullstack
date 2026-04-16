import { useState, useEffect } from "react";

function EmployeeForm({ onAdd, selectedEmp, isSubmitting }) {
  const [form, setForm] = useState({
    emp_id: "",
    name: "",
    department: "",
    designation: "",
  });

  const [errors, setErrors] = useState({});

  useEffect(() => {
    if (selectedEmp) {
      setForm({
        emp_id: selectedEmp[0] || "",
        name: selectedEmp[1] || "",
        department: selectedEmp[2] || "",
        designation: selectedEmp[3] || "",
      });
      setErrors({});
    } else {
      setForm({
        emp_id: "",
        name: "",
        department: "",
        designation: "",
      });
    }
  }, [selectedEmp]);

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
    if (!form.emp_id || isNaN(form.emp_id) || Number(form.emp_id) <= 0) {
      newErrors.emp_id = "Valid Employee ID is required";
    }
    if (!form.name || form.name.trim().length < 2) {
      newErrors.name = "Name must be at least 2 characters";
    }
    if (!form.department || form.department.trim() === "") {
      newErrors.department = "Department is required";
    }
    if (!form.designation || form.designation.trim() === "") {
      newErrors.designation = "Designation is required";
    }
    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    if (validate()) {
      onAdd({
        ...form,
        emp_id: Number(form.emp_id),
      });

      if (!selectedEmp) {
        setForm({
          emp_id: "",
          name: "",
          department: "",
          designation: "",
        });
      }
      setErrors({});
    }
  };

  return (
    <div className="form-card">
      <h2 className="form-title">{selectedEmp ? "Edit Employee" : "Add New Employee"}</h2>
      <form onSubmit={handleSubmit}>
        <div className="form-fields">
          <div className="field-group">
            <label className="field-label">Employee ID</label>
            <input
              className={`form-input ${errors.emp_id ? "input-error" : ""}`}
              type="number"
              name="emp_id"
              placeholder="Enter employee ID"
              value={form.emp_id}
              onChange={handleChange}
              disabled={!!selectedEmp} /* IDs generally shouldn't change */
            />
            {errors.emp_id && <span className="error-text">{errors.emp_id}</span>}
          </div>

          <div className="field-group">
            <label className="field-label">Full Name</label>
            <input
              className={`form-input ${errors.name ? "input-error" : ""}`}
              name="name"
              placeholder="Enter Your Name"
              value={form.name}
              onChange={handleChange}
            />
            {errors.name && <span className="error-text">{errors.name}</span>}
          </div>

          <div className="field-group">
            <label className="field-label">Department</label>
            <input
              className={`form-input ${errors.department ? "input-error" : ""}`}
              name="department"
              placeholder="Enter Department"
              value={form.department}
              onChange={handleChange}
            />
            {errors.department && <span className="error-text">{errors.department}</span>}
          </div>

          <div className="field-group">
            <label className="field-label">Designation</label>
            <input
              className={`form-input ${errors.designation ? "input-error" : ""}`}
              name="designation"
              placeholder="Enter Designation"
              value={form.designation}
              onChange={handleChange}
            />
            {errors.designation && <span className="error-text">{errors.designation}</span>}
          </div>
        </div>

        <button className="add-btn" type="submit" disabled={isSubmitting}>
          {isSubmitting ? "Processing..." : (selectedEmp ? "Update Employee" : "+ Add Employee")}
        </button>
        {selectedEmp && (
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

export default EmployeeForm;
