import React, { useEffect, useState } from 'react';

const getApiUrl = () => {
  const codespace = process.env.CODESPACE_NAME;
  if (codespace) {
    return `https://${codespace}-8000.app.github.dev/api/leaderboard/`;
  }
  return 'http://localhost:8000/api/leaderboard/';
};

const Leaderboard = () => {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch(getApiUrl())
      .then((res) => {
        if (!res.ok) throw new Error('Network response was not ok');
        return res.json();
      })
      .then((data) => {
        setData(data);
        setLoading(false);
      })
      .catch((err) => {
        setError(err.message);
        setLoading(false);
      });
  }, []);

  if (loading) return <div>Loading leaderboard...</div>;
  if (error) return <div>Error: {error}</div>;

  return (
    <div>
      <h2>Leaderboard</h2>
      {data.length === 0 ? (
        <p>No leaderboard data found.</p>
      ) : (
        <ul>
          {data.map((entry) => (
            <li key={entry.id || entry._id}>
              Team: {entry.team} - Points: {entry.points}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default Leaderboard;
