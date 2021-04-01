# sample_rest_flask_application
A Sample Flask Application With REST APIs

**Setup and Run Locally**
---
*Requirements:- Python 3.8+*<br>
1) `git clone https://github.com/anonshubh/sample_rest_flask_application.git`
(For Developer: Use your Forked URL) 
2) `cd sample_rest_flask_application`
3) `python -m venv env`
4) `source env/bin/activate` (Mac/Linux)<br>
   `env/Scripts/activate.ps1` (Windows-Powershell)
5) `pip install -r requirements.txt`
6) `python main.py`

<hr>

*API Documentation* <br>
GET REQUEST (Returns the Data From the Current List) <br>
Endpoint: http://127.0.0.1:5000/api/data <br>
<br>
POST REQUEST (Appends the New Values of Data to the List) <br>
Endpoint: http://127.0.0.1:5000/api/add <br>
<br>
PUT REQUEST (Changes the New Values of Data in the List at Given Index of Array) <br>
Endpoint: http://127.0.0.1:5000/api/change <br>
<br>
DELETE REQUEST (Resets All Values in List to 0) <br>
Endpoint: http://127.0.0.1:5000/api/delete <br>

