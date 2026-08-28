from flask import Flask

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Student Registration</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #000000; /* Changed to Black */
            margin: 0;
            padding: 0;
            color: #ffffff; /* Changed text to white for readability */        }
        .header {
            background-color: #ff0000; /* Changed to Red */          
            text-align: center;
            padding: 30px;
            border-bottom: 2px solid #555;
        }
        .header h1 {
            margin: 0;
            font-size: 28px;
        }
        .header p {
            margin: 10px 0 0 0;
            font-size: 14px;
        }
        .container {
            width: 90%;
            max-width: 1200px;
            margin: 20px auto;
        }
        .card {
            background-color: #f9f9f9;
            border: 1px solid #777;
            padding: 20px;
            margin-bottom: 20px;
            box-shadow: 3px 3px 8px rgba(0,0,0,0.1);
        }
        .card-header {
            background-color: #84ffc9;
            padding: 10px;
            font-weight: bold;
            text-align: center;
            border: 1px solid #777;
            margin: -20px -20px 20px -20px; /* Stretch to card edges */
        }
        .center-text { text-align: center; }
        .row {
            display: flex;
            gap: 20px;
            margin-bottom: 20px;
        }
        .col { flex: 1; }
        
        /* Form Styling */
        .form-group { margin-bottom: 15px; }
        .form-group label { display: block; margin-bottom: 5px; font-size: 14px; }
        .form-group input, .form-group select {
            width: 100%;
            padding: 8px;
            border: 1px solid #999;
            box-sizing: border-box;
        }
        button {
            padding: 5px 15px;
            background-color: #e0e0e0;
            border: 1px solid #777;
            cursor: pointer;
        }
        button:hover { background-color: #ccc; }

        /* Table Styling */
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 10px;
            background-color: #e6e6e6;
        }
        th, td {
            border: 1px solid #777;
            padding: 10px;
            text-align: center;
        }
        th { background-color: #84ffc9; font-weight: bold; }
        
        /* Lists */
        ul, ol { margin-top: 5px; padding-left: 20px; }

        .footer {
            background-color: #84ffc9;
            text-align: center;
            padding: 20px;
            border-top: 2px solid #555;
            margin-top: 40px;
        }
    </style>
</head>
<body>

    <div class="header">
        <h1>Student Registration Portal</h1>
        <p>Welcome to our student registration page</p>
    </div>

    <div class="container">
        <!-- About Section -->
        <div class="card center-text">
            <h2>About the Course</h2>
            <p>Welcome to the Web Development course. In this course, students will learn HTML, CSS and JavaScript.</p>
            <a href="https://google.com" target="_blank" style="color: blue;">Visit Google</a>
        </div>

        <!-- Registration & Info Row -->
        <div class="row">
            <!-- Form Card -->
            <div class="col card" style="padding-top: 0;">
                <div class="card-header">Student Registration</div>
                <div class="form-group">
                    <label>Name:</label>
                    <input type="text">
                </div>
                <div class="form-group">
                    <label>Email:</label>
                    <input type="email">
                </div>
                <div class="form-group">
                    <label>Course:</label>
                    <select>
                        <option>HTML</option>
                        <option>CSS</option>
                        <option>JavaScript</option>
                    </select>
                </div>
                <button>Register</button>
            </div>

            <!-- Image/Info Card -->
            <div class="col card" style="padding-top: 0;">
                <div class="card-header">Learn Web Development</div>
                <div class="center-text" style="padding: 20px;">
                    <p style="font-size: 50px; margin: 0;">💻</p>
                    <p>Learn the fundamentals of web development and build your own websites.</p>
                </div>
            </div>
        </div>

        <!-- Topics & Skills -->
        <div class="card" style="padding: 0;">
            <div class="card-header" style="margin: 0; text-align: left;">Course Topics</div>
            <div style="padding: 15px;">
                <ol>
                    <li>HTML Basics</li>
                    <li>CSS Basics</li>
                    <li>JavaScript Basics</li>
                </ol>
            </div>
        </div>

        <div class="card" style="padding: 0;">
            <div class="card-header" style="margin: 0; text-align: left;">Required Skills</div>
            <div style="padding: 15px;">
                <ul>
                    <li>Basic Computer Knowledge</li>
                    <li>Problem Solving</li>
                    <li>Interest in Web Development</li>
                </ul>
            </div>
        </div>

        <!-- Student Details Table -->
        <div class="card" style="padding: 0; border: none; box-shadow: none; background: transparent;">
            <div class="card-header" style="margin: 0;">Student Details</div>
            <table>
                <tr>
                    <th>Name</th>
                    <th>Gender</th>
                    <th>Course</th>
                    <th>Marks</th>
                </tr>
                <tr>
                    <td>Rahul</td>
                    <td>Male</td>
                    <td>HTML</td>
                    <td>85</td>
                </tr>
                <tr>
                    <td>Priya</td>
                    <td>Female</td>
                    <td>CSS</td>
                    <td>90</td>
                </tr>
                <tr>
                    <td>Amit</td>
                    <td>Male</td>
                    <td>JavaScript</td>
                    <td>88</td>
                </tr>
                <tr style="font-weight: bold;">
                    <td>Total</td>
                    <td>-</td>
                    <td>-</td>
                    <td>263</td>
                </tr>
            </table>
        </div>

        <!-- Registered Students Table -->
        <h2 style="margin-top: 40px; margin-bottom: 5px;">Registered Students</h2>
        <table>
            <tr>
                <th>Name</th>
                <th>Email</th>
                <th>Course</th>
            </tr>
            <tr>
                <td>rishab</td>
                <td>kumarrishab451@gmail.com</td>
                <td>JavaScript</td>
            </tr>
            <tr>
                <td>sam</td>
                <td>hariprasadkoc99@gmail.com</td>
                <td>HTML</td>
            </tr>
            <tr>
                <td>suraj</td>
                <td>rishabkumarsingh990@gmail.com</td>
                <td>CSS</td>
            </tr>
        </table>
    </div>

    <div class="footer">
        Thank you for visiting our Student Registration Portal.
    </div>

</body>
</html>
"""

@app.route("/")
def home():
    return HTML_PAGE

if __name__ == "__main__":
    app.run(debug=True)