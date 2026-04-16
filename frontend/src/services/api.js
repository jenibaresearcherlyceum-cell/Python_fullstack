const BASE_URL = import.meta.env.VITE_API_URL;

const handleApiError = async (response) => {
  if (response.status === 401) {
    localStorage.removeItem("token");
    window.location.reload();
  }
  const err = await response.json().catch(() => ({}));
  throw new Error(err.message || "API Error");
};

export const getEmployees = async () => {
  const response = await fetch(`${BASE_URL}/employees?page=1&limit=20`);
  if (!response.ok) await handleApiError(response);
  return response.json();
};

export const addEmployee = async (data) => {
  const token = localStorage.getItem("token");
  const response = await fetch(`${BASE_URL}/employees`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${token}`,
    },
    body: JSON.stringify(data),
  });
  if (!response.ok) await handleApiError(response);
  return response.json();
};

export const updateEmployee = async (id, data) => {
  const token = localStorage.getItem("token");
  const response = await fetch(`${BASE_URL}/employees/${id}`, {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${token}`,
    },
    body: JSON.stringify(data),
  });
  if (!response.ok) await handleApiError(response);
  return response.json();
};

export const deleteEmployee = async (id) => {
  const token = localStorage.getItem("token");
  const response = await fetch(`${BASE_URL}/employees/${id}`, {
    method: "DELETE",
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });
  if (!response.ok) await handleApiError(response);
  return response.json();
};

export const getTasks = async () => {
  const token = localStorage.getItem("token");
  const response = await fetch(`${BASE_URL}/tasks?page=1&limit=20`, {
    headers: { Authorization: `Bearer ${token}` }
  });
  if (!response.ok) await handleApiError(response);
  return response.json();
};

export const addTask = async (data) => {
  const token = localStorage.getItem("token");
  const response = await fetch(`${BASE_URL}/tasks`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${token}`,
    },
    body: JSON.stringify(data),
  });
  if (!response.ok) await handleApiError(response);
  return response.json();
};

export const updateTask = async (id, data) => {
  const token = localStorage.getItem("token");
  const response = await fetch(`${BASE_URL}/tasks/${id}`, {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${token}`,
    },
    body: JSON.stringify(data),
  });
  if (!response.ok) await handleApiError(response);
  return response.json();
};

export const deleteTask = async (id) => {
  const token = localStorage.getItem("token");
  const response = await fetch(`${BASE_URL}/tasks/${id}`, {
    method: "DELETE",
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });
  if (!response.ok) await handleApiError(response);
  return response.json();
};
