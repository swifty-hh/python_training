menu = {
    '아메리카노': {'가격': 3000, '옵션': ['샷 추가', '시럽 추가', '휘핑 크림']},
    '카페라떼': {'가격': 3500, '옵션': ['샷 추가', '시럽 추가', '휘핑 크림']},
    '카푸치노': {'가격': 3500, '옵션': ['샷 추가', '시럽 추가', '휘핑 크림']},
    '에스프레소': {'가격': 2500, '옵션': ['샷 추가', '시럽 추가', '휘핑 크림']},
    '카라멜 마끼아또': {'가격': 4000, '옵션': ['샷 추가', '시럽 추가', '휘핑 크림']}
}

def show_menu():
    print("\n=== 메뉴 ===")
    for drink, info in menu.items():
        print(f"{drink} - 가격: {info['가격']}원")

def place_order():
    order = {}
    while True:
        show_menu()
        drink = input("주문할 음료를 입력하세요 (q를 입력하면 주문을 종료합니다): ")
        if drink == 'q':
            break
        if drink not in menu:
            print("존재하지 않는 음료입니다. 다시 입력해주세요.")
            continue
        options = []
        while True:
            print("\n=== 옵션 ===")
            print('옵션: 샷 추가, 시럽 추가, 휘핑 크림')
            option = input("추가 옵션을 선택하세요 (추가 옵션 없으면 엔터): ")
            if option == '':
                break
            if option not in menu[drink]['옵션']:
                print("존재하지 않는 옵션입니다. 다시 입력해주세요.")
                continue
            options.append(option)
        print("\n=== 주문 수량 ===")
        quantity = input("주문 수량을 입력하세요: ")
        if not quantity.isdigit():
            print("잘못된 입력입니다. 수량은 숫자로 입력해주세요.")
            continue
        order[drink] = {'옵션': options, '수량': int(quantity)}
    return order

def print_receipt(order):
    print("\n=== 영수증 ===")
    total_price = 0
    for drink, info in order.items():
        price = menu[drink]['가격']
        quantity = info['수량']
        options = ', '.join(info['옵션'])
        subtotal = price * quantity
        total_price += subtotal
        print(f"{drink} - 가격: {price}원, 옵션: {options}, 수량: {quantity}, 소계: {subtotal}원")
    print(f"총 가격: {total_price}원")

def cafe_order():
    print("카페 음료 주문을 시작합니다.")
    order = place_order()
    print_receipt(order)
    print("!!!주문이 완료되었습니다. 감사합니다!!!")

cafe_order()