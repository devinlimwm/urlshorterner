import React, { useState } from "react";
import { ajax } from "rxjs/ajax";
import { catchError, take } from "rxjs/operators";
import "./App.css";

function App() {
  const [longUrl, setLongUrl] = useState("");
  const [shortUrl, setShortUrl] = useState("");

  const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
    // 👇️ prevent page refresh
    event.preventDefault();

    const obs = ajax
      .post<string>("localhost:8000/url/short", longUrl)
      .pipe(
        catchError((error) => error),
        take(1)
      )
      .subscribe((response: string | unknown) =>
        setShortUrl(response as string)
      );

    return () => obs.unsubscribe();
  };

  return (
    <div className="App">
      <header className="App-header">
        <form onSubmit={handleSubmit}>
          <label>
            Enter URL to shorten:
            <input
              type="text"
              value={longUrl}
              onChange={(e) => setLongUrl(e.target.value)}
            />
          </label>
          <input type="submit" value="Submit" />
        </form>
        <label>
          Shortened URL:
          <input type="text" value={shortUrl} />
        </label>
      </header>
    </div>
  );
}

export default App;
