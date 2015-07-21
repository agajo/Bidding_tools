import csv;
import os;
import csvToDictlist;
#↑こうやって呼んだ場合、モジュール名.関数名という形で書く必要がある。
import re;

def getFilesAsOne(folderpath):
#    folderpath = "../testdata/";
    finaldictlist = [];
    fileList = os.listdir(folderpath);#dataフォルダの中身をリストで取得します。
    for filename in fileList:#fileListの中身を1つずつ見ていきます。

        if (filename.startswith("AD") and filename.endswith(".csv")):#アドワーズ
            account = re.match("AD[1-9]",filename);#アカウント名を含むマッチオブジェクトを取得
            dictlist = csvToDictlist.csvToDictlist(folderpath + filename,"utf_8");#辞書リストを取得して
            dictlist = csvToDictlist.modifyADDictlist(dictlist,account.group());#名前など正しくします。
            #appendだと、リストを要素として追加する。
            finaldictlist.extend(dictlist);

        elif (filename.startswith("YDN") and filename.endswith(".csv")):#YDN
            account = re.match("YDN[1-9]",filename);#アカウント名のマッチオブジェクトを取得
            dictlist = csvToDictlist.csvToDictlist(folderpath + filename,"shift_jis");#辞書リストを取得して
            dictlist = csvToDictlist.modifyYDNDictlist(dictlist,account.group());#名前など訂正。
            #extendなら、リストの要素を要素として追加する。
            finaldictlist.extend(dictlist);

        elif (filename.startswith("YSS") and filename.endswith(".csv")):#YSS
            account = re.match("YSS[1-9]",filename);#アカウント名のマッチオブジェクトを取得
            dictlist = csvToDictlist.csvToDictlist(folderpath + filename,"shift_jis");#辞書リストを取得して
            dictlist = csvToDictlist.modifyYSSDictlist(dictlist,account.group());#名前など訂正。
            #extendなら、リストの要素を要素として追加する。
            finaldictlist.extend(dictlist);

        elif (filename.startswith("Logicad") and filename.endswith(".csv")):#Logicad
            account = "Logicad";
            dictlist = csvToDictlist.csvToDictlist(folderpath + filename,"shift_jis");#辞書リストを取得して
            dictlist = csvToDictlist.modifyLogicadDictlist(dictlist);#VLOOKUPによる下処理が必要
            finaldictlist.extend(dictlist);
        else:
            print("なんかおかしいよ!ファイル名がおかしいよ！");
            print(filename);
            exit();

    return finaldictlist;
