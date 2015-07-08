import csv
import codecs
import re

def csvToDictlist(filepath,encoding):

    #リストを用意します。
    list = [];
    #ファイルポインタを取得します。
    with codecs.open(filepath,'r',encoding) as fp:
    #↑newline=''を指定してないけど、問題ないのかな。一行飛ばしで読み込んだりしてないだろうな。←そんなことはなさそう。

        reader =csv.reader(fp);

        for row in reader:
            if len(row) >= 4:#その行の要素数が4以上で
                    #↓4要素とも"--"と一致していない場合に限り
                    condition1 = row[0]!="--" and row[1]!="--" and row[2]!="--" and row[3]!="--";
                    condition2 = row[0]!=" --" and row[1]!=" --" and row[2]!=" --" and row[3]!=" --";
                    condition3 = row[1]!= "" and row[2]!="";
                    if (condition1 and condition2 and condition3):
                        list.append(row);#listにrowを追加します。
                        #これで、1要素目がタイトル行、それ以降がデータ行のリストができたはず。

    dictlist = [];#空のリストを作ります。このあと作る辞書がどんどん追加される。
    keys = list[0];#0番の行はキーなので取得しておきます。
    for (i,row) in enumerate(list):#リスト内を順次回りながら、何番目か、と要素を取得します。
        if(i!=0):
            dictlist.append(dict(zip(keys,row)));#キーリストと値リストから辞書を作ります。

    return dictlist;

def modifyADDictlist(dictlist,account):
    for row in dictlist:
        #いらない列（の名前がついた要素）を消します。
        del(row["キャンペーンの状態"]);
        del(row["予算"]);
        del(row["ステータス"]);
        del(row["クリック率"]);
        del(row["平均クリック単価"]);
        del(row["費用/コンバージョンに至ったクリック"]);
        del(row["コンバージョンに至ったクリック/クリック数"]);
        del(row["ラベル"]);

        #列（の名前）を修正していきます。
        row["impr"] = row["表示回数"];
        del(row["表示回数"]);
        row["clicks"] = row["クリック数"];
        del(row["クリック数"]);
        row["conv"] = row["コンバージョンに至ったクリック"];
        del(row["コンバージョンに至ったクリック"]);
        row["cost"] = row["費用"];
        del(row["費用"]);
        row["avgPos"] = row["平均掲載順位"];
        del(row["平均掲載順位"]);
        #インプレッションシェアは検索とコンテンツで違うので、コンテンツも僕の管轄になったら修正が必要
        row["imprShare"] = row["検索広告のインプレッション シェア"];
        del(row["検索広告のインプレッション シェア"]);
        del(row["コンテンツのインプレッション シェア"])
 
        #ない列を追加します。
        row["account"]=account;
        match = re.search("^([A-Z]_[A-Z]{1,2})(【[0-9]{3}】.*)$",row["キャンペーン"])
        if (match):
            pass
        else:
            print("キャンペーン名がなんかおかしいよ！")
            print(row["キャンペーン"])
            print(row)
            print(match.group(1))
            print(match.group(2))
            exit()

        row["kind"] = match.group(1)
        row["category"] = match.group(2)
        del(row["キャンペーン"])
    return dictlist;

def modifyYSSDictlist(dictlist,account):
    for row in dictlist:
        #いらない列（の名前がついた要素）を消します。
        del(row["ウォッチリスト"])
        del(row["配信設定"])
        del(row["1日の予算"])
        del(row["クリック率"])
        del(row["平均CPC"])
        del(row["コスト/ユニークコンバージョン数"])
        del(row["ユニークコンバージョン率"])
        del(row["インプレッション損失率（掲載順位）"])
        del(row["キャンペーンID"])
        #列（の名前）を修正していきます。
        row["impr"] = row["インプレッション数"];
        del(row["インプレッション数"]);
        row["clicks"] = row["クリック数"];
        del(row["クリック数"]);
        row["cost"] = row["合計コスト"];
        del(row["合計コスト"]);
        row["conv"] = row["ユニークコンバージョン数"];
        del(row["ユニークコンバージョン数"]);
        row["avgPos"] = row["平均掲載順位"];
        del(row["平均掲載順位"]);
        row["imprShare"] = row["インプレッションシェア"];
        del(row["インプレッションシェア"]);
        #ない列を追加します。
        row["account"]=account;
        match = re.search("([A-Z]_[A-Z]{1,2})(【[0-9]{3}】.*)$",row["キャンペーン名"])
        if (match):
            row["kind"] = match.group(1)
            row["category"] = match.group(2)
            del(row["キャンペーン名"])
        else:
            if(row["キャンペーン名"] == "CVテスト用"):
                pass
            else:
                print("キャンペーン名がなんかおかしいよ！")
                print(row["キャンペーン名"])
                print(row)
                exit()
    return dictlist;

#この下は全然使い物になりませんよ！入札用ウィークリーデータを出力する構造になってませんよ！
def modifyYDNDictlist(dictlist,account):
    for row in dictlist:
        #print("---------------")
        #print(account)
        #print(row)
        #いらない列（の名前がついた要素）を消します。
            #YAHOOの場合はなし。
        #列（の名前）を修正していきます。
        row["広告の種類"] = row["広告タイプ"];
        del(row["広告タイプ"]);
        row["ラベル"] = row["広告名"];
        del(row["広告名"]);
        row["表示回数"] = row["インプレッション数"];
        del(row["インプレッション数"]);
        row["CTR"] = row["クリック率"];
        del(row["クリック率"]);
        row["費用"] = row["コスト"];
        del(row["コスト"]);
        row["CV"] = row["総コンバージョン数"];
        del(row["総コンバージョン数"]);
        row["コンバージョン率"] = row["総コンバージョン率"];
        del(row["総コンバージョン率"]);
        row["費用/CV"] = row["コスト/総コンバージョン数"];
        del(row["コスト/総コンバージョン数"]);
        row["キャンペーン"] = row["キャンペーン名"];
        del(row["キャンペーン名"]);
        row["広告グループ"] = row["広告グループ名"];
        del(row["広告グループ名"]);
        row["広告"] = row["タイトル"];
        del(row["タイトル"]);
        row["広告文 1"] = row["説明文1"];
        del(row["説明文1"]);
        row["広告文 2"] = row["説明文2"];
        del(row["説明文2"]);
        row["広告 ID"] = row["広告ID"];
        del(row["広告ID"]);
        row["広告グループ ID"] = row["広告グループID"];
        del(row["広告グループID"]);
        #ない列を追加します。
        row["広告の状態"] = "";
        row["媒体"]="YDN";
        row["アカウント"]=account;
    return dictlist;

def modifyLogicadDictlist(dictlist):
#カテゴリ、ーラベル、NO、LP、広告パターンが全行について埋まってるもののみ受け付けます。
#埋まってない場合不要なものが含まれてるので修正してください。削除は多分ダメ。
#逆にそれ以外はいじらないでください。
    for row in dictlist:
        #いらない列（の名前がついた要素）を消します。
        del(row["広告主"]);
        del(row["種別"]);
        del(row["CPM"]);
        del(row["VCV"]);
        #列（の名前）を修正していきます。
        row["広告 ID"] = row["クリエイティブID"];
        del(row["クリエイティブID"]);
        row["広告の状態"] = row["クリエイティブステータス"];
        del(row["クリエイティブステータス"]);
        row["広告の種類"] = row["サイズ"];
        del(row["サイズ"]);
        row["表示回数"] = row["Imp"];
        del(row["Imp"]);
        row["クリック数"] = row["Click"];
        del(row["Click"]);
        row["費用"] = row["消化金額"];
        del(row["消化金額"]);
        row["平均CPC"] = row["CPC"];
        del(row["CPC"]);
        row["コンバージョン率"] = row["CVR"];
        del(row["CVR"]);
        row["費用/CV"] = row["CPA"];
        del(row["CPA"]);
        #ない列を追加します。
        row["キャンペーンID"] = "";
        row["媒体"]="Logicad";
        row["アカウント"]="Logicad";
        row["施策"] = "ディスプレイ";
        row["媒体・施策"] = "リマーケ";
        row["平均掲載順位"] = "";
        row["広告グループ"] = "";
        row["広告"] = "";
        row["広告文 1"] = "";
        row["広告文 2"] = "";
        row["表示URL"] = "";
        row["キャンペーン"] = "";
        row["リンク先URL"] = "";
        row["広告グループ ID"] = "";
    return dictlist;


