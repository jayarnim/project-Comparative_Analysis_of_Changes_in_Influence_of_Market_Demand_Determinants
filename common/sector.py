CODEDICT = {
    "한식음식점":"CS100001",
    "중식음식점":"CS100002",
    "일식음식점":"CS100003",
    "양식음식점":"CS100004",
    "제과점":"CS100005",
    "패스트푸드점":"CS100006",
    "치킨전문점":"CS100007",
    "분식전문점":"CS100008",
    "호프-간이주점":"CS100009",
    "커피-음료":"CS100010",

    "일반교습학원":"CS200001",
    "외국어학원":"CS200002",
    "예술학원":"CS200003",
    "컴퓨터학원":"CS200004",
    "스포츠강습":"CS200005",
    "일반의원":"CS200006",
    "치과의원":"CS200007",
    "한의원":"CS200008",
    "동물병원":"CS200009",

    "변호사사무소":"CS200010",
    "변리사사무소":"CS200011", 
    "법무사사무소":"CS200012",
    "기타법무서비스":"CS200013",
    "회계사사무소":"CS200014",
    "세무사사무소":"CS200015",
    "당구장":"CS200016",
    "골프연습장":"CS200017",
    "볼링장":"CS200018",
    "PC방":"CS200019",

    "전자게임장":"CS200020",
    "기타오락장":"CS200021",
    "복권방":"CS200022",
    "통신기기수리":"CS200023",
    "스포츠클럽":"CS200024",
    "자동차수리":"CS200025", 
    "자동차미용":"CS200026",
    "모터사이클수리":"CS200027",
    "미용실":"CS200028",
    "네일숍":"CS200029",

    "피부관리실":"CS200030",
    "세탁소":"CS200031",
    "가전제품수리":"CS200032",
    "부동산중개업":"CS200033",
    "여관":"CS200034",
    "게스트하우스":"CS200035",
    "고시원":"CS200036",
    "노래방":"CS200037",
    "독서실":"CS200038",
    "DVD방":"CS200039",

    "녹음실":"CS200040",
    "사진관":"CS200041",
    "통변역서비스":"CS200042",
    "건축물청소":"CS200043",
    "여행사":"CS200044",
    "비디오/서적임대":"CS200045",
    "의류임대":"CS200046",
    "가정용품임대":"CS200047",

    "슈퍼마켓":"CS300001",
    "편의점":"CS300002",
    "컴퓨터및주변장치판매":"CS300003",
    "핸드폰":"CS300004",
    "주류도매":"CS300005",
    "미곡판매":"CS300006",
    "육류판매":"CS300007",
    "수산물판매":"CS300008",
    "청과상":"CS300009",

    "반찬가게":"CS300010",
    "일반의류":"CS300011",
    "한복점":"CS300012",
    "유아의류":"CS300013",
    "신발":"CS300014",
    "가방":"CS300015",
    "안경":"CS300016",
    "시계및귀금속":"CS300017",
    "의약품":"CS300018",
    "의료기기":"CS300019",

    "서적":"CS300020",
    "문구":"CS300021",
    "화장품":"CS300022",
    "미용재료":"CS300023",
    "운동/경기용품":"CS300024",
    "자전거및기타운송장비":"CS300025",
    "완구":"CS300026",
    "섬유제품":"CS300027",
    "화초":"CS300028",
    "애완동물":"CS300029",

    "중고가구":"CS300030",
    "가구":"CS300031",
    "가전제품":"CS300032",
    "철물점":"CS300033",
    "악기":"CS300034",
    "인테리어":"CS300035",
    "조명용품":"CS300036",
    "중고차판매":"CS300037",
    "자동차부품":"CS300038",
    "모터사이클및부품":"CS300039",

    "재생용품판매점":"CS300040",
    "예술품":"CS300041",
    "주유소":"CS300042",
    "전자상거래업":"CS300043"
    }

# 음식 서비스
FOOD = [
    "한식음식점", "중식음식점", "일식음식점", "양식음식점", "제과점",
    "패스트푸드점", "치킨전문점", "분식전문점", "호프-간이주점", "커피-음료"
    ]
FOODCODE = [CODEDICT[FOOD[i]] for i in range(len(FOOD))]

# 학원 및 교육
ACADEMY = ["일반교습학원", "외국어학원", "예술학원", "독서실"]
ACADEMYCODE = [CODEDICT[ACADEMY[i]] for i in range(len(ACADEMY))]

# 의료 서비스
HOSPITAL = ["일반의원", "치과의원", "한의원", "의약품", "의료기기"]
HOSPITALCODE = [CODEDICT[HOSPITAL[i]] for i in range(len(HOSPITAL))]

# 법률 서비스
LAW = ["변호사사무소", "법무사사무소", "회계사사무소", "세무사사무소"]
LAWCODE = [CODEDICT[LAW[i]] for i in range(len(LAW))]

# 레저 및 엔터테인먼트
LEISURE = ["당구장", "골프연습장", "볼링장", "PC방", "노래방", "사진관"]
LEISURECODE = [CODEDICT[LEISURE[i]] for i in range(len(LEISURE))]

# 자동차
CAR = ["자동차수리", "자동차미용", "자동차부품", "주유소", "중고차판매"]
CARCODE = [CODEDICT[CAR[i]] for i in range(len(CAR))]

# 미용 및 패션
BEAUTY = [
    "미용실", "네일숍", "피부관리실", "일반의류", "한복점", 
    "유아의류", "신발", "가방", "안경", "시계및귀금속", 
    "화장품"
    ]
BEAUTYCODE = [CODEDICT[BEAUTY[i]] for i in range(len(BEAUTY))]

# 음식 소매
MARKET = ["슈퍼마켓", "편의점", "미곡판매", "육류판매", "수산물판매", "청과상", "반찬가게"]
MARKETCODE = [CODEDICT[MARKET[i]] for i in range(len(MARKET))]

# 서비스 및 상담
SERVICE = ["세탁소", "여행사", "전자상거래업", "부동산중개업", "건축물청소", "여관", "고시원"]
SERVICECODE = [CODEDICT[SERVICE[i]] for i in range(len(SERVICE))]

# 스포츠
SPORTS = ["스포츠클럽", "스포츠강습", "운동/경기용품", "자전거및기타운송장비"]
SPORTSCODE = [CODEDICT[SPORTS[i]] for i in range(len(SPORTS))]

# 가전 제품
APPLIANCE = ["가전제품", "가전제품수리", "컴퓨터및주변장치판매", "핸드폰", "통신기기수리"]
APPLIANCECODE = [CODEDICT[APPLIANCE[i]] for i in range(len(APPLIANCE))]

# 기타 소매
ETC = [
    "비디오/서적임대", "철물점", "악기", "인테리어", "조명용품", 
    "예술품", "완구", "화초", "애완동물", "가구"
    ]
ETCCODE = [CODEDICT[ETC[i]] for i in range(len(ETC))]

# 유형명 리스트
NAMELIST = [
    'ALL',
    'FOOD', 'ACADEMY', 'HOSPITAL', 'LAW', 'LEISURE', 
    'CAR', 'BEAUTY', 'MARKET', 'SERVICE', 'SPORTS',
    'APPLIANCE', 'ETC'
    ]

# 유형 리스트
SECTORLIST = [
    list(CODEDICT.keys()),
    FOOD, ACADEMY, HOSPITAL, LAW, LEISURE, 
    CAR, BEAUTY, MARKET, SERVICE, SPORTS,
    APPLIANCE, ETC
    ]

# 유형 코드 리스트
CODELIST = [
    list(CODEDICT.values()),
    FOODCODE, ACADEMYCODE, HOSPITALCODE, LAWCODE, LEISURECODE, 
    CARCODE, BEAUTYCODE, MARKETCODE, SERVICECODE, SPORTSCODE,
    APPLIANCECODE, ETCCODE
    ]