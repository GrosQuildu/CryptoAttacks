
from builtins import bytes
from random import randint

from CryptoAttacks.Utils import b2i, i2b
from sage.all_cmdline import *  # import sage library

_sage_const_666476190 = Integer(666476190)
_sage_const_1910674289 = Integer(1910674289)
_sage_const_84545285 = Integer(84545285)
_sage_const_422718233 = Integer(422718233)
_sage_const_439627290 = Integer(439627290)
_sage_const_4226619131 = Integer(4226619131)
_sage_const_3537026925 = Integer(3537026925)
_sage_const_2981198280 = Integer(2981198280)
_sage_const_2099981142 = Integer(2099981142)
_sage_const_0xca = Integer(0xca)
_sage_const_4193904912 = Integer(4193904912)
_sage_const_0x2a = Integer(0x2a)
_sage_const_2021191816 = Integer(2021191816)
_sage_const_3889509095 = Integer(3889509095)
_sage_const_50529797 = Integer(50529797)
_sage_const_3366741092 = Integer(3366741092)
_sage_const_659450151 = Integer(659450151)
_sage_const_530416258 = Integer(530416258)
_sage_const_1350051880 = Integer(1350051880)
_sage_const_1408738468 = Integer(1408738468)
_sage_const_896163637 = Integer(896163637)
_sage_const_552200649 = Integer(552200649)
_sage_const_3602738027 = Integer(3602738027)
_sage_const_1094664062 = Integer(1094664062)
_sage_const_1027439175 = Integer(1027439175)
_sage_const_2391672713 = Integer(2391672713)
_sage_const_1280088276 = Integer(1280088276)
_sage_const_2724199842 = Integer(2724199842)
_sage_const_1397991157 = Integer(1397991157)
_sage_const_2299101321 = Integer(2299101321)
_sage_const_3469641545 = Integer(3469641545)
_sage_const_2419829648 = Integer(2419829648)
_sage_const_2295088196 = Integer(2295088196)
_sage_const_353708607 = Integer(353708607)
_sage_const_2358086913 = Integer(2358086913)
_sage_const_219813645 = Integer(219813645)
_sage_const_2569646233 = Integer(2569646233)
_sage_const_656219450 = Integer(656219450)
_sage_const_2675275242 = Integer(2675275242)
_sage_const_1068339858 = Integer(1068339858)
_sage_const_2459058093 = Integer(2459058093)
_sage_const_3705447295 = Integer(3705447295)
_sage_const_1893765232 = Integer(1893765232)
_sage_const_845436466 = Integer(845436466)
_sage_const_3585172693 = Integer(3585172693)
_sage_const_2610638262 = Integer(2610638262)
_sage_const_699439513 = Integer(699439513)
_sage_const_0x27 = Integer(0x27)
_sage_const_753790401 = Integer(753790401)
_sage_const_28 = Integer(28)
_sage_const_3065411521 = Integer(3065411521)
_sage_const_20 = Integer(20)
_sage_const_24 = Integer(24)
_sage_const_2189565853 = Integer(2189565853)
_sage_const_32962295 = Integer(32962295)
_sage_const_1137232011 = Integer(1137232011)
_sage_const_4069226873 = Integer(4069226873)
_sage_const_766942107 = Integer(766942107)
_sage_const_0x15 = Integer(0x15)
_sage_const_0x14 = Integer(0x14)
_sage_const_0x17 = Integer(0x17)
_sage_const_0x16 = Integer(0x16)
_sage_const_3552407251 = Integer(3552407251)
_sage_const_0x10 = Integer(0x10)
_sage_const_504434447 = Integer(504434447)
_sage_const_0x12 = Integer(0x12)
_sage_const_0x19 = Integer(0x19)
_sage_const_0x18 = Integer(0x18)
_sage_const_0x1E = Integer(0x1E)
_sage_const_0x1D = Integer(0x1D)
_sage_const_0x1F = Integer(0x1F)
_sage_const_0x1A = Integer(0x1A)
_sage_const_0x1C = Integer(0x1C)
_sage_const_0x1B = Integer(0x1B)
_sage_const_1690872932 = Integer(1690872932)
_sage_const_1684326572 = Integer(1684326572)
_sage_const_1809235307 = Integer(1809235307)
_sage_const_0x1d = Integer(0x1d)
_sage_const_0x1f = Integer(0x1f)
_sage_const_0x1a = Integer(0x1a)
_sage_const_0x1c = Integer(0x1c)
_sage_const_0x1b = Integer(0x1b)
_sage_const_856756514 = Integer(856756514)
_sage_const_3822927587 = Integer(3822927587)
_sage_const_3385428288 = Integer(3385428288)
_sage_const_3669454189 = Integer(3669454189)
_sage_const_496927619 = Integer(496927619)
_sage_const_1306962859 = Integer(1306962859)
_sage_const_3452797260 = Integer(3452797260)
_sage_const_3823361342 = Integer(3823361342)
_sage_const_1077969088 = Integer(1077969088)
_sage_const_2960903088 = Integer(2960903088)
_sage_const_1944491379 = Integer(1944491379)
_sage_const_3177933782 = Integer(3177933782)
_sage_const_3739133817 = Integer(3739133817)
_sage_const_3776773629 = Integer(3776773629)
_sage_const_1446130276 = Integer(1446130276)
_sage_const_2156497161 = Integer(2156497161)
_sage_const_1784624437 = Integer(1784624437)
_sage_const_3941256997 = Integer(3941256997)
_sage_const_3297990596 = Integer(3297990596)
_sage_const_3250690392 = Integer(3250690392)
_sage_const_3367088505 = Integer(3367088505)
_sage_const_50726147 = Integer(50726147)
_sage_const_0xb = Integer(0xb)
_sage_const_13 = Integer(13)
_sage_const_2509582756 = Integer(2509582756)
_sage_const_636152527 = Integer(636152527)
_sage_const_2436475025 = Integer(2436475025)
_sage_const_2096661628 = Integer(2096661628)
_sage_const_1420360788 = Integer(1420360788)
_sage_const_454768173 = Integer(454768173)
_sage_const_913070646 = Integer(913070646)
_sage_const_2076946608 = Integer(2076946608)
_sage_const_4294960410 = Integer(4294960410)
_sage_const_1691735473 = Integer(1691735473)
_sage_const_2564049996 = Integer(2564049996)
_sage_const_1572530013 = Integer(1572530013)
_sage_const_1819072692 = Integer(1819072692)
_sage_const_1908716981 = Integer(1908716981)
_sage_const_1893325225 = Integer(1893325225)
_sage_const_3797835452 = Integer(3797835452)
_sage_const_1539358875 = Integer(1539358875)
_sage_const_2475900334 = Integer(2475900334)
_sage_const_3076642518 = Integer(3076642518)
_sage_const_3249976951 = Integer(3249976951)
_sage_const_4276558334 = Integer(4276558334)
_sage_const_2339994098 = Integer(2339994098)
_sage_const_16909057 = Integer(16909057)
_sage_const_1942467764 = Integer(1942467764)
_sage_const_3569248874 = Integer(3569248874)
_sage_const_3135724893 = Integer(3135724893)
_sage_const_926379609 = Integer(926379609)
_sage_const_1414834428 = Integer(1414834428)
_sage_const_1111655622 = Integer(1111655622)
_sage_const_200339707 = Integer(200339707)
_sage_const_2659418909 = Integer(2659418909)
_sage_const_3873888049 = Integer(3873888049)
_sage_const_2395555655 = Integer(2395555655)
_sage_const_1417554474 = Integer(1417554474)
_sage_const_1521806938 = Integer(1521806938)
_sage_const_1499050731 = Integer(1499050731)
_sage_const_2892260552 = Integer(2892260552)
_sage_const_974525996 = Integer(974525996)
_sage_const_4199962284 = Integer(4199962284)
_sage_const_1616953504 = Integer(1616953504)
_sage_const_2149292928 = Integer(2149292928)
_sage_const_774790258 = Integer(774790258)
_sage_const_1555620956 = Integer(1555620956)
_sage_const_2088564868 = Integer(2088564868)
_sage_const_2700103760 = Integer(2700103760)
_sage_const_623200879 = Integer(623200879)
_sage_const_101452294 = Integer(101452294)
_sage_const_2423288032 = Integer(2423288032)
_sage_const_3144405200 = Integer(3144405200)
_sage_const_3974939439 = Integer(3974939439)
_sage_const_3398387146 = Integer(3398387146)
_sage_const_1475454630 = Integer(1475454630)
_sage_const_3936318837 = Integer(3936318837)
_sage_const_260409994 = Integer(260409994)
_sage_const_1471084887 = Integer(1471084887)
_sage_const_1429418854 = Integer(1429418854)
_sage_const_234025727 = Integer(234025727)
_sage_const_84083462 = Integer(84083462)
_sage_const_1640145761 = Integer(1640145761)
_sage_const_320022069 = Integer(320022069)
_sage_const_1395732834 = Integer(1395732834)
_sage_const_1859957358 = Integer(1859957358)
_sage_const_193169544 = Integer(193169544)
_sage_const_589514341 = Integer(589514341)
_sage_const_3351745874 = Integer(3351745874)
_sage_const_1008868894 = Integer(1008868894)
_sage_const_1195195770 = Integer(1195195770)
_sage_const_3374377449 = Integer(3374377449)
_sage_const_1826141292 = Integer(1826141292)
_sage_const_3685578459 = Integer(3685578459)
_sage_const_4054230615 = Integer(4054230615)
_sage_const_1248797989 = Integer(1248797989)
_sage_const_1768542907 = Integer(1768542907)
_sage_const_3318059348 = Integer(3318059348)
_sage_const_3890730290 = Integer(3890730290)
_sage_const_760903469 = Integer(760903469)
_sage_const_3991781676 = Integer(3991781676)
_sage_const_2968016984 = Integer(2968016984)
_sage_const_169090570 = Integer(169090570)
_sage_const_2976870366 = Integer(2976870366)
_sage_const_25988493 = Integer(25988493)
_sage_const_4076801522 = Integer(4076801522)
_sage_const_4272137053 = Integer(4272137053)
_sage_const_4278118169 = Integer(4278118169)
_sage_const_2790781350 = Integer(2790781350)
_sage_const_2442213800 = Integer(2442213800)
_sage_const_336333848 = Integer(336333848)
_sage_const_1951283770 = Integer(1951283770)
_sage_const_3132780501 = Integer(3132780501)
_sage_const_168166924 = Integer(168166924)
_sage_const_1513502316 = Integer(1513502316)
_sage_const_0xf0 = Integer(0xf0)
_sage_const_0xf1 = Integer(0xf1)
_sage_const_0xf2 = Integer(0xf2)
_sage_const_0xf3 = Integer(0xf3)
_sage_const_0xf4 = Integer(0xf4)
_sage_const_0xf5 = Integer(0xf5)
_sage_const_0xf6 = Integer(0xf6)
_sage_const_0xf7 = Integer(0xf7)
_sage_const_0xf8 = Integer(0xf8)
_sage_const_0xf9 = Integer(0xf9)
_sage_const_1211644016 = Integer(1211644016)
_sage_const_1615867952 = Integer(1615867952)
_sage_const_1701169839 = Integer(1701169839)
_sage_const_707417214 = Integer(707417214)
_sage_const_2542044179 = Integer(2542044179)
_sage_const_3350508659 = Integer(3350508659)
_sage_const_2906778797 = Integer(2906778797)
_sage_const_0xfa = Integer(0xfa)
_sage_const_0xfb = Integer(0xfb)
_sage_const_0xfc = Integer(0xfc)
_sage_const_0xfd = Integer(0xfd)
_sage_const_0xfe = Integer(0xfe)
_sage_const_0xff = Integer(0xff)
_sage_const_388905239 = Integer(388905239)
_sage_const_3160661948 = Integer(3160661948)
_sage_const_251987210 = Integer(251987210)
_sage_const_4003034999 = Integer(4003034999)
_sage_const_3653156455 = Integer(3653156455)
_sage_const_4154762323 = Integer(4154762323)
_sage_const_1144798328 = Integer(1144798328)
_sage_const_2543269282 = Integer(2543269282)
_sage_const_1550986798 = Integer(1550986798)
_sage_const_879254580 = Integer(879254580)
_sage_const_859006549 = Integer(859006549)
_sage_const_1115997762 = Integer(1115997762)
_sage_const_2977548465 = Integer(2977548465)
_sage_const_807933976 = Integer(807933976)
_sage_const_1315514151 = Integer(1315514151)
_sage_const_335083755 = Integer(335083755)
_sage_const_133494003 = Integer(133494003)
_sage_const_1001099408 = Integer(1001099408)
_sage_const_2045938553 = Integer(2045938553)
_sage_const_67636228 = Integer(67636228)
_sage_const_3587551588 = Integer(3587551588)
_sage_const_3612167578 = Integer(3612167578)
_sage_const_1949051992 = Integer(1949051992)
_sage_const_185998603 = Integer(185998603)
_sage_const_941890588 = Integer(941890588)
_sage_const_2382858638 = Integer(2382858638)
_sage_const_909536346 = Integer(909536346)
_sage_const_3475368682 = Integer(3475368682)
_sage_const_33818114 = Integer(33818114)
_sage_const_269492272 = Integer(269492272)
_sage_const_1255133061 = Integer(1255133061)
_sage_const_842163286 = Integer(842163286)
_sage_const_3231735904 = Integer(3231735904)
_sage_const_371002123 = Integer(371002123)
_sage_const_463175808 = Integer(463175808)
_sage_const_3144537787 = Integer(3144537787)
_sage_const_2282455944 = Integer(2282455944)
_sage_const_3570709351 = Integer(3570709351)
_sage_const_4178113009 = Integer(4178113009)
_sage_const_1917532473 = Integer(1917532473)
_sage_const_1132905795 = Integer(1132905795)
_sage_const_1851340599 = Integer(1851340599)
_sage_const_387395129 = Integer(387395129)
_sage_const_3177307325 = Integer(3177307325)
_sage_const_100991747 = Integer(100991747)
_sage_const_1454176854 = Integer(1454176854)
_sage_const_0x49 = Integer(0x49)
_sage_const_368769775 = Integer(368769775)
_sage_const_1034851219 = Integer(1034851219)
_sage_const_727088427 = Integer(727088427)
_sage_const_3736170351 = Integer(3736170351)
_sage_const_1741597031 = Integer(1741597031)
_sage_const_270010376 = Integer(270010376)
_sage_const_2807427751 = Integer(2807427751)
_sage_const_3902567540 = Integer(3902567540)
_sage_const_573772049 = Integer(573772049)
_sage_const_724260477 = Integer(724260477)
_sage_const_4261273884 = Integer(4261273884)
_sage_const_675025940 = Integer(675025940)
_sage_const_800430746 = Integer(800430746)
_sage_const_2863288293 = Integer(2863288293)
_sage_const_557998881 = Integer(557998881)
_sage_const_4110612471 = Integer(4110612471)
_sage_const_1149815876 = Integer(1149815876)
_sage_const_3433719398 = Integer(3433719398)
_sage_const_1864705354 = Integer(1864705354)
_sage_const_0x8B = Integer(0x8B)
_sage_const_1031423805 = Integer(1031423805)
_sage_const_606357612 = Integer(606357612)
_sage_const_2061492133 = Integer(2061492133)
_sage_const_1953818780 = Integer(1953818780)
_sage_const_3501832553 = Integer(3501832553)
_sage_const_0x8D = Integer(0x8D)
_sage_const_1113792801 = Integer(1113792801)
_sage_const_0x8E = Integer(0x8E)
_sage_const_2560109491 = Integer(2560109491)
_sage_const_2994720178 = Integer(2994720178)
_sage_const_252648977 = Integer(252648977)
_sage_const_2664517455 = Integer(2664517455)
_sage_const_1061125697 = Integer(1061125697)
_sage_const_2316273034 = Integer(2316273034)
_sage_const_0xA6 = Integer(0xA6)
_sage_const_236720654 = Integer(236720654)
_sage_const_3602627437 = Integer(3602627437)
_sage_const_3840201527 = Integer(3840201527)
_sage_const_1583267042 = Integer(1583267042)
_sage_const_2029029496 = Integer(2029029496)
_sage_const_1920132246 = Integer(1920132246)
_sage_const_3194645204 = Integer(3194645204)
_sage_const_3149622742 = Integer(3149622742)
_sage_const_3435955023 = Integer(3435955023)
_sage_const_1764173646 = Integer(1764173646)
_sage_const_1994120109 = Integer(1994120109)
_sage_const_3381215433 = Integer(3381215433)
_sage_const_3110654417 = Integer(3110654417)
_sage_const_2640233411 = Integer(2640233411)
_sage_const_3671764853 = Integer(3671764853)
_sage_const_1145342156 = Integer(1145342156)
_sage_const_12 = Integer(12)
_sage_const_11 = Integer(11)
_sage_const_10 = Integer(10)
_sage_const_16 = Integer(16)
_sage_const_15 = Integer(15)
_sage_const_14 = Integer(14)
_sage_const_117902857 = Integer(117902857)
_sage_const_507257374 = Integer(507257374)
_sage_const_605822008 = Integer(605822008)
_sage_const_4245615603 = Integer(4245615603)
_sage_const_3164445985 = Integer(3164445985)
_sage_const_3638078323 = Integer(3638078323)
_sage_const_4255294047 = Integer(4255294047)
_sage_const_3958099238 = Integer(3958099238)
_sage_const_3528347292 = Integer(3528347292)
_sage_const_757946999 = Integer(757946999)
_sage_const_2441512471 = Integer(2441512471)
_sage_const_1403450707 = Integer(1403450707)
_sage_const_3722289532 = Integer(3722289532)
_sage_const_3610371814 = Integer(3610371814)
_sage_const_832869781 = Integer(832869781)
_sage_const_1487988824 = Integer(1487988824)
_sage_const_1606345055 = Integer(1606345055)
_sage_const_118360327 = Integer(118360327)
_sage_const_0xBF = Integer(0xBF)
_sage_const_2408514954 = Integer(2408514954)
_sage_const_3211123391 = Integer(3211123391)
_sage_const_250868733 = Integer(250868733)
_sage_const_0xBA = Integer(0xBA)
_sage_const_4279104242 = Integer(4279104242)
_sage_const_0xBC = Integer(0xBC)
_sage_const_3668932058 = Integer(3668932058)
_sage_const_1876277946 = Integer(1876277946)
_sage_const_16843267 = Integer(16843267)
_sage_const_4025468202 = Integer(4025468202)
_sage_const_3200149465 = Integer(3200149465)
_sage_const_2740846243 = Integer(2740846243)
_sage_const_2811532339 = Integer(2811532339)
_sage_const_3027004632 = Integer(3027004632)
_sage_const_899848087 = Integer(899848087)
_sage_const_1489093017 = Integer(1489093017)
_sage_const_0x6B = Integer(0x6B)
_sage_const_2642575903 = Integer(2642575903)
_sage_const_1817851446 = Integer(1817851446)
_sage_const_1251270218 = Integer(1251270218)
_sage_const_2463844681 = Integer(2463844681)
_sage_const_151589403 = Integer(151589403)
_sage_const_0xd6 = Integer(0xd6)
_sage_const_0xd7 = Integer(0xd7)
_sage_const_2491778321 = Integer(2491778321)
_sage_const_0xd5 = Integer(0xd5)
_sage_const_0xd2 = Integer(0xd2)
_sage_const_0xd3 = Integer(0xd3)
_sage_const_0xd0 = Integer(0xd0)
_sage_const_0xd1 = Integer(0xd1)
_sage_const_0xd8 = Integer(0xd8)
_sage_const_0xd9 = Integer(0xd9)
_sage_const_3628615824 = Integer(3628615824)
_sage_const_538984544 = Integer(538984544)
_sage_const_4227591446 = Integer(4227591446)
_sage_const_1296931543 = Integer(1296931543)
_sage_const_3819481163 = Integer(3819481163)
_sage_const_3214711843 = Integer(3214711843)
_sage_const_0xdd = Integer(0xdd)
_sage_const_0xde = Integer(0xde)
_sage_const_0xdb = Integer(0xdb)
_sage_const_0xdc = Integer(0xdc)
_sage_const_2273777042 = Integer(2273777042)
_sage_const_3419114822 = Integer(3419114822)
_sage_const_2942657994 = Integer(2942657994)
_sage_const_607523346 = Integer(607523346)
_sage_const_1886445712 = Integer(1886445712)
_sage_const_3240947181 = Integer(3240947181)
_sage_const_3937382213 = Integer(3937382213)
_sage_const_1673962851 = Integer(1673962851)
_sage_const_602466507 = Integer(602466507)
_sage_const_126455438 = Integer(126455438)
_sage_const_2606481600 = Integer(2606481600)
_sage_const_4021070915 = Integer(4021070915)
_sage_const_505297954 = Integer(505297954)
_sage_const_0x11 = Integer(0x11)
_sage_const_2553000856 = Integer(2553000856)
_sage_const_2189328124 = Integer(2189328124)
_sage_const_0x13 = Integer(0x13)
_sage_const_3225436288 = Integer(3225436288)
_sage_const_2215876484 = Integer(2215876484)
_sage_const_1707781989 = Integer(1707781989)
_sage_const_1229558491 = Integer(1229558491)
_sage_const_3265487201 = Integer(3265487201)
_sage_const_690573947 = Integer(690573947)
_sage_const_2240449039 = Integer(2240449039)
_sage_const_676362280 = Integer(676362280)
_sage_const_4031795360 = Integer(4031795360)
_sage_const_1509466529 = Integer(1509466529)
_sage_const_3857043764 = Integer(3857043764)
_sage_const_3300242801 = Integer(3300242801)
_sage_const_168756485 = Integer(168756485)
_sage_const_3127891386 = Integer(3127891386)
_sage_const_993752653 = Integer(993752653)
_sage_const_294946181 = Integer(294946181)
_sage_const_3131023141 = Integer(3131023141)
_sage_const_1055122397 = Integer(1055122397)
_sage_const_4259388669 = Integer(4259388669)
_sage_const_452984805 = Integer(452984805)
_sage_const_3755976058 = Integer(3755976058)
_sage_const_3368586051 = Integer(3368586051)
_sage_const_1538714971 = Integer(1538714971)
_sage_const_2576951728 = Integer(2576951728)
_sage_const_255 = Integer(255)
_sage_const_256 = Integer(256)
_sage_const_1058346282 = Integer(1058346282)
_sage_const_67502594 = Integer(67502594)
_sage_const_1268178251 = Integer(1268178251)
_sage_const_2273148410 = Integer(2273148410)
_sage_const_2591454956 = Integer(2591454956)
_sage_const_201589768 = Integer(201589768)
_sage_const_2707028129 = Integer(2707028129)
_sage_const_2857362858 = Integer(2857362858)
_sage_const_1080041504 = Integer(1080041504)
_sage_const_1675607228 = Integer(1675607228)
_sage_const_2357986191 = Integer(2357986191)
_sage_const_0xa = Integer(0xa)
_sage_const_0xc = Integer(0xc)
_sage_const_2399505039 = Integer(2399505039)
_sage_const_0xe = Integer(0xe)
_sage_const_0xd = Integer(0xd)
_sage_const_0xf = Integer(0xf)
_sage_const_1814307912 = Integer(1814307912)
_sage_const_3009926356 = Integer(3009926356)
_sage_const_33751297 = Integer(33751297)
_sage_const_2071721613 = Integer(2071721613)
_sage_const_0x9 = Integer(0x9)
_sage_const_0x8 = Integer(0x8)
_sage_const_0x1 = Integer(0x1)
_sage_const_0x0 = Integer(0x0)
_sage_const_0x3 = Integer(0x3)
_sage_const_0x2 = Integer(0x2)
_sage_const_0x5 = Integer(0x5)
_sage_const_0x4 = Integer(0x4)
_sage_const_0x7 = Integer(0x7)
_sage_const_0x6 = Integer(0x6)
_sage_const_2332919435 = Integer(2332919435)
_sage_const_3168951902 = Integer(3168951902)
_sage_const_134746136 = Integer(134746136)
_sage_const_0x67 = Integer(0x67)
_sage_const_2505230279 = Integer(2505230279)
_sage_const_1215046692 = Integer(1215046692)
_sage_const_640044138 = Integer(640044138)
_sage_const_0xea = Integer(0xea)
_sage_const_0xec = Integer(0xec)
_sage_const_0xeb = Integer(0xeb)
_sage_const_0xee = Integer(0xee)
_sage_const_0xed = Integer(0xed)
_sage_const_0xef = Integer(0xef)
_sage_const_2835108948 = Integer(2835108948)
_sage_const_703524551 = Integer(703524551)
_sage_const_1978310517 = Integer(1978310517)
_sage_const_1683370546 = Integer(1683370546)
_sage_const_4115878822 = Integer(4115878822)
_sage_const_1584475951 = Integer(1584475951)
_sage_const_3216991706 = Integer(3216991706)
_sage_const_1338821763 = Integer(1338821763)
_sage_const_4042984432 = Integer(4042984432)
_sage_const_2711000631 = Integer(2711000631)
_sage_const_0xe9 = Integer(0xe9)
_sage_const_0xe8 = Integer(0xe8)
_sage_const_0xe1 = Integer(0xe1)
_sage_const_0xe0 = Integer(0xe0)
_sage_const_0xe3 = Integer(0xe3)
_sage_const_0xe2 = Integer(0xe2)
_sage_const_0xe5 = Integer(0xe5)
_sage_const_0xe4 = Integer(0xe4)
_sage_const_0xe7 = Integer(0xe7)
_sage_const_0xe6 = Integer(0xe6)
_sage_const_3035519578 = Integer(3035519578)
_sage_const_3870010189 = Integer(3870010189)
_sage_const_591815971 = Integer(591815971)
_sage_const_3988860141 = Integer(3988860141)
_sage_const_3326231172 = Integer(3326231172)
_sage_const_2727843637 = Integer(2727843637)
_sage_const_2962856233 = Integer(2962856233)
_sage_const_3801313649 = Integer(3801313649)
_sage_const_2110698419 = Integer(2110698419)
_sage_const_2145180835 = Integer(2145180835)
_sage_const_1262041458 = Integer(1262041458)
_sage_const_1785386174 = Integer(1785386174)
_sage_const_2993581788 = Integer(2993581788)
_sage_const_2144187058 = Integer(2144187058)
_sage_const_3415033547 = Integer(3415033547)
_sage_const_641012499 = Integer(641012499)
_sage_const_152181513 = Integer(152181513)
_sage_const_3767562352 = Integer(3767562352)
_sage_const_436141799 = Integer(436141799)
_sage_const_4183250862 = Integer(4183250862)
_sage_const_2741068226 = Integer(2741068226)
_sage_const_490350365 = Integer(490350365)
_sage_const_4093447923 = Integer(4093447923)
_sage_const_1044282434 = Integer(1044282434)
_sage_const_1007948840 = Integer(1007948840)
_sage_const_1734856361 = Integer(1734856361)
_sage_const_4008625961 = Integer(4008625961)
_sage_const_656887401 = Integer(656887401)
_sage_const_1014514748 = Integer(1014514748)
_sage_const_3839047652 = Integer(3839047652)
_sage_const_642542118 = Integer(642542118)
_sage_const_226921355 = Integer(226921355)
_sage_const_302911004 = Integer(302911004)
_sage_const_3669999461 = Integer(3669999461)
_sage_const_3011366579 = Integer(3011366579)
_sage_const_743994412 = Integer(743994412)
_sage_const_3920539207 = Integer(3920539207)
_sage_const_2823545768 = Integer(2823545768)
_sage_const_2624877800 = Integer(2624877800)
_sage_const_1183631942 = Integer(1183631942)
_sage_const_1898917726 = Integer(1898917726)
_sage_const_2307821063 = Integer(2307821063)
_sage_const_1206496942 = Integer(1206496942)
_sage_const_1876865391 = Integer(1876865391)
_sage_const_0xF1 = Integer(0xF1)
_sage_const_0xF2 = Integer(0xF2)
_sage_const_0xF3 = Integer(0xF3)
_sage_const_0xF4 = Integer(0xF4)
_sage_const_0xF5 = Integer(0xF5)
_sage_const_0xF6 = Integer(0xF6)
_sage_const_2236272591 = Integer(2236272591)
_sage_const_0xF8 = Integer(0xF8)
_sage_const_0xF9 = Integer(0xF9)
_sage_const_3910203897 = Integer(3910203897)
_sage_const_0xFA = Integer(0xFA)
_sage_const_0xFB = Integer(0xFB)
_sage_const_0xFC = Integer(0xFC)
_sage_const_0xFD = Integer(0xFD)
_sage_const_0xFE = Integer(0xFE)
_sage_const_0xFF = Integer(0xFF)
_sage_const_1234361161 = Integer(1234361161)
_sage_const_3299238498 = Integer(3299238498)
_sage_const_1758581177 = Integer(1758581177)
_sage_const_3943954680 = Integer(3943954680)
_sage_const_1842789307 = Integer(1842789307)
_sage_const_2374828428 = Integer(2374828428)
_sage_const_253628687 = Integer(253628687)
_sage_const_2586817946 = Integer(2586817946)
_sage_const_2743065820 = Integer(2743065820)
_sage_const_933336726 = Integer(933336726)
_sage_const_673730680 = Integer(673730680)
_sage_const_854058965 = Integer(854058965)
_sage_const_0xb8 = Integer(0xb8)
_sage_const_0xb9 = Integer(0xb9)
_sage_const_2930657257 = Integer(2930657257)
_sage_const_0xb4 = Integer(0xb4)
_sage_const_0xb5 = Integer(0xb5)
_sage_const_0xb6 = Integer(0xb6)
_sage_const_0xb7 = Integer(0xb7)
_sage_const_0xb0 = Integer(0xb0)
_sage_const_0xb1 = Integer(0xb1)
_sage_const_0xb2 = Integer(0xb2)
_sage_const_0xb3 = Integer(0xb3)
_sage_const_1716859699 = Integer(1716859699)
_sage_const_2779075060 = Integer(2779075060)
_sage_const_1448520954 = Integer(1448520954)
_sage_const_775493399 = Integer(775493399)
_sage_const_3718347997 = Integer(3718347997)
_sage_const_3769215305 = Integer(3769215305)
_sage_const_0xbd = Integer(0xbd)
_sage_const_0xbe = Integer(0xbe)
_sage_const_0xbf = Integer(0xbf)
_sage_const_0xba = Integer(0xba)
_sage_const_2890133420 = Integer(2890133420)
_sage_const_0xbc = Integer(0xbc)
_sage_const_3309519750 = Integer(3309519750)
_sage_const_2139094657 = Integer(2139094657)
_sage_const_4136467323 = Integer(4136467323)
_sage_const_2690670784 = Integer(2690670784)
_sage_const_566009245 = Integer(566009245)
_sage_const_1802229437 = Integer(1802229437)
_sage_const_2694863867 = Integer(2694863867)
_sage_const_2012125559 = Integer(2012125559)
_sage_const_907153956 = Integer(907153956)
_sage_const_1330618065 = Integer(1330618065)
_sage_const_284817897 = Integer(284817897)
_sage_const_1371981463 = Integer(1371981463)
_sage_const_2206763019 = Integer(2206763019)
_sage_const_4059629809 = Integer(4059629809)
_sage_const_1758509160 = Integer(1758509160)
_sage_const_3898103984 = Integer(3898103984)
_sage_const_937747667 = Integer(937747667)
_sage_const_2183110018 = Integer(2183110018)
_sage_const_4143383030 = Integer(4143383030)
_sage_const_3969545846 = Integer(3969545846)
_sage_const_3924412704 = Integer(3924412704)
_sage_const_2362066502 = Integer(2362066502)
_sage_const_3183305180 = Integer(3183305180)
_sage_const_1496790894 = Integer(1496790894)
_sage_const_892693087 = Integer(892693087)
_sage_const_1422247313 = Integer(1422247313)
_sage_const_150073849 = Integer(150073849)
_sage_const_361924487 = Integer(361924487)
_sage_const_202119188 = Integer(202119188)
_sage_const_338181140 = Integer(338181140)
_sage_const_3678134496 = Integer(3678134496)
_sage_const_3520182632 = Integer(3520182632)
_sage_const_3043153879 = Integer(3043153879)
_sage_const_804056259 = Integer(804056259)
_sage_const_825320019 = Integer(825320019)
_sage_const_2678007226 = Integer(2678007226)
_sage_const_3144247762 = Integer(3144247762)
_sage_const_2408352771 = Integer(2408352771)
_sage_const_908925723 = Integer(908925723)
_sage_const_287453969 = Integer(287453969)
_sage_const_0xA4 = Integer(0xA4)
_sage_const_2631028302 = Integer(2631028302)
_sage_const_286335539 = Integer(286335539)
_sage_const_336865340 = Integer(336865340)
_sage_const_708777237 = Integer(708777237)
_sage_const_67373068 = Integer(67373068)
_sage_const_2531085131 = Integer(2531085131)
_sage_const_837215959 = Integer(837215959)
_sage_const_1780885068 = Integer(1780885068)
_sage_const_3431157708 = Integer(3431157708)
_sage_const_2172721560 = Integer(2172721560)
_sage_const_3905627112 = Integer(3905627112)
_sage_const_3464972750 = Integer(3464972750)
_sage_const_1657054818 = Integer(1657054818)
_sage_const_3644383713 = Integer(3644383713)
_sage_const_2876496088 = Integer(2876496088)
_sage_const_487262998 = Integer(487262998)
_sage_const_1835915959 = Integer(1835915959)
_sage_const_828527409 = Integer(828527409)
_sage_const_0xcf = Integer(0xcf)
_sage_const_0xce = Integer(0xce)
_sage_const_0xcd = Integer(0xcd)
_sage_const_0xcc = Integer(0xcc)
_sage_const_0xcb = Integer(0xcb)
_sage_const_3970805057 = Integer(3970805057)
_sage_const_3872862694 = Integer(3872862694)
_sage_const_1162185423 = Integer(1162185423)
_sage_const_1859376061 = Integer(1859376061)
_sage_const_976909390 = Integer(976909390)
_sage_const_1961401460 = Integer(1961401460)
_sage_const_3402272581 = Integer(3402272581)
_sage_const_0xc9 = Integer(0xc9)
_sage_const_0xc8 = Integer(0xc8)
_sage_const_0xc7 = Integer(0xc7)
_sage_const_0xc6 = Integer(0xc6)
_sage_const_0xc5 = Integer(0xc5)
_sage_const_0xc4 = Integer(0xc4)
_sage_const_0xc3 = Integer(0xc3)
_sage_const_0xc2 = Integer(0xc2)
_sage_const_0xc1 = Integer(0xc1)
_sage_const_0xc0 = Integer(0xc0)
_sage_const_791633521 = Integer(791633521)
_sage_const_49805301 = Integer(49805301)
_sage_const_2155879323 = Integer(2155879323)
_sage_const_2062847610 = Integer(2062847610)
_sage_const_4160222466 = Integer(4160222466)
_sage_const_3114180135 = Integer(3114180135)
_sage_const_3806519101 = Integer(3806519101)
_sage_const_1212715224 = Integer(1212715224)
_sage_const_4035475576 = Integer(4035475576)
_sage_const_3441880043 = Integer(3441880043)
_sage_const_572399164 = Integer(572399164)
_sage_const_1775418217 = Integer(1775418217)
_sage_const_1663115586 = Integer(1663115586)
_sage_const_1472513171 = Integer(1472513171)
_sage_const_3166462943 = Integer(3166462943)
_sage_const_4176155640 = Integer(4176155640)
_sage_const_963791673 = Integer(963791673)
_sage_const_2536874647 = Integer(2536874647)
_sage_const_3735517662 = Integer(3735517662)
_sage_const_957814574 = Integer(957814574)
_sage_const_1597322602 = Integer(1597322602)
_sage_const_0x8b = Integer(0x8b)
_sage_const_0x8c = Integer(0x8c)
_sage_const_0x8a = Integer(0x8a)
_sage_const_0x8f = Integer(0x8f)
_sage_const_0x8d = Integer(0x8d)
_sage_const_0x8e = Integer(0x8e)
_sage_const_1128498885 = Integer(1128498885)
_sage_const_1352724560 = Integer(1352724560)
_sage_const_3561770136 = Integer(3561770136)
_sage_const_1999449434 = Integer(1999449434)
_sage_const_1099088705 = Integer(1099088705)
_sage_const_370551866 = Integer(370551866)
_sage_const_0x8C = Integer(0x8C)
_sage_const_0x8A = Integer(0x8A)
_sage_const_0x8F = Integer(0x8F)
_sage_const_3099093971 = Integer(3099093971)
_sage_const_3752164063 = Integer(3752164063)
_sage_const_0x88 = Integer(0x88)
_sage_const_0x89 = Integer(0x89)
_sage_const_540020752 = Integer(540020752)
_sage_const_0x82 = Integer(0x82)
_sage_const_0x83 = Integer(0x83)
_sage_const_0x80 = Integer(0x80)
_sage_const_0x81 = Integer(0x81)
_sage_const_0x86 = Integer(0x86)
_sage_const_0x87 = Integer(0x87)
_sage_const_0x84 = Integer(0x84)
_sage_const_0x85 = Integer(0x85)
_sage_const_967348625 = Integer(967348625)
_sage_const_202904588 = Integer(202904588)
_sage_const_1751699640 = Integer(1751699640)
_sage_const_1987505306 = Integer(1987505306)
_sage_const_3281870531 = Integer(3281870531)
_sage_const_1048330814 = Integer(1048330814)
_sage_const_2257292045 = Integer(2257292045)
_sage_const_0x6A = Integer(0x6A)
_sage_const_1742001331 = Integer(1742001331)
_sage_const_0x6C = Integer(0x6C)
_sage_const_0x6D = Integer(0x6D)
_sage_const_0x6E = Integer(0x6E)
_sage_const_0x6F = Integer(0x6F)
_sage_const_777810478 = Integer(777810478)
_sage_const_1246401758 = Integer(1246401758)
_sage_const_1465364217 = Integer(1465364217)
_sage_const_2878378043 = Integer(2878378043)
_sage_const_1381147894 = Integer(1381147894)
_sage_const_0x6a = Integer(0x6a)
_sage_const_0x6b = Integer(0x6b)
_sage_const_0x6c = Integer(0x6c)
_sage_const_0x6d = Integer(0x6d)
_sage_const_0x6e = Integer(0x6e)
_sage_const_0x6f = Integer(0x6f)
_sage_const_59739276 = Integer(59739276)
_sage_const_2597801293 = Integer(2597801293)
_sage_const_2507371494 = Integer(2507371494)
_sage_const_1883781176 = Integer(1883781176)
_sage_const_3635114968 = Integer(3635114968)
_sage_const_2608889883 = Integer(2608889883)
_sage_const_0x60 = Integer(0x60)
_sage_const_0x61 = Integer(0x61)
_sage_const_4203183485 = Integer(4203183485)
_sage_const_0x63 = Integer(0x63)
_sage_const_0x64 = Integer(0x64)
_sage_const_0x65 = Integer(0x65)
_sage_const_0x66 = Integer(0x66)
_sage_const_1696801606 = Integer(1696801606)
_sage_const_0x68 = Integer(0x68)
_sage_const_0x69 = Integer(0x69)
_sage_const_524165407 = Integer(524165407)
_sage_const_437718285 = Integer(437718285)
_sage_const_3048567236 = Integer(3048567236)
_sage_const_2203045068 = Integer(2203045068)
_sage_const_3044132021 = Integer(3044132021)
_sage_const_3266819957 = Integer(3266819957)
_sage_const_0xF0 = Integer(0xF0)
_sage_const_3679013266 = Integer(3679013266)
_sage_const_0xD6 = Integer(0xD6)
_sage_const_0xD7 = Integer(0xD7)
_sage_const_0xD4 = Integer(0xD4)
_sage_const_0xD5 = Integer(0xD5)
_sage_const_0xD2 = Integer(0xD2)
_sage_const_0xD3 = Integer(0xD3)
_sage_const_0xD0 = Integer(0xD0)
_sage_const_0xD1 = Integer(0xD1)
_sage_const_0xD8 = Integer(0xD8)
_sage_const_0xD9 = Integer(0xD9)
_sage_const_0xDF = Integer(0xDF)
_sage_const_0xDD = Integer(0xDD)
_sage_const_0xDE = Integer(0xDE)
_sage_const_0xDB = Integer(0xDB)
_sage_const_0xDC = Integer(0xDC)
_sage_const_0xDA = Integer(0xDA)
_sage_const_723065138 = Integer(723065138)
_sage_const_943222856 = Integer(943222856)
_sage_const_0xF7 = Integer(0xF7)
_sage_const_4006029806 = Integer(4006029806)
_sage_const_2603464347 = Integer(2603464347)
_sage_const_2438251973 = Integer(2438251973)
_sage_const_2172616702 = Integer(2172616702)
_sage_const_453576978 = Integer(453576978)
_sage_const_3275833730 = Integer(3275833730)
_sage_const_2520228246 = Integer(2520228246)
_sage_const_2147385727 = Integer(2147385727)
_sage_const_1484008492 = Integer(1484008492)
_sage_const_1282024998 = Integer(1282024998)
_sage_const_1147544098 = Integer(1147544098)
_sage_const_652995533 = Integer(652995533)
_sage_const_2526427041 = Integer(2526427041)
_sage_const_1975695287 = Integer(1975695287)
_sage_const_3013122091 = Integer(3013122091)
_sage_const_2673722050 = Integer(2673722050)
_sage_const_355090197 = Integer(355090197)
_sage_const_486407649 = Integer(486407649)
_sage_const_1667483301 = Integer(1667483301)
_sage_const_742004246 = Integer(742004246)
_sage_const_3307925487 = Integer(3307925487)
_sage_const_4011195130 = Integer(4011195130)
_sage_const_3063651117 = Integer(3063651117)
_sage_const_1340451498 = Integer(1340451498)
_sage_const_4169432188 = Integer(4169432188)
_sage_const_2842745305 = Integer(2842745305)
_sage_const_1984772923 = Integer(1984772923)
_sage_const_3702681198 = Integer(3702681198)
_sage_const_2497595978 = Integer(2497595978)
_sage_const_3341414126 = Integer(3341414126)
_sage_const_720367557 = Integer(720367557)
_sage_const_2774754246 = Integer(2774754246)
_sage_const_0xCE = Integer(0xCE)
_sage_const_2266337927 = Integer(2266337927)
_sage_const_0x1e = Integer(0x1e)
_sage_const_1610457762 = Integer(1610457762)
_sage_const_3972214764 = Integer(3972214764)
_sage_const_3334903633 = Integer(3334903633)
_sage_const_2370227147 = Integer(2370227147)
_sage_const_3618988759 = Integer(3618988759)
_sage_const_1612718144 = Integer(1612718144)
_sage_const_3535760850 = Integer(3535760850)
_sage_const_1600110305 = Integer(1600110305)
_sage_const_1573044895 = Integer(1573044895)
_sage_const_2593796021 = Integer(2593796021)
_sage_const_4126213365 = Integer(4126213365)
_sage_const_0x99 = Integer(0x99)
_sage_const_0x98 = Integer(0x98)
_sage_const_0x95 = Integer(0x95)
_sage_const_0x94 = Integer(0x94)
_sage_const_0x97 = Integer(0x97)
_sage_const_0x96 = Integer(0x96)
_sage_const_0x91 = Integer(0x91)
_sage_const_0x90 = Integer(0x90)
_sage_const_0x93 = Integer(0x93)
_sage_const_0x92 = Integer(0x92)
_sage_const_2017737788 = Integer(2017737788)
_sage_const_4244431647 = Integer(4244431647)
_sage_const_3265224130 = Integer(3265224130)
_sage_const_3248052417 = Integer(3248052417)
_sage_const_1546925160 = Integer(1546925160)
_sage_const_4102978170 = Integer(4102978170)
_sage_const_1869602481 = Integer(1869602481)
_sage_const_159418761 = Integer(159418761)
_sage_const_2261074755 = Integer(2261074755)
_sage_const_0x9e = Integer(0x9e)
_sage_const_0x9d = Integer(0x9d)
_sage_const_0x9f = Integer(0x9f)
_sage_const_3701702620 = Integer(3701702620)
_sage_const_0x9c = Integer(0x9c)
_sage_const_0x9b = Integer(0x9b)
_sage_const_2015897680 = Integer(2015897680)
_sage_const_1970662047 = Integer(1970662047)
_sage_const_0x9E = Integer(0x9E)
_sage_const_0x9D = Integer(0x9D)
_sage_const_0x9F = Integer(0x9F)
_sage_const_0x9A = Integer(0x9A)
_sage_const_0x9C = Integer(0x9C)
_sage_const_0x9B = Integer(0x9B)
_sage_const_488454695 = Integer(488454695)
_sage_const_0xEA = Integer(0xEA)
_sage_const_0xEC = Integer(0xEC)
_sage_const_3977706491 = Integer(3977706491)
_sage_const_0xEE = Integer(0xEE)
_sage_const_0xED = Integer(0xED)
_sage_const_0xEF = Integer(0xEF)
_sage_const_3654920560 = Integer(3654920560)
_sage_const_456535323 = Integer(456535323)
_sage_const_3602342358 = Integer(3602342358)
_sage_const_1217452104 = Integer(1217452104)
_sage_const_0x56 = Integer(0x56)
_sage_const_2193834305 = Integer(2193834305)
_sage_const_2524082916 = Integer(2524082916)
_sage_const_0x73 = Integer(0x73)
_sage_const_0x72 = Integer(0x72)
_sage_const_0x71 = Integer(0x71)
_sage_const_0x70 = Integer(0x70)
_sage_const_0x77 = Integer(0x77)
_sage_const_1566423783 = Integer(1566423783)
_sage_const_0x75 = Integer(0x75)
_sage_const_0x74 = Integer(0x74)
_sage_const_0x79 = Integer(0x79)
_sage_const_0x78 = Integer(0x78)
_sage_const_1995217526 = Integer(1995217526)
_sage_const_1482207464 = Integer(1482207464)
_sage_const_4092853518 = Integer(4092853518)
_sage_const_3853167183 = Integer(3853167183)
_sage_const_2038035083 = Integer(2038035083)
_sage_const_0x7C = Integer(0x7C)
_sage_const_2733855057 = Integer(2733855057)
_sage_const_0x7A = Integer(0x7A)
_sage_const_2711706104 = Integer(2711706104)
_sage_const_2661164985 = Integer(2661164985)
_sage_const_0x7D = Integer(0x7D)
_sage_const_3233848155 = Integer(3233848155)
_sage_const_1623236704 = Integer(1623236704)
_sage_const_2425371563 = Integer(2425371563)
_sage_const_2240090516 = Integer(2240090516)
_sage_const_2222750968 = Integer(2222750968)
_sage_const_0x7c = Integer(0x7c)
_sage_const_0x7b = Integer(0x7b)
_sage_const_0x7a = Integer(0x7a)
_sage_const_0x7f = Integer(0x7f)
_sage_const_0x7e = Integer(0x7e)
_sage_const_0x7d = Integer(0x7d)
_sage_const_0xE1 = Integer(0xE1)
_sage_const_0xE0 = Integer(0xE0)
_sage_const_0xE3 = Integer(0xE3)
_sage_const_0xE2 = Integer(0xE2)
_sage_const_0xE5 = Integer(0xE5)
_sage_const_0xE4 = Integer(0xE4)
_sage_const_0xE7 = Integer(0xE7)
_sage_const_0xE6 = Integer(0xE6)
_sage_const_337512970 = Integer(337512970)
_sage_const_2472002756 = Integer(2472002756)
_sage_const_733190296 = Integer(733190296)
_sage_const_2809781982 = Integer(2809781982)
_sage_const_2227585602 = Integer(2227585602)
_sage_const_2947499498 = Integer(2947499498)
_sage_const_3178157011 = Integer(3178157011)
_sage_const_2269761230 = Integer(2269761230)
_sage_const_2910247899 = Integer(2910247899)
_sage_const_3408128232 = Integer(3408128232)
_sage_const_2165938305 = Integer(2165938305)
_sage_const_1718013098 = Integer(1718013098)
_sage_const_2206408094 = Integer(2206408094)
_sage_const_1641469623 = Integer(1641469623)
_sage_const_1936975509 = Integer(1936975509)
_sage_const_756751158 = Integer(756751158)
_sage_const_3806281186 = Integer(3806281186)
_sage_const_2365688973 = Integer(2365688973)
_sage_const_3843751935 = Integer(3843751935)
_sage_const_2880130534 = Integer(2880130534)
_sage_const_4177062675 = Integer(4177062675)
_sage_const_3982187446 = Integer(3982187446)
_sage_const_0xa5 = Integer(0xa5)
_sage_const_0xa4 = Integer(0xa4)
_sage_const_0xa7 = Integer(0xa7)
_sage_const_0xa6 = Integer(0xa6)
_sage_const_0xa1 = Integer(0xa1)
_sage_const_0xa0 = Integer(0xa0)
_sage_const_0xa3 = Integer(0xa3)
_sage_const_0xa2 = Integer(0xa2)
_sage_const_555827811 = Integer(555827811)
_sage_const_2801095507 = Integer(2801095507)
_sage_const_0xa9 = Integer(0xa9)
_sage_const_0xa8 = Integer(0xa8)
_sage_const_1903288979 = Integer(1903288979)
_sage_const_0x5F = Integer(0x5F)
_sage_const_2912064063 = Integer(2912064063)
_sage_const_3231407040 = Integer(3231407040)
_sage_const_4192801017 = Integer(4192801017)
_sage_const_0xae = Integer(0xae)
_sage_const_0xad = Integer(0xad)
_sage_const_1166724933 = Integer(1166724933)
_sage_const_0xaf = Integer(0xaf)
_sage_const_0xaa = Integer(0xaa)
_sage_const_3031724999 = Integer(3031724999)
_sage_const_0xac = Integer(0xac)
_sage_const_0xab = Integer(0xab)
_sage_const_2998042573 = Integer(2998042573)
_sage_const_794718511 = Integer(794718511)
_sage_const_3115936208 = Integer(3115936208)
_sage_const_3604395873 = Integer(3604395873)
_sage_const_1650640038 = Integer(1650640038)
_sage_const_3331805638 = Integer(3331805638)
_sage_const_1318900302 = Integer(1318900302)
_sage_const_0xC7 = Integer(0xC7)
_sage_const_632987551 = Integer(632987551)
_sage_const_0xbb = Integer(0xbb)
_sage_const_0xC6 = Integer(0xC6)
_sage_const_0xC5 = Integer(0xC5)
_sage_const_887481809 = Integer(887481809)
_sage_const_2874009259 = Integer(2874009259)
_sage_const_4104496465 = Integer(4104496465)
_sage_const_0xC4 = Integer(0xC4)
_sage_const_0x5e = Integer(0x5e)
_sage_const_0xC2 = Integer(0xC2)
_sage_const_2928907069 = Integer(2928907069)
_sage_const_0x5f = Integer(0x5f)
_sage_const_3417354363 = Integer(3417354363)
_sage_const_3518589137 = Integer(3518589137)
_sage_const_2644320700 = Integer(2644320700)
_sage_const_2430093384 = Integer(2430093384)
_sage_const_710180394 = Integer(710180394)
_sage_const_997608763 = Integer(997608763)
_sage_const_0x4F = Integer(0x4F)
_sage_const_0x4D = Integer(0x4D)
_sage_const_0x4E = Integer(0x4E)
_sage_const_0x4B = Integer(0x4B)
_sage_const_0x4C = Integer(0x4C)
_sage_const_1239460265 = Integer(1239460265)
_sage_const_0x4A = Integer(0x4A)
_sage_const_3348452039 = Integer(3348452039)
_sage_const_3772832571 = Integer(3772832571)
_sage_const_811618352 = Integer(811618352)
_sage_const_437924910 = Integer(437924910)
_sage_const_4077384948 = Integer(4077384948)
_sage_const_0x4f = Integer(0x4f)
_sage_const_4233385128 = Integer(4233385128)
_sage_const_0x4d = Integer(0x4d)
_sage_const_0x4e = Integer(0x4e)
_sage_const_0x4b = Integer(0x4b)
_sage_const_0x4c = Integer(0x4c)
_sage_const_1517759789 = Integer(1517759789)
_sage_const_0x4a = Integer(0x4a)
_sage_const_693271337 = Integer(693271337)
_sage_const_2756966308 = Integer(2756966308)
_sage_const_741103732 = Integer(741103732)
_sage_const_2896970735 = Integer(2896970735)
_sage_const_1451043627 = Integer(1451043627)
_sage_const_0x46 = Integer(0x46)
_sage_const_0x47 = Integer(0x47)
_sage_const_0x44 = Integer(0x44)
_sage_const_0x45 = Integer(0x45)
_sage_const_0x42 = Integer(0x42)
_sage_const_0x43 = Integer(0x43)
_sage_const_0x40 = Integer(0x40)
_sage_const_0x41 = Integer(0x41)
_sage_const_1383803177 = Integer(1383803177)
_sage_const_303761673 = Integer(303761673)
_sage_const_0x48 = Integer(0x48)
_sage_const_2043195825 = Integer(2043195825)
_sage_const_4126535940 = Integer(4126535940)
_sage_const_3001768281 = Integer(3001768281)
_sage_const_151455502 = Integer(151455502)
_sage_const_321271059 = Integer(321271059)
_sage_const_1285084236 = Integer(1285084236)
_sage_const_2776293343 = Integer(2776293343)
_sage_const_404238376 = Integer(404238376)
_sage_const_1369633617 = Integer(1369633617)
_sage_const_625635109 = Integer(625635109)
_sage_const_866620564 = Integer(866620564)
_sage_const_2130477694 = Integer(2130477694)
_sage_const_3467883389 = Integer(3467883389)
_sage_const_0xB8 = Integer(0xB8)
_sage_const_0xB9 = Integer(0xB9)
_sage_const_0xB4 = Integer(0xB4)
_sage_const_0xB5 = Integer(0xB5)
_sage_const_0xB6 = Integer(0xB6)
_sage_const_0xB7 = Integer(0xB7)
_sage_const_0xB0 = Integer(0xB0)
_sage_const_0xB1 = Integer(0xB1)
_sage_const_0xB2 = Integer(0xB2)
_sage_const_0xB3 = Integer(0xB3)
_sage_const_1170918031 = Integer(1170918031)
_sage_const_0xBD = Integer(0xBD)
_sage_const_0xBE = Integer(0xBE)
_sage_const_1589887901 = Integer(1589887901)
_sage_const_286199582 = Integer(286199582)
_sage_const_0xBB = Integer(0xBB)
_sage_const_4209972730 = Integer(4209972730)
_sage_const_3509904869 = Integer(3509904869)
_sage_const_2940594863 = Integer(2940594863)
_sage_const_3998898868 = Integer(3998898868)
_sage_const_4143380225 = Integer(4143380225)
_sage_const_2223248279 = Integer(2223248279)
_sage_const_4211863792 = Integer(4211863792)
_sage_const_2249691526 = Integer(2249691526)
_sage_const_1374987685 = Integer(1374987685)
_sage_const_0x9a = Integer(0x9a)
_sage_const_4132590244 = Integer(4132590244)
_sage_const_1809037496 = Integer(1809037496)
_sage_const_1004593371 = Integer(1004593371)
_sage_const_2761266481 = Integer(2761266481)
_sage_const_1187761037 = Integer(1187761037)
_sage_const_3948501426 = Integer(3948501426)
_sage_const_3772464096 = Integer(3772464096)
_sage_const_1927583346 = Integer(1927583346)
_sage_const_4210749205 = Integer(4210749205)
_sage_const_83228145 = Integer(83228145)
_sage_const_3 = Integer(3)
_sage_const_2 = Integer(2)
_sage_const_1 = Integer(1)
_sage_const_0 = Integer(0)
_sage_const_7 = Integer(7)
_sage_const_6 = Integer(6)
_sage_const_5 = Integer(5)
_sage_const_4 = Integer(4)
_sage_const_9 = Integer(9)
_sage_const_8 = Integer(8)
_sage_const_1543217312 = Integer(1543217312)
_sage_const_1549580516 = Integer(1549580516)
_sage_const_980700730 = Integer(980700730)
_sage_const_2767606354 = Integer(2767606354)
_sage_const_2636233885 = Integer(2636233885)
_sage_const_304363026 = Integer(304363026)
_sage_const_2840191145 = Integer(2840191145)
_sage_const_2943736538 = Integer(2943736538)
_sage_const_2791465668 = Integer(2791465668)
_sage_const_135005188 = Integer(135005188)
_sage_const_2328839493 = Integer(2328839493)
_sage_const_3267534685 = Integer(3267534685)
_sage_const_2812761586 = Integer(2812761586)
_sage_const_2004348569 = Integer(2004348569)
_sage_const_2653403550 = Integer(2653403550)
_sage_const_3753688163 = Integer(3753688163)
_sage_const_33686534 = Integer(33686534)
_sage_const_3855693029 = Integer(3855693029)
_sage_const_3274697964 = Integer(3274697964)
_sage_const_2324664069 = Integer(2324664069)
_sage_const_3211645650 = Integer(3211645650)
_sage_const_2113570685 = Integer(2113570685)
_sage_const_2690382752 = Integer(2690382752)
_sage_const_0xEB = Integer(0xEB)
_sage_const_1181033251 = Integer(1181033251)
_sage_const_1852759218 = Integer(1852759218)
_sage_const_4283782570 = Integer(4283782570)
_sage_const_1364304627 = Integer(1364304627)
_sage_const_574907938 = Integer(574907938)
_sage_const_3781124030 = Integer(3781124030)
_sage_const_3703422305 = Integer(3703422305)
_sage_const_1842533055 = Integer(1842533055)
_sage_const_806359072 = Integer(806359072)
_sage_const_2094914977 = Integer(2094914977)
_sage_const_1106029997 = Integer(1106029997)
_sage_const_0xCF = Integer(0xCF)
_sage_const_2913812972 = Integer(2913812972)
_sage_const_0xCD = Integer(0xCD)
_sage_const_0xCC = Integer(0xCC)
_sage_const_0xCB = Integer(0xCB)
_sage_const_0xCA = Integer(0xCA)
_sage_const_2619588508 = Integer(2619588508)
_sage_const_1641856445 = Integer(1641856445)
_sage_const_0x59 = Integer(0x59)
_sage_const_0x58 = Integer(0x58)
_sage_const_890442534 = Integer(890442534)
_sage_const_0x51 = Integer(0x51)
_sage_const_0x50 = Integer(0x50)
_sage_const_0x53 = Integer(0x53)
_sage_const_0x52 = Integer(0x52)
_sage_const_0x55 = Integer(0x55)
_sage_const_0x54 = Integer(0x54)
_sage_const_0x57 = Integer(0x57)
_sage_const_3332727651 = Integer(3332727651)
_sage_const_1943591083 = Integer(1943591083)
_sage_const_2492740519 = Integer(2492740519)
_sage_const_1347461360 = Integer(1347461360)
_sage_const_2044649127 = Integer(2044649127)
_sage_const_3376891790 = Integer(3376891790)
_sage_const_2745392638 = Integer(2745392638)
_sage_const_0x5A = Integer(0x5A)
_sage_const_0x5C = Integer(0x5C)
_sage_const_0x5B = Integer(0x5B)
_sage_const_0x5E = Integer(0x5E)
_sage_const_0x5D = Integer(0x5D)
_sage_const_0x76 = Integer(0x76)
_sage_const_2829601763 = Integer(2829601763)
_sage_const_1576969123 = Integer(1576969123)
_sage_const_0xC9 = Integer(0xC9)
_sage_const_0xC8 = Integer(0xC8)
_sage_const_0x5a = Integer(0x5a)
_sage_const_92966799 = Integer(92966799)
_sage_const_0x5c = Integer(0x5c)
_sage_const_0x5b = Integer(0x5b)
_sage_const_0xC3 = Integer(0xC3)
_sage_const_0x5d = Integer(0x5d)
_sage_const_0xC1 = Integer(0xC1)
_sage_const_0xC0 = Integer(0xC0)
_sage_const_2199756419 = Integer(2199756419)
_sage_const_3688607094 = Integer(3688607094)
_sage_const_1708834751 = Integer(1708834751)
_sage_const_395413126 = Integer(395413126)
_sage_const_2558624025 = Integer(2558624025)
_sage_const_2302724553 = Integer(2302724553)
_sage_const_2976175573 = Integer(2976175573)
_sage_const_0xd4 = Integer(0xd4)
_sage_const_2289596656 = Integer(2289596656)
_sage_const_1724688998 = Integer(1724688998)
_sage_const_3061301686 = Integer(3061301686)
_sage_const_4293204735 = Integer(4293204735)
_sage_const_875849820 = Integer(875849820)
_sage_const_3789674808 = Integer(3789674808)
_sage_const_1111375484 = Integer(1111375484)
_sage_const_3284376926 = Integer(3284376926)
_sage_const_1441965991 = Integer(1441965991)
_sage_const_555687742 = Integer(555687742)
_sage_const_1038279391 = Integer(1038279391)
_sage_const_2232521861 = Integer(2232521861)
_sage_const_1658312629 = Integer(1658312629)
_sage_const_1532737261 = Integer(1532737261)
_sage_const_875436570 = Integer(875436570)
_sage_const_773462580 = Integer(773462580)
_sage_const_2458355477 = Integer(2458355477)
_sage_const_0x7B = Integer(0x7B)
_sage_const_1915629148 = Integer(1915629148)
_sage_const_0x7F = Integer(0x7F)
_sage_const_235805714 = Integer(235805714)
_sage_const_0x7E = Integer(0x7E)
_sage_const_3101973596 = Integer(3101973596)
_sage_const_3481619151 = Integer(3481619151)
_sage_const_2828112185 = Integer(2828112185)
_sage_const_0x0A = Integer(0x0A)
_sage_const_1094812355 = Integer(1094812355)
_sage_const_2902087254 = Integer(2902087254)
_sage_const_0x0E = Integer(0x0E)
_sage_const_2795919345 = Integer(2795919345)
_sage_const_3956090603 = Integer(3956090603)
_sage_const_3447803085 = Integer(3447803085)
_sage_const_2079755643 = Integer(2079755643)
_sage_const_2118205247 = Integer(2118205247)
_sage_const_3501746280 = Integer(3501746280)
_sage_const_2324303749 = Integer(2324303749)
_sage_const_303178806 = Integer(303178806)
_sage_const_2858837708 = Integer(2858837708)
_sage_const_0xdf = Integer(0xdf)
_sage_const_1010595908 = Integer(1010595908)
_sage_const_2670049951 = Integer(2670049951)
_sage_const_0x2D = Integer(0x2D)
_sage_const_0x2E = Integer(0x2E)
_sage_const_0x2F = Integer(0x2F)
_sage_const_808476752 = Integer(808476752)
_sage_const_0x2A = Integer(0x2A)
_sage_const_0x2B = Integer(0x2B)
_sage_const_0x2C = Integer(0x2C)
_sage_const_0xE9 = Integer(0xE9)
_sage_const_0xE8 = Integer(0xE8)
_sage_const_3202441055 = Integer(3202441055)
_sage_const_0xda = Integer(0xda)
_sage_const_2473685474 = Integer(2473685474)
_sage_const_4109693703 = Integer(4109693703)
_sage_const_0x2d = Integer(0x2d)
_sage_const_0x2e = Integer(0x2e)
_sage_const_0x2f = Integer(0x2f)
_sage_const_1335808335 = Integer(1335808335)
_sage_const_2923948462 = Integer(2923948462)
_sage_const_0x2b = Integer(0x2b)
_sage_const_0x2c = Integer(0x2c)
_sage_const_1345335392 = Integer(1345335392)
_sage_const_3621238114 = Integer(3621238114)
_sage_const_3451040383 = Integer(3451040383)
_sage_const_0x28 = Integer(0x28)
_sage_const_0x29 = Integer(0x29)
_sage_const_0x24 = Integer(0x24)
_sage_const_0x25 = Integer(0x25)
_sage_const_0x26 = Integer(0x26)
_sage_const_3077948087 = Integer(3077948087)
_sage_const_0x20 = Integer(0x20)
_sage_const_0x21 = Integer(0x21)
_sage_const_0x22 = Integer(0x22)
_sage_const_0x23 = Integer(0x23)
_sage_const_1139780780 = Integer(1139780780)
_sage_const_2066295122 = Integer(2066295122)
_sage_const_3467208551 = Integer(3467208551)
_sage_const_2762232823 = Integer(2762232823)
_sage_const_3301217111 = Integer(3301217111)
_sage_const_3789109473 = Integer(3789109473)
_sage_const_3535497577 = Integer(3535497577)
_sage_const_201983494 = Integer(201983494)
_sage_const_2846444000 = Integer(2846444000)
_sage_const_371997206 = Integer(371997206)
_sage_const_2009183926 = Integer(2009183926)
_sage_const_470945294 = Integer(470945294)
_sage_const_2574743534 = Integer(2574743534)
_sage_const_2627478463 = Integer(2627478463)
_sage_const_3939444202 = Integer(3939444202)
_sage_const_3576883175 = Integer(3576883175)
_sage_const_403966988 = Integer(403966988)
_sage_const_3881655738 = Integer(3881655738)
_sage_const_1295727478 = Integer(1295727478)
_sage_const_2054878350 = Integer(2054878350)
_sage_const_3314635973 = Integer(3314635973)
_sage_const_2538718918 = Integer(2538718918)
_sage_const_3835064946 = Integer(3835064946)
_sage_const_3543655652 = Integer(3543655652)
_sage_const_2336475336 = Integer(2336475336)
_sage_const_4171342169 = Integer(4171342169)
_sage_const_2773611685 = Integer(2773611685)
_sage_const_1504897881 = Integer(1504897881)
_sage_const_3553869166 = Integer(3553869166)
_sage_const_3364570056 = Integer(3364570056)
_sage_const_2868860245 = Integer(2868860245)
_sage_const_1515893998 = Integer(1515893998)
_sage_const_235472647 = Integer(235472647)
_sage_const_1065238847 = Integer(1065238847)
_sage_const_403179536 = Integer(403179536)
_sage_const_1313774802 = Integer(1313774802)
_sage_const_2290617219 = Integer(2290617219)
_sage_const_2470293139 = Integer(2470293139)
_sage_const_50397442 = Integer(50397442)
_sage_const_405809176 = Integer(405809176)
_sage_const_1742323390 = Integer(1742323390)
_sage_const_2503058581 = Integer(2503058581)
_sage_const_608726052 = Integer(608726052)
_sage_const_3831258296 = Integer(3831258296)
_sage_const_1977277103 = Integer(1977277103)
_sage_const_3194476990 = Integer(3194476990)
_sage_const_2084716094 = Integer(2084716094)
_sage_const_960066123 = Integer(960066123)
_sage_const_3082253762 = Integer(3082253762)
_sage_const_185275933 = Integer(185275933)
_sage_const_1263245021 = Integer(1263245021)
_sage_const_168432670 = Integer(168432670)
_sage_const_101059594 = Integer(101059594)
_sage_const_3093850320 = Integer(3093850320)
_sage_const_1173008303 = Integer(1173008303)
_sage_const_2122251394 = Integer(2122251394)
_sage_const_3585784431 = Integer(3585784431)
_sage_const_84216335 = Integer(84216335)
_sage_const_954327513 = Integer(954327513)
_sage_const_4071073621 = Integer(4071073621)
_sage_const_3501943760 = Integer(3501943760)
_sage_const_3568527316 = Integer(3568527316)
_sage_const_4221608027 = Integer(4221608027)
_sage_const_2169294285 = Integer(2169294285)
_sage_const_2116692564 = Integer(2116692564)
_sage_const_1388824469 = Integer(1388824469)
_sage_const_2453646738 = Integer(2453646738)
_sage_const_3046808111 = Integer(3046808111)
_sage_const_0x62 = Integer(0x62)
_sage_const_3027486644 = Integer(3027486644)
_sage_const_0x39 = Integer(0x39)
_sage_const_0x38 = Integer(0x38)
_sage_const_0x37 = Integer(0x37)
_sage_const_0x36 = Integer(0x36)
_sage_const_0x35 = Integer(0x35)
_sage_const_0x34 = Integer(0x34)
_sage_const_0x33 = Integer(0x33)
_sage_const_0x32 = Integer(0x32)
_sage_const_0x31 = Integer(0x31)
_sage_const_0x30 = Integer(0x30)
_sage_const_0xAE = Integer(0xAE)
_sage_const_0xAD = Integer(0xAD)
_sage_const_3393603212 = Integer(3393603212)
_sage_const_0xAF = Integer(0xAF)
_sage_const_0xAA = Integer(0xAA)
_sage_const_0xAC = Integer(0xAC)
_sage_const_0xAB = Integer(0xAB)
_sage_const_0xA5 = Integer(0xA5)
_sage_const_2307459456 = Integer(2307459456)
_sage_const_0xA7 = Integer(0xA7)
_sage_const_929978679 = Integer(929978679)
_sage_const_0xA1 = Integer(0xA1)
_sage_const_0xA0 = Integer(0xA0)
_sage_const_0xA3 = Integer(0xA3)
_sage_const_0xA2 = Integer(0xA2)
_sage_const_4160029431 = Integer(4160029431)
_sage_const_0xA9 = Integer(0xA9)
_sage_const_0xA8 = Integer(0xA8)
_sage_const_503974420 = Integer(503974420)
_sage_const_4109567988 = Integer(4109567988)
_sage_const_0x3F = Integer(0x3F)
_sage_const_0x3E = Integer(0x3E)
_sage_const_0x3D = Integer(0x3D)
_sage_const_0x3C = Integer(0x3C)
_sage_const_0x3B = Integer(0x3B)
_sage_const_0x3A = Integer(0x3A)
_sage_const_3486483786 = Integer(3486483786)
_sage_const_429425025 = Integer(429425025)
_sage_const_3712699286 = Integer(3712699286)
_sage_const_0x3f = Integer(0x3f)
_sage_const_0x3e = Integer(0x3e)
_sage_const_0x3d = Integer(0x3d)
_sage_const_0x3c = Integer(0x3c)
_sage_const_0x3b = Integer(0x3b)
_sage_const_0x3a = Integer(0x3a)
_sage_const_1082179648 = Integer(1082179648)
_sage_const_135272456 = Integer(135272456)
_sage_const_3729410708 = Integer(3729410708)
_sage_const_1288555905 = Integer(1288555905)
_sage_const_3552098411 = Integer(3552098411)
_sage_const_1301993293 = Integer(1301993293)
_sage_const_1042358047 = Integer(1042358047)
_sage_const_1843050349 = Integer(1843050349)
_sage_const_2842126286 = Integer(2842126286)
_sage_const_841685273 = Integer(841685273)
_sage_const_4022676207 = Integer(4022676207)
_sage_const_3711886307 = Integer(3711886307)
_sage_const_4082192802 = Integer(4082192802)
_sage_const_946882616 = Integer(946882616)
_sage_const_3477423498 = Integer(3477423498)
_sage_const_1200539975 = Integer(1200539975)
_sage_const_1775286713 = Integer(1775286713)
_sage_const_1437269845 = Integer(1437269845)
_sage_const_1431677695 = Integer(1431677695)
_sage_const_3907570467 = Integer(3907570467)
_sage_const_2403715786 = Integer(2403715786)
_sage_const_328696964 = Integer(328696964)
_sage_const_4076011277 = Integer(4076011277)
_sage_const_3651760345 = Integer(3651760345)
_sage_const_386731290 = Integer(386731290)
_sage_const_975641885 = Integer(975641885)
_sage_const_4242743292 = Integer(4242743292)
_sage_const_3877240574 = Integer(3877240574)
_sage_const_3810524412 = Integer(3810524412)
_sage_const_1649619249 = Integer(1649619249)
_sage_const_3069008731 = Integer(3069008731)
_sage_const_4042324747 = Integer(4042324747)
_sage_const_3077402074 = Integer(3077402074)
_sage_const_572671078 = Integer(572671078)
_sage_const_2349043596 = Integer(2349043596)
_sage_const_3922272489 = Integer(3922272489)
_sage_const_862344499 = Integer(862344499)
_sage_const_3635702892 = Integer(3635702892)
_sage_const_2160083008 = Integer(2160083008)
_sage_const_536673507 = Integer(536673507)
_sage_const_2105408135 = Integer(2105408135)
_sage_const_2256934801 = Integer(2256934801)
_sage_const_2486413204 = Integer(2486413204)
_sage_const_1792327274 = Integer(1792327274)
_sage_const_1750873140 = Integer(1750873140)
_sage_const_4043634165 = Integer(4043634165)
_sage_const_1808847035 = Integer(1808847035)
_sage_const_599760028 = Integer(599760028)
_sage_const_1633796771 = Integer(1633796771)
_sage_const_3110719673 = Integer(3110719673)
_sage_const_2709315037 = Integer(2709315037)
_sage_const_0x0B = Integer(0x0B)
_sage_const_0x0C = Integer(0x0C)
_sage_const_2051489085 = Integer(2051489085)
_sage_const_1273211048 = Integer(1273211048)
_sage_const_0x0F = Integer(0x0F)
_sage_const_0x0D = Integer(0x0D)
_sage_const_3511635870 = Integer(3511635870)
_sage_const_2964356043 = Integer(2964356043)
_sage_const_1713513028 = Integer(1713513028)
_sage_const_1086966153 = Integer(1086966153)
_sage_const_473441308 = Integer(473441308)
_sage_const_100794884 = Integer(100794884)
_sage_const_3745374946 = Integer(3745374946)
_sage_const_4059166984 = Integer(4059166984)
_sage_const_3094074296 = Integer(3094074296)
_sage_const_4144101110 = Integer(4144101110)
_sage_const_0x0b = Integer(0x0b)
_sage_const_0x0c = Integer(0x0c)
_sage_const_0x0a = Integer(0x0a)
_sage_const_0x0f = Integer(0x0f)
_sage_const_0x0d = Integer(0x0d)
_sage_const_0x0e = Integer(0x0e)
_sage_const_2341145990 = Integer(2341145990)
_sage_const_541089824 = Integer(541089824)
_sage_const_1195871945 = Integer(1195871945)
_sage_const_3014884814 = Integer(3014884814)
_sage_const_1238290055 = Integer(1238290055)
_sage_const_3400492389 = Integer(3400492389)
_sage_const_3427026056 = Integer(3427026056)
_sage_const_218962455 = Integer(218962455)
_sage_const_522141217 = Integer(522141217)
_sage_const_0x02 = Integer(0x02)
_sage_const_0x03 = Integer(0x03)
_sage_const_0x00 = Integer(0x00)
_sage_const_0x01 = Integer(0x01)
_sage_const_0x06 = Integer(0x06)
_sage_const_0x07 = Integer(0x07)
_sage_const_0x04 = Integer(0x04)
_sage_const_0x05 = Integer(0x05)
_sage_const_0x08 = Integer(0x08)
_sage_const_0x09 = Integer(0x09)
_sage_const_1386542674 = Integer(1386542674)
_sage_const_1179028682 = Integer(1179028682)
_sage_const_385612781 = Integer(385612781)
_sage_const_1312438900 = Integer(1312438900)
_sage_const_2935576407 = Integer(2935576407)
_sage_const_2373680118 = Integer(2373680118)
_sage_const_3503340395 = Integer(3503340395)
_sage_const_672667696 = Integer(672667696)
_sage_const_2390391540 = Integer(2390391540)
_sage_const_1589437022 = Integer(1589437022)
_sage_const_2572730817 = Integer(2572730817)
_sage_const_3868554099 = Integer(3868554099)
_sage_const_2728550397 = Integer(2728550397)
_sage_const_421081643 = Integer(421081643)
_sage_const_471611428 = Integer(471611428)
_sage_const_4269899647 = Integer(4269899647)
_sage_const_270544912 = Integer(270544912)
_sage_const_4236410494 = Integer(4236410494)

#!/usr/bin/env sage




XorBox = [_sage_const_0x0 ,_sage_const_0x1 ,_sage_const_0x2 ,_sage_const_0x3 ,_sage_const_0x4 ,_sage_const_0x5 ,_sage_const_0x6 ,_sage_const_0x7 ,_sage_const_0x8 ,_sage_const_0x9 ,_sage_const_0xa ,_sage_const_0xb ,_sage_const_0xc ,_sage_const_0xd ,_sage_const_0xe ,_sage_const_0xf ,_sage_const_0x1 ,_sage_const_0x0 ,_sage_const_0x3 ,_sage_const_0x2 ,_sage_const_0x5 ,_sage_const_0x4 ,_sage_const_0x7 ,_sage_const_0x6 ,_sage_const_0x9 ,_sage_const_0x8 ,_sage_const_0xb ,_sage_const_0xa ,_sage_const_0xd ,_sage_const_0xc ,_sage_const_0xf ,_sage_const_0xe ,_sage_const_0x2 ,_sage_const_0x3 ,_sage_const_0x0 ,_sage_const_0x1 ,_sage_const_0x6 ,_sage_const_0x7 ,_sage_const_0x4 ,_sage_const_0x5 ,_sage_const_0xa ,_sage_const_0xb ,_sage_const_0x8 ,_sage_const_0x9 ,_sage_const_0xe ,_sage_const_0xf ,_sage_const_0xc ,_sage_const_0xd ,_sage_const_0x3 ,_sage_const_0x2 ,_sage_const_0x1 ,_sage_const_0x0 ,_sage_const_0x7 ,_sage_const_0x6 ,_sage_const_0x5 ,_sage_const_0x4 ,_sage_const_0xb ,_sage_const_0xa ,_sage_const_0x9 ,_sage_const_0x8 ,_sage_const_0xf ,_sage_const_0xe ,_sage_const_0xd ,_sage_const_0xc ,_sage_const_0x4 ,_sage_const_0x5 ,_sage_const_0x6 ,_sage_const_0x7 ,_sage_const_0x0 ,_sage_const_0x1 ,_sage_const_0x2 ,_sage_const_0x3 ,_sage_const_0xc ,_sage_const_0xd ,_sage_const_0xe ,_sage_const_0xf ,_sage_const_0x8 ,_sage_const_0x9 ,_sage_const_0xa ,_sage_const_0xb ,_sage_const_0x5 ,_sage_const_0x4 ,_sage_const_0x7 ,_sage_const_0x6 ,_sage_const_0x1 ,_sage_const_0x0 ,_sage_const_0x3 ,_sage_const_0x2 ,_sage_const_0xd ,_sage_const_0xc ,_sage_const_0xf ,_sage_const_0xe ,_sage_const_0x9 ,_sage_const_0x8 ,_sage_const_0xb ,_sage_const_0xa ,_sage_const_0x6 ,_sage_const_0x7 ,_sage_const_0x4 ,_sage_const_0x5 ,_sage_const_0x2 ,_sage_const_0x3 ,_sage_const_0x0 ,_sage_const_0x1 ,_sage_const_0xe ,_sage_const_0xf ,_sage_const_0xc ,_sage_const_0xd ,_sage_const_0xa ,_sage_const_0xb ,_sage_const_0x8 ,_sage_const_0x9 ,_sage_const_0x7 ,_sage_const_0x6 ,_sage_const_0x5 ,_sage_const_0x4 ,_sage_const_0x3 ,_sage_const_0x2 ,_sage_const_0x1 ,_sage_const_0x0 ,_sage_const_0xf ,_sage_const_0xe ,_sage_const_0xd ,_sage_const_0xc ,_sage_const_0xb ,_sage_const_0xa ,_sage_const_0x9 ,_sage_const_0x8 ,_sage_const_0x8 ,_sage_const_0x9 ,_sage_const_0xa ,_sage_const_0xb ,_sage_const_0xc ,_sage_const_0xd ,_sage_const_0xe ,_sage_const_0xf ,_sage_const_0x0 ,_sage_const_0x1 ,_sage_const_0x2 ,_sage_const_0x3 ,_sage_const_0x4 ,_sage_const_0x5 ,_sage_const_0x6 ,_sage_const_0x7 ,_sage_const_0x9 ,_sage_const_0x8 ,_sage_const_0xb ,_sage_const_0xa ,_sage_const_0xd ,_sage_const_0xc ,_sage_const_0xf ,_sage_const_0xe ,_sage_const_0x1 ,_sage_const_0x0 ,_sage_const_0x3 ,_sage_const_0x2 ,_sage_const_0x5 ,_sage_const_0x4 ,_sage_const_0x7 ,_sage_const_0x6 ,_sage_const_0xa ,_sage_const_0xb ,_sage_const_0x8 ,_sage_const_0x9 ,_sage_const_0xe ,_sage_const_0xf ,_sage_const_0xc ,_sage_const_0xd ,_sage_const_0x2 ,_sage_const_0x3 ,_sage_const_0x0 ,_sage_const_0x1 ,_sage_const_0x6 ,_sage_const_0x7 ,_sage_const_0x4 ,_sage_const_0x5 ,_sage_const_0xb ,_sage_const_0xa ,_sage_const_0x9 ,_sage_const_0x8 ,_sage_const_0xf ,_sage_const_0xe ,_sage_const_0xd ,_sage_const_0xc ,_sage_const_0x3 ,_sage_const_0x2 ,_sage_const_0x1 ,_sage_const_0x0 ,_sage_const_0x7 ,_sage_const_0x6 ,_sage_const_0x5 ,_sage_const_0x4 ,_sage_const_0xc ,_sage_const_0xd ,_sage_const_0xe ,_sage_const_0xf ,_sage_const_0x8 ,_sage_const_0x9 ,_sage_const_0xa ,_sage_const_0xb ,_sage_const_0x4 ,_sage_const_0x5 ,_sage_const_0x6 ,_sage_const_0x7 ,_sage_const_0x0 ,_sage_const_0x1 ,_sage_const_0x2 ,_sage_const_0x3 ,_sage_const_0xd ,_sage_const_0xc ,_sage_const_0xf ,_sage_const_0xe ,_sage_const_0x9 ,_sage_const_0x8 ,_sage_const_0xb ,_sage_const_0xa ,_sage_const_0x5 ,_sage_const_0x4 ,_sage_const_0x7 ,_sage_const_0x6 ,_sage_const_0x1 ,_sage_const_0x0 ,_sage_const_0x3 ,_sage_const_0x2 ,_sage_const_0xe ,_sage_const_0xf ,_sage_const_0xc ,_sage_const_0xd ,_sage_const_0xa ,_sage_const_0xb ,_sage_const_0x8 ,_sage_const_0x9 ,_sage_const_0x6 ,_sage_const_0x7 ,_sage_const_0x4 ,_sage_const_0x5 ,_sage_const_0x2 ,_sage_const_0x3 ,_sage_const_0x0 ,_sage_const_0x1 ,_sage_const_0xf ,_sage_const_0xe ,_sage_const_0xd ,_sage_const_0xc ,_sage_const_0xb ,_sage_const_0xa ,_sage_const_0x9 ,_sage_const_0x8 ,_sage_const_0x7 ,_sage_const_0x6 ,_sage_const_0x5 ,_sage_const_0x4 ,_sage_const_0x3 ,_sage_const_0x2 ,_sage_const_0x1 ,_sage_const_0x0 ]
Ty = [[_sage_const_0 , _sage_const_50397442 , _sage_const_100794884 , _sage_const_84083462 , _sage_const_201589768 , _sage_const_251987210 , _sage_const_168166924 , _sage_const_151455502 , _sage_const_403179536 , _sage_const_453576978 , _sage_const_503974420 ,
       _sage_const_487262998 , _sage_const_336333848 , _sage_const_386731290 , _sage_const_302911004 , _sage_const_286199582 , _sage_const_806359072 , _sage_const_856756514 , _sage_const_907153956 , _sage_const_890442534 , _sage_const_1007948840 ,
       _sage_const_1058346282 , _sage_const_974525996 , _sage_const_957814574 , _sage_const_672667696 , _sage_const_723065138 , _sage_const_773462580 , _sage_const_756751158 , _sage_const_605822008 , _sage_const_656219450 , _sage_const_572399164 ,
       _sage_const_555687742 , _sage_const_1612718144 , _sage_const_1663115586 , _sage_const_1713513028 , _sage_const_1696801606 , _sage_const_1814307912 , _sage_const_1864705354 , _sage_const_1780885068 , _sage_const_1764173646 ,
       _sage_const_2015897680 , _sage_const_2066295122 , _sage_const_2116692564 , _sage_const_2099981142 , _sage_const_1949051992 , _sage_const_1999449434 , _sage_const_1915629148 , _sage_const_1898917726 , _sage_const_1345335392 ,
       _sage_const_1395732834 , _sage_const_1446130276 , _sage_const_1429418854 , _sage_const_1546925160 , _sage_const_1597322602 , _sage_const_1513502316 , _sage_const_1496790894 , _sage_const_1211644016 , _sage_const_1262041458 ,
       _sage_const_1312438900 , _sage_const_1295727478 , _sage_const_1144798328 , _sage_const_1195195770 , _sage_const_1111375484 , _sage_const_1094664062 , _sage_const_3225436288 , _sage_const_3275833730 , _sage_const_3326231172 ,
       _sage_const_3309519750 , _sage_const_3427026056 , _sage_const_3477423498 , _sage_const_3393603212 , _sage_const_3376891790 , _sage_const_3628615824 , _sage_const_3679013266 , _sage_const_3729410708 , _sage_const_3712699286 ,
       _sage_const_3561770136 , _sage_const_3612167578 , _sage_const_3528347292 , _sage_const_3511635870 , _sage_const_4031795360 , _sage_const_4082192802 , _sage_const_4132590244 , _sage_const_4115878822 , _sage_const_4233385128 ,
       _sage_const_4283782570 , _sage_const_4199962284 , _sage_const_4183250862 , _sage_const_3898103984 , _sage_const_3948501426 , _sage_const_3998898868 , _sage_const_3982187446 , _sage_const_3831258296 , _sage_const_3881655738 ,
       _sage_const_3797835452 , _sage_const_3781124030 , _sage_const_2690670784 , _sage_const_2741068226 , _sage_const_2791465668 , _sage_const_2774754246 , _sage_const_2892260552 , _sage_const_2942657994 , _sage_const_2858837708 ,
       _sage_const_2842126286 , _sage_const_3093850320 , _sage_const_3144247762 , _sage_const_3194645204 , _sage_const_3177933782 , _sage_const_3027004632 , _sage_const_3077402074 , _sage_const_2993581788 , _sage_const_2976870366 ,
       _sage_const_2423288032 , _sage_const_2473685474 , _sage_const_2524082916 , _sage_const_2507371494 , _sage_const_2624877800 , _sage_const_2675275242 , _sage_const_2591454956 , _sage_const_2574743534 , _sage_const_2289596656 ,
       _sage_const_2339994098 , _sage_const_2390391540 , _sage_const_2373680118 , _sage_const_2222750968 , _sage_const_2273148410 , _sage_const_2189328124 , _sage_const_2172616702 , _sage_const_2608889883 , _sage_const_2558624025 ,
       _sage_const_2642575903 , _sage_const_2659418909 , _sage_const_2542044179 , _sage_const_2491778321 , _sage_const_2441512471 , _sage_const_2458355477 , _sage_const_2206763019 , _sage_const_2156497161 , _sage_const_2240449039 ,
       _sage_const_2257292045 , _sage_const_2408352771 , _sage_const_2358086913 , _sage_const_2307821063 , _sage_const_2324664069 , _sage_const_2878378043 , _sage_const_2828112185 , _sage_const_2912064063 , _sage_const_2928907069 ,
       _sage_const_2811532339 , _sage_const_2761266481 , _sage_const_2711000631 , _sage_const_2727843637 , _sage_const_3013122091 , _sage_const_2962856233 , _sage_const_3046808111 , _sage_const_3063651117 , _sage_const_3214711843 ,
       _sage_const_3164445985 , _sage_const_3114180135 , _sage_const_3131023141 , _sage_const_4221608027 , _sage_const_4171342169 , _sage_const_4255294047 , _sage_const_4272137053 , _sage_const_4154762323 , _sage_const_4104496465 ,
       _sage_const_4054230615 , _sage_const_4071073621 , _sage_const_3819481163 , _sage_const_3769215305 , _sage_const_3853167183 , _sage_const_3870010189 , _sage_const_4021070915 , _sage_const_3970805057 , _sage_const_3920539207 ,
       _sage_const_3937382213 , _sage_const_3417354363 , _sage_const_3367088505 , _sage_const_3451040383 , _sage_const_3467883389 , _sage_const_3350508659 , _sage_const_3300242801 , _sage_const_3249976951 , _sage_const_3266819957 ,
       _sage_const_3552098411 , _sage_const_3501832553 , _sage_const_3585784431 , _sage_const_3602627437 , _sage_const_3753688163 , _sage_const_3703422305 , _sage_const_3653156455 , _sage_const_3669999461 , _sage_const_1539358875 ,
       _sage_const_1489093017 , _sage_const_1573044895 , _sage_const_1589887901 , _sage_const_1472513171 , _sage_const_1422247313 , _sage_const_1371981463 , _sage_const_1388824469 , _sage_const_1137232011 , _sage_const_1086966153 ,
       _sage_const_1170918031 , _sage_const_1187761037 , _sage_const_1338821763 , _sage_const_1288555905 , _sage_const_1238290055 , _sage_const_1255133061 , _sage_const_1808847035 , _sage_const_1758581177 , _sage_const_1842533055 ,
       _sage_const_1859376061 , _sage_const_1742001331 , _sage_const_1691735473 , _sage_const_1641469623 , _sage_const_1658312629 , _sage_const_1943591083 , _sage_const_1893325225 , _sage_const_1977277103 , _sage_const_1994120109 ,
       _sage_const_2145180835 , _sage_const_2094914977 , _sage_const_2044649127 , _sage_const_2061492133 , _sage_const_1004593371 , _sage_const_954327513 , _sage_const_1038279391 , _sage_const_1055122397 , _sage_const_937747667 ,
       _sage_const_887481809 , _sage_const_837215959 , _sage_const_854058965 , _sage_const_602466507 , _sage_const_552200649 , _sage_const_636152527 , _sage_const_652995533 , _sage_const_804056259 , _sage_const_753790401 , _sage_const_703524551 ,
       _sage_const_720367557 , _sage_const_200339707 , _sage_const_150073849 , _sage_const_234025727 , _sage_const_250868733 , _sage_const_133494003 , _sage_const_83228145 , _sage_const_32962295 , _sage_const_49805301 , _sage_const_335083755 ,
       _sage_const_284817897 , _sage_const_368769775 , _sage_const_385612781 , _sage_const_536673507 , _sage_const_486407649 , _sage_const_436141799 , _sage_const_452984805 ],
      [_sage_const_0 , _sage_const_16843267 , _sage_const_33686534 , _sage_const_50529797 , _sage_const_67373068 , _sage_const_84216335 , _sage_const_101059594 , _sage_const_117902857 , _sage_const_134746136 , _sage_const_151589403 , _sage_const_168432670 ,
       _sage_const_185275933 , _sage_const_202119188 , _sage_const_218962455 , _sage_const_235805714 , _sage_const_252648977 , _sage_const_269492272 , _sage_const_286335539 , _sage_const_303178806 , _sage_const_320022069 , _sage_const_336865340 ,
       _sage_const_353708607 , _sage_const_370551866 , _sage_const_387395129 , _sage_const_404238376 , _sage_const_421081643 , _sage_const_437924910 , _sage_const_454768173 , _sage_const_471611428 , _sage_const_488454695 , _sage_const_505297954 ,
       _sage_const_522141217 , _sage_const_538984544 , _sage_const_555827811 , _sage_const_572671078 , _sage_const_589514341 , _sage_const_606357612 , _sage_const_623200879 , _sage_const_640044138 , _sage_const_656887401 , _sage_const_673730680 ,
       _sage_const_690573947 , _sage_const_707417214 , _sage_const_724260477 , _sage_const_741103732 , _sage_const_757946999 , _sage_const_774790258 , _sage_const_791633521 , _sage_const_808476752 , _sage_const_825320019 , _sage_const_842163286 ,
       _sage_const_859006549 , _sage_const_875849820 , _sage_const_892693087 , _sage_const_909536346 , _sage_const_926379609 , _sage_const_943222856 , _sage_const_960066123 , _sage_const_976909390 , _sage_const_993752653 , _sage_const_1010595908 ,
       _sage_const_1027439175 , _sage_const_1044282434 , _sage_const_1061125697 , _sage_const_1077969088 , _sage_const_1094812355 , _sage_const_1111655622 , _sage_const_1128498885 , _sage_const_1145342156 , _sage_const_1162185423 ,
       _sage_const_1179028682 , _sage_const_1195871945 , _sage_const_1212715224 , _sage_const_1229558491 , _sage_const_1246401758 , _sage_const_1263245021 , _sage_const_1280088276 , _sage_const_1296931543 , _sage_const_1313774802 ,
       _sage_const_1330618065 , _sage_const_1347461360 , _sage_const_1364304627 , _sage_const_1381147894 , _sage_const_1397991157 , _sage_const_1414834428 , _sage_const_1431677695 , _sage_const_1448520954 , _sage_const_1465364217 ,
       _sage_const_1482207464 , _sage_const_1499050731 , _sage_const_1515893998 , _sage_const_1532737261 , _sage_const_1549580516 , _sage_const_1566423783 , _sage_const_1583267042 , _sage_const_1600110305 , _sage_const_1616953504 ,
       _sage_const_1633796771 , _sage_const_1650640038 , _sage_const_1667483301 , _sage_const_1684326572 , _sage_const_1701169839 , _sage_const_1718013098 , _sage_const_1734856361 , _sage_const_1751699640 , _sage_const_1768542907 ,
       _sage_const_1785386174 , _sage_const_1802229437 , _sage_const_1819072692 , _sage_const_1835915959 , _sage_const_1852759218 , _sage_const_1869602481 , _sage_const_1886445712 , _sage_const_1903288979 , _sage_const_1920132246 ,
       _sage_const_1936975509 , _sage_const_1953818780 , _sage_const_1970662047 , _sage_const_1987505306 , _sage_const_2004348569 , _sage_const_2021191816 , _sage_const_2038035083 , _sage_const_2054878350 , _sage_const_2071721613 ,
       _sage_const_2088564868 , _sage_const_2105408135 , _sage_const_2122251394 , _sage_const_2139094657 , _sage_const_2155879323 , _sage_const_2172721560 , _sage_const_2189565853 , _sage_const_2206408094 , _sage_const_2223248279 ,
       _sage_const_2240090516 , _sage_const_2256934801 , _sage_const_2273777042 , _sage_const_2290617219 , _sage_const_2307459456 , _sage_const_2324303749 , _sage_const_2341145990 , _sage_const_2357986191 , _sage_const_2374828428 ,
       _sage_const_2391672713 , _sage_const_2408514954 , _sage_const_2425371563 , _sage_const_2442213800 , _sage_const_2459058093 , _sage_const_2475900334 , _sage_const_2492740519 , _sage_const_2509582756 , _sage_const_2526427041 ,
       _sage_const_2543269282 , _sage_const_2560109491 , _sage_const_2576951728 , _sage_const_2593796021 , _sage_const_2610638262 , _sage_const_2627478463 , _sage_const_2644320700 , _sage_const_2661164985 , _sage_const_2678007226 ,
       _sage_const_2694863867 , _sage_const_2711706104 , _sage_const_2728550397 , _sage_const_2745392638 , _sage_const_2762232823 , _sage_const_2779075060 , _sage_const_2795919345 , _sage_const_2812761586 , _sage_const_2829601763 ,
       _sage_const_2846444000 , _sage_const_2863288293 , _sage_const_2880130534 , _sage_const_2896970735 , _sage_const_2913812972 , _sage_const_2930657257 , _sage_const_2947499498 , _sage_const_2964356043 , _sage_const_2981198280 ,
       _sage_const_2998042573 , _sage_const_3014884814 , _sage_const_3031724999 , _sage_const_3048567236 , _sage_const_3065411521 , _sage_const_3082253762 , _sage_const_3099093971 , _sage_const_3115936208 , _sage_const_3132780501 ,
       _sage_const_3149622742 , _sage_const_3166462943 , _sage_const_3183305180 , _sage_const_3200149465 , _sage_const_3216991706 , _sage_const_3233848155 , _sage_const_3250690392 , _sage_const_3267534685 , _sage_const_3284376926 ,
       _sage_const_3301217111 , _sage_const_3318059348 , _sage_const_3334903633 , _sage_const_3351745874 , _sage_const_3368586051 , _sage_const_3385428288 , _sage_const_3402272581 , _sage_const_3419114822 , _sage_const_3435955023 ,
       _sage_const_3452797260 , _sage_const_3469641545 , _sage_const_3486483786 , _sage_const_3503340395 , _sage_const_3520182632 , _sage_const_3537026925 , _sage_const_3553869166 , _sage_const_3570709351 , _sage_const_3587551588 ,
       _sage_const_3604395873 , _sage_const_3621238114 , _sage_const_3638078323 , _sage_const_3654920560 , _sage_const_3671764853 , _sage_const_3688607094 , _sage_const_3705447295 , _sage_const_3722289532 , _sage_const_3739133817 ,
       _sage_const_3755976058 , _sage_const_3772832571 , _sage_const_3789674808 , _sage_const_3806519101 , _sage_const_3823361342 , _sage_const_3840201527 , _sage_const_3857043764 , _sage_const_3873888049 , _sage_const_3890730290 ,
       _sage_const_3907570467 , _sage_const_3924412704 , _sage_const_3941256997 , _sage_const_3958099238 , _sage_const_3974939439 , _sage_const_3991781676 , _sage_const_4008625961 , _sage_const_4025468202 , _sage_const_4042324747 ,
       _sage_const_4059166984 , _sage_const_4076011277 , _sage_const_4092853518 , _sage_const_4109693703 , _sage_const_4126535940 , _sage_const_4143380225 , _sage_const_4160222466 , _sage_const_4177062675 , _sage_const_4193904912 ,
       _sage_const_4210749205 , _sage_const_4227591446 , _sage_const_4244431647 , _sage_const_4261273884 , _sage_const_4278118169 , _sage_const_4294960410 ],
      [_sage_const_0 , _sage_const_16909057 , _sage_const_33818114 , _sage_const_50726147 , _sage_const_67636228 , _sage_const_84545285 , _sage_const_101452294 , _sage_const_118360327 , _sage_const_135272456 , _sage_const_152181513 , _sage_const_169090570 ,
       _sage_const_185998603 , _sage_const_202904588 , _sage_const_219813645 , _sage_const_236720654 , _sage_const_253628687 , _sage_const_270544912 , _sage_const_287453969 , _sage_const_304363026 , _sage_const_321271059 , _sage_const_338181140 ,
       _sage_const_355090197 , _sage_const_371997206 , _sage_const_388905239 , _sage_const_405809176 , _sage_const_422718233 , _sage_const_439627290 , _sage_const_456535323 , _sage_const_473441308 , _sage_const_490350365 , _sage_const_507257374 ,
       _sage_const_524165407 , _sage_const_541089824 , _sage_const_557998881 , _sage_const_574907938 , _sage_const_591815971 , _sage_const_608726052 , _sage_const_625635109 , _sage_const_642542118 , _sage_const_659450151 , _sage_const_676362280 ,
       _sage_const_693271337 , _sage_const_710180394 , _sage_const_727088427 , _sage_const_743994412 , _sage_const_760903469 , _sage_const_777810478 , _sage_const_794718511 , _sage_const_811618352 , _sage_const_828527409 , _sage_const_845436466 ,
       _sage_const_862344499 , _sage_const_879254580 , _sage_const_896163637 , _sage_const_913070646 , _sage_const_929978679 , _sage_const_946882616 , _sage_const_963791673 , _sage_const_980700730 , _sage_const_997608763 , _sage_const_1014514748 ,
       _sage_const_1031423805 , _sage_const_1048330814 , _sage_const_1065238847 , _sage_const_1082179648 , _sage_const_1099088705 , _sage_const_1115997762 , _sage_const_1132905795 , _sage_const_1149815876 , _sage_const_1166724933 ,
       _sage_const_1183631942 , _sage_const_1200539975 , _sage_const_1217452104 , _sage_const_1234361161 , _sage_const_1251270218 , _sage_const_1268178251 , _sage_const_1285084236 , _sage_const_1301993293 , _sage_const_1318900302 ,
       _sage_const_1335808335 , _sage_const_1352724560 , _sage_const_1369633617 , _sage_const_1386542674 , _sage_const_1403450707 , _sage_const_1420360788 , _sage_const_1437269845 , _sage_const_1454176854 , _sage_const_1471084887 ,
       _sage_const_1487988824 , _sage_const_1504897881 , _sage_const_1521806938 , _sage_const_1538714971 , _sage_const_1555620956 , _sage_const_1572530013 , _sage_const_1589437022 , _sage_const_1606345055 , _sage_const_1623236704 ,
       _sage_const_1640145761 , _sage_const_1657054818 , _sage_const_1673962851 , _sage_const_1690872932 , _sage_const_1707781989 , _sage_const_1724688998 , _sage_const_1741597031 , _sage_const_1758509160 , _sage_const_1775418217 ,
       _sage_const_1792327274 , _sage_const_1809235307 , _sage_const_1826141292 , _sage_const_1843050349 , _sage_const_1859957358 , _sage_const_1876865391 , _sage_const_1893765232 , _sage_const_1910674289 , _sage_const_1927583346 ,
       _sage_const_1944491379 , _sage_const_1961401460 , _sage_const_1978310517 , _sage_const_1995217526 , _sage_const_2012125559 , _sage_const_2029029496 , _sage_const_2045938553 , _sage_const_2062847610 , _sage_const_2079755643 ,
       _sage_const_2096661628 , _sage_const_2113570685 , _sage_const_2130477694 , _sage_const_2147385727 , _sage_const_2149292928 , _sage_const_2165938305 , _sage_const_2183110018 , _sage_const_2199756419 , _sage_const_2215876484 ,
       _sage_const_2232521861 , _sage_const_2249691526 , _sage_const_2266337927 , _sage_const_2282455944 , _sage_const_2299101321 , _sage_const_2316273034 , _sage_const_2332919435 , _sage_const_2349043596 , _sage_const_2365688973 ,
       _sage_const_2382858638 , _sage_const_2399505039 , _sage_const_2419829648 , _sage_const_2436475025 , _sage_const_2453646738 , _sage_const_2470293139 , _sage_const_2486413204 , _sage_const_2503058581 , _sage_const_2520228246 ,
       _sage_const_2536874647 , _sage_const_2553000856 , _sage_const_2569646233 , _sage_const_2586817946 , _sage_const_2603464347 , _sage_const_2619588508 , _sage_const_2636233885 , _sage_const_2653403550 , _sage_const_2670049951 ,
       _sage_const_2690382752 , _sage_const_2707028129 , _sage_const_2724199842 , _sage_const_2740846243 , _sage_const_2756966308 , _sage_const_2773611685 , _sage_const_2790781350 , _sage_const_2807427751 , _sage_const_2823545768 ,
       _sage_const_2840191145 , _sage_const_2857362858 , _sage_const_2874009259 , _sage_const_2890133420 , _sage_const_2906778797 , _sage_const_2923948462 , _sage_const_2940594863 , _sage_const_2960903088 , _sage_const_2977548465 ,
       _sage_const_2994720178 , _sage_const_3011366579 , _sage_const_3027486644 , _sage_const_3044132021 , _sage_const_3061301686 , _sage_const_3077948087 , _sage_const_3094074296 , _sage_const_3110719673 , _sage_const_3127891386 ,
       _sage_const_3144537787 , _sage_const_3160661948 , _sage_const_3177307325 , _sage_const_3194476990 , _sage_const_3211123391 , _sage_const_3231407040 , _sage_const_3248052417 , _sage_const_3265224130 , _sage_const_3281870531 ,
       _sage_const_3297990596 , _sage_const_3314635973 , _sage_const_3331805638 , _sage_const_3348452039 , _sage_const_3364570056 , _sage_const_3381215433 , _sage_const_3398387146 , _sage_const_3415033547 , _sage_const_3431157708 ,
       _sage_const_3447803085 , _sage_const_3464972750 , _sage_const_3481619151 , _sage_const_3501943760 , _sage_const_3518589137 , _sage_const_3535760850 , _sage_const_3552407251 , _sage_const_3568527316 , _sage_const_3585172693 ,
       _sage_const_3602342358 , _sage_const_3618988759 , _sage_const_3635114968 , _sage_const_3651760345 , _sage_const_3668932058 , _sage_const_3685578459 , _sage_const_3701702620 , _sage_const_3718347997 , _sage_const_3735517662 ,
       _sage_const_3752164063 , _sage_const_3772464096 , _sage_const_3789109473 , _sage_const_3806281186 , _sage_const_3822927587 , _sage_const_3839047652 , _sage_const_3855693029 , _sage_const_3872862694 , _sage_const_3889509095 ,
       _sage_const_3905627112 , _sage_const_3922272489 , _sage_const_3939444202 , _sage_const_3956090603 , _sage_const_3972214764 , _sage_const_3988860141 , _sage_const_4006029806 , _sage_const_4022676207 , _sage_const_4042984432 ,
       _sage_const_4059629809 , _sage_const_4076801522 , _sage_const_4093447923 , _sage_const_4109567988 , _sage_const_4126213365 , _sage_const_4143383030 , _sage_const_4160029431 , _sage_const_4176155640 , _sage_const_4192801017 ,
       _sage_const_4209972730 , _sage_const_4226619131 , _sage_const_4242743292 , _sage_const_4259388669 , _sage_const_4276558334 , _sage_const_4293204735 ],
      [_sage_const_0 , _sage_const_33751297 , _sage_const_67502594 , _sage_const_100991747 , _sage_const_135005188 , _sage_const_168756485 , _sage_const_201983494 , _sage_const_235472647 , _sage_const_270010376 , _sage_const_303761673 , _sage_const_337512970 ,
       _sage_const_371002123 , _sage_const_403966988 , _sage_const_437718285 , _sage_const_470945294 , _sage_const_504434447 , _sage_const_540020752 , _sage_const_573772049 , _sage_const_607523346 , _sage_const_641012499 , _sage_const_675025940 ,
       _sage_const_708777237 , _sage_const_742004246 , _sage_const_775493399 , _sage_const_807933976 , _sage_const_841685273 , _sage_const_875436570 , _sage_const_908925723 , _sage_const_941890588 , _sage_const_975641885 , _sage_const_1008868894 ,
       _sage_const_1042358047 , _sage_const_1080041504 , _sage_const_1113792801 , _sage_const_1147544098 , _sage_const_1181033251 , _sage_const_1215046692 , _sage_const_1248797989 , _sage_const_1282024998 , _sage_const_1315514151 ,
       _sage_const_1350051880 , _sage_const_1383803177 , _sage_const_1417554474 , _sage_const_1451043627 , _sage_const_1484008492 , _sage_const_1517759789 , _sage_const_1550986798 , _sage_const_1584475951 , _sage_const_1615867952 ,
       _sage_const_1649619249 , _sage_const_1683370546 , _sage_const_1716859699 , _sage_const_1750873140 , _sage_const_1784624437 , _sage_const_1817851446 , _sage_const_1851340599 , _sage_const_1883781176 , _sage_const_1917532473 ,
       _sage_const_1951283770 , _sage_const_1984772923 , _sage_const_2017737788 , _sage_const_2051489085 , _sage_const_2084716094 , _sage_const_2118205247 , _sage_const_2160083008 , _sage_const_2193834305 , _sage_const_2227585602 ,
       _sage_const_2261074755 , _sage_const_2295088196 , _sage_const_2328839493 , _sage_const_2362066502 , _sage_const_2395555655 , _sage_const_2430093384 , _sage_const_2463844681 , _sage_const_2497595978 , _sage_const_2531085131 ,
       _sage_const_2564049996 , _sage_const_2597801293 , _sage_const_2631028302 , _sage_const_2664517455 , _sage_const_2700103760 , _sage_const_2733855057 , _sage_const_2767606354 , _sage_const_2801095507 , _sage_const_2835108948 ,
       _sage_const_2868860245 , _sage_const_2902087254 , _sage_const_2935576407 , _sage_const_2968016984 , _sage_const_3001768281 , _sage_const_3035519578 , _sage_const_3069008731 , _sage_const_3101973596 , _sage_const_3135724893 ,
       _sage_const_3168951902 , _sage_const_3202441055 , _sage_const_3231735904 , _sage_const_3265487201 , _sage_const_3299238498 , _sage_const_3332727651 , _sage_const_3366741092 , _sage_const_3400492389 , _sage_const_3433719398 ,
       _sage_const_3467208551 , _sage_const_3501746280 , _sage_const_3535497577 , _sage_const_3569248874 , _sage_const_3602738027 , _sage_const_3635702892 , _sage_const_3669454189 , _sage_const_3702681198 , _sage_const_3736170351 ,
       _sage_const_3767562352 , _sage_const_3801313649 , _sage_const_3835064946 , _sage_const_3868554099 , _sage_const_3902567540 , _sage_const_3936318837 , _sage_const_3969545846 , _sage_const_4003034999 , _sage_const_4035475576 ,
       _sage_const_4069226873 , _sage_const_4102978170 , _sage_const_4136467323 , _sage_const_4169432188 , _sage_const_4203183485 , _sage_const_4236410494 , _sage_const_4269899647 , _sage_const_463175808 , _sage_const_429425025 ,
       _sage_const_530416258 , _sage_const_496927619 , _sage_const_328696964 , _sage_const_294946181 , _sage_const_395413126 , _sage_const_361924487 , _sage_const_193169544 , _sage_const_159418761 , _sage_const_260409994 , _sage_const_226921355 ,
       _sage_const_59739276 , _sage_const_25988493 , _sage_const_126455438 , _sage_const_92966799 , _sage_const_1001099408 , _sage_const_967348625 , _sage_const_1068339858 , _sage_const_1034851219 , _sage_const_866620564 , _sage_const_832869781 ,
       _sage_const_933336726 , _sage_const_899848087 , _sage_const_733190296 , _sage_const_699439513 , _sage_const_800430746 , _sage_const_766942107 , _sage_const_599760028 , _sage_const_566009245 , _sage_const_666476190 , _sage_const_632987551 ,
       _sage_const_1543217312 , _sage_const_1509466529 , _sage_const_1610457762 , _sage_const_1576969123 , _sage_const_1408738468 , _sage_const_1374987685 , _sage_const_1475454630 , _sage_const_1441965991 , _sage_const_1273211048 ,
       _sage_const_1239460265 , _sage_const_1340451498 , _sage_const_1306962859 , _sage_const_1139780780 , _sage_const_1106029997 , _sage_const_1206496942 , _sage_const_1173008303 , _sage_const_2076946608 , _sage_const_2043195825 ,
       _sage_const_2144187058 , _sage_const_2110698419 , _sage_const_1942467764 , _sage_const_1908716981 , _sage_const_2009183926 , _sage_const_1975695287 , _sage_const_1809037496 , _sage_const_1775286713 , _sage_const_1876277946 ,
       _sage_const_1842789307 , _sage_const_1675607228 , _sage_const_1641856445 , _sage_const_1742323390 , _sage_const_1708834751 , _sage_const_2606481600 , _sage_const_2572730817 , _sage_const_2673722050 , _sage_const_2640233411 ,
       _sage_const_2472002756 , _sage_const_2438251973 , _sage_const_2538718918 , _sage_const_2505230279 , _sage_const_2336475336 , _sage_const_2302724553 , _sage_const_2403715786 , _sage_const_2370227147 , _sage_const_2203045068 ,
       _sage_const_2169294285 , _sage_const_2269761230 , _sage_const_2236272591 , _sage_const_3144405200 , _sage_const_3110654417 , _sage_const_3211645650 , _sage_const_3178157011 , _sage_const_3009926356 , _sage_const_2976175573 ,
       _sage_const_3076642518 , _sage_const_3043153879 , _sage_const_2876496088 , _sage_const_2842745305 , _sage_const_2943736538 , _sage_const_2910247899 , _sage_const_2743065820 , _sage_const_2709315037 , _sage_const_2809781982 ,
       _sage_const_2776293343 , _sage_const_3678134496 , _sage_const_3644383713 , _sage_const_3745374946 , _sage_const_3711886307 , _sage_const_3543655652 , _sage_const_3509904869 , _sage_const_3610371814 , _sage_const_3576883175 ,
       _sage_const_3408128232 , _sage_const_3374377449 , _sage_const_3475368682 , _sage_const_3441880043 , _sage_const_3274697964 , _sage_const_3240947181 , _sage_const_3341414126 , _sage_const_3307925487 , _sage_const_4211863792 ,
       _sage_const_4178113009 , _sage_const_4279104242 , _sage_const_4245615603 , _sage_const_4077384948 , _sage_const_4043634165 , _sage_const_4144101110 , _sage_const_4110612471 , _sage_const_3943954680 , _sage_const_3910203897 ,
       _sage_const_4011195130 , _sage_const_3977706491 , _sage_const_3810524412 , _sage_const_3776773629 , _sage_const_3877240574 , _sage_const_3843751935 ]]

mulby = {}
mulby[_sage_const_1 ] = [x for x in xrange(_sage_const_256 )]
mulby[_sage_const_2 ] = [_sage_const_0x00 , _sage_const_0x02 , _sage_const_0x04 , _sage_const_0x06 , _sage_const_0x08 , _sage_const_0x0a , _sage_const_0x0c , _sage_const_0x0e , _sage_const_0x10 , _sage_const_0x12 , _sage_const_0x14 , _sage_const_0x16 , _sage_const_0x18 , _sage_const_0x1a , _sage_const_0x1c , _sage_const_0x1e , _sage_const_0x20 , _sage_const_0x22 ,
            _sage_const_0x24 , _sage_const_0x26 , _sage_const_0x28 , _sage_const_0x2a , _sage_const_0x2c , _sage_const_0x2e , _sage_const_0x30 , _sage_const_0x32 , _sage_const_0x34 , _sage_const_0x36 , _sage_const_0x38 , _sage_const_0x3a , _sage_const_0x3c , _sage_const_0x3e , _sage_const_0x40 , _sage_const_0x42 , _sage_const_0x44 , _sage_const_0x46 ,
            _sage_const_0x48 , _sage_const_0x4a , _sage_const_0x4c , _sage_const_0x4e , _sage_const_0x50 , _sage_const_0x52 , _sage_const_0x54 , _sage_const_0x56 , _sage_const_0x58 , _sage_const_0x5a , _sage_const_0x5c , _sage_const_0x5e , _sage_const_0x60 , _sage_const_0x62 , _sage_const_0x64 , _sage_const_0x66 , _sage_const_0x68 , _sage_const_0x6a ,
            _sage_const_0x6c , _sage_const_0x6e , _sage_const_0x70 , _sage_const_0x72 , _sage_const_0x74 , _sage_const_0x76 , _sage_const_0x78 , _sage_const_0x7a , _sage_const_0x7c , _sage_const_0x7e , _sage_const_0x80 , _sage_const_0x82 , _sage_const_0x84 , _sage_const_0x86 , _sage_const_0x88 , _sage_const_0x8a , _sage_const_0x8c , _sage_const_0x8e ,
            _sage_const_0x90 , _sage_const_0x92 , _sage_const_0x94 , _sage_const_0x96 , _sage_const_0x98 , _sage_const_0x9a , _sage_const_0x9c , _sage_const_0x9e , _sage_const_0xa0 , _sage_const_0xa2 , _sage_const_0xa4 , _sage_const_0xa6 , _sage_const_0xa8 , _sage_const_0xaa , _sage_const_0xac , _sage_const_0xae , _sage_const_0xb0 , _sage_const_0xb2 ,
            _sage_const_0xb4 , _sage_const_0xb6 , _sage_const_0xb8 , _sage_const_0xba , _sage_const_0xbc , _sage_const_0xbe , _sage_const_0xc0 , _sage_const_0xc2 , _sage_const_0xc4 , _sage_const_0xc6 , _sage_const_0xc8 , _sage_const_0xca , _sage_const_0xcc , _sage_const_0xce , _sage_const_0xd0 , _sage_const_0xd2 , _sage_const_0xd4 , _sage_const_0xd6 ,
            _sage_const_0xd8 , _sage_const_0xda , _sage_const_0xdc , _sage_const_0xde , _sage_const_0xe0 , _sage_const_0xe2 , _sage_const_0xe4 , _sage_const_0xe6 , _sage_const_0xe8 , _sage_const_0xea , _sage_const_0xec , _sage_const_0xee , _sage_const_0xf0 , _sage_const_0xf2 , _sage_const_0xf4 , _sage_const_0xf6 , _sage_const_0xf8 , _sage_const_0xfa ,
            _sage_const_0xfc , _sage_const_0xfe , _sage_const_0x1b , _sage_const_0x19 , _sage_const_0x1f , _sage_const_0x1d , _sage_const_0x13 , _sage_const_0x11 , _sage_const_0x17 , _sage_const_0x15 , _sage_const_0x0b , _sage_const_0x09 , _sage_const_0x0f , _sage_const_0x0d , _sage_const_0x03 , _sage_const_0x01 , _sage_const_0x07 , _sage_const_0x05 ,
            _sage_const_0x3b , _sage_const_0x39 , _sage_const_0x3f , _sage_const_0x3d , _sage_const_0x33 , _sage_const_0x31 , _sage_const_0x37 , _sage_const_0x35 , _sage_const_0x2b , _sage_const_0x29 , _sage_const_0x2f , _sage_const_0x2d , _sage_const_0x23 , _sage_const_0x21 , _sage_const_0x27 , _sage_const_0x25 , _sage_const_0x5b , _sage_const_0x59 ,
            _sage_const_0x5f , _sage_const_0x5d , _sage_const_0x53 , _sage_const_0x51 , _sage_const_0x57 , _sage_const_0x55 , _sage_const_0x4b , _sage_const_0x49 , _sage_const_0x4f , _sage_const_0x4d , _sage_const_0x43 , _sage_const_0x41 , _sage_const_0x47 , _sage_const_0x45 , _sage_const_0x7b , _sage_const_0x79 , _sage_const_0x7f , _sage_const_0x7d ,
            _sage_const_0x73 , _sage_const_0x71 , _sage_const_0x77 , _sage_const_0x75 , _sage_const_0x6b , _sage_const_0x69 , _sage_const_0x6f , _sage_const_0x6d , _sage_const_0x63 , _sage_const_0x61 , _sage_const_0x67 , _sage_const_0x65 , _sage_const_0x9b , _sage_const_0x99 , _sage_const_0x9f , _sage_const_0x9d , _sage_const_0x93 , _sage_const_0x91 ,
            _sage_const_0x97 , _sage_const_0x95 , _sage_const_0x8b , _sage_const_0x89 , _sage_const_0x8f , _sage_const_0x8d , _sage_const_0x83 , _sage_const_0x81 , _sage_const_0x87 , _sage_const_0x85 , _sage_const_0xbb , _sage_const_0xb9 , _sage_const_0xbf , _sage_const_0xbd , _sage_const_0xb3 , _sage_const_0xb1 , _sage_const_0xb7 , _sage_const_0xb5 ,
            _sage_const_0xab , _sage_const_0xa9 , _sage_const_0xaf , _sage_const_0xad , _sage_const_0xa3 , _sage_const_0xa1 , _sage_const_0xa7 , _sage_const_0xa5 , _sage_const_0xdb , _sage_const_0xd9 , _sage_const_0xdf , _sage_const_0xdd , _sage_const_0xd3 , _sage_const_0xd1 , _sage_const_0xd7 , _sage_const_0xd5 , _sage_const_0xcb , _sage_const_0xc9 ,
            _sage_const_0xcf , _sage_const_0xcd , _sage_const_0xc3 , _sage_const_0xc1 , _sage_const_0xc7 , _sage_const_0xc5 , _sage_const_0xfb , _sage_const_0xf9 , _sage_const_0xff , _sage_const_0xfd , _sage_const_0xf3 , _sage_const_0xf1 , _sage_const_0xf7 , _sage_const_0xf5 , _sage_const_0xeb , _sage_const_0xe9 , _sage_const_0xef , _sage_const_0xed ,
            _sage_const_0xe3 , _sage_const_0xe1 , _sage_const_0xe7 , _sage_const_0xe5 ]
mulby[_sage_const_3 ] = [_sage_const_0x00 , _sage_const_0x03 , _sage_const_0x06 , _sage_const_0x05 , _sage_const_0x0c , _sage_const_0x0f , _sage_const_0x0a , _sage_const_0x09 , _sage_const_0x18 , _sage_const_0x1b , _sage_const_0x1e , _sage_const_0x1d , _sage_const_0x14 , _sage_const_0x17 , _sage_const_0x12 , _sage_const_0x11 , _sage_const_0x30 , _sage_const_0x33 ,
            _sage_const_0x36 , _sage_const_0x35 , _sage_const_0x3c , _sage_const_0x3f , _sage_const_0x3a , _sage_const_0x39 , _sage_const_0x28 , _sage_const_0x2b , _sage_const_0x2e , _sage_const_0x2d , _sage_const_0x24 , _sage_const_0x27 , _sage_const_0x22 , _sage_const_0x21 , _sage_const_0x60 , _sage_const_0x63 , _sage_const_0x66 , _sage_const_0x65 ,
            _sage_const_0x6c , _sage_const_0x6f , _sage_const_0x6a , _sage_const_0x69 , _sage_const_0x78 , _sage_const_0x7b , _sage_const_0x7e , _sage_const_0x7d , _sage_const_0x74 , _sage_const_0x77 , _sage_const_0x72 , _sage_const_0x71 , _sage_const_0x50 , _sage_const_0x53 , _sage_const_0x56 , _sage_const_0x55 , _sage_const_0x5c , _sage_const_0x5f ,
            _sage_const_0x5a , _sage_const_0x59 , _sage_const_0x48 , _sage_const_0x4b , _sage_const_0x4e , _sage_const_0x4d , _sage_const_0x44 , _sage_const_0x47 , _sage_const_0x42 , _sage_const_0x41 , _sage_const_0xc0 , _sage_const_0xc3 , _sage_const_0xc6 , _sage_const_0xc5 , _sage_const_0xcc , _sage_const_0xcf , _sage_const_0xca , _sage_const_0xc9 ,
            _sage_const_0xd8 , _sage_const_0xdb , _sage_const_0xde , _sage_const_0xdd , _sage_const_0xd4 , _sage_const_0xd7 , _sage_const_0xd2 , _sage_const_0xd1 , _sage_const_0xf0 , _sage_const_0xf3 , _sage_const_0xf6 , _sage_const_0xf5 , _sage_const_0xfc , _sage_const_0xff , _sage_const_0xfa , _sage_const_0xf9 , _sage_const_0xe8 , _sage_const_0xeb ,
            _sage_const_0xee , _sage_const_0xed , _sage_const_0xe4 , _sage_const_0xe7 , _sage_const_0xe2 , _sage_const_0xe1 , _sage_const_0xa0 , _sage_const_0xa3 , _sage_const_0xa6 , _sage_const_0xa5 , _sage_const_0xac , _sage_const_0xaf , _sage_const_0xaa , _sage_const_0xa9 , _sage_const_0xb8 , _sage_const_0xbb , _sage_const_0xbe , _sage_const_0xbd ,
            _sage_const_0xb4 , _sage_const_0xb7 , _sage_const_0xb2 , _sage_const_0xb1 , _sage_const_0x90 , _sage_const_0x93 , _sage_const_0x96 , _sage_const_0x95 , _sage_const_0x9c , _sage_const_0x9f , _sage_const_0x9a , _sage_const_0x99 , _sage_const_0x88 , _sage_const_0x8b , _sage_const_0x8e , _sage_const_0x8d , _sage_const_0x84 , _sage_const_0x87 ,
            _sage_const_0x82 , _sage_const_0x81 , _sage_const_0x9b , _sage_const_0x98 , _sage_const_0x9d , _sage_const_0x9e , _sage_const_0x97 , _sage_const_0x94 , _sage_const_0x91 , _sage_const_0x92 , _sage_const_0x83 , _sage_const_0x80 , _sage_const_0x85 , _sage_const_0x86 , _sage_const_0x8f , _sage_const_0x8c , _sage_const_0x89 , _sage_const_0x8a ,
            _sage_const_0xab , _sage_const_0xa8 , _sage_const_0xad , _sage_const_0xae , _sage_const_0xa7 , _sage_const_0xa4 , _sage_const_0xa1 , _sage_const_0xa2 , _sage_const_0xb3 , _sage_const_0xb0 , _sage_const_0xb5 , _sage_const_0xb6 , _sage_const_0xbf , _sage_const_0xbc , _sage_const_0xb9 , _sage_const_0xba , _sage_const_0xfb , _sage_const_0xf8 ,
            _sage_const_0xfd , _sage_const_0xfe , _sage_const_0xf7 , _sage_const_0xf4 , _sage_const_0xf1 , _sage_const_0xf2 , _sage_const_0xe3 , _sage_const_0xe0 , _sage_const_0xe5 , _sage_const_0xe6 , _sage_const_0xef , _sage_const_0xec , _sage_const_0xe9 , _sage_const_0xea , _sage_const_0xcb , _sage_const_0xc8 , _sage_const_0xcd , _sage_const_0xce ,
            _sage_const_0xc7 , _sage_const_0xc4 , _sage_const_0xc1 , _sage_const_0xc2 , _sage_const_0xd3 , _sage_const_0xd0 , _sage_const_0xd5 , _sage_const_0xd6 , _sage_const_0xdf , _sage_const_0xdc , _sage_const_0xd9 , _sage_const_0xda , _sage_const_0x5b , _sage_const_0x58 , _sage_const_0x5d , _sage_const_0x5e , _sage_const_0x57 , _sage_const_0x54 ,
            _sage_const_0x51 , _sage_const_0x52 , _sage_const_0x43 , _sage_const_0x40 , _sage_const_0x45 , _sage_const_0x46 , _sage_const_0x4f , _sage_const_0x4c , _sage_const_0x49 , _sage_const_0x4a , _sage_const_0x6b , _sage_const_0x68 , _sage_const_0x6d , _sage_const_0x6e , _sage_const_0x67 , _sage_const_0x64 , _sage_const_0x61 , _sage_const_0x62 ,
            _sage_const_0x73 , _sage_const_0x70 , _sage_const_0x75 , _sage_const_0x76 , _sage_const_0x7f , _sage_const_0x7c , _sage_const_0x79 , _sage_const_0x7a , _sage_const_0x3b , _sage_const_0x38 , _sage_const_0x3d , _sage_const_0x3e , _sage_const_0x37 , _sage_const_0x34 , _sage_const_0x31 , _sage_const_0x32 , _sage_const_0x23 , _sage_const_0x20 ,
            _sage_const_0x25 , _sage_const_0x26 , _sage_const_0x2f , _sage_const_0x2c , _sage_const_0x29 , _sage_const_0x2a , _sage_const_0x0b , _sage_const_0x08 , _sage_const_0x0d , _sage_const_0x0e , _sage_const_0x07 , _sage_const_0x04 , _sage_const_0x01 , _sage_const_0x02 , _sage_const_0x13 , _sage_const_0x10 , _sage_const_0x15 , _sage_const_0x16 ,
            _sage_const_0x1f , _sage_const_0x1c , _sage_const_0x19 , _sage_const_0x1a ]
mulby[_sage_const_9 ] = [_sage_const_0x00 , _sage_const_0x09 , _sage_const_0x12 , _sage_const_0x1b , _sage_const_0x24 , _sage_const_0x2d , _sage_const_0x36 , _sage_const_0x3f , _sage_const_0x48 , _sage_const_0x41 , _sage_const_0x5a , _sage_const_0x53 , _sage_const_0x6c , _sage_const_0x65 , _sage_const_0x7e , _sage_const_0x77 , _sage_const_0x90 , _sage_const_0x99 ,
            _sage_const_0x82 , _sage_const_0x8b , _sage_const_0xb4 , _sage_const_0xbd , _sage_const_0xa6 , _sage_const_0xaf , _sage_const_0xd8 , _sage_const_0xd1 , _sage_const_0xca , _sage_const_0xc3 , _sage_const_0xfc , _sage_const_0xf5 , _sage_const_0xee , _sage_const_0xe7 , _sage_const_0x3b , _sage_const_0x32 , _sage_const_0x29 , _sage_const_0x20 ,
            _sage_const_0x1f , _sage_const_0x16 , _sage_const_0x0d , _sage_const_0x04 , _sage_const_0x73 , _sage_const_0x7a , _sage_const_0x61 , _sage_const_0x68 , _sage_const_0x57 , _sage_const_0x5e , _sage_const_0x45 , _sage_const_0x4c , _sage_const_0xab , _sage_const_0xa2 , _sage_const_0xb9 , _sage_const_0xb0 , _sage_const_0x8f , _sage_const_0x86 ,
            _sage_const_0x9d , _sage_const_0x94 , _sage_const_0xe3 , _sage_const_0xea , _sage_const_0xf1 , _sage_const_0xf8 , _sage_const_0xc7 , _sage_const_0xce , _sage_const_0xd5 , _sage_const_0xdc , _sage_const_0x76 , _sage_const_0x7f , _sage_const_0x64 , _sage_const_0x6d , _sage_const_0x52 , _sage_const_0x5b , _sage_const_0x40 , _sage_const_0x49 ,
            _sage_const_0x3e , _sage_const_0x37 , _sage_const_0x2c , _sage_const_0x25 , _sage_const_0x1a , _sage_const_0x13 , _sage_const_0x08 , _sage_const_0x01 , _sage_const_0xe6 , _sage_const_0xef , _sage_const_0xf4 , _sage_const_0xfd , _sage_const_0xc2 , _sage_const_0xcb , _sage_const_0xd0 , _sage_const_0xd9 , _sage_const_0xae , _sage_const_0xa7 ,
            _sage_const_0xbc , _sage_const_0xb5 , _sage_const_0x8a , _sage_const_0x83 , _sage_const_0x98 , _sage_const_0x91 , _sage_const_0x4d , _sage_const_0x44 , _sage_const_0x5f , _sage_const_0x56 , _sage_const_0x69 , _sage_const_0x60 , _sage_const_0x7b , _sage_const_0x72 , _sage_const_0x05 , _sage_const_0x0c , _sage_const_0x17 , _sage_const_0x1e ,
            _sage_const_0x21 , _sage_const_0x28 , _sage_const_0x33 , _sage_const_0x3a , _sage_const_0xdd , _sage_const_0xd4 , _sage_const_0xcf , _sage_const_0xc6 , _sage_const_0xf9 , _sage_const_0xf0 , _sage_const_0xeb , _sage_const_0xe2 , _sage_const_0x95 , _sage_const_0x9c , _sage_const_0x87 , _sage_const_0x8e , _sage_const_0xb1 , _sage_const_0xb8 ,
            _sage_const_0xa3 , _sage_const_0xaa , _sage_const_0xec , _sage_const_0xe5 , _sage_const_0xfe , _sage_const_0xf7 , _sage_const_0xc8 , _sage_const_0xc1 , _sage_const_0xda , _sage_const_0xd3 , _sage_const_0xa4 , _sage_const_0xad , _sage_const_0xb6 , _sage_const_0xbf , _sage_const_0x80 , _sage_const_0x89 , _sage_const_0x92 , _sage_const_0x9b ,
            _sage_const_0x7c , _sage_const_0x75 , _sage_const_0x6e , _sage_const_0x67 , _sage_const_0x58 , _sage_const_0x51 , _sage_const_0x4a , _sage_const_0x43 , _sage_const_0x34 , _sage_const_0x3d , _sage_const_0x26 , _sage_const_0x2f , _sage_const_0x10 , _sage_const_0x19 , _sage_const_0x02 , _sage_const_0x0b , _sage_const_0xd7 , _sage_const_0xde ,
            _sage_const_0xc5 , _sage_const_0xcc , _sage_const_0xf3 , _sage_const_0xfa , _sage_const_0xe1 , _sage_const_0xe8 , _sage_const_0x9f , _sage_const_0x96 , _sage_const_0x8d , _sage_const_0x84 , _sage_const_0xbb , _sage_const_0xb2 , _sage_const_0xa9 , _sage_const_0xa0 , _sage_const_0x47 , _sage_const_0x4e , _sage_const_0x55 , _sage_const_0x5c ,
            _sage_const_0x63 , _sage_const_0x6a , _sage_const_0x71 , _sage_const_0x78 , _sage_const_0x0f , _sage_const_0x06 , _sage_const_0x1d , _sage_const_0x14 , _sage_const_0x2b , _sage_const_0x22 , _sage_const_0x39 , _sage_const_0x30 , _sage_const_0x9a , _sage_const_0x93 , _sage_const_0x88 , _sage_const_0x81 , _sage_const_0xbe , _sage_const_0xb7 ,
            _sage_const_0xac , _sage_const_0xa5 , _sage_const_0xd2 , _sage_const_0xdb , _sage_const_0xc0 , _sage_const_0xc9 , _sage_const_0xf6 , _sage_const_0xff , _sage_const_0xe4 , _sage_const_0xed , _sage_const_0x0a , _sage_const_0x03 , _sage_const_0x18 , _sage_const_0x11 , _sage_const_0x2e , _sage_const_0x27 , _sage_const_0x3c , _sage_const_0x35 ,
            _sage_const_0x42 , _sage_const_0x4b , _sage_const_0x50 , _sage_const_0x59 , _sage_const_0x66 , _sage_const_0x6f , _sage_const_0x74 , _sage_const_0x7d , _sage_const_0xa1 , _sage_const_0xa8 , _sage_const_0xb3 , _sage_const_0xba , _sage_const_0x85 , _sage_const_0x8c , _sage_const_0x97 , _sage_const_0x9e , _sage_const_0xe9 , _sage_const_0xe0 ,
            _sage_const_0xfb , _sage_const_0xf2 , _sage_const_0xcd , _sage_const_0xc4 , _sage_const_0xdf , _sage_const_0xd6 , _sage_const_0x31 , _sage_const_0x38 , _sage_const_0x23 , _sage_const_0x2a , _sage_const_0x15 , _sage_const_0x1c , _sage_const_0x07 , _sage_const_0x0e , _sage_const_0x79 , _sage_const_0x70 , _sage_const_0x6b , _sage_const_0x62 ,
            _sage_const_0x5d , _sage_const_0x54 , _sage_const_0x4f , _sage_const_0x46 ]
mulby[_sage_const_11 ] = [_sage_const_0x00 , _sage_const_0x0b , _sage_const_0x16 , _sage_const_0x1d , _sage_const_0x2c , _sage_const_0x27 , _sage_const_0x3a , _sage_const_0x31 , _sage_const_0x58 , _sage_const_0x53 , _sage_const_0x4e , _sage_const_0x45 , _sage_const_0x74 , _sage_const_0x7f , _sage_const_0x62 , _sage_const_0x69 , _sage_const_0xb0 , _sage_const_0xbb ,
             _sage_const_0xa6 , _sage_const_0xad , _sage_const_0x9c , _sage_const_0x97 , _sage_const_0x8a , _sage_const_0x81 , _sage_const_0xe8 , _sage_const_0xe3 , _sage_const_0xfe , _sage_const_0xf5 , _sage_const_0xc4 , _sage_const_0xcf , _sage_const_0xd2 , _sage_const_0xd9 , _sage_const_0x7b , _sage_const_0x70 , _sage_const_0x6d , _sage_const_0x66 ,
             _sage_const_0x57 , _sage_const_0x5c , _sage_const_0x41 , _sage_const_0x4a , _sage_const_0x23 , _sage_const_0x28 , _sage_const_0x35 , _sage_const_0x3e , _sage_const_0x0f , _sage_const_0x04 , _sage_const_0x19 , _sage_const_0x12 , _sage_const_0xcb , _sage_const_0xc0 , _sage_const_0xdd , _sage_const_0xd6 , _sage_const_0xe7 , _sage_const_0xec ,
             _sage_const_0xf1 , _sage_const_0xfa , _sage_const_0x93 , _sage_const_0x98 , _sage_const_0x85 , _sage_const_0x8e , _sage_const_0xbf , _sage_const_0xb4 , _sage_const_0xa9 , _sage_const_0xa2 , _sage_const_0xf6 , _sage_const_0xfd , _sage_const_0xe0 , _sage_const_0xeb , _sage_const_0xda , _sage_const_0xd1 , _sage_const_0xcc , _sage_const_0xc7 ,
             _sage_const_0xae , _sage_const_0xa5 , _sage_const_0xb8 , _sage_const_0xb3 , _sage_const_0x82 , _sage_const_0x89 , _sage_const_0x94 , _sage_const_0x9f , _sage_const_0x46 , _sage_const_0x4d , _sage_const_0x50 , _sage_const_0x5b , _sage_const_0x6a , _sage_const_0x61 , _sage_const_0x7c , _sage_const_0x77 , _sage_const_0x1e , _sage_const_0x15 ,
             _sage_const_0x08 , _sage_const_0x03 , _sage_const_0x32 , _sage_const_0x39 , _sage_const_0x24 , _sage_const_0x2f , _sage_const_0x8d , _sage_const_0x86 , _sage_const_0x9b , _sage_const_0x90 , _sage_const_0xa1 , _sage_const_0xaa , _sage_const_0xb7 , _sage_const_0xbc , _sage_const_0xd5 , _sage_const_0xde , _sage_const_0xc3 , _sage_const_0xc8 ,
             _sage_const_0xf9 , _sage_const_0xf2 , _sage_const_0xef , _sage_const_0xe4 , _sage_const_0x3d , _sage_const_0x36 , _sage_const_0x2b , _sage_const_0x20 , _sage_const_0x11 , _sage_const_0x1a , _sage_const_0x07 , _sage_const_0x0c , _sage_const_0x65 , _sage_const_0x6e , _sage_const_0x73 , _sage_const_0x78 , _sage_const_0x49 , _sage_const_0x42 ,
             _sage_const_0x5f , _sage_const_0x54 , _sage_const_0xf7 , _sage_const_0xfc , _sage_const_0xe1 , _sage_const_0xea , _sage_const_0xdb , _sage_const_0xd0 , _sage_const_0xcd , _sage_const_0xc6 , _sage_const_0xaf , _sage_const_0xa4 , _sage_const_0xb9 , _sage_const_0xb2 , _sage_const_0x83 , _sage_const_0x88 , _sage_const_0x95 , _sage_const_0x9e ,
             _sage_const_0x47 , _sage_const_0x4c , _sage_const_0x51 , _sage_const_0x5a , _sage_const_0x6b , _sage_const_0x60 , _sage_const_0x7d , _sage_const_0x76 , _sage_const_0x1f , _sage_const_0x14 , _sage_const_0x09 , _sage_const_0x02 , _sage_const_0x33 , _sage_const_0x38 , _sage_const_0x25 , _sage_const_0x2e , _sage_const_0x8c , _sage_const_0x87 ,
             _sage_const_0x9a , _sage_const_0x91 , _sage_const_0xa0 , _sage_const_0xab , _sage_const_0xb6 , _sage_const_0xbd , _sage_const_0xd4 , _sage_const_0xdf , _sage_const_0xc2 , _sage_const_0xc9 , _sage_const_0xf8 , _sage_const_0xf3 , _sage_const_0xee , _sage_const_0xe5 , _sage_const_0x3c , _sage_const_0x37 , _sage_const_0x2a , _sage_const_0x21 ,
             _sage_const_0x10 , _sage_const_0x1b , _sage_const_0x06 , _sage_const_0x0d , _sage_const_0x64 , _sage_const_0x6f , _sage_const_0x72 , _sage_const_0x79 , _sage_const_0x48 , _sage_const_0x43 , _sage_const_0x5e , _sage_const_0x55 , _sage_const_0x01 , _sage_const_0x0a , _sage_const_0x17 , _sage_const_0x1c , _sage_const_0x2d , _sage_const_0x26 ,
             _sage_const_0x3b , _sage_const_0x30 , _sage_const_0x59 , _sage_const_0x52 , _sage_const_0x4f , _sage_const_0x44 , _sage_const_0x75 , _sage_const_0x7e , _sage_const_0x63 , _sage_const_0x68 , _sage_const_0xb1 , _sage_const_0xba , _sage_const_0xa7 , _sage_const_0xac , _sage_const_0x9d , _sage_const_0x96 , _sage_const_0x8b , _sage_const_0x80 ,
             _sage_const_0xe9 , _sage_const_0xe2 , _sage_const_0xff , _sage_const_0xf4 , _sage_const_0xc5 , _sage_const_0xce , _sage_const_0xd3 , _sage_const_0xd8 , _sage_const_0x7a , _sage_const_0x71 , _sage_const_0x6c , _sage_const_0x67 , _sage_const_0x56 , _sage_const_0x5d , _sage_const_0x40 , _sage_const_0x4b , _sage_const_0x22 , _sage_const_0x29 ,
             _sage_const_0x34 , _sage_const_0x3f , _sage_const_0x0e , _sage_const_0x05 , _sage_const_0x18 , _sage_const_0x13 , _sage_const_0xca , _sage_const_0xc1 , _sage_const_0xdc , _sage_const_0xd7 , _sage_const_0xe6 , _sage_const_0xed , _sage_const_0xf0 , _sage_const_0xfb , _sage_const_0x92 , _sage_const_0x99 , _sage_const_0x84 , _sage_const_0x8f ,
             _sage_const_0xbe , _sage_const_0xb5 , _sage_const_0xa8 , _sage_const_0xa3 ]
mulby[_sage_const_13 ] = [_sage_const_0x00 , _sage_const_0x0d , _sage_const_0x1a , _sage_const_0x17 , _sage_const_0x34 , _sage_const_0x39 , _sage_const_0x2e , _sage_const_0x23 , _sage_const_0x68 , _sage_const_0x65 , _sage_const_0x72 , _sage_const_0x7f , _sage_const_0x5c , _sage_const_0x51 , _sage_const_0x46 , _sage_const_0x4b , _sage_const_0xd0 , _sage_const_0xdd ,
             _sage_const_0xca , _sage_const_0xc7 , _sage_const_0xe4 , _sage_const_0xe9 , _sage_const_0xfe , _sage_const_0xf3 , _sage_const_0xb8 , _sage_const_0xb5 , _sage_const_0xa2 , _sage_const_0xaf , _sage_const_0x8c , _sage_const_0x81 , _sage_const_0x96 , _sage_const_0x9b , _sage_const_0xbb , _sage_const_0xb6 , _sage_const_0xa1 , _sage_const_0xac ,
             _sage_const_0x8f , _sage_const_0x82 , _sage_const_0x95 , _sage_const_0x98 , _sage_const_0xd3 , _sage_const_0xde , _sage_const_0xc9 , _sage_const_0xc4 , _sage_const_0xe7 , _sage_const_0xea , _sage_const_0xfd , _sage_const_0xf0 , _sage_const_0x6b , _sage_const_0x66 , _sage_const_0x71 , _sage_const_0x7c , _sage_const_0x5f , _sage_const_0x52 ,
             _sage_const_0x45 , _sage_const_0x48 , _sage_const_0x03 , _sage_const_0x0e , _sage_const_0x19 , _sage_const_0x14 , _sage_const_0x37 , _sage_const_0x3a , _sage_const_0x2d , _sage_const_0x20 , _sage_const_0x6d , _sage_const_0x60 , _sage_const_0x77 , _sage_const_0x7a , _sage_const_0x59 , _sage_const_0x54 , _sage_const_0x43 , _sage_const_0x4e ,
             _sage_const_0x05 , _sage_const_0x08 , _sage_const_0x1f , _sage_const_0x12 , _sage_const_0x31 , _sage_const_0x3c , _sage_const_0x2b , _sage_const_0x26 , _sage_const_0xbd , _sage_const_0xb0 , _sage_const_0xa7 , _sage_const_0xaa , _sage_const_0x89 , _sage_const_0x84 , _sage_const_0x93 , _sage_const_0x9e , _sage_const_0xd5 , _sage_const_0xd8 ,
             _sage_const_0xcf , _sage_const_0xc2 , _sage_const_0xe1 , _sage_const_0xec , _sage_const_0xfb , _sage_const_0xf6 , _sage_const_0xd6 , _sage_const_0xdb , _sage_const_0xcc , _sage_const_0xc1 , _sage_const_0xe2 , _sage_const_0xef , _sage_const_0xf8 , _sage_const_0xf5 , _sage_const_0xbe , _sage_const_0xb3 , _sage_const_0xa4 , _sage_const_0xa9 ,
             _sage_const_0x8a , _sage_const_0x87 , _sage_const_0x90 , _sage_const_0x9d , _sage_const_0x06 , _sage_const_0x0b , _sage_const_0x1c , _sage_const_0x11 , _sage_const_0x32 , _sage_const_0x3f , _sage_const_0x28 , _sage_const_0x25 , _sage_const_0x6e , _sage_const_0x63 , _sage_const_0x74 , _sage_const_0x79 , _sage_const_0x5a , _sage_const_0x57 ,
             _sage_const_0x40 , _sage_const_0x4d , _sage_const_0xda , _sage_const_0xd7 , _sage_const_0xc0 , _sage_const_0xcd , _sage_const_0xee , _sage_const_0xe3 , _sage_const_0xf4 , _sage_const_0xf9 , _sage_const_0xb2 , _sage_const_0xbf , _sage_const_0xa8 , _sage_const_0xa5 , _sage_const_0x86 , _sage_const_0x8b , _sage_const_0x9c , _sage_const_0x91 ,
             _sage_const_0x0a , _sage_const_0x07 , _sage_const_0x10 , _sage_const_0x1d , _sage_const_0x3e , _sage_const_0x33 , _sage_const_0x24 , _sage_const_0x29 , _sage_const_0x62 , _sage_const_0x6f , _sage_const_0x78 , _sage_const_0x75 , _sage_const_0x56 , _sage_const_0x5b , _sage_const_0x4c , _sage_const_0x41 , _sage_const_0x61 , _sage_const_0x6c ,
             _sage_const_0x7b , _sage_const_0x76 , _sage_const_0x55 , _sage_const_0x58 , _sage_const_0x4f , _sage_const_0x42 , _sage_const_0x09 , _sage_const_0x04 , _sage_const_0x13 , _sage_const_0x1e , _sage_const_0x3d , _sage_const_0x30 , _sage_const_0x27 , _sage_const_0x2a , _sage_const_0xb1 , _sage_const_0xbc , _sage_const_0xab , _sage_const_0xa6 ,
             _sage_const_0x85 , _sage_const_0x88 , _sage_const_0x9f , _sage_const_0x92 , _sage_const_0xd9 , _sage_const_0xd4 , _sage_const_0xc3 , _sage_const_0xce , _sage_const_0xed , _sage_const_0xe0 , _sage_const_0xf7 , _sage_const_0xfa , _sage_const_0xb7 , _sage_const_0xba , _sage_const_0xad , _sage_const_0xa0 , _sage_const_0x83 , _sage_const_0x8e ,
             _sage_const_0x99 , _sage_const_0x94 , _sage_const_0xdf , _sage_const_0xd2 , _sage_const_0xc5 , _sage_const_0xc8 , _sage_const_0xeb , _sage_const_0xe6 , _sage_const_0xf1 , _sage_const_0xfc , _sage_const_0x67 , _sage_const_0x6a , _sage_const_0x7d , _sage_const_0x70 , _sage_const_0x53 , _sage_const_0x5e , _sage_const_0x49 , _sage_const_0x44 ,
             _sage_const_0x0f , _sage_const_0x02 , _sage_const_0x15 , _sage_const_0x18 , _sage_const_0x3b , _sage_const_0x36 , _sage_const_0x21 , _sage_const_0x2c , _sage_const_0x0c , _sage_const_0x01 , _sage_const_0x16 , _sage_const_0x1b , _sage_const_0x38 , _sage_const_0x35 , _sage_const_0x22 , _sage_const_0x2f , _sage_const_0x64 , _sage_const_0x69 ,
             _sage_const_0x7e , _sage_const_0x73 , _sage_const_0x50 , _sage_const_0x5d , _sage_const_0x4a , _sage_const_0x47 , _sage_const_0xdc , _sage_const_0xd1 , _sage_const_0xc6 , _sage_const_0xcb , _sage_const_0xe8 , _sage_const_0xe5 , _sage_const_0xf2 , _sage_const_0xff , _sage_const_0xb4 , _sage_const_0xb9 , _sage_const_0xae , _sage_const_0xa3 ,
             _sage_const_0x80 , _sage_const_0x8d , _sage_const_0x9a , _sage_const_0x97 ]
mulby[_sage_const_14 ] = [_sage_const_0x00 , _sage_const_0x0e , _sage_const_0x1c , _sage_const_0x12 , _sage_const_0x38 , _sage_const_0x36 , _sage_const_0x24 , _sage_const_0x2a , _sage_const_0x70 , _sage_const_0x7e , _sage_const_0x6c , _sage_const_0x62 , _sage_const_0x48 , _sage_const_0x46 , _sage_const_0x54 , _sage_const_0x5a , _sage_const_0xe0 , _sage_const_0xee ,
             _sage_const_0xfc , _sage_const_0xf2 , _sage_const_0xd8 , _sage_const_0xd6 , _sage_const_0xc4 , _sage_const_0xca , _sage_const_0x90 , _sage_const_0x9e , _sage_const_0x8c , _sage_const_0x82 , _sage_const_0xa8 , _sage_const_0xa6 , _sage_const_0xb4 , _sage_const_0xba , _sage_const_0xdb , _sage_const_0xd5 , _sage_const_0xc7 , _sage_const_0xc9 ,
             _sage_const_0xe3 , _sage_const_0xed , _sage_const_0xff , _sage_const_0xf1 , _sage_const_0xab , _sage_const_0xa5 , _sage_const_0xb7 , _sage_const_0xb9 , _sage_const_0x93 , _sage_const_0x9d , _sage_const_0x8f , _sage_const_0x81 , _sage_const_0x3b , _sage_const_0x35 , _sage_const_0x27 , _sage_const_0x29 , _sage_const_0x03 , _sage_const_0x0d ,
             _sage_const_0x1f , _sage_const_0x11 , _sage_const_0x4b , _sage_const_0x45 , _sage_const_0x57 , _sage_const_0x59 , _sage_const_0x73 , _sage_const_0x7d , _sage_const_0x6f , _sage_const_0x61 , _sage_const_0xad , _sage_const_0xa3 , _sage_const_0xb1 , _sage_const_0xbf , _sage_const_0x95 , _sage_const_0x9b , _sage_const_0x89 , _sage_const_0x87 ,
             _sage_const_0xdd , _sage_const_0xd3 , _sage_const_0xc1 , _sage_const_0xcf , _sage_const_0xe5 , _sage_const_0xeb , _sage_const_0xf9 , _sage_const_0xf7 , _sage_const_0x4d , _sage_const_0x43 , _sage_const_0x51 , _sage_const_0x5f , _sage_const_0x75 , _sage_const_0x7b , _sage_const_0x69 , _sage_const_0x67 , _sage_const_0x3d , _sage_const_0x33 ,
             _sage_const_0x21 , _sage_const_0x2f , _sage_const_0x05 , _sage_const_0x0b , _sage_const_0x19 , _sage_const_0x17 , _sage_const_0x76 , _sage_const_0x78 , _sage_const_0x6a , _sage_const_0x64 , _sage_const_0x4e , _sage_const_0x40 , _sage_const_0x52 , _sage_const_0x5c , _sage_const_0x06 , _sage_const_0x08 , _sage_const_0x1a , _sage_const_0x14 ,
             _sage_const_0x3e , _sage_const_0x30 , _sage_const_0x22 , _sage_const_0x2c , _sage_const_0x96 , _sage_const_0x98 , _sage_const_0x8a , _sage_const_0x84 , _sage_const_0xae , _sage_const_0xa0 , _sage_const_0xb2 , _sage_const_0xbc , _sage_const_0xe6 , _sage_const_0xe8 , _sage_const_0xfa , _sage_const_0xf4 , _sage_const_0xde , _sage_const_0xd0 ,
             _sage_const_0xc2 , _sage_const_0xcc , _sage_const_0x41 , _sage_const_0x4f , _sage_const_0x5d , _sage_const_0x53 , _sage_const_0x79 , _sage_const_0x77 , _sage_const_0x65 , _sage_const_0x6b , _sage_const_0x31 , _sage_const_0x3f , _sage_const_0x2d , _sage_const_0x23 , _sage_const_0x09 , _sage_const_0x07 , _sage_const_0x15 , _sage_const_0x1b ,
             _sage_const_0xa1 , _sage_const_0xaf , _sage_const_0xbd , _sage_const_0xb3 , _sage_const_0x99 , _sage_const_0x97 , _sage_const_0x85 , _sage_const_0x8b , _sage_const_0xd1 , _sage_const_0xdf , _sage_const_0xcd , _sage_const_0xc3 , _sage_const_0xe9 , _sage_const_0xe7 , _sage_const_0xf5 , _sage_const_0xfb , _sage_const_0x9a , _sage_const_0x94 ,
             _sage_const_0x86 , _sage_const_0x88 , _sage_const_0xa2 , _sage_const_0xac , _sage_const_0xbe , _sage_const_0xb0 , _sage_const_0xea , _sage_const_0xe4 , _sage_const_0xf6 , _sage_const_0xf8 , _sage_const_0xd2 , _sage_const_0xdc , _sage_const_0xce , _sage_const_0xc0 , _sage_const_0x7a , _sage_const_0x74 , _sage_const_0x66 , _sage_const_0x68 ,
             _sage_const_0x42 , _sage_const_0x4c , _sage_const_0x5e , _sage_const_0x50 , _sage_const_0x0a , _sage_const_0x04 , _sage_const_0x16 , _sage_const_0x18 , _sage_const_0x32 , _sage_const_0x3c , _sage_const_0x2e , _sage_const_0x20 , _sage_const_0xec , _sage_const_0xe2 , _sage_const_0xf0 , _sage_const_0xfe , _sage_const_0xd4 , _sage_const_0xda ,
             _sage_const_0xc8 , _sage_const_0xc6 , _sage_const_0x9c , _sage_const_0x92 , _sage_const_0x80 , _sage_const_0x8e , _sage_const_0xa4 , _sage_const_0xaa , _sage_const_0xb8 , _sage_const_0xb6 , _sage_const_0x0c , _sage_const_0x02 , _sage_const_0x10 , _sage_const_0x1e , _sage_const_0x34 , _sage_const_0x3a , _sage_const_0x28 , _sage_const_0x26 ,
             _sage_const_0x7c , _sage_const_0x72 , _sage_const_0x60 , _sage_const_0x6e , _sage_const_0x44 , _sage_const_0x4a , _sage_const_0x58 , _sage_const_0x56 , _sage_const_0x37 , _sage_const_0x39 , _sage_const_0x2b , _sage_const_0x25 , _sage_const_0x0f , _sage_const_0x01 , _sage_const_0x13 , _sage_const_0x1d , _sage_const_0x47 , _sage_const_0x49 ,
             _sage_const_0x5b , _sage_const_0x55 , _sage_const_0x7f , _sage_const_0x71 , _sage_const_0x63 , _sage_const_0x6d , _sage_const_0xd7 , _sage_const_0xd9 , _sage_const_0xcb , _sage_const_0xc5 , _sage_const_0xef , _sage_const_0xe1 , _sage_const_0xf3 , _sage_const_0xfd , _sage_const_0xa7 , _sage_const_0xa9 , _sage_const_0xbb , _sage_const_0xb5 ,
             _sage_const_0x9f , _sage_const_0x91 , _sage_const_0x83 , _sage_const_0x8d ]

Sbox = (
_sage_const_0x63 , _sage_const_0x7C , _sage_const_0x77 , _sage_const_0x7B , _sage_const_0xF2 , _sage_const_0x6B , _sage_const_0x6F , _sage_const_0xC5 , _sage_const_0x30 , _sage_const_0x01 , _sage_const_0x67 , _sage_const_0x2B , _sage_const_0xFE , _sage_const_0xD7 , _sage_const_0xAB , _sage_const_0x76 , _sage_const_0xCA , _sage_const_0x82 , _sage_const_0xC9 , _sage_const_0x7D ,
_sage_const_0xFA , _sage_const_0x59 , _sage_const_0x47 , _sage_const_0xF0 , _sage_const_0xAD , _sage_const_0xD4 , _sage_const_0xA2 , _sage_const_0xAF , _sage_const_0x9C , _sage_const_0xA4 , _sage_const_0x72 , _sage_const_0xC0 , _sage_const_0xB7 , _sage_const_0xFD , _sage_const_0x93 , _sage_const_0x26 , _sage_const_0x36 , _sage_const_0x3F , _sage_const_0xF7 , _sage_const_0xCC ,
_sage_const_0x34 , _sage_const_0xA5 , _sage_const_0xE5 , _sage_const_0xF1 , _sage_const_0x71 , _sage_const_0xD8 , _sage_const_0x31 , _sage_const_0x15 , _sage_const_0x04 , _sage_const_0xC7 , _sage_const_0x23 , _sage_const_0xC3 , _sage_const_0x18 , _sage_const_0x96 , _sage_const_0x05 , _sage_const_0x9A , _sage_const_0x07 , _sage_const_0x12 , _sage_const_0x80 , _sage_const_0xE2 ,
_sage_const_0xEB , _sage_const_0x27 , _sage_const_0xB2 , _sage_const_0x75 , _sage_const_0x09 , _sage_const_0x83 , _sage_const_0x2C , _sage_const_0x1A , _sage_const_0x1B , _sage_const_0x6E , _sage_const_0x5A , _sage_const_0xA0 , _sage_const_0x52 , _sage_const_0x3B , _sage_const_0xD6 , _sage_const_0xB3 , _sage_const_0x29 , _sage_const_0xE3 , _sage_const_0x2F , _sage_const_0x84 ,
_sage_const_0x53 , _sage_const_0xD1 , _sage_const_0x00 , _sage_const_0xED , _sage_const_0x20 , _sage_const_0xFC , _sage_const_0xB1 , _sage_const_0x5B , _sage_const_0x6A , _sage_const_0xCB , _sage_const_0xBE , _sage_const_0x39 , _sage_const_0x4A , _sage_const_0x4C , _sage_const_0x58 , _sage_const_0xCF , _sage_const_0xD0 , _sage_const_0xEF , _sage_const_0xAA , _sage_const_0xFB ,
_sage_const_0x43 , _sage_const_0x4D , _sage_const_0x33 , _sage_const_0x85 , _sage_const_0x45 , _sage_const_0xF9 , _sage_const_0x02 , _sage_const_0x7F , _sage_const_0x50 , _sage_const_0x3C , _sage_const_0x9F , _sage_const_0xA8 , _sage_const_0x51 , _sage_const_0xA3 , _sage_const_0x40 , _sage_const_0x8F , _sage_const_0x92 , _sage_const_0x9D , _sage_const_0x38 , _sage_const_0xF5 ,
_sage_const_0xBC , _sage_const_0xB6 , _sage_const_0xDA , _sage_const_0x21 , _sage_const_0x10 , _sage_const_0xFF , _sage_const_0xF3 , _sage_const_0xD2 , _sage_const_0xCD , _sage_const_0x0C , _sage_const_0x13 , _sage_const_0xEC , _sage_const_0x5F , _sage_const_0x97 , _sage_const_0x44 , _sage_const_0x17 , _sage_const_0xC4 , _sage_const_0xA7 , _sage_const_0x7E , _sage_const_0x3D ,
_sage_const_0x64 , _sage_const_0x5D , _sage_const_0x19 , _sage_const_0x73 , _sage_const_0x60 , _sage_const_0x81 , _sage_const_0x4F , _sage_const_0xDC , _sage_const_0x22 , _sage_const_0x2A , _sage_const_0x90 , _sage_const_0x88 , _sage_const_0x46 , _sage_const_0xEE , _sage_const_0xB8 , _sage_const_0x14 , _sage_const_0xDE , _sage_const_0x5E , _sage_const_0x0B , _sage_const_0xDB ,
_sage_const_0xE0 , _sage_const_0x32 , _sage_const_0x3A , _sage_const_0x0A , _sage_const_0x49 , _sage_const_0x06 , _sage_const_0x24 , _sage_const_0x5C , _sage_const_0xC2 , _sage_const_0xD3 , _sage_const_0xAC , _sage_const_0x62 , _sage_const_0x91 , _sage_const_0x95 , _sage_const_0xE4 , _sage_const_0x79 , _sage_const_0xE7 , _sage_const_0xC8 , _sage_const_0x37 , _sage_const_0x6D ,
_sage_const_0x8D , _sage_const_0xD5 , _sage_const_0x4E , _sage_const_0xA9 , _sage_const_0x6C , _sage_const_0x56 , _sage_const_0xF4 , _sage_const_0xEA , _sage_const_0x65 , _sage_const_0x7A , _sage_const_0xAE , _sage_const_0x08 , _sage_const_0xBA , _sage_const_0x78 , _sage_const_0x25 , _sage_const_0x2E , _sage_const_0x1C , _sage_const_0xA6 , _sage_const_0xB4 , _sage_const_0xC6 ,
_sage_const_0xE8 , _sage_const_0xDD , _sage_const_0x74 , _sage_const_0x1F , _sage_const_0x4B , _sage_const_0xBD , _sage_const_0x8B , _sage_const_0x8A , _sage_const_0x70 , _sage_const_0x3E , _sage_const_0xB5 , _sage_const_0x66 , _sage_const_0x48 , _sage_const_0x03 , _sage_const_0xF6 , _sage_const_0x0E , _sage_const_0x61 , _sage_const_0x35 , _sage_const_0x57 , _sage_const_0xB9 ,
_sage_const_0x86 , _sage_const_0xC1 , _sage_const_0x1D , _sage_const_0x9E , _sage_const_0xE1 , _sage_const_0xF8 , _sage_const_0x98 , _sage_const_0x11 , _sage_const_0x69 , _sage_const_0xD9 , _sage_const_0x8E , _sage_const_0x94 , _sage_const_0x9B , _sage_const_0x1E , _sage_const_0x87 , _sage_const_0xE9 , _sage_const_0xCE , _sage_const_0x55 , _sage_const_0x28 , _sage_const_0xDF ,
_sage_const_0x8C , _sage_const_0xA1 , _sage_const_0x89 , _sage_const_0x0D , _sage_const_0xBF , _sage_const_0xE6 , _sage_const_0x42 , _sage_const_0x68 , _sage_const_0x41 , _sage_const_0x99 , _sage_const_0x2D , _sage_const_0x0F , _sage_const_0xB0 , _sage_const_0x54 , _sage_const_0xBB , _sage_const_0x16 )
Sbox_inv = (
_sage_const_0x52 , _sage_const_0x09 , _sage_const_0x6A , _sage_const_0xD5 , _sage_const_0x30 , _sage_const_0x36 , _sage_const_0xA5 , _sage_const_0x38 , _sage_const_0xBF , _sage_const_0x40 , _sage_const_0xA3 , _sage_const_0x9E , _sage_const_0x81 , _sage_const_0xF3 , _sage_const_0xD7 , _sage_const_0xFB , _sage_const_0x7C , _sage_const_0xE3 , _sage_const_0x39 , _sage_const_0x82 ,
_sage_const_0x9B , _sage_const_0x2F , _sage_const_0xFF , _sage_const_0x87 , _sage_const_0x34 , _sage_const_0x8E , _sage_const_0x43 , _sage_const_0x44 , _sage_const_0xC4 , _sage_const_0xDE , _sage_const_0xE9 , _sage_const_0xCB , _sage_const_0x54 , _sage_const_0x7B , _sage_const_0x94 , _sage_const_0x32 , _sage_const_0xA6 , _sage_const_0xC2 , _sage_const_0x23 , _sage_const_0x3D ,
_sage_const_0xEE , _sage_const_0x4C , _sage_const_0x95 , _sage_const_0x0B , _sage_const_0x42 , _sage_const_0xFA , _sage_const_0xC3 , _sage_const_0x4E , _sage_const_0x08 , _sage_const_0x2E , _sage_const_0xA1 , _sage_const_0x66 , _sage_const_0x28 , _sage_const_0xD9 , _sage_const_0x24 , _sage_const_0xB2 , _sage_const_0x76 , _sage_const_0x5B , _sage_const_0xA2 , _sage_const_0x49 ,
_sage_const_0x6D , _sage_const_0x8B , _sage_const_0xD1 , _sage_const_0x25 , _sage_const_0x72 , _sage_const_0xF8 , _sage_const_0xF6 , _sage_const_0x64 , _sage_const_0x86 , _sage_const_0x68 , _sage_const_0x98 , _sage_const_0x16 , _sage_const_0xD4 , _sage_const_0xA4 , _sage_const_0x5C , _sage_const_0xCC , _sage_const_0x5D , _sage_const_0x65 , _sage_const_0xB6 , _sage_const_0x92 ,
_sage_const_0x6C , _sage_const_0x70 , _sage_const_0x48 , _sage_const_0x50 , _sage_const_0xFD , _sage_const_0xED , _sage_const_0xB9 , _sage_const_0xDA , _sage_const_0x5E , _sage_const_0x15 , _sage_const_0x46 , _sage_const_0x57 , _sage_const_0xA7 , _sage_const_0x8D , _sage_const_0x9D , _sage_const_0x84 , _sage_const_0x90 , _sage_const_0xD8 , _sage_const_0xAB , _sage_const_0x00 ,
_sage_const_0x8C , _sage_const_0xBC , _sage_const_0xD3 , _sage_const_0x0A , _sage_const_0xF7 , _sage_const_0xE4 , _sage_const_0x58 , _sage_const_0x05 , _sage_const_0xB8 , _sage_const_0xB3 , _sage_const_0x45 , _sage_const_0x06 , _sage_const_0xD0 , _sage_const_0x2C , _sage_const_0x1E , _sage_const_0x8F , _sage_const_0xCA , _sage_const_0x3F , _sage_const_0x0F , _sage_const_0x02 ,
_sage_const_0xC1 , _sage_const_0xAF , _sage_const_0xBD , _sage_const_0x03 , _sage_const_0x01 , _sage_const_0x13 , _sage_const_0x8A , _sage_const_0x6B , _sage_const_0x3A , _sage_const_0x91 , _sage_const_0x11 , _sage_const_0x41 , _sage_const_0x4F , _sage_const_0x67 , _sage_const_0xDC , _sage_const_0xEA , _sage_const_0x97 , _sage_const_0xF2 , _sage_const_0xCF , _sage_const_0xCE ,
_sage_const_0xF0 , _sage_const_0xB4 , _sage_const_0xE6 , _sage_const_0x73 , _sage_const_0x96 , _sage_const_0xAC , _sage_const_0x74 , _sage_const_0x22 , _sage_const_0xE7 , _sage_const_0xAD , _sage_const_0x35 , _sage_const_0x85 , _sage_const_0xE2 , _sage_const_0xF9 , _sage_const_0x37 , _sage_const_0xE8 , _sage_const_0x1C , _sage_const_0x75 , _sage_const_0xDF , _sage_const_0x6E ,
_sage_const_0x47 , _sage_const_0xF1 , _sage_const_0x1A , _sage_const_0x71 , _sage_const_0x1D , _sage_const_0x29 , _sage_const_0xC5 , _sage_const_0x89 , _sage_const_0x6F , _sage_const_0xB7 , _sage_const_0x62 , _sage_const_0x0E , _sage_const_0xAA , _sage_const_0x18 , _sage_const_0xBE , _sage_const_0x1B , _sage_const_0xFC , _sage_const_0x56 , _sage_const_0x3E , _sage_const_0x4B ,
_sage_const_0xC6 , _sage_const_0xD2 , _sage_const_0x79 , _sage_const_0x20 , _sage_const_0x9A , _sage_const_0xDB , _sage_const_0xC0 , _sage_const_0xFE , _sage_const_0x78 , _sage_const_0xCD , _sage_const_0x5A , _sage_const_0xF4 , _sage_const_0x1F , _sage_const_0xDD , _sage_const_0xA8 , _sage_const_0x33 , _sage_const_0x88 , _sage_const_0x07 , _sage_const_0xC7 , _sage_const_0x31 ,
_sage_const_0xB1 , _sage_const_0x12 , _sage_const_0x10 , _sage_const_0x59 , _sage_const_0x27 , _sage_const_0x80 , _sage_const_0xEC , _sage_const_0x5F , _sage_const_0x60 , _sage_const_0x51 , _sage_const_0x7F , _sage_const_0xA9 , _sage_const_0x19 , _sage_const_0xB5 , _sage_const_0x4A , _sage_const_0x0D , _sage_const_0x2D , _sage_const_0xE5 , _sage_const_0x7A , _sage_const_0x9F ,
_sage_const_0x93 , _sage_const_0xC9 , _sage_const_0x9C , _sage_const_0xEF , _sage_const_0xA0 , _sage_const_0xE0 , _sage_const_0x3B , _sage_const_0x4D , _sage_const_0xAE , _sage_const_0x2A , _sage_const_0xF5 , _sage_const_0xB0 , _sage_const_0xC8 , _sage_const_0xEB , _sage_const_0xBB , _sage_const_0x3C , _sage_const_0x83 , _sage_const_0x53 , _sage_const_0x99 , _sage_const_0x61 ,
_sage_const_0x17 , _sage_const_0x2B , _sage_const_0x04 , _sage_const_0x7E , _sage_const_0xBA , _sage_const_0x77 , _sage_const_0xD6 , _sage_const_0x26 , _sage_const_0xE1 , _sage_const_0x69 , _sage_const_0x14 , _sage_const_0x63 , _sage_const_0x55 , _sage_const_0x21 , _sage_const_0x0C , _sage_const_0x7D )
Rcon = (_sage_const_0x8d , _sage_const_0x01 , _sage_const_0x02 , _sage_const_0x04 , _sage_const_0x08 , _sage_const_0x10 , _sage_const_0x20 , _sage_const_0x40 , _sage_const_0x80 , _sage_const_0x1b , _sage_const_0x36 , _sage_const_0x6c , _sage_const_0xd8 , _sage_const_0xab , _sage_const_0x4d , _sage_const_0x9a )

mix_columns_matrix = [
    _sage_const_2 , _sage_const_3 , _sage_const_1 , _sage_const_1 ,
    _sage_const_1 , _sage_const_2 , _sage_const_3 , _sage_const_1 ,
    _sage_const_1 , _sage_const_1 , _sage_const_2 , _sage_const_3 ,
    _sage_const_3 , _sage_const_1 , _sage_const_1 , _sage_const_2 
]

inv_mix_columns_matrix = [
    _sage_const_14 , _sage_const_11 , _sage_const_13 , _sage_const_9 ,
    _sage_const_9 , _sage_const_14 , _sage_const_11 , _sage_const_13 ,
    _sage_const_13 , _sage_const_9 , _sage_const_14 , _sage_const_11 ,
    _sage_const_11 , _sage_const_13 , _sage_const_9 , _sage_const_14 
]


# HELPER FUNCTIONS
# abcd, 1234 -> d4 c3 b2 a1
def change_nibbles(a, b, size=_sage_const_4 ):
    return [(((a >> (i * size)) & _sage_const_0xf ) << _sage_const_4 ) | (b >> (i * size)) & _sage_const_0xf  for i in xrange(size * _sage_const_2 )]


def array_to_matrix(array, n=_sage_const_4 ):
    assert len(array) == n * n
    return matrix([array[i * n:(i * n) + n] for i in xrange(n)]).transpose()


def matrix_to_array(m):
    return [e for sublist in list(m.transpose()) for e in sublist]


def xor_matrices(a, b):
    return matrix([[a[i][j] ^ b[i][j] for j in xrange(a.dimensions()[_sage_const_0 ])] for i in xrange(a.dimensions()[_sage_const_0 ])])


def xor_vector(a, b):
    return vector([x ^ y for x, y in zip(a, b)])


def array_to_hexstring(array):
    return ''.join(chr(x) for x in array).encode('hex')


def matrix_to_hexstring(m):
    return array_to_hexstring(matrix_to_array(m))


def bytes_to_matrix(v):
    return array_to_matrix(map(int, v), _sage_const_4 )


# AES FUNCTIONS
def shift_rows(state):
    """
    0   4   8   12
    1   5   9   13
    2   6   10  14
    3   7   11  15

    0   4   8   12
    5   9   13  1
    10  14  2   6
    15  3   7   11
    """
    return matrix([state[_sage_const_0 ], list(state[_sage_const_1 ][_sage_const_1 :]) + [state[_sage_const_1 ][_sage_const_0 ]], [state[_sage_const_2 ][_sage_const_2 ], state[_sage_const_2 ][_sage_const_3 ], state[_sage_const_2 ][_sage_const_0 ], state[_sage_const_2 ][_sage_const_1 ]],
                   [state[_sage_const_3 ][_sage_const_3 ]] + list(state[_sage_const_3 ][:_sage_const_3 ])])


def inv_shift_rows(state):
    return matrix([state[_sage_const_0 ], [state[_sage_const_1 ][_sage_const_3 ]] + list(state[_sage_const_1 ][:_sage_const_3 ]), [state[_sage_const_2 ][_sage_const_2 ], state[_sage_const_2 ][_sage_const_3 ], state[_sage_const_2 ][_sage_const_0 ], state[_sage_const_2 ][_sage_const_1 ]],
                   list(state[_sage_const_3 ][_sage_const_1 :]) + [state[_sage_const_3 ][_sage_const_0 ]]])


def sub_bytes(state):
    """
    0   4   8   12
    1   5   9   13
    2   6   10  14
    3   7   11  15

    Sbox[0]   Sbox[4]   Sbox[8]   Sbox[12]
    Sbox[1]   Sbox[5]   Sbox[9]   Sbox[13]
    Sbox[2]   Sbox[6]   Sbox[10]  Sbox[14]
    Sbox[3]   Sbox[7]   Sbox[11]  Sbox[15]
    """
    new_state = []
    for i in xrange(state.dimensions()[_sage_const_0 ]):
        new_state.append([Sbox[state[i][j]] for j in xrange(state.dimensions()[_sage_const_1 ])])
    return matrix(new_state)


def inv_sub_bytes(state):
    new_state = []
    for i in xrange(state.dimensions()[_sage_const_0 ]):
        new_state.append([Sbox_inv[state[i][j]] for j in xrange(state.dimensions()[_sage_const_1 ])])
    return matrix(new_state)


def mix_column(col):
    b0, b1, b2, b3 = col
    d0 = mulby[_sage_const_2 ][b0] ^ mulby[_sage_const_3 ][b1] ^ b2 ^ b3
    d1 = b0 ^ mulby[_sage_const_2 ][b1] ^ mulby[_sage_const_3 ][b2] ^ b3
    d2 = b0 ^ b1 ^ mulby[_sage_const_2 ][b2] ^ mulby[_sage_const_3 ][b3]
    d3 = mulby[_sage_const_3 ][b0] ^ b1 ^ b2 ^ mulby[_sage_const_2 ][b3]
    return vector([d0, d1, d2, d3])


def mix_columns(m):
    """
    for all columns:
    |d0|   |2 3 1 1|   |c0|
    |d1| = |1 2 3 1| * |c1|
    |d2|   |1 1 2 3|   |c2|
    |d3|   |3 1 1 2|   |c3|
    """
    return matrix(map(mix_column, m.columns())).transpose()


def inverse_mix_column(col):
    b0, b1, b2, b3 = col
    d0 = mulby[_sage_const_14 ][b0] ^ mulby[_sage_const_11 ][b1] ^ mulby[_sage_const_13 ][b2] ^ mulby[_sage_const_9 ][b3]
    d1 = mulby[_sage_const_9 ][b0] ^ mulby[_sage_const_14 ][b1] ^ mulby[_sage_const_11 ][b2] ^ mulby[_sage_const_13 ][b3]
    d2 = mulby[_sage_const_13 ][b0] ^ mulby[_sage_const_9 ][b1] ^ mulby[_sage_const_14 ][b2] ^ mulby[_sage_const_11 ][b3]
    d3 = mulby[_sage_const_11 ][b0] ^ mulby[_sage_const_13 ][b1] ^ mulby[_sage_const_9 ][b2] ^ mulby[_sage_const_14 ][b3]
    return vector([d0, d1, d2, d3])


def inverse_mix_columns(m):
    return matrix(map(inverse_mix_column, m.columns()))


def key_schedule_once(key, no):
    c0 = list(key.column(_sage_const_3 )[_sage_const_1 :]) + [key.column(_sage_const_3 )[_sage_const_0 ]]
    c0 = vector([Sbox[x] for x in c0])
    c0[_sage_const_0 ] ^= Rcon[no]
    c0 = xor_vector(c0, key.column(_sage_const_0 ))

    c1 = xor_vector(c0, key.column(_sage_const_1 ))
    c2 = xor_vector(c1, key.column(_sage_const_2 ))
    c3 = xor_vector(c2, key.column(_sage_const_3 ))
    return matrix([c0, c1, c2, c3]).transpose()


def key_schedule(key):
    """
    returns 11 round keys as 4x4 matrices
    """
    round_keys = [[]] * _sage_const_11 
    round_keys[_sage_const_0 ] = key
    for no in xrange(_sage_const_1 , _sage_const_11 ):
        key = key_schedule_once(key, no)
        round_keys[no] = key
    return round_keys


def inv_key_schedule_once(key, round_no):
    c3 = xor_vector(key.column(_sage_const_2 ), key.column(_sage_const_3 ))
    c2 = xor_vector(key.column(_sage_const_1 ), key.column(_sage_const_2 ))
    c1 = xor_vector(key.column(_sage_const_0 ), key.column(_sage_const_1 ))

    c3_roted = list(c3[_sage_const_1 :]) + [c3[_sage_const_0 ]]
    c3_sub = vector([Sbox[x] for x in c3_roted])
    c3_sub[_sage_const_0 ] ^= Rcon[round_no]
    c0 = xor_vector(c3_sub, key.column(_sage_const_0 ))
    return matrix([c0, c1, c2, c3]).transpose()


def inv_key_schedule(key, round_no=_sage_const_10 ):
    """
    returns aes key from given round key
    """
    for x in xrange(round_no):
        key = inv_key_schedule_once(key, round_no - x)
    return key


def add_round_key(state, round_key):
    return xor_matrices(state, round_key)


def encrypt(state, key):
    """ Standard AES-128 encryption
    State: 4x4 matrix
    Key: 4x4 matrix
    """
    round_keys = key_schedule(key)
    # initial round
    state = add_round_key(state, round_keys[_sage_const_0 ])

    # rounds
    for round_no in xrange(_sage_const_1 , _sage_const_10 ):
        state = sub_bytes(state)
        state = shift_rows(state)
        state = mix_columns(state)
        state = add_round_key(state, round_keys[round_no])

    # final round
    state = sub_bytes(state)
    state = shift_rows(state)
    state = add_round_key(state, round_keys[-_sage_const_1 ])

    return state

def round(state, no, Tboxes, Tyboxes, TTyboxesComposed=None):
    state = shift_rows(state)

    for i in xrange(_sage_const_4 ):
        if TTyboxesComposed is not None:
            v3 = TTyboxesComposed[no][(_sage_const_4  * i)][state.column(i)[_sage_const_0 ]]
            v4 = TTyboxesComposed[no][(_sage_const_4  * i) + _sage_const_1 ][state.column(i)[_sage_const_1 ]]
            v5 = TTyboxesComposed[no][(_sage_const_4  * i) + _sage_const_2 ][state.column(i)[_sage_const_2 ]]
            v6 = TTyboxesComposed[no][(_sage_const_4  * i) + _sage_const_3 ][state.column(i)[_sage_const_3 ]]

            a = (XorBox[(_sage_const_16  * ((XorBox[(_sage_const_16  * ((v3 >> _sage_const_4 ) & _sage_const_0xf )) + ((v4 >> _sage_const_4 ) & _sage_const_0xf )]) & _sage_const_0xf )) + (
            XorBox[(_sage_const_16  * ((v5 >> _sage_const_4 ) & _sage_const_0xf )) + ((v6 >> _sage_const_4 ) & _sage_const_0xf )])] << _sage_const_4 ) | XorBox[
                    (_sage_const_16  * (XorBox[(_sage_const_16  * (v3 & _sage_const_0xf )) + (v4 & _sage_const_0xf )] & _sage_const_0xf )) + (
                    XorBox[(_sage_const_16  * (v5 & _sage_const_0xf )) + (v6 & _sage_const_0xf )] & _sage_const_0xf )]
            b = (XorBox[(_sage_const_16  * ((XorBox[(_sage_const_16  * ((v3 >> _sage_const_12 ) & _sage_const_0xf )) + ((v4 >> _sage_const_12 ) & _sage_const_0xf )]) & _sage_const_0xf )) + (
            XorBox[(_sage_const_16  * ((v5 >> _sage_const_12 ) & _sage_const_0xf )) + ((v6 >> _sage_const_12 ) & _sage_const_0xf )])] << _sage_const_4 ) | XorBox[
                    (_sage_const_16  * ((XorBox[(_sage_const_16  * ((v3 >> _sage_const_8 ) & _sage_const_0xf )) + ((v4 >> _sage_const_8 ) & _sage_const_0xf )]) & _sage_const_0xf )) + (
                    XorBox[(_sage_const_16  * ((v5 >> _sage_const_8 ) & _sage_const_0xf )) + ((v6 >> _sage_const_8 ) & _sage_const_0xf )])]
            c = (XorBox[(_sage_const_16  * ((XorBox[(_sage_const_16  * ((v3 >> _sage_const_20 ) & _sage_const_0xf )) + ((v4 >> _sage_const_20 ) & _sage_const_0xf )]) & _sage_const_0xf )) + (
            XorBox[(_sage_const_16  * ((v5 >> _sage_const_20 ) & _sage_const_0xf )) + ((v6 >> _sage_const_20 ) & _sage_const_0xf )])] << _sage_const_4 ) | XorBox[
                    (_sage_const_16  * ((XorBox[(_sage_const_16  * ((v3 >> _sage_const_16 ) & _sage_const_0xf )) + ((v4 >> _sage_const_16 ) & _sage_const_0xf )]) & _sage_const_0xf )) + (
                    XorBox[(_sage_const_16  * ((v5 >> _sage_const_16 ) & _sage_const_0xf )) + ((v6 >> _sage_const_16 ) & _sage_const_0xf )])]
            d = (XorBox[(_sage_const_16  * ((XorBox[(_sage_const_16  * ((v3 >> _sage_const_28 ) & _sage_const_0xf )) + ((v4 >> _sage_const_28 ) & _sage_const_0xf )]) & _sage_const_0xf )) + (
            XorBox[(_sage_const_16  * ((v5 >> _sage_const_28 ) & _sage_const_0xf )) + ((v6 >> _sage_const_28 ) & _sage_const_0xf )])] << _sage_const_4 ) | XorBox[
                    (_sage_const_16  * ((XorBox[(_sage_const_16  * ((v3 >> _sage_const_24 ) & _sage_const_0xf )) + ((v4 >> _sage_const_24 ) & _sage_const_0xf )]) & _sage_const_0xf )) + (
                    XorBox[(_sage_const_16  * ((v5 >> _sage_const_24 ) & _sage_const_0xf )) + ((v6 >> _sage_const_24 ) & _sage_const_0xf )])]
        else:
            v3 = Tboxes[no][(_sage_const_4  * i)][state.column(i)[_sage_const_0 ]]
            v4 = Tboxes[no][(_sage_const_4  * i) + _sage_const_1 ][state.column(i)[_sage_const_1 ]]
            v5 = Tboxes[no][(_sage_const_4  * i) + _sage_const_2 ][state.column(i)[_sage_const_2 ]]
            v6 = Tboxes[no][(_sage_const_4  * i) + _sage_const_3 ][state.column(i)[_sage_const_3 ]]

            new_column = Tyboxes[_sage_const_0 ][v3] ^ Tyboxes[_sage_const_1 ][v4] ^ Tyboxes[_sage_const_2 ][v5] ^ Tyboxes[_sage_const_3 ][v6]
            d, c, b, a = [int(x) for x in i2b(new_column, _sage_const_4  * _sage_const_8 )]
        state[:, i] = vector([a, b, c, d])

    return state


def encrypt_whitebox(state, Tboxes, Tyboxes, TTyboxesComposed=None, TTyboxFinal=None):
    """
    state: matrix(4x4), plaintext
    Tboxes: T[round_no][byte_no][x] = Sbox[x ^^ shift_rows(k[round_no][byte_no])] -> 10*16*256
    Tyboxes: Ty[byte_in_column_no][x] -> 4*256
    TTyboxesComposed: TTyboxesComposed[round_no][byte_no][x] = Ty[byte_no%4][ T[round_no][byte_no][x] ] -> 9*16*256
    TTyboxFinal: Sbox[x ^^ shift_rows(k[last_round][byte_no])], if None Tboxes[-1] is used
    """
    if TTyboxFinal is None:
        TTyboxFinal = Tboxes[-_sage_const_1 ]

    for no in xrange(_sage_const_9 ):
        state = round(state, no, Tboxes, Tyboxes, TTyboxesComposed)

    state = shift_rows(state)
    for i in xrange(_sage_const_4 ):
        state[:, i] = vector([TTyboxFinal[(i * _sage_const_4 ) + j][state[j][i]] for j in xrange(_sage_const_4 )])

    return state


def generate_tyboxes():
    Ty = []
    for i in xrange(_sage_const_4 ):
        tmp = []
        for j in xrange(_sage_const_256 ):
            mi = []
            mi.append(mulby[mix_columns_matrix[i + _sage_const_0 ]][j])
            mi.append(mulby[mix_columns_matrix[i + _sage_const_4 ]][j])
            mi.append(mulby[mix_columns_matrix[i + _sage_const_8 ]][j])
            mi.append(mulby[mix_columns_matrix[i + _sage_const_12 ]][j])
            tmp.append((mi[_sage_const_3 ] << _sage_const_24 ) | (mi[_sage_const_2 ] << _sage_const_16 ) | (mi[_sage_const_1 ] << _sage_const_8 ) | mi[_sage_const_0 ])
        Ty.append(tmp)
    return Ty


def generate_tboxes(key):
    round_keys = key_schedule(key)

    T = [[]] * _sage_const_10 
    for round_no in xrange(_sage_const_10 ):
        T[round_no] = [[]] * _sage_const_16 
        key_round = matrix_to_array(shift_rows(round_keys[round_no]))
        for byte_no in xrange(_sage_const_16 ):
            T[round_no][byte_no] = []
            for x in xrange(_sage_const_256 ):
                if round_no == _sage_const_9 :
                    T[round_no][byte_no].append(
                        Sbox[x ^ key_round[byte_no]] ^ matrix_to_array(round_keys[round_no + _sage_const_1 ])[byte_no])
                else:
                    T[round_no][byte_no].append(Sbox[x ^ key_round[byte_no]])
    return T


def compose_T_Ty_boxes(Tboxes, Tyboxes):
    TTyboxesComposed = [[]] * _sage_const_10 
    for round_no in xrange(_sage_const_10 ):
        TTyboxesComposed[round_no] = [[]] * _sage_const_16 
        for byte_no in xrange(_sage_const_16 ):
            TTyboxesComposed[round_no][byte_no] = []
            for x in xrange(_sage_const_256 ):
                TTyboxesComposed[round_no][byte_no].append(Tyboxes[byte_no % _sage_const_4 ][Tboxes[round_no][byte_no][x]])
    return TTyboxesComposed


def generate_boxes(key):
    """Returns boxes used by whitebox AES:
    T-boxes
    Ty tables
    composed T and Ty boxes
    final (last) composed T box

    for dfa attack you need only last two
    """
    T = generate_tboxes(key)
    Ty = generate_tyboxes()
    TTy_composed = compose_T_Ty_boxes(T, Ty)
    TTyboxFinal = T[-_sage_const_1 ]
    return T, Ty, TTy_composed, TTyboxFinal


def recover_key_unprotected_wbaes(TTyboxesComposed, Tyboxes):
    x = _sage_const_1 
    scrambled_key = []
    for i in xrange(_sage_const_16 ):
        value = TTyboxesComposed[_sage_const_0 ][i][x]
        for j in xrange(_sage_const_256 ):
            if value == Tyboxes[i % _sage_const_4 ][Sbox[x ^ j]]:
                scrambled_key.append(j)
                break

    if len(scrambled_key) < _sage_const_16 :
        print('error')
        return None
    key = inv_shift_rows(array_to_matrix(scrambled_key, _sage_const_4 ))
    return key


def recover_key_unprotected_wbaes_from_TTyboxFinal(TTyboxFinal, probes=_sage_const_3 ):
    key = []
    for i in xrange(_sage_const_16 ):
        Ti = TTyboxFinal[i]

        k_found_probes = set()
        for probe in xrange(probes):
            k_found = []
            x, y = randint(_sage_const_0 , _sage_const_255 ), randint(_sage_const_0 , _sage_const_255 )
            for k in xrange(_sage_const_256 ):
                if Ti[x] ^ Ti[y] == Sbox[x ^ k] ^ Sbox[y ^ k] and (probe == _sage_const_0  or k in k_found_probes):
                    k_found.append(k)

            if len(k_found_probes) == _sage_const_0 :
                k_found_probes.update(k_found)
            else:
                k_found_probes.intersection_update(k_found)

        if len(k_found_probes) != _sage_const_1 :
            print('error')
            return None
        key.append(k_found_probes.pop())

    key = inv_shift_rows(array_to_matrix(key, _sage_const_4 ))
    key = inv_key_schedule(key, _sage_const_9 )
    return key


def generate_faults(TTyboxesComposed, TTyboxFinal, group_no, trials):
    """
    group_no(int): in [0, 1, 2, 3], column in which fault will be made
    trials(int): more trials, higher probability of unique subkeys
    """
    plaintext = array_to_matrix(map(int, bytes(b'a' * _sage_const_16 )), _sage_const_4 )
    ciphertexts_with_faults = []

    for j in xrange(trials):
        # preapare fault
        fault_in_row_no = _sage_const_0 
        position = _sage_const_4  * group_no + fault_in_row_no
        fault = randint(_sage_const_0 , _sage_const_255 )
        TTyboxesComposed_copy = copy(TTyboxesComposed[_sage_const_8 ][position])
        TTyboxesComposed[_sage_const_8 ][position] = [Ty[fault_in_row_no][fault] for x in TTyboxesComposed[_sage_const_8 ][position]]
        '''
        A E I M
        B F J N
        C G K O
        D H L P

        Ty[0] <- fault in row 0 (in place of A, E, I or M)
        if fault is in any other row (position == 4*group_no + row_no), the equations in dfa need to be changed (mulby[mix_columns_matrix[(4*group_no)+2]] etc)
        for row == 1, mix_columns_matrix will be:
        2, 3, 1, 1 -> 3, 1, 1, 2
        1, 2, 3, 1 -> 2, 3, 1, 1
        1, 1, 2, 3 -> 1, 2, 3, 1
        3, 1, 1, 2 -> 1, 1, 2, 3
        '''

        # faulty encrypt_whiteboxion
        ciphertext = encrypt_whitebox(plaintext, None, None, TTyboxesComposed, TTyboxFinal)
        ciphertexts_with_faults.append(ciphertext)

        # unfault
        TTyboxesComposed[_sage_const_8 ][position] = TTyboxesComposed_copy

    # normal ciphertext
    ciphertext_original = encrypt_whitebox(plaintext, None, None, TTyboxesComposed, TTyboxFinal)

    return ciphertext_original, ciphertexts_with_faults


def dfa(TTyboxesComposed, TTyboxFinal, trials=_sage_const_5 ):
    """
    Differential fault analysis attack on whitebox AES-128

    k' = shift_rows(k)

    A ... ... ...
    B ... ... ...
    C ... ... ...
    D ... ... ...

    S[ 2.S[A+k'8,0] + 3.S[B+k'8,1] + S[C+k'8,2]   + S[D+k'8,3] + k'9,0 ] + k10,0
    ... ... ... S[ S[A+k'8,0]   + 2.S[B+k'8,1] + 3.S[C+k'8,2] + S[D+k'8,3] + k'9,7 ] + k10,7
    ... ... S[ S[A+k'8,0]   + S[B+k'8,1]   + 2.S[C+k'8,2] + 3.S[D+k'8,3] + k'9,10 ] + k10,10
    ... S[ 3.S[A+k'8,0] + S[B+k'8,1]   + S[C+k'8,2]   + 2.S[D+k'8,3] + k'9,13 ] + k10,13


    TTyboxesComposed[8][0] = Ty[0][X]  <-- fault in TTyboxesComposed

    S[ 2.X + 3.S[B+k'8,1] + S[C+k'8,2]   + S[D+k'8,3] + k'9,0 ] + k10,0
    ... ... ... S[ X   + 2.S[B+k'8,1] + 3.S[C+k'8,2] + S[D+k'8,3] + k'9,7 ] + k10,7
    ... ... S[ X   + S[B+k'8,1]   + 2.S[C+k'8,2] + 3.S[D+k'8,3] + k'9,10 ] + k10,10
    ... S[ 3.X + S[B+k'8,1]   + S[C+k'8,2]   + 2.S[D+k'8,3] + k'9,13 ] + k10,13
    """
    key = {}
    groups = [
        [_sage_const_0 , _sage_const_7 , _sage_const_10 , _sage_const_13 ],
        [_sage_const_1 , _sage_const_4 , _sage_const_11 , _sage_const_14 ],
        [_sage_const_2 , _sage_const_5 , _sage_const_8 , _sage_const_15 ],
        [_sage_const_3 , _sage_const_6 , _sage_const_9 , _sage_const_12 ]
    ]

    for group_no, group in enumerate(groups):
        print('Group no {} ({}):'.format(group_no, group))
        ciphertext_original, ciphertexts_with_faults = generate_faults(TTyboxesComposed, TTyboxFinal, group_no,
                                                                       trials=trials)
        for fault_no in xrange(len(ciphertexts_with_faults)):
            O = [matrix_to_array(ciphertext_original)[position] for position in group]
            Op = [matrix_to_array(ciphertexts_with_faults[fault_no])[position] for position in group]

            key_candidates = {x: set() for x in group}
            for Z in xrange(_sage_const_256 ):
                for Y0 in xrange(_sage_const_256 ):
                    if O[_sage_const_0 ] ^ Op[_sage_const_0 ] == Sbox[Y0] ^ Sbox[mulby[mix_columns_matrix[(_sage_const_4  * group_no) + _sage_const_0 ]][Z] ^ Y0]:
                        for Y1 in xrange(_sage_const_256 ):
                            if O[_sage_const_1 ] ^ Op[_sage_const_1 ] == Sbox[Y1] ^ Sbox[
                                                mulby[mix_columns_matrix[(_sage_const_4  * group_no) + _sage_const_1 ]][Z] ^ Y1]:
                                for Y2 in xrange(_sage_const_256 ):
                                    if O[_sage_const_2 ] ^ Op[_sage_const_2 ] == Sbox[Y2] ^ Sbox[
                                                        mulby[mix_columns_matrix[(_sage_const_4  * group_no) + _sage_const_2 ]][Z] ^ Y2]:
                                        for Y3 in xrange(_sage_const_256 ):
                                            if O[_sage_const_3 ] ^ Op[_sage_const_3 ] == Sbox[Y3] ^ Sbox[
                                                                mulby[mix_columns_matrix[(_sage_const_4  * group_no) + _sage_const_3 ]][
                                                                    Z] ^ Y3]:
                                                key_candidates[group[_sage_const_0 ]].add(O[_sage_const_0 ] ^ Sbox[Y0])
                                                key_candidates[group[_sage_const_1 ]].add(O[_sage_const_1 ] ^ Sbox[Y1])
                                                key_candidates[group[_sage_const_2 ]].add(O[_sage_const_2 ] ^ Sbox[Y2])
                                                key_candidates[group[_sage_const_3 ]].add(O[_sage_const_3 ] ^ Sbox[Y3])
            for position in group:
                if position not in key:
                    key[position] = key_candidates[position]
                else:
                    key[position].intersection_update(key_candidates[position])

    if any(len(key[position]) == _sage_const_0  for position in xrange(_sage_const_16 )):
        print('Key not recovered')
        print(key)
        return None

    if any(len(key[position]) > _sage_const_1  for position in xrange(_sage_const_16 )):
        print('Key not recovered, trying with trials={}'.format(trials + _sage_const_3 ))
        return dfa(TTyboxesComposed, TTyboxFinal, trials=trials + _sage_const_3 )

    key = array_to_matrix([key[position].pop() for position in xrange(_sage_const_16 )])
    return inv_key_schedule(key)


def boxes_to_binformat(TTyboxesComposed):
    result = ''
    for round_no in xrange(_sage_const_9 ):
        for byte_no in xrange(_sage_const_16 ):
            for value in xrange(_sage_const_256 ):
                result += i2b(TTyboxesComposed[round_no][byte_no][value], _sage_const_4  * _sage_const_8 )

    with open('TTyboxesComposed.bin', 'wb') as f:
        f.write(result)


def boxes_from_binformat():
    with open('TTyboxesComposed.bin', 'rb') as f:
        bin_boxes = f.read()

    TTyboxesComposed = []
    for round_no in xrange(_sage_const_9 ):
        TTyboxesComposed.append([])
        for byte_no in xrange(_sage_const_16 ):
            TTyboxesComposed[round_no].append([])
            for value in xrange(_sage_const_256 ):
                TTyboxesComposed[round_no][byte_no].append(b2i(bin_boxes[:_sage_const_4 ]))
                bin_boxes = bin_boxes[_sage_const_4 :]
    return TTyboxesComposed
