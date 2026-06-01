import { useEffect, useState } from "react";
import axios from "axios";
import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  PieChart,
  Pie,
  Cell,
  Legend,
} from "recharts";

function App() {
  const [cityData, setCityData] = useState([]);
  const [categoryData, setCategoryData] = useState([]);
  const [sourceData, setSourceData] = useState([]);

  useEffect(() => {
    axios.get("http://127.0.0.1:8000/city-wise")
      .then((res) => setCityData(res.data));

    axios.get("http://127.0.0.1:8000/category-wise")
      .then((res) => setCategoryData(res.data));

    axios.get("http://127.0.0.1:8000/source-wise")
      .then((res) => setSourceData(res.data));
  }, []);

  const colors = [
    "#0088FE",
    "#00C49F",
    "#FFBB28",
    "#FF8042",
    "#A28CFF",
    "#FF6699",
  ];

  return (
    <div
      style={{
        padding: "30px",
        fontFamily: "Arial",
      }}
    >
      <h1 style={{ textAlign: "center" }}>
        Business Listings Dashboard
      </h1>

      <h2>City Wise Business Count</h2>

      <BarChart width={900} height={350} data={cityData}>
        <XAxis dataKey="city" />
        <YAxis />
        <Tooltip />
        <Bar dataKey="count" fill="#3b82f6" />
      </BarChart>

      <br />

      <h2>Category Wise Business Count</h2>

      <BarChart width={900} height={350} data={categoryData}>
        <XAxis dataKey="category" />
        <YAxis />
        <Tooltip />
        <Bar dataKey="count" fill="#10b981" />
      </BarChart>

      <br />

      <h2>Source Wise Distribution</h2>

      <PieChart width={600} height={400}>
        <Pie
          data={sourceData}
          dataKey="count"
          nameKey="source"
          outerRadius={130}
          label
        >
          {sourceData.map((entry, index) => (
            <Cell
              key={index}
              fill={colors[index % colors.length]}
            />
          ))}
        </Pie>

        <Tooltip />
        <Legend />
      </PieChart>
    </div>
  );
}

export default App;