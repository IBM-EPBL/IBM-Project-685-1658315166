from flask import Flask,render_template,request
import cv2
from tensorflow.keras.models import load_model
import numpy as np
from werkzeug.utils import secure_filename
app=Flask(__name__,template_folder="template")
model=load_model("analysis.h5")
print("loaded model")
@app.route('/',methods=['GET'])
def index():
    return render_template('h.html')
@app.route('/h',methods=['GET'])
def home():
    return render_template('h.html')
@app.route('/i',methods=['GET'])
def about():
    return render_template('i.html')
@app.route('/u',methods=['GET','POST'])
def predict():
    cap = cv2.Videocapture(0)
    while True:
        _, frame = cap.read()
        frame = cv2.flip(frame,1)
        while True:
            (grabbed,frame) =vs.read()
            if not grabbed:
                break
            if W is None or H is None:
                (H,W) = frame.shape[:2]
            output = frame.copy()
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = cv2.resize(frame, (64, 64))
            x=np.expand_dims(frame, axis=0)
            result = np.argmax(model.predict(x),axis =-1)
            index=['Cyclone','Earthquake','Flood','wildfire']
            result=str(index[result[0]])
            cv2.putText(output,"activity: {}".format(result), (10,120),cv2.FONT_HERSHEY_PLAIN,1, (0,25,255) ,1)
            cv2.imshow("Output",output)
            key = cv2.waitKey(1) & 0xFF
            if key == ord("q"):
                break
        print("[INFO]cleaning up...")
        vs.release()
        cv2.destroyAllWindows()
        return render_template("u.html")
if __name__ == '__main__':
    app.run(host='0.0.0.0' , port=8000, debug=False)

    