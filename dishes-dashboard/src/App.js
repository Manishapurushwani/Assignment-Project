import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [dishes, setDishes] = useState([]);

  useEffect(() => {
    fetchDishes();
  }, []);

  const fetchDishes = async () => {
    try {
      const response = await axios.get('http://127.0.0.1:5000/api/dishes');
      setDishes(response.data);
    } catch (error) {
      console.error('Error fetching dishes:', error);
    }
  };

  const togglePublish = async (dishId) => {
    try {
      const response = await axios.put(`http://127.0.0.1:5000/api/dishes/${dishId}/publish`);
      setDishes(dishes.map(dish => (dish.dishId === dishId ? { ...dish, isPublished: response.data.isPublished } : dish)));
    } catch (error) {
      console.error('Error toggling publish status:', error);
    }
  };

  return (
    <div className="App">
      <h1>Dish Dashboard</h1>
      <div className="dish-list">
        {dishes.map(dish => (
          <div key={dish.dishId} className="dish-card">
            <img src={dish.imageUrl} alt={dish.dishName} />
            <h2>{dish.dishName}</h2>
            <button onClick={() => togglePublish(dish.dishId)}>
              {dish.isPublished ? 'Unpublish' : 'Publish'}
            </button>
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;
