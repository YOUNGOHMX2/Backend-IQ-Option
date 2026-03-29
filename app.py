import google.generativeai as genai
from PIL import Image
from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import io

app = Flask(__name__)
CORS(app)

# --- 1. การตั้งค่า Gemini AI ---
# นำ API Key ที่ได้จาก Google AI Studio มาวางในเครื่องหมายคำพูดด้านล่างนี้
API_KEY = "คัดลอก_API_Key_มาวางตรงนี้" 
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

@app.route('/analyze', methods=['POST'])
def analyze_chart():
    # ตรวจสอบว่ามีไฟล์ส่งมาไหม
    if 'image' not in request.files:
        return jsonify({"error": "No image uploaded"}), 400
    
    try:
        # 2. รับรูปจากหน้าเว็บและแปลงให้พร้อมส่งให้ AI
        file = request.files['image']
        image_data = file.read()
        image = Image.open(io.BytesIO(image_data))

        # 3. คำสั่ง (Prompt) จ้าง AI ให้วิเคราะห์
        prompt = """
        คุณคือผู้เชี่ยวชาญด้านการเทรด (Expert Trader) จงวิเคราะห์รูปกราฟนี้ด้วยความละเอียด:
        1. ระบุชื่อ Pattern ที่เห็น (เช่น Bullish Engulfing, Head and Shoulders) 
        2. วิเคราะห์แนวโน้มตลาดปัจจุบัน (Bullish / Bearish / Sideways)
        3. ให้จุดเข้า (Entry), จุดตัดขาดทุน (Stop Loss - SL) และจุดทำกำไร (Take Profit - TP) 
        4. ให้คำแนะนำเพิ่มเติมในการบริหารความเสี่ยง (Risk Management)

        **ข้อกำหนดการตอบกลับ:**
        - ตอบเป็นภาษาไทย
        - ใช้รูปแบบ HTML เพื่อให้แสดงผลสวยงามบนหน้าเว็บ
        - ใช้สีเขียว (#00e676) สำหรับ TP และสีแดง (#ff4d4d) สำหรับ SL
        - ใส่กล่องดีไซน์ที่ดูทันสมัย
        """

        # 4. ส่งข้อมูลไปประมวลผลจริง
        response = model.generate_content([prompt, image])
        
        # คืนค่าผลลัพธ์จาก AI กลับไปที่หน้าเว็บ
        return jsonify({"result": response.text})

    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({"result": f"<div style='color:red;'>❌ เกิดข้อผิดพลาดจาก AI: {str(e)}<br>โปรดตรวจสอบว่าผูกบัตรใน Google AI Studio หรือยัง</div>"})

# --- 5. การรันเซิร์ฟเวอร์ ---
if __name__ == '__main__':
    # ส่วนนี้จะทำให้รันได้ทั้งในคอม และบน Render (Port จะถูกตั้งอัตโนมัติ)
    port = int(os.environ.get("PORT", 5000))
    print(f"--- AI Trading Server Started on Port {port} ---")
    app.run(host='0.0.0.0', port=port, debug=True)
