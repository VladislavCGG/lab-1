import streamlit as st

# Налаштування сторінки
st.set_page_config(page_title="Аналіз чисел — Варіант 29", page_icon="📊")

# Заголовок
st.title("Аналіз набору чисел (Варіант 29)")

# Підпис розробника — ⚠️ ЗАМІНИ [Ім’я] на своє!
st.markdown("**Розробник: Чава Владислав**")

# Інструкція
st.info(
    "Введіть 10 чисел через кому (наприклад: 139,941,287,797,414,333,814,533,743,204). "
    "Числа мають бути від 10 до 1000. Дробові числа — з крапкою (наприклад: 12.5)."
)

# Поле вводу
user_input = st.text_input(
    "Ваші числа:",
    value="139,941,287,797,414,333,814,533,743,204",
    help="Введіть рівно 10 чисел через кому"
)

# Кнопка аналізу (не обов’язкова, але зручна)
if st.button("Аналізувати") or user_input:
    if not user_input.strip():
        st.error("Будь ласка, введіть числа.")
    else:
        parts = [p.strip() for p in user_input.split(",")]
        
        # Перевірка кількості
        if len(parts) != 10:
            st.error(f"Помилка: потрібно рівно 10 чисел, а введено {len(parts)}.")
        else:
            numbers = []
            valid = True
            for part in parts:
                if not part:
                    st.error("Помилка: знайдено порожній елемент.")
                    valid = False
                    break
                try:
                    num = float(part)
                    if num < 10 or num > 1000:
                        st.error(f"Помилка: число {num} поза діапазоном [10, 1000].")
                        valid = False
                        break
                    numbers.append(num)
                except ValueError:
                    st.error(f'Помилка: "{part}" — не число. Використовуйте крапку для дробової частини.')
                    valid = False
                    break
            
            if valid and len(numbers) == 10:
                min_val = min(numbers)
                max_val = max(numbers)
                avg_val = round(sum(numbers) / len(numbers), 2)
                
                # Виведення результатів
                st.success("✅ Аналіз завершено!")
                st.markdown(f"<p style='color:red; font-weight:bold;'>Min: {min_val}</p>", unsafe_allow_html=True)
                st.markdown(f"<p style='color:green; font-weight:bold;'>Max: {max_val}</p>", unsafe_allow_html=True)
                st.write(f"Average: {avg_val}")