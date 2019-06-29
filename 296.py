def main():

    N, H, M, T = map(int, input().split())

    late_time = (N - 1) * T
    late_hour = late_time // 60
    late_minutes = late_time - late_hour * 60

    lateMinutes = (M + late_minutes) % 60
    addition = (M + late_minutes) // 60
    lateHour = (H + late_hour + addition) % 24

    print(lateHour)
    print(lateMinutes)

if __name__ == '__main__':
    main()