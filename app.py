from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
  {
    "job_title": "Software Engineer",
    "company": "TechCorp",
    "location": "San Francisco, CA",
    "salary": "$120,000",
    "description": "Develop and maintain software applications."
  },
  {
    "job_title": "Data Scientist",
    "company": "DataInsights",
    "location": "New York, NY",
    "salary": "$110,000",
    "description": "Analyze and interpret complex data to assist business decisions."
  },

  {
    "job_title": "Product Manager",
    "company": "InnovateTech",
    "location": "Seattle, WA",
    "salary": "$130,000",
    "description": "Lead the development and launch of new products."
  },

  {
    "job_title": "UX Designer",
    "company": "DesignHub",
    "location": "Austin, TX",
    "salary": "$90,000",
    "description": "Design user interfaces and experiences for web and mobile applications."
  }
]

@app.route('/')
def hello_world():
    return render_template('jobs.html', jobs=JOBS)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)