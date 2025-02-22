from flask import Flask
import os
import getpass
import datetime

app = Flask(__name__)

@app.route('/htop')
def htop():
    try:
        name = "Dikshit"
        username = getpass.getuser()
        ist_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        try:
            top_output = os.popen("top -b -n 1").read()
        except Exception as e:
            top_output = f"Error fetching top output: {e}"

        return f"""
        <pre>
        Name: {name}
        Username: {username}
        Server Time (IST): {ist_time}
        
        TOP output:
        {top_output}
        </pre>
        """
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
