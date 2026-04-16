import { useState } from "react";
import Notification from "../components/Notification";
import BASE_URL from "../services/api";

function Login({ onLogin }) {
  const [formData, setFormData] = useState({
    username: "",
    password: "",
  });
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
    setError(""); // Clear error on typing
  };

  const handleSubmit = async (e) => {
    e.preventDefault(); // Good practice if they hit Enter

    if(!formData.username || !formData.password) {
      setError("Please enter both username and password");
      return;
    }

    try {
      setLoading(true);
      const response = await fetch(
        `${BASE_URL}/login`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(formData),
        }
      );

      const data = await response.json();

      if (response.ok) {
        localStorage.setItem("token", data.token);
        localStorage.setItem("username", data.user.username);
        localStorage.setItem("role", data.user.role || "user");

        onLogin();
      } else {
        setError(data.message || "Invalid username or password");
      }
    } catch (error) {
      console.error("LOGIN ERROR:", error);
      setError("Network or API Error. Please wait and try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="dashboard-container" style={{maxWidth: "400px", margin: "100px auto"}}>
      <Notification type="error" message={error} onClose={() => setError("")} />
      
      <div className="form-card">
        <h1 className="dashboard-title" style={{textAlign: "center"}}>Login</h1>

        <form onSubmit={handleSubmit} className="form-fields" style={{display: "flex", flexDirection: "column", gap: "15px"}}>
          <div className="field-group">
            <label className="field-label">Username</label>
            <input
              type="text"
              name="username"
              placeholder="Enter Username"
              className="form-input"
              value={formData.username}
              onChange={handleChange}
            />
          </div>

          <div className="field-group">
            <label className="field-label">Password</label>
            <input
              type="password"
              name="password"
              placeholder="Enter Password"
              className="form-input"
              value={formData.password}
              onChange={handleChange}
            />
          </div>

          <button 
            type="submit" 
            className="add-btn" 
            disabled={loading}
            style={{marginTop: "10px", width: "100%"}}
          >
            {loading ? "Processing..." : "Login"}
          </button>
        </form>
      </div>
    </div>
  );
}

export default Login;