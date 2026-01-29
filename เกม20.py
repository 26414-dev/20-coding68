import tkinter as tk
from tkinter import messagebox

def check_exercise():
    goal_minutes = 30
    try:
        exercise_minutes = int(entry.get())
        
        if exercise_minutes >= goal_minutes:
            messagebox.showinfo("ผลลัพธ์", "✨ ยินดีด้วยครับ! คุณออกกำลังกายถึงเป้าหมายแล้ว 🎉")
        else:
            remaining = goal_minutes - exercise_minutes
            messagebox.showwarning("ผลลัพธ์", f"💪 อีกนิดเดียว! คุณขาดอีก {remaining} นาที จะถึงเป้าหมาย")
            
    except ValueError:
        messagebox.showerror("ข้อผิดพลาด", "❌ กรุณากรอกตัวเลขเท่านั้นครับ")

# สร้างหน้าต่างโปรแกรม
root = tk.Tk()
root.title("My Fitness Tracker 🏃‍♂️")
root.geometry("350x250")

# กำหนดสีพื้นหลังหน้าต่างหลัก (Light Blue)
root.configure(bg="#E1F5FE")

# สร้าง Label คำแนะนำ (เอาคลื่นน้ำออกแล้ว)
label = tk.Label(
    root, 
    text="วันนี้คุณออกกำลังกายกี่นาที?", 
    font=("Arial", 12, "bold"),
    bg="#E1F5FE",
    fg="#0277BD"
)
label.pack(pady=15)

# สร้างช่องกรอกข้อมูล
entry = tk.Entry(root, font=("Arial", 12), justify='center')
entry.pack(pady=5)

# สร้างปุ่มตรวจสอบ (สีน้ำเงินเข้ม ตัวหนังสือขาว)
check_button = tk.Button(
    root, 
    text="🚀 ตรวจสอบผลความสำเร็จ", 
    command=check_exercise,
    bg="#0288D1", 
    fg="white",
    font=("Arial", 10, "bold"),
    padx=10,
    pady=5,
    activebackground="#01579B", # สีเวลาถูกกด
    activeforeground="white"
)
check_button.pack(pady=20)

# ข้อความตกแต่งด้านล่าง (เอาหยดน้ำออก)
footer = tk.Label(root, text="Keep Moving! 🏃‍♂️", bg="#E1F5FE", font=("Arial", 8, "italic"), fg="#01579B")
footer.pack(side="bottom", pady=10)

# เริ่มรันโปรแกรม
root.mainloop()
