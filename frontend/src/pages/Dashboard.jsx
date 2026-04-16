import { useEffect, useState } from "react";
import { getEmployees, addEmployee, updateEmployee, deleteEmployee } from "../services/api";
import EmployeeTable from "../components/EmployeeTable";
import EmployeeForm from "../components/EmployeeForm";
import LoadingSpinner from "../components/LoadingSpinner";
import Notification from "../components/Notification";
import ConfirmModal from "../components/ConfirmModal";

function Dashboard() {
  const [employees, setEmployees] = useState([]);
  const [loading, setLoading] = useState(true);
  const [saving, setSaving] = useState(false);
  
  const [error, setError] = useState("");
  const [success, setSuccess] = useState("");

  const [employeeToDelete, setEmployeeToDelete] = useState(null);
  const [selectedEmp, setSelectedEmp] = useState(null);

  const fetchEmployees = async () => {
    try {
      setLoading(true);
      const data = await getEmployees();
      setEmployees(data.data || []);
      setError("");
    } catch (err) {
      setError(err.message || "Unable to load employee data");
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchEmployees();
  }, []);

  const handleLogout = () => {
    localStorage.removeItem("token");
    window.location.reload();
  };

  const handleEdit = (emp) => {
    setSelectedEmp(emp);
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  const handleSubmit = async (form) => {
    if (form === null) {
      setSelectedEmp(null);
      return;
    }

    try {
      setSaving(true);
      if (selectedEmp) {
        await updateEmployee(form.emp_id, form);
        setSuccess(`Employee ${form.name} updated successfully!`);
      } else {
        await addEmployee(form);
        setSuccess(`Employee ${form.name} added successfully!`);
      }
      
      await fetchEmployees();
      setSelectedEmp(null);
      setError("");
    } catch (err) {
      setError(err.message || "Failed to process employee");
      setSuccess("");
    } finally {
      setSaving(false);
    }
  };

  const handleDeleteRequest = (id, name) => {
    setEmployeeToDelete({ id, name });
  };

  const handleConfirmDelete = async () => {
    if (!employeeToDelete) return;
    try {
      await deleteEmployee(employeeToDelete.id);
      await fetchEmployees();
      if(selectedEmp && selectedEmp[0] === employeeToDelete.id) {
        setSelectedEmp(null);
      }
      setSuccess(`Employee ${employeeToDelete.name} deleted successfully!`);
      setError("");
    } catch (err) {
      setError(err.message || "Failed to delete employee");
      setSuccess("");
    } finally {
      setEmployeeToDelete(null);
    }
  };

  const role = localStorage.getItem("role") || "user";

  return (
    <div className="dashboard-container">
      <Notification type="success" message={success} onClose={() => setSuccess("")} />
      <Notification type="error" message={error} onClose={() => setError("")} />

      <div style={{display: "flex", justifyContent: "space-between", alignItems: "center"}}>
         <div>
           <h1 className="dashboard-title" style={{marginBottom: "5px"}}>Employee Dashboard</h1>
           <p style={{color: "#64748b", fontSize: "14px", marginTop: "0"}}>Logged in as: <strong>{role.toUpperCase()}</strong></p>
         </div>
         <button className="delete-btn" style={{padding: "8px 16px"}} onClick={handleLogout}>Logout</button>
      </div>

      {role === "admin" && <EmployeeForm onAdd={handleSubmit} selectedEmp={selectedEmp} isSubmitting={saving} />}

      {loading && <LoadingSpinner />}

      {!loading && (
        <EmployeeTable employees={employees} onDelete={handleDeleteRequest} onEdit={handleEdit} role={role} />
      )}

      <ConfirmModal 
        isOpen={!!employeeToDelete}
        title="Confirm Deletion"
        message={`Are you sure you want to delete ${employeeToDelete?.name}? This action cannot be undone.`}
        onConfirm={handleConfirmDelete}
        onCancel={() => setEmployeeToDelete(null)}
      />
    </div>
  );
}

export default Dashboard;
