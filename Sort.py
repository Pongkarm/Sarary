#ข้อแนะนำเกี่ยวกับการแบ่งเงิน การแบ่งเงินจำเป็นต่อการใช้ชิวิตมีเป้าหมาย 
# ช่วยให้คุณควบคุมการเงินได้ดีขึ้นและบรรลุเป้าหมายในชีวิตได้เร็วขึ้น
# ✅ 1. ควบคุมรายจ่ายได้ดีขึ้น
# การแบ่งเงินทำให้คุณรู้ว่าแต่ละเดือนควรใช้จ่ายเท่าไรกับแต่ละเรื่อง เช่น ค่าอาหาร ค่าเดินทาง หรือของใช้ส่วนตัว ช่วยลดการใช้เงินเกินตัว
# ✅ 2. มีเงินเก็บเพื่ออนาคต
# เมื่อคุณกันเงินบางส่วนไว้สำหรับออมทุกเดือน จะช่วยให้คุณมีเงินสำรองในยามฉุกเฉิน หรือเก็บไว้เพื่อเป้าหมายในอนาคต เช่น ซื้อบ้าน เที่ยวต่างประเทศ หรือเรียนต่อ
#และแนะนำว่าให้คุณมีเงินเดือนจากการทำงานก่อนค่อยแบ่งไม่แนะนำให้แบ่งแบบนี้ในกรณียังเรียนอยู่เงินที่ได้มาจากค่าขนมพ่อแม่ เพราะอาจจะต้องเปลี่ยนวิธีแบ่งเงิน
#Emergency savings 5%
#Invest 15%
#to_spend 40%
# Various installments 10%
# Normal storage.txt 20%
# For_parents 10%
#ทุกครั้งที่กดรันจะเป็นการคำนวนเงินเดือน ไม่แนะนำให้กดหลายครั้งเพราะเงินอาจและได้

from datetime import datetime
import re

def change_balance(filename, increase_amount):
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()

    for i, line in enumerate(lines):
        if line.strip().startswith("#"):
            continue

        match = re.search(r"คงเหลือ\s+(\d+)\s+บาท", line)
        if match:
            old_balance = int(match.group(1))
            new_balance = old_balance + increase_amount
            print(f"[{filename}] เพิ่มเงินจาก: {old_balance} → {new_balance}")
            lines[i] = f"คงเหลือ {new_balance} บาท\n"
            break
    else:
        print(f"[{filename}] ไม่พบบรรทัด 'คงเหลือ ... บาท'")
        return None, None

    with open(filename, "w", encoding="utf-8") as file:
        file.writelines(lines)

    return old_balance, new_balance

# อ่านไฟล์เงินเดือน
with open("__Sarary.txt__", "r", encoding="utf-8") as file:
    content = file.read()

match = re.search(r"เงินเดือน\s+(\d+)\s+บาท", content)
if match:
    salary = int(match.group(1))
    print("เงินเดือนที่ได้คือ:", salary)
else:
    print("ไม่พบข้อมูลเงินเดือนในไฟล์")
    exit()

# คำนวณสัดส่วน
savings = salary * 0.05
invest = salary * 0.15
to_spend = salary * 0.40
various_installments = salary * 0.10
normal_storage = salary * 0.20
for_parents = salary * 0.10

# เวลาปัจจุบัน (ปี พ.ศ.)
now = datetime.now()
formatted_time = now.strftime("%d/%m/{} %H:%M:%S".format(now.year + 543))

# เขียนลง history.txt
with open("history.txt", "a+", encoding="utf-8") as file:
    file.write(f"เงินเดือน {salary} บาท วันเวลา {formatted_time} น.\n")

    def write_wallet_log(name, filename, amount):
        old, new = change_balance(filename, amount)
        if old is not None:
            file.write(f"  {name:<22} เพิ่ม {amount:.2f} บาท | จาก {old:.2f} → {new:.2f} บาท\n")

    write_wallet_log("Emergency savings", "Emergency savings.txt", savings)
    write_wallet_log("Invest", "Invest.txt", invest)
    write_wallet_log("To spend", "To_sped.txt", to_spend)
    write_wallet_log("Various installments", "Various installments.txt", various_installments)
    write_wallet_log("Normal storage", "Normal storage.txt", normal_storage)
    write_wallet_log("For parents", "For_parents.txt", for_parents)

    file.write("\n")

print("บันทึกเรียบร้อยแล้ว:", salary, 'บาท')

