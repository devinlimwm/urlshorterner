import React, { useState } from "react";
import "./App.css";

function App() {
  const [url, setUrl] = useState("");

  const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
    // 👇️ prevent page refresh
    event.preventDefault();
  };

  return (
    <div className="App">
      <header className="App-header">
        <form onSubmit={handleSubmit}>
          <label>
            Enter URL to shorten:
            <input
              type="text"
              value={url}
              onChange={(e) => setUrl(e.target.value)}
            />
          </label>
          <input type="submit" value="Submit" />
        </form>
      </header>
    </div>
  );
}

export default App;
