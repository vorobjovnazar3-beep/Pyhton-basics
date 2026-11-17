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
