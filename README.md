# goit-algo-hw-09

## Жадібний алгоритм

Жадібний алгоритм обирає монету найбільшого номіналу на кожному кроці. Це швидкий метод, але не завжди гарантує мінімальну кількість монет.

- Часова складність **O(n)**
- Просторова складність **O(1)**
- **Швидкість**: Дуже швидкий для великих сум.
- **Оптимальність**: Не завжди знаходить мінімальну кількість монет.

## Алгоритм динамічного програмування

Алгоритм динамічного програмування знаходить мінімальну кількість монет для всіх сум до заданої включно.

- Часова складність **O(m * n)**
- Просторова складність **O(n)**
- **Швидкість**: Може бути повільнішим для великих сум.
- **Оптимальність**: Завжди знаходить мінімальну кількість монет.

## Висновки
- **Жадібний алгоритм** підходить для швидких оцінок і наборів монет, де він працює оптимально.
- **Алгоритм динамічного програмування** підходить для випадків, де важливо мінімізувати кількість монет, навіть якщо це займає більше часу.