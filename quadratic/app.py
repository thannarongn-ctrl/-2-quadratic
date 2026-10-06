import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# คำอธิบายแอปพลิเคชัน
st.title("📐 Quadratic Function Explorer")
st.write("""
แอปพลิเคชันนี้ช่วยจำลองและวิเคราะห์สมการกำลังสอง $f(x) = ax^2 + bx + c$ 
**วิธีใช้งาน:** ปรับค่าสัมประสิทธิ์ $a, b, c$ ที่เมนูด้านข้างเพื่อดูผลการเปลี่ยนแปลง
""")

st.sidebar.header("⚙️ ตั้งค่า Input")

# Input 1-3: ใช้ Slider ปรับ
a = st.sidebar.slider("สัมประสิทธิ์ a", -10.0, 10.0, 1.0, 0.5)
b = st.sidebar.slider("สัมประสิทธิ์ b", -10.0, 10.0, 0.0, 0.5)
c = st.sidebar.slider("สัมประสิทธิ์ c", -10.0, 10.0, -4.0, 0.5)

# ตรวจสอบค่าผิดปกติ (a ต้องไม่เป็น 0)
if a == 0:
    st.error("⚠️ ค่า 'a' ไม่สามารถเป็น 0 ได้! เนื่องจากจะไม่ใช่สมการกำลังสอง")
    st.stop()

# ส่วนคำนวณ (Calculation)
h = -b / (2 * a)
k = a * (h ** 2) + b * h + c
discriminant = (b ** 2) - (4 * a * c)

if discriminant > 0:
    root1 = (-b + np.sqrt(discriminant)) / (2 * a)
    root2 = (-b - np.sqrt(discriminant)) / (2 * a)
    roots_str = f"x₁ = {root1:.2f}, x₂ = {root2:.2f}"
elif discriminant == 0:
    root1 = -b / (2 * a)
    roots_str = f"x = {root1:.2f} (รากซ้ำ)"
else:
    roots_str = "ไม่มีรากที่เป็นจำนวนจริง"

# แสดงผลลัพธ์ (Output)
st.subheader("📊 ผลการคำนวณ")

col1, col2, col3 = st.columns(3)
col1.metric("จุดยอด (Vertex)", f"({h:.2f}, {k:.2f})")
col2.metric("ค่า Discriminant (Δ)", f"{discriminant:.2f}")
col3.metric("คำตอบสมการ (Roots)", roots_str)

x_vals = np.linspace(h - 10, h + 10, 100)
y_vals = a * (x_vals ** 2) + b * x_vals + c

tab1, tab2 = st.tabs(["📈 กราฟแสดงผล", "📋 ตารางข้อมูล"])

with tab1:
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(x_vals, y_vals, label=f'f(x) = {a}x² + {b}x + {c}', color='tab:blue', lw=2)
    ax.axhline(0, color='gray', linestyle='--', linewidth=0.8)
    ax.axvline(0, color='gray', linestyle='--', linewidth=0.8)
    ax.scatter([h], [k], color='red', zorder=5, label=f'Vertex ({h:.2f}, {k:.2f})')
    ax.grid(True, alpha=0.3)
    ax.legend()
    st.pyplot(fig)

with tab2:
    df = pd.DataFrame({"x": x_vals[::10], "f(x)": y_vals[::10]})
    st.dataframe(df, use_container_width=True)