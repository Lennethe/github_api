## 実装した内容

### USER.py
ここに自分のGithubのtokenと、取得したgithubのリポジトリのURLを記述する。
必要であるならばconcerened_fileを記述する

### get_concern_file.py
これを実行すると、PRを一単位としてconcerened_fileと同時に編集されたファイルを編集行が多い順に並べる。もしconcerened_fileがNoneの場合全てのPRにおいて、編集行が多いものを順に並べる。

#### 改善案
- 得られた結果の中である文字列を含むものだけを抽出すると言った、フィルタリング機能。
- 編集行だけでなく追加された行、削除された行、PRを一単位とした編集された回数を表示する。

### get_concern_reviewer.py
これを実行すると、PRを一単位としてconcerened_fileに存在するコメントを全て取得。
コメントした人と回数の一覧を得る。concerened_fileがNoneの場合、全てのファイルでコメントした人とその回数の一覧を得る。

#### 改善案
- ファイル単位ではなく、ソースコード単位で検索できるようにする。
 