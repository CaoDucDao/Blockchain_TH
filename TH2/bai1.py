def adjust_difficulty(old_target: int, time_start: int, time_end: int):

    actual_time = time_end - time_start
    expected_time = 2016 * 10 * 60
    ratio = actual_time / expected_time

    if ratio < 0.25:
        ratio = 0.25
        actual_time = expected_time // 4
    elif ratio > 4.00:
        ratio = 4.00
        actual_time = expected_time * 4

    new_target = old_target * actual_time // expected_time
   
    actual_minutes = (time_end - time_start) / 60

    print(f"- Thời gian thực tế: {actual_minutes:.2f} phút")
    print(f"- Tỷ lệ điều chỉnh (ratio): {ratio:.4f}")
    print(f"- Giá trị new_target: {new_target}")

    return actual_minutes, ratio, new_target

if __name__ == "__main__":
    print("=== BÀI 1: ĐIỀU CHỈNH ĐỘ KHÓ ===")
  
    old_target = int(input("old_target: "), 0)
    time_start = int(input("time_start: "))
    time_end = int(input("time_end: "))

    adjust_difficulty(old_target, time_start, time_end)

    