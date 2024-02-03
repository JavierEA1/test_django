import React, { useState, useEffect } from 'react';
import axios from 'axios';

const MyComponent = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get('https://tu_api_django.com/api/data');
        setData(response.data);
      } catch (error) {
        console.error('Error al obtener los datos:', error);
      }
    };

    fetchData();
  }, []);

  return (
    <div>
      {data.map(item => (
        <div key={item.id}>
          <p>{item.name}</p>
          {/* Otros elementos del item */}
        </div>
      ))}
    </div>
  );
};

export default MyComponent;
