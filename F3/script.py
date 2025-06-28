# 整数の並びの中に2, 5, 2, 5が続けて現れる回数を数えるプログラム

# ファイルを読み込んで整数のリストを返す関数
def read_numbers_from_file(filename):
    numbers = []
    try:
        with open(filename, 'r') as f:
            # 1行目はnの値なのでスキップ
            f.readline()
            for line in f:
                try:
                    numbers.append(int(line.strip()))
                except ValueError:
                    print(f"警告: 不正な数値データが検出されました: {line.strip()}")
    except FileNotFoundError:
        print(f"エラー: ファイル '{filename}' が見つかりません。")
    return numbers

# 整数パターンの出現回数を返すプログラム
def count_occurrences(numbers):
    # パターンを指定
    pattern = [2, 5, 2, 5]
    
    count = 0
    pattern_len = len(pattern)
    list_len = len(numbers)

    for i in range(list_len - pattern_len + 1):
        match = True
        for j in range(pattern_len):
            if numbers[i + j] != pattern[j]:
                match = False
                break
        if match:
            count += 1
    return count

# ファイル名の入力からパターン出現回数の出力を行う関数
def main():
    while True:
        filename = input("ファイル名を入力してください (終了するには何も入力せずにEnter): ")
        if not filename:
            print("プログラムを終了します。")
            break

        numbers = read_numbers_from_file(filename)
        # ファイルが正常に読み込まれた場合のみ処理を続行
        if numbers:
            occurrence_count = count_occurrences(numbers)
            # 1行に出力する
            print(occurrence_count)

if __name__ == "__main__":
    main()