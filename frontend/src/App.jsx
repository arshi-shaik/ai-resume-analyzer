import { useState } from "react";
import "./App.css";

const API_URL =
  "https://ai-resume-analyzer-9re2.onrender.com";

function App() {
  const [resume, setResume] = useState(null);
  const [jobDescription, setJobDescription] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const analyzeResume = async () => {
    if (!resume) {
      setError("Please upload your resume PDF.");
      return;
    }

    if (!jobDescription.trim()) {
      setError("Please enter a job description.");
      return;
    }

    setLoading(true);
    setError("");
    setResult(null);

    const formData = new FormData();

    formData.append("resume", resume);
    formData.append("job_description", jobDescription);

    try {
      const response = await fetch(`${API_URL}/analyze`, {
        method: "POST",
        body: formData,
      });

      if (!response.ok) {
        throw new Error("Failed to analyze resume.");
      }

      const data = await response.json();

      setResult(data);
    } catch (err) {
      setError(
        "Unable to connect to the backend. Please try again."
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app">

      <header className="header">
        <div className="logo">
          <span>AI</span> Resume Analyzer
        </div>

        <p>
          AI-powered resume analysis and job matching
        </p>
      </header>

      <main className="container">

        <section className="hero">
          <h1>
            Find out how well your resume
            <span> matches the job</span>
          </h1>

          <p>
            Upload your resume and enter a job description to discover
            matched skills, missing skills and your overall match score.
          </p>
        </section>

        <section className="analyzer-card">

          <div className="input-section">

            <label>Upload Resume</label>

            <div className="upload-box">

              <input
                type="file"
                accept=".pdf"
                onChange={(event) => {
                  setResume(event.target.files[0]);
                  setError("");
                }}
              />

              {resume ? (
                <div className="file-name">
                  📄 {resume.name}
                </div>
              ) : (
                <div className="upload-text">
                  <div className="upload-icon">
                    📄
                  </div>

                  <strong>
                    Choose your resume PDF
                  </strong>

                  <span>
                    PDF files only
                  </span>
                </div>
              )}

            </div>

          </div>

          <div className="input-section">

            <label>
              Job Description
            </label>

            <textarea
              value={jobDescription}
              onChange={(event) =>
                setJobDescription(event.target.value)
              }
              placeholder="Paste the job description here..."
              rows="12"
            />

          </div>

          {error && (
            <div className="error">
              ⚠️ {error}
            </div>
          )}

          <button
            className="analyze-button"
            onClick={analyzeResume}
            disabled={loading}
          >
            {loading
              ? "Analyzing Resume..."
              : "Analyze Resume"}
          </button>

        </section>

        {result && (
          <section className="results">

            <h2>
              Analysis Results
            </h2>

            <div className="score-card">

              <div className="score">
                {result.match_percentage}%
              </div>

              <div>
                <h3>
                  Resume Match
                </h3>

                <p>
                  Your resume matches{" "}
                  {result.match_percentage}% of the
                  recognized skills in the job description.
                </p>
              </div>

            </div>

            <div className="result-grid">

              <div className="result-card matched">

                <h3>
                  ✅ Matched Skills
                </h3>

                {result.matched_skills.length > 0 ? (
                  <div className="skills">

                    {result.matched_skills.map((skill) => (
                      <span key={skill}>
                        {skill}
                      </span>
                    ))}

                  </div>
                ) : (
                  <p>
                    No matching skills found.
                  </p>
                )}

              </div>

              <div className="result-card missing">

                <h3>
                  ⚠️ Missing Skills
                </h3>

                {result.missing_skills.length > 0 ? (
                  <div className="skills">

                    {result.missing_skills.map((skill) => (
                      <span key={skill}>
                        {skill}
                      </span>
                    ))}

                  </div>
                ) : (
                  <p>
                    No missing skills detected.
                  </p>
                )}

              </div>

            </div>

            <div className="resume-skills">

              <h3>
                Skills Detected in Your Resume
              </h3>

              <div className="skills">

                {result.resume_skills.map((skill) => (
                  <span key={skill}>
                    {skill}
                  </span>
                ))}

              </div>

            </div>

          </section>
        )}

      </main>

      <footer>
        <p>
          AI Resume Analyzer • Built with React + FastAPI
        </p>
      </footer>

    </div>
  );
}

export default App;