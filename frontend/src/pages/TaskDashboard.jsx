import { useEffect, useState } from "react";
import { getTasks, addTask, updateTask, deleteTask } from "../services/api";
import TaskTable from "../components/TaskTable";
import TaskForm from "../components/TaskForm";
import LoadingSpinner from "../components/LoadingSpinner";
import Notification from "../components/Notification";
import ConfirmModal from "../components/ConfirmModal";

function TaskDashboard() {
  const [tasks, setTasks] = useState([]);
  const [loading, setLoading] = useState(true);
  const [saving, setSaving] = useState(false);
  
  const [error, setError] = useState("");
  const [success, setSuccess] = useState("");

  const [taskToDelete, setTaskToDelete] = useState(null);
  const [selectedTask, setSelectedTask] = useState(null);

  const fetchTasks = async () => {
    try {
      setLoading(true);
      const data = await getTasks();
      setTasks(data.data || []);
      setError("");
    } catch (err) {
      setError(err.message || "Unable to load tasks data");
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchTasks();
  }, []);

  const handleLogout = () => {
    localStorage.removeItem("token");
    window.location.reload();
  };

  const handleEdit = (task) => {
    setSelectedTask(task);
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  const handleSubmit = async (form) => {
    if (form === null) {
      setSelectedTask(null);
      return;
    }

    try {
      setSaving(true);
      if (selectedTask) {
        await updateTask(form.task_id, form);
        setSuccess(`Task "${form.title}" updated successfully!`);
      } else {
        await addTask(form);
        setSuccess(`Task "${form.title}" added successfully!`);
      }
      
      await fetchTasks();
      setSelectedTask(null);
      setError("");
    } catch (err) {
      setError(err.message || "Failed to process task");
      setSuccess("");
    } finally {
      setSaving(false);
    }
  };

  const handleDeleteRequest = (id, title) => {
    setTaskToDelete({ id, title });
  };

  const handleConfirmDelete = async () => {
    if (!taskToDelete) return;
    try {
      await deleteTask(taskToDelete.id);
      await fetchTasks();
      if(selectedTask && selectedTask[0] === taskToDelete.id) {
        setSelectedTask(null);
      }
      setSuccess(`Task "${taskToDelete.title}" deleted successfully!`);
      setError("");
    } catch (err) {
      setError(err.message || "Failed to delete task");
      setSuccess("");
    } finally {
      setTaskToDelete(null);
    }
  };

  const role = localStorage.getItem("role") || "user";

  return (
    <div className="dashboard-container">
      <Notification type="success" message={success} onClose={() => setSuccess("")} />
      <Notification type="error" message={error} onClose={() => setError("")} />

      <div style={{display: "flex", justifyContent: "space-between", alignItems: "center"}}>
         <div>
           <h1 className="dashboard-title" style={{marginBottom: "5px"}}>Task Dashboard</h1>
           <p style={{color: "#64748b", fontSize: "14px", marginTop: "0"}}>Logged in as: <strong>{role.toUpperCase()}</strong></p>
         </div>
         <button className="delete-btn" style={{padding: "8px 16px"}} onClick={handleLogout}>Logout</button>
      </div>

      {(role === "admin" || selectedTask) && <TaskForm onAdd={handleSubmit} selectedTask={selectedTask} isSubmitting={saving} role={role} />}

      {loading && <LoadingSpinner />}

      {!loading && (
        <TaskTable tasks={tasks} onDelete={handleDeleteRequest} onEdit={handleEdit} role={role} />
      )}

      <ConfirmModal 
        isOpen={!!taskToDelete}
        title="Confirm Deletion"
        message={`Are you sure you want to delete task "${taskToDelete?.title}"? This action cannot be undone.`}
        onConfirm={handleConfirmDelete}
        onCancel={() => setTaskToDelete(null)}
      />
    </div>
  );
}

export default TaskDashboard;
