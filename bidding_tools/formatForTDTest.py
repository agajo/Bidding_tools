##アドワーズのcsvはユニコードかもしれない。怒られたら、Excelでcsv指定して保存しなおしてください。
#カテゴリや施策しぼるのはあとから手動でやってください。

folderpath = "../data/tokka16/";#この場所にあるデータを全部読みに行きます。中身確認しておいて。最後のスラッシュ忘れずに。
output = '../outputs/tokka16/tokka16.csv';#このパス・ファイルを出力します。好みがあれば変えといて。
filterpath = "../tokka16_target_categories.csv";#有効にするカテゴリーを指定しているcsvファイルを指定してください。

import modifyDictlist;
import getFilesAsOne;
import csv;

finaldictlist = getFilesAsOne.getFilesAsOne(folderpath);

with open(filterpath,'r',newline='') as catfil:
    reader = csv.reader(catfil);
    for row in reader:#readerオブジェクトから一行取り出す方法をこれしか知らないのでこうしてますが、正解じゃないと思う
        catnofilter = row;


#newline = ''  を入れないと、出力の一行毎に空行ができる。
with open(output, 'w',newline='') as csvfile:
    fieldnames = ['媒体', 'アカウント','施策','媒体・施策','カテゴリー','広告の状態','広告の種類','ラベル','NO','LP','広告パターン','表示回数','クリック数','CTR','費用','平均CPC','平均掲載順位','CV','コンバージョン率','費用/CV','キャンペーン','広告グループ','広告','広告文 1','広告文 2','表示URL','リンク先URL','キャンペーンID','広告グループ ID','広告 ID'];
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, extrasaction='ignore')
    writer.writeheader()
    for row in finaldictlist:
        filtering = (row["カテゴリー"] in catnofilter) and (row["施策"] == "ディスプレイ")
        if (filtering):
            writer.writerow(row);
