import React, { useState, useEffect } from 'react';
import Plotly from 'plotly.js-basic-dist';

function Heatmap() {
  const [data, setData] = useState([]);

  useEffect(() => {
    async function fetchData() {
      const response = await fetch('/api/matrix');
      const matrixData = await response.json();
      setData(matrixData);
    }
    fetchData();
  }, []);

  return (
    <div>
      <Plotly
        data={[
          {
            x: data.x,
            y: data.y,
            z: data.z,
            type: 'heatmap'
          }
        ]}
        layout={{
          width: 500,
          height: 500
        }}
      />
    </div>
  );
}

export default Heatmap;
