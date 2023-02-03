import React, { useState, useEffect } from "react";
import Plot from "react-plotly.js";
import axios from "axios";

const HeatmapV2 = () => {
  const [data2D, setData2D] = useState([]);
  const [data3D, setData3D] = useState([]);
  const [random2D, setRandom2D] = useState([]);

  useEffect(() => {
    axios
      .get("http://localhost:5555/heatmap_data_2d")
      .then(res => setData2D(res.data))
      .catch(err => console.error(err));

    axios
      .get("http://localhost:5555/heatmap_data_3d")
      .then(res => setData3D(res.data))
      .catch(err => console.error(err));

      axios
      .get("http://localhost:5555/heatmap_random_2d")
      .then(res => setRandom2D(res.data))
      .catch(err => console.error(err));
  }, []);


      return (
        <div>
          <Plot
            data={[
              {
                z: data2D,
                type: "heatmap",
                colorscale: "Viridis"
              }
            ]}
          />
          <Plot
            data={[
              {
                type: "surface",                
                x: [...Array(501).keys()].slice(1),
                y: [...Array(501).keys()].slice(1),
                z: random2D,
                colorscale: "Viridis",
              }
            ]}
            layout={{
              width: 800,
              height: 600,
              margin: {
                l: 50,
                r: 50,
                b: 80,
                t: 90,
                pad: 4
              },
              title: "3D matrix heatmap",
              }
            }
          />
        </div>
      );
    };
export default HeatmapV2;