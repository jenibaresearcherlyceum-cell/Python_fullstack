function Home({ onSelect }) {
  return (
    <div className="dashboard-container">
      <h1 className="dashboard-title">Dashboard Menu</h1>

      <div className="form-row">
        <button className="add-btn" onClick={() => onSelect("employees")}>
          Employees
        </button>

        <button className="add-btn" onClick={() => onSelect("tasks")}>
          Tasks
        </button>
      </div>
    </div>
  );
}

export default Home;
