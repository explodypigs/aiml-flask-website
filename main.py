from flask import Flask, render_template, Response
from cam import VideoCamera

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <body>
        <div style= text-align:center>
            <img src="/video" alt="webcam footage(use a device with webcam)"/>
            <p>
                <h1>Read pls</h1>
                You need a camera for this if you didnt notice :/<br/>
                if it doesnt detect you then make sure you're in a well lit room<br/>
                and a wall behind you. If it still doesnt work then \_(:/)_/.<br/>
                Dont bully me i know it looks bad i only spent a couple hours on it<br/>
                Its all in python btw cuz i use c++ and js too much
                <br/>its also kinda racist tbh but thats cuz i didnt use 100k images<br/>
                and every single person in the world to train(make) it
            </p>
            
        </div>
    </body>
    '''

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
               
@app.route('/video')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(debug=True)