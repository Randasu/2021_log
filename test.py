import re
import pathlib
import chardet
import os

file_name = "2021_log"  # ここに処理を実行したいディレクトリ名を入力してください
after_folder = file_name + "_処理済み"
os.makedirs(after_folder, exist_ok=True)
for Path in pathlib.Path(file_name).iterdir():
    with open(Path, "rb") as f:
        s = f.read()
        enc = chardet.detect(s)
    with open(Path, "r", encoding=enc["encoding"]) as rf:
        try:
            s = rf.read()
            print(after_folder + "/" + Path.name)

            # このプログラムでは/bunkazai/という文字列を含む行を抽出しています。
            # 抽出したい文字列に合わせて下の行を書き換えてください。
            lines = "\n".join([line for line in s.splitlines() if "/bunkazai/" in line])

            with open(after_folder + "/" + Path.name, "w", encoding="utf-8") as wf:
                for i in range(4):
                    wf.writelines(rf.readline())
                wf.writelines(lines)
        except UnicodeDecodeError:
            # 読み込んだファイルが文字化けしてる時に実行
            # 文字化けしたファイルを読み込むのは難しいので手動でやってください
            with open(
                after_folder + "/" + Path.name + "文字化け", "w", encoding="utf-8"
            ) as wf:
                wf.write("文字化け")
