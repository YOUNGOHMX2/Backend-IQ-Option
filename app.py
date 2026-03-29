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
    # --- ส่วนที่เพิ่มใหม่ (คำนวณ SL/TP) ---
    current_price = round(random.uniform(1.0500, 1.0900), 5)
    sl = round(current_price - 0.0025, 5) # จุดตัดขาดทุน
    tp = round(current_price + 0.0050, 5) # จุดทำกำไร
    # ----------------------------------

    mock_response = f"""
    <strong>🔍 ตรวจพบรูปแบบ:</strong> {selected_pattern}<br>
    <strong>📈 ราคาปัจจุบัน:</strong> {current_price}<br>
    <hr>
    <strong>🎯 ความแม่นยำ:</strong> 89.5%<br>
    <hr>
    <strong>📊 การวิเคราะห์แนวโน้ม:</strong><br>
    🟢 โอกาสปรับตัว <strong>ขึ้น</strong>: {up_percent}%<br> 
    🔴 โอกาสปรับตัว <strong>ลง</strong>: {down_percent}%<br><br>
    <div style="color: #d32f2f;">🔴 <strong>Stop Loss (SL):</strong> {sl}</div>
    <div style="color: #388e3c;">🟢 <strong>Take Profit (TP):</strong> {tp}</div>
    <hr>
    {response.text if 'response' in locals() else "วิเคราะห์ตามเทรนด์ปัจจุบัน"}
    """

    return jsonify({"result": mock_response})

if __name__ == '__main__':
    print("--- Server Simulation Started (No API Key Required) ---")
    app.run(debug=True, port=5000)
