import React, { useEffect } from "react";

function Notification({ type, message, onClose }) {
  useEffect(() => {
    if (message) {
      const timer = setTimeout(() => {
        onClose();
      }, 4000); // auto dismiss after 4s
      return () => clearTimeout(timer);
    }
  }, [message, onClose]);

  if (!message) return null;

  return (
    <div className={`notification ${type === "success" ? "notification-success" : "notification-error"}`}>
      <span>{message}</span>
      <button className="notification-close" onClick={onClose}>&times;</button>
    </div>
  );
}

export default Notification;
