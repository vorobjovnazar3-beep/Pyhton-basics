# ============================================================
# Програма: Калькулятор вартості замовлення в інтернет-магазині
# Опис: Розрахунок вартості товарів зі знижками, типом клієнта
#        та вартістю доставки
# ============================================================

# Константи
DISCOUNT_THRESHOLD_SMALL: float = 1000.0   # поріг для знижки 5%
DISCOUNT_THRESHOLD_MEDIUM: float = 3000.0  # поріг для знижки 10%
DISCOUNT_THRESHOLD_LARGE: float = 5000.0   # поріг для знижки 15%
VAT_RATE: float = 0.20                     # ПДВ 20%


def main() -> None:
    print("=" * 55)
    print("   КАЛЬКУЛЯТОР ВАРТОСТІ ЗАМОВЛЕННЯ")
    print("=" * 55)

    # --- 1. Введення даних ---
    customer_name: str = input("Введіть ваше ім'я: ").strip()
    
    # Перевірка, чи ім'я не порожнє
    if not customer_name:
        customer_name = "Гість"

    age_input: str = input("Введіть ваш вік: ")
    age: int = int(age_input)  # перетворення str → int

    product_name: str = input("Назва товару: ").strip()
    
    quantity_input: str = input("Кількість товару: ")
    quantity: int = int(quantity_input)

    price_input: str = input("Ціна за одиницю (грн): ")
    price: float = float(price_input)  # перетворення str → float

    is_student_input: str = input("Ви студент? (так/ні): ").strip().lower()
    is_student: bool = is_student_input in ("так", "yes", "y", "т")

    has_coupon_input: str = input("Є купон на знижку 7%? (так/ні): ").strip().lower()
    has_coupon: bool = has_coupon_input in ("так", "yes", "y", "т")

    # --- 2. Базові обчислення ---
    subtotal: float = quantity * price                     # математична операція
    print(f"\nПідсумок без знижок: {subtotal:.2f} грн")

    # --- 3. Визначення знижки за сумою (if / elif / else) ---
    discount_percent: float = 0.0

    if subtotal >= DISCOUNT_THRESHOLD_LARGE:
        discount_percent = 15.0
    elif subtotal >= DISCOUNT_THRESHOLD_MEDIUM:
        discount_percent = 10.0
    elif subtotal >= DISCOUNT_THRESHOLD_SMALL:
        discount_percent = 5.0
    else:
        discount_percent = 0.0

    # --- 4. Вкладені умови + логічні оператори ---
    extra_discount: float = 0.0

    if is_student and age < 25:
        extra_discount += 5.0
        print("Додаткова знижка студенту до 25 років: +5%")
    elif is_student and not (age < 25):
        extra_discount += 3.0
        print("Додаткова знижка студенту: +3%")

    if has_coupon:
        extra_discount += 7.0
        print("Застосовано купон: +7%")

    # Загальна знижка не більше 25%
    total_discount_percent: float = min(discount_percent + extra_discount, 25.0)

    # --- 5. Умовний вираз (ternary) ---
    discount_status: str = "є знижка" if total_discount_percent > 0 else "знижки немає"
    print(f"Статус знижки: {discount_status}")

    # --- 6. Розрахунок суми зі знижкою ---
    discount_amount: float = subtotal * (total_discount_percent / 100)
    amount_after_discount: float = subtotal - discount_amount

    # --- 7. Вибір способу доставки (match-case) ---
    print("\nОберіть спосіб доставки:")
    print("1 - Самовивіз (безкоштовно)")
    print("2 - Нова Пошта (70 грн)")
    print("3 - Кур'єр по місту (120 грн)")
    print("4 - Міжнародна доставка (350 грн)")

    delivery_choice: str = input("Ваш вибір (1-4): ").strip()

    delivery_cost: float = 0.0
    delivery_name: str = ""

    match delivery_choice:
        case "1":
            delivery_cost = 0.0
            delivery_name = "Самовивіз"
        case "2":
            delivery_cost = 70.0
            delivery_name = "Нова Пошта"
        case "3":
            delivery_cost = 120.0
            delivery_name = "Кур'єр по місту"
        case "4":
            delivery_cost = 350.0
            delivery_name = "Міжнародна доставка"
        case _:
            print("Невірний вибір. Встановлено самовивіз.")
            delivery_cost = 0.0
            delivery_name = "Самовивіз (за замовчуванням)"

    # --- 8. Фінальні розрахунки ---
    amount_with_delivery: float = amount_after_discount + delivery_cost
    vat: float = amount_with_delivery * VAT_RATE
    total_to_pay: float = amount_with_delivery + vat

    # --- 9. Форматоване виведення результатів (f-рядки) ---
    print("\n" + "=" * 55)
    print("           ПІДСУМОК ЗАМОВЛЕННЯ")
    print("=" * 55)
    print(f"Клієнт:              {customer_name}")
    print(f"Вік:                 {age} років")
    print(f"Студент:             {'Так' if is_student else 'Ні'}")
    print(f"Товар:               {product_name}")
    print(f"Кількість:           {quantity} шт.")
    print(f"Ціна за одиницю:     {price:.2f} грн")
    print("-" * 55)
    print(f"Сума без знижок:     {subtotal:.2f} грн")
    print(f"Знижка ({total_discount_percent:.0f}%):     -{discount_amount:.2f} грн")
    print(f"Після знижки:        {amount_after_discount:.2f} грн")
    print(f"Доставка ({delivery_name}): {delivery_cost:.2f} грн")
    print(f"ПДВ (20%):           {vat:.2f} грн")
    print("=" * 55)
    print(f"ДО СПЛАТИ:           {total_to_pay:.2f} грн")
    print("=" * 55)

    # Додаткова перевірка (логічні оператори)
    if total_to_pay > 10000 and not is_student:
        print("\nУвага: велике замовлення. Рекомендуємо оформити розстрочку.")
    elif total_to_pay < 200:
        print("\nМаленьке замовлення. Можливо, варто додати ще товари.")

    print("\nДякуємо за замовлення! Гарного дня!")


if __name__ == "__main__":
    main()

