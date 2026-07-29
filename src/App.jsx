import { useState } from "react";

function App() {
  const [likes, setLikes] = useState(0);

  // Like button handler
  const handleLike = () => {
    setLikes(likes + 1);
  };

  // Reset button handler
  const handleReset = () => {
    setLikes(0);
  };

  return (
    <div style={{ textAlign: "center", marginTop: "100px" }}>
      <h1>Like Button Application</h1>

      <h2>Likes Count: {likes}</h2>

      <button onClick={handleLike}>
        Like
      </button>

      <button onClick={handleReset} style={{ marginLeft: "10px" }}>
        Reset
      </button>
    </div>
  );
}

export default App;