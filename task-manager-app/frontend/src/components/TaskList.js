import React from 'react';

const TaskList = ({ tasks, onDelete, onToggle }) => {
  return (
    <div>
      {tasks.map((task) => (
        <div key={task.id} style={{ backgroundColor: '#f5f5f5', padding: '10px', marginTop: '10px' }}>
          <input
            type="checkbox"
            checked={task.completed}
            onChange={() => onToggle(task)}
            style={{ marginRight: '10px' }}
          />
          <strong style={{ textDecoration: task.completed ? 'line-through' : 'none' }}>
            {task.title}
          </strong>
          <p style={{ textDecoration: task.completed ? 'line-through' : 'none' }}>
            {task.description}
          </p>
          <button onClick={() => onDelete(task.id)} style={{ backgroundColor: 'red', color: 'white' }}>
            Delete
          </button>
        </div>
      ))}
    </div>
  );
};

export default TaskList;