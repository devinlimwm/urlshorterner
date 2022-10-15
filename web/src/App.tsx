import React, { useState } from "react";
import "./App.css";
import axios from "axios";
import toast, { Toaster } from "react-hot-toast";
import Cookies from "js-cookie";

function App() {
  const [longUrl, setLongUrl] = useState("");
  const [shortUrl, setShortUrl] = useState("");

  const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
    // 👇️ prevent page refresh
    event.preventDefault();

    const params = new URLSearchParams();
    params.append("long_url", longUrl);

    const csrftoken = Cookies.get("csrftoken");

    try {
      const res = await axios({
        method: "post",
        url: "http://localhost:8000/create/",
        data: params,
        headers: { "X-CSRFToken": csrftoken },
      });

      setShortUrl(res.data.short_url);
    } catch (e: any) {
      toast.error(e?.response?.data?.message ?? "Error occurred");
    }
  };

  const linkComponent = shortUrl ? (
    <label>
      Shortened URL:
      <a
        href={`http://localhost:8000/goto/${shortUrl}`}
      >{`http://localhost:8000/goto/${shortUrl}`}</a>
    </label>
  ) : (
    <></>
  );

  return (
    <div className="App">
      <div>
        <Toaster />
      </div>
      <link
        rel="stylesheet"
        href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/css/bootstrap.min.css"
        integrity="sha384-0evHe/X+R7YkIZDRvuzKMRqM+OrBnVFBL6DOitfPri4tjfHxaWutUpFmBp4vmVor"
        crossOrigin="anonymous"
      />
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
        {linkComponent}
      </header>
    </div>
  );
}

export default App;
