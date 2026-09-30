## CoreMIDI

> `/System/Library/Frameworks/CoreMIDI.framework/CoreMIDI`

```diff

-319.0.0.0.0
-  __TEXT.__text: 0x980b0
-  __TEXT.__auth_stubs: 0x1c50
-  __TEXT.__objc_methlist: 0x1220
-  __TEXT.__const: 0x9a7
+320.0.0.0.0
+  __TEXT.__text: 0xa5568
+  __TEXT.__auth_stubs: 0x1d50
+  __TEXT.__objc_methlist: 0x15a0
+  __TEXT.__const: 0x9b4
   __TEXT.__dlopen_cstrs: 0x4e
-  __TEXT.__gcc_except_tab: 0xc988
-  __TEXT.__cstring: 0x4163
-  __TEXT.__oslogstring: 0x2a36
-  __TEXT.__unwind_info: 0x39f0
-  __TEXT.__objc_classname: 0x1c0
-  __TEXT.__objc_methname: 0x29c5
-  __TEXT.__objc_methtype: 0x6e3
-  __TEXT.__objc_stubs: 0x1a80
-  __DATA_CONST.__got: 0x310
-  __DATA_CONST.__const: 0x448
-  __DATA_CONST.__objc_classlist: 0xa0
+  __TEXT.__gcc_except_tab: 0xdd48
+  __TEXT.__cstring: 0x44e7
+  __TEXT.__oslogstring: 0x2b44
+  __TEXT.__unwind_info: 0x3e90
+  __TEXT.__objc_classname: 0x1f4
+  __TEXT.__objc_methname: 0x2dd9
+  __TEXT.__objc_methtype: 0x112a
+  __TEXT.__objc_stubs: 0x2000
+  __DATA_CONST.__got: 0x320
+  __DATA_CONST.__const: 0x4e8
+  __DATA_CONST.__objc_classlist: 0xb0
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa18
-  __DATA_CONST.__objc_superrefs: 0x80
-  __AUTH_CONST.__auth_got: 0xe38
-  __AUTH_CONST.__const: 0x3818
-  __AUTH_CONST.__cfstring: 0x1a20
-  __AUTH_CONST.__objc_const: 0x2260
+  __DATA_CONST.__objc_selrefs: 0xbb0
+  __DATA_CONST.__objc_superrefs: 0x98
+  __AUTH_CONST.__auth_got: 0xeb8
+  __AUTH_CONST.__const: 0x3a40
+  __AUTH_CONST.__cfstring: 0x1a60
+  __AUTH_CONST.__objc_const: 0x2660
   __AUTH_CONST.__objc_intobj: 0x60
-  __DATA.__objc_ivar: 0x1b8
+  __AUTH.__objc_data: 0xa0
+  __DATA.__objc_ivar: 0x208
   __DATA.__data: 0x1e0
-  __DATA.__bss: 0x1380
+  __DATA.__bss: 0x13b0
   __DATA.__common: 0x188
   __DATA_DIRTY.__objc_data: 0x640
   __DATA_DIRTY.__data: 0x68

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E543736F-A031-3F6F-AAE3-03FBEAA13642
-  Functions: 2456
-  Symbols:   7319
-  CStrings:  1776
+  UUID: 1EBE09B5-4B4D-3130-8726-1B82AF9F3344
+  Functions: 2630
+  Symbols:   7863
+  CStrings:  1899
 
Symbols:
+ +[MIDICIMutableDevice description]
+ +[MIDIUMPMutableCIProfile description]
+ -[MIDI2DeviceInfo(UMPCIInternal) copyWithZone:]
+ -[MIDI2DeviceInfo(UMPCIInternal) copy]
+ -[MIDICIDevice .cxx_construct]
+ -[MIDICIDevice addProfile:]
+ -[MIDICIDevice detailsInquiry:target:completion:]
+ -[MIDICIDevice findProfileForID:]
+ -[MIDICIDevice group]
+ -[MIDICIDevice handleProcessInquiryReplyMessage:]
+ -[MIDICIDevice handleProfileDetailsReplyMessage:]
+ -[MIDICIDevice isMine]
+ -[MIDICIDevice removeProfile:]
+ -[MIDICIDevice requestProcessInquiryMessageReport:channelControllerMessages:noteDataMessages:dataControl:completion:]
+ -[MIDICIDevice sendMessage:deviceID:data:error:]
+ -[MIDICIDevice sendMessageFromDevice:withSubType:deviceID:data:error:]
+ -[MIDICIDevice sendProfileSpecificData:profileData:error:]
+ -[MIDICIDevice serverSideTransactionDictionary:]
+ -[MIDICIDevice setGroup:]
+ -[MIDICIDeviceManager .cxx_construct]
+ -[MIDICIDeviceManager addMutableDevice:]
+ -[MIDICIDeviceManager findDeviceWithMUID:]
+ -[MIDICIDeviceManager handleProcessInquiryReplyMessage:]
+ -[MIDICIDeviceManager handleProfileDetailsReplyMessage:]
+ -[MIDICIDeviceManager mutableDevices]
+ -[MIDICIDeviceManager removeMutableDevice:]
+ -[MIDICIDeviceManager setMutableDevices:]
+ -[MIDICIMutableDevice .cxx_construct]
+ -[MIDICIMutableDevice .cxx_destruct]
+ -[MIDICIMutableDevice addProfile:error:]
+ -[MIDICIMutableDevice callbackQueue]
+ -[MIDICIMutableDevice dealloc]
+ -[MIDICIMutableDevice findProfile:]
+ -[MIDICIMutableDevice handleDiscoveryInquiry:view:]
+ -[MIDICIMutableDevice handleDiscoveryReply:view:]
+ -[MIDICIMutableDevice handleEndpointInformationInquiry:view:]
+ -[MIDICIMutableDevice handleGetProperty:fromDevice:view:]
+ -[MIDICIMutableDevice handleInvalidateMUID:view:]
+ -[MIDICIMutableDevice handleNAK:view:]
+ -[MIDICIMutableDevice handleProfileDetailsInquiry:view:]
+ -[MIDICIMutableDevice handleProfileIDView:view:]
+ -[MIDICIMutableDevice handleProfileInquiry:view:]
+ -[MIDICIMutableDevice handleProfileSpecificData:fromDevice:view:]
+ -[MIDICIMutableDevice handleSysExIdentityRequest:]
+ -[MIDICIMutableDevice handleSysex:sysEx:]
+ -[MIDICIMutableDevice initWithUMPEndpointPair:functionBlock:capabilities:sysExSizeLimit:maxPERequests:profileSpecificDataCallback:messageCallback:]
+ -[MIDICIMutableDevice initWithUMPEndpointPair:functionBlock:capabilities:sysExSizeLimit:maxPERequests:queue:profileSpecificDataCallback:messageCallback:]
+ -[MIDICIMutableDevice receiveMessageViaSource:error:]
+ -[MIDICIMutableDevice registerWithServer]
+ -[MIDICIMutableDevice removeProfile:error:]
+ -[MIDICIMutableDevice respondViaSource:]
+ -[MIDICIMutableDevice sendMessageToCIDevice:withSubType:deviceID:data:error:]
+ -[MIDICIMutableDevice setCallbackQueue:]
+ -[MIDICIMutableDevice setEnabled:error:]
+ -[MIDICIMutableDevice setProfile:newState:enabledChannelCount:error:]
+ -[MIDICIMutableDevice setResourceList:error:]
+ -[MIDICIMutableDevice setupMIDIStreamObjects]
+ -[MIDIUMPCIProfile .cxx_construct]
+ -[MIDIUMPCIProfile detailsInquiryWithTarget:completion:]
+ -[MIDIUMPCIProfile initWithProfileID:name:profileType:groupOffset:firstChannel:enabledChannelCount:totalChannelCount:]
+ -[MIDIUMPCIProfile isEqual:]
+ -[MIDIUMPCIProfile ownerObjectRef]
+ -[MIDIUMPCIProfile sendProfileSpecificData:error:]
+ -[MIDIUMPCIProfile setOwnerObjectRef:]
+ -[MIDIUMPEndpoint .cxx_construct]
+ -[MIDIUMPEndpoint sendEventList:error:]
+ -[MIDIUMPEndpoint setStreamProtocol:error:]
+ -[MIDIUMPEndpointManager .cxx_construct]
+ -[MIDIUMPFunctionBlock .cxx_construct]
+ -[MIDIUMPFunctionBlock isMine]
+ -[MIDIUMPMutableCIProfile dealloc]
+ -[MIDIUMPMutableCIProfile initWithProfileID:name:profileType:groupOffset:firstChannel:enabledChannelCount:totalChannelCount:]
+ -[MIDIUMPMutableCIProfile setProfileState:enabledChannelCount:error:]
+ -[MIDIUMPMutableEndpoint .cxx_construct]
+ -[MIDIUMPMutableEndpoint dealloc]
+ -[MIDIUMPMutableEndpoint setReceiveTapBlock:]
+ -[MIDIUMPMutableEndpoint setStreamProtocol:error:]
+ -[MIDIUMPMutableFunctionBlock UMPEndpoint]
+ -[MIDIUMPMutableFunctionBlock dealloc]
+ GCC_except_table1053
+ GCC_except_table1054
+ GCC_except_table1056
+ GCC_except_table1057
+ GCC_except_table1058
+ GCC_except_table1060
+ GCC_except_table1070
+ GCC_except_table1071
+ GCC_except_table1072
+ GCC_except_table1073
+ GCC_except_table1074
+ GCC_except_table1075
+ GCC_except_table1076
+ GCC_except_table1077
+ GCC_except_table1078
+ GCC_except_table1084
+ GCC_except_table1085
+ GCC_except_table1086
+ GCC_except_table1090
+ GCC_except_table1092
+ GCC_except_table1093
+ GCC_except_table1094
+ GCC_except_table1095
+ GCC_except_table1096
+ GCC_except_table1097
+ GCC_except_table1099
+ GCC_except_table110
+ GCC_except_table1101
+ GCC_except_table1102
+ GCC_except_table1103
+ GCC_except_table1104
+ GCC_except_table1105
+ GCC_except_table1106
+ GCC_except_table1108
+ GCC_except_table1109
+ GCC_except_table1110
+ GCC_except_table1111
+ GCC_except_table1112
+ GCC_except_table1113
+ GCC_except_table1114
+ GCC_except_table1115
+ GCC_except_table1116
+ GCC_except_table1117
+ GCC_except_table1118
+ GCC_except_table1119
+ GCC_except_table1120
+ GCC_except_table1121
+ GCC_except_table1122
+ GCC_except_table1124
+ GCC_except_table1125
+ GCC_except_table1126
+ GCC_except_table1127
+ GCC_except_table1128
+ GCC_except_table1129
+ GCC_except_table1130
+ GCC_except_table1131
+ GCC_except_table1132
+ GCC_except_table1134
+ GCC_except_table1136
+ GCC_except_table1137
+ GCC_except_table1138
+ GCC_except_table1139
+ GCC_except_table114
+ GCC_except_table1140
+ GCC_except_table1141
+ GCC_except_table1142
+ GCC_except_table1143
+ GCC_except_table1145
+ GCC_except_table1146
+ GCC_except_table1147
+ GCC_except_table1154
+ GCC_except_table1158
+ GCC_except_table1164
+ GCC_except_table1170
+ GCC_except_table1178
+ GCC_except_table1185
+ GCC_except_table1193
+ GCC_except_table1195
+ GCC_except_table1204
+ GCC_except_table1211
+ GCC_except_table1227
+ GCC_except_table1248
+ GCC_except_table1252
+ GCC_except_table1253
+ GCC_except_table1254
+ GCC_except_table1255
+ GCC_except_table1264
+ GCC_except_table127
+ GCC_except_table128
+ GCC_except_table1286
+ GCC_except_table1290
+ GCC_except_table1294
+ GCC_except_table1295
+ GCC_except_table1296
+ GCC_except_table1298
+ GCC_except_table130
+ GCC_except_table1307
+ GCC_except_table131
+ GCC_except_table1312
+ GCC_except_table132
+ GCC_except_table1320
+ GCC_except_table1321
+ GCC_except_table1322
+ GCC_except_table1323
+ GCC_except_table1324
+ GCC_except_table134
+ GCC_except_table1341
+ GCC_except_table1343
+ GCC_except_table1347
+ GCC_except_table1348
+ GCC_except_table1350
+ GCC_except_table1351
+ GCC_except_table1353
+ GCC_except_table1360
+ GCC_except_table1363
+ GCC_except_table1374
+ GCC_except_table1375
+ GCC_except_table1377
+ GCC_except_table1378
+ GCC_except_table1379
+ GCC_except_table1381
+ GCC_except_table1382
+ GCC_except_table1384
+ GCC_except_table1385
+ GCC_except_table1386
+ GCC_except_table1387
+ GCC_except_table1392
+ GCC_except_table1394
+ GCC_except_table1400
+ GCC_except_table1407
+ GCC_except_table1416
+ GCC_except_table1417
+ GCC_except_table1420
+ GCC_except_table1421
+ GCC_except_table1426
+ GCC_except_table1428
+ GCC_except_table1433
+ GCC_except_table1444
+ GCC_except_table145
+ GCC_except_table1450
+ GCC_except_table1453
+ GCC_except_table1454
+ GCC_except_table1457
+ GCC_except_table1460
+ GCC_except_table1464
+ GCC_except_table1469
+ GCC_except_table1470
+ GCC_except_table1473
+ GCC_except_table1474
+ GCC_except_table1475
+ GCC_except_table1476
+ GCC_except_table1478
+ GCC_except_table1479
+ GCC_except_table1484
+ GCC_except_table1491
+ GCC_except_table1498
+ GCC_except_table1501
+ GCC_except_table1506
+ GCC_except_table1520
+ GCC_except_table1523
+ GCC_except_table153
+ GCC_except_table1532
+ GCC_except_table1534
+ GCC_except_table1536
+ GCC_except_table1539
+ GCC_except_table154
+ GCC_except_table1540
+ GCC_except_table1543
+ GCC_except_table1545
+ GCC_except_table1547
+ GCC_except_table1548
+ GCC_except_table157
+ GCC_except_table1581
+ GCC_except_table159
+ GCC_except_table1612
+ GCC_except_table1614
+ GCC_except_table1627
+ GCC_except_table1628
+ GCC_except_table163
+ GCC_except_table1630
+ GCC_except_table1631
+ GCC_except_table1651
+ GCC_except_table1652
+ GCC_except_table1653
+ GCC_except_table1668
+ GCC_except_table1669
+ GCC_except_table1670
+ GCC_except_table1671
+ GCC_except_table1674
+ GCC_except_table1683
+ GCC_except_table169
+ GCC_except_table1715
+ GCC_except_table1716
+ GCC_except_table1718
+ GCC_except_table1719
+ GCC_except_table1720
+ GCC_except_table1721
+ GCC_except_table1785
+ GCC_except_table1786
+ GCC_except_table1792
+ GCC_except_table1808
+ GCC_except_table1810
+ GCC_except_table1819
+ GCC_except_table1820
+ GCC_except_table1821
+ GCC_except_table183
+ GCC_except_table1830
+ GCC_except_table1839
+ GCC_except_table1853
+ GCC_except_table186
+ GCC_except_table1870
+ GCC_except_table1871
+ GCC_except_table1877
+ GCC_except_table188
+ GCC_except_table1881
+ GCC_except_table1882
+ GCC_except_table1884
+ GCC_except_table1885
+ GCC_except_table1886
+ GCC_except_table1887
+ GCC_except_table1888
+ GCC_except_table1889
+ GCC_except_table1890
+ GCC_except_table1891
+ GCC_except_table1892
+ GCC_except_table1894
+ GCC_except_table1899
+ GCC_except_table190
+ GCC_except_table1900
+ GCC_except_table1901
+ GCC_except_table1902
+ GCC_except_table1904
+ GCC_except_table1906
+ GCC_except_table1907
+ GCC_except_table1908
+ GCC_except_table1910
+ GCC_except_table1911
+ GCC_except_table1912
+ GCC_except_table1914
+ GCC_except_table1915
+ GCC_except_table1916
+ GCC_except_table1918
+ GCC_except_table1919
+ GCC_except_table1920
+ GCC_except_table1922
+ GCC_except_table1923
+ GCC_except_table1924
+ GCC_except_table1925
+ GCC_except_table1926
+ GCC_except_table1927
+ GCC_except_table1932
+ GCC_except_table1934
+ GCC_except_table1935
+ GCC_except_table1936
+ GCC_except_table194
+ GCC_except_table1943
+ GCC_except_table1944
+ GCC_except_table1945
+ GCC_except_table1946
+ GCC_except_table1947
+ GCC_except_table1948
+ GCC_except_table1949
+ GCC_except_table1950
+ GCC_except_table1951
+ GCC_except_table1952
+ GCC_except_table1953
+ GCC_except_table1956
+ GCC_except_table197
+ GCC_except_table1985
+ GCC_except_table1986
+ GCC_except_table1987
+ GCC_except_table199
+ GCC_except_table1993
+ GCC_except_table1994
+ GCC_except_table1995
+ GCC_except_table1996
+ GCC_except_table1997
+ GCC_except_table1999
+ GCC_except_table2000
+ GCC_except_table2001
+ GCC_except_table2006
+ GCC_except_table2018
+ GCC_except_table202
+ GCC_except_table2020
+ GCC_except_table2022
+ GCC_except_table2023
+ GCC_except_table2028
+ GCC_except_table2030
+ GCC_except_table2031
+ GCC_except_table2032
+ GCC_except_table2034
+ GCC_except_table2035
+ GCC_except_table2039
+ GCC_except_table2040
+ GCC_except_table2041
+ GCC_except_table2042
+ GCC_except_table2044
+ GCC_except_table2045
+ GCC_except_table2046
+ GCC_except_table2049
+ GCC_except_table2059
+ GCC_except_table2061
+ GCC_except_table2062
+ GCC_except_table2063
+ GCC_except_table2064
+ GCC_except_table2069
+ GCC_except_table2071
+ GCC_except_table2079
+ GCC_except_table2087
+ GCC_except_table209
+ GCC_except_table2100
+ GCC_except_table2107
+ GCC_except_table212
+ GCC_except_table2128
+ GCC_except_table2129
+ GCC_except_table2140
+ GCC_except_table2156
+ GCC_except_table2158
+ GCC_except_table2159
+ GCC_except_table2172
+ GCC_except_table2175
+ GCC_except_table2176
+ GCC_except_table2181
+ GCC_except_table2182
+ GCC_except_table2184
+ GCC_except_table2185
+ GCC_except_table2197
+ GCC_except_table2242
+ GCC_except_table2243
+ GCC_except_table2244
+ GCC_except_table2246
+ GCC_except_table2248
+ GCC_except_table2249
+ GCC_except_table2256
+ GCC_except_table2260
+ GCC_except_table2262
+ GCC_except_table2288
+ GCC_except_table229
+ GCC_except_table2325
+ GCC_except_table2327
+ GCC_except_table2331
+ GCC_except_table2332
+ GCC_except_table2336
+ GCC_except_table2338
+ GCC_except_table234
+ GCC_except_table2340
+ GCC_except_table2357
+ GCC_except_table2358
+ GCC_except_table2360
+ GCC_except_table2361
+ GCC_except_table2364
+ GCC_except_table2367
+ GCC_except_table2376
+ GCC_except_table238
+ GCC_except_table2388
+ GCC_except_table2392
+ GCC_except_table2395
+ GCC_except_table2396
+ GCC_except_table2399
+ GCC_except_table2400
+ GCC_except_table2402
+ GCC_except_table2403
+ GCC_except_table2404
+ GCC_except_table2405
+ GCC_except_table2406
+ GCC_except_table2407
+ GCC_except_table2408
+ GCC_except_table2410
+ GCC_except_table2433
+ GCC_except_table2453
+ GCC_except_table2454
+ GCC_except_table2458
+ GCC_except_table246
+ GCC_except_table2464
+ GCC_except_table2467
+ GCC_except_table2468
+ GCC_except_table247
+ GCC_except_table2475
+ GCC_except_table2476
+ GCC_except_table248
+ GCC_except_table2482
+ GCC_except_table2483
+ GCC_except_table2484
+ GCC_except_table250
+ GCC_except_table251
+ GCC_except_table2516
+ GCC_except_table2517
+ GCC_except_table2518
+ GCC_except_table2519
+ GCC_except_table252
+ GCC_except_table2521
+ GCC_except_table2524
+ GCC_except_table2525
+ GCC_except_table2527
+ GCC_except_table2528
+ GCC_except_table2529
+ GCC_except_table253
+ GCC_except_table2532
+ GCC_except_table2535
+ GCC_except_table2538
+ GCC_except_table2539
+ GCC_except_table254
+ GCC_except_table2541
+ GCC_except_table2542
+ GCC_except_table2545
+ GCC_except_table2546
+ GCC_except_table2547
+ GCC_except_table2548
+ GCC_except_table2549
+ GCC_except_table2550
+ GCC_except_table2551
+ GCC_except_table2553
+ GCC_except_table2554
+ GCC_except_table2555
+ GCC_except_table2556
+ GCC_except_table2557
+ GCC_except_table2558
+ GCC_except_table2559
+ GCC_except_table2560
+ GCC_except_table2561
+ GCC_except_table2562
+ GCC_except_table2563
+ GCC_except_table2565
+ GCC_except_table2566
+ GCC_except_table2567
+ GCC_except_table2569
+ GCC_except_table257
+ GCC_except_table2570
+ GCC_except_table2573
+ GCC_except_table2574
+ GCC_except_table2577
+ GCC_except_table258
+ GCC_except_table2585
+ GCC_except_table2587
+ GCC_except_table2588
+ GCC_except_table2589
+ GCC_except_table2590
+ GCC_except_table2591
+ GCC_except_table2592
+ GCC_except_table2593
+ GCC_except_table2594
+ GCC_except_table2595
+ GCC_except_table2596
+ GCC_except_table2597
+ GCC_except_table2599
+ GCC_except_table2600
+ GCC_except_table2601
+ GCC_except_table2602
+ GCC_except_table2603
+ GCC_except_table2606
+ GCC_except_table2607
+ GCC_except_table2608
+ GCC_except_table2609
+ GCC_except_table2610
+ GCC_except_table2612
+ GCC_except_table2613
+ GCC_except_table2614
+ GCC_except_table2617
+ GCC_except_table2618
+ GCC_except_table2619
+ GCC_except_table262
+ GCC_except_table2620
+ GCC_except_table2621
+ GCC_except_table2622
+ GCC_except_table2623
+ GCC_except_table2624
+ GCC_except_table2625
+ GCC_except_table2626
+ GCC_except_table2627
+ GCC_except_table2628
+ GCC_except_table2629
+ GCC_except_table2630
+ GCC_except_table2633
+ GCC_except_table2634
+ GCC_except_table2635
+ GCC_except_table2639
+ GCC_except_table2640
+ GCC_except_table2641
+ GCC_except_table2647
+ GCC_except_table2649
+ GCC_except_table2651
+ GCC_except_table2656
+ GCC_except_table2657
+ GCC_except_table2658
+ GCC_except_table2665
+ GCC_except_table2669
+ GCC_except_table267
+ GCC_except_table2674
+ GCC_except_table2675
+ GCC_except_table2677
+ GCC_except_table2679
+ GCC_except_table2681
+ GCC_except_table2682
+ GCC_except_table2683
+ GCC_except_table2685
+ GCC_except_table2686
+ GCC_except_table2687
+ GCC_except_table2691
+ GCC_except_table2692
+ GCC_except_table2694
+ GCC_except_table270
+ GCC_except_table273
+ GCC_except_table274
+ GCC_except_table277
+ GCC_except_table279
+ GCC_except_table285
+ GCC_except_table286
+ GCC_except_table287
+ GCC_except_table288
+ GCC_except_table289
+ GCC_except_table291
+ GCC_except_table292
+ GCC_except_table294
+ GCC_except_table295
+ GCC_except_table312
+ GCC_except_table313
+ GCC_except_table314
+ GCC_except_table316
+ GCC_except_table323
+ GCC_except_table364
+ GCC_except_table365
+ GCC_except_table381
+ GCC_except_table382
+ GCC_except_table384
+ GCC_except_table385
+ GCC_except_table386
+ GCC_except_table387
+ GCC_except_table388
+ GCC_except_table389
+ GCC_except_table390
+ GCC_except_table391
+ GCC_except_table393
+ GCC_except_table394
+ GCC_except_table395
+ GCC_except_table396
+ GCC_except_table397
+ GCC_except_table398
+ GCC_except_table399
+ GCC_except_table407
+ GCC_except_table408
+ GCC_except_table412
+ GCC_except_table414
+ GCC_except_table415
+ GCC_except_table419
+ GCC_except_table423
+ GCC_except_table424
+ GCC_except_table425
+ GCC_except_table428
+ GCC_except_table430
+ GCC_except_table433
+ GCC_except_table434
+ GCC_except_table442
+ GCC_except_table451
+ GCC_except_table454
+ GCC_except_table457
+ GCC_except_table460
+ GCC_except_table463
+ GCC_except_table464
+ GCC_except_table465
+ GCC_except_table468
+ GCC_except_table497
+ GCC_except_table501
+ GCC_except_table506
+ GCC_except_table517
+ GCC_except_table520
+ GCC_except_table523
+ GCC_except_table524
+ GCC_except_table525
+ GCC_except_table526
+ GCC_except_table531
+ GCC_except_table535
+ GCC_except_table536
+ GCC_except_table543
+ GCC_except_table544
+ GCC_except_table546
+ GCC_except_table547
+ GCC_except_table557
+ GCC_except_table558
+ GCC_except_table561
+ GCC_except_table562
+ GCC_except_table563
+ GCC_except_table570
+ GCC_except_table576
+ GCC_except_table577
+ GCC_except_table581
+ GCC_except_table592
+ GCC_except_table596
+ GCC_except_table597
+ GCC_except_table598
+ GCC_except_table599
+ GCC_except_table600
+ GCC_except_table603
+ GCC_except_table610
+ GCC_except_table620
+ GCC_except_table621
+ GCC_except_table622
+ GCC_except_table625
+ GCC_except_table626
+ GCC_except_table629
+ GCC_except_table65
+ GCC_except_table70
+ GCC_except_table71
+ GCC_except_table72
+ GCC_except_table73
+ GCC_except_table74
+ GCC_except_table75
+ GCC_except_table763
+ GCC_except_table767
+ GCC_except_table768
+ GCC_except_table769
+ GCC_except_table770
+ GCC_except_table772
+ GCC_except_table774
+ GCC_except_table775
+ GCC_except_table777
+ GCC_except_table779
+ GCC_except_table781
+ GCC_except_table782
+ GCC_except_table784
+ GCC_except_table790
+ GCC_except_table792
+ GCC_except_table794
+ GCC_except_table817
+ GCC_except_table82
+ GCC_except_table826
+ GCC_except_table827
+ GCC_except_table83
+ GCC_except_table842
+ GCC_except_table849
+ GCC_except_table85
+ GCC_except_table851
+ GCC_except_table852
+ GCC_except_table853
+ GCC_except_table855
+ GCC_except_table890
+ GCC_except_table891
+ GCC_except_table90
+ GCC_except_table904
+ GCC_except_table907
+ GCC_except_table915
+ GCC_except_table92
+ GCC_except_table927
+ GCC_except_table929
+ GCC_except_table93
+ GCC_except_table935
+ GCC_except_table936
+ GCC_except_table937
+ GCC_except_table941
+ GCC_except_table942
+ GCC_except_table943
+ GCC_except_table960
+ GCC_except_table965
+ GCC_except_table966
+ GCC_except_table967
+ GCC_except_table98
+ GCC_except_table99
+ GCC_except_table998
+ _OBJC_CLASS_$_MIDICIMutableDevice
+ _OBJC_CLASS_$_MIDIUMPMutableCIProfile
+ _OBJC_CLASS_$_NSPointerArray
+ _OBJC_IVAR_$_MIDICIDevice._activeTransactions
+ _OBJC_IVAR_$_MIDICIDevice._endpoint
+ _OBJC_IVAR_$_MIDICIDevice._group
+ _OBJC_IVAR_$_MIDICIDevice._isEnabled
+ _OBJC_IVAR_$_MIDICIDevice._ownerClientRef
+ _OBJC_IVAR_$_MIDICIDevice._resourceList
+ _OBJC_IVAR_$_MIDICIDevice.mMutex
+ _OBJC_IVAR_$_MIDICIDeviceManager._mutableDevices
+ _OBJC_IVAR_$_MIDICIDeviceManager.mMutex
+ _OBJC_IVAR_$_MIDICIMutableDevice._callbackQueue
+ _OBJC_IVAR_$_MIDICIMutableDevice._messageCallback
+ _OBJC_IVAR_$_MIDICIMutableDevice._messenger
+ _OBJC_IVAR_$_MIDICIMutableDevice._profileSpecificDataCallback
+ _OBJC_IVAR_$_MIDICIMutableDevice._sysexCollector
+ _OBJC_IVAR_$_MIDIUMPCIProfile._ownerClientRef
+ _OBJC_IVAR_$_MIDIUMPCIProfile._ownerObjectRef
+ _OBJC_IVAR_$_MIDIUMPCIProfile.mMutex
+ _OBJC_IVAR_$_MIDIUMPEndpoint._ownerClientRef
+ _OBJC_IVAR_$_MIDIUMPEndpoint.mMutex
+ _OBJC_IVAR_$_MIDIUMPEndpointManager.mMutex
+ _OBJC_IVAR_$_MIDIUMPFunctionBlock._ownerClientRef
+ _OBJC_IVAR_$_MIDIUMPFunctionBlock.mMutex
+ _OBJC_IVAR_$_MIDIUMPMutableEndpoint._callbackData
+ _OBJC_IVAR_$_MIDIUMPMutableEndpoint._callbackMutex
+ _OBJC_METACLASS_$_MIDICIMutableDevice
+ _OBJC_METACLASS_$_MIDIUMPMutableCIProfile
+ _UMPCIObjectDispose
+ _UMPCIServerSideMIDICITransaction
+ __OBJC_$_CLASS_METHODS_MIDICIMutableDevice
+ __OBJC_$_CLASS_METHODS_MIDIUMPMutableCIProfile
+ __OBJC_$_INSTANCE_METHODS_MIDICIMutableDevice
+ __OBJC_$_INSTANCE_METHODS_MIDIUMPMutableCIProfile
+ __OBJC_$_INSTANCE_VARIABLES_MIDICIMutableDevice
+ __OBJC_$_PROP_LIST_MIDICIMutableDevice
+ __OBJC_CLASS_RO_$_MIDICIMutableDevice
+ __OBJC_CLASS_RO_$_MIDIUMPMutableCIProfile
+ __OBJC_METACLASS_RO_$_MIDICIMutableDevice
+ __OBJC_METACLASS_RO_$_MIDIUMPMutableCIProfile
+ __UMPCIServerSideMIDICITransaction
+ __XUMPCIServerSideMIDICITransaction
+ __Z12cf_serializeIPK8__CFDataEP6NSDataRKT_
+ __Z14cf_deserializeIPK8__CFDataLb1EEDaNSt3__14spanIKhLm18446744073709551615EEE
+ __Z14sendUMPMessagejPK13MIDIEventList
+ __Z17OSStatusToNSErroriPU15__autoreleasingP7NSError
+ __Z20deviceInfoToIdentityP15MIDI2DeviceInfo
+ __Z24NSNumberArrayToProfileIDPK7NSArrayIP8NSNumberE
+ __ZGVZ14sendUMPMessagejPK13MIDIEventListE4port
+ __ZL20kAppleDeviceIdentity
+ __ZN10applesauce2CF7details23find_at_key_or_optionalINSt3__16vectorIyNS3_9allocatorIyEEEERKPKcEENS3_8optionalIT_EEPK14__CFDictionaryOT0_NS1_15counterpart_tagE
+ __ZN10applesauce2CF7details23find_at_key_or_optionalIhRKPKcEENSt3__18optionalIT_EEPK14__CFDictionaryOT0_NS1_15counterpart_tagE
+ __ZN12MIDIEndpoint11SetPropertyEPK10__CFStringPKv
+ __ZN20MIDIServerXPC_Server32umpciServerSideMIDICITransactionERKN4swix4dataE
+ __ZN25ProcessInquiryTransaction6isTypeE23InternalTransactionType
+ __ZN25ProcessInquiryTransaction7timeoutER18UMPCIServerContext
+ __ZN25ProcessInquiryTransaction8completeER18UMPCIServerContextb
+ __ZN25ProcessInquiryTransactionD0Ev
+ __ZN25ProcessInquiryTransactionD1Ev
+ __ZN25ProfileDetailsTransaction6isTypeE23InternalTransactionType
+ __ZN25ProfileDetailsTransaction7timeoutER18UMPCIServerContext
+ __ZN25ProfileDetailsTransaction8completeER18UMPCIServerContextbPKvm
+ __ZN25ProfileDetailsTransactionD0Ev
+ __ZN25ProfileDetailsTransactionD1Ev
+ __ZN4MIDI23ChunkedEventListEmitterIZZ153-[MIDICIMutableDevice initWithUMPEndpointPair:functionBlock:capabilities:sysExSizeLimit:maxPERequests:queue:profileSpecificDataCallback:messageCallback:]EUb_E3$_1E5flushEv
+ __ZN4MIDIL13_gMessageSizeE.1962
+ __ZN4midi15universal_sysex14identity_replyC1ERKNS_15device_identityE
+ __ZN4midi2ci16make_nak_messageERKNS_23capability_inquiry_viewEhhPhRKNSt3__117basic_string_viewIcNS5_11char_traitsIcEEEE
+ __ZN4midi2ci2asINS0_20profile_inquiry_viewEEENSt3__18optionalIT_EERKNS_6sysex7E
+ __ZN4midi2ci2asINS0_26profile_details_reply_viewEEENSt3__18optionalIT_EERKNS_6sysex7E
+ __ZN4midi2ci2asINS0_26profile_specific_data_viewEEENSt3__18optionalIT_EERKNS_6sysex7E
+ __ZN4midi2ci2asINS0_28midi_message_report_end_viewEEENSt3__18optionalIT_EERKNS_6sysex7E
+ __ZN4midi2ci2asINS0_28profile_details_inquiry_viewEEENSt3__18optionalIT_EERKNS_6sysex7E
+ __ZN4midi2ci2asINS0_30midi_message_report_reply_viewEEENSt3__18optionalIT_EERKNS_6sysex7E
+ __ZN4midi2ci2asINS0_8nak_viewEEENSt3__18optionalIT_EERKNS_6sysex7E
+ __ZN4midi2ci7messageC1Ehjjh
+ __ZN4midi2ci9discovery22make_discovery_messageEhjjRKNS_15device_identityEhjh
+ __ZN5caulk10concurrent26lf_read_synchronized_writeIN10applesauce8dispatch2v15blockIFvPK13MIDIEventListPvEEEEaSESB_
+ __ZN5caulk10concurrent7details15rt_message_callIZZZ153-[MIDICIMutableDevice initWithUMPEndpointPair:functionBlock:capabilities:sysExSizeLimit:maxPERequests:queue:profileSpecificDataCallback:messageCallback:]EUb_ENK3$_1clEPK13MIDIEventListEUlvE_JEE10rt_cleanupD1Ev
+ __ZN5caulk10concurrent7details15rt_message_callIZZZ153-[MIDICIMutableDevice initWithUMPEndpointPair:functionBlock:capabilities:sysExSizeLimit:maxPERequests:queue:profileSpecificDataCallback:messageCallback:]EUb_ENK3$_1clEPK13MIDIEventListEUlvE_JEE7performEv
+ __ZN5caulk10concurrent7details15rt_message_callIZZZ153-[MIDICIMutableDevice initWithUMPEndpointPair:functionBlock:capabilities:sysExSizeLimit:maxPERequests:queue:profileSpecificDataCallback:messageCallback:]EUb_ENK3$_1clEPK13MIDIEventListEUlvE_JEED0Ev
+ __ZN5caulk10concurrent7details15rt_message_callIZZZ153-[MIDICIMutableDevice initWithUMPEndpointPair:functionBlock:capabilities:sysExSizeLimit:maxPERequests:queue:profileSpecificDataCallback:messageCallback:]EUb_ENK3$_1clEPK13MIDIEventListEUlvE_JEED1Ev
+ __ZN5caulk10concurrent7details23lf_read_sync_write_impl10end_mutateEj
+ __ZN5caulk10concurrent7details23lf_read_sync_write_impl12begin_mutateEv
+ __ZN5caulk10concurrent7details23lf_read_sync_write_implC1Ev
+ __ZN5caulk10concurrent7messageD2Ev
+ __ZN5caulk10concurrent9messenger7enqueueERNS0_7messageE
+ __ZN5caulk10concurrent9messengerC1ENS1_15thread_strategyERKNS_6thread10attributesE
+ __ZN5caulk10concurrent9messengerD1Ev
+ __ZN5caulk23rt_safe_memory_resource11rt_allocateEmm
+ __ZN5caulk23rt_safe_memory_resource13rt_deallocateEPvmm
+ __ZN5caulk24g_realtime_safe_resourceE
+ __ZN6MIDICI13DeviceManager17removeTransactionEPK21InternalCITransaction
+ __ZN6MIDICI13DeviceManager21isDiscoveryFromServerEN4midi23capability_inquiry_viewE
+ __ZN6MIDICI13DeviceManager25handleProfileDetailsReplyEPNS_6DeviceEN4midi2ci26profile_details_reply_viewEj
+ __ZN6MIDICI13DeviceManager28findFirstTransactionMatchingI25ProcessInquiryTransactionEEPT_NSt3__18functionIFbS4_EEE
+ __ZN6MIDICI13DeviceManager31handleProcessInquiryReportEndedEPNS_6DeviceEjj
+ __ZN6MIDICI13DeviceManager31handleProcessInquiryReportReplyEPNS_6DeviceEN4midi2ci30midi_message_report_reply_viewEj
+ __ZN6MIDICI14SysexCollector4feedEPK13MIDIEventList
+ __ZN6MIDICI14SysexCollectorC1ENSt3__18functionIFvhRKN4midi6sysex7EEEE
+ __ZN6MIDICI6DeviceD2Ev
+ __ZN9MIGClient32UMPCIServerSideMIDICITransactionEPK14__CFDictionaryPS2_
+ __ZN9XPCClient32UMPCIServerSideMIDICITransactionEPK14__CFDictionaryPS2_
+ __ZNK12MIDIEndpoint17GetPairedEndpointEv
+ __ZNK4midi6sysex720make_device_identityEm
+ __ZNK5caulk10concurrent7details23lf_read_sync_write_impl10end_accessEv
+ __ZNK5caulk10concurrent7details23lf_read_sync_write_impl12begin_accessEv
+ __ZNKSt3__110__function6__funcIZ45-[MIDICIMutableDevice setupMIDIStreamObjects]E3$_3NS_9allocatorIS2_EEFvhRKN4midi6sysex7EEE7__cloneEPNS0_6__baseIS9_EE
+ __ZNKSt3__110__function6__funcIZ45-[MIDICIMutableDevice setupMIDIStreamObjects]E3$_3NS_9allocatorIS2_EEFvhRKN4midi6sysex7EEE7__cloneEv
+ __ZNKSt3__110__function6__funcIZN6MIDICI13DeviceManager21performProcessInquiryERKN10applesauce2CF13DictionaryRefENS5_9ObjectRefIP14__CFDictionaryEEE3$_0NS_9allocatorISD_EEFvvEE7__cloneEPNS0_6__baseISG_EE
+ __ZNKSt3__110__function6__funcIZN6MIDICI13DeviceManager21performProcessInquiryERKN10applesauce2CF13DictionaryRefENS5_9ObjectRefIP14__CFDictionaryEEE3$_0NS_9allocatorISD_EEFvvEE7__cloneEv
+ __ZNKSt3__110__function6__funcIZN6MIDICI13DeviceManager25handleProfileDetailsReplyEPNS2_6DeviceEN4midi2ci26profile_details_reply_viewEjE3$_0NS_9allocatorIS9_EEFbP25ProfileDetailsTransactionEE7__cloneEPNS0_6__baseISE_EE
+ __ZNKSt3__110__function6__funcIZN6MIDICI13DeviceManager25handleProfileDetailsReplyEPNS2_6DeviceEN4midi2ci26profile_details_reply_viewEjE3$_0NS_9allocatorIS9_EEFbP25ProfileDetailsTransactionEE7__cloneEv
+ __ZNKSt3__110__function6__funcIZN6MIDICI13DeviceManager31handleProcessInquiryReportEndedEPNS2_6DeviceEjjE3$_0NS_9allocatorIS6_EEFbP25ProcessInquiryTransactionEE7__cloneEPNS0_6__baseISB_EE
+ __ZNKSt3__110__function6__funcIZN6MIDICI13DeviceManager31handleProcessInquiryReportEndedEPNS2_6DeviceEjjE3$_0NS_9allocatorIS6_EEFbP25ProcessInquiryTransactionEE7__cloneEv
+ __ZNKSt3__110__function6__funcIZN6MIDICI13DeviceManager31handleProcessInquiryReportReplyEPNS2_6DeviceEN4midi2ci30midi_message_report_reply_viewEjE3$_0NS_9allocatorIS9_EEFbP25ProcessInquiryTransactionEE7__cloneEPNS0_6__baseISE_EE
+ __ZNKSt3__110__function6__funcIZN6MIDICI13DeviceManager31handleProcessInquiryReportReplyEPNS2_6DeviceEN4midi2ci30midi_message_report_reply_viewEjE3$_0NS_9allocatorIS9_EEFbP25ProcessInquiryTransactionEE7__cloneEv
+ __ZNKSt3__114default_deleteI25ProcessInquiryTransactionEclB8ne200100EPS1_
+ __ZNSt3__110__function12__value_funcIFbP25ProcessInquiryTransactionEED2B8ne200100Ev
+ __ZNSt3__110__function12__value_funcIFbP25ProfileDetailsTransactionEED2B8ne200100Ev
+ __ZNSt3__110__function6__funcIZ45-[MIDICIMutableDevice setupMIDIStreamObjects]E3$_3NS_9allocatorIS2_EEFvhRKN4midi6sysex7EEE18destroy_deallocateEv
+ __ZNSt3__110__function6__funcIZ45-[MIDICIMutableDevice setupMIDIStreamObjects]E3$_3NS_9allocatorIS2_EEFvhRKN4midi6sysex7EEE7destroyEv
+ __ZNSt3__110__function6__funcIZ45-[MIDICIMutableDevice setupMIDIStreamObjects]E3$_3NS_9allocatorIS2_EEFvhRKN4midi6sysex7EEED0Ev
+ __ZNSt3__110__function6__funcIZ45-[MIDICIMutableDevice setupMIDIStreamObjects]E3$_3NS_9allocatorIS2_EEFvhRKN4midi6sysex7EEED1Ev
+ __ZNSt3__110__function6__funcIZ45-[MIDICIMutableDevice setupMIDIStreamObjects]E3$_3NS_9allocatorIS2_EEFvhRKN4midi6sysex7EEEclEOhS8_
+ __ZNSt3__110__function6__funcIZN6MIDICI13DeviceManager21performProcessInquiryERKN10applesauce2CF13DictionaryRefENS5_9ObjectRefIP14__CFDictionaryEEE3$_0NS_9allocatorISD_EEFvvEE18destroy_deallocateEv
+ __ZNSt3__110__function6__funcIZN6MIDICI13DeviceManager21performProcessInquiryERKN10applesauce2CF13DictionaryRefENS5_9ObjectRefIP14__CFDictionaryEEE3$_0NS_9allocatorISD_EEFvvEE7destroyEv
+ __ZNSt3__110__function6__funcIZN6MIDICI13DeviceManager21performProcessInquiryERKN10applesauce2CF13DictionaryRefENS5_9ObjectRefIP14__CFDictionaryEEE3$_0NS_9allocatorISD_EEFvvEED0Ev
+ __ZNSt3__110__function6__funcIZN6MIDICI13DeviceManager21performProcessInquiryERKN10applesauce2CF13DictionaryRefENS5_9ObjectRefIP14__CFDictionaryEEE3$_0NS_9allocatorISD_EEFvvEED1Ev
+ __ZNSt3__110__function6__funcIZN6MIDICI13DeviceManager21performProcessInquiryERKN10applesauce2CF13DictionaryRefENS5_9ObjectRefIP14__CFDictionaryEEE3$_0NS_9allocatorISD_EEFvvEEclEv
+ __ZNSt3__110__function6__funcIZN6MIDICI13DeviceManager25handleProfileDetailsReplyEPNS2_6DeviceEN4midi2ci26profile_details_reply_viewEjE3$_0NS_9allocatorIS9_EEFbP25ProfileDetailsTransactionEE18destroy_deallocateEv
+ __ZNSt3__110__function6__funcIZN6MIDICI13DeviceManager25handleProfileDetailsReplyEPNS2_6DeviceEN4midi2ci26profile_details_reply_viewEjE3$_0NS_9allocatorIS9_EEFbP25ProfileDetailsTransactionEE7destroyEv
+ __ZNSt3__110__function6__funcIZN6MIDICI13DeviceManager25handleProfileDetailsReplyEPNS2_6DeviceEN4midi2ci26profile_details_reply_viewEjE3$_0NS_9allocatorIS9_EEFbP25ProfileDetailsTransactionEED0Ev
+ __ZNSt3__110__function6__funcIZN6MIDICI13DeviceManager25handleProfileDetailsReplyEPNS2_6DeviceEN4midi2ci26profile_details_reply_viewEjE3$_0NS_9allocatorIS9_EEFbP25ProfileDetailsTransactionEED1Ev
+ __ZNSt3__110__function6__funcIZN6MIDICI13DeviceManager25handleProfileDetailsReplyEPNS2_6DeviceEN4midi2ci26profile_details_reply_viewEjE3$_0NS_9allocatorIS9_EEFbP25ProfileDetailsTransactionEEclEOSD_
+ __ZNSt3__110__function6__funcIZN6MIDICI13DeviceManager31handleProcessInquiryReportEndedEPNS2_6DeviceEjjE3$_0NS_9allocatorIS6_EEFbP25ProcessInquiryTransactionEE18destroy_deallocateEv
+ __ZNSt3__110__function6__funcIZN6MIDICI13DeviceManager31handleProcessInquiryReportEndedEPNS2_6DeviceEjjE3$_0NS_9allocatorIS6_EEFbP25ProcessInquiryTransactionEE7destroyEv
+ __ZNSt3__110__function6__funcIZN6MIDICI13DeviceManager31handleProcessInquiryReportEndedEPNS2_6DeviceEjjE3$_0NS_9allocatorIS6_EEFbP25ProcessInquiryTransactionEED0Ev
+ __ZNSt3__110__function6__funcIZN6MIDICI13DeviceManager31handleProcessInquiryReportEndedEPNS2_6DeviceEjjE3$_0NS_9allocatorIS6_EEFbP25ProcessInquiryTransactionEED1Ev
+ __ZNSt3__110__function6__funcIZN6MIDICI13DeviceManager31handleProcessInquiryReportEndedEPNS2_6DeviceEjjE3$_0NS_9allocatorIS6_EEFbP25ProcessInquiryTransactionEEclEOSA_
+ __ZNSt3__110__function6__funcIZN6MIDICI13DeviceManager31handleProcessInquiryReportReplyEPNS2_6DeviceEN4midi2ci30midi_message_report_reply_viewEjE3$_0NS_9allocatorIS9_EEFbP25ProcessInquiryTransactionEE18destroy_deallocateEv
+ __ZNSt3__110__function6__funcIZN6MIDICI13DeviceManager31handleProcessInquiryReportReplyEPNS2_6DeviceEN4midi2ci30midi_message_report_reply_viewEjE3$_0NS_9allocatorIS9_EEFbP25ProcessInquiryTransactionEE7destroyEv
+ __ZNSt3__110__function6__funcIZN6MIDICI13DeviceManager31handleProcessInquiryReportReplyEPNS2_6DeviceEN4midi2ci30midi_message_report_reply_viewEjE3$_0NS_9allocatorIS9_EEFbP25ProcessInquiryTransactionEED0Ev
+ __ZNSt3__110__function6__funcIZN6MIDICI13DeviceManager31handleProcessInquiryReportReplyEPNS2_6DeviceEN4midi2ci30midi_message_report_reply_viewEjE3$_0NS_9allocatorIS9_EEFbP25ProcessInquiryTransactionEED1Ev
+ __ZNSt3__110__function6__funcIZN6MIDICI13DeviceManager31handleProcessInquiryReportReplyEPNS2_6DeviceEN4midi2ci30midi_message_report_reply_viewEjE3$_0NS_9allocatorIS9_EEFbP25ProcessInquiryTransactionEEclEOSD_
+ __ZNSt3__110unique_ptrIN5caulk10concurrent9messengerENS_14default_deleteIS3_EEE5resetB8ne200100EPS3_
+ __ZNSt3__114__split_bufferI18CIAsyncTransactionRNS_9allocatorIS1_EEED2Ev
+ __ZNSt3__123__optional_storage_baseINS_4pairIU8__strongP12MIDICIDeviceU8__strongP16MIDIUMPCIProfileEELb0EE13__assign_fromB8ne200100INS_27__optional_move_assign_baseIS8_Lb0EEEEEvOT_
+ __ZNSt3__16vectorI18CIAsyncTransactionNS_9allocatorIS1_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorI18CIAsyncTransactionNS_9allocatorIS1_EEE22__base_destruct_at_endB8ne200100EPS1_
+ __ZNSt3__16vectorI18CIAsyncTransactionNS_9allocatorIS1_EEE24__emplace_back_slow_pathIJS1_EEEPS1_DpOT_
+ __ZNSt3__16vectorINS_10unique_ptrI21InternalCITransactionNS_14default_deleteIS2_EEEENS_9allocatorIS5_EEE16__destroy_vectorclB8ne200100Ev
+ __ZNSt3__16vectorINS_10unique_ptrI21InternalCITransactionNS_14default_deleteIS2_EEEENS_9allocatorIS5_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorINS_10unique_ptrI21InternalCITransactionNS_14default_deleteIS2_EEEENS_9allocatorIS5_EEE5eraseENS_11__wrap_iterIPKS5_EESC_
+ __ZNSt3__16vectorINS_10unique_ptrI21InternalCITransactionNS_14default_deleteIS2_EEEENS_9allocatorIS5_EEE9push_backB8ne200100EOS5_
+ __ZNSt3__16vectorIP10MIDISourceNS_9allocatorIS2_EEE16__init_with_sizeB8ne200100IPS2_S7_EEvT_T0_m
+ __ZNSt3__16vectorISt4byteNS_9allocatorIS1_EEE20__throw_length_errorB8ne200100Ev
+ __ZTV25ProcessInquiryTransaction
+ __ZTV25ProfileDetailsTransaction
+ __ZTVN5caulk10concurrent7details15rt_message_callIZZZ153-[MIDICIMutableDevice initWithUMPEndpointPair:functionBlock:capabilities:sysExSizeLimit:maxPERequests:queue:profileSpecificDataCallback:messageCallback:]EUb_ENK3$_1clEPK13MIDIEventListEUlvE_JEEE
+ __ZTVNSt3__110__function6__funcIZ45-[MIDICIMutableDevice setupMIDIStreamObjects]E3$_3NS_9allocatorIS2_EEFvhRKN4midi6sysex7EEEE
+ __ZTVNSt3__110__function6__funcIZN6MIDICI13DeviceManager21performProcessInquiryERKN10applesauce2CF13DictionaryRefENS5_9ObjectRefIP14__CFDictionaryEEE3$_0NS_9allocatorISD_EEFvvEEE
+ __ZTVNSt3__110__function6__funcIZN6MIDICI13DeviceManager25handleProfileDetailsReplyEPNS2_6DeviceEN4midi2ci26profile_details_reply_viewEjE3$_0NS_9allocatorIS9_EEFbP25ProfileDetailsTransactionEEE
+ __ZTVNSt3__110__function6__funcIZN6MIDICI13DeviceManager31handleProcessInquiryReportEndedEPNS2_6DeviceEjjE3$_0NS_9allocatorIS6_EEFbP25ProcessInquiryTransactionEEE
+ __ZTVNSt3__110__function6__funcIZN6MIDICI13DeviceManager31handleProcessInquiryReportReplyEPNS2_6DeviceEN4midi2ci30midi_message_report_reply_viewEjE3$_0NS_9allocatorIS9_EEFbP25ProcessInquiryTransactionEEE
+ __ZZ14sendUMPMessagejPK13MIDIEventListE4port
+ __ZZ23SysexMessageToEventListIZ14sendUMPMessagejhRKN4midi6sysex7EE3$_0EvhS3_T_ENKUlRKNS0_12data_messageEE_clES8_
+ __ZZ23SysexMessageToEventListIZ53-[MIDICIMutableDevice receiveMessageViaSource:error:]E3$_2EvhRKN4midi6sysex7ET_ENKUlRKNS1_12data_messageEE_clES8_
+ __ZZN14MIDIStringDumpL8hexBytesENSt3__14spanIKhLm18446744073709551615EEEE3hex.2002
+ ___101-[MIDIUMPMutableEndpoint initWithName:deviceInfo:productInstanceID:MIDIProtocol:destinationCallback:]_block_invoke
+ ___153-[MIDICIMutableDevice initWithUMPEndpointPair:functionBlock:capabilities:sysExSizeLimit:maxPERequests:queue:profileSpecificDataCallback:messageCallback:]_block_invoke
+ ___41-[MIDICIMutableDevice handleSysex:sysEx:]_block_invoke
+ ___65-[MIDICIMutableDevice handleProfileSpecificData:fromDevice:view:]_block_invoke
+ ___block_descriptor_40_ea8_32r_e59_v24?0r^{MIDIEventList=iI[1{MIDIEventPacket=QI[64I]}]}8^v16lr32l8
+ ___block_descriptor_56_ea8_32bs_e59_v24?0r^{MIDIEventList=iI[1{MIDIEventPacket=QI[64I]}]}8^v16ls32l8
+ ___block_descriptor_64_ea8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_descriptor_81_ea8_32s40s48s56r_e5_v8?0lr56l8s32l8s40l8s48l8
+ ___block_descriptor_tmp.10.255
+ ___block_descriptor_tmp.1582
+ ___block_descriptor_tmp.1938
+ ___block_descriptor_tmp.2044
+ ___block_descriptor_tmp.273
+ ___block_descriptor_tmp.3046
+ ___block_descriptor_tmp.3165
+ ___block_descriptor_tmp.3874
+ ___block_descriptor_tmp.7.289
+ ___block_descriptor_tmp.8.290
+ ___block_literal_global.1015
+ ___block_literal_global.1115
+ ___block_literal_global.1518
+ ___block_literal_global.274
+ _objc_copyWeak
+ _objc_initWeak
+ _objc_moveWeak
+ _objc_msgSend$addMutableDevice:
+ _objc_msgSend$addPointer:
+ _objc_msgSend$allocWithZone:
+ _objc_msgSend$arrayByAddingObject:
+ _objc_msgSend$arrayWithArray:
+ _objc_msgSend$copyWithZone:
+ _objc_msgSend$detailsInquiry:target:completion:
+ _objc_msgSend$findDeviceWithMUID:
+ _objc_msgSend$findProfileForID:
+ _objc_msgSend$firstGroup
+ _objc_msgSend$group
+ _objc_msgSend$handleDiscoveryInquiry:view:
+ _objc_msgSend$handleDiscoveryReply:view:
+ _objc_msgSend$handleEndpointInformationInquiry:view:
+ _objc_msgSend$handleGetProperty:fromDevice:view:
+ _objc_msgSend$handleInvalidateMUID:view:
+ _objc_msgSend$handleNAK:view:
+ _objc_msgSend$handleProcessInquiryReplyMessage:
+ _objc_msgSend$handleProfileDetailsInquiry:view:
+ _objc_msgSend$handleProfileDetailsReplyMessage:
+ _objc_msgSend$handleProfileIDView:view:
+ _objc_msgSend$handleProfileInquiry:view:
+ _objc_msgSend$handleProfileSpecificData:fromDevice:view:
+ _objc_msgSend$handleSysExIdentityRequest:
+ _objc_msgSend$handleSysex:sysEx:
+ _objc_msgSend$initWithArray:
+ _objc_msgSend$initWithProfileID:name:profileType:groupOffset:firstChannel:enabledChannelCount:totalChannelCount:
+ _objc_msgSend$initWithUMPEndpointPair:functionBlock:capabilities:sysExSizeLimit:maxPERequests:queue:profileSpecificDataCallback:messageCallback:
+ _objc_msgSend$isMine
+ _objc_msgSend$ownerObjectRef
+ _objc_msgSend$pointerAtIndex:
+ _objc_msgSend$productInstanceID
+ _objc_msgSend$receiveBlock
+ _objc_msgSend$receiveMessageViaSource:error:
+ _objc_msgSend$removeMutableDevice:
+ _objc_msgSend$removePointerAtIndex:
+ _objc_msgSend$sendEventList:error:
+ _objc_msgSend$sendMessageToCIDevice:withSubType:deviceID:data:error:
+ _objc_msgSend$sendProfileSpecificData:profileData:error:
+ _objc_msgSend$serverSideTransactionDictionary:
+ _objc_msgSend$setGroup:
+ _objc_msgSend$setProfileState:enabledChannelCount:error:
+ _objc_msgSend$setReceiveTapBlock:
+ _objc_msgSend$setupMIDIStreamObjects
+ _objc_msgSend$weakObjectsPointerArray
+ _objc_retain_x4
+ _objc_retain_x6
- -[MIDICIDeviceManager profiles]
- -[MIDICIDeviceManager setProfiles:]
- -[MIDIUMPCIProfile initWithProfileID:name:type:firstGroup:firstChannel:enabledChannelCount:totalChannelCount:]
- -[MIDIUMPCIProfile setIsMine:]
- -[MIDIUMPEndpoint setIsMine:]
- -[MIDIUMPMutableEndpoint changeStreamProtocol:]
- -[MIDIUMPMutableEndpoint disableFunctionBlock:]
- -[MIDIUMPMutableEndpoint enableFunctionBlock:]
- -[MIDIUMPMutableFunctionBlock setFunctionBlockID:]
- GCC_except_table100
- GCC_except_table1009
- GCC_except_table1012
- GCC_except_table1013
- GCC_except_table1014
- GCC_except_table1015
- GCC_except_table1016
- GCC_except_table102
- GCC_except_table1025
- GCC_except_table1030
- GCC_except_table1031
- GCC_except_table1033
- GCC_except_table1034
- GCC_except_table1037
- GCC_except_table1038
- GCC_except_table1039
- GCC_except_table104
- GCC_except_table1040
- GCC_except_table1041
- GCC_except_table1043
- GCC_except_table1044
- GCC_except_table1045
- GCC_except_table1046
- GCC_except_table1047
- GCC_except_table1048
- GCC_except_table1051
- GCC_except_table1055
- GCC_except_table106
- GCC_except_table1061
- GCC_except_table1063
- GCC_except_table1065
- GCC_except_table108
- GCC_except_table1082
- GCC_except_table1100
- GCC_except_table111
- GCC_except_table112
- GCC_except_table1152
- GCC_except_table116
- GCC_except_table1160
- GCC_except_table1162
- GCC_except_table1168
- GCC_except_table1173
- GCC_except_table1177
- GCC_except_table118
- GCC_except_table1182
- GCC_except_table1190
- GCC_except_table1191
- GCC_except_table1192
- GCC_except_table1194
- GCC_except_table120
- GCC_except_table1203
- GCC_except_table1208
- GCC_except_table1209
- GCC_except_table1214
- GCC_except_table1216
- GCC_except_table1217
- GCC_except_table1218
- GCC_except_table1219
- GCC_except_table122
- GCC_except_table1220
- GCC_except_table1239
- GCC_except_table124
- GCC_except_table1241
- GCC_except_table1242
- GCC_except_table1243
- GCC_except_table1244
- GCC_except_table1245
- GCC_except_table1246
- GCC_except_table1247
- GCC_except_table1249
- GCC_except_table1259
- GCC_except_table126
- GCC_except_table1267
- GCC_except_table1270
- GCC_except_table1271
- GCC_except_table1274
- GCC_except_table1275
- GCC_except_table1278
- GCC_except_table1279
- GCC_except_table1282
- GCC_except_table1283
- GCC_except_table1284
- GCC_except_table1289
- GCC_except_table1291
- GCC_except_table1297
- GCC_except_table1303
- GCC_except_table1304
- GCC_except_table1314
- GCC_except_table1319
- GCC_except_table1325
- GCC_except_table1336
- GCC_except_table1342
- GCC_except_table1352
- GCC_except_table1356
- GCC_except_table1361
- GCC_except_table1362
- GCC_except_table1365
- GCC_except_table1366
- GCC_except_table1367
- GCC_except_table1368
- GCC_except_table1372
- GCC_except_table1380
- GCC_except_table1383
- GCC_except_table139
- GCC_except_table1390
- GCC_except_table1393
- GCC_except_table1398
- GCC_except_table1401
- GCC_except_table1403
- GCC_except_table1404
- GCC_except_table141
- GCC_except_table1415
- GCC_except_table1424
- GCC_except_table1427
- GCC_except_table143
- GCC_except_table1431
- GCC_except_table1435
- GCC_except_table1437
- GCC_except_table1442
- GCC_except_table1443
- GCC_except_table1448
- GCC_except_table146
- GCC_except_table147
- GCC_except_table1477
- GCC_except_table148
- GCC_except_table1481
- GCC_except_table1482
- GCC_except_table1485
- GCC_except_table1486
- GCC_except_table1489
- GCC_except_table1494
- GCC_except_table1495
- GCC_except_table1497
- GCC_except_table1511
- GCC_except_table152
- GCC_except_table1524
- GCC_except_table1526
- GCC_except_table1527
- GCC_except_table1528
- GCC_except_table1533
- GCC_except_table1542
- GCC_except_table1555
- GCC_except_table1556
- GCC_except_table1571
- GCC_except_table1574
- GCC_except_table1577
- GCC_except_table1578
- GCC_except_table1579
- GCC_except_table158
- GCC_except_table1584
- GCC_except_table1585
- GCC_except_table1587
- GCC_except_table1589
- GCC_except_table1595
- GCC_except_table160
- GCC_except_table1605
- GCC_except_table1608
- GCC_except_table1611
- GCC_except_table1616
- GCC_except_table1620
- GCC_except_table1621
- GCC_except_table1625
- GCC_except_table1626
- GCC_except_table1629
- GCC_except_table1633
- GCC_except_table1638
- GCC_except_table1640
- GCC_except_table1642
- GCC_except_table1643
- GCC_except_table1649
- GCC_except_table1662
- GCC_except_table1666
- GCC_except_table1676
- GCC_except_table1677
- GCC_except_table1678
- GCC_except_table1687
- GCC_except_table1710
- GCC_except_table172
- GCC_except_table1730
- GCC_except_table1731
- GCC_except_table1733
- GCC_except_table1734
- GCC_except_table1735
- GCC_except_table1736
- GCC_except_table1739
- GCC_except_table1740
- GCC_except_table1741
- GCC_except_table1742
- GCC_except_table1743
- GCC_except_table1744
- GCC_except_table1745
- GCC_except_table1746
- GCC_except_table1747
- GCC_except_table1749
- GCC_except_table1750
- GCC_except_table1752
- GCC_except_table1753
- GCC_except_table1755
- GCC_except_table1756
- GCC_except_table1757
- GCC_except_table1758
- GCC_except_table176
- GCC_except_table1760
- GCC_except_table1761
- GCC_except_table1762
- GCC_except_table1765
- GCC_except_table177
- GCC_except_table1770
- GCC_except_table1771
- GCC_except_table1773
- GCC_except_table1774
- GCC_except_table1775
- GCC_except_table1777
- GCC_except_table1778
- GCC_except_table178
- GCC_except_table1788
- GCC_except_table1790
- GCC_except_table1791
- GCC_except_table1796
- GCC_except_table1798
- GCC_except_table1799
- GCC_except_table180
- GCC_except_table1800
- GCC_except_table1801
- GCC_except_table1802
- GCC_except_table1803
- GCC_except_table1804
- GCC_except_table1806
- GCC_except_table181
- GCC_except_table182
- GCC_except_table1832
- GCC_except_table1833
- GCC_except_table1834
- GCC_except_table1835
- GCC_except_table1836
- GCC_except_table1841
- GCC_except_table1842
- GCC_except_table1852
- GCC_except_table1854
- GCC_except_table1856
- GCC_except_table1857
- GCC_except_table1862
- GCC_except_table1864
- GCC_except_table1865
- GCC_except_table1866
- GCC_except_table1867
- GCC_except_table1868
- GCC_except_table187
- GCC_except_table1880
- GCC_except_table191
- GCC_except_table1933
- GCC_except_table1940
- GCC_except_table196
- GCC_except_table1961
- GCC_except_table1962
- GCC_except_table1988
- GCC_except_table1989
- GCC_except_table1990
- GCC_except_table2003
- GCC_except_table2004
- GCC_except_table2013
- GCC_except_table2014
- GCC_except_table2016
- GCC_except_table2017
- GCC_except_table2025
- GCC_except_table2029
- GCC_except_table205
- GCC_except_table2056
- GCC_except_table2057
- GCC_except_table2070
- GCC_except_table2072
- GCC_except_table2073
- GCC_except_table2074
- GCC_except_table2076
- GCC_except_table2077
- GCC_except_table2078
- GCC_except_table2080
- GCC_except_table2081
- GCC_except_table2088
- GCC_except_table2089
- GCC_except_table2092
- GCC_except_table2094
- GCC_except_table2114
- GCC_except_table2118
- GCC_except_table2120
- GCC_except_table2124
- GCC_except_table213
- GCC_except_table214
- GCC_except_table2161
- GCC_except_table2162
- GCC_except_table2168
- GCC_except_table2174
- GCC_except_table2187
- GCC_except_table2188
- GCC_except_table2190
- GCC_except_table2191
- GCC_except_table2194
- GCC_except_table2195
- GCC_except_table2196
- GCC_except_table2198
- GCC_except_table2199
- GCC_except_table2200
- GCC_except_table2202
- GCC_except_table2203
- GCC_except_table2204
- GCC_except_table2205
- GCC_except_table2207
- GCC_except_table2208
- GCC_except_table2209
- GCC_except_table221
- GCC_except_table2210
- GCC_except_table2215
- GCC_except_table2216
- GCC_except_table2217
- GCC_except_table2218
- GCC_except_table2219
- GCC_except_table222
- GCC_except_table2220
- GCC_except_table2221
- GCC_except_table2222
- GCC_except_table2223
- GCC_except_table2226
- GCC_except_table2227
- GCC_except_table2228
- GCC_except_table2229
- GCC_except_table2230
- GCC_except_table2231
- GCC_except_table2232
- GCC_except_table2233
- GCC_except_table2234
- GCC_except_table2235
- GCC_except_table2236
- GCC_except_table2237
- GCC_except_table2239
- GCC_except_table224
- GCC_except_table2247
- GCC_except_table2250
- GCC_except_table2252
- GCC_except_table2253
- GCC_except_table2258
- GCC_except_table2259
- GCC_except_table226
- GCC_except_table2261
- GCC_except_table2268
- GCC_except_table2269
- GCC_except_table2275
- GCC_except_table2276
- GCC_except_table2277
- GCC_except_table2278
- GCC_except_table2279
- GCC_except_table2280
- GCC_except_table2281
- GCC_except_table2283
- GCC_except_table2284
- GCC_except_table2290
- GCC_except_table2295
- GCC_except_table2296
- GCC_except_table2303
- GCC_except_table2304
- GCC_except_table231
- GCC_except_table2310
- GCC_except_table2311
- GCC_except_table2312
- GCC_except_table2342
- GCC_except_table2343
- GCC_except_table2345
- GCC_except_table2347
- GCC_except_table2348
- GCC_except_table2349
- GCC_except_table235
- GCC_except_table2351
- GCC_except_table2352
- GCC_except_table2353
- GCC_except_table2356
- GCC_except_table2362
- GCC_except_table2382
- GCC_except_table2383
- GCC_except_table2384
- GCC_except_table2385
- GCC_except_table2413
- GCC_except_table2414
- GCC_except_table2416
- GCC_except_table2418
- GCC_except_table242
- GCC_except_table2420
- GCC_except_table2421
- GCC_except_table2428
- GCC_except_table2432
- GCC_except_table2434
- GCC_except_table2435
- GCC_except_table2436
- GCC_except_table2439
- GCC_except_table2442
- GCC_except_table2443
- GCC_except_table2444
- GCC_except_table2445
- GCC_except_table2446
- GCC_except_table2457
- GCC_except_table2461
- GCC_except_table2463
- GCC_except_table2470
- GCC_except_table2472
- GCC_except_table2477
- GCC_except_table2478
- GCC_except_table2479
- GCC_except_table2486
- GCC_except_table2490
- GCC_except_table2495
- GCC_except_table2496
- GCC_except_table2498
- GCC_except_table2500
- GCC_except_table2502
- GCC_except_table2503
- GCC_except_table2504
- GCC_except_table2506
- GCC_except_table2507
- GCC_except_table2508
- GCC_except_table2512
- GCC_except_table255
- GCC_except_table256
- GCC_except_table282
- GCC_except_table283
- GCC_except_table300
- GCC_except_table301
- GCC_except_table304
- GCC_except_table319
- GCC_except_table320
- GCC_except_table321
- GCC_except_table324
- GCC_except_table326
- GCC_except_table327
- GCC_except_table330
- GCC_except_table331
- GCC_except_table335
- GCC_except_table340
- GCC_except_table341
- GCC_except_table342
- GCC_except_table346
- GCC_except_table354
- GCC_except_table361
- GCC_except_table366
- GCC_except_table368
- GCC_except_table369
- GCC_except_table371
- GCC_except_table372
- GCC_except_table375
- GCC_except_table376
- GCC_except_table377
- GCC_except_table380
- GCC_except_table416
- GCC_except_table436
- GCC_except_table437
- GCC_except_table438
- GCC_except_table443
- GCC_except_table445
- GCC_except_table446
- GCC_except_table447
- GCC_except_table448
- GCC_except_table450
- GCC_except_table455
- GCC_except_table458
- GCC_except_table469
- GCC_except_table470
- GCC_except_table473
- GCC_except_table474
- GCC_except_table475
- GCC_except_table482
- GCC_except_table488
- GCC_except_table489
- GCC_except_table493
- GCC_except_table509
- GCC_except_table510
- GCC_except_table511
- GCC_except_table512
- GCC_except_table515
- GCC_except_table522
- GCC_except_table532
- GCC_except_table541
- GCC_except_table64
- GCC_except_table673
- GCC_except_table676
- GCC_except_table677
- GCC_except_table678
- GCC_except_table679
- GCC_except_table681
- GCC_except_table683
- GCC_except_table684
- GCC_except_table686
- GCC_except_table688
- GCC_except_table690
- GCC_except_table691
- GCC_except_table693
- GCC_except_table695
- GCC_except_table696
- GCC_except_table697
- GCC_except_table699
- GCC_except_table701
- GCC_except_table703
- GCC_except_table724
- GCC_except_table733
- GCC_except_table736
- GCC_except_table739
- GCC_except_table746
- GCC_except_table748
- GCC_except_table749
- GCC_except_table751
- GCC_except_table753
- GCC_except_table758
- GCC_except_table76
- GCC_except_table761
- GCC_except_table762
- GCC_except_table77
- GCC_except_table78
- GCC_except_table789
- GCC_except_table79
- GCC_except_table793
- GCC_except_table800
- GCC_except_table802
- GCC_except_table803
- GCC_except_table811
- GCC_except_table821
- GCC_except_table822
- GCC_except_table825
- GCC_except_table831
- GCC_except_table832
- GCC_except_table833
- GCC_except_table834
- GCC_except_table837
- GCC_except_table838
- GCC_except_table847
- GCC_except_table86
- GCC_except_table860
- GCC_except_table861
- GCC_except_table863
- GCC_except_table864
- GCC_except_table867
- GCC_except_table87
- GCC_except_table870
- GCC_except_table894
- GCC_except_table895
- GCC_except_table896
- GCC_except_table898
- GCC_except_table899
- GCC_except_table900
- GCC_except_table901
- GCC_except_table902
- GCC_except_table903
- GCC_except_table905
- GCC_except_table912
- GCC_except_table913
- GCC_except_table916
- GCC_except_table917
- GCC_except_table918
- GCC_except_table919
- GCC_except_table920
- GCC_except_table921
- GCC_except_table923
- GCC_except_table924
- GCC_except_table931
- GCC_except_table932
- GCC_except_table939
- GCC_except_table952
- GCC_except_table955
- GCC_except_table956
- GCC_except_table964
- GCC_except_table976
- GCC_except_table979
- GCC_except_table982
- GCC_except_table983
- GCC_except_table984
- GCC_except_table987
- GCC_except_table988
- GCC_except_table989
- GCC_except_table990
- GCC_except_table991
- GCC_except_table992
- GCC_except_table993
- GCC_except_table994
- GCC_except_table995
- _OBJC_IVAR_$_MIDICIDeviceManager._profiles
- _OBJC_IVAR_$_MIDIUMPCIProfile._isMine
- _OBJC_IVAR_$_MIDIUMPEndpoint._isMine
- _OBJC_IVAR_$_MIDIUMPFunctionBlock._isMine
- __ZGVZ14sendUMPMessagejhRKN4midi6sysex7EE4port
- __ZN4MIDIL13_gMessageSizeE.1762
- __ZZ14sendUMPMessagejhRKN4midi6sysex7EE4port
- __ZZ14sendUMPMessagejhRKN4midi6sysex7EENK3$_0clERKNS_12data_messageE
- __ZZN14MIDIStringDumpL8hexBytesENSt3__14spanIKhLm18446744073709551615EEEE3hex.1802
- ___block_descriptor_tmp.10.147
- ___block_descriptor_tmp.1416
- ___block_descriptor_tmp.165
- ___block_descriptor_tmp.1738
- ___block_descriptor_tmp.1842
- ___block_descriptor_tmp.2757
- ___block_descriptor_tmp.2876
- ___block_descriptor_tmp.3509
- ___block_descriptor_tmp.7.181
- ___block_descriptor_tmp.8.182
- ___block_literal_global.1352
- ___block_literal_global.166
- ___block_literal_global.860
- ___block_literal_global.953
- _objc_msgSend$initWithProfileID:name:type:firstGroup:firstChannel:enabledChannelCount:totalChannelCount:
CStrings:
+ "%25s:%-5d Completed Profile Details transaction between %ud -> %ud"
+ "%25s:%-5d ERROR: Failed to find Profile Details transaction between %ud -> %ud"
+ "%25s:%-5d ERROR: Failed to handleProfileDetailsReply for null device"
+ "%25s:%-5d INFO: Received inquiry from self, ignoring.."
+ "(identity.family & 0xC000) == 0"
+ "(identity.manufacturer & 0xFF808080) == 0"
+ "(identity.model & 0xC000) == 0"
+ "(identity.revision & 0xF0000000) == 0"
+ ".cxx_construct"
+ "@\"MIDIUMPMutableEndpoint\""
+ "@\"NSObject<OS_dispatch_queue>\""
+ "@\"NSPointerArray\""
+ "@20@0:8i16"
+ "@21@0:8{profile_id=CCCCC}16"
+ "@24@0:8^{_NSZone=}16"
+ "@24@0:8r^v16"
+ "@68@0:8@16@24C32Q36Q44@?52@?60"
+ "@76@0:8@16@24C32Q36Q44@52@?60@?68"
+ "B20@0:8C16"
+ "B24@0:8r^v16"
+ "B24@0:8r^{InternalUMPCI_ProcessInquiryReport=iIIICCC^{__CFData}B}16"
+ "B28@0:8C16r^v20"
+ "B28@0:8C16r^{discovery_inquiry_view=^{sysex7}}20"
+ "B28@0:8C16r^{discovery_reply_view=^{sysex7}}20"
+ "B28@0:8C16r^{endpoint_information_inquiry_view=^{sysex7}}20"
+ "B28@0:8C16r^{invalidate_muid_view=^{sysex7}}20"
+ "B28@0:8C16r^{nak_view=^{sysex7}}20"
+ "B28@0:8C16r^{profile_details_inquiry_view=^{sysex7}}20"
+ "B28@0:8C16r^{profile_id_view=^{sysex7}}20"
+ "B28@0:8C16r^{profile_inquiry_view=^{sysex7}}20"
+ "B28@0:8i16^@20"
+ "B32@0:8r^v16^@24"
+ "B32@0:8r^{MIDIEventList=iI[1{MIDIEventPacket=QI[64I]}]}16^@24"
+ "B36@0:8C16@20r^{get_property_data_view=^{sysex7}}28"
+ "B36@0:8C16@20r^{profile_specific_data_view=^{sysex7}}28"
+ "B40@0:8@16@24^@32"
+ "B40@0:8C16C20@24^@32"
+ "B48@0:8@16C24C28@32^@40"
+ "Invalid profile for device!"
+ "MIDI-CI Mutable Device"
+ "MIDICIMutableDevice"
+ "MIDICIMutableDevice messenger"
+ "MIDIUMP Mutable CI Profile"
+ "MIDIUMPMutableCIProfile"
+ "ProcessInquiryTransaction.mm"
+ "ProfileDetailsTransaction.cpp"
+ "T@\"MIDI2DeviceInfo\",R,N"
+ "T@\"MIDIUMPEndpoint\",R,W,N"
+ "T@\"NSArray\",R,N"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_callbackQueue"
+ "T@\"NSPointerArray\",&,N,V_mutableDevices"
+ "TB,R,N"
+ "TC,R,N"
+ "TC,V_group"
+ "TI,N,V_ownerObjectRef"
+ "TI,R,V_serverMUID"
+ "TS,R,N"
+ "Ti,R,N"
+ "UMPCIObjectDispose"
+ "UMPCIServerSideMIDICITransaction"
+ "_activeTransactions"
+ "_callbackData"
+ "_callbackMutex"
+ "_callbackQueue"
+ "_endpoint"
+ "_group"
+ "_messageCallback"
+ "_messenger"
+ "_mutableDevices"
+ "_ownerClientRef"
+ "_ownerObjectRef"
+ "_resourceList"
+ "_sysexCollector"
+ "a"
+ "addMutableDevice:"
+ "addPointer:"
+ "addProfile:error:"
+ "add_device_identity"
+ "allocWithZone:"
+ "arrayByAddingObject:"
+ "arrayWithArray:"
+ "callbackQueue"
+ "channel_controller"
+ "copyWithZone:"
+ "data_size"
+ "destination_muid"
+ "detailsInquiry:target:completion:"
+ "detailsInquiryWithTarget:completion:"
+ "device_id <= uint7_max"
+ "findDeviceWithMUID:"
+ "findProfileForID:"
+ "group"
+ "handleDiscoveryInquiry:view:"
+ "handleDiscoveryReply:view:"
+ "handleEndpointInformationInquiry:view:"
+ "handleGetProperty:fromDevice:view:"
+ "handleInvalidateMUID:view:"
+ "handleNAK:view:"
+ "handleProcessInquiryReplyMessage:"
+ "handleProfileDetailsInquiry:view:"
+ "handleProfileDetailsReplyMessage:"
+ "handleProfileIDView:view:"
+ "handleProfileInquiry:view:"
+ "handleProfileSpecificData:fromDevice:view:"
+ "handleSysExIdentityRequest:"
+ "handleSysex:sysEx:"
+ "i24@0:8r^{MIDIEventList=iI[1{MIDIEventPacket=QI[64I]}]}16"
+ "initWithArray:"
+ "initWithProfileID:name:profileType:groupOffset:firstChannel:enabledChannelCount:totalChannelCount:"
+ "initWithUMPEndpointPair:functionBlock:capabilities:sysExSizeLimit:maxPERequests:profileSpecificDataCallback:messageCallback:"
+ "initWithUMPEndpointPair:functionBlock:capabilities:sysExSizeLimit:maxPERequests:queue:profileSpecificDataCallback:messageCallback:"
+ "mMutex"
+ "make_profile_inquiry_reply"
+ "mutableDevices"
+ "note_data"
+ "num_disabled_profiles <= sysex7::uint14_max"
+ "num_enabled_profiles <= sysex7::uint14_max"
+ "ownerObjectRef"
+ "owner_client_ref"
+ "parseDictionary"
+ "performTransaction"
+ "pointerAtIndex:"
+ "receiveMessageViaSource:error:"
+ "removeMutableDevice:"
+ "removePointerAtIndex:"
+ "removeProfile:error:"
+ "requestProcessInquiryMessageReport:channelControllerMessages:noteDataMessages:dataControl:completion:"
+ "respondViaSource:"
+ "sendEventList:error:"
+ "sendMessage:deviceID:data:error:"
+ "sendMessageFromDevice:withSubType:deviceID:data:error:"
+ "sendMessageToCIDevice:withSubType:deviceID:data:error:"
+ "sendProfileSpecificData:error:"
+ "sendProfileSpecificData:profileData:error:"
+ "sender_object_ref"
+ "serverSideTransactionDictionary:"
+ "setCallbackQueue:"
+ "setGroup:"
+ "setMutableDevices:"
+ "setOwnerObjectRef:"
+ "setReceiveTapBlock:"
+ "setResourceList:error:"
+ "setStreamProtocol:error:"
+ "setupMIDIStreamObjects"
+ "subtype <= uint7_max"
+ "system_messages"
+ "target"
+ "transactionType"
+ "transaction_type"
+ "type.value() == InternalTransactionType::processInquiry"
+ "type.value() == InternalTransactionType::profileDetails"
+ "v24@0:8r^v16"
+ "v24@0:8r^{InternalUMPCI_ProcessInquiryReport=iIIICCC^{__CFData}B}16"
+ "v24@0:8{block<void (const MIDIEventList *, void *)>=@?}16"
+ "v24@?0r^{MIDIEventList=iI[1{MIDIEventPacket=QI[64I]}]}8^v16"
+ "v28@0:8C16@?20"
+ "v40@0:8C16C20C24C28@?32"
+ "weakObjectsPointerArray"
+ "{CallbackData=\"mUserReceiveBlock\"@?\"mReceiveTapBlock\"{lf_read_synchronized_write<applesauce::dispatch::block<void (const MIDIEventList *, void *)>>=\"mImpl\"{lf_read_sync_write_impl=\"mState\"{atomic<caulk::concurrent::details::lf_read_sync_write_impl::State>=\"__a_\"{__cxx_atomic_impl<caulk::concurrent::details::lf_read_sync_write_impl::State, std::__cxx_atomic_base_impl<caulk::concurrent::details::lf_read_sync_write_impl::State>>=\"__a_value\"A{State}}}\"mMutationLock\"{unfair_lock=\"m_lock\"{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}}}\"mValueValid\"{array<bool, 2UL>=\"__elems_\"[2B]}\"mValues\"{array<caulk::concurrent::lf_read_synchronized_write<applesauce::dispatch::block<void (const MIDIEventList *, void *)>>::T_storage, 2UL>=\"__elems_\"[2{T_storage=\"bytes\"{array<std::byte, 8UL>=\"__elems_\"[8C]}}]}}}"
+ "{mutex=\"__m_\"{_opaque_pthread_mutex_t=\"__sig\"q\"__opaque\"[56c]}}"
+ "{unfair_lock=\"m_lock\"{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}}"
+ "{unfair_recursive_lock=\"m_lock\"{os_unfair_recursive_lock_s=\"ourl_lock\"{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}\"ourl_count\"I}}"
+ "{unique_ptr<MIDICI::SysexCollector, std::default_delete<MIDICI::SysexCollector>>=\"__ptr_\"^{SysexCollector}}"
+ "{unique_ptr<caulk::concurrent::messenger, std::default_delete<caulk::concurrent::messenger>>=\"__ptr_\"^{messenger}}"
+ "{vector<CIAsyncTransaction, std::allocator<CIAsyncTransaction>>=\"__begin_\"^{CIAsyncTransaction}\"__end_\"^{CIAsyncTransaction}\"__cap_\"^{CIAsyncTransaction}}"
- "1!"
- "5"
- "B20@0:8i16"
- "T@\"MIDI2DeviceInfo\",R,N,V_deviceInfo"
- "T@\"MIDIUMPEndpoint\",R,W,N,V_UMPEndpoint"
- "T@\"NSArray\",R,N,V_profiles"
- "T@\"NSMutableArray\",&,N,V_profiles"
- "T@\"NSString\",R,N,V_productInstanceID"
- "TB,N,V_isMine"
- "TB,R,N,V_hasJRTSReceiveCapability"
- "TB,R,N,V_hasJRTSTransmitCapability"
- "TB,R,N,V_hasStaticFunctionBlocks"
- "TB,R,N,V_isEnabled"
- "TB,R,N,V_supportsProcessInquiry"
- "TB,R,N,V_supportsProfileConfiguration"
- "TB,R,N,V_supportsPropertyExchange"
- "TB,R,N,V_supportsProtocolNegotiation"
- "TC,R,N,V_deviceType"
- "TC,R,N,V_endpointType"
- "TC,R,N,V_firstChannel"
- "TC,R,N,V_firstGroup"
- "TC,R,N,V_functionBlockID"
- "TC,R,N,V_groupOffset"
- "TC,R,N,V_maxSysEx8Streams"
- "TC,R,N,V_profileType"
- "TC,R,N,V_supportedMIDIProtocols"
- "TC,R,N,V_totalGroupsSpanned"
- "TI,R,N,V_MIDIDestination"
- "TI,R,N,V_MIDISource"
- "TI,R,N,V_MUID"
- "TI,R,N,V_serverMUID"
- "TQ,R,N,V_maxPropertyExchangeRequests"
- "TQ,R,N,V_maxSysExSize"
- "TS,R,N,V_enabledChannelCount"
- "TS,R,N,V_totalChannelCount"
- "Ti,R,N,V_MIDI1Info"
- "Ti,R,N,V_MIDIProtocol"
- "Ti,R,N,V_UIHint"
- "Ti,R,N,V_direction"
- "_isMine"
- "changeStreamProtocol:"
- "disableFunctionBlock:"
- "enableFunctionBlock:"
- "initWithProfileID:name:type:firstGroup:firstChannel:enabledChannelCount:totalChannelCount:"
- "setIsMine:"
- "setProfiles:"

```
