from flask import Flask, request, jsonify
from flask_cors import CORS
import time
import random

app = Flask(__name__)
CORS(app)

@app.route('/analyze', methods=['POST'])
def analyze_chart():
    # ตรวจสอบว่ามีไฟล์ส่งมาไหม
    if 'image' not in request.files:
        return jsonify({"error": "ไม่พบไฟล์รูปภาพ"}), 400
    
    # จำลองเวลาประมวลผล (เหมือน AI กำลังคิดจริงๆ)
    time.sleep(3) 

    # สุ่มผลวิเคราะห์จำลอง (ให้ดูเหมือน AI วิเคราะห์ละเอียด)
    patterns = ["Bullish Engulfing", "Head and Shoulders", "Double Bottom", "Hammer Pin Bar"]
    selected_pattern = random.choice(patterns)
    up_percent = random.randint(60, 85)
    down_percent = 100 - up_percent

    mock_response = f"""
    <strong>🔍 ตรวจพบรูปแบบ:</strong> {selected_pattern}<br>
    <strong>🎯 ความแม่นยำ:</strong> 89.5%<br>
    <hr>
    <strong>📊 การวิเคราะห์แนวโน้ม:</strong><br>
    🟢 โอกาสปรับตัว <strong>ขึ้น</strong>: {up_percent}%<br>
    🔴 โอกาสปรับตัว <strong>ลง</strong>: {down_percent}%<br><br>
    <strong>💡 คำแนะนำจาก AI:</strong> รูปแบบกราฟแสดงถึงแรงซื้อที่หนาแน่นในโซนแนวรับ มีโอกาสที่ราคาจะเบรคเอาท์ (Breakout) ในเร็วๆ นี้ ควรเฝ้าระวังจุด Take Profit ที่แนวต้านถัดไป
    """

    return jsonify({"result": mock_response})

if __name__ == '__main__':
    print("--- Server Simulation Started (No API Key Required) ---")
    app.run(debug=True, port=5000)