import streamlit as st

# قائمة لتخزين أسماء الموظفين
employees = []

# عنوان التطبيق
st.title("📋 نظام تسجيل الحضور والانصراف")
st.write("مرحبًا بك في تطبيق إدارة الحضور اليومي 👩‍💻")

# واجهة الإدخال
employee_name = st.text_input("🧑‍💼 أدخل اسم الموظف:")

# أزرار التفاعل
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("✅ تسجيل حضور"):
        if employee_name:
            if employee_name not in employees:
                employees.append(employee_name)
                st.success(f"تم تسجيل حضور {employee_name} بنجاح ✅")
            else:
                st.warning("هذا الموظف تم تسجيل حضوره بالفعل ⚠️")
        else:
            st.error("من فضلك أدخل اسم الموظف أولاً ❗")

with col2:
    if st.button("🚪 تسجيل انصراف"):
        if employee_name:
            if employee_name in employees:
                employees.remove(employee_name)
                st.info(f"تم تسجيل انصراف {employee_name} 👋")
            else:
                st.warning("هذا الموظف غير مسجل كحاضر ⚠️")
        else:
            st.error("من فضلك أدخل اسم الموظف أولاً ❗")

with col3:
    if st.button("📄 عرض قائمة الحضور"):
        if employees:
            st.subheader("قائمة الحضور الحالية:")
            for i, emp in enumerate(employees, 1):
                st.write(f"{i}. {emp}")
        else:
            st.info("لا يوجد موظفون حاليًا في قائمة الحضور 📭")

# رسالة ختامية
st.markdown("---")
st.caption("👩‍💻 تطبيق تجريبي من تطوير لمياء محمد إبراهيم - باستخدام Streamlit")

