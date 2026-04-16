import { useState } from "react";
import Login from "./pages/Login";
import Home from "./pages/Home";
import Dashboard from "./pages/Dashboard";
import TaskDashboard from "./pages/TaskDashboard";
import "./index.css";

function App() {
  const [isLoggedIn, setIsLoggedIn] = useState(
    !!localStorage.getItem("token")
  );
  const [page, setPage] = useState("home");

  const handleLogin = () => {
    setIsLoggedIn(true);
    setPage("home");
  };

  if (!isLoggedIn) {
    return <Login onLogin={handleLogin} />;
  }

  if (page === "employees") {
    return <Dashboard />;
  }
  
  if (page === "tasks") {
    return <TaskDashboard />;
  }

  return <Home onSelect={setPage} />;
}

export default App;