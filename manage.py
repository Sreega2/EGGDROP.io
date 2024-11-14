import argparse
import uuid

# Список пользователей (вместо базы данных)
users = {}

def reset_user(user_id):
    """Удаляет пользователя по его ID."""
    if user_id in users:
        del users[user_id]
        print(f"Пользователь {user_id} был удален.")
    else:
        print(f"Пользователь с ID {user_id} не найден.")

def give_money(user_id, amount):
    """Выдает деньги пользователю."""
    if user_id not in users:
        users[user_id] = {"balance": 50.0, "inventory": []}  # Начальный баланс 50 для новых пользователей
        print(f"Пользователь {user_id} был создан с начальным балансом 50$")
    
    users[user_id]['balance'] += amount
    print(f"Баланс пользователя {user_id} теперь: {users[user_id]['balance']}$")

def main():
    """Основная функция для обработки команд."""
    try:
        parser = argparse.ArgumentParser(description="Управление пользователями и балансами.")
        
        # Команда для сброса пользователя
        parser.add_argument('command', choices=['reset_user', 'give_money'], help="Команда для выполнения.")
        
        # Аргументы для команд
        parser.add_argument('user_id', type=str, help="ID пользователя.")
        parser.add_argument('amount', type=float, nargs='?', default=0, help="Сумма для пополнения баланса.")
        
        args = parser.parse_args()

        # Выполнение соответствующей команды
        if args.command == 'reset_user':
            reset_user(args.user_id)
        elif args.command == 'give_money':
            give_money(args.user_id, args.amount)

    except Exception as e:
        print(f"Произошла ошибка: {e}")

    # Задержка, чтобы окно не закрывалось
    input("Нажмите Enter для выхода...")

if __name__ == '__main__':
    main()
