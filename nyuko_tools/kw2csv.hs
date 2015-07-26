type JikuWord = String
type KakeWord = String
type campaignName = String
type KWList = [([JikuWord],[KakeWord])]

kwList :: KWList
kwList = [(["軸1","jiku2"],["kake1","かけ２","kake3"]),(["j1","j2"],["k1"])]

data AdGroup = AdGroup { agAdGroupName :: String
           , agCampaignName :: String
           , maxCPC :: Int} deriving (Show)

data TD = TD { tdCampaignName :: String
       , tdAdGroupName :: String
       , headline :: String
       , descriptionLine1 :: String
       , descriptionLine2 :: String
       , displayURL :: String
       , finalURL :: String
       , linkSakiName :: String
       , adName :: String} deriving (Show)

data KW = KW { kwCamapignName :: String
       , kwAdGroupName :: String
       , keyword :: String
       , criterionType :: String} deriving (Show)

type SysNegKW = KW
type SougoNegKW = KW

kwList2AdGr :: campaignName -> KWList -> [AdGroup]
kwList2AdGr c kl = AdGroup {
  agAdGroupName = 

kwList2KW :: KWList -> KW
kwList2KW x = undefined

kwList2TD :: KWList -> TD
kwList2TD x = undefined

kwList2SysNeg :: KWList -> SysNegKW
kwList2SysNeg = undefined

kwList2SougoNeg :: KWList -> SougoNegKW
kwList2SougoNeg x = undefined
