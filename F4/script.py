# 椀から飴玉を減らしていくプログラム

# 飴玉の減少プロセスをシミュレートし、最終的な残数を計算して出力する処理
def solve():
    while True:
        # ユーザーからの入力を受け取る
        s = input("4個の整数をスペース区切りで入力してください (終了するには0 0 0 0を入力): ")
        
        # 入力をスペースで分割し、整数に変換してリストにする
        # ヒントに基づき、s.split(" ")を使用
        try:
            boxes = list(map(int, s.split(" ")))
        except ValueError:
            print("無効な入力です。4つの整数をスペース区切りで入力してください。")
            continue

        # 0 0 0 0 が入力されたらプログラムを終了
        if sum(boxes) == 0 and len(boxes) == 4: # 4つの0が入力された場合
            print("プログラムを終了します。")
            break

        # 入力値の検証 (0以上100以下、少なくとも1つは0でない)
        if not all(0 <= x <= 100 for x in boxes) or all(x == 0 for x in boxes) or len(boxes) != 4:
            print("入力値は0以上100以下で、少なくとも1つは0でない4つの整数である必要があります。")
            continue
        
        # 飴玉の減少処理を実行
        remaining_candies = simulate_candy_reduction(boxes)
        
        # 残った飴玉の数を表示
        print(remaining_candies)

# 飴玉の減少プロセスをシミュレートする関数
def simulate_candy_reduction(initial_boxes):
    boxes = list(initial_boxes) # 元のリストを破壊しないようにコピー
    
    # print_boxes(boxes) # デバッグ用に初期状態を表示

    while True:
        # 飴玉を減らせるかどうかのフラグ
        can_reduce = False
        
        # 1. 一番少ない飴玉の数が2つ以上ある箱を見つける
        # どの箱から選ぶべきかを判断するための一時的なリスト
        eligible_boxes = [] 
        for i, count in enumerate(boxes):
            if count >= 2:
                eligible_boxes.append((count, i)) # (飴玉の数, 元のインデックス)
        
        # 飴玉の数が少ない順にソート (値が同じ場合は元のインデックスが小さい方を優先)
        # 問題文「一番少ない飴玉の数が2つ以上となる箱が、少なくとも1つ以上となるときは、一番左の腕を選ぶ。」
        # これを考慮すると、ソート順は (飴玉の数, インデックス) のタプルでソートすれば自然とインデックスが小さい方が前になる。
        eligible_boxes.sort() # デフォルトでタプルの最初の要素、次に2番目の要素でソートされる

        selected_box_index = -1
        selected_candy_count = -1

        if eligible_boxes:
            selected_candy_count, selected_box_index = eligible_boxes[0]
            can_reduce = True
        
        if not can_reduce:
            # 減らせる飴玉がなければ終了 (2つ以上ある箱がない場合)
            break

        # 2. 選んだ箱以外のすべての箱から、選んだ箱の飴玉と同数の飴玉を取り除く
        # 「選んだ腕の中の飴玉はそのままにしておく。」という記述を反映
        candies_to_remove = selected_candy_count # 選ぶ前のその箱の飴玉の数が基準

        next_boxes_state = []
        for i, count in enumerate(boxes):
            if i == selected_box_index:
                # 選んだ箱の飴玉はそのまま
                next_boxes_state.append(count)
            else:
                # 選んだ箱以外の箱から、candies_to_removeと同数取り除く（ただし0を下回らない）
                next_boxes_state.append(max(0, count - candies_to_remove)) 
        
        # すべての箱が空になったら終了（これ以上処理できないため）
        if sum(next_boxes_state) == 0:
            boxes = next_boxes_state
            break

        boxes = next_boxes_state

        # 3. 残った飴玉を多い順に並べ替える
        # ただし、空の箱は無視して並べ替える必要があるか？
        # 「空でない腕から空でない腕がすべて隣り合う腕が、一番少ない飴玉の数が2つ以上となるときは、一番左の腕を選ぶ。」
        # 「この手順を空でない腕が1つだけになるまで繰り返す。」
        # → 空でない腕だけを抽出し、並べ替えるのが自然。
        
        # 0以外の要素だけを抽出してソートし、その後に0を追加する
        non_empty_boxes = [b for b in boxes if b > 0]
        non_empty_boxes.sort(reverse=True)
        
        # 元の4つの箱の数に戻すために、足りない分だけ0を追加
        boxes = non_empty_boxes + [0] * (4 - len(non_empty_boxes))
        
        # print_boxes(boxes) # 各ステップでの状態表示（デバッグ用）

        # 次のターンで減らせる飴玉があるかどうかのチェック
        # 全ての箱が1以下になった場合、これ以上減らせないのでループを抜ける
        if all(b < 2 for b in boxes if b > 0): # 空でない箱が全て1以下
             break # ループを終了

        # 問題文の「空でない腕が1つだけになるまで繰り返す」を反映
        # 1つだけになったらループを終了
        if len(non_empty_boxes) == 1:
            break
            
    # 最終的に残った飴玉の総数を計算
    return sum(boxes)

# プログラムの実行
if __name__ == "__main__":
    solve()