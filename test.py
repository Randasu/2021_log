import re
import pathlib
import chardet
import os


def get_encoding(
    path,
    eachline=False,
    lookup=(
        "cp932",
        "utf_8",
        "utf_8_sig",
        "shift_jis",
        "iso2022_jp",
        "euc_jp",
        "ascii",
    ),
):
    """
    テキストファイルのエンコードを調べる。

    :param path: ファイルパス
    :param eachline: 1行ずつ確かめる（メモリに一度に載りきらないファイルなど。ただし時間かかる）
    :param lookup: 試すエンコード名候補のiterable
    :return: eachline=True の時は、エンコード名を返す
             eachline=False の時は、エンコード名と読み取ったデータを返す
    """
    encoding = None
    if eachline:
        for trying_encoding in lookup:
            try:
                with open(path, "r", encoding=trying_encoding) as rh:
                    for line in rh:
                        pass
                encoding = trying_encoding
                break
            except UnicodeDecodeError:
                continue
        return encoding
    else:
        encoded = None
        with open(path, "rb") as rh:
            data = rh.read()
        for trying_encoding in lookup:
            try:
                encoded = data.decode(trying_encoding)
                encoding = trying_encoding
                break
            except UnicodeDecodeError:
                continue
        return encoding


def extracter(Path):
    first_4_lines = []
    for i in range(4):
        line = rf.readline()
        first_4_lines.append(line)
    s = rf.read()
    print(after_folder + "/" + Path.name)

    # このプログラムでは/bunkazai/という文字列を含む行を抽出しています。
    # 抽出したい文字列に合わせて下の行を書き換えてください。
    lines = "\n".join([line for line in s.splitlines() if "/bunkazai/" in line])

    with open(after_folder + "/" + Path.name, "w", encoding="utf-8") as wf:
        wf.writelines(first_4_lines)
        wf.writelines(lines)


file_name = "2021_log"  # ここに処理を実行したいディレクトリ名を入力してください
after_folder = file_name + "_処理済み"
os.makedirs(after_folder, exist_ok=True)
for Path in pathlib.Path(file_name).iterdir():
    with open(Path, "rb") as f:
        s = f.read()
        enc = chardet.detect(s)
    with open(Path, "r", encoding=enc["encoding"]) as rf:
        try:
            extracter(Path)
        except UnicodeDecodeError:
            # 読み込んだファイルが文字化けしてる時に実行
            # 文字化けしたファイルを読み込むのは難しいので手動でやってください
            # with open(
            #     after_folder + "/" + Path.name + "文字化け", "w", encoding="utf-8"
            # ) as wf:
            #     wf.write("文字化け")
            encoding = get_encoding(Path)
            if encoding:
                with open(Path, "r", encoding=encoding) as rf:
                    extracter(Path)
            else:
                pass
# https://ginneko-atelier.com/blogs/entry336/
