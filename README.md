# shareToDo

## 概要
- ToDoリストを公開する
- ルームを作ってメンバーを招待する
- メンバーに共有のToDoリストを作成する
- 誰が誰に対してのタスクがあるのかを明確にする
- 割り勘や回収物などをあれできる

## テーブル
### ルームテーブル(room)
|カラム名(和名)|カラム名|データ型|必須？|
|------|------|-----|----|
|ルーム名|room_name|varchar|M|
|設立日|est_date|date|M:デフォルトで登録|
|責任者|representative|FK(user_id)|M|
|公開/非公開|open_close|boolean|M:デフォルトでfalse|

### ユーザーテーブル(user)
|カラム名(和名)|カラム名|データ型|必須？|
|------|------|-----|----|
|ユーザー名|user_name|varchar|M|
|登録日|est_date|date|M:デフォルトで登録|

### ルーム：ユーザー中間テーブル
|カラム名(和名)|カラム名|データ型|必須？|
|------|------|-----|----|
|ルームID|room_id|FK|M|
|ユーザーID|user_id|FK|M|

### タスクテーブル(task)
|カラム名(和名)|カラム名|データ型|必須？|
|------|------|-----|----|
|タスク名|task_name|varchar|M|
|作った人|author|FK(user_id)|M|
|ルーム|room_id|FK(room_id)|M|
|期限|deadline|date|O|
|カテゴリ|category_id|FK(category_id)|M|

### 関係者テーブル(participant)
|カラム名(和名)|カラム名|データ型|必須？|
|------|------|-----|----|
|ユーザーID|user_id|FK(user_id)|M|
|役割|role|int|M|

|id|role|詳細|
|---|---|---|
|1|ターゲット|この人に対して何かを行う|
|2||ワーカー|この人たちがタスクを行う|

### カテゴリーテーブル(category)
|カラム名(和名)|カラム名|データ型|必須？|
|------|------|-----|----|
|カテゴリー名|cateogry_name|varchar|M|

#### 初期データ
|id|カテゴリー名|
|----|--|
|1|勉強|
|2|支払い|
|3|提出|

## ページ
1. トップページ
 shareTodo/index
2. ルーム作成ページ
 shareTodo/room/create
 shareTodo/room/edit/
 shareTodo/room/delete/
 shareTodo/room/
3. タスク登録ページ
 shareTodo/task/create
 shareTodo/task/edit
 shareTodo/task/delete
