#######################################
# テストデータ生成スクリプト
#
# 1行目に整数の個数n、
# 2行目以降に2または5がn行出力された
# テキストファイルを指定個数生成
#######################################

import os
import random


# --- 設定項目 ---

# ファイルを生成するディレクトリ
OUTPUT_DIR = "./"

# 生成するファイル数
NUM_FILES_TO_GENERATE = 15

# 各ファイルの整数の個数(n)の最小値・最大値
MIN_N = 5
MAX_N = 2000


def generate_file(file_path, min_n, max_n):
    """
    指定された仕様でテストデータファイルを1つ生成します。
    """
    # 1行目に出力する整数の個数(n)をランダムに決定
    n = random.randint(min_n, max_n)

    with open(file_path, 'w', encoding='utf-8') as f:
        # 1行目にnを書き込む
        f.write(f"{n}\n")

        # 2行目以降に、2か5をランダムにn個書き込む
        for _ in range(n):
            num = random.choice([2, 5])
            f.write(f"{num}\n")


if __name__ == "__main__":
    # 出力用ディレクトリがなければ作成
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    print(f"ファイルを '{OUTPUT_DIR}' ディレクトリに生成します...")

    for i in range(1, NUM_FILES_TO_GENERATE + 1):
        file_name = f"input_{i:02}.txt"
        path = os.path.join(OUTPUT_DIR, file_name)
        generate_file(path, MIN_N, MAX_N)
        print(f"  {path} を生成しました。")

    print("完了しました。")
