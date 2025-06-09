## AudioToolbox

> `/System/Library/Frameworks/AudioToolbox.framework/AudioToolbox`

```diff

-1456.607.0.0.0
-  __TEXT.__text: 0x2976c4
-  __TEXT.__auth_stubs: 0x3bb0
-  __TEXT.__objc_methlist: 0x1d4c
-  __TEXT.__const: 0x135c
-  __TEXT.__dlopen_cstrs: 0x676
-  __TEXT.__gcc_except_tab: 0x284b8
-  __TEXT.__cstring: 0x1dd7a
-  __TEXT.__oslogstring: 0x35dbc
-  __TEXT.__unwind_info: 0xc3f8
-  __TEXT.__objc_classname: 0x3c0
-  __TEXT.__objc_methname: 0x5710
-  __TEXT.__objc_methtype: 0x42db
-  __TEXT.__objc_stubs: 0x4200
-  __DATA_CONST.__got: 0xd68
-  __DATA_CONST.__const: 0x3298
-  __DATA_CONST.__objc_classlist: 0xc8
-  __DATA_CONST.__objc_protolist: 0x88
+1534.2.30.1.0
+  __TEXT.__text: 0x2a4f80
+  __TEXT.__auth_stubs: 0x3b50
+  __TEXT.__delay_stubs: 0x58
+  __TEXT.__delay_helper: 0xa4
+  __TEXT.__objc_methlist: 0x203c
+  __TEXT.__const: 0x1348
+  __TEXT.__dlopen_cstrs: 0x71d
+  __TEXT.__gcc_except_tab: 0x28418
+  __TEXT.__cstring: 0x1f4c4
+  __TEXT.__oslogstring: 0x38e45
+  __TEXT.__unwind_info: 0xc6e0
+  __TEXT.__objc_classname: 0x417
+  __TEXT.__objc_methname: 0x5d13
+  __TEXT.__objc_methtype: 0x3900
+  __TEXT.__objc_stubs: 0x4640
+  __DATA_CONST.__got: 0xe58
+  __DATA_CONST.__const: 0x3450
+  __DATA_CONST.__objc_classlist: 0xd8
+  __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1648
+  __DATA_CONST.__objc_selrefs: 0x1808
   __DATA_CONST.__objc_protorefs: 0x28
-  __DATA_CONST.__objc_superrefs: 0xb0
+  __DATA_CONST.__objc_superrefs: 0xc0
   __DATA_CONST.__objc_arraydata: 0x358
-  __AUTH_CONST.__auth_got: 0x1df0
-  __AUTH_CONST.__const: 0x10c00
-  __AUTH_CONST.__cfstring: 0x5540
-  __AUTH_CONST.__objc_const: 0x2e70
-  __AUTH_CONST.__objc_intobj: 0x5b8
+  __AUTH_CONST.__auth_got: 0x1dd0
+  __AUTH_CONST.__const: 0x10cc0
+  __AUTH_CONST.__cfstring: 0x5c40
+  __AUTH_CONST.__objc_const: 0x3250
+  __AUTH_CONST.__objc_intobj: 0x5d0
   __AUTH_CONST.__objc_arrayobj: 0x408
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH.__objc_data: 0xa0
-  __AUTH.__data: 0x30
-  __DATA.__objc_ivar: 0x204
-  __DATA.__data: 0x7f8
-  __DATA.__bss: 0x20e1
-  __DATA_DIRTY.__objc_data: 0x730
+  __AUTH.__objc_data: 0x230
+  __AUTH.__data: 0x28
+  __DATA.__objc_ivar: 0x230
+  __DATA.__data: 0x82c
+  __DATA.__bss: 0x1fa1
+  __DATA_DIRTY.__objc_data: 0x640
   __DATA_DIRTY.__data: 0x48
-  __DATA_DIRTY.__bss: 0x2a70
+  __DATA_DIRTY.__bss: 0x2a60
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreAudio.framework/CoreAudio
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /System/Library/PrivateFrameworks/TCC.framework/TCC
+  - /System/Library/PrivateFrameworks/VoiceProcessor.framework/VoiceProcessor
   - /System/Library/PrivateFrameworks/WatchdogClient.framework/WatchdogClient
   - /System/Library/PrivateFrameworks/caulk.framework/caulk
   - /usr/lib/libAudioStatistics.dylib

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D8F95F9D-F94F-3804-A76D-928A38503C07
-  Functions: 9237
-  Symbols:   25588
-  CStrings:  9209
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreMIDI.dylib
+  - /usr/lib/swift/libswiftDarwin.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
+  - /usr/lib/swift/libswiftos.dylib
+  UUID: 106E4093-27AF-30D4-AA7D-7A0D5BEE5FA8
+  Functions: 9431
+  Symbols:   26143
+  CStrings:  9560
 
Symbols:
+ -[ATAudioTapDescription initProcessTapWithFormat:PID:deviceUID:]
+ -[ATAudioTapDescription muteBehavior]
+ -[ATAudioTapDescription setMuteBehavior:]
+ -[ATBlurMixer .cxx_construct]
+ -[ATBlurMixer .cxx_destruct]
+ -[ATBlurMixer audioUnit]
+ -[ATBlurMixer blendTimeMs]
+ -[ATBlurMixer blurHoldTimeSec]
+ -[ATBlurMixer configure]
+ -[ATBlurMixer getAUStripPath]
+ -[ATBlurMixer getBusCountForScope:]
+ -[ATBlurMixer getDSPGraphPath]
+ -[ATBlurMixer getPropStripPath]
+ -[ATBlurMixer initDownlinkWithFormat:maxFrames:error:]
+ -[ATBlurMixer initInternalWithFormat:maxFrames:isUplink:error:]
+ -[ATBlurMixer initUplinkWithFormat:maxFrames:error:]
+ -[ATBlurMixer initializeAU]
+ -[ATBlurMixer isBlurEnabled]
+ -[ATBlurMixer isUplink]
+ -[ATBlurMixer processBlock]
+ -[ATBlurMixer setAUStrip:propertyStrip:]
+ -[ATBlurMixer setBlendTimeMs:]
+ -[ATBlurMixer setDSPGraph:]
+ -[ATBlurMixer setElementCount:]
+ -[ATBlurMixer setEnableBlur:]
+ -[ATBlurMixer setFormat:]
+ -[ATBlurMixer setMaxFramesPerSlice]
+ -[ATBlurMixer setupAU]
+ -[ATBlurMixer uninitializeAU]
+ -[ATBlurMixer updateFormat:error:]
+ -[ATBlurMixer updateFormats]
+ -[ATServerDelegatePriv setIOPropertiesForSession:values:]
+ -[ATThreadSafeHeadTracker initWithRateLimit:detectPredictionAnchor:userContext:factory:execution:finalizer:useSleepWakeDetector:]
+ -[AVVoiceTriggerServer .cxx_destruct]
+ -[AVVoiceTriggerServer activateSecureSession:reply:]
+ -[AVVoiceTriggerServer afSiriActivationBuiltInMicVoiceFuncPtr]
+ -[AVVoiceTriggerServer clientConnections]
+ -[AVVoiceTriggerServer clsVTStateManager]
+ -[AVVoiceTriggerServer dealloc]
+ -[AVVoiceTriggerServer enableBargeInMode:reply:]
+ -[AVVoiceTriggerServer enableListeningOnPorts:reply:]
+ -[AVVoiceTriggerServer enableSpeakerStateListening:reply:]
+ -[AVVoiceTriggerServer enableVoiceTriggerListening:reply:]
+ -[AVVoiceTriggerServer getInputChannelInfoCompletion:]
+ -[AVVoiceTriggerServer hardwareSupportsVoiceTrigger]
+ -[AVVoiceTriggerServer init]
+ -[AVVoiceTriggerServer initializeWithReply:]
+ -[AVVoiceTriggerServer isAssistantVoiceTriggerEnabled]
+ -[AVVoiceTriggerServer listener:shouldAcceptNewConnection:]
+ -[AVVoiceTriggerServer listeningEnabledReply:]
+ -[AVVoiceTriggerServer mobileAssistantDylib]
+ -[AVVoiceTriggerServer notificationQueue]
+ -[AVVoiceTriggerServer portsActiveReply:]
+ -[AVVoiceTriggerServer sendActiveStateChangedNotificationForPort:isActive:]
+ -[AVVoiceTriggerServer sendSpeakerMuteStateChangedNotification:]
+ -[AVVoiceTriggerServer sendVoiceTriggerOccuredNotification:triggerTime:]
+ -[AVVoiceTriggerServer serverListener]
+ -[AVVoiceTriggerServer setAfSiriActivationBuiltInMicVoiceFuncPtr:]
+ -[AVVoiceTriggerServer setAggressiveECMode:reply:]
+ -[AVVoiceTriggerServer setClientConnections:]
+ -[AVVoiceTriggerServer setClsVTStateManager:]
+ -[AVVoiceTriggerServer setListeningProperty:reply:]
+ -[AVVoiceTriggerServer setMobileAssistantDylib:]
+ -[AVVoiceTriggerServer setNotificationQueue:]
+ -[AVVoiceTriggerServer setServerListener:]
+ -[AVVoiceTriggerServer setVoiceTriggerDylib:]
+ -[AVVoiceTriggerServer setVtStateManager:]
+ -[AVVoiceTriggerServer siriClientRecordStateChanged:]
+ -[AVVoiceTriggerServer siriClientsRecordingReply:]
+ -[AVVoiceTriggerServer speakerStateActiveReply:]
+ -[AVVoiceTriggerServer speakerStateMutedReply:]
+ -[AVVoiceTriggerServer speechDetectionVADCreated]
+ -[AVVoiceTriggerServer updateVoiceTriggerConfiguration:reply:]
+ -[AVVoiceTriggerServer voiceTriggerDylib]
+ -[AVVoiceTriggerServer voiceTriggerPastDataFramesAvailable:]
+ -[AVVoiceTriggerServer vtStateManager]
+ -[AVVoiceTriggerServerHysteresisNotifier .cxx_destruct]
+ -[AVVoiceTriggerServerHysteresisNotifier addPortToMonitor:hysteresisDurationSeconds:notificationBlock:]
+ -[AVVoiceTriggerServerHysteresisNotifier dealloc]
+ -[AVVoiceTriggerServerHysteresisNotifier getPortManagerForType:]
+ -[AVVoiceTriggerServerHysteresisNotifier initWithSerialQueue:]
+ -[AVVoiceTriggerServerHysteresisNotifier isPortActive:activePortsToken:]
+ -[AVVoiceTriggerServerHysteresisNotifier portsToMonitor]
+ -[AVVoiceTriggerServerHysteresisNotifier processState:]
+ -[AVVoiceTriggerServerHysteresisNotifier queue]
+ -[AVVoiceTriggerServerHysteresisNotifier removePortToMonitor:]
+ -[AVVoiceTriggerServerHysteresisNotifier sendState:]
+ -[AVVoiceTriggerServerHysteresisNotifier setPortsToMonitor:]
+ -[AVVoiceTriggerServerHysteresisNotifier setQueue:]
+ -[AVVoiceTriggerServerHysteresisNotifier stateChanged:]
+ -[AVVoiceTriggerServerHysteresisNotifier stateChanged:forPort:]
+ -[AVVoiceTriggerServerPortManager .cxx_destruct]
+ -[AVVoiceTriggerServerPortManager callNotificationBlock:]
+ -[AVVoiceTriggerServerPortManager generation]
+ -[AVVoiceTriggerServerPortManager hysteresisDurationSeconds]
+ -[AVVoiceTriggerServerPortManager initWithPortType:hysteresisDurationSeconds:notificationBlock:]
+ -[AVVoiceTriggerServerPortManager lastStateSent]
+ -[AVVoiceTriggerServerPortManager listeningEnabled]
+ -[AVVoiceTriggerServerPortManager notificationBlock]
+ -[AVVoiceTriggerServerPortManager notifyStateChanged:onQueue:]
+ -[AVVoiceTriggerServerPortManager portType]
+ -[AVVoiceTriggerServerPortManager setGeneration:]
+ -[AVVoiceTriggerServerPortManager setHysteresisDurationSeconds:]
+ -[AVVoiceTriggerServerPortManager setLastStateSent:]
+ -[AVVoiceTriggerServerPortManager setListeningEnabled:]
+ -[AVVoiceTriggerServerPortManager setNotificationBlock:]
+ -[AVVoiceTriggerServerPortManager setPortType:]
+ -[TranslatorClientDelegate .cxx_construct]
+ -[TranslatorClientDelegate .cxx_destruct]
+ -[TranslatorClientDelegate audioGenerationDidFinishForClient:]
+ -[TranslatorClientDelegate client:didGenerateTranslatedAudio:]
+ -[TranslatorClientDelegate client:didPauseTranslationWithReason:]
+ -[TranslatorClientDelegate client:didReceiveTranscriptionResult:]
+ -[TranslatorClientDelegate client:didReceiveTranslationResult:]
+ -[TranslatorClientDelegate client:didStopTranslationWithError:]
+ -[TranslatorClientDelegate client:willStartTranslatedAudioWithMetadata:]
+ -[TranslatorClientDelegate initWithWeakImpl:scope:]
+ -[TranslatorClientDelegate serverDidDisconnectForClient:]
+ -[TranslatorClientDelegate translationDidResumeForClient:]
+ -[TranslatorClientDelegate translationDidStartForClient:]
+ GCC_except_table0
+ GCC_except_table1
+ GCC_except_table100
+ GCC_except_table1003
+ GCC_except_table1008
+ GCC_except_table1016
+ GCC_except_table1024
+ GCC_except_table1027
+ GCC_except_table1028
+ GCC_except_table1030
+ GCC_except_table1031
+ GCC_except_table1033
+ GCC_except_table1035
+ GCC_except_table1036
+ GCC_except_table1037
+ GCC_except_table1038
+ GCC_except_table1039
+ GCC_except_table1040
+ GCC_except_table1043
+ GCC_except_table1044
+ GCC_except_table1045
+ GCC_except_table1046
+ GCC_except_table1049
+ GCC_except_table1065
+ GCC_except_table107
+ GCC_except_table1071
+ GCC_except_table1072
+ GCC_except_table1079
+ GCC_except_table108
+ GCC_except_table1082
+ GCC_except_table1084
+ GCC_except_table1091
+ GCC_except_table1097
+ GCC_except_table1098
+ GCC_except_table1101
+ GCC_except_table1102
+ GCC_except_table1106
+ GCC_except_table1107
+ GCC_except_table1111
+ GCC_except_table1112
+ GCC_except_table1113
+ GCC_except_table1120
+ GCC_except_table1122
+ GCC_except_table1137
+ GCC_except_table1155
+ GCC_except_table1157
+ GCC_except_table116
+ GCC_except_table1163
+ GCC_except_table1167
+ GCC_except_table1171
+ GCC_except_table1172
+ GCC_except_table1173
+ GCC_except_table1174
+ GCC_except_table1184
+ GCC_except_table1185
+ GCC_except_table1193
+ GCC_except_table120
+ GCC_except_table1202
+ GCC_except_table1225
+ GCC_except_table1226
+ GCC_except_table1227
+ GCC_except_table1233
+ GCC_except_table1234
+ GCC_except_table1235
+ GCC_except_table1236
+ GCC_except_table1237
+ GCC_except_table1243
+ GCC_except_table1246
+ GCC_except_table1249
+ GCC_except_table125
+ GCC_except_table1256
+ GCC_except_table1260
+ GCC_except_table1262
+ GCC_except_table1296
+ GCC_except_table1297
+ GCC_except_table1299
+ GCC_except_table1303
+ GCC_except_table1308
+ GCC_except_table1313
+ GCC_except_table1317
+ GCC_except_table1318
+ GCC_except_table1320
+ GCC_except_table1321
+ GCC_except_table1322
+ GCC_except_table1323
+ GCC_except_table1324
+ GCC_except_table1332
+ GCC_except_table1335
+ GCC_except_table1337
+ GCC_except_table1338
+ GCC_except_table1343
+ GCC_except_table1350
+ GCC_except_table1356
+ GCC_except_table1358
+ GCC_except_table136
+ GCC_except_table1368
+ GCC_except_table1369
+ GCC_except_table137
+ GCC_except_table1383
+ GCC_except_table1384
+ GCC_except_table1385
+ GCC_except_table1388
+ GCC_except_table1391
+ GCC_except_table1396
+ GCC_except_table140
+ GCC_except_table1400
+ GCC_except_table1403
+ GCC_except_table1419
+ GCC_except_table1421
+ GCC_except_table1426
+ GCC_except_table1427
+ GCC_except_table1429
+ GCC_except_table1430
+ GCC_except_table1431
+ GCC_except_table1433
+ GCC_except_table1434
+ GCC_except_table1435
+ GCC_except_table1436
+ GCC_except_table1439
+ GCC_except_table144
+ GCC_except_table1456
+ GCC_except_table1458
+ GCC_except_table146
+ GCC_except_table1462
+ GCC_except_table147
+ GCC_except_table1474
+ GCC_except_table1492
+ GCC_except_table1493
+ GCC_except_table1495
+ GCC_except_table1496
+ GCC_except_table1499
+ GCC_except_table150
+ GCC_except_table1502
+ GCC_except_table1503
+ GCC_except_table1504
+ GCC_except_table1506
+ GCC_except_table1509
+ GCC_except_table1510
+ GCC_except_table1518
+ GCC_except_table1519
+ GCC_except_table1520
+ GCC_except_table1525
+ GCC_except_table1535
+ GCC_except_table1550
+ GCC_except_table1551
+ GCC_except_table1553
+ GCC_except_table1554
+ GCC_except_table156
+ GCC_except_table1561
+ GCC_except_table1562
+ GCC_except_table1563
+ GCC_except_table1564
+ GCC_except_table1566
+ GCC_except_table1567
+ GCC_except_table1568
+ GCC_except_table1569
+ GCC_except_table157
+ GCC_except_table1570
+ GCC_except_table1571
+ GCC_except_table1572
+ GCC_except_table1573
+ GCC_except_table1576
+ GCC_except_table1577
+ GCC_except_table1578
+ GCC_except_table1579
+ GCC_except_table1580
+ GCC_except_table1587
+ GCC_except_table1594
+ GCC_except_table1595
+ GCC_except_table1602
+ GCC_except_table1603
+ GCC_except_table1604
+ GCC_except_table1606
+ GCC_except_table1607
+ GCC_except_table1612
+ GCC_except_table1615
+ GCC_except_table1617
+ GCC_except_table1619
+ GCC_except_table1620
+ GCC_except_table1621
+ GCC_except_table1622
+ GCC_except_table1627
+ GCC_except_table1629
+ GCC_except_table1630
+ GCC_except_table1651
+ GCC_except_table1654
+ GCC_except_table1656
+ GCC_except_table1658
+ GCC_except_table1663
+ GCC_except_table1668
+ GCC_except_table1670
+ GCC_except_table1678
+ GCC_except_table1679
+ GCC_except_table1680
+ GCC_except_table1685
+ GCC_except_table1686
+ GCC_except_table1687
+ GCC_except_table1688
+ GCC_except_table170
+ GCC_except_table1702
+ GCC_except_table1712
+ GCC_except_table1715
+ GCC_except_table174
+ GCC_except_table1742
+ GCC_except_table1743
+ GCC_except_table1746
+ GCC_except_table175
+ GCC_except_table1751
+ GCC_except_table1755
+ GCC_except_table1762
+ GCC_except_table1785
+ GCC_except_table1787
+ GCC_except_table180
+ GCC_except_table1801
+ GCC_except_table1802
+ GCC_except_table1804
+ GCC_except_table1812
+ GCC_except_table1813
+ GCC_except_table1816
+ GCC_except_table1822
+ GCC_except_table1825
+ GCC_except_table1827
+ GCC_except_table1828
+ GCC_except_table1829
+ GCC_except_table183
+ GCC_except_table1830
+ GCC_except_table1845
+ GCC_except_table1851
+ GCC_except_table1853
+ GCC_except_table1881
+ GCC_except_table189
+ GCC_except_table190
+ GCC_except_table1912
+ GCC_except_table1921
+ GCC_except_table1930
+ GCC_except_table1931
+ GCC_except_table1932
+ GCC_except_table1933
+ GCC_except_table1936
+ GCC_except_table1937
+ GCC_except_table1942
+ GCC_except_table1945
+ GCC_except_table1946
+ GCC_except_table1949
+ GCC_except_table1952
+ GCC_except_table1961
+ GCC_except_table1962
+ GCC_except_table1964
+ GCC_except_table1968
+ GCC_except_table1970
+ GCC_except_table1975
+ GCC_except_table1976
+ GCC_except_table1977
+ GCC_except_table1978
+ GCC_except_table1979
+ GCC_except_table1982
+ GCC_except_table1983
+ GCC_except_table1984
+ GCC_except_table1985
+ GCC_except_table1986
+ GCC_except_table1987
+ GCC_except_table1991
+ GCC_except_table1992
+ GCC_except_table1994
+ GCC_except_table1995
+ GCC_except_table1997
+ GCC_except_table1998
+ GCC_except_table2
+ GCC_except_table2001
+ GCC_except_table2004
+ GCC_except_table2009
+ GCC_except_table2010
+ GCC_except_table2012
+ GCC_except_table2017
+ GCC_except_table2021
+ GCC_except_table2022
+ GCC_except_table2023
+ GCC_except_table2032
+ GCC_except_table2033
+ GCC_except_table2035
+ GCC_except_table2049
+ GCC_except_table206
+ GCC_except_table2062
+ GCC_except_table2063
+ GCC_except_table2066
+ GCC_except_table2068
+ GCC_except_table2069
+ GCC_except_table207
+ GCC_except_table2072
+ GCC_except_table2073
+ GCC_except_table2074
+ GCC_except_table2082
+ GCC_except_table209
+ GCC_except_table21
+ GCC_except_table210
+ GCC_except_table2105
+ GCC_except_table2107
+ GCC_except_table2116
+ GCC_except_table2121
+ GCC_except_table2126
+ GCC_except_table213
+ GCC_except_table2132
+ GCC_except_table2133
+ GCC_except_table2134
+ GCC_except_table2137
+ GCC_except_table2139
+ GCC_except_table2142
+ GCC_except_table2152
+ GCC_except_table2153
+ GCC_except_table2157
+ GCC_except_table2158
+ GCC_except_table2159
+ GCC_except_table2162
+ GCC_except_table2167
+ GCC_except_table217
+ GCC_except_table2178
+ GCC_except_table2179
+ GCC_except_table2182
+ GCC_except_table2184
+ GCC_except_table2186
+ GCC_except_table2188
+ GCC_except_table2198
+ GCC_except_table22
+ GCC_except_table220
+ GCC_except_table2207
+ GCC_except_table2208
+ GCC_except_table2210
+ GCC_except_table222
+ GCC_except_table2229
+ GCC_except_table223
+ GCC_except_table2231
+ GCC_except_table2235
+ GCC_except_table2237
+ GCC_except_table224
+ GCC_except_table2242
+ GCC_except_table2248
+ GCC_except_table2249
+ GCC_except_table2252
+ GCC_except_table2258
+ GCC_except_table2259
+ GCC_except_table2260
+ GCC_except_table2261
+ GCC_except_table227
+ GCC_except_table2273
+ GCC_except_table2286
+ GCC_except_table2287
+ GCC_except_table2288
+ GCC_except_table2289
+ GCC_except_table2298
+ GCC_except_table230
+ GCC_except_table2304
+ GCC_except_table2324
+ GCC_except_table2329
+ GCC_except_table2331
+ GCC_except_table2332
+ GCC_except_table2336
+ GCC_except_table2348
+ GCC_except_table2351
+ GCC_except_table2353
+ GCC_except_table2365
+ GCC_except_table2373
+ GCC_except_table238
+ GCC_except_table239
+ GCC_except_table2396
+ GCC_except_table2403
+ GCC_except_table2405
+ GCC_except_table2407
+ GCC_except_table2408
+ GCC_except_table2411
+ GCC_except_table2412
+ GCC_except_table2413
+ GCC_except_table2415
+ GCC_except_table2420
+ GCC_except_table2421
+ GCC_except_table244
+ GCC_except_table2463
+ GCC_except_table2466
+ GCC_except_table2468
+ GCC_except_table2469
+ GCC_except_table2470
+ GCC_except_table2472
+ GCC_except_table2474
+ GCC_except_table2482
+ GCC_except_table2485
+ GCC_except_table2489
+ GCC_except_table2494
+ GCC_except_table2495
+ GCC_except_table2502
+ GCC_except_table2503
+ GCC_except_table2504
+ GCC_except_table2505
+ GCC_except_table2506
+ GCC_except_table251
+ GCC_except_table2511
+ GCC_except_table2512
+ GCC_except_table2514
+ GCC_except_table2517
+ GCC_except_table2523
+ GCC_except_table2527
+ GCC_except_table2528
+ GCC_except_table2531
+ GCC_except_table2532
+ GCC_except_table2533
+ GCC_except_table2541
+ GCC_except_table2542
+ GCC_except_table2543
+ GCC_except_table2545
+ GCC_except_table2548
+ GCC_except_table2549
+ GCC_except_table2551
+ GCC_except_table2554
+ GCC_except_table2555
+ GCC_except_table2556
+ GCC_except_table2558
+ GCC_except_table2559
+ GCC_except_table2564
+ GCC_except_table2565
+ GCC_except_table2571
+ GCC_except_table2578
+ GCC_except_table2581
+ GCC_except_table261
+ GCC_except_table2618
+ GCC_except_table262
+ GCC_except_table263
+ GCC_except_table2642
+ GCC_except_table2652
+ GCC_except_table2653
+ GCC_except_table267
+ GCC_except_table2681
+ GCC_except_table2691
+ GCC_except_table2692
+ GCC_except_table2693
+ GCC_except_table271
+ GCC_except_table2714
+ GCC_except_table2718
+ GCC_except_table2719
+ GCC_except_table272
+ GCC_except_table2747
+ GCC_except_table2748
+ GCC_except_table275
+ GCC_except_table2750
+ GCC_except_table2751
+ GCC_except_table2759
+ GCC_except_table2770
+ GCC_except_table2780
+ GCC_except_table2781
+ GCC_except_table279
+ GCC_except_table2790
+ GCC_except_table2798
+ GCC_except_table2799
+ GCC_except_table281
+ GCC_except_table2814
+ GCC_except_table2815
+ GCC_except_table2817
+ GCC_except_table2820
+ GCC_except_table2823
+ GCC_except_table2826
+ GCC_except_table2828
+ GCC_except_table2829
+ GCC_except_table283
+ GCC_except_table2842
+ GCC_except_table2843
+ GCC_except_table2867
+ GCC_except_table2868
+ GCC_except_table2869
+ GCC_except_table2872
+ GCC_except_table2882
+ GCC_except_table2886
+ GCC_except_table2891
+ GCC_except_table2900
+ GCC_except_table2901
+ GCC_except_table2904
+ GCC_except_table2905
+ GCC_except_table2906
+ GCC_except_table2907
+ GCC_except_table2908
+ GCC_except_table2909
+ GCC_except_table2921
+ GCC_except_table2925
+ GCC_except_table2926
+ GCC_except_table2935
+ GCC_except_table2936
+ GCC_except_table2946
+ GCC_except_table2947
+ GCC_except_table2950
+ GCC_except_table2994
+ GCC_except_table3005
+ GCC_except_table3007
+ GCC_except_table3008
+ GCC_except_table3009
+ GCC_except_table3011
+ GCC_except_table3013
+ GCC_except_table3014
+ GCC_except_table3017
+ GCC_except_table3019
+ GCC_except_table3020
+ GCC_except_table3021
+ GCC_except_table3022
+ GCC_except_table3023
+ GCC_except_table3025
+ GCC_except_table3026
+ GCC_except_table3027
+ GCC_except_table3028
+ GCC_except_table3029
+ GCC_except_table3031
+ GCC_except_table3032
+ GCC_except_table3039
+ GCC_except_table3059
+ GCC_except_table3061
+ GCC_except_table3065
+ GCC_except_table3066
+ GCC_except_table3070
+ GCC_except_table3072
+ GCC_except_table3074
+ GCC_except_table3076
+ GCC_except_table3077
+ GCC_except_table3078
+ GCC_except_table3082
+ GCC_except_table3083
+ GCC_except_table3084
+ GCC_except_table3086
+ GCC_except_table3087
+ GCC_except_table3089
+ GCC_except_table3090
+ GCC_except_table3091
+ GCC_except_table3092
+ GCC_except_table3093
+ GCC_except_table3096
+ GCC_except_table3097
+ GCC_except_table3104
+ GCC_except_table3105
+ GCC_except_table3106
+ GCC_except_table3107
+ GCC_except_table3108
+ GCC_except_table3109
+ GCC_except_table3110
+ GCC_except_table3111
+ GCC_except_table3113
+ GCC_except_table3116
+ GCC_except_table3121
+ GCC_except_table3124
+ GCC_except_table3127
+ GCC_except_table3128
+ GCC_except_table3131
+ GCC_except_table3133
+ GCC_except_table3134
+ GCC_except_table3138
+ GCC_except_table3139
+ GCC_except_table3143
+ GCC_except_table3145
+ GCC_except_table3146
+ GCC_except_table3148
+ GCC_except_table3149
+ GCC_except_table3154
+ GCC_except_table3156
+ GCC_except_table3157
+ GCC_except_table3158
+ GCC_except_table3160
+ GCC_except_table3162
+ GCC_except_table3163
+ GCC_except_table3164
+ GCC_except_table3165
+ GCC_except_table3166
+ GCC_except_table3167
+ GCC_except_table3168
+ GCC_except_table3169
+ GCC_except_table317
+ GCC_except_table3170
+ GCC_except_table3171
+ GCC_except_table3172
+ GCC_except_table3173
+ GCC_except_table3174
+ GCC_except_table3175
+ GCC_except_table3176
+ GCC_except_table3177
+ GCC_except_table3179
+ GCC_except_table3180
+ GCC_except_table3181
+ GCC_except_table3182
+ GCC_except_table3183
+ GCC_except_table3184
+ GCC_except_table3188
+ GCC_except_table3191
+ GCC_except_table3205
+ GCC_except_table3213
+ GCC_except_table324
+ GCC_except_table3255
+ GCC_except_table3257
+ GCC_except_table3258
+ GCC_except_table3268
+ GCC_except_table3309
+ GCC_except_table3329
+ GCC_except_table3330
+ GCC_except_table3333
+ GCC_except_table3343
+ GCC_except_table3344
+ GCC_except_table3346
+ GCC_except_table3347
+ GCC_except_table3350
+ GCC_except_table3351
+ GCC_except_table3352
+ GCC_except_table3360
+ GCC_except_table3391
+ GCC_except_table3395
+ GCC_except_table3397
+ GCC_except_table3398
+ GCC_except_table3399
+ GCC_except_table3400
+ GCC_except_table3403
+ GCC_except_table3409
+ GCC_except_table3410
+ GCC_except_table3414
+ GCC_except_table3418
+ GCC_except_table3419
+ GCC_except_table3420
+ GCC_except_table3421
+ GCC_except_table3424
+ GCC_except_table3425
+ GCC_except_table3433
+ GCC_except_table3450
+ GCC_except_table3452
+ GCC_except_table3453
+ GCC_except_table3454
+ GCC_except_table3455
+ GCC_except_table3457
+ GCC_except_table3458
+ GCC_except_table3478
+ GCC_except_table3479
+ GCC_except_table3484
+ GCC_except_table3487
+ GCC_except_table350
+ GCC_except_table3502
+ GCC_except_table3505
+ GCC_except_table3506
+ GCC_except_table3507
+ GCC_except_table3509
+ GCC_except_table3511
+ GCC_except_table3512
+ GCC_except_table3514
+ GCC_except_table3515
+ GCC_except_table3516
+ GCC_except_table3518
+ GCC_except_table3521
+ GCC_except_table3523
+ GCC_except_table3532
+ GCC_except_table3533
+ GCC_except_table3536
+ GCC_except_table3537
+ GCC_except_table3538
+ GCC_except_table3539
+ GCC_except_table3541
+ GCC_except_table3542
+ GCC_except_table3544
+ GCC_except_table3548
+ GCC_except_table3550
+ GCC_except_table3553
+ GCC_except_table3557
+ GCC_except_table3563
+ GCC_except_table3564
+ GCC_except_table3565
+ GCC_except_table3567
+ GCC_except_table358
+ GCC_except_table3581
+ GCC_except_table3582
+ GCC_except_table3586
+ GCC_except_table3598
+ GCC_except_table3605
+ GCC_except_table3606
+ GCC_except_table3607
+ GCC_except_table3608
+ GCC_except_table3609
+ GCC_except_table3610
+ GCC_except_table3611
+ GCC_except_table3612
+ GCC_except_table3614
+ GCC_except_table3617
+ GCC_except_table3629
+ GCC_except_table3631
+ GCC_except_table3632
+ GCC_except_table3633
+ GCC_except_table3637
+ GCC_except_table3638
+ GCC_except_table3640
+ GCC_except_table3641
+ GCC_except_table3642
+ GCC_except_table3647
+ GCC_except_table3648
+ GCC_except_table3651
+ GCC_except_table3653
+ GCC_except_table3654
+ GCC_except_table3659
+ GCC_except_table3660
+ GCC_except_table3661
+ GCC_except_table3662
+ GCC_except_table3663
+ GCC_except_table3665
+ GCC_except_table3666
+ GCC_except_table3667
+ GCC_except_table3668
+ GCC_except_table3669
+ GCC_except_table3670
+ GCC_except_table3671
+ GCC_except_table3672
+ GCC_except_table3678
+ GCC_except_table368
+ GCC_except_table3684
+ GCC_except_table3689
+ GCC_except_table3696
+ GCC_except_table3697
+ GCC_except_table3700
+ GCC_except_table3704
+ GCC_except_table3707
+ GCC_except_table3708
+ GCC_except_table371
+ GCC_except_table3720
+ GCC_except_table3721
+ GCC_except_table3722
+ GCC_except_table373
+ GCC_except_table3742
+ GCC_except_table3748
+ GCC_except_table3750
+ GCC_except_table3758
+ GCC_except_table3769
+ GCC_except_table379
+ GCC_except_table3793
+ GCC_except_table3795
+ GCC_except_table3800
+ GCC_except_table3802
+ GCC_except_table3812
+ GCC_except_table3815
+ GCC_except_table3817
+ GCC_except_table383
+ GCC_except_table3846
+ GCC_except_table3849
+ GCC_except_table3927
+ GCC_except_table3939
+ GCC_except_table3942
+ GCC_except_table3944
+ GCC_except_table3948
+ GCC_except_table3949
+ GCC_except_table3951
+ GCC_except_table3952
+ GCC_except_table3969
+ GCC_except_table3990
+ GCC_except_table4
+ GCC_except_table40
+ GCC_except_table4007
+ GCC_except_table4018
+ GCC_except_table402
+ GCC_except_table4020
+ GCC_except_table4025
+ GCC_except_table4026
+ GCC_except_table4027
+ GCC_except_table4029
+ GCC_except_table4030
+ GCC_except_table4032
+ GCC_except_table4033
+ GCC_except_table4037
+ GCC_except_table4038
+ GCC_except_table4040
+ GCC_except_table4041
+ GCC_except_table4044
+ GCC_except_table4047
+ GCC_except_table4053
+ GCC_except_table4054
+ GCC_except_table4055
+ GCC_except_table4058
+ GCC_except_table4059
+ GCC_except_table4060
+ GCC_except_table4062
+ GCC_except_table4065
+ GCC_except_table4067
+ GCC_except_table4075
+ GCC_except_table4076
+ GCC_except_table4080
+ GCC_except_table4082
+ GCC_except_table4083
+ GCC_except_table4084
+ GCC_except_table4086
+ GCC_except_table4092
+ GCC_except_table4093
+ GCC_except_table4094
+ GCC_except_table4096
+ GCC_except_table4099
+ GCC_except_table4100
+ GCC_except_table4101
+ GCC_except_table4102
+ GCC_except_table4109
+ GCC_except_table411
+ GCC_except_table4111
+ GCC_except_table4121
+ GCC_except_table4122
+ GCC_except_table4123
+ GCC_except_table4129
+ GCC_except_table4133
+ GCC_except_table4152
+ GCC_except_table4154
+ GCC_except_table4156
+ GCC_except_table4161
+ GCC_except_table4163
+ GCC_except_table422
+ GCC_except_table4220
+ GCC_except_table4222
+ GCC_except_table4223
+ GCC_except_table4224
+ GCC_except_table4225
+ GCC_except_table4228
+ GCC_except_table4239
+ GCC_except_table4249
+ GCC_except_table425
+ GCC_except_table4250
+ GCC_except_table4252
+ GCC_except_table4253
+ GCC_except_table4254
+ GCC_except_table4255
+ GCC_except_table4256
+ GCC_except_table4257
+ GCC_except_table4258
+ GCC_except_table4260
+ GCC_except_table4261
+ GCC_except_table4275
+ GCC_except_table4281
+ GCC_except_table4295
+ GCC_except_table4296
+ GCC_except_table4309
+ GCC_except_table4310
+ GCC_except_table4325
+ GCC_except_table4326
+ GCC_except_table4327
+ GCC_except_table4328
+ GCC_except_table4331
+ GCC_except_table4342
+ GCC_except_table4343
+ GCC_except_table4345
+ GCC_except_table4359
+ GCC_except_table4360
+ GCC_except_table4366
+ GCC_except_table4367
+ GCC_except_table4368
+ GCC_except_table4369
+ GCC_except_table4370
+ GCC_except_table4371
+ GCC_except_table4372
+ GCC_except_table4373
+ GCC_except_table4382
+ GCC_except_table4383
+ GCC_except_table4395
+ GCC_except_table4396
+ GCC_except_table4397
+ GCC_except_table4399
+ GCC_except_table44
+ GCC_except_table4400
+ GCC_except_table4403
+ GCC_except_table4410
+ GCC_except_table4422
+ GCC_except_table4425
+ GCC_except_table4427
+ GCC_except_table4428
+ GCC_except_table4430
+ GCC_except_table4431
+ GCC_except_table4451
+ GCC_except_table4454
+ GCC_except_table4456
+ GCC_except_table4459
+ GCC_except_table4462
+ GCC_except_table4469
+ GCC_except_table4481
+ GCC_except_table4482
+ GCC_except_table4484
+ GCC_except_table4485
+ GCC_except_table4486
+ GCC_except_table4487
+ GCC_except_table4489
+ GCC_except_table4490
+ GCC_except_table4492
+ GCC_except_table4493
+ GCC_except_table4495
+ GCC_except_table450
+ GCC_except_table4502
+ GCC_except_table4514
+ GCC_except_table4518
+ GCC_except_table4520
+ GCC_except_table4540
+ GCC_except_table4542
+ GCC_except_table4543
+ GCC_except_table4544
+ GCC_except_table4545
+ GCC_except_table4551
+ GCC_except_table4552
+ GCC_except_table4554
+ GCC_except_table456
+ GCC_except_table457
+ GCC_except_table459
+ GCC_except_table46
+ GCC_except_table4615
+ GCC_except_table4616
+ GCC_except_table4617
+ GCC_except_table4679
+ GCC_except_table4695
+ GCC_except_table47
+ GCC_except_table4704
+ GCC_except_table4716
+ GCC_except_table4718
+ GCC_except_table475
+ GCC_except_table480
+ GCC_except_table483
+ GCC_except_table4841
+ GCC_except_table4842
+ GCC_except_table4843
+ GCC_except_table4845
+ GCC_except_table4846
+ GCC_except_table4851
+ GCC_except_table4853
+ GCC_except_table4854
+ GCC_except_table4855
+ GCC_except_table4856
+ GCC_except_table4857
+ GCC_except_table4858
+ GCC_except_table486
+ GCC_except_table4867
+ GCC_except_table487
+ GCC_except_table4871
+ GCC_except_table4872
+ GCC_except_table4873
+ GCC_except_table4877
+ GCC_except_table4878
+ GCC_except_table4879
+ GCC_except_table488
+ GCC_except_table4885
+ GCC_except_table4894
+ GCC_except_table4897
+ GCC_except_table4900
+ GCC_except_table4908
+ GCC_except_table4909
+ GCC_except_table4915
+ GCC_except_table492
+ GCC_except_table4929
+ GCC_except_table4930
+ GCC_except_table4931
+ GCC_except_table4932
+ GCC_except_table4933
+ GCC_except_table4936
+ GCC_except_table4937
+ GCC_except_table4942
+ GCC_except_table4943
+ GCC_except_table4945
+ GCC_except_table4947
+ GCC_except_table495
+ GCC_except_table4951
+ GCC_except_table4957
+ GCC_except_table4959
+ GCC_except_table4960
+ GCC_except_table4961
+ GCC_except_table4965
+ GCC_except_table4966
+ GCC_except_table4967
+ GCC_except_table4968
+ GCC_except_table4969
+ GCC_except_table4971
+ GCC_except_table4972
+ GCC_except_table4977
+ GCC_except_table4981
+ GCC_except_table4982
+ GCC_except_table4987
+ GCC_except_table4988
+ GCC_except_table499
+ GCC_except_table4992
+ GCC_except_table4997
+ GCC_except_table4998
+ GCC_except_table4999
+ GCC_except_table5001
+ GCC_except_table5006
+ GCC_except_table5007
+ GCC_except_table5008
+ GCC_except_table5012
+ GCC_except_table5013
+ GCC_except_table5014
+ GCC_except_table5017
+ GCC_except_table5019
+ GCC_except_table502
+ GCC_except_table5021
+ GCC_except_table5024
+ GCC_except_table5026
+ GCC_except_table5028
+ GCC_except_table503
+ GCC_except_table5031
+ GCC_except_table5032
+ GCC_except_table5034
+ GCC_except_table504
+ GCC_except_table5041
+ GCC_except_table5042
+ GCC_except_table5043
+ GCC_except_table5045
+ GCC_except_table5047
+ GCC_except_table5051
+ GCC_except_table5052
+ GCC_except_table5054
+ GCC_except_table5058
+ GCC_except_table506
+ GCC_except_table507
+ GCC_except_table5077
+ GCC_except_table508
+ GCC_except_table5080
+ GCC_except_table5087
+ GCC_except_table509
+ GCC_except_table5100
+ GCC_except_table5102
+ GCC_except_table5105
+ GCC_except_table5106
+ GCC_except_table5107
+ GCC_except_table5110
+ GCC_except_table5111
+ GCC_except_table5112
+ GCC_except_table5113
+ GCC_except_table5124
+ GCC_except_table5129
+ GCC_except_table5132
+ GCC_except_table5133
+ GCC_except_table5134
+ GCC_except_table5135
+ GCC_except_table5137
+ GCC_except_table5144
+ GCC_except_table5145
+ GCC_except_table5146
+ GCC_except_table5150
+ GCC_except_table5152
+ GCC_except_table5156
+ GCC_except_table5157
+ GCC_except_table5158
+ GCC_except_table5159
+ GCC_except_table516
+ GCC_except_table5161
+ GCC_except_table5162
+ GCC_except_table517
+ GCC_except_table5174
+ GCC_except_table5177
+ GCC_except_table52
+ GCC_except_table528
+ GCC_except_table53
+ GCC_except_table531
+ GCC_except_table532
+ GCC_except_table533
+ GCC_except_table534
+ GCC_except_table535
+ GCC_except_table536
+ GCC_except_table537
+ GCC_except_table54
+ GCC_except_table548
+ GCC_except_table549
+ GCC_except_table56
+ GCC_except_table564
+ GCC_except_table567
+ GCC_except_table57
+ GCC_except_table571
+ GCC_except_table572
+ GCC_except_table574
+ GCC_except_table59
+ GCC_except_table60
+ GCC_except_table6084
+ GCC_except_table6085
+ GCC_except_table6086
+ GCC_except_table609
+ GCC_except_table6109
+ GCC_except_table6110
+ GCC_except_table6115
+ GCC_except_table6117
+ GCC_except_table6119
+ GCC_except_table6121
+ GCC_except_table6123
+ GCC_except_table6125
+ GCC_except_table6127
+ GCC_except_table6129
+ GCC_except_table6131
+ GCC_except_table6155
+ GCC_except_table617
+ GCC_except_table6217
+ GCC_except_table6232
+ GCC_except_table6233
+ GCC_except_table6234
+ GCC_except_table6238
+ GCC_except_table6241
+ GCC_except_table6243
+ GCC_except_table6245
+ GCC_except_table6247
+ GCC_except_table6255
+ GCC_except_table6259
+ GCC_except_table6260
+ GCC_except_table6266
+ GCC_except_table6270
+ GCC_except_table6272
+ GCC_except_table6282
+ GCC_except_table6292
+ GCC_except_table6294
+ GCC_except_table6300
+ GCC_except_table6302
+ GCC_except_table6303
+ GCC_except_table6307
+ GCC_except_table6309
+ GCC_except_table6312
+ GCC_except_table6317
+ GCC_except_table6319
+ GCC_except_table6331
+ GCC_except_table6337
+ GCC_except_table6346
+ GCC_except_table6348
+ GCC_except_table6349
+ GCC_except_table635
+ GCC_except_table6350
+ GCC_except_table6351
+ GCC_except_table6356
+ GCC_except_table6357
+ GCC_except_table636
+ GCC_except_table6362
+ GCC_except_table6363
+ GCC_except_table6366
+ GCC_except_table637
+ GCC_except_table6370
+ GCC_except_table6376
+ GCC_except_table6377
+ GCC_except_table6378
+ GCC_except_table6379
+ GCC_except_table638
+ GCC_except_table6381
+ GCC_except_table6382
+ GCC_except_table6386
+ GCC_except_table6387
+ GCC_except_table6388
+ GCC_except_table6389
+ GCC_except_table639
+ GCC_except_table6397
+ GCC_except_table6399
+ GCC_except_table64
+ GCC_except_table640
+ GCC_except_table6404
+ GCC_except_table6414
+ GCC_except_table6428
+ GCC_except_table643
+ GCC_except_table6445
+ GCC_except_table6447
+ GCC_except_table6451
+ GCC_except_table646
+ GCC_except_table6469
+ GCC_except_table647
+ GCC_except_table6481
+ GCC_except_table6483
+ GCC_except_table6485
+ GCC_except_table649
+ GCC_except_table6490
+ GCC_except_table65
+ GCC_except_table6507
+ GCC_except_table651
+ GCC_except_table6513
+ GCC_except_table6514
+ GCC_except_table6517
+ GCC_except_table6518
+ GCC_except_table652
+ GCC_except_table6520
+ GCC_except_table6521
+ GCC_except_table6522
+ GCC_except_table6524
+ GCC_except_table6526
+ GCC_except_table6529
+ GCC_except_table6534
+ GCC_except_table6539
+ GCC_except_table6541
+ GCC_except_table6546
+ GCC_except_table6547
+ GCC_except_table6549
+ GCC_except_table6550
+ GCC_except_table6567
+ GCC_except_table6569
+ GCC_except_table6573
+ GCC_except_table6574
+ GCC_except_table6576
+ GCC_except_table6577
+ GCC_except_table6578
+ GCC_except_table6582
+ GCC_except_table6583
+ GCC_except_table6599
+ GCC_except_table66
+ GCC_except_table6604
+ GCC_except_table6606
+ GCC_except_table6607
+ GCC_except_table6609
+ GCC_except_table662
+ GCC_except_table6621
+ GCC_except_table6632
+ GCC_except_table6633
+ GCC_except_table6634
+ GCC_except_table6636
+ GCC_except_table6640
+ GCC_except_table6642
+ GCC_except_table6643
+ GCC_except_table6644
+ GCC_except_table6645
+ GCC_except_table6650
+ GCC_except_table6670
+ GCC_except_table6671
+ GCC_except_table6673
+ GCC_except_table6675
+ GCC_except_table6679
+ GCC_except_table6680
+ GCC_except_table6683
+ GCC_except_table6684
+ GCC_except_table6685
+ GCC_except_table6687
+ GCC_except_table6688
+ GCC_except_table6689
+ GCC_except_table669
+ GCC_except_table67
+ GCC_except_table6700
+ GCC_except_table671
+ GCC_except_table6718
+ GCC_except_table672
+ GCC_except_table6725
+ GCC_except_table6727
+ GCC_except_table6728
+ GCC_except_table673
+ GCC_except_table6730
+ GCC_except_table6731
+ GCC_except_table674
+ GCC_except_table6742
+ GCC_except_table6743
+ GCC_except_table6744
+ GCC_except_table675
+ GCC_except_table6756
+ GCC_except_table676
+ GCC_except_table677
+ GCC_except_table678
+ GCC_except_table679
+ GCC_except_table6796
+ GCC_except_table68
+ GCC_except_table680
+ GCC_except_table6802
+ GCC_except_table6805
+ GCC_except_table6806
+ GCC_except_table6807
+ GCC_except_table681
+ GCC_except_table6810
+ GCC_except_table6812
+ GCC_except_table6816
+ GCC_except_table6818
+ GCC_except_table6819
+ GCC_except_table682
+ GCC_except_table6820
+ GCC_except_table6821
+ GCC_except_table6822
+ GCC_except_table6823
+ GCC_except_table683
+ GCC_except_table6832
+ GCC_except_table6834
+ GCC_except_table6837
+ GCC_except_table6838
+ GCC_except_table684
+ GCC_except_table6840
+ GCC_except_table6841
+ GCC_except_table685
+ GCC_except_table6852
+ GCC_except_table6854
+ GCC_except_table6859
+ GCC_except_table686
+ GCC_except_table6861
+ GCC_except_table6862
+ GCC_except_table6863
+ GCC_except_table6864
+ GCC_except_table6865
+ GCC_except_table6866
+ GCC_except_table6868
+ GCC_except_table6869
+ GCC_except_table687
+ GCC_except_table6870
+ GCC_except_table6871
+ GCC_except_table6872
+ GCC_except_table6873
+ GCC_except_table6874
+ GCC_except_table688
+ GCC_except_table6885
+ GCC_except_table6886
+ GCC_except_table6889
+ GCC_except_table6891
+ GCC_except_table6892
+ GCC_except_table6893
+ GCC_except_table6894
+ GCC_except_table6895
+ GCC_except_table6896
+ GCC_except_table6897
+ GCC_except_table6900
+ GCC_except_table6901
+ GCC_except_table6902
+ GCC_except_table6903
+ GCC_except_table6904
+ GCC_except_table6909
+ GCC_except_table6914
+ GCC_except_table6921
+ GCC_except_table6926
+ GCC_except_table6929
+ GCC_except_table6938
+ GCC_except_table6939
+ GCC_except_table6956
+ GCC_except_table6957
+ GCC_except_table6958
+ GCC_except_table6959
+ GCC_except_table6960
+ GCC_except_table6965
+ GCC_except_table697
+ GCC_except_table6982
+ GCC_except_table700
+ GCC_except_table701
+ GCC_except_table7010
+ GCC_except_table7012
+ GCC_except_table7013
+ GCC_except_table703
+ GCC_except_table704
+ GCC_except_table7054
+ GCC_except_table7055
+ GCC_except_table7057
+ GCC_except_table706
+ GCC_except_table7060
+ GCC_except_table7061
+ GCC_except_table7063
+ GCC_except_table7064
+ GCC_except_table7067
+ GCC_except_table7069
+ GCC_except_table708
+ GCC_except_table709
+ GCC_except_table7093
+ GCC_except_table7094
+ GCC_except_table7097
+ GCC_except_table7098
+ GCC_except_table7101
+ GCC_except_table7104
+ GCC_except_table7105
+ GCC_except_table7106
+ GCC_except_table7107
+ GCC_except_table7108
+ GCC_except_table711
+ GCC_except_table7110
+ GCC_except_table7111
+ GCC_except_table7112
+ GCC_except_table7113
+ GCC_except_table7115
+ GCC_except_table7117
+ GCC_except_table7119
+ GCC_except_table7135
+ GCC_except_table7138
+ GCC_except_table714
+ GCC_except_table7151
+ GCC_except_table7152
+ GCC_except_table7153
+ GCC_except_table7154
+ GCC_except_table7155
+ GCC_except_table7156
+ GCC_except_table7161
+ GCC_except_table7162
+ GCC_except_table7163
+ GCC_except_table7164
+ GCC_except_table717
+ GCC_except_table718
+ GCC_except_table7185
+ GCC_except_table7199
+ GCC_except_table7213
+ GCC_except_table7227
+ GCC_except_table7228
+ GCC_except_table7241
+ GCC_except_table7255
+ GCC_except_table7261
+ GCC_except_table7263
+ GCC_except_table7277
+ GCC_except_table7279
+ GCC_except_table7298
+ GCC_except_table73
+ GCC_except_table7306
+ GCC_except_table7314
+ GCC_except_table7316
+ GCC_except_table7318
+ GCC_except_table7322
+ GCC_except_table7327
+ GCC_except_table7330
+ GCC_except_table7335
+ GCC_except_table7337
+ GCC_except_table7339
+ GCC_except_table7341
+ GCC_except_table7354
+ GCC_except_table7356
+ GCC_except_table7358
+ GCC_except_table737
+ GCC_except_table7371
+ GCC_except_table7372
+ GCC_except_table7373
+ GCC_except_table7374
+ GCC_except_table7377
+ GCC_except_table7378
+ GCC_except_table7379
+ GCC_except_table7386
+ GCC_except_table7388
+ GCC_except_table7389
+ GCC_except_table7390
+ GCC_except_table7391
+ GCC_except_table7392
+ GCC_except_table7397
+ GCC_except_table74
+ GCC_except_table7400
+ GCC_except_table7404
+ GCC_except_table7407
+ GCC_except_table7409
+ GCC_except_table7412
+ GCC_except_table7413
+ GCC_except_table7414
+ GCC_except_table7424
+ GCC_except_table7425
+ GCC_except_table7427
+ GCC_except_table7428
+ GCC_except_table7429
+ GCC_except_table7439
+ GCC_except_table744
+ GCC_except_table7444
+ GCC_except_table745
+ GCC_except_table7450
+ GCC_except_table7451
+ GCC_except_table7459
+ GCC_except_table7460
+ GCC_except_table7465
+ GCC_except_table7478
+ GCC_except_table7483
+ GCC_except_table7490
+ GCC_except_table7491
+ GCC_except_table7508
+ GCC_except_table752
+ GCC_except_table7531
+ GCC_except_table7535
+ GCC_except_table7536
+ GCC_except_table7537
+ GCC_except_table7538
+ GCC_except_table7539
+ GCC_except_table7540
+ GCC_except_table7541
+ GCC_except_table7543
+ GCC_except_table7575
+ GCC_except_table7577
+ GCC_except_table7584
+ GCC_except_table7585
+ GCC_except_table7586
+ GCC_except_table76
+ GCC_except_table7600
+ GCC_except_table7601
+ GCC_except_table7604
+ GCC_except_table7608
+ GCC_except_table7610
+ GCC_except_table7612
+ GCC_except_table7631
+ GCC_except_table7634
+ GCC_except_table7641
+ GCC_except_table7662
+ GCC_except_table7663
+ GCC_except_table7664
+ GCC_except_table7665
+ GCC_except_table7666
+ GCC_except_table767
+ GCC_except_table7677
+ GCC_except_table7678
+ GCC_except_table7680
+ GCC_except_table7684
+ GCC_except_table7685
+ GCC_except_table7688
+ GCC_except_table7690
+ GCC_except_table7691
+ GCC_except_table7693
+ GCC_except_table7696
+ GCC_except_table7698
+ GCC_except_table77
+ GCC_except_table7702
+ GCC_except_table7711
+ GCC_except_table7713
+ GCC_except_table7717
+ GCC_except_table7719
+ GCC_except_table7721
+ GCC_except_table7723
+ GCC_except_table7725
+ GCC_except_table7727
+ GCC_except_table7728
+ GCC_except_table7729
+ GCC_except_table7735
+ GCC_except_table7737
+ GCC_except_table7739
+ GCC_except_table7741
+ GCC_except_table7743
+ GCC_except_table7747
+ GCC_except_table7748
+ GCC_except_table7750
+ GCC_except_table7751
+ GCC_except_table7756
+ GCC_except_table7759
+ GCC_except_table7761
+ GCC_except_table7763
+ GCC_except_table7765
+ GCC_except_table7767
+ GCC_except_table7769
+ GCC_except_table7771
+ GCC_except_table7772
+ GCC_except_table7774
+ GCC_except_table7776
+ GCC_except_table7777
+ GCC_except_table7779
+ GCC_except_table7780
+ GCC_except_table7782
+ GCC_except_table7784
+ GCC_except_table7786
+ GCC_except_table779
+ GCC_except_table7791
+ GCC_except_table7792
+ GCC_except_table7794
+ GCC_except_table7802
+ GCC_except_table7803
+ GCC_except_table7807
+ GCC_except_table781
+ GCC_except_table7810
+ GCC_except_table782
+ GCC_except_table7821
+ GCC_except_table7822
+ GCC_except_table7827
+ GCC_except_table7829
+ GCC_except_table7836
+ GCC_except_table7837
+ GCC_except_table7838
+ GCC_except_table7839
+ GCC_except_table7840
+ GCC_except_table7841
+ GCC_except_table7842
+ GCC_except_table7849
+ GCC_except_table785
+ GCC_except_table7850
+ GCC_except_table7851
+ GCC_except_table7852
+ GCC_except_table7853
+ GCC_except_table7854
+ GCC_except_table7855
+ GCC_except_table7863
+ GCC_except_table7866
+ GCC_except_table7869
+ GCC_except_table7873
+ GCC_except_table7878
+ GCC_except_table7879
+ GCC_except_table7886
+ GCC_except_table7888
+ GCC_except_table7894
+ GCC_except_table79
+ GCC_except_table7901
+ GCC_except_table7902
+ GCC_except_table7908
+ GCC_except_table7909
+ GCC_except_table7923
+ GCC_except_table7926
+ GCC_except_table7941
+ GCC_except_table7942
+ GCC_except_table7943
+ GCC_except_table7945
+ GCC_except_table7949
+ GCC_except_table7951
+ GCC_except_table7952
+ GCC_except_table7953
+ GCC_except_table7963
+ GCC_except_table7979
+ GCC_except_table7980
+ GCC_except_table7981
+ GCC_except_table7982
+ GCC_except_table7983
+ GCC_except_table7988
+ GCC_except_table7989
+ GCC_except_table7993
+ GCC_except_table80
+ GCC_except_table8000
+ GCC_except_table8001
+ GCC_except_table8003
+ GCC_except_table8013
+ GCC_except_table8027
+ GCC_except_table8029
+ GCC_except_table8034
+ GCC_except_table8036
+ GCC_except_table8038
+ GCC_except_table8043
+ GCC_except_table8046
+ GCC_except_table8047
+ GCC_except_table8050
+ GCC_except_table8052
+ GCC_except_table8054
+ GCC_except_table8056
+ GCC_except_table8057
+ GCC_except_table8058
+ GCC_except_table8080
+ GCC_except_table8094
+ GCC_except_table8097
+ GCC_except_table81
+ GCC_except_table8101
+ GCC_except_table8102
+ GCC_except_table8103
+ GCC_except_table813
+ GCC_except_table8131
+ GCC_except_table8135
+ GCC_except_table8136
+ GCC_except_table8138
+ GCC_except_table8146
+ GCC_except_table8147
+ GCC_except_table8148
+ GCC_except_table8149
+ GCC_except_table815
+ GCC_except_table8153
+ GCC_except_table816
+ GCC_except_table8163
+ GCC_except_table8166
+ GCC_except_table8167
+ GCC_except_table8168
+ GCC_except_table8170
+ GCC_except_table8171
+ GCC_except_table8174
+ GCC_except_table8175
+ GCC_except_table818
+ GCC_except_table819
+ GCC_except_table8193
+ GCC_except_table822
+ GCC_except_table8222
+ GCC_except_table8253
+ GCC_except_table8261
+ GCC_except_table8263
+ GCC_except_table8264
+ GCC_except_table8265
+ GCC_except_table8268
+ GCC_except_table8277
+ GCC_except_table8280
+ GCC_except_table8288
+ GCC_except_table8295
+ GCC_except_table8296
+ GCC_except_table8297
+ GCC_except_table8298
+ GCC_except_table8310
+ GCC_except_table8311
+ GCC_except_table8326
+ GCC_except_table8327
+ GCC_except_table8329
+ GCC_except_table8335
+ GCC_except_table834
+ GCC_except_table8342
+ GCC_except_table8343
+ GCC_except_table8344
+ GCC_except_table8347
+ GCC_except_table8348
+ GCC_except_table8349
+ GCC_except_table835
+ GCC_except_table8350
+ GCC_except_table8351
+ GCC_except_table8357
+ GCC_except_table8358
+ GCC_except_table8359
+ GCC_except_table836
+ GCC_except_table8365
+ GCC_except_table837
+ GCC_except_table8402
+ GCC_except_table8403
+ GCC_except_table8405
+ GCC_except_table8411
+ GCC_except_table8426
+ GCC_except_table8427
+ GCC_except_table8433
+ GCC_except_table8444
+ GCC_except_table8445
+ GCC_except_table8448
+ GCC_except_table8449
+ GCC_except_table8450
+ GCC_except_table8451
+ GCC_except_table8453
+ GCC_except_table8455
+ GCC_except_table8458
+ GCC_except_table846
+ GCC_except_table8460
+ GCC_except_table8476
+ GCC_except_table8477
+ GCC_except_table8487
+ GCC_except_table8488
+ GCC_except_table8489
+ GCC_except_table8490
+ GCC_except_table8493
+ GCC_except_table8495
+ GCC_except_table8499
+ GCC_except_table8510
+ GCC_except_table8518
+ GCC_except_table852
+ GCC_except_table8526
+ GCC_except_table8534
+ GCC_except_table8550
+ GCC_except_table8558
+ GCC_except_table8566
+ GCC_except_table8575
+ GCC_except_table858
+ GCC_except_table8583
+ GCC_except_table8592
+ GCC_except_table8593
+ GCC_except_table8594
+ GCC_except_table8595
+ GCC_except_table8596
+ GCC_except_table8598
+ GCC_except_table86
+ GCC_except_table861
+ GCC_except_table8611
+ GCC_except_table8613
+ GCC_except_table862
+ GCC_except_table8621
+ GCC_except_table8622
+ GCC_except_table8624
+ GCC_except_table8625
+ GCC_except_table8629
+ GCC_except_table8633
+ GCC_except_table8635
+ GCC_except_table8639
+ GCC_except_table864
+ GCC_except_table8640
+ GCC_except_table8641
+ GCC_except_table8642
+ GCC_except_table8643
+ GCC_except_table8644
+ GCC_except_table8645
+ GCC_except_table8646
+ GCC_except_table8647
+ GCC_except_table8648
+ GCC_except_table8649
+ GCC_except_table865
+ GCC_except_table8650
+ GCC_except_table8651
+ GCC_except_table8653
+ GCC_except_table8655
+ GCC_except_table8656
+ GCC_except_table8657
+ GCC_except_table8658
+ GCC_except_table8659
+ GCC_except_table866
+ GCC_except_table8660
+ GCC_except_table8661
+ GCC_except_table8662
+ GCC_except_table8663
+ GCC_except_table8664
+ GCC_except_table8665
+ GCC_except_table8666
+ GCC_except_table8667
+ GCC_except_table8684
+ GCC_except_table8689
+ GCC_except_table8691
+ GCC_except_table8692
+ GCC_except_table8693
+ GCC_except_table8705
+ GCC_except_table8706
+ GCC_except_table8708
+ GCC_except_table872
+ GCC_except_table874
+ GCC_except_table877
+ GCC_except_table8810
+ GCC_except_table8834
+ GCC_except_table8835
+ GCC_except_table8850
+ GCC_except_table8861
+ GCC_except_table8862
+ GCC_except_table8866
+ GCC_except_table8868
+ GCC_except_table8869
+ GCC_except_table8873
+ GCC_except_table8877
+ GCC_except_table8885
+ GCC_except_table8886
+ GCC_except_table8896
+ GCC_except_table8900
+ GCC_except_table891
+ GCC_except_table8915
+ GCC_except_table8917
+ GCC_except_table8943
+ GCC_except_table8945
+ GCC_except_table8948
+ GCC_except_table8950
+ GCC_except_table8957
+ GCC_except_table8958
+ GCC_except_table8960
+ GCC_except_table8962
+ GCC_except_table8964
+ GCC_except_table8971
+ GCC_except_table8973
+ GCC_except_table8974
+ GCC_except_table8977
+ GCC_except_table8978
+ GCC_except_table8979
+ GCC_except_table8985
+ GCC_except_table8987
+ GCC_except_table8988
+ GCC_except_table8989
+ GCC_except_table8990
+ GCC_except_table8991
+ GCC_except_table8992
+ GCC_except_table8993
+ GCC_except_table8994
+ GCC_except_table8995
+ GCC_except_table8996
+ GCC_except_table8997
+ GCC_except_table8998
+ GCC_except_table9000
+ GCC_except_table9001
+ GCC_except_table9004
+ GCC_except_table9006
+ GCC_except_table9007
+ GCC_except_table9008
+ GCC_except_table9009
+ GCC_except_table9010
+ GCC_except_table9011
+ GCC_except_table9015
+ GCC_except_table9017
+ GCC_except_table9018
+ GCC_except_table9019
+ GCC_except_table9021
+ GCC_except_table9025
+ GCC_except_table9026
+ GCC_except_table9027
+ GCC_except_table9029
+ GCC_except_table9032
+ GCC_except_table9033
+ GCC_except_table9034
+ GCC_except_table9035
+ GCC_except_table9036
+ GCC_except_table9037
+ GCC_except_table9038
+ GCC_except_table9039
+ GCC_except_table9040
+ GCC_except_table9045
+ GCC_except_table9047
+ GCC_except_table9049
+ GCC_except_table9052
+ GCC_except_table9056
+ GCC_except_table9057
+ GCC_except_table9058
+ GCC_except_table9059
+ GCC_except_table9060
+ GCC_except_table9061
+ GCC_except_table9062
+ GCC_except_table9063
+ GCC_except_table9064
+ GCC_except_table9065
+ GCC_except_table9068
+ GCC_except_table9070
+ GCC_except_table9072
+ GCC_except_table9073
+ GCC_except_table9086
+ GCC_except_table9087
+ GCC_except_table9093
+ GCC_except_table9094
+ GCC_except_table9101
+ GCC_except_table9103
+ GCC_except_table9104
+ GCC_except_table9105
+ GCC_except_table9106
+ GCC_except_table9107
+ GCC_except_table9108
+ GCC_except_table9109
+ GCC_except_table9110
+ GCC_except_table9118
+ GCC_except_table9130
+ GCC_except_table9158
+ GCC_except_table9165
+ GCC_except_table9166
+ GCC_except_table9168
+ GCC_except_table9171
+ GCC_except_table9173
+ GCC_except_table9175
+ GCC_except_table9203
+ GCC_except_table9218
+ GCC_except_table9220
+ GCC_except_table9222
+ GCC_except_table9229
+ GCC_except_table9231
+ GCC_except_table9247
+ GCC_except_table9251
+ GCC_except_table9253
+ GCC_except_table9269
+ GCC_except_table9279
+ GCC_except_table928
+ GCC_except_table9281
+ GCC_except_table9283
+ GCC_except_table9287
+ GCC_except_table9289
+ GCC_except_table9290
+ GCC_except_table9295
+ GCC_except_table930
+ GCC_except_table9312
+ GCC_except_table9314
+ GCC_except_table9316
+ GCC_except_table9319
+ GCC_except_table9335
+ GCC_except_table9340
+ GCC_except_table9342
+ GCC_except_table9345
+ GCC_except_table9348
+ GCC_except_table9349
+ GCC_except_table9352
+ GCC_except_table9353
+ GCC_except_table9354
+ GCC_except_table9356
+ GCC_except_table9357
+ GCC_except_table9359
+ GCC_except_table9360
+ GCC_except_table9362
+ GCC_except_table9363
+ GCC_except_table9364
+ GCC_except_table9366
+ GCC_except_table9372
+ GCC_except_table9377
+ GCC_except_table9381
+ GCC_except_table9384
+ GCC_except_table9386
+ GCC_except_table9388
+ GCC_except_table9390
+ GCC_except_table9391
+ GCC_except_table9392
+ GCC_except_table9396
+ GCC_except_table9398
+ GCC_except_table9399
+ GCC_except_table9400
+ GCC_except_table9402
+ GCC_except_table9404
+ GCC_except_table9406
+ GCC_except_table9408
+ GCC_except_table9409
+ GCC_except_table9410
+ GCC_except_table9412
+ GCC_except_table9414
+ GCC_except_table9415
+ GCC_except_table9416
+ GCC_except_table9417
+ GCC_except_table9418
+ GCC_except_table9419
+ GCC_except_table9420
+ GCC_except_table9425
+ GCC_except_table9427
+ GCC_except_table9429
+ GCC_except_table9430
+ GCC_except_table9432
+ GCC_except_table9434
+ GCC_except_table9436
+ GCC_except_table9440
+ GCC_except_table9442
+ GCC_except_table9444
+ GCC_except_table9446
+ GCC_except_table9448
+ GCC_except_table9450
+ GCC_except_table9452
+ GCC_except_table9454
+ GCC_except_table9456
+ GCC_except_table9458
+ GCC_except_table9460
+ GCC_except_table9462
+ GCC_except_table9464
+ GCC_except_table9466
+ GCC_except_table9468
+ GCC_except_table9472
+ GCC_except_table9474
+ GCC_except_table9476
+ GCC_except_table9478
+ GCC_except_table9480
+ GCC_except_table9482
+ GCC_except_table9484
+ GCC_except_table9486
+ GCC_except_table9488
+ GCC_except_table9490
+ GCC_except_table9495
+ GCC_except_table9496
+ GCC_except_table9497
+ GCC_except_table9501
+ GCC_except_table9503
+ GCC_except_table9505
+ GCC_except_table9510
+ GCC_except_table9511
+ GCC_except_table9513
+ GCC_except_table9514
+ GCC_except_table9515
+ GCC_except_table9517
+ GCC_except_table9521
+ GCC_except_table9522
+ GCC_except_table9523
+ GCC_except_table9524
+ GCC_except_table9526
+ GCC_except_table9527
+ GCC_except_table9562
+ GCC_except_table9568
+ GCC_except_table9577
+ GCC_except_table9580
+ GCC_except_table9581
+ GCC_except_table9582
+ GCC_except_table9583
+ GCC_except_table9586
+ GCC_except_table9589
+ GCC_except_table9594
+ GCC_except_table960
+ GCC_except_table9600
+ GCC_except_table9601
+ GCC_except_table961
+ GCC_except_table9610
+ GCC_except_table9614
+ GCC_except_table962
+ GCC_except_table9645
+ GCC_except_table9646
+ GCC_except_table9676
+ GCC_except_table9677
+ GCC_except_table9678
+ GCC_except_table975
+ GCC_except_table976
+ _AQOfflineMixerRenderWithPacketDependencies
+ _AudioBufferList_GetMetadataFrame
+ _AudioConverterFillComplexBufferRealtimeSafe
+ _AudioConverterFillComplexBufferWithPacketDependencies
+ _AudioMetadataFrame_AppendEvent
+ _AudioMetadataFrame_BeginNew
+ _AudioMetadataFrame_Clear
+ _AudioMetadataFrame_GetHeader
+ _AudioUnitProcessMultiple
+ _CAAssertRtn
+ _CAVerboseAbort
+ _CFDictionaryApplyFunction
+ _CFGetRetainCount
+ _CFPreferencesCopyAppValue
+ _CFPreferencesCopyMultiple
+ _CFStringAppend
+ _CFStringAppendCharacters
+ _CFStringCreateMutable
+ _CFStringCreateMutableCopy
+ _CFStringCreateWithBytesNoCopy
+ _CFStringCreateWithCStringNoCopy
+ _CFStringFind
+ _CFStringHasPrefix
+ _GetACQThreadID
+ _OBJC_CLASS_$_ATBlurMixer
+ _OBJC_CLASS_$_AVHapticPlayerParameterCurve
+ _OBJC_CLASS_$_AVHapticPlayerParameterCurveControlPoint
+ _OBJC_CLASS_$_AVHapticProcessTaskToken
+ _OBJC_CLASS_$_AVVoiceTriggerServer
+ _OBJC_CLASS_$_AVVoiceTriggerServerHysteresisNotifier
+ _OBJC_CLASS_$_AVVoiceTriggerServerPortManager
+ _OBJC_CLASS_$_TranslatorClientDelegate
+ _OBJC_IVAR_$_ATAudioTapDescription._muteBehavior
+ _OBJC_IVAR_$_ATBlurMixer._isUplink
+ _OBJC_IVAR_$_ATBlurMixer.mAUDSPGraph
+ _OBJC_IVAR_$_ATBlurMixer.mBlurHoldTimeSec
+ _OBJC_IVAR_$_ATBlurMixer.mIsInitialized
+ _OBJC_IVAR_$_ATBlurMixer.mMaxFrames
+ _OBJC_IVAR_$_ATBlurMixer.mRemoteFeedbackFeatureEnabled
+ _OBJC_IVAR_$_ATBlurMixer.mStreamDescription
+ _OBJC_IVAR_$_ATBlurMixer.mTuningDirectory
+ _OBJC_IVAR_$_AVVoiceTriggerServer._afSiriActivationBuiltInMicVoiceFuncPtr
+ _OBJC_IVAR_$_AVVoiceTriggerServer._clientConnections
+ _OBJC_IVAR_$_AVVoiceTriggerServer._clsVTStateManager
+ _OBJC_IVAR_$_AVVoiceTriggerServer._mobileAssistantDylib
+ _OBJC_IVAR_$_AVVoiceTriggerServer._notificationQueue
+ _OBJC_IVAR_$_AVVoiceTriggerServer._serverListener
+ _OBJC_IVAR_$_AVVoiceTriggerServer._voiceTriggerDylib
+ _OBJC_IVAR_$_AVVoiceTriggerServer._vtStateManager
+ _OBJC_IVAR_$_AVVoiceTriggerServer.serverImpl
+ _OBJC_IVAR_$_AVVoiceTriggerServerHysteresisNotifier._portsToMonitor
+ _OBJC_IVAR_$_AVVoiceTriggerServerHysteresisNotifier._queue
+ _OBJC_IVAR_$_AVVoiceTriggerServerPortManager._generation
+ _OBJC_IVAR_$_AVVoiceTriggerServerPortManager._hysteresisDurationSeconds
+ _OBJC_IVAR_$_AVVoiceTriggerServerPortManager._lastStateSent
+ _OBJC_IVAR_$_AVVoiceTriggerServerPortManager._listeningEnabled
+ _OBJC_IVAR_$_AVVoiceTriggerServerPortManager._notificationBlock
+ _OBJC_IVAR_$_AVVoiceTriggerServerPortManager._portType
+ _OBJC_IVAR_$_TranslatorClientDelegate.mImpl
+ _OBJC_IVAR_$_TranslatorClientDelegate.mScope
+ _OBJC_METACLASS_$_ATBlurMixer
+ _OBJC_METACLASS_$_AVVoiceTriggerServer
+ _OBJC_METACLASS_$_AVVoiceTriggerServerHysteresisNotifier
+ _OBJC_METACLASS_$_AVVoiceTriggerServerPortManager
+ _OBJC_METACLASS_$_TranslatorClientDelegate
+ _TranslateAudioStreamPacketDependenciesBackward
+ _VoiceProcessorCreate
+ _VoiceProcessorCreate$delayInitStub
+ _VoiceProcessorGetVersion
+ _VoiceProcessorGetVersion$delayInitStub
+ __OBJC_$_INSTANCE_METHODS_ATBlurMixer
+ __OBJC_$_INSTANCE_METHODS_AVVoiceTriggerServer
+ __OBJC_$_INSTANCE_METHODS_AVVoiceTriggerServerHysteresisNotifier
+ __OBJC_$_INSTANCE_METHODS_AVVoiceTriggerServerPortManager
+ __OBJC_$_INSTANCE_METHODS_TranslatorClientDelegate
+ __OBJC_$_INSTANCE_VARIABLES_ATBlurMixer
+ __OBJC_$_INSTANCE_VARIABLES_AVVoiceTriggerServer
+ __OBJC_$_INSTANCE_VARIABLES_AVVoiceTriggerServerHysteresisNotifier
+ __OBJC_$_INSTANCE_VARIABLES_AVVoiceTriggerServerPortManager
+ __OBJC_$_INSTANCE_VARIABLES_TranslatorClientDelegate
+ __OBJC_$_PROP_LIST_ATBlurMixer
+ __OBJC_$_PROP_LIST_AVVoiceTriggerServer
+ __OBJC_$_PROP_LIST_AVVoiceTriggerServerHysteresisNotifier
+ __OBJC_$_PROP_LIST_AVVoiceTriggerServerPortManager
+ __OBJC_$_PROP_LIST_TranslatorClientDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CHHapticServerInterface
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_STSpeechTranslatorClientDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_STSpeechTranslatorClientDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_STSpeechTranslatorClientDelegate
+ __OBJC_$_PROTOCOL_REFS_STSpeechTranslatorClientDelegate
+ __OBJC_CLASS_PROTOCOLS_$_AVVoiceTriggerServer
+ __OBJC_CLASS_PROTOCOLS_$_TranslatorClientDelegate
+ __OBJC_CLASS_RO_$_ATBlurMixer
+ __OBJC_CLASS_RO_$_AVVoiceTriggerServer
+ __OBJC_CLASS_RO_$_AVVoiceTriggerServerHysteresisNotifier
+ __OBJC_CLASS_RO_$_AVVoiceTriggerServerPortManager
+ __OBJC_CLASS_RO_$_TranslatorClientDelegate
+ __OBJC_LABEL_PROTOCOL_$_STSpeechTranslatorClientDelegate
+ __OBJC_METACLASS_RO_$_ATBlurMixer
+ __OBJC_METACLASS_RO_$_AVVoiceTriggerServer
+ __OBJC_METACLASS_RO_$_AVVoiceTriggerServerHysteresisNotifier
+ __OBJC_METACLASS_RO_$_AVVoiceTriggerServerPortManager
+ __OBJC_METACLASS_RO_$_TranslatorClientDelegate
+ __OBJC_PROTOCOL_$_STSpeechTranslatorClientDelegate
+ __Z12gEDSubmixLogv
+ __Z15gEDProcessorLogv
+ __Z16NewAudioCapturer20AudioCapturerOptionsPKcS1_jPK27AudioStreamBasicDescriptionRS3_
+ __Z16setLMAULNMaxGainP14AQIONodeClientP8AQIONodef
+ __Z17CompleteTimestampI15XAudioTimeStampEbRT_RKS1_df
+ __Z18setLMAULNResetModeP14AQIONodeClientP8AQIONodef
+ __Z20gEDParallelSubmixLogv
+ __Z21IONodeSessionLogScopev
+ __Z21setLMAULNResetTimeoutP14AQIONodeClientP8AQIONodef
+ __Z22AUIOServer_StopIO_Privj13audit_token_tj
+ __Z22setLMAULNOutputCeilingP14AQIONodeClientP8AQIONodef
+ __Z22setLMAULNRenderQualityP14AQIONodeClientP8AQIONodef
+ __Z23setLMAULNLoudnessTargetP14AQIONodeClientP8AQIONodef
+ __Z24GetBehaviorForSSIDAndPIDjibbbjPPK14__CFDictionary
+ __Z24setLMAULNPeakLevelOffsetP14AQIONodeClientP8AQIONodef
+ __Z24setLMAULNWeightingFilterP14AQIONodeClientP8AQIONodef
+ __Z25setLMAULNAlgorithmVersionP14AQIONodeClientP8AQIONodef
+ __Z25setLMAULNEnableCompressorP14AQIONodeClientP8AQIONodef
+ __Z25setLMAULNLookaheadDelayMSP14AQIONodeClientP8AQIONodef
+ __Z26AudioQueueIOBindingChangedPv
+ __Z27setLMAULNLoudnessAfterResetP14AQIONodeClientP8AQIONodef
+ __Z29applyLMAULNLoudnessPropertiesP14AQIONodeClientP8AQIONodeRKN15LoudnessManager8SettingsE
+ __Z31setLMAULNUpwardCompressionRangeP14AQIONodeClientP8AQIONodef
+ __Z33setLMAULNDownwardCompressionRangeP14AQIONodeClientP8AQIONodef
+ __Z35getMinimalRampDurationForValueDeltaff
+ __Z35setLMAULNSideChainHighPassFrequencyP14AQIONodeClientP8AQIONodef
+ __ZGVZ12gEDSubmixLogvE6global
+ __ZGVZ15gEDProcessorLogvE6global
+ __ZGVZ20gEDParallelSubmixLogvE6global
+ __ZGVZ21IONodeSessionLogScopevE6global
+ __ZGVZL13GetAcousticIDvE13optionalValue.5354
+ __ZGVZL26ACQContextAssertionEnabledvE7enabled
+ __ZGVZL30gAudioTapHALReferenceStreamLogvE6global
+ __ZGVZN18SlicePlayerFactory8instanceEvE7factory
+ __ZGVZN21AVVoiceTriggerManager8instanceEvE8instance
+ __ZGVZN2AT11Translation18CallTranslatorBase17injectable_globalEvE16injectableGlobal
+ __ZGVZN2AT13SessionFacadeL34PopulateSourceFormatInfoDictionaryEP14__CFDictionaryPKvRK14AQIONodeClientRN2CA17StreamDescriptionEbbbE10sessionMap
+ __ZGVZZN2AT11Translation18CallTranslatorBase17injectable_globalEvENK3$_0clEvE4impl
+ __ZL11CPMSLibraryv.10441
+ __ZL11CPMSLibraryv.3467
+ __ZL16audit_stringCPMS.10456
+ __ZL16audit_stringCPMS.3484
+ __ZL16audit_stringCPMS.6318
+ __ZL18gAQMEClientCapture
+ __ZL18kVoiceTriggerScope
+ __ZL19gHasVoiceTriggerXPC
+ __ZL19gSupportsAHAPForSSS
+ __ZL19sVoiceTriggerServer
+ __ZL20CoreMediaLibraryCorePPc.7055
+ __ZL20audit_stringAVFAudio.12643
+ __ZL21audit_stringCoreMedia.5039
+ __ZL21audit_stringCoreMedia.7064
+ __ZL21gAQMETimePitchCapture
+ __ZL22gAQCaptureOutputDecode
+ __ZL22gOutputCapturesEnabled
+ __ZL23MediaToolboxLibraryCorePPc.7045
+ __ZL23gAQCaptureOfflineRender
+ __ZL23gAQCaptureOutputEnqueue
+ __ZL24audit_stringMediaToolbox.7054
+ __ZL24getAutomationValueAtTimeP24OpaqueMusicEventIteratordRf
+ __ZL24getRBSProcessHandleClassv
+ __ZL25doGetHapticPatternWithKeyP8NSString
+ __ZL29audit_stringSpeechTranslation
+ __ZL30audit_stringAudioSessionServer.8308
+ __ZL30gAudioTapHALReferenceStreamLogv
+ __ZL32PV_GetAirPodsOffloadModeFromDictRKN10applesauce2CF13DictionaryRefE
+ __ZL33getCMBaseObjectGetVTableSymbolLocv.7056
+ __ZL33kBuiltInSSIDsToReplaceOnPhoneCall
+ __ZL40GetAtmosChannelLayoutTagFromDescriptionsRKN2CA13ChannelLayoutE
+ __ZL58getFigCPECryptorCreateCryptorFromSerializedRecipeSymbolLocv.7046
+ __ZL9PlaySoundjNSt3__110shared_ptrI19SSClientPlayOptionsEEPhjj
+ __ZN10AQMEDevice10DebugPrintEP7__sFILE
+ __ZN10AQMEDevice11SetBitDepthEbj
+ __ZN10AQMEDevice12RouteChangedEv
+ __ZN10AQMEDevice12maintainTapsEb
+ __ZN10AQMEDevice13GetIdentifierEv
+ __ZN10AQMEDevice13GetParametersER14AQIONodeClientiPKjPf
+ __ZN10AQMEDevice13SetChannelMapEPK8__CFData
+ __ZN10AQMEDevice13SetParametersER14AQIONodeClientPK15XAudioTimeStampiPK24AudioQueueParameterEvent
+ __ZN10AQMEDevice13silenceOutputERK11AQMESessionj
+ __ZN10AQMEDevice15ResetProcessorsER14AQIONodeClientbb
+ __ZN10AQMEDevice16AddRunningClientER14AQIONodeClientbb
+ __ZN10AQMEDevice16DetachConnectorsER17MEConnectorVectorRK17MEDetachSpecifier
+ __ZN10AQMEDevice17AddProcessingNodeER14AQIONodeClientR16AQProcessingNode
+ __ZN10AQMEDevice17GetRemovalPendingEv
+ __ZN10AQMEDevice17SetRemovalPendingEb
+ __ZN10AQMEDevice17schedulingVectorsEv
+ __ZN10AQMEDevice18GetOfflineRendererEv
+ __ZN10AQMEDevice18ResetOfflineRenderEv
+ __ZN10AQMEDevice18SetDeviceStartTimeERK15XAudioTimeStamp
+ __ZN10AQMEDevice18setDynamicsEnabledE15EDynamicsEnable
+ __ZN10AQMEDevice20RemoveProcessingNodeER14AQIONodeClientRK16AQProcessingNode
+ __ZN10AQMEDevice20hasRunningIORequestsEv
+ __ZN10AQMEDevice21GetDeviceStreamClientE14MEStreamTypeID
+ __ZN10AQMEDevice22PrepareForConfigChangeEv
+ __ZN10AQMEDevice22RemoveAndReAddIOClientER14AQIONodeClient
+ __ZN10AQMEDevice22updateTapsForSessionIDEj
+ __ZN10AQMEDevice23GetSessionOutputTrackerEv
+ __ZN10AQMEDevice24ClearScheduledParametersER14AQIONodeClient
+ __ZN10AQMEDevice25AccessibilityPrefsChangedEv
+ __ZN10AQMEDevice25ScreenSharingStateChangedEy
+ __ZN10AQMEDevice26IsProcessingFeatureEnabledER14AQIONodeClient13MEProcessorIDRj
+ __ZN10AQMEDevice26SetProcessOrSystemTappableEb
+ __ZN10AQMEDevice27SetProcessingFeatureEnabledER14AQIONodeClient13MEProcessorIDbP27AudioStreamBasicDescriptionPK20ProcessingFormatInfo
+ __ZN10AQMEDevice28mapClientSessionToThisDeviceERK14AQIONodeClient
+ __ZN10AQMEDevice29GetPersistedOnLastRouteChangeEv
+ __ZN10AQMEDevice29SetPersistedOnLastRouteChangeEb
+ __ZN10AQMEDevice32ProcessingNodeScheduleParametersER14AQIONodeClientRK16AQProcessingNodeRK15XAudioTimeStampjPK32ATAudioProcessingNodeParameterIDPKf
+ __ZN10AQMEDevice35maintainSystemTapAfterDeviceRemovalEv
+ __ZN10AQMEDevice37SetAudioObjectPropertyData_DeprecatedEjRK26AudioObjectPropertyAddressjPKvjS4_
+ __ZN10AQMEDevice38GetHadRunningRequestsOnLastRouteChangeEv
+ __ZN10AQMEDevice38SetHadRunningRequestsOnLastRouteChangeEb
+ __ZN10AQMEDevice39ProcessingNodeCancelScheduledParametersER14AQIONodeClientR16AQProcessingNodeb
+ __ZN10AQMEDevice39ProcessingNodeSchedulePendingParametersER14AQIONodeClientR16AQProcessingNode
+ __ZN10AQMEDevice9GetIOUnitEv
+ __ZN10AQMEDevice9MixEngineEv
+ __ZN10AQMEDevice9SetIOUnitENSt3__110shared_ptrI16AQMEIO_InterfaceEE
+ __ZN10AQMEIO_DSP14AdaptToVARouteEPK14__CFDictionaryb
+ __ZN10AQMEWaiterD0Ev
+ __ZN10AQMEWaiterD1Ev
+ __ZN10IMixEngine17AsAQMixEngine_VADEv
+ __ZN10IMixEngine18AsAQMixEngine_BaseEv
+ __ZN10applesauce2CF10BooleanRefD2Ev
+ __ZN10applesauce2CF11TypeRefPairC1IRA5_KcNS0_7DataRefEEEOT_OT0_
+ __ZN10applesauce2CF13DataRef_proxyC1ERKNS0_7DataRefE
+ __ZN10applesauce2CF13DictionaryRefC1EPK14__CFDictionary
+ __ZN10applesauce2CF13DictionaryRefD2Ev
+ __ZN10applesauce2CF15get_byte_lengthEPK8__CFData
+ __ZN10applesauce2CF6URLRefD2Ev
+ __ZN10applesauce2CF7DataRef11from_createEPK8__CFData
+ __ZN10applesauce2CF7DataRefD2Ev
+ __ZN10applesauce2CF7TypeRefD2Ev
+ __ZN10applesauce2CF7details11find_at_keyINS0_13DictionaryRefERKPK10__CFStringEET_PK14__CFDictionaryOT0_NS1_17applesauce_cf_tagE
+ __ZN10applesauce2CF7details16make_json_stringENSt3__117basic_string_viewIcNS2_11char_traitsIcEEEE
+ __ZN10applesauce2CF7details23find_at_key_or_optionalI35kAudioTranslation_SignalMaskingModeRKPK10__CFStringEENSt3__18optionalIT_EEPK14__CFDictionaryOT0_NS1_15counterpart_tagE
+ __ZN10applesauce2CF7details6RetainIPK14__CFDictionaryEET_S6_
+ __ZN10applesauce2CF7details7has_keyIPK10__CFStringEEbPK14__CFDictionaryOT_NS1_10raw_cf_tagE
+ __ZN10applesauce2CF8ArrayRefD2Ev
+ __ZN10applesauce2CF9NumberRefD2Ev
+ __ZN10applesauce2CF9ObjectRefIPK10__CFNumberED2Ev
+ __ZN10applesauce2CF9ObjectRefIPK10__CFStringED2Ev
+ __ZN10applesauce2CF9ObjectRefIPK11__CFBooleanED2Ev
+ __ZN10applesauce2CF9ObjectRefIPK14__CFDictionaryED2Ev
+ __ZN10applesauce2CF9ObjectRefIPK14__CFDictionaryEaSERKS5_
+ __ZN10applesauce2CF9ObjectRefIPK7__CFURLED2Ev
+ __ZN10applesauce2CF9ObjectRefIPK8__CFDataED2Ev
+ __ZN10applesauce2CF9ObjectRefIPK8__CFDataEaSEDn
+ __ZN10applesauce2CF9ObjectRefIPK9__CFArrayED2Ev
+ __ZN10applesauce2CF9ObjectRefIPKvED2Ev
+ __ZN10applesauce2CF9StringRef11from_createEPK10__CFString
+ __ZN10applesauce2CF9StringRef17from_get_noexceptEPK10__CFString
+ __ZN10applesauce2CF9StringRef20from_create_noexceptEPK10__CFString
+ __ZN10applesauce2CF9StringRefC1EPKcm
+ __ZN10applesauce2CF9StringRefC2ERKS1_
+ __ZN10applesauce2CF9StringRefD2Ev
+ __ZN10applesauce3xpc5array8iteratorC1ES1_m
+ __ZN10applesauce3xpc6objectC1ERKS1_
+ __ZN10applesauce3xpc6objectC1Eb
+ __ZN10applesauce3xpc6objectC1Ed
+ __ZN10applesauce3xpc6objectC1Ej
+ __ZN10applesauce3xpc8endpointC2ERKS1_
+ __ZN10applesauce4raii2v16detail10ScopeGuardIZ29SystemSoundServerPlayActionIDE3$_0NS2_15StackFailPolicyEED1Ev
+ __ZN10applesauce4raii2v16detail10ScopeGuardIZL23addFinalAutomationEventP16OpaqueMusicTrackdE3$_0NS2_15StackExitPolicyEED1Ev
+ __ZN10applesauce4raii2v16detail10ScopeGuardIZL26addInitialAutomationEventsP16OpaqueMusicTrackE3$_0NS2_15StackExitPolicyEED1Ev
+ __ZN10applesauce4raii2v16detail10ScopeGuardIZL26guaranteePreservationPointP16OpaqueMusicTrackE3$_0NS2_15StackExitPolicyEED1Ev
+ __ZN10applesauce4raii2v16detail10ScopeGuardIZN23FigCPECryptorMarshaller11DeserializeER14CADeserializerRPvRjEUlvE_NS2_15StackExitPolicyEED2Ev
+ __ZN10applesauce4raii2v16detail10ScopeGuardIZZN14DSP_Routing_VP28SetCallTranslationPropertiesEPK14__CFDictionaryRbEUb_E4$_13NS2_15StackExitPolicyEED1Ev
+ __ZN10applesauce8dispatch2v15queueD2Ev
+ __ZN11AQMESession16setSubsessionRefEPKv
+ __ZN11AQMESessionC2ERKS_
+ __ZN11AQMESessionD2Ev
+ __ZN11ClientEntry17doPrepareSequenceENSt3__110shared_ptrI14HapticSequenceEEN5caulk16inplace_functionIFvmELm32ELm8ENS4_23inplace_function_detail6vtableEEE
+ __ZN11ClientEntry19handleSequenceEndedEmN5caulk16inplace_functionIFvmELm32ELm8ENS0_23inplace_function_detail6vtableEEE
+ __ZN11ClientEntry31ensureCustomAudioEventOutputBusEj
+ __ZN11DSP_Routing28SetCallTranslationPropertiesEPK14__CFDictionaryRb
+ __ZN11HapticSynth9stopEventEjjj
+ __ZN11MEConnector11SetSTSLabelERKN10applesauce2CF9StringRefEb
+ __ZN11PListLogger12logDictEntryEPKvS1_Pv
+ __ZN11PListLogger12logItemEntryEPKvPKcPv
+ __ZN11SSClientIPC13PlayWithFlagsEjNSt3__110shared_ptrI19SSClientPlayOptionsEEPhjbj
+ __ZN12CADeprecated11XMachServer6ClientD2Ev
+ __ZN12CADeprecated12CABufferList7SetFromEPK15AudioBufferListj
+ __ZN12CADeprecated13TAtomicStack2IN16XAtomicAllocator8FreeNodeEE10pop_atomicEv
+ __ZN12CADeprecated13TAtomicStack2IN16XAtomicAllocator8FreeNodeEE11push_atomicEPS2_
+ __ZN12CASerializer9WriteDataEPK8__CFData
+ __ZN12CAXException11FormatErrorEPcmi
+ __ZN12MemAllocator8AllocMemEm
+ __ZN12SequenceImpl17registerWithSynthEP11HapticSynth
+ __ZN13MESubmixGraph12maintainTapsEb
+ __ZN13MESubmixGraph18createMixerChannelER14AQIONodeClient
+ __ZN13MESubmixGraph19attachMixerChannelsER17MEConnectorVector
+ __ZN13MESubmixGraph19detach1MixerChannelEP14MEMixerChannel
+ __ZN13MESubmixGraph19setMixerInputVolumeEjf
+ __ZN13MESubmixGraph22startStopSubmixCaptureEb
+ __ZN13MESubmixGraph22updateTapsForSessionIDEj
+ __ZN13MESubmixGraph25setEnhanceDialogueEnabledE22EEnhanceDialogueEnable
+ __ZN13MESubmixGraph26SetProcessOrSystemTappableEb
+ __ZN13MESubmixGraph26updateEnhanceDialogueLevelEv
+ __ZN13MESubmixGraph26updateEnhanceDialogueRouteEv
+ __ZN13MESubmixGraph31checkEnhanceDialogueModeChangedEbP14MEMixerChannel
+ __ZN13MESubmixGraph32enhanceDialogueProcessorIsActiveEv
+ __ZN13MESubmixGraph34attachAndConnectChannelToTapSubmixER9TapSubmixR14MEMixerChannel
+ __ZN13MESubmixGraph35maintainSystemTapAfterDeviceRemovalEv
+ __ZN13MESubmixGraph39disconnectAndDetachChannelFromTapSubmixER9TapSubmixR14MEMixerChannel
+ __ZN13MESubmixGraph6renderEiR15AudioBufferListRK14AudioTimeStamp
+ __ZN13MESubmixGraphC2ERK17AudioTapSpecifieriR11IAQMEDeviceR19IDeviceStreamClientb
+ __ZN13MESubmixGraphD0Ev
+ __ZN13MESubmixGraphD1Ev
+ __ZN13ServerManager15prepareSequenceENSt3__110shared_ptrI11ClientEntryEEmN5caulk16inplace_functionIFvmELm32ELm8ENS4_23inplace_function_detail6vtableEEE
+ __ZN13ServerManager25requestPowerCheckForMediaEb
+ __ZN13ServerManager35cancelOngoingParameterCurveOfSameIDENSt3__110shared_ptrI11ClientEntryEERK13HapticCommand
+ __ZN13TrackIterator12SetEventInfoEjPKv
+ __ZN13TrackIterator9CheckLoopEd
+ __ZN13XOSTransactorD2Ev
+ __ZN14AQIONodeClient17InitIONodeSessionERK11AQMESession
+ __ZN14AQIONodeClient20GetCinematicMetadataEv
+ __ZN14AQIONodeClient27EnhanceableMuteStateChangedEv
+ __ZN14AQInputChunkerC2EPDoFvPvP12AQInputChunkES0_
+ __ZN14DSP_Routing_VP28SetCallTranslationPropertiesEPK14__CFDictionaryRb
+ __ZN14DSP_Routing_VP8UpstreamD2Ev
+ __ZN14MEInputManager10GetClientsEv
+ __ZN14MEInputManager12StreamClientEv
+ __ZN14MEInputManager13DispatchInputERK14AudioTimeStampjRK15AudioBufferList
+ __ZN14MEInputManager13volumeChangedEv
+ __ZN14MEInputManager14AddInputClientER14AQIONodeClient
+ __ZN14MEInputManager14latencyChangedEv
+ __ZN14MEInputManager17RemoveInputClientER14AQIONodeClient
+ __ZN14MEInputManager22AttachInputDispatchersERK17MEConnectorVector
+ __ZN14MEInputManager22DetachInputDispatchersER17MEConnectorVectorRK17MEDetachSpecifier
+ __ZN14MEInputManager6DeviceEv
+ __ZN14MEMixerChannel11SetSTSLabelERKN10applesauce2CF9StringRefEb
+ __ZN14MEMixerChannel14TimePitchStateD2Ev
+ __ZN14MEMixerChannel15_CombineVolumesExRbb
+ __ZN14MEMixerChannel16ForEachTapSubmixEN5caulk12function_refIFvR9TapSubmixiEEE
+ __ZN14MEMixerChannel17AddProcessingNodeER16AQProcessingNode
+ __ZN14MEMixerChannel17schedulingVectorsEv
+ __ZN14MEMixerChannel19ForEachTapSubmix_RTEN5caulk15rt_function_refIFvR9TapSubmixibEEE
+ __ZN14MEMixerChannel24ConfigureSpatializerHostEv
+ __ZN14MEMixerChannel28StartStopMixerChannelCaptureEb
+ __ZN14MixTapToUplink10DestroyTapEv
+ __ZN14MixTapToUplink11FetchAndMixERK15AudioBufferListRS0_jiRK15XAudioTimeStamp
+ __ZN14MixTapToUplink11FetchAndMixERK15AudioBufferListiRK15XAudioTimeStamp
+ __ZN14MixTapToUplink16AQMETapConnector20getBundleIDOrDefaultEjPKc
+ __ZN14MixTapToUplink16AQMETapConnector30ShouldTappedAudioBypassMicMuteEv
+ __ZN14MixTapToUplink16AQMETapConnector5StartEP19TappedAudioConsumer
+ __ZN14MixTapToUplink16AQMETapConnector6CreateERKN2CA17StreamDescriptionERKNS1_13ChannelLayoutEiRKNSt3__113unordered_setIjNS8_4hashIjEENS8_8equal_toIjEENS8_9allocatorIjEEEE
+ __ZN14MixTapToUplink19TappedAudioProducer21SetReferenceTimeStampERK15XAudioTimeStamp
+ __ZN14MixTapToUplink34RefreshMutedSpeechActivityListenerER26MutedSpeechActivityManager
+ __ZN14MixTapToUplink49GetAudioSessionsWithMixToUplinkPreferenceInternalEv
+ __ZN14MixTapToUplink5StoreERK15AudioBufferListiRK15XAudioTimeStamp
+ __ZN14MixTapToUplinkC1ERKN2CA17StreamDescriptionERKNS0_13ChannelLayoutE
+ __ZN14MixTapToUplinkD0Ev
+ __ZN14MixTapToUplinkD2Ev
+ __ZN14RemoteIOClient18OutputIONodeClient27EnhanceableMuteStateChangedEv
+ __ZN14RemoteIOClient27SetTranslationConfigurationEPK14__CFDictionary
+ __ZN14RemoteIOServer10ServerLockEv
+ __ZN14RemoteIOServer13SetInputMutedERK11AQMESessionb
+ __ZN14RemoteIOServer13SetInputMutedERK11AQMESessionbf
+ __ZN14RemoteIOServer14ClientStartingER14RemoteIOClient
+ __ZN14RemoteIOServer14ClientStoppingER14RemoteIOClient
+ __ZN14RemoteIOServer16MuteAudioSessionERK11AQMESessionb
+ __ZN14RemoteIOServer16RefreshInputMuteEv
+ __ZN14RemoteIOServer16SuspendCallbacksERK11AQMESessionb
+ __ZN14RemoteIOServer20ActivateAudioSessionERK11AQMESessionbb
+ __ZN14RemoteIOServer34RefreshRecordPermissionsForClientsE13audit_token_t
+ __ZN14RemoteIOServer6globalEv
+ __ZN14SSSClientEntry19handleSequenceEndedEmN5caulk16inplace_functionIFvmELm32ELm8ENS0_23inplace_function_detail6vtableEEE
+ __ZN14SequenceChaserD2Ev
+ __ZN15AQMixEngine_VAD10MEVADevice13GetIdentifierEv
+ __ZN15AQMixEngine_VAD10MEVADevice17GetRemovalPendingEv
+ __ZN15AQMixEngine_VAD10MEVADevice17SetRemovalPendingEb
+ __ZN15AQMixEngine_VAD10MEVADevice29GetPersistedOnLastRouteChangeEv
+ __ZN15AQMixEngine_VAD10MEVADevice29SetPersistedOnLastRouteChangeEb
+ __ZN15AQMixEngine_VAD10MEVADevice38GetHadRunningRequestsOnLastRouteChangeEv
+ __ZN15AQMixEngine_VAD10MEVADevice38SetHadRunningRequestsOnLastRouteChangeEb
+ __ZN15AQMixEngine_VAD13ForAllDevicesERKNSt3__18functionIFvR11IAQMEDeviceEEE
+ __ZN15AQMixEngine_VAD28SetCallTranslationPropertiesEPK14__CFDictionaryRb
+ __ZN15AQProcessingTapC2ER16AudioQueueObjectji13MEProcessorIDjbRK24CAStreamBasicDescription
+ __ZN15ActiveSoundList23RegisterSoundCompletionEj27ActiveSoundCompletedPortionb
+ __ZN15DummyNodeClientD2Ev
+ __ZN15InputDispatcher17AddProcessingNodeER16AQProcessingNode
+ __ZN15LoudnessManager11GetSettingsEPK10__CFStringjP18AQConverterOrCodecPK14__CFDictionaryRK11AQMESessionRK14AQMEIO_BindingbbPNS_8SettingsE
+ __ZN15LoudnessManager8InstanceEv
+ __ZN15MEVADIdentifierD2Ev
+ __ZN16AQMixEngine_Base14DebugPrintFromEP7__sFILEPKc
+ __ZN16AQMixEngine_Base17AddProcessingNodeER14AQIONodeClientR16AQProcessingNode
+ __ZN16AQMixEngine_Base22updateTapsForSessionIDEj
+ __ZN16AQMixEngine_Base27getPlaySilenceUntilHostTimeEv
+ __ZN16AudioQueueObject17PlaySliceCompleteEPvPN20ScheduledSlicePlayer24XScheduledAudioSliceBaseE
+ __ZN16AudioQueueObject18ConfigureTapDeviceER17AudioTapInterface
+ __ZN16AudioQueueObject20GetCinematicMetadataEv
+ __ZN16AudioQueueObject23SetDecoderChannelLayoutEj
+ __ZN16AudioQueueObject26SetCodecLoudnessParametersEPNS_19ConverterConnectionEPK14__CFDictionary
+ __ZN16AudioQueueObject27EnhanceableMuteStateChangedEv
+ __ZN16AudioQueueObject32DispatchProcessingNodeParametersEv
+ __ZN16AudioQueueObject4StopEbbPNS_10StopStatusE
+ __ZN16AudioQueueObject55GetUpdatedAudioChannelLayoutTagFromDescriptionsOrBitmapERKN2CA13ChannelLayoutE
+ __ZN16MCProcessingNode5ResetEjj
+ __ZN16RTCountedDataRef13releaseObjectEv
+ __ZN16RTCountedDataRefD0Ev
+ __ZN16RTCountedDataRefD1Ev
+ __ZN16SSSHapticsPlayer19cancelHapticPatternEb
+ __ZN16SSSHapticsPlayer28patternIsActuallyGoingToVibeEPK14__CFDictionary
+ __ZN16TArrayMarshallerIyE11DeserializeER14CADeserializerRPvRj
+ __ZN16TArrayMarshallerIyED0Ev
+ __ZN16TArrayMarshallerIyED1Ev
+ __ZN17AQMECaptureInsert12StartCaptureERK15AQIONodeManagerPKc
+ __ZN17AQMECaptureInsert6RenderEPjPK14AudioTimeStampjjP15AudioBufferList
+ __ZN17AQMECaptureInsertD0Ev
+ __ZN17AQMECaptureInsertD1Ev
+ __ZN17AspenActionPlayer12SetClientPidEi
+ __ZN17AspenActionPlayer17SetSpatialDetailsEN10applesauce2CF7TypeRefE
+ __ZN17AspenActionPlayer37SetPrefersToPlayAudioToHeadphonesOnlyEb
+ __ZN17AudioEventManager23updateAudioEventsOutputERNSt3__16vectorIjNS0_9allocatorIjEEEEj
+ __ZN17AudioTapInterface4Impl15createTapDeviceEv
+ __ZN17AudioTapInterface4Impl23setupScreenSharingStateEv
+ __ZN17AudioTapInterface4Impl26teardownScreenSharingStateEv
+ __ZN17AudioTapInterface4Impl6updateERK17AudioTapSpecifier
+ __ZN17AudioTapInterface6hasTapEv
+ __ZN17AudioTapInterfaceC2ERK17AudioTapSpecifierb
+ __ZN17AudioTapInterfaceD2Ev
+ __ZN17AudioTapSpecifierC1EP21ATAudioTapDescription
+ __ZN17AudioTapSpecifieraSERKS_
+ __ZN17AudioTapUtilities17UseHALTapCodePathEv
+ __ZN17CACFMutableStringD2Ev
+ __ZN17IONodeSessionStub15setOwnerSessionERK11AQMESession
+ __ZN17IONodeSessionStub33getIntendedSpatialAudioExperienceERN10applesauce2CF7TypeRefE
+ __ZN17IONodeSessionStub33setIntendedSpatialAudioExperienceEN10applesauce2CF7TypeRefE
+ __ZN17IONodeSessionStubD0Ev
+ __ZN17IONodeSessionStubD1Ev
+ __ZN17PlatformUtilities15IsInternalBuildEv
+ __ZN17ResolvedOpaqueRefI15AudioQueueOwnerEC2EN16BaseOpaqueObject3RefE
+ __ZN17SharedAudioBufferD2Ev
+ __ZN17TCFDictionaryBaseD0Ev
+ __ZN17TCFDictionaryBaseD1Ev
+ __ZN17TCFDictionaryBaseD2Ev
+ __ZN18AQMixEngine_Single13ForAllDevicesERKNSt3__18functionIFvR11IAQMEDeviceEEE
+ __ZN18MCSpatialAudioUnit19setSpatialParameterE35SpatialExperienceRenderingParameterPKvj
+ __ZN18MCSpatialAudioUnitD0Ev
+ __ZN18MCSpatialAudioUnitD1Ev
+ __ZN18MixTapToUplinkHost30RefreshMixTapToUplinkInstancesERKNSt3__113unordered_mapIjiNS0_4hashIjEENS0_8equal_toIjEENS0_9allocatorINS0_4pairIKjiEEEEEE
+ __ZN18MixTapToUplinkHost46MixTapToUplinkGroupedByMicrophoneInjectionMode33SupportedMicrophoneInjectionModesE
+ __ZN18MixTapToUplinkHost46MixTapToUplinkGroupedByMicrophoneInjectionMode42GetIndexOfSupportedMicrophoneInjectionModeEi
+ __ZN18MixTapToUplinkHost49StartAdvertisingMixTapToTelephonyUplinkCapabilityEv
+ __ZN18MixTapToUplinkHost77RefreshProxyMutedSpeechActivityListenerFromMutedSpeechActivityManagerProviderEv
+ __ZN18MuteFadeController16MaybeApplyMutingEiRK15AudioBufferListRS0_RKN2CA17StreamDescriptionE
+ __ZN18RemoteIOServerBase10ClientDiedEPN12CADeprecated11XMachServer6ClientE
+ __ZN18RemoteIOServerBase10ServerLockEv
+ __ZN18RemoteIOServerBase13SetInputMutedERK11AQMESessionb
+ __ZN18RemoteIOServerBase13SetInputMutedERK11AQMESessionbf
+ __ZN18RemoteIOServerBase14ClientStartingER14RemoteIOClient
+ __ZN18RemoteIOServerBase14ClientStoppingER14RemoteIOClient
+ __ZN18RemoteIOServerBase15ClientFromTokenE13audit_token_tj
+ __ZN18RemoteIOServerBase16MuteAudioSessionERK11AQMESessionb
+ __ZN18RemoteIOServerBase16RefreshInputMuteEv
+ __ZN18RemoteIOServerBase16SuspendCallbacksERK11AQMESessionb
+ __ZN18RemoteIOServerBase19MuteAudioSubsessionEyb
+ __ZN18RemoteIOServerBase20ActivateAudioSessionERK11AQMESessionbb
+ __ZN18RemoteIOServerBase24AudioSessionStateChangedERK11AQMESessionjPK14__CFDictionary
+ __ZN18RemoteIOServerBase25FadeClientsInAudioSessionERK11AQMESessionff
+ __ZN18RemoteIOServerBase34RefreshRecordPermissionsForClientsE13audit_token_t
+ __ZN18SSSCallbackMessage7performEv
+ __ZN18SlicePlayerFactory8instanceEv
+ __ZN18TCFDictionary_CF2CIPK10__CFStringPN18AQConverterManager17AQConverterThreadEED0Ev
+ __ZN18TCFDictionary_CF2CIPK10__CFStringPN18AQConverterManager17AQConverterThreadEED1Ev
+ __ZN19IDeviceStreamClient11InitOfflineEv
+ __ZN19IDeviceStreamClient11muteChangedEv
+ __ZN19IDeviceStreamClient12ApplyDuckingEf
+ __ZN19IDeviceStreamClient12RouteChangedEv
+ __ZN19IDeviceStreamClient12inLockScreenEv
+ __ZN19IDeviceStreamClient12maintainTapsEb
+ __ZN19IDeviceStreamClient13volumeChangedEv
+ __ZN19IDeviceStreamClient14isUsingRawModeEv
+ __ZN19IDeviceStreamClient14latencyChangedEv
+ __ZN19IDeviceStreamClient16AddActiveChannelEb
+ __ZN19IDeviceStreamClient17SoundCheckChangedEv
+ __ZN19IDeviceStreamClient17setDynamicsEnableE15EDynamicsEnable
+ __ZN19IDeviceStreamClient17submixTapDisposalEv
+ __ZN19IDeviceStreamClient18ResetOfflineRenderEv
+ __ZN19IDeviceStreamClient22updateTapsForSessionIDEj
+ __ZN19IDeviceStreamClient23AccessProcessorPropertyE13MEProcessorIDjbRjPv
+ __ZN19IDeviceStreamClient24ResetActiveChannelCountsEv
+ __ZN19IDeviceStreamClient24canEnableEnhanceDialogueEb
+ __ZN19IDeviceStreamClient24spatialCustomHRTFChangedEv
+ __ZN19IDeviceStreamClient25AccessibilityPrefsChangedEv
+ __ZN19IDeviceStreamClient25ScreenSharingStateChangedEy
+ __ZN19IDeviceStreamClient25getEnhanceableSessionTypeEb
+ __ZN19IDeviceStreamClient25spatialPreferencesChangedEv
+ __ZN19IDeviceStreamClient26SetProcessOrSystemTappableEb
+ __ZN19IDeviceStreamClient35maintainSystemTapAfterDeviceRemovalEv
+ __ZN19IDeviceStreamClient44ConfigureMovieClientSpatialMixerSurroundGainEf
+ __ZN19IONodeSessionLegacy15setOwnerSessionERK11AQMESession
+ __ZN19IONodeSessionLegacy33getIntendedSpatialAudioExperienceERN10applesauce2CF7TypeRefE
+ __ZN19IONodeSessionLegacy33setIntendedSpatialAudioExperienceEN10applesauce2CF7TypeRefE
+ __ZN19IONodeSessionLegacyD0Ev
+ __ZN19IONodeSessionLegacyD1Ev
+ __ZN19MEInputStreamClient13volumeChangedEv
+ __ZN19MEInputStreamClient14latencyChangedEv
+ __ZN19MESchedulingVectorsD2Ev
+ __ZN19SSClientPlayOptionsD1Ev
+ __ZN19SequenceDestination14ReseekIfNeededEd
+ __ZN19SequenceDestination15InvalidateRampsEb
+ __ZN19SequenceDestination23InvalidateRampsForTrackEP13SequenceTrack
+ __ZN19SequenceDestination4SeekEd
+ __ZN20AudioPriorityManager35getActiveHighestPriorityClientCountEv
+ __ZN20CA_UISoundClientBaseC2EdjPK14__CFDictionaryjN10applesauce2CF7TypeRefEib
+ __ZN20HapticEventConverter11loadPatternEP7NSArrayRbS2_
+ __ZN20HapticEventConverter36publishControlPointToAutomationTrackE27AVHapticPlayerParameterTypeP40AVHapticPlayerParameterCurveControlPointRNS_23CurveConsolidationStateE
+ __ZN20MEDeviceStreamClient11AddIOClientER14AQIONodeClientP11MEConnector
+ __ZN20MEDeviceStreamClient14RemoveIOClientER14AQIONodeClient
+ __ZN20MEDeviceStreamClient16AddRunningClientER14AQIONodeClientbb
+ __ZN20MEDeviceStreamClient21addOrRemoveAuditTokenER14AQIONodeClientb
+ __ZN20MEDeviceStreamClient22prepareForConfigChangeEv
+ __ZN20MEDeviceStreamClientC2ER11IAQMEDevice14MEStreamTypeID
+ __ZN20MEOutputStreamClient11InitOfflineEv
+ __ZN20MEOutputStreamClient11muteChangedEv
+ __ZN20MEOutputStreamClient12ApplyDuckingEf
+ __ZN20MEOutputStreamClient12RouteChangedEv
+ __ZN20MEOutputStreamClient12inLockScreenEv
+ __ZN20MEOutputStreamClient12maintainTapsEb
+ __ZN20MEOutputStreamClient13volumeChangedEv
+ __ZN20MEOutputStreamClient14isUsingRawModeEv
+ __ZN20MEOutputStreamClient14latencyChangedEv
+ __ZN20MEOutputStreamClient16AddActiveChannelEb
+ __ZN20MEOutputStreamClient17SoundCheckChangedEv
+ __ZN20MEOutputStreamClient17setDynamicsEnableE15EDynamicsEnable
+ __ZN20MEOutputStreamClient17submixTapDisposalEv
+ __ZN20MEOutputStreamClient18ResetOfflineRenderEv
+ __ZN20MEOutputStreamClient22updateTapsForSessionIDEj
+ __ZN20MEOutputStreamClient24ResetActiveChannelCountsEv
+ __ZN20MEOutputStreamClient24spatialCustomHRTFChangedEv
+ __ZN20MEOutputStreamClient25AccessibilityPrefsChangedEv
+ __ZN20MEOutputStreamClient25ScreenSharingStateChangedEy
+ __ZN20MEOutputStreamClient25getEnhanceableSessionTypeEb
+ __ZN20MEOutputStreamClient26SetProcessOrSystemTappableEb
+ __ZN20MEOutputStreamClient35maintainSystemTapAfterDeviceRemovalEv
+ __ZN20MEOutputStreamClient44ConfigureMovieClientSpatialMixerSurroundGainEf
+ __ZN21AVVoiceTriggerManager10InitializeEv
+ __ZN21AVVoiceTriggerManager10initializeEv
+ __ZN21AVVoiceTriggerManager14HeySiriEnabledEv
+ __ZN21AVVoiceTriggerManager18hasVoiceTriggerXPCEv
+ __ZN21AVVoiceTriggerManager23useSpeechDetectionRouteEv
+ __ZN21AVVoiceTriggerManager25SpeechDetectionVADCreatedEv
+ __ZN21AVVoiceTriggerManager28SiriClientRecordStateChangedEb
+ __ZN21AVVoiceTriggerManager28hardwareSupportsVoiceTriggerEv
+ __ZN21AVVoiceTriggerManager8instanceEv
+ __ZN21AVVoiceTriggerManagerC1Ev
+ __ZN21AVVoiceTriggerManagerC2Ev
+ __ZN21HapticPriorityManager35getActiveHighestPriorityClientCountEv
+ __ZN21IPCAUSharedMemoryBaseD2Ev
+ __ZN21ResourcePathUtilitiesL14CFDictFromPathERKN10applesauce2CF9StringRefE.3583
+ __ZN21ResourcePathUtilitiesL19ResolveResourcePathERKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEES8_.3582
+ __ZN21ScheduledSlicePlayer212SetStartTimeERK15XAudioTimeStampxj
+ __ZN21ScheduledSlicePlayer213ClearScheduleEv
+ __ZN21ScheduledSlicePlayer213PrepareToPlayEv
+ __ZN21ScheduledSlicePlayer213ReleaseBufferEPNS_20XScheduledAudioSliceEj
+ __ZN21ScheduledSlicePlayer213ScheduleSliceEPN20ScheduledSlicePlayer24XScheduledAudioSliceBaseE
+ __ZN21ScheduledSlicePlayer214BufferCompleteERN5caulk10sync_guardINS_13RenderGuardedENS0_22pooled_semaphore_mutexEEEPNS_20XScheduledAudioSliceEx
+ __ZN21ScheduledSlicePlayer215MarkEndOfStreamEv
+ __ZN21ScheduledSlicePlayer216ScheduleMetadataEPK18AudioMetadataEventxj
+ __ZN21ScheduledSlicePlayer218ChangeOutputFormatERK27AudioStreamBasicDescription
+ __ZN21ScheduledSlicePlayer218DeltaEndOfTimelineEv
+ __ZN21ScheduledSlicePlayer218DoResolveStartTimeERN5caulk10sync_guardINS_13RenderGuardedENS0_22pooled_semaphore_mutexEEERK15XAudioTimeStamp
+ __ZN21ScheduledSlicePlayer220CurrentEndOfTimelineEv
+ __ZN21ScheduledSlicePlayer220XScheduledAudioSlice9ResetNextEv
+ __ZN21ScheduledSlicePlayer220XScheduledAudioSliceD0Ev
+ __ZN21ScheduledSlicePlayer220XScheduledAudioSliceD1Ev
+ __ZN21ScheduledSlicePlayer221CheckResolveStartTimeERK15XAudioTimeStampi
+ __ZN21ScheduledSlicePlayer26RenderERK15XAudioTimeStampiR15AudioBufferListb
+ __ZN21ScheduledSlicePlayer29CopySliceERN5caulk10sync_guardINS_13RenderGuardedENS0_22pooled_semaphore_mutexEEExPNS_20XScheduledAudioSliceEiR15AudioBufferListiib
+ __ZN21ScheduledSlicePlayer2D0Ev
+ __ZN21ScheduledSlicePlayer2D1Ev
+ __ZN21ScheduledSlicePlayer2D2Ev
+ __ZN22SpatializationLoggerV1D2Ev
+ __ZN22SpatializationLoggerV2D2Ev
+ __ZN24AVVoiceTriggerServerImpl10InitializeEv
+ __ZN24AVVoiceTriggerServerImpl15isAOPConfiguredEv
+ __ZN24AVVoiceTriggerServerImpl17enableBargeInModeEbU13block_pointerFvP7NSErrorE
+ __ZN24AVVoiceTriggerServerImpl21enableListeningOnPortEmb
+ __ZN24AVVoiceTriggerServerImpl21fetchAssistantEnabledEb
+ __ZN24AVVoiceTriggerServerImpl22getCachedPortStateInfoEv
+ __ZN24AVVoiceTriggerServerImpl22safeUpdatePrefWithLockEU13block_pointerFvvERbS2_S2_S2_
+ __ZN24AVVoiceTriggerServerImpl26GetSpeechDetectionDeviceIDE39AVVoiceTriggerServerSpeechDeviceUIDTypePi
+ __ZN24AVVoiceTriggerServerImpl27assistantPrefsChangedNoLockEbb
+ __ZN24AVVoiceTriggerServerImpl27enableVoiceTriggerListeningEbbU13block_pointerFvP7NSErrorE
+ __ZN24AVVoiceTriggerServerImpl30notifyAOPListeningStateChangedEj
+ __ZN24AVVoiceTriggerServerImpl32getDictionaryForPropertySelectorEj39AVVoiceTriggerServerSpeechDeviceUIDTypePi
+ __ZN24AVVoiceTriggerServerImpl33fetchAssistantVoiceTriggerEnabledEv
+ __ZN24AVVoiceTriggerServerImpl38createAndActivateSecureSessionIfNeededEv
+ __ZN24AVVoiceTriggerServerImpl40registerStateChangedNotificationHandlersEb
+ __ZN24AVVoiceTriggerServerImpl41deactivateAndDestroySecureSessionIfExistsEv
+ __ZN24AVVoiceTriggerServerImpl42registerAOPVoiceTriggerNotificationHandlerEjb
+ __ZN24AVVoiceTriggerServerImpl43registerAOPEnableChangedNotificationHandlerEb
+ __ZN24AVVoiceTriggerServerImplD0Ev
+ __ZN24AVVoiceTriggerServerImplD1Ev
+ __ZN24AVVoiceTriggerServerImplD2Ev
+ __ZN24EnhanceDialogueProcessorC1Ev
+ __ZN24MEEnhanceableSubmixGraph10initializeEv
+ __ZN24MEEnhanceableSubmixGraph12rebuildChainEv
+ __ZN24MEEnhanceableSubmixGraph12uninitializeEv
+ __ZN24MEEnhanceableSubmixGraph16_changeMixFormatERKN2CA17StreamDescriptionERKNS0_13ChannelLayoutE
+ __ZN24MEEnhanceableSubmixGraph21setMixerChannelLayoutEjiRKN2CA13ChannelLayoutE
+ __ZN24MEEnhanceableSubmixGraph31checkEnhanceDialogueModeChangedEbP14MEMixerChannel
+ __ZN24MEEnhanceableSubmixGraphD0Ev
+ __ZN24MEEnhanceableSubmixGraphD1Ev
+ __ZN25AUNodeSequenceDestination14ReseekIfNeededEd
+ __ZN25AUNodeSequenceDestination15InvalidateRampsEb
+ __ZN25AUNodeSequenceDestination23InvalidateRampsForTrackEP13SequenceTrack
+ __ZN25AUNodeSequenceDestination4SeekEd
+ __ZN25MEParallelPathSubmixGraph15_addSourceGraphER13MESubmixGraphR24MEEnhanceableSubmixGraphb
+ __ZN25MEParallelPathSubmixGraph22ParallelPathRenderProcEPvPjPK14AudioTimeStampjjP15AudioBufferList
+ __ZN25MEParallelPathSubmixGraph26chooseSubmixGraphForClientER14AQIONodeClient
+ __ZN25MEParallelPathSubmixGraph34_connectEnhanceDialogueSubmixGraphER13MESubmixGraphR24MEEnhanceableSubmixGraphb
+ __ZN25MEParallelPathSubmixGraphD1Ev
+ __ZN26AudioTapHALReferenceStreamD1Ev
+ __ZN26MutedSpeechActivityManager4Impl35GetProxyMutedSpeechActivityListenerEm
+ __ZN26MutedSpeechActivityManager4Impl44ReleaseProxyMutedSpeechActivityEventListenerEm
+ __ZN27ScheduledSlicePlayer_Legacy12SetStartTimeERK15XAudioTimeStampxj
+ __ZN27ScheduledSlicePlayer_Legacy13ClearScheduleEv
+ __ZN27ScheduledSlicePlayer_Legacy13PrepareToPlayEv
+ __ZN27ScheduledSlicePlayer_Legacy13ReleaseBufferEPNS_20XScheduledAudioSliceEi
+ __ZN27ScheduledSlicePlayer_Legacy13ScheduleSliceEPN20ScheduledSlicePlayer24XScheduledAudioSliceBaseE
+ __ZN27ScheduledSlicePlayer_Legacy14BufferCompleteEPNS_20XScheduledAudioSliceEx
+ __ZN27ScheduledSlicePlayer_Legacy15MarkEndOfStreamEv
+ __ZN27ScheduledSlicePlayer_Legacy16ScheduleMetadataEPK18AudioMetadataEventxj
+ __ZN27ScheduledSlicePlayer_Legacy18ChangeOutputFormatERK27AudioStreamBasicDescription
+ __ZN27ScheduledSlicePlayer_Legacy18DeltaEndOfTimelineEv
+ __ZN27ScheduledSlicePlayer_Legacy18DoResolveStartTimeERK15XAudioTimeStampi
+ __ZN27ScheduledSlicePlayer_Legacy20CurrentEndOfTimelineEv
+ __ZN27ScheduledSlicePlayer_Legacy20XScheduledAudioSlice9ResetNextEv
+ __ZN27ScheduledSlicePlayer_Legacy20XScheduledAudioSliceD0Ev
+ __ZN27ScheduledSlicePlayer_Legacy20XScheduledAudioSliceD1Ev
+ __ZN27ScheduledSlicePlayer_Legacy21CheckResolveStartTimeERK15XAudioTimeStampi
+ __ZN27ScheduledSlicePlayer_Legacy6RenderERK15XAudioTimeStampiR15AudioBufferListb
+ __ZN27ScheduledSlicePlayer_Legacy9CopySliceExPNS_20XScheduledAudioSliceEiR15AudioBufferListiib
+ __ZN27ScheduledSlicePlayer_LegacyD0Ev
+ __ZN27ScheduledSlicePlayer_LegacyD1Ev
+ __ZN27ScheduledSlicePlayer_LegacyD2Ev
+ __ZN2AQ3API17ProcessingTapBaseD2Ev
+ __ZN2AQ3API6V2Impl20AQOfflineMixerRenderEP20OpaqueAQOfflineMixerjPjP15AudioBufferListP28AudioStreamPacketDescriptionP38AudioStreamPacketDependencyDescriptionPh
+ __ZN2AQ6Server12RemoteClient18ProcessingTapStateD2Ev
+ __ZN2AT11Translation13AudioInjector18AudioFormatChangedENS0_14CallTranslator5ScopeERKN2CA17StreamDescriptionERKNS4_13ChannelLayoutE
+ __ZN2AT11Translation13AudioInjectorD0Ev
+ __ZN2AT11Translation13AudioInjectorD1Ev
+ __ZN2AT11Translation14CallTranslator12ProcessAudioENS1_5ScopeER15AudioBufferListiRK15XAudioTimeStamp
+ __ZN2AT11Translation14CallTranslator12SetInputMuteEb
+ __ZN2AT11Translation14CallTranslator13StopAnalyticsEv
+ __ZN2AT11Translation14CallTranslator13sCacheCounterE
+ __ZN2AT11Translation14CallTranslator14StartAnalyticsEv
+ __ZN2AT11Translation14CallTranslator16SetStoredInCacheEb
+ __ZN2AT11Translation14CallTranslator17ReleaseAfterDelayENSt3__110shared_ptrIS1_EE
+ __ZN2AT11Translation14CallTranslator18AudioFormatChangedENS1_5ScopeERKN2CA17StreamDescriptionERKNS3_13ChannelLayoutE
+ __ZN2AT11Translation14CallTranslator21sCachedCallTranslatorE
+ __ZN2AT11Translation14CallTranslator23InferActiveAudioChannelEPv
+ __ZN2AT11Translation14CallTranslator28HandleInjectionEndedCallbackENS1_5ScopeENS0_17AudioInjectorModeE
+ __ZN2AT11Translation14CallTranslator30CreateAudioTranslationInjectorERNS0_24TranslationConfigurationERNS0_35AudioStreamTranslationConfigurationENS1_5ScopeERKN2CA17StreamDescriptionERKNS7_13ChannelLayoutEj
+ __ZN2AT11Translation14CallTranslatorD2Ev
+ __ZN2AT11Translation15gTranslationLogE
+ __ZN2AT11Translation16TranslatorClient14sEnableCaptureE
+ __ZN2AT11Translation16TranslatorClient8setStateENS0_16TranslationStateE
+ __ZN2AT11Translation18CallTranslatorBaseC2ERKNS1_12DependenciesE
+ __ZN2AT11Translation18CallTranslatorBaseD0Ev
+ __ZN2AT11Translation18CallTranslatorBaseD1Ev
+ __ZN2AT11Translation19AUAsyncRendererHost10InitializeEv
+ __ZN2AT11Translation19AUAsyncRendererHost12UninitializeEv
+ __ZN2AT11Translation19AUAsyncRendererHost13UpdateFormatsEv
+ __ZN2AT11Translation21AudioStreamTranslator12ProcessAudioERK15AudioBufferListi
+ __ZN2AT11Translation21AudioStreamTranslator14BufferCompleteEPK15AudioBufferListb
+ __ZN2AT11Translation21AudioStreamTranslator39getPreferredAudioStreamBasicDescriptionEv
+ __ZN2AT11Translation21AudioStreamTranslator6CreateENS0_14CallTranslator5ScopeERKNS0_24TranslationConfigurationE
+ __ZN2AT11Translation21AudioStreamTranslatorD0Ev
+ __ZN2AT11Translation21AudioStreamTranslatorD1Ev
+ __ZN2AT11Translation21AudioStreamTranslatorD2Ev
+ __ZN2AT11Translation23gTranslationDeferredLogE
+ __ZN2AT11Translation24AudioTranslationInjector11InjectAudioER15AudioBufferListiRK15XAudioTimeStamp
+ __ZN2AT11Translation24AudioTranslationInjector11InjectAudioERK15AudioBufferListRS2_iRK15XAudioTimeStamp
+ __ZN2AT11Translation24AudioTranslationInjector18AudioFormatChangedENS0_14CallTranslator5ScopeERKN2CA17StreamDescriptionERKNS4_13ChannelLayoutE
+ __ZN2AT11Translation24AudioTranslationInjector19InjectAudioInternalERK15AudioBufferListRS2_iRK15XAudioTimeStamp
+ __ZN2AT11Translation24AudioTranslationInjector29HandleProcessingEndedCallbackEv
+ __ZN2AT11Translation24AudioTranslationInjector7getModeEv
+ __ZN2AT11Translation24AudioTranslationInjectorD0Ev
+ __ZN2AT11Translation24AudioTranslationInjectorD1Ev
+ __ZN2AT11Translation24AudioTranslationInjectorD2Ev
+ __ZN2AT11Translation25AsyncAudioStreamProcessorD0Ev
+ __ZN2AT11Translation25AsyncAudioStreamProcessorD1Ev
+ __ZN2AT11Translation25AsyncAudioStreamProcessorD2Ev
+ __ZN2AT11Translation27TranslationFeedbackInjector11InjectAudioER15AudioBufferListiRK15XAudioTimeStamp
+ __ZN2AT11Translation27TranslationFeedbackInjector11InjectAudioERK15AudioBufferListRS2_iRK15XAudioTimeStamp
+ __ZN2AT11Translation27TranslationFeedbackInjector12SetInputMuteEb
+ __ZN2AT11Translation27TranslationFeedbackInjector18AudioFormatChangedENS0_14CallTranslator5ScopeERKN2CA17StreamDescriptionERKNS4_13ChannelLayoutE
+ __ZN2AT11Translation27TranslationFeedbackInjector6CreateENS0_14CallTranslator5ScopeERKN2CA17StreamDescriptionERKNS4_13ChannelLayoutES3_S7_SA_j
+ __ZN2AT11Translation27TranslationFeedbackInjector7getModeEv
+ __ZN2AT11Translation27TranslationFeedbackInjectorD0Ev
+ __ZN2AT11Translation27TranslationFeedbackInjectorD1Ev
+ __ZN2AT11Translation27TranslationFeedbackInjectorD2Ev
+ __ZN2AT11TranslationeqERKNS0_24TranslationConfigurationES3_
+ __ZN2AT11TranslationeqERKNS0_35AudioStreamTranslationConfigurationES3_
+ __ZN2AT13SessionFacade11ManagerBase19createIONodeSessionERK11AQMESession
+ __ZN2AT13SessionFacade11ManagerBase20allowEnhanceDialogueERK11AQMESession
+ __ZN2AT13SessionFacade11ManagerBase21requestApplyInputMuteEjb
+ __ZN2AT13SessionFacade11ManagerBase25resolvedSpatialExperienceERK11AQMESession
+ __ZN2AT13SessionFacade11ManagerBase26clientMayUseHardwareCodecsEjPh
+ __ZN2AT13SessionFacade11ManagerBase28getAudioSesionServerPropertyEjjPvPj
+ __ZN2AT13SessionFacade11ManagerBase28setAudioSesionServerPropertyEjjPvj
+ __ZN2AT13SessionFacade11ManagerBase30setAudioSessionClientMuteStateEj30AVAudioSessionClientPlayerTypePvb
+ __ZN2AT13SessionFacade11ManagerBase31setCurrentlyPlayingSourceFormatEPKvRK14AQIONodeClientRN2CA17StreamDescriptionEbbb
+ __ZN2AT13SessionFacade7Manager19createIONodeSessionERK11AQMESession
+ __ZN2AT13SessionFacade7Manager20allowEnhanceDialogueERK11AQMESession
+ __ZN2AT13SessionFacade7Manager21requestApplyInputMuteEjb
+ __ZN2AT13SessionFacade7Manager25resolvedSpatialExperienceERK11AQMESession
+ __ZN2AT13SessionFacade7Manager26clientMayUseHardwareCodecsEjPh
+ __ZN2AT13SessionFacade7Manager28getAudioSesionServerPropertyEjjPvPj
+ __ZN2AT13SessionFacade7Manager28setAudioSesionServerPropertyEjjPvj
+ __ZN2AT13SessionFacade7Manager30setAudioSessionClientMuteStateEj30AVAudioSessionClientPlayerTypePvb
+ __ZN2AT13SessionFacade7Manager31setCurrentlyPlayingSourceFormatEPKvRK14AQIONodeClientRN2CA17StreamDescriptionEbbb
+ __ZN2AT14AudioTapClient4Impl12TapInterfaceEv
+ __ZN2AT17AudioTapClientHAL15CreateTapDeviceEv
+ __ZN2AT17AudioTapClientHAL23SetupScreenSharingStateEv
+ __ZN2AT17AudioTapClientHAL6UpdateERKS0_
+ __ZN2AT17AudioTapClientHALC1EPKvj
+ __ZN2AT17AudioTapClientHALC2EPKvj
+ __ZN2AT17AudioTapClientHALD0Ev
+ __ZN2AT17AudioTapClientHALD1Ev
+ __ZN2AT17AudioTapClientHALD2Ev
+ __ZN2CA16AudioBuffersBaseC1ERK27AudioStreamBasicDescriptionj
+ __ZN2CA16AudioBuffersBaseC2EP23ExtendedAudioBufferListj
+ __ZN2CA16AudioBuffersBaseC2ERK27AudioStreamBasicDescriptionj
+ __ZN2CA16AudioBuffersBaseD1Ev
+ __ZN2CA22AudioBuffersDeprecated7PrepareEjj
+ __ZN2CA22AudioBuffersDeprecatedD1Ev
+ __ZN2LS15LSDatabaseReadyEv
+ __ZN4swix17connection_configD2Ev
+ __ZN4swix6resultIJN10applesauce3xpc6objectENS_6stringEjEED2Ev
+ __ZN4swix6resultIJN10applesauce3xpc6objectEjjbNSt3__16vectorIjNS4_9allocatorIjEEEEEED2Ev
+ __ZN4swix6resultIJjj27AudioStreamBasicDescriptionN10applesauce3xpc6objectES4_EED2Ev
+ __ZN5Phase13ServerManager12IONodeClientD2Ev
+ __ZN5boost3msm4back13state_machineIN11SequenceFSM10StateFront11ActiveFrontENS_9parameter5void_ES7_S7_S7_E20clear_deferred_queueEv
+ __ZN5boost3msm4back13state_machineIN11SequenceFSM10StateFrontENS_9parameter5void_ES6_S6_S6_ED2Ev
+ __ZN5boost6fusion3setIJNS_3msm5front4euml10func_stateIN11SequenceFSM10StateFront12PausingNamerENS7_12PausingEntryENS7_11PausingExitENS0_6vectorIJEEENS_3mpl6vectorINS6_9IsRunningENS6_9IsPausingEN4mpl_2naESI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_EENSE_INS6_6ResumeENS6_4PlayENS6_4SeekENS6_4StopENS6_13EnableLoopingESI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_EENS6_9NamedBaseIS8_EEEENS5_INS7_13FinishedNamerENS7_12DefaultEntryENS7_11DefaultExitESC_NSE_INS6_10IsFinishedESI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_EENSD_7vector0ISI_EENSQ_IST_EEEENS2_4back13state_machineINS7_11ActiveFrontENS_9parameter5void_ES16_S16_S16_EENS5_INS7_13StartingNamerENS7_13StartingEntryENS7_12StartingExitESC_NSE_INS6_10IsStartingESI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_EESZ_NSQ_IS18_EEEENS5_INS7_20StartingForPlayNamerENS7_20StartingForPlayEntryENS7_19StartingForPlayExitESC_S1C_SZ_NSQ_IS1F_EEEENS5_INS7_13PreparedNamerESU_SV_SC_SX_SZ_NSQ_IS1K_EEEENS5_INS7_11LoadedNamerESU_SV_SC_SZ_SZ_NSQ_IS1N_EEEENS5_INS7_18UninitializedNamerESU_SV_SC_SZ_SZ_NSQ_IS1Q_EEEEEED2Ev
+ __ZN5boost9typeindex6detailL23ctti_skip_until_runtimeE.9430
+ __ZN5caulk10concurrent26lf_read_synchronized_writeIN15AQProcessingTap12TimelineInfoEE9T_storage7destroyEv
+ __ZN5caulk10concurrent26lf_read_synchronized_writeIN15AQProcessingTap12TimelineInfoEED2Ev
+ __ZN5caulk10concurrent26lf_read_synchronized_writeINSt3__110shared_ptrIN2AT11Translation14CallTranslatorEEEE7mutatorD2Ev
+ __ZN5caulk10concurrent26lf_read_synchronized_writeINSt3__110shared_ptrIN2AT11Translation14CallTranslatorEEEED2Ev
+ __ZN5caulk10concurrent26lf_read_synchronized_writeINSt3__110unique_ptrIN18MixTapToUplinkHost46MixTapToUplinkGroupedByMicrophoneInjectionModeENS2_14default_deleteIS5_EEEEE5writeES8_
+ __ZN5caulk10concurrent26lf_read_synchronized_writeIPN2AT11Translation13AudioInjectorEE5writeES5_
+ __ZN5caulk10concurrent26lf_read_synchronized_writeIPN2AT11Translation13AudioInjectorEEC2Ev
+ __ZN5caulk10concurrent5stackIN16AudioQueueObject14ScheduledSliceENS2_23ScheduledSliceAllocator16SliceNextAdapterEE3popEv
+ __ZN5caulk10concurrent7details12message_callIRZN11ClientEntry19handleSequenceEndedEmNS_16inplace_functionIFvmELm32ELm8ENS_23inplace_function_detail6vtableEEEE3$_0JEE7performEv
+ __ZN5caulk10concurrent7details12message_callIRZN11ClientEntry19handleSequenceEndedEmNS_16inplace_functionIFvmELm32ELm8ENS_23inplace_function_detail6vtableEEEE3$_0JEED0Ev
+ __ZN5caulk10concurrent7details12message_callIRZN11ClientEntry19handleSequenceEndedEmNS_16inplace_functionIFvmELm32ELm8ENS_23inplace_function_detail6vtableEEEE3$_0JEED1Ev
+ __ZN5caulk10concurrent7details15rt_message_callIRZN10XAudioUnit6RenderEPjPK14AudioTimeStampjjP15AudioBufferListEUlvE_JEE6createESB_
+ __ZN5caulk10concurrent7details15rt_message_callIRZN11ClientEntry19handleSequenceEndedEmNS_16inplace_functionIFvmELm32ELm8ENS_23inplace_function_detail6vtableEEEE3$_0JEE10rt_cleanupD1Ev
+ __ZN5caulk10concurrent7details15rt_message_callIRZN11ClientEntry19handleSequenceEndedEmNS_16inplace_functionIFvmELm32ELm8ENS_23inplace_function_detail6vtableEEEE3$_0JEE7performEv
+ __ZN5caulk10concurrent7details15rt_message_callIRZN11ClientEntry19handleSequenceEndedEmNS_16inplace_functionIFvmELm32ELm8ENS_23inplace_function_detail6vtableEEEE3$_0JEED0Ev
+ __ZN5caulk10concurrent7details15rt_message_callIRZN11ClientEntry19handleSequenceEndedEmNS_16inplace_functionIFvmELm32ELm8ENS_23inplace_function_detail6vtableEEEE3$_0JEED1Ev
+ __ZN5caulk12function_refIFvR9TapSubmixEE15functor_invokerIZN13MESubmixGraph19attach1MixerChannelEP14MEMixerChannelE3$_1EEvRKNS_7details15erased_callableIS3_EES2_
+ __ZN5caulk12function_refIFvR9TapSubmixiEE15functor_invokerIZN12_GLOBAL__N_131GetNumberOfTapSubmixConnectionsER14MEMixerChannelRK17AudioTapSpecifierE3$_0EEvRKNS_7details15erased_callableIS3_EES2_i
+ __ZN5caulk12function_refIFvR9TapSubmixiEE15functor_invokerIZN14MEMixerChannel24SetMixerInputBalanceModeEj20AudioBalanceFadeTypeE3$_0EEvRKNS_7details15erased_callableIS3_EES2_i
+ __ZN5caulk12synchronizedIN2AQ3API7Manager12GuardedStateENS_4mach11unfair_lockENS_22empty_atomic_interfaceIS4_EEED2Ev
+ __ZN5caulk15lazy_injectableIN2AT11Translation18CallTranslatorBaseEE9lazy_initEv
+ __ZN5caulk15rt_function_refIFvR9TapSubmixibEE15functor_invokerIZN14MEMixerChannel15ResetMixerInputEjE3$_0EEvRKNS_7details18erased_callable_rtIFvS2_ibEEES2_ib
+ __ZN5caulk15rt_function_refIFvR9TapSubmixibEE15functor_invokerIZN14MEMixerChannel16SetMixerInputPanEjfE3$_0EEvRKNS_7details18erased_callable_rtIFvS2_ibEEES2_ib
+ __ZN5caulk15rt_function_refIFvR9TapSubmixibEE15functor_invokerIZN14MEMixerChannel23ScheduleMixerParametersEjRNS_2rt6vectorI23AudioUnitParameterEventEEE3$_0EEvRKNS_7details18erased_callable_rtIFvS2_ibEEES2_ib
+ __ZN5caulk16inplace_functionIFvmELm32ELm8ENS_23inplace_function_detail6vtableEE16k_wrapper_vtableINSt3__18functionIS1_EEEE
+ __ZN5caulk16inplace_functionIFvmELm32ELm8ENS_23inplace_function_detail6vtableEE16k_wrapper_vtableIZ54-[AVHapticServerInstance prepareHapticSequence:reply:]E3$_1EE
+ __ZN5caulk16inplace_functionIFvmELm32ELm8ENS_23inplace_function_detail6vtableEE16k_wrapper_vtableIZN13ServerManager16playAlertPatternENSt3__110shared_ptrI11ClientEntryEEPKvfP20SSPlayerSynchronizerjU13block_pointerFvvEE3$_0EE
+ __ZN5caulk17__expected_detail4baseINSt3__14pairINS2_10unique_ptrIN2AT11Translation24AudioTranslationInjectorENS2_14default_deleteIS7_EEEENS4_INS6_27TranslationFeedbackInjectorENS8_ISB_EEEEEEiED2Ev
+ __ZN5caulk23inplace_function_detail6vtableIvJmEE5emptyE
+ __ZN5caulk23inplace_function_detail9rt_vtableIvJRKNS_10concurrent7details13skiplist_nodeIPvNS_5alloc6detail13tracked_blockEE9layout_vkEEE5emptyE
+ __ZN5caulk23recursive_mutex_adapterINS_22pooled_semaphore_mutexEE4lockEv
+ __ZN5caulk23recursive_mutex_adapterINS_22pooled_semaphore_mutexEE6unlockEv
+ __ZN5caulk23recursive_mutex_adapterINS_22pooled_semaphore_mutexEE8try_lockEv
+ __ZN5caulk23recursive_mutex_adapterINS_4mach11unfair_lockEE6unlockEv
+ __ZN5caulk2rt6vectorI10ChaseEventE9push_backEOS2_
+ __ZN5caulk2rt6vectorI11VolumeEventE9push_backEOS2_
+ __ZN5caulk2rt6vectorI23AudioUnitParameterEventE9push_backEOS2_
+ __ZN5caulk2rt6vectorINSt3__14pairIffEEE12emplace_backIJRffEEERS4_DpOT_
+ __ZN5caulk2rt6vectorIcE6resizeEm
+ __ZN5caulk5alloc16serial_allocatorINS0_18embed_block_memoryELm16368EE8allocateEmm
+ __ZN5caulk5build6detail8get_kindEv
+ __ZN5caulk7details19lifetime_guard_baseIN2AT11Translation16TranslatorClientEED2Ev
+ __ZN5caulk7product16get_device_classEv
+ __ZN5caulk7product25short_hardware_model_nameEv
+ __ZN5caulk8expectedI11AQMESessioniED1Ev
+ __ZN5caulk8expectedI35ATAudioProcessingNodeConnectionInfoiED1Ev
+ __ZN5caulk8expectedINSt3__15tupleIJN4swix4dataEEEEiEC2EOS6_
+ __ZN8AQIONode17AddProcessingNodeER14AQIONodeClientR16AQProcessingNode
+ __ZN8AQIONode22updateTapsForSessionIDEj
+ __ZN8AQIONode28SetCallTranslationPropertiesEPK14__CFDictionaryRb
+ __ZN8RTLockedINSt3__13mapEKjJjEED1Ev
+ __ZN8RTLockedINSt3__13mapEmJNS0_10shared_ptrI11ClientEntryEEEED1Ev
+ __ZN8RTLockedINSt3__13mapEmJjEED1Ev
+ __ZN8XAUMixerD2Ev
+ __ZN8audioipc13ipc_node_baseILNS_15ipcnode_optionsE0ENS_19eventlink_primitiveEN5caulk3ipc13mapped_memoryEE4sendEd
+ __ZN9TapSourceD2Ev
+ __ZN9TapSubmix10InputStateD2Ev
+ __ZNK10AQMEDevice15IsOfflineRenderEv
+ __ZNK10AQMEDevice18AnyDuckingChannelsEv
+ __ZNK10AQMEDevice18GetIOUnitMaxFramesEv
+ __ZNK10AQMEDevice26SingleChannelMappingClientEv
+ __ZNK10applesauce2CF13DictionaryRef6get_nsEv
+ __ZNK10applesauce2CF7TypeRefcvNS0_13DictionaryRefEEv
+ __ZNK10applesauce2CF9StringRef6get_nsEv
+ __ZNK11PListLogger3logEPKcz
+ __ZNK13MESubmixGraph12streamClientEv
+ __ZNK13MESubmixGraph12tapSpecifierEv
+ __ZNK13MESubmixGraph16mixChannelLayoutEv
+ __ZNK13MESubmixGraph25IsProcessOrSystemTappableEv
+ __ZNK13MESubmixGraph25getProcessingChainLatencyEv
+ __ZNK13MESubmixGraph6deviceEv
+ __ZNK13MESubmixGraph7debugIDEv
+ __ZNK13MESubmixGraph9mixFormatEv
+ __ZNK14AQIONodeClient13IsEnhanceableEv
+ __ZNK14AQIONodeClient25AudioSessionIsEnhanceableEv
+ __ZNK14AQIONodeClient25EnhanceDialogueIsSelectedEv
+ __ZNK14MEInputManager10DebugPrintEP7__sFILE
+ __ZNK14MEMixerChannel15GetHeadTrackingEv
+ __ZNK14MEMixerChannel15MixerSampleRateEv
+ __ZNK14MixTapToUplink16AQMETapConnector14GetDescriptionEv
+ __ZNK14MixTapToUplink16AQMETapConnector24GetAudioSessionIDsOfTapsEv
+ __ZNK14MixTapToUplink24GetAudioSessionIDsOfTapsEv
+ __ZNK15LoudnessManager19IsHardwareSupportedEv
+ __ZNK16AudioQueueObject13IsEnhanceableEv
+ __ZNK16AudioQueueObject19AudioSessionIsValidEv
+ __ZNK16AudioQueueObject19ConverterConnection17DecoderHandlesDRCEv
+ __ZNK17AudioTapSpecifier17isAudioSessionTapEv
+ __ZNK17AudioTapSpecifier7getUUIDEv
+ __ZNK17IONodeSessionStub12ownerSessionEv
+ __ZNK17IONodeSessionStub18getSceneIdentifierERN10applesauce2CF9StringRefE
+ __ZNK17IONodeSessionStub33getResolvedSpatialAudioExperienceERN10applesauce2CF7TypeRefE
+ __ZNK19IDeviceStreamClient15isDefaultOutputEv
+ __ZNK19IONodeSessionLegacy12ownerSessionEv
+ __ZNK19IONodeSessionLegacy18getSceneIdentifierERN10applesauce2CF9StringRefE
+ __ZNK19IONodeSessionLegacy33getResolvedSpatialAudioExperienceERN10applesauce2CF7TypeRefE
+ __ZNK19SSClientPlayOptions12GetXPCObjectEv
+ __ZNK20MEDeviceStreamClient10MEStreamIDEv
+ __ZNK20MEDeviceStreamClient13IsHighQualityEv
+ __ZNK20MEDeviceStreamClient13cachedLatencyEv
+ __ZNK20MEDeviceStreamClient18IOUnitClientFormatEv
+ __ZNK20MEDeviceStreamClient18RunningClientCountEv
+ __ZNK20MEDeviceStreamClient19IOUnitChannelLayoutEv
+ __ZNK20MEDeviceStreamClient21pendingAttachToStreamEv
+ __ZNK20MEDeviceStreamClient7IsInputEv
+ __ZNK20MEOutputStreamClient15isDefaultOutputEv
+ __ZNK21ScheduledSlicePlayer221FutureFramesScheduledEv
+ __ZNK21ScheduledSlicePlayer222GetRecentRenderEndTimeEv
+ __ZNK21ScheduledSlicePlayer222LatestBufferRenderTimeEv
+ __ZNK21ScheduledSlicePlayer230WriteAlignmentAdjustmentNeededEv
+ __ZNK21ScheduledSlicePlayer25emptyEv
+ __ZNK24CAStreamBasicDescription12IsEquivalentERK27AudioStreamBasicDescription
+ __ZNK25MEParallelPathSubmixGraph10activePortEv
+ __ZNK25MEParallelPathSubmixGraph34isEnhanceDialogueCapableActivePortEv
+ __ZNK26AudioTapHALReferenceStream12tapDeviceUIDEv
+ __ZNK26MutedSpeechActivityManager4Impl15getClientTokensEv
+ __ZNK27ScheduledSlicePlayer_Legacy21FutureFramesScheduledEv
+ __ZNK27ScheduledSlicePlayer_Legacy22GetRecentRenderEndTimeEv
+ __ZNK27ScheduledSlicePlayer_Legacy22LatestBufferRenderTimeEv
+ __ZNK27ScheduledSlicePlayer_Legacy30WriteAlignmentAdjustmentNeededEv
+ __ZNK27ScheduledSlicePlayer_Legacy5emptyEv
+ __ZNK2AT11Translation21AudioStreamTranslator15IsOutputEnabledEv
+ __ZNK2AT11Translation21AudioStreamTranslator22GetNumberOfInputFramesEv
+ __ZNK2AT17AudioTapClientHAL15GetTapDeviceUIDEv
+ __ZNK4swix14decode_message6decodeIiEET_PKc
+ __ZNK4swix14decode_message6decodeIjEET_PKc
+ __ZNK5caulk10concurrent26lf_read_synchronized_writeINSt3__110shared_ptrIN2AT11Translation14CallTranslatorEEEE6accessIZN19DSP_Routing_VoiceIO23AccessProcessorPropertyE13MEProcessorIDjbRjPvE3$_0EEvOT_
+ __ZNK5caulk10concurrent26lf_read_synchronized_writeINSt3__16vectorINS2_10shared_ptrI9TapSubmixEENS2_9allocatorIS6_EEEEE6accessIZN13MESubmixGraph17renderTapSubmixesEiRK14AudioTimeStampEUlRKT_E_EEvOSG_
+ __ZNK9TapSubmix16canAttachChannelERK14MEMixerChannel
+ __ZNKRSt3__118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEE3strB8ne200100Ev
+ __ZNKRSt3__119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEE3strB8ne200100Ev
+ __ZNKSt3__110__function6__funcIN5caulk16inplace_functionIFvmELm32ELm8ENS2_23inplace_function_detail6vtableEEENS_9allocatorIS7_EES4_E7__cloneEPNS0_6__baseIS4_EE
+ __ZNKSt3__110__function6__funcIN5caulk16inplace_functionIFvmELm32ELm8ENS2_23inplace_function_detail6vtableEEENS_9allocatorIS7_EES4_E7__cloneEv
+ __ZNKSt3__110__function6__funcINS_6__bindIMN2AT11Translation14CallTranslatorEFvNS5_5ScopeENS4_17AudioInjectorModeEEJPS5_RKNS_12placeholders4__phILi1EEERKNSC_ILi2EEEEEENS_9allocatorISJ_EEFvS6_S7_EE7__cloneEPNS0_6__baseISM_EE
+ __ZNKSt3__110__function6__funcINS_6__bindIMN2AT11Translation14CallTranslatorEFvNS5_5ScopeENS4_17AudioInjectorModeEEJPS5_RKNS_12placeholders4__phILi1EEERKNSC_ILi2EEEEEENS_9allocatorISJ_EEFvS6_S7_EE7__cloneEv
+ __ZNKSt3__110__function6__funcINS_6__bindIMN2AT11Translation24AudioTranslationInjectorEFvvEJPS5_EEENS_9allocatorIS9_EEFvvEE7__cloneEPNS0_6__baseISC_EE
+ __ZNKSt3__110__function6__funcINS_6__bindIMN2AT11Translation24AudioTranslationInjectorEFvvEJPS5_EEENS_9allocatorIS9_EEFvvEE7__cloneEv
+ __ZNKSt3__110__function6__funcINS_6__bindIRFN5caulk8expectedINS_10unique_ptrIN14MixTapToUplink19TappedAudioProducerENS_14default_deleteIS7_EEEEiEERKN2CA17StreamDescriptionERKNSC_13ChannelLayoutEiRKNS_13unordered_setIjNS_4hashIjEENS_8equal_toIjEENS_9allocatorIjEEEEEJRKNS_12placeholders4__phILi1EEERKNSW_ILi2EEERKNSW_ILi3EEERKNSW_ILi4EEEEEENSO_IS19_EEST_E7__cloneEPNS0_6__baseIST_EE
+ __ZNKSt3__110__function6__funcINS_6__bindIRFN5caulk8expectedINS_10unique_ptrIN14MixTapToUplink19TappedAudioProducerENS_14default_deleteIS7_EEEEiEERKN2CA17StreamDescriptionERKNSC_13ChannelLayoutEiRKNS_13unordered_setIjNS_4hashIjEENS_8equal_toIjEENS_9allocatorIjEEEEEJRKNS_12placeholders4__phILi1EEERKNSW_ILi2EEERKNSW_ILi3EEERKNSW_ILi4EEEEEENSO_IS19_EEST_E7__cloneEv
+ __ZNKSt3__110__function6__funcINS_6__bindIRFN5caulk8expectedINS_10unique_ptrIN2AT11Translation25AsyncAudioStreamProcessorENS_14default_deleteIS8_EEEEiEENS7_14CallTranslator5ScopeERKNS7_24TranslationConfigurationEEJRKNS_12placeholders4__phILi1EEERKNSL_ILi2EEEEEENS_9allocatorISS_EESI_E7__cloneEPNS0_6__baseISI_EE
+ __ZNKSt3__110__function6__funcINS_6__bindIRFN5caulk8expectedINS_10unique_ptrIN2AT11Translation25AsyncAudioStreamProcessorENS_14default_deleteIS8_EEEEiEENS7_14CallTranslator5ScopeERKNS7_24TranslationConfigurationEEJRKNS_12placeholders4__phILi1EEERKNSL_ILi2EEEEEENS_9allocatorISS_EESI_E7__cloneEv
+ __ZNKSt3__110__function6__funcINS_6__bindIRFNS_13unordered_mapIjiNS_4hashIjEENS_8equal_toIjEENS_9allocatorINS_4pairIKjiEEEEEEvEJEEENS8_ISG_EESE_E7__cloneEPNS0_6__baseISE_EE
+ __ZNKSt3__110__function6__funcINS_6__bindIRFNS_13unordered_mapIjiNS_4hashIjEENS_8equal_toIjEENS_9allocatorINS_4pairIKjiEEEEEEvEJEEENS8_ISG_EESE_E7__cloneEv
+ __ZNKSt3__110__function6__funcIZ24AQMEIOManager_FindIOUnitRK14AQMEIO_BindingE3$_0NS_9allocatorIS5_EEFNS_10unique_ptrI16AQMEIO_InterfaceNS_14default_deleteIS9_EEEES4_RiEE7__cloneEPNS0_6__baseISE_EE
+ __ZNKSt3__110__function6__funcIZ24AQMEIOManager_FindIOUnitRK14AQMEIO_BindingE3$_0NS_9allocatorIS5_EEFNS_10unique_ptrI16AQMEIO_InterfaceNS_14default_deleteIS9_EEEES4_RiEE7__cloneEv
+ __ZNKSt3__110__function6__funcIZ25AudioSessionSetCMPropertyE3$_1NS_9allocatorIS2_EEFNS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS3_IcEEEESA_EEN10applesauce2CF7TypeRefESE_EE7__cloneEPNS0_6__baseISF_EE
+ __ZNKSt3__110__function6__funcIZ25AudioSessionSetCMPropertyE3$_1NS_9allocatorIS2_EEFNS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS3_IcEEEESA_EEN10applesauce2CF7TypeRefESE_EE7__cloneEv
+ __ZNKSt3__110__function6__funcIZ27TranslateCMSessionErrorCodePKcRKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEiiE3$_1NS7_ISC_EEFNS_4pairIS9_S9_EEN10applesauce2CF7TypeRefESI_EE7__cloneEPNS0_6__baseISJ_EE
+ __ZNKSt3__110__function6__funcIZ27TranslateCMSessionErrorCodePKcRKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEiiE3$_1NS7_ISC_EEFNS_4pairIS9_S9_EEN10applesauce2CF7TypeRefESI_EE7__cloneEv
+ __ZNKSt3__110__function6__funcIZ29SystemSoundServerPlayActionIDE3$_1NS_9allocatorIS2_EEFvvEE7__cloneEPNS0_6__baseIS5_EE
+ __ZNKSt3__110__function6__funcIZ29SystemSoundServerPlayActionIDE3$_1NS_9allocatorIS2_EEFvvEE7__cloneEv
+ __ZNKSt3__110__function6__funcIZ62-[AVHapticServer incrementRunningCountForAudio:haptics:entry:]E3$_3NS_9allocatorIS2_EEFivEE7__cloneEPNS0_6__baseIS5_EE
+ __ZNKSt3__110__function6__funcIZ62-[AVHapticServer incrementRunningCountForAudio:haptics:entry:]E3$_3NS_9allocatorIS2_EEFivEE7__cloneEv
+ __ZNKSt3__110__function6__funcIZN10AQMEIO_HAL13UpdateStreamsEvE3$_0NS_9allocatorIS3_EEFbRK26AudioObjectPropertyAddressEE7__cloneEPNS0_6__baseIS9_EE
+ __ZNKSt3__110__function6__funcIZN10AQMEIO_HAL13UpdateStreamsEvE3$_0NS_9allocatorIS3_EEFbRK26AudioObjectPropertyAddressEE7__cloneEv
+ __ZNKSt3__110__function6__funcIZN11ClientEntry17doPrepareSequenceENS_10shared_ptrI14HapticSequenceEEN5caulk16inplace_functionIFvmELm32ELm8ENS6_23inplace_function_detail6vtableEEEE3$_0NS_9allocatorISC_EES8_E7__cloneEPNS0_6__baseIS8_EE
+ __ZNKSt3__110__function6__funcIZN11ClientEntry17doPrepareSequenceENS_10shared_ptrI14HapticSequenceEEN5caulk16inplace_functionIFvmELm32ELm8ENS6_23inplace_function_detail6vtableEEEE3$_0NS_9allocatorISC_EES8_E7__cloneEv
+ __ZNKSt3__110__function6__funcIZN13MESubmixGraph19attach1MixerChannelEP14MEMixerChannelE3$_0NS_9allocatorIS5_EEFvvEE7__cloneEPNS0_6__baseIS8_EE
+ __ZNKSt3__110__function6__funcIZN13MESubmixGraph19attach1MixerChannelEP14MEMixerChannelE3$_0NS_9allocatorIS5_EEFvvEE7__cloneEv
+ __ZNKSt3__110__function6__funcIZN13ServerManager12DoRenderProcERK14AudioTimeStampjE3$_0NS_9allocatorIS6_EEFKNS2_12SynthCommandEvEE7__cloneEPNS0_6__baseISB_EE
+ __ZNKSt3__110__function6__funcIZN13ServerManager12DoRenderProcERK14AudioTimeStampjE3$_0NS_9allocatorIS6_EEFKNS2_12SynthCommandEvEE7__cloneEv
+ __ZNKSt3__110__function6__funcIZN14DSP_Routing_VP28SetCallTranslationPropertiesEPK14__CFDictionaryRbE3$_0NS_9allocatorIS7_EEFvvEE7__cloneEPNS0_6__baseISA_EE
+ __ZNKSt3__110__function6__funcIZN14DSP_Routing_VP28SetCallTranslationPropertiesEPK14__CFDictionaryRbE3$_0NS_9allocatorIS7_EEFvvEE7__cloneEv
+ __ZNKSt3__110__function6__funcIZN15AQMixEngine_VAD17maintainVADevicesEbE3$_0NS_9allocatorIS3_EEFbR14AQIONodeClientEE7__cloneEPNS0_6__baseIS8_EE
+ __ZNKSt3__110__function6__funcIZN15AQMixEngine_VAD17maintainVADevicesEbE3$_0NS_9allocatorIS3_EEFbR14AQIONodeClientEE7__cloneEv
+ __ZNKSt3__110__function6__funcIZN15AQMixEngine_VAD28routeSupportsEnhanceDialogueEvE3$_0NS_9allocatorIS3_EEFvR11IAQMEDeviceEE7__cloneEPNS0_6__baseIS8_EE
+ __ZNKSt3__110__function6__funcIZN15AQMixEngine_VAD28routeSupportsEnhanceDialogueEvE3$_0NS_9allocatorIS3_EEFvR11IAQMEDeviceEE7__cloneEv
+ __ZNKSt3__110__function6__funcIZN15AQMixEngine_VAD31IsOwnerOfAudioObject_DeprecatedEjEUlR11IAQMEDeviceE_NS_9allocatorIS5_EEFvS4_EE7__cloneEPNS0_6__baseIS8_EE
+ __ZNKSt3__110__function6__funcIZN15AQMixEngine_VAD31IsOwnerOfAudioObject_DeprecatedEjEUlR11IAQMEDeviceE_NS_9allocatorIS5_EEFvS4_EE7__cloneEv
+ __ZNKSt3__110__function6__funcIZN15AQMixEngine_VAD37SetAudioObjectPropertyData_DeprecatedEjRK26AudioObjectPropertyAddressjPKvjS7_EUlR11IAQMEDeviceE_NS_9allocatorISA_EEFvS9_EE7__cloneEPNS0_6__baseISD_EE
+ __ZNKSt3__110__function6__funcIZN15AQMixEngine_VAD37SetAudioObjectPropertyData_DeprecatedEjRK26AudioObjectPropertyAddressjPKvjS7_EUlR11IAQMEDeviceE_NS_9allocatorISA_EEFvS9_EE7__cloneEv
+ __ZNKSt3__110__function6__funcIZN16AQMixEngine_Base12maintainTapsEbEUlR11IAQMEDeviceE_NS_9allocatorIS5_EEFvS4_EE7__cloneEPNS0_6__baseIS8_EE
+ __ZNKSt3__110__function6__funcIZN16AQMixEngine_Base12maintainTapsEbEUlR11IAQMEDeviceE_NS_9allocatorIS5_EEFvS4_EE7__cloneEv
+ __ZNKSt3__110__function6__funcIZN16AQMixEngine_Base13silenceOutputERK11AQMESessionjEUlR11IAQMEDeviceE_NS_9allocatorIS8_EEFvS7_EE7__cloneEPNS0_6__baseISB_EE
+ __ZNKSt3__110__function6__funcIZN16AQMixEngine_Base13silenceOutputERK11AQMESessionjEUlR11IAQMEDeviceE_NS_9allocatorIS8_EEFvS7_EE7__cloneEv
+ __ZNKSt3__110__function6__funcIZN16AQMixEngine_Base14DebugPrintFromEP7__sFILEPKcE3$_0NS_9allocatorIS7_EEFvR11IAQMEDeviceEE7__cloneEPNS0_6__baseISC_EE
+ __ZNKSt3__110__function6__funcIZN16AQMixEngine_Base14DebugPrintFromEP7__sFILEPKcE3$_0NS_9allocatorIS7_EEFvR11IAQMEDeviceEE7__cloneEv
+ __ZNKSt3__110__function6__funcIZN16AQMixEngine_Base16StopFreewheelingEvEUlR11IAQMEDeviceE_NS_9allocatorIS5_EEFvS4_EE7__cloneEPNS0_6__baseIS8_EE
+ __ZNKSt3__110__function6__funcIZN16AQMixEngine_Base16StopFreewheelingEvEUlR11IAQMEDeviceE_NS_9allocatorIS5_EEFvS4_EE7__cloneEv
+ __ZNKSt3__110__function6__funcIZN16AQMixEngine_Base17SoundCheckChangedEvEUlR11IAQMEDeviceE_NS_9allocatorIS5_EEFvS4_EE7__cloneEPNS0_6__baseIS8_EE
+ __ZNKSt3__110__function6__funcIZN16AQMixEngine_Base17SoundCheckChangedEvEUlR11IAQMEDeviceE_NS_9allocatorIS5_EEFvS4_EE7__cloneEv
+ __ZNKSt3__110__function6__funcIZN16AQMixEngine_Base18setDynamicsEnabledE15EDynamicsEnableEUlR11IAQMEDeviceE_NS_9allocatorIS6_EEFvS5_EE7__cloneEPNS0_6__baseIS9_EE
+ __ZNKSt3__110__function6__funcIZN16AQMixEngine_Base18setDynamicsEnabledE15EDynamicsEnableEUlR11IAQMEDeviceE_NS_9allocatorIS6_EEFvS5_EE7__cloneEv
+ __ZNKSt3__110__function6__funcIZN16AQMixEngine_Base22updateTapsForSessionIDEjEUlR11IAQMEDeviceE_NS_9allocatorIS5_EEFvS4_EE7__cloneEPNS0_6__baseIS8_EE
+ __ZNKSt3__110__function6__funcIZN16AQMixEngine_Base22updateTapsForSessionIDEjEUlR11IAQMEDeviceE_NS_9allocatorIS5_EEFvS4_EE7__cloneEv
+ __ZNKSt3__110__function6__funcIZN16AQMixEngine_Base23MonoAudioSettingChangedEvEUlR11IAQMEDeviceE_NS_9allocatorIS5_EEFvS4_EE7__cloneEPNS0_6__baseIS8_EE
+ __ZNKSt3__110__function6__funcIZN16AQMixEngine_Base23MonoAudioSettingChangedEvEUlR11IAQMEDeviceE_NS_9allocatorIS5_EEFvS4_EE7__cloneEv
+ __ZNKSt3__110__function6__funcIZN16AQMixEngine_Base25AccessibilityPrefsChangedEvEUlR11IAQMEDeviceE_NS_9allocatorIS5_EEFvS4_EE7__cloneEPNS0_6__baseIS8_EE
+ __ZNKSt3__110__function6__funcIZN16AQMixEngine_Base25AccessibilityPrefsChangedEvEUlR11IAQMEDeviceE_NS_9allocatorIS5_EEFvS4_EE7__cloneEv
+ __ZNKSt3__110__function6__funcIZN16AQMixEngine_Base25ScreenSharingStateChangedEyEUlR11IAQMEDeviceE_NS_9allocatorIS5_EEFvS4_EE7__cloneEPNS0_6__baseIS8_EE
+ __ZNKSt3__110__function6__funcIZN16AQMixEngine_Base25ScreenSharingStateChangedEyEUlR11IAQMEDeviceE_NS_9allocatorIS5_EEFvS4_EE7__cloneEv
+ __ZNKSt3__110__function6__funcIZN16AQMixEngine_Base27DistributeProcessorPropertyE13MEProcessorIDjRjPvEUlR11IAQMEDeviceE_NS_9allocatorIS8_EEFvS7_EE7__cloneEPNS0_6__baseISB_EE
+ __ZNKSt3__110__function6__funcIZN16AQMixEngine_Base27DistributeProcessorPropertyE13MEProcessorIDjRjPvEUlR11IAQMEDeviceE_NS_9allocatorIS8_EEFvS7_EE7__cloneEv
+ __ZNKSt3__110__function6__funcIZN16AQMixEngine_Base29RestartIOFollowingRouteChangeEvEUlR11IAQMEDeviceE_NS_9allocatorIS5_EEFvS4_EE7__cloneEPNS0_6__baseIS8_EE
+ __ZNKSt3__110__function6__funcIZN16AQMixEngine_Base29RestartIOFollowingRouteChangeEvEUlR11IAQMEDeviceE_NS_9allocatorIS5_EEFvS4_EE7__cloneEv
+ __ZNKSt3__110__function6__funcIZN17LegacyHapticSynth19handleRunModeChangeEjE3$_0NS_9allocatorIS3_EEFivEE7__cloneEPNS0_6__baseIS6_EE
+ __ZNKSt3__110__function6__funcIZN17LegacyHapticSynth19handleRunModeChangeEjE3$_0NS_9allocatorIS3_EEFivEE7__cloneEv
+ __ZNKSt3__110__function6__funcIZN21AVVoiceTriggerManager10InitializeEvE3$_0NS_9allocatorIS3_EEFbjRKN15CAListenerProxy15HALNotificationEEE7__cloneEPNS0_6__baseISA_EE
+ __ZNKSt3__110__function6__funcIZN21AVVoiceTriggerManager10InitializeEvE3$_0NS_9allocatorIS3_EEFbjRKN15CAListenerProxy15HALNotificationEEE7__cloneEv
+ __ZNKSt3__110__function6__funcIZN22MultiOutputHapticSynth12startRunningEbbjNS_8functionIFivEEEjE3$_0NS_9allocatorIS6_EES4_E7__cloneEPNS0_6__baseIS4_EE
+ __ZNKSt3__110__function6__funcIZN22MultiOutputHapticSynth12startRunningEbbjNS_8functionIFivEEEjE3$_0NS_9allocatorIS6_EES4_E7__cloneEv
+ __ZNKSt3__110__function6__funcIZN22MultiOutputHapticSynth19handleRunModeChangeEjE3$_0NS_9allocatorIS3_EEFivEE7__cloneEPNS0_6__baseIS6_EE
+ __ZNKSt3__110__function6__funcIZN22MultiOutputHapticSynth19handleRunModeChangeEjE3$_0NS_9allocatorIS3_EEFivEE7__cloneEv
+ __ZNKSt3__110__function6__funcIZN24AVVoiceTriggerServerImpl27enableVoiceTriggerListeningEbbU13block_pointerFvP7NSErrorEEUljRKN15CAListenerProxy15HALNotificationEE_NS_9allocatorISB_EEFbjSA_EE7__cloneEPNS0_6__baseISE_EE
+ __ZNKSt3__110__function6__funcIZN24AVVoiceTriggerServerImpl27enableVoiceTriggerListeningEbbU13block_pointerFvP7NSErrorEEUljRKN15CAListenerProxy15HALNotificationEE_NS_9allocatorISB_EEFbjSA_EE7__cloneEv
+ __ZNKSt3__110__function6__funcIZN24AVVoiceTriggerServerImpl31updateVoiceTriggerConfigurationEPK14__CFDictionaryU13block_pointerFvP7NSErrorEEUljRKN15CAListenerProxy15HALNotificationEE_NS_9allocatorISE_EEFbjSD_EE7__cloneEPNS0_6__baseISH_EE
+ __ZNKSt3__110__function6__funcIZN24AVVoiceTriggerServerImpl31updateVoiceTriggerConfigurationEPK14__CFDictionaryU13block_pointerFvP7NSErrorEEUljRKN15CAListenerProxy15HALNotificationEE_NS_9allocatorISE_EEFbjSD_EE7__cloneEv
+ __ZNKSt3__110__function6__funcIZN24AVVoiceTriggerServerImpl40registerStateChangedNotificationHandlersEbEUljRKN15CAListenerProxy15HALNotificationEE_NS_9allocatorIS7_EEFbjS6_EE7__cloneEPNS0_6__baseISA_EE
+ __ZNKSt3__110__function6__funcIZN24AVVoiceTriggerServerImpl40registerStateChangedNotificationHandlersEbEUljRKN15CAListenerProxy15HALNotificationEE_NS_9allocatorIS7_EEFbjS6_EE7__cloneEv
+ __ZNKSt3__110__function6__funcIZN24AVVoiceTriggerServerImpl42registerAOPVoiceTriggerNotificationHandlerEjbEUljRKN15CAListenerProxy15HALNotificationEE_NS_9allocatorIS7_EEFbjS6_EE7__cloneEPNS0_6__baseISA_EE
+ __ZNKSt3__110__function6__funcIZN24AVVoiceTriggerServerImpl42registerAOPVoiceTriggerNotificationHandlerEjbEUljRKN15CAListenerProxy15HALNotificationEE_NS_9allocatorIS7_EEFbjS6_EE7__cloneEv
+ __ZNKSt3__110__function6__funcIZN24AVVoiceTriggerServerImpl43registerAOPEnableChangedNotificationHandlerEbEUljRKN15CAListenerProxy15HALNotificationEE_NS_9allocatorIS7_EEFbjS6_EE7__cloneEPNS0_6__baseISA_EE
+ __ZNKSt3__110__function6__funcIZN24AVVoiceTriggerServerImpl43registerAOPEnableChangedNotificationHandlerEbEUljRKN15CAListenerProxy15HALNotificationEE_NS_9allocatorIS7_EEFbjS6_EE7__cloneEv
+ __ZNKSt3__110__function6__funcIZN2AQ3API7ManagerC1EbRNS3_11CaptureBaseEN5caulk19lifetime_erased_ptrI23AudioQueueXPC_InterfaceEEE3$_0NS_9allocatorISB_EEFvRN4swix12ipc_endpointERKN10applesauce3xpc6objectEEE7__cloneEPNS0_6__baseISM_EE
+ __ZNKSt3__110__function6__funcIZN2AQ3API7ManagerC1EbRNS3_11CaptureBaseEN5caulk19lifetime_erased_ptrI23AudioQueueXPC_InterfaceEEE3$_0NS_9allocatorISB_EEFvRN4swix12ipc_endpointERKN10applesauce3xpc6objectEEE7__cloneEv
+ __ZNKSt3__110__function6__funcIZN2AQ3API7ManagerC1EbRNS3_11CaptureBaseEN5caulk19lifetime_erased_ptrI23AudioQueueXPC_InterfaceEEE3$_1NS_9allocatorISB_EEFiN10applesauce3xpc6objectEEE7__cloneEPNS0_6__baseISH_EE
+ __ZNKSt3__110__function6__funcIZN2AQ3API7ManagerC1EbRNS3_11CaptureBaseEN5caulk19lifetime_erased_ptrI23AudioQueueXPC_InterfaceEEE3$_1NS_9allocatorISB_EEFiN10applesauce3xpc6objectEEE7__cloneEv
+ __ZNKSt3__110__function6__funcIZN2AT11Translation19AUAsyncRendererHost9ConfigureEvE3$_0NS_9allocatorIS5_EEFvNS_6chrono10time_pointINS8_12steady_clockENS8_8durationIxNS_5ratioILl1ELl1000000000EEEEEEERK15AudioBufferListiEE7__cloneEPNS0_6__baseISJ_EE
+ __ZNKSt3__110__function6__funcIZN2AT11Translation19AUAsyncRendererHost9ConfigureEvE3$_0NS_9allocatorIS5_EEFvNS_6chrono10time_pointINS8_12steady_clockENS8_8durationIxNS_5ratioILl1ELl1000000000EEEEEEERK15AudioBufferListiEE7__cloneEv
+ __ZNKSt3__110__function6__funcIZN30AudioSessionPropertyMarshaller15GetPropertyInfoEjE5$_127NS_9allocatorIS3_EEFP10MarshallervEE7__cloneEPNS0_6__baseIS8_EE
+ __ZNKSt3__110__function6__funcIZN30AudioSessionPropertyMarshaller15GetPropertyInfoEjE5$_127NS_9allocatorIS3_EEFP10MarshallervEE7__cloneEv
+ __ZNKSt3__110__function6__funcIZZN13MESubmixGraph19attach1MixerChannelEP14MEMixerChannelENK3$_1clI9TapSubmixEEDaRT_EUlvE_NS_9allocatorISB_EEFvvEE7__cloneEPNS0_6__baseISE_EE
+ __ZNKSt3__110__function6__funcIZZN13MESubmixGraph19attach1MixerChannelEP14MEMixerChannelENK3$_1clI9TapSubmixEEDaRT_EUlvE_NS_9allocatorISB_EEFvvEE7__cloneEv
+ __ZNKSt3__110__function6__funcIZZN14RemoteIOClient20IONode_FormatChangedEjEUb_E3$_1NS_9allocatorIS3_EEFvvEE7__cloneEPNS0_6__baseIS6_EE
+ __ZNKSt3__110__function6__funcIZZN14RemoteIOClient20IONode_FormatChangedEjEUb_E3$_1NS_9allocatorIS3_EEFvvEE7__cloneEv
+ __ZNKSt3__110__function6__funcIZZN22MultiOutputHapticSynth11stopRunningEbbjENK3$_0clERNS_10unique_ptrI11SynthOutputNS_14default_deleteIS5_EEEEEUlvE_NS_9allocatorISA_EEFvvEE7__cloneEPNS0_6__baseISD_EE
+ __ZNKSt3__110__function6__funcIZZN22MultiOutputHapticSynth11stopRunningEbbjENK3$_0clERNS_10unique_ptrI11SynthOutputNS_14default_deleteIS5_EEEEEUlvE_NS_9allocatorISA_EEFvvEE7__cloneEv
+ __ZNKSt3__111__copy_implclB8ne200100IP11AQMESessionS3_S3_EENS_4pairIT_T1_EES5_T0_S6_
+ __ZNKSt3__111__copy_implclB8ne200100IP15MEVADIdentifierS3_S3_EENS_4pairIT_T1_EES5_T0_S6_
+ __ZNKSt3__111__copy_implclB8ne200100IPK11AQMESessionS4_PS2_EENS_4pairIT_T1_EES7_T0_S8_
+ __ZNKSt3__111__move_implINS_17_ClassicAlgPolicyEEclB8ne200100IPNS_4pairIN5boost8functionIFNS5_3msm4back11HandledEnumEvEEEbEENS_16__deque_iteratorISC_SD_RSC_PSD_lLl102EEELi0EEENS4_IT_T0_EESI_SI_SJ_
+ __ZNKSt3__112__hash_tableINS_17__hash_value_typeIPK15AudioBufferListNS_4pairINS_6chrono10time_pointINS6_12steady_clockENS6_8durationIxNS_5ratioILl1ELl1000000000EEEEEEEU8__strongP16AVAudioPCMBufferEEEENS_22__unordered_map_hasherIS4_SI_NS_4hashIS4_EENS_8equal_toIS4_EELb1EEENS_21__unordered_map_equalIS4_SI_SN_SL_Lb1EEENS_9allocatorISI_EEE4findIS4_EENS_21__hash_const_iteratorIPNS_11__hash_nodeISI_PvEEEERKT_
+ __ZNKSt3__112__hash_tableINS_17__hash_value_typeIijEENS_22__unordered_map_hasherIiS2_NS_4hashIiEENS_8equal_toIiEELb1EEENS_21__unordered_map_equalIiS2_S7_S5_Lb1EEENS_9allocatorIS2_EEE19__equal_range_multiIiEENS_4pairINS_21__hash_const_iteratorIPNS_11__hash_nodeIS2_PvEEEESL_EERKT_
+ __ZNKSt3__113__string_hashIcNS_9allocatorIcEEEclB8ne200100ERKNS_12basic_stringIcNS_11char_traitsIcEES2_EE
+ __ZNKSt3__114default_deleteI13XOSTransactorEclB8ne200100EPS1_
+ __ZNKSt3__114default_deleteI15AudioTapManagerEclB8ne200100EPS1_
+ __ZNKSt3__114default_deleteI20SSSBufferClickFilterEclB8ne200100EPS1_
+ __ZNKSt3__114default_deleteI29AudioSessionPropertyListenersEclB8ne200100EPS1_
+ __ZNKSt3__114default_deleteI8AQBufferEclB8ne200100EPS1_
+ __ZNKSt3__114default_deleteIN12CADeprecated12CABufferListEEclB8ne200100EPS2_
+ __ZNKSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE4viewB8ne200100Ev
+ __ZNKSt3__120__move_backward_implINS_17_ClassicAlgPolicyEEclB8ne200100IPNS_4pairIN5boost8functionIFNS5_3msm4back11HandledEnumEvEEEbEENS_16__deque_iteratorISC_SD_RSC_PSD_lLl102EEELi0EEENS4_IT_T0_EESI_SI_SJ_
+ __ZNKSt3__18equal_toINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEclB8ne200100ERKS6_S9_
+ __ZNKSt3__18functionIFvNS_6chrono10time_pointINS1_12steady_clockENS1_8durationIxNS_5ratioILl1ELl1000000000EEEEEEERK15AudioBufferListiEEclES8_SB_i
+ __ZNR5caulk8expectedINSt3__110unique_ptrIN2AT11Translation24AudioTranslationInjectorENS1_14default_deleteIS5_EEEEiE5valueEv
+ __ZNR5caulk8expectedINSt3__110unique_ptrIN2AT11Translation27TranslationFeedbackInjectorENS1_14default_deleteIS5_EEEEiE5valueEv
+ __ZNR5caulk8expectedINSt3__14pairINS1_10unique_ptrIN2AT11Translation24AudioTranslationInjectorENS1_14default_deleteIS6_EEEENS3_INS5_27TranslationFeedbackInjectorENS7_ISA_EEEEEEiE5valueEv
+ __ZNSt12length_errorC1B8ne200100EPKc
+ __ZNSt12out_of_rangeC1B8ne200100EPKc
+ __ZNSt13exception_ptrC1ERKS_
+ __ZNSt13exception_ptrD1Ev
+ __ZNSt14overflow_errorC1B8ne200100EPKc
+ __ZNSt3__110__function12__value_funcIFKN13ServerManager12SynthCommandEvEED2B8ne200100Ev
+ __ZNSt3__110__function12__value_funcIFN5caulk8expectedINS_10unique_ptrIN14MixTapToUplink19TappedAudioProducerENS_14default_deleteIS6_EEEEiEERKN2CA17StreamDescriptionERKNSB_13ChannelLayoutEiRKNS_13unordered_setIjNS_4hashIjEENS_8equal_toIjEENS_9allocatorIjEEEEEEC2B8ne200100ERKST_
+ __ZNSt3__110__function12__value_funcIFN5caulk8expectedINS_10unique_ptrIN14MixTapToUplink19TappedAudioProducerENS_14default_deleteIS6_EEEEiEERKN2CA17StreamDescriptionERKNSB_13ChannelLayoutEiRKNS_13unordered_setIjNS_4hashIjEENS_8equal_toIjEENS_9allocatorIjEEEEEED2B8ne200100Ev
+ __ZNSt3__110__function12__value_funcIFN5caulk8expectedINS_10unique_ptrIN2AT11Translation25AsyncAudioStreamProcessorENS_14default_deleteIS7_EEEEiEENS6_14CallTranslator5ScopeERKNS6_24TranslationConfigurationEEEC2B8ne200100ERKSI_
+ __ZNSt3__110__function12__value_funcIFN5caulk8expectedINS_10unique_ptrIN2AT11Translation25AsyncAudioStreamProcessorENS_14default_deleteIS7_EEEEiEENS6_14CallTranslator5ScopeERKNS6_24TranslationConfigurationEEED2B8ne200100Ev
+ __ZNSt3__110__function12__value_funcIFN5caulk8expectedIbiEEjEEC2B8ne200100ERKS6_
+ __ZNSt3__110__function12__value_funcIFN5caulk8expectedIbiEEjEED2B8ne200100Ev
+ __ZNSt3__110__function12__value_funcIFNS_10unique_ptrI16AQMEIO_InterfaceNS_14default_deleteIS3_EEEERK14AQMEIO_BindingRiEEC2B8ne200100ERKSC_
+ __ZNSt3__110__function12__value_funcIFNS_10unique_ptrI16AQMEIO_InterfaceNS_14default_deleteIS3_EEEERK14AQMEIO_BindingRiEED2B8ne200100Ev
+ __ZNSt3__110__function12__value_funcIFNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEvEED2B8ne200100Ev
+ __ZNSt3__110__function12__value_funcIFNS_13unordered_mapIjiNS_4hashIjEENS_8equal_toIjEENS_9allocatorINS_4pairIKjiEEEEEEvEEC2B8ne200100ERKSE_
+ __ZNSt3__110__function12__value_funcIFNS_13unordered_mapIjiNS_4hashIjEENS_8equal_toIjEENS_9allocatorINS_4pairIKjiEEEEEEvEED2B8ne200100Ev
+ __ZNSt3__110__function12__value_funcIFNS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEES8_EEN10applesauce2CF7TypeRefESC_EEC2B8ne200100ERKSE_
+ __ZNSt3__110__function12__value_funcIFNS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEES8_EEN10applesauce2CF7TypeRefESC_EED2B8ne200100Ev
+ __ZNSt3__110__function12__value_funcIFP10MarshallervEEC2B8ne200100ERKS5_
+ __ZNSt3__110__function12__value_funcIFP10MarshallervEED2B8ne200100Ev
+ __ZNSt3__110__function12__value_funcIFPK10__CFStringS4_EEC2B8ne200100ERKS6_
+ __ZNSt3__110__function12__value_funcIFPK10__CFStringS4_EED2B8ne200100Ev
+ __ZNSt3__110__function12__value_funcIFR26MutedSpeechActivityManagervEEC2B8ne200100ERKS5_
+ __ZNSt3__110__function12__value_funcIFR26MutedSpeechActivityManagervEED2B8ne200100Ev
+ __ZNSt3__110__function12__value_funcIFbNS_10shared_ptrI11ClientEntryEEEED2B8ne200100Ev
+ __ZNSt3__110__function12__value_funcIFbPKN17ParameterSchedule5EventEEED2B8ne200100Ev
+ __ZNSt3__110__function12__value_funcIFbPKvEED2B8ne200100Ev
+ __ZNSt3__110__function12__value_funcIFbR14AQIONodeClientEED2B8ne200100Ev
+ __ZNSt3__110__function12__value_funcIFbRK26AudioObjectPropertyAddressEED2B8ne200100Ev
+ __ZNSt3__110__function12__value_funcIFbRmbEED2B8ne200100Ev
+ __ZNSt3__110__function12__value_funcIFbjRKN15CAListenerProxy15HALNotificationEEEC2B8ne200100ERKS7_
+ __ZNSt3__110__function12__value_funcIFbjRKN15CAListenerProxy15HALNotificationEEED2B8ne200100Ev
+ __ZNSt3__110__function12__value_funcIFbjiEEC2B8ne200100ERKS3_
+ __ZNSt3__110__function12__value_funcIFbjiEED2B8ne200100Ev
+ __ZNSt3__110__function12__value_funcIFbvEEC2B8ne200100ERKS3_
+ __ZNSt3__110__function12__value_funcIFbvEED2B8ne200100Ev
+ __ZNSt3__110__function12__value_funcIFiN10applesauce3xpc6objectEEED2B8ne200100Ev
+ __ZNSt3__110__function12__value_funcIFiP7__sFILEEED2B8ne200100Ev
+ __ZNSt3__110__function12__value_funcIFivEEC2B8ne200100ERKS3_
+ __ZNSt3__110__function12__value_funcIFivEED2B8ne200100Ev
+ __ZNSt3__110__function12__value_funcIFvN2AT11Translation14CallTranslator5ScopeENS3_17AudioInjectorModeEEED2B8ne200100Ev
+ __ZNSt3__110__function12__value_funcIFvNS_6chrono10time_pointINS2_12steady_clockENS2_8durationIxNS_5ratioILl1ELl1000000000EEEEEEERK15AudioBufferListiEED2B8ne200100Ev
+ __ZNSt3__110__function12__value_funcIFvPK14MIDIPacketListEED2B8ne200100Ev
+ __ZNSt3__110__function12__value_funcIFvR11IAQMEDeviceEED2B8ne200100Ev
+ __ZNSt3__110__function12__value_funcIFvRN4swix12ipc_endpointERKN10applesauce3xpc6objectEEED2B8ne200100Ev
+ __ZNSt3__110__function12__value_funcIFvbEEC2B8ne200100EOS3_
+ __ZNSt3__110__function12__value_funcIFvbEEC2B8ne200100ERKS3_
+ __ZNSt3__110__function12__value_funcIFvbEED2B8ne200100Ev
+ __ZNSt3__110__function12__value_funcIFvdEEC2B8ne200100ERKS3_
+ __ZNSt3__110__function12__value_funcIFvdEED2B8ne200100Ev
+ __ZNSt3__110__function12__value_funcIFviEEC2B8ne200100ERKS3_
+ __ZNSt3__110__function12__value_funcIFviEED2B8ne200100Ev
+ __ZNSt3__110__function12__value_funcIFvmEEC2B8ne200100ERKS3_
+ __ZNSt3__110__function12__value_funcIFvmEED2B8ne200100Ev
+ __ZNSt3__110__function12__value_funcIFvvEEC2B8ne200100EOS3_
+ __ZNSt3__110__function12__value_funcIFvvEEC2B8ne200100ERKS3_
+ __ZNSt3__110__function12__value_funcIFvvEED2B8ne200100Ev
+ __ZNSt3__110__function12__value_funcIFvxEEC2B8ne200100ERKS3_
+ __ZNSt3__110__function12__value_funcIFvxEED2B8ne200100Ev
+ __ZNSt3__110__function6__funcIN5caulk16inplace_functionIFvmELm32ELm8ENS2_23inplace_function_detail6vtableEEENS_9allocatorIS7_EES4_E18destroy_deallocateEv
+ __ZNSt3__110__function6__funcIN5caulk16inplace_functionIFvmELm32ELm8ENS2_23inplace_function_detail6vtableEEENS_9allocatorIS7_EES4_E7destroyEv
+ __ZNSt3__110__function6__funcIN5caulk16inplace_functionIFvmELm32ELm8ENS2_23inplace_function_detail6vtableEEENS_9allocatorIS7_EES4_ED0Ev
+ __ZNSt3__110__function6__funcIN5caulk16inplace_functionIFvmELm32ELm8ENS2_23inplace_function_detail6vtableEEENS_9allocatorIS7_EES4_ED1Ev
+ __ZNSt3__110__function6__funcIN5caulk16inplace_functionIFvmELm32ELm8ENS2_23inplace_function_detail6vtableEEENS_9allocatorIS7_EES4_EclEOm
+ __ZNSt3__110__function6__funcINS_6__bindIMN2AT11Translation14CallTranslatorEFvNS5_5ScopeENS4_17AudioInjectorModeEEJPS5_RKNS_12placeholders4__phILi1EEERKNSC_ILi2EEEEEENS_9allocatorISJ_EEFvS6_S7_EE18destroy_deallocateEv
+ __ZNSt3__110__function6__funcINS_6__bindIMN2AT11Translation14CallTranslatorEFvNS5_5ScopeENS4_17AudioInjectorModeEEJPS5_RKNS_12placeholders4__phILi1EEERKNSC_ILi2EEEEEENS_9allocatorISJ_EEFvS6_S7_EE7destroyEv
+ __ZNSt3__110__function6__funcINS_6__bindIMN2AT11Translation14CallTranslatorEFvNS5_5ScopeENS4_17AudioInjectorModeEEJPS5_RKNS_12placeholders4__phILi1EEERKNSC_ILi2EEEEEENS_9allocatorISJ_EEFvS6_S7_EED0Ev
+ __ZNSt3__110__function6__funcINS_6__bindIMN2AT11Translation14CallTranslatorEFvNS5_5ScopeENS4_17AudioInjectorModeEEJPS5_RKNS_12placeholders4__phILi1EEERKNSC_ILi2EEEEEENS_9allocatorISJ_EEFvS6_S7_EED1Ev
+ __ZNSt3__110__function6__funcINS_6__bindIMN2AT11Translation14CallTranslatorEFvNS5_5ScopeENS4_17AudioInjectorModeEEJPS5_RKNS_12placeholders4__phILi1EEERKNSC_ILi2EEEEEENS_9allocatorISJ_EEFvS6_S7_EEclEOS6_OS7_
+ __ZNSt3__110__function6__funcINS_6__bindIMN2AT11Translation24AudioTranslationInjectorEFvvEJPS5_EEENS_9allocatorIS9_EEFvvEE18destroy_deallocateEv
+ __ZNSt3__110__function6__funcINS_6__bindIMN2AT11Translation24AudioTranslationInjectorEFvvEJPS5_EEENS_9allocatorIS9_EEFvvEE7destroyEv
+ __ZNSt3__110__function6__funcINS_6__bindIMN2AT11Translation24AudioTranslationInjectorEFvvEJPS5_EEENS_9allocatorIS9_EEFvvEED0Ev
+ __ZNSt3__110__function6__funcINS_6__bindIMN2AT11Translation24AudioTranslationInjectorEFvvEJPS5_EEENS_9allocatorIS9_EEFvvEED1Ev
+ __ZNSt3__110__function6__funcINS_6__bindIMN2AT11Translation24AudioTranslationInjectorEFvvEJPS5_EEENS_9allocatorIS9_EEFvvEEclEv
+ __ZNSt3__110__function6__funcINS_6__bindIRFN5caulk8expectedINS_10unique_ptrIN14MixTapToUplink19TappedAudioProducerENS_14default_deleteIS7_EEEEiEERKN2CA17StreamDescriptionERKNSC_13ChannelLayoutEiRKNS_13unordered_setIjNS_4hashIjEENS_8equal_toIjEENS_9allocatorIjEEEEEJRKNS_12placeholders4__phILi1EEERKNSW_ILi2EEERKNSW_ILi3EEERKNSW_ILi4EEEEEENSO_IS19_EEST_E18destroy_deallocateEv
+ __ZNSt3__110__function6__funcINS_6__bindIRFN5caulk8expectedINS_10unique_ptrIN14MixTapToUplink19TappedAudioProducerENS_14default_deleteIS7_EEEEiEERKN2CA17StreamDescriptionERKNSC_13ChannelLayoutEiRKNS_13unordered_setIjNS_4hashIjEENS_8equal_toIjEENS_9allocatorIjEEEEEJRKNS_12placeholders4__phILi1EEERKNSW_ILi2EEERKNSW_ILi3EEERKNSW_ILi4EEEEEENSO_IS19_EEST_E7destroyEv
+ __ZNSt3__110__function6__funcINS_6__bindIRFN5caulk8expectedINS_10unique_ptrIN14MixTapToUplink19TappedAudioProducerENS_14default_deleteIS7_EEEEiEERKN2CA17StreamDescriptionERKNSC_13ChannelLayoutEiRKNS_13unordered_setIjNS_4hashIjEENS_8equal_toIjEENS_9allocatorIjEEEEEJRKNS_12placeholders4__phILi1EEERKNSW_ILi2EEERKNSW_ILi3EEERKNSW_ILi4EEEEEENSO_IS19_EEST_ED0Ev
+ __ZNSt3__110__function6__funcINS_6__bindIRFN5caulk8expectedINS_10unique_ptrIN14MixTapToUplink19TappedAudioProducerENS_14default_deleteIS7_EEEEiEERKN2CA17StreamDescriptionERKNSC_13ChannelLayoutEiRKNS_13unordered_setIjNS_4hashIjEENS_8equal_toIjEENS_9allocatorIjEEEEEJRKNS_12placeholders4__phILi1EEERKNSW_ILi2EEERKNSW_ILi3EEERKNSW_ILi4EEEEEENSO_IS19_EEST_ED1Ev
+ __ZNSt3__110__function6__funcINS_6__bindIRFN5caulk8expectedINS_10unique_ptrIN14MixTapToUplink19TappedAudioProducerENS_14default_deleteIS7_EEEEiEERKN2CA17StreamDescriptionERKNSC_13ChannelLayoutEiRKNS_13unordered_setIjNS_4hashIjEENS_8equal_toIjEENS_9allocatorIjEEEEEJRKNS_12placeholders4__phILi1EEERKNSW_ILi2EEERKNSW_ILi3EEERKNSW_ILi4EEEEEENSO_IS19_EEST_EclESF_SI_OiSS_
+ __ZNSt3__110__function6__funcINS_6__bindIRFN5caulk8expectedINS_10unique_ptrIN2AT11Translation25AsyncAudioStreamProcessorENS_14default_deleteIS8_EEEEiEENS7_14CallTranslator5ScopeERKNS7_24TranslationConfigurationEEJRKNS_12placeholders4__phILi1EEERKNSL_ILi2EEEEEENS_9allocatorISS_EESI_E18destroy_deallocateEv
+ __ZNSt3__110__function6__funcINS_6__bindIRFN5caulk8expectedINS_10unique_ptrIN2AT11Translation25AsyncAudioStreamProcessorENS_14default_deleteIS8_EEEEiEENS7_14CallTranslator5ScopeERKNS7_24TranslationConfigurationEEJRKNS_12placeholders4__phILi1EEERKNSL_ILi2EEEEEENS_9allocatorISS_EESI_E7destroyEv
+ __ZNSt3__110__function6__funcINS_6__bindIRFN5caulk8expectedINS_10unique_ptrIN2AT11Translation25AsyncAudioStreamProcessorENS_14default_deleteIS8_EEEEiEENS7_14CallTranslator5ScopeERKNS7_24TranslationConfigurationEEJRKNS_12placeholders4__phILi1EEERKNSL_ILi2EEEEEENS_9allocatorISS_EESI_ED0Ev
+ __ZNSt3__110__function6__funcINS_6__bindIRFN5caulk8expectedINS_10unique_ptrIN2AT11Translation25AsyncAudioStreamProcessorENS_14default_deleteIS8_EEEEiEENS7_14CallTranslator5ScopeERKNS7_24TranslationConfigurationEEJRKNS_12placeholders4__phILi1EEERKNSL_ILi2EEEEEENS_9allocatorISS_EESI_ED1Ev
+ __ZNSt3__110__function6__funcINS_6__bindIRFN5caulk8expectedINS_10unique_ptrIN2AT11Translation25AsyncAudioStreamProcessorENS_14default_deleteIS8_EEEEiEENS7_14CallTranslator5ScopeERKNS7_24TranslationConfigurationEEJRKNS_12placeholders4__phILi1EEERKNSL_ILi2EEEEEENS_9allocatorISS_EESI_EclEOSE_SH_
+ __ZNSt3__110__function6__funcINS_6__bindIRFNS_13unordered_mapIjiNS_4hashIjEENS_8equal_toIjEENS_9allocatorINS_4pairIKjiEEEEEEvEJEEENS8_ISG_EESE_E18destroy_deallocateEv
+ __ZNSt3__110__function6__funcINS_6__bindIRFNS_13unordered_mapIjiNS_4hashIjEENS_8equal_toIjEENS_9allocatorINS_4pairIKjiEEEEEEvEJEEENS8_ISG_EESE_E7destroyEv
+ __ZNSt3__110__function6__funcINS_6__bindIRFNS_13unordered_mapIjiNS_4hashIjEENS_8equal_toIjEENS_9allocatorINS_4pairIKjiEEEEEEvEJEEENS8_ISG_EESE_ED0Ev
+ __ZNSt3__110__function6__funcINS_6__bindIRFNS_13unordered_mapIjiNS_4hashIjEENS_8equal_toIjEENS_9allocatorINS_4pairIKjiEEEEEEvEJEEENS8_ISG_EESE_ED1Ev
+ __ZNSt3__110__function6__funcINS_6__bindIRFNS_13unordered_mapIjiNS_4hashIjEENS_8equal_toIjEENS_9allocatorINS_4pairIKjiEEEEEEvEJEEENS8_ISG_EESE_EclEv
+ __ZNSt3__110__function6__funcIZ24AQMEIOManager_FindIOUnitRK14AQMEIO_BindingE3$_0NS_9allocatorIS5_EEFNS_10unique_ptrI16AQMEIO_InterfaceNS_14default_deleteIS9_EEEES4_RiEE18destroy_deallocateEv
+ __ZNSt3__110__function6__funcIZ24AQMEIOManager_FindIOUnitRK14AQMEIO_BindingE3$_0NS_9allocatorIS5_EEFNS_10unique_ptrI16AQMEIO_InterfaceNS_14default_deleteIS9_EEEES4_RiEE7destroyEv
+ __ZNSt3__110__function6__funcIZ24AQMEIOManager_FindIOUnitRK14AQMEIO_BindingE3$_0NS_9allocatorIS5_EEFNS_10unique_ptrI16AQMEIO_InterfaceNS_14default_deleteIS9_EEEES4_RiEED0Ev
+ __ZNSt3__110__function6__funcIZ24AQMEIOManager_FindIOUnitRK14AQMEIO_BindingE3$_0NS_9allocatorIS5_EEFNS_10unique_ptrI16AQMEIO_InterfaceNS_14default_deleteIS9_EEEES4_RiEED1Ev
+ __ZNSt3__110__function6__funcIZ24AQMEIOManager_FindIOUnitRK14AQMEIO_BindingE3$_0NS_9allocatorIS5_EEFNS_10unique_ptrI16AQMEIO_InterfaceNS_14default_deleteIS9_EEEES4_RiEEclES4_SD_
+ __ZNSt3__110__function6__funcIZ25AudioSessionSetCMPropertyE3$_1NS_9allocatorIS2_EEFNS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS3_IcEEEESA_EEN10applesauce2CF7TypeRefESE_EE18destroy_deallocateEv
+ __ZNSt3__110__function6__funcIZ25AudioSessionSetCMPropertyE3$_1NS_9allocatorIS2_EEFNS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS3_IcEEEESA_EEN10applesauce2CF7TypeRefESE_EE7destroyEv
+ __ZNSt3__110__function6__funcIZ25AudioSessionSetCMPropertyE3$_1NS_9allocatorIS2_EEFNS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS3_IcEEEESA_EEN10applesauce2CF7TypeRefESE_EED0Ev
+ __ZNSt3__110__function6__funcIZ25AudioSessionSetCMPropertyE3$_1NS_9allocatorIS2_EEFNS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS3_IcEEEESA_EEN10applesauce2CF7TypeRefESE_EED1Ev
+ __ZNSt3__110__function6__funcIZ25AudioSessionSetCMPropertyE3$_1NS_9allocatorIS2_EEFNS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS3_IcEEEESA_EEN10applesauce2CF7TypeRefESE_EEclEOSE_SH_
+ __ZNSt3__110__function6__funcIZ27TranslateCMSessionErrorCodePKcRKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEiiE3$_1NS7_ISC_EEFNS_4pairIS9_S9_EEN10applesauce2CF7TypeRefESI_EE18destroy_deallocateEv
+ __ZNSt3__110__function6__funcIZ27TranslateCMSessionErrorCodePKcRKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEiiE3$_1NS7_ISC_EEFNS_4pairIS9_S9_EEN10applesauce2CF7TypeRefESI_EE7destroyEv
+ __ZNSt3__110__function6__funcIZ27TranslateCMSessionErrorCodePKcRKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEiiE3$_1NS7_ISC_EEFNS_4pairIS9_S9_EEN10applesauce2CF7TypeRefESI_EED0Ev
+ __ZNSt3__110__function6__funcIZ27TranslateCMSessionErrorCodePKcRKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEiiE3$_1NS7_ISC_EEFNS_4pairIS9_S9_EEN10applesauce2CF7TypeRefESI_EED1Ev
+ __ZNSt3__110__function6__funcIZ27TranslateCMSessionErrorCodePKcRKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEiiE3$_1NS7_ISC_EEFNS_4pairIS9_S9_EEN10applesauce2CF7TypeRefESI_EEclEOSI_SL_
+ __ZNSt3__110__function6__funcIZ29SystemSoundServerPlayActionIDE3$_1NS_9allocatorIS2_EEFvvEE18destroy_deallocateEv
+ __ZNSt3__110__function6__funcIZ29SystemSoundServerPlayActionIDE3$_1NS_9allocatorIS2_EEFvvEE7destroyEv
+ __ZNSt3__110__function6__funcIZ29SystemSoundServerPlayActionIDE3$_1NS_9allocatorIS2_EEFvvEED0Ev
+ __ZNSt3__110__function6__funcIZ29SystemSoundServerPlayActionIDE3$_1NS_9allocatorIS2_EEFvvEED1Ev
+ __ZNSt3__110__function6__funcIZ29SystemSoundServerPlayActionIDE3$_1NS_9allocatorIS2_EEFvvEEclEv
+ __ZNSt3__110__function6__funcIZ62-[AVHapticServer incrementRunningCountForAudio:haptics:entry:]E3$_3NS_9allocatorIS2_EEFivEE18destroy_deallocateEv
+ __ZNSt3__110__function6__funcIZ62-[AVHapticServer incrementRunningCountForAudio:haptics:entry:]E3$_3NS_9allocatorIS2_EEFivEE7destroyEv
+ __ZNSt3__110__function6__funcIZ62-[AVHapticServer incrementRunningCountForAudio:haptics:entry:]E3$_3NS_9allocatorIS2_EEFivEED0Ev
+ __ZNSt3__110__function6__funcIZ62-[AVHapticServer incrementRunningCountForAudio:haptics:entry:]E3$_3NS_9allocatorIS2_EEFivEED1Ev
+ __ZNSt3__110__function6__funcIZ62-[AVHapticServer incrementRunningCountForAudio:haptics:entry:]E3$_3NS_9allocatorIS2_EEFivEEclEv
+ __ZNSt3__110__function6__funcIZN10AQMEIO_HAL13UpdateStreamsEvE3$_0NS_9allocatorIS3_EEFbRK26AudioObjectPropertyAddressEE18destroy_deallocateEv
+ __ZNSt3__110__function6__funcIZN10AQMEIO_HAL13UpdateStreamsEvE3$_0NS_9allocatorIS3_EEFbRK26AudioObjectPropertyAddressEE7destroyEv
+ __ZNSt3__110__function6__funcIZN10AQMEIO_HAL13UpdateStreamsEvE3$_0NS_9allocatorIS3_EEFbRK26AudioObjectPropertyAddressEED0Ev
+ __ZNSt3__110__function6__funcIZN10AQMEIO_HAL13UpdateStreamsEvE3$_0NS_9allocatorIS3_EEFbRK26AudioObjectPropertyAddressEED1Ev
+ __ZNSt3__110__function6__funcIZN10AQMEIO_HAL13UpdateStreamsEvE3$_0NS_9allocatorIS3_EEFbRK26AudioObjectPropertyAddressEEclES8_
+ __ZNSt3__110__function6__funcIZN11ClientEntry17doPrepareSequenceENS_10shared_ptrI14HapticSequenceEEN5caulk16inplace_functionIFvmELm32ELm8ENS6_23inplace_function_detail6vtableEEEE3$_0NS_9allocatorISC_EES8_E18destroy_deallocateEv
+ __ZNSt3__110__function6__funcIZN11ClientEntry17doPrepareSequenceENS_10shared_ptrI14HapticSequenceEEN5caulk16inplace_functionIFvmELm32ELm8ENS6_23inplace_function_detail6vtableEEEE3$_0NS_9allocatorISC_EES8_E7destroyEv
+ __ZNSt3__110__function6__funcIZN11ClientEntry17doPrepareSequenceENS_10shared_ptrI14HapticSequenceEEN5caulk16inplace_functionIFvmELm32ELm8ENS6_23inplace_function_detail6vtableEEEE3$_0NS_9allocatorISC_EES8_ED0Ev
+ __ZNSt3__110__function6__funcIZN11ClientEntry17doPrepareSequenceENS_10shared_ptrI14HapticSequenceEEN5caulk16inplace_functionIFvmELm32ELm8ENS6_23inplace_function_detail6vtableEEEE3$_0NS_9allocatorISC_EES8_ED1Ev
+ __ZNSt3__110__function6__funcIZN11ClientEntry17doPrepareSequenceENS_10shared_ptrI14HapticSequenceEEN5caulk16inplace_functionIFvmELm32ELm8ENS6_23inplace_function_detail6vtableEEEE3$_0NS_9allocatorISC_EES8_EclEOm
+ __ZNSt3__110__function6__funcIZN13MESubmixGraph19attach1MixerChannelEP14MEMixerChannelE3$_0NS_9allocatorIS5_EEFvvEE18destroy_deallocateEv
+ __ZNSt3__110__function6__funcIZN13MESubmixGraph19attach1MixerChannelEP14MEMixerChannelE3$_0NS_9allocatorIS5_EEFvvEE7destroyEv
+ __ZNSt3__110__function6__funcIZN13MESubmixGraph19attach1MixerChannelEP14MEMixerChannelE3$_0NS_9allocatorIS5_EEFvvEED0Ev
+ __ZNSt3__110__function6__funcIZN13MESubmixGraph19attach1MixerChannelEP14MEMixerChannelE3$_0NS_9allocatorIS5_EEFvvEED1Ev
+ __ZNSt3__110__function6__funcIZN13MESubmixGraph19attach1MixerChannelEP14MEMixerChannelE3$_0NS_9allocatorIS5_EEFvvEEclEv
+ __ZNSt3__110__function6__funcIZN13ServerManager12DoRenderProcERK14AudioTimeStampjE3$_0NS_9allocatorIS6_EEFKNS2_12SynthCommandEvEE18destroy_deallocateEv
+ __ZNSt3__110__function6__funcIZN13ServerManager12DoRenderProcERK14AudioTimeStampjE3$_0NS_9allocatorIS6_EEFKNS2_12SynthCommandEvEE7destroyEv
+ __ZNSt3__110__function6__funcIZN13ServerManager12DoRenderProcERK14AudioTimeStampjE3$_0NS_9allocatorIS6_EEFKNS2_12SynthCommandEvEED0Ev
+ __ZNSt3__110__function6__funcIZN13ServerManager12DoRenderProcERK14AudioTimeStampjE3$_0NS_9allocatorIS6_EEFKNS2_12SynthCommandEvEED1Ev
+ __ZNSt3__110__function6__funcIZN13ServerManager12DoRenderProcERK14AudioTimeStampjE3$_0NS_9allocatorIS6_EEFKNS2_12SynthCommandEvEEclEv
+ __ZNSt3__110__function6__funcIZN14DSP_Routing_VP28SetCallTranslationPropertiesEPK14__CFDictionaryRbE3$_0NS_9allocatorIS7_EEFvvEE18destroy_deallocateEv
+ __ZNSt3__110__function6__funcIZN14DSP_Routing_VP28SetCallTranslationPropertiesEPK14__CFDictionaryRbE3$_0NS_9allocatorIS7_EEFvvEE7destroyEv
+ __ZNSt3__110__function6__funcIZN14DSP_Routing_VP28SetCallTranslationPropertiesEPK14__CFDictionaryRbE3$_0NS_9allocatorIS7_EEFvvEED0Ev
+ __ZNSt3__110__function6__funcIZN14DSP_Routing_VP28SetCallTranslationPropertiesEPK14__CFDictionaryRbE3$_0NS_9allocatorIS7_EEFvvEED1Ev
+ __ZNSt3__110__function6__funcIZN14DSP_Routing_VP28SetCallTranslationPropertiesEPK14__CFDictionaryRbE3$_0NS_9allocatorIS7_EEFvvEEclEv
+ __ZNSt3__110__function6__funcIZN15AQMixEngine_VAD17maintainVADevicesEbE3$_0NS_9allocatorIS3_EEFbR14AQIONodeClientEE18destroy_deallocateEv
+ __ZNSt3__110__function6__funcIZN15AQMixEngine_VAD17maintainVADevicesEbE3$_0NS_9allocatorIS3_EEFbR14AQIONodeClientEE7destroyEv
+ __ZNSt3__110__function6__funcIZN15AQMixEngine_VAD17maintainVADevicesEbE3$_0NS_9allocatorIS3_EEFbR14AQIONodeClientEED0Ev
+ __ZNSt3__110__function6__funcIZN15AQMixEngine_VAD17maintainVADevicesEbE3$_0NS_9allocatorIS3_EEFbR14AQIONodeClientEED1Ev
+ __ZNSt3__110__function6__funcIZN15AQMixEngine_VAD17maintainVADevicesEbE3$_0NS_9allocatorIS3_EEFbR14AQIONodeClientEEclES7_
+ __ZNSt3__110__function6__funcIZN15AQMixEngine_VAD28routeSupportsEnhanceDialogueEvE3$_0NS_9allocatorIS3_EEFvR11IAQMEDeviceEE18destroy_deallocateEv
+ __ZNSt3__110__function6__funcIZN15AQMixEngine_VAD28routeSupportsEnhanceDialogueEvE3$_0NS_9allocatorIS3_EEFvR11IAQMEDeviceEE7destroyEv
+ __ZNSt3__110__function6__funcIZN15AQMixEngine_VAD28routeSupportsEnhanceDialogueEvE3$_0NS_9allocatorIS3_EEFvR11IAQMEDeviceEED0Ev
+ __ZNSt3__110__function6__funcIZN15AQMixEngine_VAD28routeSupportsEnhanceDialogueEvE3$_0NS_9allocatorIS3_EEFvR11IAQMEDeviceEED1Ev
+ __ZNSt3__110__function6__funcIZN15AQMixEngine_VAD28routeSupportsEnhanceDialogueEvE3$_0NS_9allocatorIS3_EEFvR11IAQMEDeviceEEclES7_
+ __ZNSt3__110__function6__funcIZN15AQMixEngine_VAD31IsOwnerOfAudioObject_DeprecatedEjEUlR11IAQMEDeviceE_NS_9allocatorIS5_EEFvS4_EE18destroy_deallocateEv
+ __ZNSt3__110__function6__funcIZN15AQMixEngine_VAD31IsOwnerOfAudioObject_DeprecatedEjEUlR11IAQMEDeviceE_NS_9allocatorIS5_EEFvS4_EE7destroyEv
+ __ZNSt3__110__function6__funcIZN15AQMixEngine_VAD31IsOwnerOfAudioObject_DeprecatedEjEUlR11IAQMEDeviceE_NS_9allocatorIS5_EEFvS4_EED0Ev
+ __ZNSt3__110__function6__funcIZN15AQMixEngine_VAD31IsOwnerOfAudioObject_DeprecatedEjEUlR11IAQMEDeviceE_NS_9allocatorIS5_EEFvS4_EED1Ev
+ __ZNSt3__110__function6__funcIZN15AQMixEngine_VAD31IsOwnerOfAudioObject_DeprecatedEjEUlR11IAQMEDeviceE_NS_9allocatorIS5_EEFvS4_EEclES4_
+ __ZNSt3__110__function6__funcIZN15AQMixEngine_VAD37SetAudioObjectPropertyData_DeprecatedEjRK26AudioObjectPropertyAddressjPKvjS7_EUlR11IAQMEDeviceE_NS_9allocatorISA_EEFvS9_EE18destroy_deallocateEv
+ __ZNSt3__110__function6__funcIZN15AQMixEngine_VAD37SetAudioObjectPropertyData_DeprecatedEjRK26AudioObjectPropertyAddressjPKvjS7_EUlR11IAQMEDeviceE_NS_9allocatorISA_EEFvS9_EE7destroyEv
+ __ZNSt3__110__function6__funcIZN15AQMixEngine_VAD37SetAudioObjectPropertyData_DeprecatedEjRK26AudioObjectPropertyAddressjPKvjS7_EUlR11IAQMEDeviceE_NS_9allocatorISA_EEFvS9_EED0Ev
+ __ZNSt3__110__function6__funcIZN15AQMixEngine_VAD37SetAudioObjectPropertyData_DeprecatedEjRK26AudioObjectPropertyAddressjPKvjS7_EUlR11IAQMEDeviceE_NS_9allocatorISA_EEFvS9_EED1Ev
+ __ZNSt3__110__function6__funcIZN15AQMixEngine_VAD37SetAudioObjectPropertyData_DeprecatedEjRK26AudioObjectPropertyAddressjPKvjS7_EUlR11IAQMEDeviceE_NS_9allocatorISA_EEFvS9_EEclES9_
+ __ZNSt3__110__function6__funcIZN16AQMixEngine_Base12maintainTapsEbEUlR11IAQMEDeviceE_NS_9allocatorIS5_EEFvS4_EE18destroy_deallocateEv
+ __ZNSt3__110__function6__funcIZN16AQMixEngine_Base12maintainTapsEbEUlR11IAQMEDeviceE_NS_9allocatorIS5_EEFvS4_EE7destroyEv
+ __ZNSt3__110__function6__funcIZN16AQMixEngine_Base12maintainTapsEbEUlR11IAQMEDeviceE_NS_9allocatorIS5_EEFvS4_EED0Ev
+ __ZNSt3__110__function6__funcIZN16AQMixEngine_Base12maintainTapsEbEUlR11IAQMEDeviceE_NS_9allocatorIS5_EEFvS4_EED1Ev
+ __ZNSt3__110__function6__funcIZN16AQMixEngine_Base12maintainTapsEbEUlR11IAQMEDeviceE_NS_9allocatorIS5_EEFvS4_EEclES4_
+ __ZNSt3__110__function6__funcIZN16AQMixEngine_Base13silenceOutputERK11AQMESessionjEUlR11IAQMEDeviceE_NS_9allocatorIS8_EEFvS7_EE18destroy_deallocateEv
+ __ZNSt3__110__function6__funcIZN16AQMixEngine_Base13silenceOutputERK11AQMESessionjEUlR11IAQMEDeviceE_NS_9allocatorIS8_EEFvS7_EE7destroyEv
+ __ZNSt3__110__function6__funcIZN16AQMixEngine_Base13silenceOutputERK11AQMESessionjEUlR11IAQMEDeviceE_NS_9allocatorIS8_EEFvS7_EED0Ev
+ __ZNSt3__110__function6__funcIZN16AQMixEngine_Base13silenceOutputERK11AQMESessionjEUlR11IAQMEDeviceE_NS_9allocatorIS8_EEFvS7_EED1Ev
+ __ZNSt3__110__function6__funcIZN16AQMixEngine_Base13silenceOutputERK11AQMESessionjEUlR11IAQMEDeviceE_NS_9allocatorIS8_EEFvS7_EEclES7_
+ __ZNSt3__110__function6__funcIZN16AQMixEngine_Base14DebugPrintFromEP7__sFILEPKcE3$_0NS_9allocatorIS7_EEFvR11IAQMEDeviceEE18destroy_deallocateEv
+ __ZNSt3__110__function6__funcIZN16AQMixEngine_Base14DebugPrintFromEP7__sFILEPKcE3$_0NS_9allocatorIS7_EEFvR11IAQMEDeviceEE7destroyEv
+ __ZNSt3__110__function6__funcIZN16AQMixEngine_Base14DebugPrintFromEP7__sFILEPKcE3$_0NS_9allocatorIS7_EEFvR11IAQMEDeviceEED0Ev
+ __ZNSt3__110__function6__funcIZN16AQMixEngine_Base14DebugPrintFromEP7__sFILEPKcE3$_0NS_9allocatorIS7_EEFvR11IAQMEDeviceEED1Ev
+ __ZNSt3__110__function6__funcIZN16AQMixEngine_Base14DebugPrintFromEP7__sFILEPKcE3$_0NS_9allocatorIS7_EEFvR11IAQMEDeviceEEclESB_
+ __ZNSt3__110__function6__funcIZN16AQMixEngine_Base16StopFreewheelingEvEUlR11IAQMEDeviceE_NS_9allocatorIS5_EEFvS4_EE18destroy_deallocateEv
+ __ZNSt3__110__function6__funcIZN16AQMixEngine_Base16StopFreewheelingEvEUlR11IAQMEDeviceE_NS_9allocatorIS5_EEFvS4_EE7destroyEv
+ __ZNSt3__110__function6__funcIZN16AQMixEngine_Base16StopFreewheelingEvEUlR11IAQMEDeviceE_NS_9allocatorIS5_EEFvS4_EED0Ev
+ __ZNSt3__110__function6__funcIZN16AQMixEngine_Base16StopFreewheelingEvEUlR11IAQMEDeviceE_NS_9allocatorIS5_EEFvS4_EED1Ev
+ __ZNSt3__110__function6__funcIZN16AQMixEngine_Base16StopFreewheelingEvEUlR11IAQMEDeviceE_NS_9allocatorIS5_EEFvS4_EEclES4_
+ __ZNSt3__110__function6__funcIZN16AQMixEngine_Base17SoundCheckChangedEvEUlR11IAQMEDeviceE_NS_9allocatorIS5_EEFvS4_EE18destroy_deallocateEv
+ __ZNSt3__110__function6__funcIZN16AQMixEngine_Base17SoundCheckChangedEvEUlR11IAQMEDeviceE_NS_9allocatorIS5_EEFvS4_EE7destroyEv
+ __ZNSt3__110__function6__funcIZN16AQMixEngine_Base17SoundCheckChangedEvEUlR11IAQMEDeviceE_NS_9allocatorIS5_EEFvS4_EED0Ev
+ __ZNSt3__110__function6__funcIZN16AQMixEngine_Base17SoundCheckChangedEvEUlR11IAQMEDeviceE_NS_9allocatorIS5_EEFvS4_EED1Ev
+ __ZNSt3__110__function6__funcIZN16AQMixEngine_Base17SoundCheckChangedEvEUlR11IAQMEDeviceE_NS_9allocatorIS5_EEFvS4_EEclES4_
+ __ZNSt3__110__function6__funcIZN16AQMixEngine_Base18setDynamicsEnabledE15EDynamicsEnableEUlR11IAQMEDeviceE_NS_9allocatorIS6_EEFvS5_EE18destroy_deallocateEv
+ __ZNSt3__110__function6__funcIZN16AQMixEngine_Base18setDynamicsEnabledE15EDynamicsEnableEUlR11IAQMEDeviceE_NS_9allocatorIS6_EEFvS5_EE7destroyEv
+ __ZNSt3__110__function6__funcIZN16AQMixEngine_Base18setDynamicsEnabledE15EDynamicsEnableEUlR11IAQMEDeviceE_NS_9allocatorIS6_EEFvS5_EED0Ev
+ __ZNSt3__110__function6__funcIZN16AQMixEngine_Base18setDynamicsEnabledE15EDynamicsEnableEUlR11IAQMEDeviceE_NS_9allocatorIS6_EEFvS5_EED1Ev
+ __ZNSt3__110__function6__funcIZN16AQMixEngine_Base18setDynamicsEnabledE15EDynamicsEnableEUlR11IAQMEDeviceE_NS_9allocatorIS6_EEFvS5_EEclES5_
+ __ZNSt3__110__function6__funcIZN16AQMixEngine_Base22updateTapsForSessionIDEjEUlR11IAQMEDeviceE_NS_9allocatorIS5_EEFvS4_EE18destroy_deallocateEv
+ __ZNSt3__110__function6__funcIZN16AQMixEngine_Base22updateTapsForSessionIDEjEUlR11IAQMEDeviceE_NS_9allocatorIS5_EEFvS4_EE7destroyEv
+ __ZNSt3__110__function6__funcIZN16AQMixEngine_Base22updateTapsForSessionIDEjEUlR11IAQMEDeviceE_NS_9allocatorIS5_EEFvS4_EED0Ev
+ __ZNSt3__110__function6__funcIZN16AQMixEngine_Base22updateTapsForSessionIDEjEUlR11IAQMEDeviceE_NS_9allocatorIS5_EEFvS4_EED1Ev
+ __ZNSt3__110__function6__funcIZN16AQMixEngine_Base22updateTapsForSessionIDEjEUlR11IAQMEDeviceE_NS_9allocatorIS5_EEFvS4_EEclES4_
+ __ZNSt3__110__function6__funcIZN16AQMixEngine_Base23MonoAudioSettingChangedEvEUlR11IAQMEDeviceE_NS_9allocatorIS5_EEFvS4_EE18destroy_deallocateEv
+ __ZNSt3__110__function6__funcIZN16AQMixEngine_Base23MonoAudioSettingChangedEvEUlR11IAQMEDeviceE_NS_9allocatorIS5_EEFvS4_EE7destroyEv
+ __ZNSt3__110__function6__funcIZN16AQMixEngine_Base23MonoAudioSettingChangedEvEUlR11IAQMEDeviceE_NS_9allocatorIS5_EEFvS4_EED0Ev
+ __ZNSt3__110__function6__funcIZN16AQMixEngine_Base23MonoAudioSettingChangedEvEUlR11IAQMEDeviceE_NS_9allocatorIS5_EEFvS4_EED1Ev
+ __ZNSt3__110__function6__funcIZN16AQMixEngine_Base23MonoAudioSettingChangedEvEUlR11IAQMEDeviceE_NS_9allocatorIS5_EEFvS4_EEclES4_
+ __ZNSt3__110__function6__funcIZN16AQMixEngine_Base25AccessibilityPrefsChangedEvEUlR11IAQMEDeviceE_NS_9allocatorIS5_EEFvS4_EE18destroy_deallocateEv
+ __ZNSt3__110__function6__funcIZN16AQMixEngine_Base25AccessibilityPrefsChangedEvEUlR11IAQMEDeviceE_NS_9allocatorIS5_EEFvS4_EE7destroyEv
+ __ZNSt3__110__function6__funcIZN16AQMixEngine_Base25AccessibilityPrefsChangedEvEUlR11IAQMEDeviceE_NS_9allocatorIS5_EEFvS4_EED0Ev
+ __ZNSt3__110__function6__funcIZN16AQMixEngine_Base25AccessibilityPrefsChangedEvEUlR11IAQMEDeviceE_NS_9allocatorIS5_EEFvS4_EED1Ev
+ __ZNSt3__110__function6__funcIZN16AQMixEngine_Base25AccessibilityPrefsChangedEvEUlR11IAQMEDeviceE_NS_9allocatorIS5_EEFvS4_EEclES4_
+ __ZNSt3__110__function6__funcIZN16AQMixEngine_Base25ScreenSharingStateChangedEyEUlR11IAQMEDeviceE_NS_9allocatorIS5_EEFvS4_EE18destroy_deallocateEv
+ __ZNSt3__110__function6__funcIZN16AQMixEngine_Base25ScreenSharingStateChangedEyEUlR11IAQMEDeviceE_NS_9allocatorIS5_EEFvS4_EE7destroyEv
+ __ZNSt3__110__function6__funcIZN16AQMixEngine_Base25ScreenSharingStateChangedEyEUlR11IAQMEDeviceE_NS_9allocatorIS5_EEFvS4_EED0Ev
+ __ZNSt3__110__function6__funcIZN16AQMixEngine_Base25ScreenSharingStateChangedEyEUlR11IAQMEDeviceE_NS_9allocatorIS5_EEFvS4_EED1Ev
+ __ZNSt3__110__function6__funcIZN16AQMixEngine_Base25ScreenSharingStateChangedEyEUlR11IAQMEDeviceE_NS_9allocatorIS5_EEFvS4_EEclES4_
+ __ZNSt3__110__function6__funcIZN16AQMixEngine_Base27DistributeProcessorPropertyE13MEProcessorIDjRjPvEUlR11IAQMEDeviceE_NS_9allocatorIS8_EEFvS7_EE18destroy_deallocateEv
+ __ZNSt3__110__function6__funcIZN16AQMixEngine_Base27DistributeProcessorPropertyE13MEProcessorIDjRjPvEUlR11IAQMEDeviceE_NS_9allocatorIS8_EEFvS7_EE7destroyEv
+ __ZNSt3__110__function6__funcIZN16AQMixEngine_Base27DistributeProcessorPropertyE13MEProcessorIDjRjPvEUlR11IAQMEDeviceE_NS_9allocatorIS8_EEFvS7_EED0Ev
+ __ZNSt3__110__function6__funcIZN16AQMixEngine_Base27DistributeProcessorPropertyE13MEProcessorIDjRjPvEUlR11IAQMEDeviceE_NS_9allocatorIS8_EEFvS7_EED1Ev
+ __ZNSt3__110__function6__funcIZN16AQMixEngine_Base27DistributeProcessorPropertyE13MEProcessorIDjRjPvEUlR11IAQMEDeviceE_NS_9allocatorIS8_EEFvS7_EEclES7_
+ __ZNSt3__110__function6__funcIZN16AQMixEngine_Base29RestartIOFollowingRouteChangeEvEUlR11IAQMEDeviceE_NS_9allocatorIS5_EEFvS4_EE18destroy_deallocateEv
+ __ZNSt3__110__function6__funcIZN16AQMixEngine_Base29RestartIOFollowingRouteChangeEvEUlR11IAQMEDeviceE_NS_9allocatorIS5_EEFvS4_EE7destroyEv
+ __ZNSt3__110__function6__funcIZN16AQMixEngine_Base29RestartIOFollowingRouteChangeEvEUlR11IAQMEDeviceE_NS_9allocatorIS5_EEFvS4_EED0Ev
+ __ZNSt3__110__function6__funcIZN16AQMixEngine_Base29RestartIOFollowingRouteChangeEvEUlR11IAQMEDeviceE_NS_9allocatorIS5_EEFvS4_EED1Ev
+ __ZNSt3__110__function6__funcIZN16AQMixEngine_Base29RestartIOFollowingRouteChangeEvEUlR11IAQMEDeviceE_NS_9allocatorIS5_EEFvS4_EEclES4_
+ __ZNSt3__110__function6__funcIZN17LegacyHapticSynth19handleRunModeChangeEjE3$_0NS_9allocatorIS3_EEFivEE18destroy_deallocateEv
+ __ZNSt3__110__function6__funcIZN17LegacyHapticSynth19handleRunModeChangeEjE3$_0NS_9allocatorIS3_EEFivEE7destroyEv
+ __ZNSt3__110__function6__funcIZN17LegacyHapticSynth19handleRunModeChangeEjE3$_0NS_9allocatorIS3_EEFivEED0Ev
+ __ZNSt3__110__function6__funcIZN17LegacyHapticSynth19handleRunModeChangeEjE3$_0NS_9allocatorIS3_EEFivEED1Ev
+ __ZNSt3__110__function6__funcIZN17LegacyHapticSynth19handleRunModeChangeEjE3$_0NS_9allocatorIS3_EEFivEEclEv
+ __ZNSt3__110__function6__funcIZN21AVVoiceTriggerManager10InitializeEvE3$_0NS_9allocatorIS3_EEFbjRKN15CAListenerProxy15HALNotificationEEE18destroy_deallocateEv
+ __ZNSt3__110__function6__funcIZN21AVVoiceTriggerManager10InitializeEvE3$_0NS_9allocatorIS3_EEFbjRKN15CAListenerProxy15HALNotificationEEE7destroyEv
+ __ZNSt3__110__function6__funcIZN21AVVoiceTriggerManager10InitializeEvE3$_0NS_9allocatorIS3_EEFbjRKN15CAListenerProxy15HALNotificationEEED0Ev
+ __ZNSt3__110__function6__funcIZN21AVVoiceTriggerManager10InitializeEvE3$_0NS_9allocatorIS3_EEFbjRKN15CAListenerProxy15HALNotificationEEED1Ev
+ __ZNSt3__110__function6__funcIZN21AVVoiceTriggerManager10InitializeEvE3$_0NS_9allocatorIS3_EEFbjRKN15CAListenerProxy15HALNotificationEEEclEOjS9_
+ __ZNSt3__110__function6__funcIZN22MultiOutputHapticSynth12startRunningEbbjNS_8functionIFivEEEjE3$_0NS_9allocatorIS6_EES4_E18destroy_deallocateEv
+ __ZNSt3__110__function6__funcIZN22MultiOutputHapticSynth12startRunningEbbjNS_8functionIFivEEEjE3$_0NS_9allocatorIS6_EES4_E7destroyEv
+ __ZNSt3__110__function6__funcIZN22MultiOutputHapticSynth12startRunningEbbjNS_8functionIFivEEEjE3$_0NS_9allocatorIS6_EES4_ED0Ev
+ __ZNSt3__110__function6__funcIZN22MultiOutputHapticSynth12startRunningEbbjNS_8functionIFivEEEjE3$_0NS_9allocatorIS6_EES4_ED1Ev
+ __ZNSt3__110__function6__funcIZN22MultiOutputHapticSynth12startRunningEbbjNS_8functionIFivEEEjE3$_0NS_9allocatorIS6_EES4_EclEv
+ __ZNSt3__110__function6__funcIZN22MultiOutputHapticSynth19handleRunModeChangeEjE3$_0NS_9allocatorIS3_EEFivEE18destroy_deallocateEv
+ __ZNSt3__110__function6__funcIZN22MultiOutputHapticSynth19handleRunModeChangeEjE3$_0NS_9allocatorIS3_EEFivEE7destroyEv
+ __ZNSt3__110__function6__funcIZN22MultiOutputHapticSynth19handleRunModeChangeEjE3$_0NS_9allocatorIS3_EEFivEED0Ev
+ __ZNSt3__110__function6__funcIZN22MultiOutputHapticSynth19handleRunModeChangeEjE3$_0NS_9allocatorIS3_EEFivEED1Ev
+ __ZNSt3__110__function6__funcIZN22MultiOutputHapticSynth19handleRunModeChangeEjE3$_0NS_9allocatorIS3_EEFivEEclEv
+ __ZNSt3__110__function6__funcIZN24AVVoiceTriggerServerImpl27enableVoiceTriggerListeningEbbU13block_pointerFvP7NSErrorEEUljRKN15CAListenerProxy15HALNotificationEE_NS_9allocatorISB_EEFbjSA_EE18destroy_deallocateEv
+ __ZNSt3__110__function6__funcIZN24AVVoiceTriggerServerImpl27enableVoiceTriggerListeningEbbU13block_pointerFvP7NSErrorEEUljRKN15CAListenerProxy15HALNotificationEE_NS_9allocatorISB_EEFbjSA_EE7destroyEv
+ __ZNSt3__110__function6__funcIZN24AVVoiceTriggerServerImpl27enableVoiceTriggerListeningEbbU13block_pointerFvP7NSErrorEEUljRKN15CAListenerProxy15HALNotificationEE_NS_9allocatorISB_EEFbjSA_EED0Ev
+ __ZNSt3__110__function6__funcIZN24AVVoiceTriggerServerImpl27enableVoiceTriggerListeningEbbU13block_pointerFvP7NSErrorEEUljRKN15CAListenerProxy15HALNotificationEE_NS_9allocatorISB_EEFbjSA_EED1Ev
+ __ZNSt3__110__function6__funcIZN24AVVoiceTriggerServerImpl27enableVoiceTriggerListeningEbbU13block_pointerFvP7NSErrorEEUljRKN15CAListenerProxy15HALNotificationEE_NS_9allocatorISB_EEFbjSA_EEclEOjSA_
+ __ZNSt3__110__function6__funcIZN24AVVoiceTriggerServerImpl31updateVoiceTriggerConfigurationEPK14__CFDictionaryU13block_pointerFvP7NSErrorEEUljRKN15CAListenerProxy15HALNotificationEE_NS_9allocatorISE_EEFbjSD_EE18destroy_deallocateEv
+ __ZNSt3__110__function6__funcIZN24AVVoiceTriggerServerImpl31updateVoiceTriggerConfigurationEPK14__CFDictionaryU13block_pointerFvP7NSErrorEEUljRKN15CAListenerProxy15HALNotificationEE_NS_9allocatorISE_EEFbjSD_EE7destroyEv
+ __ZNSt3__110__function6__funcIZN24AVVoiceTriggerServerImpl31updateVoiceTriggerConfigurationEPK14__CFDictionaryU13block_pointerFvP7NSErrorEEUljRKN15CAListenerProxy15HALNotificationEE_NS_9allocatorISE_EEFbjSD_EED0Ev
+ __ZNSt3__110__function6__funcIZN24AVVoiceTriggerServerImpl31updateVoiceTriggerConfigurationEPK14__CFDictionaryU13block_pointerFvP7NSErrorEEUljRKN15CAListenerProxy15HALNotificationEE_NS_9allocatorISE_EEFbjSD_EED1Ev
+ __ZNSt3__110__function6__funcIZN24AVVoiceTriggerServerImpl31updateVoiceTriggerConfigurationEPK14__CFDictionaryU13block_pointerFvP7NSErrorEEUljRKN15CAListenerProxy15HALNotificationEE_NS_9allocatorISE_EEFbjSD_EEclEOjSD_
+ __ZNSt3__110__function6__funcIZN24AVVoiceTriggerServerImpl40registerStateChangedNotificationHandlersEbEUljRKN15CAListenerProxy15HALNotificationEE_NS_9allocatorIS7_EEFbjS6_EE18destroy_deallocateEv
+ __ZNSt3__110__function6__funcIZN24AVVoiceTriggerServerImpl40registerStateChangedNotificationHandlersEbEUljRKN15CAListenerProxy15HALNotificationEE_NS_9allocatorIS7_EEFbjS6_EE7destroyEv
+ __ZNSt3__110__function6__funcIZN24AVVoiceTriggerServerImpl40registerStateChangedNotificationHandlersEbEUljRKN15CAListenerProxy15HALNotificationEE_NS_9allocatorIS7_EEFbjS6_EED0Ev
+ __ZNSt3__110__function6__funcIZN24AVVoiceTriggerServerImpl40registerStateChangedNotificationHandlersEbEUljRKN15CAListenerProxy15HALNotificationEE_NS_9allocatorIS7_EEFbjS6_EED1Ev
+ __ZNSt3__110__function6__funcIZN24AVVoiceTriggerServerImpl40registerStateChangedNotificationHandlersEbEUljRKN15CAListenerProxy15HALNotificationEE_NS_9allocatorIS7_EEFbjS6_EEclEOjS6_
+ __ZNSt3__110__function6__funcIZN24AVVoiceTriggerServerImpl42registerAOPVoiceTriggerNotificationHandlerEjbEUljRKN15CAListenerProxy15HALNotificationEE_NS_9allocatorIS7_EEFbjS6_EE18destroy_deallocateEv
+ __ZNSt3__110__function6__funcIZN24AVVoiceTriggerServerImpl42registerAOPVoiceTriggerNotificationHandlerEjbEUljRKN15CAListenerProxy15HALNotificationEE_NS_9allocatorIS7_EEFbjS6_EE7destroyEv
+ __ZNSt3__110__function6__funcIZN24AVVoiceTriggerServerImpl42registerAOPVoiceTriggerNotificationHandlerEjbEUljRKN15CAListenerProxy15HALNotificationEE_NS_9allocatorIS7_EEFbjS6_EED0Ev
+ __ZNSt3__110__function6__funcIZN24AVVoiceTriggerServerImpl42registerAOPVoiceTriggerNotificationHandlerEjbEUljRKN15CAListenerProxy15HALNotificationEE_NS_9allocatorIS7_EEFbjS6_EED1Ev
+ __ZNSt3__110__function6__funcIZN24AVVoiceTriggerServerImpl42registerAOPVoiceTriggerNotificationHandlerEjbEUljRKN15CAListenerProxy15HALNotificationEE_NS_9allocatorIS7_EEFbjS6_EEclEOjS6_
+ __ZNSt3__110__function6__funcIZN24AVVoiceTriggerServerImpl43registerAOPEnableChangedNotificationHandlerEbEUljRKN15CAListenerProxy15HALNotificationEE_NS_9allocatorIS7_EEFbjS6_EE18destroy_deallocateEv
+ __ZNSt3__110__function6__funcIZN24AVVoiceTriggerServerImpl43registerAOPEnableChangedNotificationHandlerEbEUljRKN15CAListenerProxy15HALNotificationEE_NS_9allocatorIS7_EEFbjS6_EE7destroyEv
+ __ZNSt3__110__function6__funcIZN24AVVoiceTriggerServerImpl43registerAOPEnableChangedNotificationHandlerEbEUljRKN15CAListenerProxy15HALNotificationEE_NS_9allocatorIS7_EEFbjS6_EED0Ev
+ __ZNSt3__110__function6__funcIZN24AVVoiceTriggerServerImpl43registerAOPEnableChangedNotificationHandlerEbEUljRKN15CAListenerProxy15HALNotificationEE_NS_9allocatorIS7_EEFbjS6_EED1Ev
+ __ZNSt3__110__function6__funcIZN24AVVoiceTriggerServerImpl43registerAOPEnableChangedNotificationHandlerEbEUljRKN15CAListenerProxy15HALNotificationEE_NS_9allocatorIS7_EEFbjS6_EEclEOjS6_
+ __ZNSt3__110__function6__funcIZN2AQ3API7ManagerC1EbRNS3_11CaptureBaseEN5caulk19lifetime_erased_ptrI23AudioQueueXPC_InterfaceEEE3$_0NS_9allocatorISB_EEFvRN4swix12ipc_endpointERKN10applesauce3xpc6objectEEE18destroy_deallocateEv
+ __ZNSt3__110__function6__funcIZN2AQ3API7ManagerC1EbRNS3_11CaptureBaseEN5caulk19lifetime_erased_ptrI23AudioQueueXPC_InterfaceEEE3$_0NS_9allocatorISB_EEFvRN4swix12ipc_endpointERKN10applesauce3xpc6objectEEE7destroyEv
+ __ZNSt3__110__function6__funcIZN2AQ3API7ManagerC1EbRNS3_11CaptureBaseEN5caulk19lifetime_erased_ptrI23AudioQueueXPC_InterfaceEEE3$_0NS_9allocatorISB_EEFvRN4swix12ipc_endpointERKN10applesauce3xpc6objectEEED0Ev
+ __ZNSt3__110__function6__funcIZN2AQ3API7ManagerC1EbRNS3_11CaptureBaseEN5caulk19lifetime_erased_ptrI23AudioQueueXPC_InterfaceEEE3$_0NS_9allocatorISB_EEFvRN4swix12ipc_endpointERKN10applesauce3xpc6objectEEED1Ev
+ __ZNSt3__110__function6__funcIZN2AQ3API7ManagerC1EbRNS3_11CaptureBaseEN5caulk19lifetime_erased_ptrI23AudioQueueXPC_InterfaceEEE3$_0NS_9allocatorISB_EEFvRN4swix12ipc_endpointERKN10applesauce3xpc6objectEEEclESG_SL_
+ __ZNSt3__110__function6__funcIZN2AQ3API7ManagerC1EbRNS3_11CaptureBaseEN5caulk19lifetime_erased_ptrI23AudioQueueXPC_InterfaceEEE3$_1NS_9allocatorISB_EEFiN10applesauce3xpc6objectEEE18destroy_deallocateEv
+ __ZNSt3__110__function6__funcIZN2AQ3API7ManagerC1EbRNS3_11CaptureBaseEN5caulk19lifetime_erased_ptrI23AudioQueueXPC_InterfaceEEE3$_1NS_9allocatorISB_EEFiN10applesauce3xpc6objectEEE7destroyEv
+ __ZNSt3__110__function6__funcIZN2AQ3API7ManagerC1EbRNS3_11CaptureBaseEN5caulk19lifetime_erased_ptrI23AudioQueueXPC_InterfaceEEE3$_1NS_9allocatorISB_EEFiN10applesauce3xpc6objectEEED0Ev
+ __ZNSt3__110__function6__funcIZN2AQ3API7ManagerC1EbRNS3_11CaptureBaseEN5caulk19lifetime_erased_ptrI23AudioQueueXPC_InterfaceEEE3$_1NS_9allocatorISB_EEFiN10applesauce3xpc6objectEEED1Ev
+ __ZNSt3__110__function6__funcIZN2AQ3API7ManagerC1EbRNS3_11CaptureBaseEN5caulk19lifetime_erased_ptrI23AudioQueueXPC_InterfaceEEE3$_1NS_9allocatorISB_EEFiN10applesauce3xpc6objectEEEclEOSG_
+ __ZNSt3__110__function6__funcIZN2AT11Translation19AUAsyncRendererHost9ConfigureEvE3$_0NS_9allocatorIS5_EEFvNS_6chrono10time_pointINS8_12steady_clockENS8_8durationIxNS_5ratioILl1ELl1000000000EEEEEEERK15AudioBufferListiEE18destroy_deallocateEv
+ __ZNSt3__110__function6__funcIZN2AT11Translation19AUAsyncRendererHost9ConfigureEvE3$_0NS_9allocatorIS5_EEFvNS_6chrono10time_pointINS8_12steady_clockENS8_8durationIxNS_5ratioILl1ELl1000000000EEEEEEERK15AudioBufferListiEE7destroyEv
+ __ZNSt3__110__function6__funcIZN2AT11Translation19AUAsyncRendererHost9ConfigureEvE3$_0NS_9allocatorIS5_EEFvNS_6chrono10time_pointINS8_12steady_clockENS8_8durationIxNS_5ratioILl1ELl1000000000EEEEEEERK15AudioBufferListiEED0Ev
+ __ZNSt3__110__function6__funcIZN2AT11Translation19AUAsyncRendererHost9ConfigureEvE3$_0NS_9allocatorIS5_EEFvNS_6chrono10time_pointINS8_12steady_clockENS8_8durationIxNS_5ratioILl1ELl1000000000EEEEEEERK15AudioBufferListiEED1Ev
+ __ZNSt3__110__function6__funcIZN2AT11Translation19AUAsyncRendererHost9ConfigureEvE3$_0NS_9allocatorIS5_EEFvNS_6chrono10time_pointINS8_12steady_clockENS8_8durationIxNS_5ratioILl1ELl1000000000EEEEEEERK15AudioBufferListiEEclEOSF_SI_Oi
+ __ZNSt3__110__function6__funcIZN30AudioSessionPropertyMarshaller15GetPropertyInfoEjE5$_127NS_9allocatorIS3_EEFP10MarshallervEE18destroy_deallocateEv
+ __ZNSt3__110__function6__funcIZN30AudioSessionPropertyMarshaller15GetPropertyInfoEjE5$_127NS_9allocatorIS3_EEFP10MarshallervEE7destroyEv
+ __ZNSt3__110__function6__funcIZN30AudioSessionPropertyMarshaller15GetPropertyInfoEjE5$_127NS_9allocatorIS3_EEFP10MarshallervEED0Ev
+ __ZNSt3__110__function6__funcIZN30AudioSessionPropertyMarshaller15GetPropertyInfoEjE5$_127NS_9allocatorIS3_EEFP10MarshallervEED1Ev
+ __ZNSt3__110__function6__funcIZN30AudioSessionPropertyMarshaller15GetPropertyInfoEjE5$_127NS_9allocatorIS3_EEFP10MarshallervEEclEv
+ __ZNSt3__110__function6__funcIZZN13MESubmixGraph19attach1MixerChannelEP14MEMixerChannelENK3$_1clI9TapSubmixEEDaRT_EUlvE_NS_9allocatorISB_EEFvvEE18destroy_deallocateEv
+ __ZNSt3__110__function6__funcIZZN13MESubmixGraph19attach1MixerChannelEP14MEMixerChannelENK3$_1clI9TapSubmixEEDaRT_EUlvE_NS_9allocatorISB_EEFvvEE7destroyEv
+ __ZNSt3__110__function6__funcIZZN13MESubmixGraph19attach1MixerChannelEP14MEMixerChannelENK3$_1clI9TapSubmixEEDaRT_EUlvE_NS_9allocatorISB_EEFvvEED0Ev
+ __ZNSt3__110__function6__funcIZZN13MESubmixGraph19attach1MixerChannelEP14MEMixerChannelENK3$_1clI9TapSubmixEEDaRT_EUlvE_NS_9allocatorISB_EEFvvEED1Ev
+ __ZNSt3__110__function6__funcIZZN13MESubmixGraph19attach1MixerChannelEP14MEMixerChannelENK3$_1clI9TapSubmixEEDaRT_EUlvE_NS_9allocatorISB_EEFvvEEclEv
+ __ZNSt3__110__function6__funcIZZN14RemoteIOClient20IONode_FormatChangedEjEUb_E3$_1NS_9allocatorIS3_EEFvvEE18destroy_deallocateEv
+ __ZNSt3__110__function6__funcIZZN14RemoteIOClient20IONode_FormatChangedEjEUb_E3$_1NS_9allocatorIS3_EEFvvEE7destroyEv
+ __ZNSt3__110__function6__funcIZZN14RemoteIOClient20IONode_FormatChangedEjEUb_E3$_1NS_9allocatorIS3_EEFvvEED0Ev
+ __ZNSt3__110__function6__funcIZZN14RemoteIOClient20IONode_FormatChangedEjEUb_E3$_1NS_9allocatorIS3_EEFvvEED1Ev
+ __ZNSt3__110__function6__funcIZZN14RemoteIOClient20IONode_FormatChangedEjEUb_E3$_1NS_9allocatorIS3_EEFvvEEclEv
+ __ZNSt3__110__function6__funcIZZN22MultiOutputHapticSynth11stopRunningEbbjENK3$_0clERNS_10unique_ptrI11SynthOutputNS_14default_deleteIS5_EEEEEUlvE_NS_9allocatorISA_EEFvvEE18destroy_deallocateEv
+ __ZNSt3__110__function6__funcIZZN22MultiOutputHapticSynth11stopRunningEbbjENK3$_0clERNS_10unique_ptrI11SynthOutputNS_14default_deleteIS5_EEEEEUlvE_NS_9allocatorISA_EEFvvEE7destroyEv
+ __ZNSt3__110__function6__funcIZZN22MultiOutputHapticSynth11stopRunningEbbjENK3$_0clERNS_10unique_ptrI11SynthOutputNS_14default_deleteIS5_EEEEEUlvE_NS_9allocatorISA_EEFvvEED0Ev
+ __ZNSt3__110__function6__funcIZZN22MultiOutputHapticSynth11stopRunningEbbjENK3$_0clERNS_10unique_ptrI11SynthOutputNS_14default_deleteIS5_EEEEEUlvE_NS_9allocatorISA_EEFvvEED1Ev
+ __ZNSt3__110__function6__funcIZZN22MultiOutputHapticSynth11stopRunningEbbjENK3$_0clERNS_10unique_ptrI11SynthOutputNS_14default_deleteIS5_EEEEEUlvE_NS_9allocatorISA_EEFvvEEclEv
+ __ZNSt3__110__list_impI15SystemSoundInfoNS_9allocatorIS1_EEE13__create_nodeB8ne200100IJRKS1_EEEPNS_11__list_nodeIS1_PvEEPNS_16__list_node_baseIS1_S9_EESE_DpOT_
+ __ZNSt3__110__list_impIN13ServerManager12SynthCommandEN5caulk12rt_allocatorIS2_EEE13__create_nodeB8ne200100IJRKS2_EEEPNS_11__list_nodeIS2_PvEEPNS_16__list_node_baseIS2_SB_EESG_DpOT_
+ __ZNSt3__110shared_ptrI11AQTapIONodeEC2B8ne200100IS1_PFvP8AQIONodeELi0EEEPT_T0_
+ __ZNSt3__110shared_ptrI11ClientEntryEC2B8ne200100IS1_Li0EEERKNS_8weak_ptrIT_EE
+ __ZNSt3__110shared_ptrI12SequenceImplEC2B8ne200100IS1_Li0EEERKNS_8weak_ptrIT_EE
+ __ZNSt3__110shared_ptrI14HapticSequenceEC2B8ne200100IS1_Li0EEEPT_
+ __ZNSt3__110shared_ptrI18AQMixEngine_SingleEC2B8ne200100IS1_PFvP8AQIONodeELi0EEEPT_T0_
+ __ZNSt3__110shared_ptrI19AQMixEngine_OfflineEC2B8ne200100IS1_PFvP8AQIONodeELi0EEEPT_T0_
+ __ZNSt3__110shared_ptrI21ThreadSafeHeadTrackerE18__enable_weak_thisB8ne200100IS1_S1_Li0EEEvPKNS_23enable_shared_from_thisIT_EEPT0_
+ __ZNSt3__110shared_ptrIN18PowerUsageWatchdog4ImplEEC2B8ne200100IS2_Li0EEERKNS_8weak_ptrIT_EE
+ __ZNSt3__110shared_ptrIN2AQ3API5QueueEEC2B8ne200100IS3_Li0EEERKNS_8weak_ptrIT_EE
+ __ZNSt3__110shared_ptrIN2AQ3API9SubmixTapEEC2B8ne200100IS3_Li0EEERKNS_8weak_ptrIT_EE
+ __ZNSt3__110shared_ptrIN2AT9IOBinding4ImplEE18__enable_weak_thisB8ne200100IS3_S3_Li0EEEvPKNS_23enable_shared_from_thisIT_EEPT0_
+ __ZNSt3__110unique_ptrI10AQMEIO_DSPNS_14default_deleteIS1_EEE5resetB8ne200100EPS1_
+ __ZNSt3__110unique_ptrI11AQAC3IONodeNS_14default_deleteIS1_EEED1B8ne200100Ev
+ __ZNSt3__110unique_ptrI11AQTapIONodeNS_14default_deleteIS1_EEE5resetB8ne200100EPS1_
+ __ZNSt3__110unique_ptrI11AQTapIONodeNS_14default_deleteIS1_EEED1B8ne200100Ev
+ __ZNSt3__110unique_ptrI11SynthOutputNS_14default_deleteIS1_EEE5resetB8ne200100EPS1_
+ __ZNSt3__110unique_ptrI11SynthOutputNS_14default_deleteIS1_EEED1B8ne200100Ev
+ __ZNSt3__110unique_ptrI12CASerializerNS_14default_deleteIS1_EEE5resetB8ne200100EPS1_
+ __ZNSt3__110unique_ptrI14AQClientBufferN2AQ3API13BufferDeleterEE5resetB8ne200100EPS1_
+ __ZNSt3__110unique_ptrI14CADeserializerNS_14default_deleteIS1_EEE5resetB8ne200100EPS1_
+ __ZNSt3__110unique_ptrI14CAMemoryStreamNS_14default_deleteIS1_EEE5resetB8ne200100EPS1_
+ __ZNSt3__110unique_ptrI14InputConverterNS_14default_deleteIS1_EEE5resetB8ne200100EPS1_
+ __ZNSt3__110unique_ptrI14MixTapToUplinkNS_14default_deleteIS1_EEE5resetB8ne200100EPS1_
+ __ZNSt3__110unique_ptrI14__CFReadStreamN10applesauce4raii2v16detail23opaque_deletion_functorIPS1_XadL_Z9CFReleaseEEEEE5resetB8ne200100ES7_
+ __ZNSt3__110unique_ptrI15AQMixEngine_VADNS_14default_deleteIS1_EEED1B8ne200100Ev
+ __ZNSt3__110unique_ptrI16SSSVibrationDataNS_14default_deleteIS1_EEE5resetB8ne200100EPS1_
+ __ZNSt3__110unique_ptrI16SSSVibrationDataNS_14default_deleteIS1_EEED1B8ne200100Ev
+ __ZNSt3__110unique_ptrI17AudioEventManagerNS_14default_deleteIS1_EEED1B8ne200100Ev
+ __ZNSt3__110unique_ptrI17AudioTapInterfaceNS_14default_deleteIS1_EEE5resetB8ne200100EPS1_
+ __ZNSt3__110unique_ptrI17AudioTapSpecifierNS_14default_deleteIS1_EEE5resetB8ne200100EPS1_
+ __ZNSt3__110unique_ptrI17ZenAQIONodeClientNS_14default_deleteIS1_EEE5resetB8ne200100EPS1_
+ __ZNSt3__110unique_ptrI18AQHapticOutputNodeNS_14default_deleteIS1_EEED1B8ne200100Ev
+ __ZNSt3__110unique_ptrI18AudioRingAllocatorNS_14default_deleteIS1_EEE5resetB8ne200100EPS1_
+ __ZNSt3__110unique_ptrI18VADPropertyManagerNS_14default_deleteIS1_EEED1B8ne200100Ev
+ __ZNSt3__110unique_ptrI19AQMixEngine_OfflineNS_14default_deleteIS1_EEED1B8ne200100Ev
+ __ZNSt3__110unique_ptrI19MESchedulingVectorsNS_14default_deleteIS1_EEE5resetB8ne200100EPS1_
+ __ZNSt3__110unique_ptrI20AudioImpulseInjectorNS_14default_deleteIS1_EEE5resetB8ne200100EPS1_
+ __ZNSt3__110unique_ptrI26SSClientCompletionProcInfoNS_14default_deleteIS1_EEED1B8ne200100Ev
+ __ZNSt3__110unique_ptrI27SpatialTrackingServiceProxyNS_14default_deleteIS1_EEE5resetB8ne200100EPS1_
+ __ZNSt3__110unique_ptrI28OpaqueAudioComponentInstanceN10applesauce4raii2v16detail23opaque_deletion_functorIPS1_XadL_Z29AudioComponentInstanceDisposeEEEEE5resetB8ne200100ES7_
+ __ZNSt3__110unique_ptrI30ProductTuningAdjustmentManagerNS_14default_deleteIS1_EEED1B8ne200100Ev
+ __ZNSt3__110unique_ptrI7__sFILENS_8functionIFiPS1_EEEE5resetB8ne200100ES3_
+ __ZNSt3__110unique_ptrI8XPromiseNS_14default_deleteIS1_EEE5resetB8ne200100EPS1_
+ __ZNSt3__110unique_ptrIKvN10applesauce4raii2v16detail23opaque_deletion_functorIPS1_XadL_Z9CFReleaseEEEEE5resetB8ne200100ES7_
+ __ZNSt3__110unique_ptrIN11AQMEIO_Base12IOSuspensionENS_14default_deleteIS2_EEE5resetB8ne200100EPS2_
+ __ZNSt3__110unique_ptrIN11HeadTracker18HeadTrackerSessionENS_14default_deleteIS2_EEED1B8ne200100Ev
+ __ZNSt3__110unique_ptrIN14MixTapToUplink16AQMETapConnectorENS_14default_deleteIS2_EEED1B8ne200100Ev
+ __ZNSt3__110unique_ptrIN14MixTapToUplink27UplinkSpeechMixerCPPWrapperENS_14default_deleteIS2_EEE5resetB8ne200100EPS2_
+ __ZNSt3__110unique_ptrIN14MixTapToUplink28AQIONodeClientForInternalTapENS_14default_deleteIS2_EEE5resetB8ne200100EPS2_
+ __ZNSt3__110unique_ptrIN14MixTapToUplink41RAIIUnregisterMutedSpeechActivityListenerENS_14default_deleteIS2_EEE5resetB8ne200100EPS2_
+ __ZNSt3__110unique_ptrIN14SpeechDetector18SpeechDetectorImplENS_14default_deleteIS2_EEE5resetB8ne200100EPS2_
+ __ZNSt3__110unique_ptrIN17AudioTapInterface4ImplENS_14default_deleteIS2_EEE5resetB8ne200100EPS2_
+ __ZNSt3__110unique_ptrIN18ATSecureVADManager4ImplENS_14default_deleteIS2_EEE5resetB8ne200100EPS2_
+ __ZNSt3__110unique_ptrIN18MixTapToUplinkHost46MixTapToUplinkGroupedByMicrophoneInjectionModeENS_14default_deleteIS2_EEED1B8ne200100Ev
+ __ZNSt3__110unique_ptrIN18PowerUsageWatchdog23AudioSessionDescriptionENS_14default_deleteIS2_EEE5resetB8ne200100EPS2_
+ __ZNSt3__110unique_ptrIN18PowerUsageWatchdog4ImplENS_14default_deleteIS2_EEED1B8ne200100Ev
+ __ZNSt3__110unique_ptrIN2AQ6Server12RemoteClientENS_14default_deleteIS3_EEE5resetB8ne200100EPS3_
+ __ZNSt3__110unique_ptrIN2AT11Translation14CallTranslatorENS_14default_deleteIS3_EEED1B8ne200100Ev
+ __ZNSt3__110unique_ptrIN2AT11Translation19AUAsyncRendererHostENS_14default_deleteIS3_EEED1B8ne200100Ev
+ __ZNSt3__110unique_ptrIN2AT11Translation24AudioTranslationInjectorENS_14default_deleteIS3_EEE5resetB8ne200100EPS3_
+ __ZNSt3__110unique_ptrIN2AT11Translation25BlurringMixerDSPGraphHost20ATBlurMixerInterfaceENS_14default_deleteIS4_EEE5resetB8ne200100EPS4_
+ __ZNSt3__110unique_ptrIN2AT11Translation25BlurringMixerDSPGraphHostENS_14default_deleteIS3_EEED1B8ne200100Ev
+ __ZNSt3__110unique_ptrIN2AT11Translation27TranslationFeedbackInjectorENS_14default_deleteIS3_EEE5resetB8ne200100EPS3_
+ __ZNSt3__110unique_ptrIN2AT14AudioTapClient4ImplENS_14default_deleteIS3_EEE5resetB8ne200100EPS3_
+ __ZNSt3__110unique_ptrIN2CA16AudioBuffersBaseENS_14default_deleteIS2_EEE5resetB8ne200100EPS2_
+ __ZNSt3__110unique_ptrIN2CA22AudioBuffersDeprecatedENS_14default_deleteIS2_EEE5resetB8ne200100EPS2_
+ __ZNSt3__110unique_ptrIN5Phase13ServerManagerENS_14default_deleteIS2_EEE5resetB8ne200100EPS2_
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeI27AVHapticPlayerParameterTypeN20HapticEventConverter23CurveConsolidationStateEEEPvEENS_22__hash_node_destructorINS_9allocatorIS8_EEEEED1B8ne200100Ev
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEN20AudioImpulseInjector4Impl20NotificationListener17NotificationStateEEEPvEENS_22__hash_node_destructorINS6_ISF_EEEEED1B8ne200100Ev
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIPK15AudioBufferListNS_4pairINS_6chrono10time_pointINS7_12steady_clockENS7_8durationIxNS_5ratioILl1ELl1000000000EEEEEEEU8__strongP16AVAudioPCMBufferEEEEPvEENS_22__hash_node_destructorINS_9allocatorISL_EEEEED1B8ne200100Ev
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIjNS0_I26SSClientCompletionProcInfoNS_14default_deleteIS3_EEEEEEPvEENS_22__hash_node_destructorINS_9allocatorIS9_EEEEED1B8ne200100Ev
+ __ZNSt3__110unique_ptrINS_11__tree_nodeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE8LocalityEEPvEENS_22__tree_node_destructorINS6_ISC_EEEEED1B8ne200100Ev
+ __ZNSt3__110unique_ptrINS_11__tree_nodeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI29NewNotificationCenterObserverEEEEPvEENS_22__tree_node_destructorINS6_ISE_EEEEED1B8ne200100Ev
+ __ZNSt3__110unique_ptrINS_11__tree_nodeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI29OldNotificationCenterObserverEEEEPvEENS_22__tree_node_destructorINS6_ISE_EEEEED1B8ne200100Ev
+ __ZNSt3__110unique_ptrINS_11__tree_nodeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEES8_EEPvEENS_22__tree_node_destructorINS6_ISB_EEEEED1B8ne200100Ev
+ __ZNSt3__110unique_ptrINS_5tupleIJN5caulk6thread10attributesEZN2AQ3API20ProcessingTapManager7RTStateC1ERKN10applesauce3xpc6objectERNS6_23ProcessingTapAttributesERiE3$_0NS1_IJEEEEEENS_14default_deleteISJ_EEED1B8ne200100Ev
+ __ZNSt3__110unique_ptrIZN20CAOrientationManager14UpdateHandlersENS1_11HandlerTypeEE3$_0NS_14default_deleteIS3_EEED1B8ne200100Ev
+ __ZNSt3__110unique_ptrIZN20CAOrientationManager23AddUIOrientationHandlerEPK10__CFStringU13block_pointerFv13CAOrientationEE3$_0NS_14default_deleteIS8_EEED1B8ne200100Ev
+ __ZNSt3__110unique_ptrIZN20CAOrientationManager27AddDeviceOrientationHandlerEPK10__CFStringU13block_pointerFv13CAOrientationEE3$_0NS_14default_deleteIS8_EEED1B8ne200100Ev
+ __ZNSt3__111__introsortINS_17_ClassicAlgPolicyERZN17AudioTapSpecifierC1ENS_6vectorIjNS_9allocatorIjEEEE22ATAudioTapMuteBehaviorEUlRK11AQMESessionSA_E_PS8_Lb0EEEvT1_SE_T0_NS_15iterator_traitsISE_E15difference_typeEb
+ __ZNSt3__111__introsortINS_17_ClassicAlgPolicyERZZZN2AT11Translation19AUAsyncRendererHost9ConfigureEvENK3$_0clENS_6chrono10time_pointINS6_12steady_clockENS6_8durationIxNS_5ratioILl1ELl1000000000EEEEEEERK15AudioBufferListiENKUlRT_E_clINS_6vectorINS4_34TemporallyOrdereredAudioBufferListENS_9allocatorISM_EEEEEEDaSI_EUlRKSM_SS_E_PSM_Lb0EEEvT1_SW_T0_NS_15iterator_traitsISW_E15difference_typeEb
+ __ZNSt3__111make_uniqueB8ne200100I17AudioTapInterfaceJ17AudioTapSpecifierELi0EEENS_10unique_ptrIT_NS_14default_deleteIS4_EEEEDpOT0_
+ __ZNSt3__111make_uniqueB8ne200100I17AudioTapInterfaceJPK8__CFDataELi0EEENS_10unique_ptrIT_NS_14default_deleteIS6_EEEEDpOT0_
+ __ZNSt3__111make_uniqueB8ne200100IN2CA22AudioBuffersDeprecatedEJRNS1_17StreamDescriptionERjELi0EEENS_10unique_ptrIT_NS_14default_deleteIS7_EEEEDpOT0_
+ __ZNSt3__111shared_lockIN5caulk10concurrent16shared_spin_lockEED2B8ne200100Ev
+ __ZNSt3__111shared_lockINS_12shared_mutexEED2B8ne200100Ev
+ __ZNSt3__111unique_lockIN5caulk10concurrent16shared_spin_lockEED2B8ne200100Ev
+ __ZNSt3__111unique_lockIN5caulk4mach21unfair_recursive_lockEE4lockB8ne200100Ev
+ __ZNSt3__111unique_lockIN5caulk4mach21unfair_recursive_lockEE6unlockB8ne200100Ev
+ __ZNSt3__111unique_lockINS_12shared_mutexEED2B8ne200100Ev
+ __ZNSt3__112__destroy_atB8ne200100I15MEVADIdentifierLi0EEEvPT_
+ __ZNSt3__112__destroy_atB8ne200100IN10applesauce2CF7TypeRefELi0EEEvPT_
+ __ZNSt3__112__destroy_atB8ne200100IN10applesauce2CF9NumberRefELi0EEEvPT_
+ __ZNSt3__112__destroy_atB8ne200100IN2AQ6Server12RemoteClient18ProcessingTapStateELi0EEEvPT_
+ __ZNSt3__112__destroy_atB8ne200100IN2AU8Property10Attributes7details15AUPresetWrapperELi0EEEvPT_
+ __ZNSt3__112__destroy_atB8ne200100IN8audioipc18SharedAudioBuffers7ElementELi0EEEvPT_
+ __ZNSt3__112__destroy_atB8ne200100INS_4pairIKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE8LocalityEELi0EEEvPT_
+ __ZNSt3__112__destroy_atB8ne200100INS_4pairIKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI29NewNotificationCenterObserverEEEELi0EEEvPT_
+ __ZNSt3__112__destroy_atB8ne200100INS_4pairIKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI29OldNotificationCenterObserverEEEELi0EEEvPT_
+ __ZNSt3__112__destroy_atB8ne200100INS_4pairIKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEES7_EELi0EEEvPT_
+ __ZNSt3__112__destroy_atB8ne200100INS_4pairIKP14MEMixerChannelN9TapSubmix10InputStateEEELi0EEEvPT_
+ __ZNSt3__112__destroy_atB8ne200100INS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEES7_EELi0EEEvPT_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeI27AVHapticPlayerParameterTypeN20HapticEventConverter23CurveConsolidationStateEEENS_22__unordered_map_hasherIS2_S5_NS_4hashIS2_EENS_8equal_toIS2_EELb1EEENS_21__unordered_map_equalIS2_S5_SA_S8_Lb1EEENS_9allocatorIS5_EEED2Ev
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIPK15AudioBufferListNS_4pairINS_6chrono10time_pointINS6_12steady_clockENS6_8durationIxNS_5ratioILl1ELl1000000000EEEEEEEU8__strongP16AVAudioPCMBufferEEEENS_22__unordered_map_hasherIS4_SI_NS_4hashIS4_EENS_8equal_toIS4_EELb1EEENS_21__unordered_map_equalIS4_SI_SN_SL_Lb1EEENS_9allocatorISI_EEE8__rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIPK15AudioBufferListNS_4pairINS_6chrono10time_pointINS6_12steady_clockENS6_8durationIxNS_5ratioILl1ELl1000000000EEEEEEEU8__strongP16AVAudioPCMBufferEEEENS_22__unordered_map_hasherIS4_SI_NS_4hashIS4_EENS_8equal_toIS4_EELb1EEENS_21__unordered_map_equalIS4_SI_SN_SL_Lb1EEENS_9allocatorISI_EEED2Ev
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIijEENS_22__unordered_map_hasherIiS2_NS_4hashIiEENS_8equal_toIiEELb1EEENS_21__unordered_map_equalIiS2_S7_S5_Lb1EEENS_9allocatorIS2_EEE15__emplace_multiIJNS_4pairIijEEEEENS_15__hash_iteratorIPNS_11__hash_nodeIS2_PvEEEEDpOT_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIijEENS_22__unordered_map_hasherIiS2_NS_4hashIiEENS_8equal_toIiEELb1EEENS_21__unordered_map_equalIiS2_S7_S5_Lb1EEENS_9allocatorIS2_EEE19__equal_range_multiIiEENS_4pairINS_15__hash_iteratorIPNS_11__hash_nodeIS2_PvEEEESL_EERKT_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIijEENS_22__unordered_map_hasherIiS2_NS_4hashIiEENS_8equal_toIiEELb1EEENS_21__unordered_map_equalIiS2_S7_S5_Lb1EEENS_9allocatorIS2_EEED2Ev
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIjP24OpaqueMusicEventIteratorEENS_22__unordered_map_hasherIjS4_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS4_S9_S7_Lb1EEENS_9allocatorIS4_EEED2Ev
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIjiEENS_22__unordered_map_hasherIjS2_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS2_S7_S5_Lb1EEENS_9allocatorIS2_EEE25__emplace_unique_key_argsIjJRKNS_21piecewise_construct_tENS_5tupleIJRKjEEENSI_IJEEEEEENS_4pairINS_15__hash_iteratorIPNS_11__hash_nodeIS2_PvEEEEbEERKT_DpOT0_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeImNS_8optionalI28AUVoiceIOSpeechActivityEventEEEENS_22__unordered_map_hasherImS5_NS_4hashImEENS_8equal_toImEELb1EEENS_21__unordered_map_equalImS5_SA_S8_Lb1EEENS_9allocatorIS5_EEE4findImEENS_15__hash_iteratorIPNS_11__hash_nodeIS5_PvEEEERKT_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeImU13block_pointerFv28AUVoiceIOSpeechActivityEventEEENS_22__unordered_map_hasherImS5_NS_4hashImEENS_8equal_toImEELb1EEENS_21__unordered_map_equalImS5_SA_S8_Lb1EEENS_9allocatorIS5_EEE25__emplace_unique_key_argsImJRKNS_21piecewise_construct_tENS_5tupleIJRKmEEENSL_IJEEEEEENS_4pairINS_15__hash_iteratorIPNS_11__hash_nodeIS5_PvEEEEbEERKT_DpOT0_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeImU13block_pointerFv28AUVoiceIOSpeechActivityEventEEENS_22__unordered_map_hasherImS5_NS_4hashImEENS_8equal_toImEELb1EEENS_21__unordered_map_equalImS5_SA_S8_Lb1EEENS_9allocatorIS5_EEE4findImEENS_15__hash_iteratorIPNS_11__hash_nodeIS5_PvEEEERKT_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeImbEENS_22__unordered_map_hasherImS2_NS_4hashImEENS_8equal_toImEELb1EEENS_21__unordered_map_equalImS2_S7_S5_Lb1EEEN5caulk12rt_allocatorIS2_EEE17__deallocate_nodeEPNS_16__hash_node_baseIPNS_11__hash_nodeIS2_PvEEEE
+ __ZNSt3__112__hash_tableIjNS_4hashIjEENS_8equal_toIjEENS_9allocatorIjEEE8__rehashILb1EEEvm
+ __ZNSt3__112__tuple_leafILm0EN10applesauce3xpc6objectELb0EEC2B8ne200100ERKS4_
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_out_of_rangeB8ne200100Ev
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6__initEPKcm
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B8ne200100EPKcm
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B8ne200100Emc
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B8ne200100ILi0EEEPKc
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne200100ENS_24__uninitialized_size_tagEmRKS4_
+ __ZNSt3__112construct_atB8ne200100I11AQMESessionJS1_EPS1_EEPT_S4_DpOT0_
+ __ZNSt3__112construct_atB8ne200100I15MEVADIdentifierJR14MEDeviceTypeIDRjRN10applesauce2CF9StringRefEEPS1_EEPT_SB_DpOT0_
+ __ZNSt3__112construct_atB8ne200100I15MEVADIdentifierJRS1_EPS1_EEPT_S5_DpOT0_
+ __ZNSt3__112construct_atB8ne200100IN10applesauce2CF9StringRefEJRKS3_EPS3_EEPT_S8_DpOT0_
+ __ZNSt3__112future_errorC1ENS_10error_codeE
+ __ZNSt3__112future_errorD1Ev
+ __ZNSt3__113__assoc_stateIU8__strongP13AVAudioFormatE16__on_zero_sharedEv
+ __ZNSt3__113__assoc_stateIU8__strongP13AVAudioFormatED0Ev
+ __ZNSt3__113__assoc_stateIU8__strongP13AVAudioFormatED1Ev
+ __ZNSt3__113__fill_n_boolB8ne200100ILb0ENS_8__bitsetILm1ELm13EEEEEvNS_14__bit_iteratorIT0_Lb0EXLi0EEEENS_29__size_difference_type_traitsIS4_vE9size_typeE
+ __ZNSt3__113__tree_removeB8ne200100IPNS_16__tree_node_baseIPvEEEEvT_S5_
+ __ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEElsEPKv
+ __ZNSt3__113unordered_setIjNS_4hashIjEENS_8equal_toIjEENS_9allocatorIjEEEC2ERKS7_
+ __ZNSt3__114__shared_countD2Ev
+ __ZNSt3__114__split_bufferI10ChaseEventRN5caulk12rt_allocatorIS1_EEED2Ev
+ __ZNSt3__114__split_bufferI11VolumeEventRN5caulk12rt_allocatorIS1_EEED2Ev
+ __ZNSt3__114__split_bufferI23AudioUnitParameterEventRN5caulk12rt_allocatorIS1_EEED2Ev
+ __ZNSt3__114__split_bufferINS_10unique_ptrI11IAQMEDeviceNS_14default_deleteIS2_EEEERNS_9allocatorIS5_EEED2Ev
+ __ZNSt3__114__split_bufferINS_4pairIffEERN5caulk12rt_allocatorIS2_EEED2Ev
+ __ZNSt3__114__split_bufferIPN5boost8functionIFNS1_3msm4back11HandledEnumEvEEENS_9allocatorIS8_EEE12emplace_backIJRS8_EEEvDpOT_
+ __ZNSt3__114__split_bufferIPNS_4pairIN5boost8functionIFNS2_3msm4back11HandledEnumEvEEEbEENS_9allocatorISA_EEE12emplace_backIJRSA_EEEvDpOT_
+ __ZNSt3__114__split_bufferIPjNS_9allocatorIS1_EEE12emplace_backIJRS1_EEEvDpOT_
+ __ZNSt3__114__split_bufferIPmNS_9allocatorIS1_EEE12emplace_backIJRS1_EEEvDpOT_
+ __ZNSt3__115allocate_sharedB8ne200100I14HapticSequenceNS_9allocatorIS1_EEJNS_10shared_ptrI11MuteManagerEEELi0EEENS4_IT_EERKT0_DpOT1_
+ __ZNSt3__115allocate_sharedB8ne200100I19SSClientPlayOptionsNS_9allocatorIS1_EEJRN10applesauce3xpc6objectEELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
+ __ZNSt3__115allocate_sharedB8ne200100I8TFileBSDNS_9allocatorIS1_EEJRPK7__CFURLELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
+ __ZNSt3__115allocate_sharedB8ne200100IN2AQ3API9SubmixTapENS_9allocatorIS3_EEJRNS2_7ManagerERjELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
+ __ZNSt3__115allocate_sharedB8ne200100IN2AT9IOBinding4ImplENS_9allocatorIS3_EEJN10applesauce2CF9StringRefEELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
+ __ZNSt3__115allocate_sharedB8ne200100IN2AT9IOBinding4ImplENS_9allocatorIS3_EEJR24ATIsolatedAudioUseCaseIDELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
+ __ZNSt3__115allocate_sharedB8ne200100IN5caulk7details19lifetime_guard_baseIN2AQ6Server12RemoteClientEE13control_blockENS_9allocatorIS8_EEJRS7_ELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
+ __ZNSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne200100Ej
+ __ZNSt3__115future_categoryEv
+ __ZNSt3__116__deque_iteratorINS_4pairIN5boost8functionIFNS2_3msm4back11HandledEnumEvEEEbEEPS9_RS9_PSA_lLl102EEpLB8ne200100El
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm0EEE10__dispatchB8ne200100IOZNS0_6__ctorINS0_8__traitsIJPFvPvP16OpaqueAudioQueueP16AudioQueueBufferEPFvS8_SA_SC_PK14AudioTimeStampjPK28AudioStreamPacketDescriptionEN10applesauce8dispatch2v15blockIFvSA_SC_EEENSQ_IFvSA_SC_SH_jSK_EEEEEEE19__generic_constructB8ne200100IRKNS0_18__copy_constructorISV_LNS0_6_TraitE1EEEEEvRSW_OT_EUlS15_E_JRKNS0_6__baseILSZ_1EJSE_SM_SS_SU_EEEEEEDcS14_DpT0_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm0EEE10__dispatchB8ne200100IOZNS0_6__dtorINS0_8__traitsIJNS_9monostateEN15AQProcessingTap10DirectImplEEEELNS0_6_TraitE1EE9__destroyB8ne200100EvEUlRT_E_JRNS0_6__baseILSC_1EJS8_SA_EEEEEEDcSE_DpT0_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm0EEE10__dispatchB8ne200100IOZNS0_6__dtorINS0_8__traitsIJNS_9monostateEN2AQ6Server11XPCListenerENSA_9IPCBypassEEEELNS0_6_TraitE1EE9__destroyB8ne200100EvEUlRT_E_JRNS0_6__baseILSE_1EJS8_SB_SC_EEEEEEDcSG_DpT0_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm0EEE10__dispatchB8ne200100IOZNS0_6__dtorINS0_8__traitsIJNS_9monostateEN2AT13SessionFacade7ManagerENSA_11ManagerBaseEEEELNS0_6_TraitE1EE9__destroyB8ne200100EvEUlRT_E_JRNS0_6__baseILSE_1EJS8_SB_SC_EEEEEEDcSG_DpT0_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm0EEE10__dispatchB8ne200100IOZNS0_6__dtorINS0_8__traitsIJPFvPvP16OpaqueAudioQueueP16AudioQueueBufferEPFvS8_SA_SC_PK14AudioTimeStampjPK28AudioStreamPacketDescriptionEN10applesauce8dispatch2v15blockIFvSA_SC_EEENSQ_IFvSA_SC_SH_jSK_EEEEEELNS0_6_TraitE1EE9__destroyB8ne200100EvEUlRT_E_JRNS0_6__baseILSW_1EJSE_SM_SS_SU_EEEEEEDcSY_DpT0_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm1EEE10__dispatchB8ne200100IOZNS0_6__ctorINS0_8__traitsIJPFvPvP16OpaqueAudioQueueP16AudioQueueBufferEPFvS8_SA_SC_PK14AudioTimeStampjPK28AudioStreamPacketDescriptionEN10applesauce8dispatch2v15blockIFvSA_SC_EEENSQ_IFvSA_SC_SH_jSK_EEEEEEE19__generic_constructB8ne200100IRKNS0_18__copy_constructorISV_LNS0_6_TraitE1EEEEEvRSW_OT_EUlS15_E_JRKNS0_6__baseILSZ_1EJSE_SM_SS_SU_EEEEEEDcS14_DpT0_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm1EEE10__dispatchB8ne200100IOZNS0_6__dtorINS0_8__traitsIJNS_9monostateEN15AQProcessingTap10DirectImplEEEELNS0_6_TraitE1EE9__destroyB8ne200100EvEUlRT_E_JRNS0_6__baseILSC_1EJS8_SA_EEEEEEDcSE_DpT0_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm1EEE10__dispatchB8ne200100IOZNS0_6__dtorINS0_8__traitsIJNS_9monostateEN2AQ6Server11XPCListenerENSA_9IPCBypassEEEELNS0_6_TraitE1EE9__destroyB8ne200100EvEUlRT_E_JRNS0_6__baseILSE_1EJS8_SB_SC_EEEEEEDcSG_DpT0_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm1EEE10__dispatchB8ne200100IOZNS0_6__dtorINS0_8__traitsIJNS_9monostateEN2AT13SessionFacade7ManagerENSA_11ManagerBaseEEEELNS0_6_TraitE1EE9__destroyB8ne200100EvEUlRT_E_JRNS0_6__baseILSE_1EJS8_SB_SC_EEEEEEDcSG_DpT0_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm1EEE10__dispatchB8ne200100IOZNS0_6__dtorINS0_8__traitsIJPFvPvP16OpaqueAudioQueueP16AudioQueueBufferEPFvS8_SA_SC_PK14AudioTimeStampjPK28AudioStreamPacketDescriptionEN10applesauce8dispatch2v15blockIFvSA_SC_EEENSQ_IFvSA_SC_SH_jSK_EEEEEELNS0_6_TraitE1EE9__destroyB8ne200100EvEUlRT_E_JRNS0_6__baseILSW_1EJSE_SM_SS_SU_EEEEEEDcSY_DpT0_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm2EEE10__dispatchB8ne200100IOZNS0_6__ctorINS0_8__traitsIJPFvPvP16OpaqueAudioQueueP16AudioQueueBufferEPFvS8_SA_SC_PK14AudioTimeStampjPK28AudioStreamPacketDescriptionEN10applesauce8dispatch2v15blockIFvSA_SC_EEENSQ_IFvSA_SC_SH_jSK_EEEEEEE19__generic_constructB8ne200100IRKNS0_18__copy_constructorISV_LNS0_6_TraitE1EEEEEvRSW_OT_EUlS15_E_JRKNS0_6__baseILSZ_1EJSE_SM_SS_SU_EEEEEEDcS14_DpT0_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm2EEE10__dispatchB8ne200100IOZNS0_6__dtorINS0_8__traitsIJNS_9monostateEN2AQ6Server11XPCListenerENSA_9IPCBypassEEEELNS0_6_TraitE1EE9__destroyB8ne200100EvEUlRT_E_JRNS0_6__baseILSE_1EJS8_SB_SC_EEEEEEDcSG_DpT0_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm2EEE10__dispatchB8ne200100IOZNS0_6__dtorINS0_8__traitsIJNS_9monostateEN2AT13SessionFacade7ManagerENSA_11ManagerBaseEEEELNS0_6_TraitE1EE9__destroyB8ne200100EvEUlRT_E_JRNS0_6__baseILSE_1EJS8_SB_SC_EEEEEEDcSG_DpT0_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm2EEE10__dispatchB8ne200100IOZNS0_6__dtorINS0_8__traitsIJPFvPvP16OpaqueAudioQueueP16AudioQueueBufferEPFvS8_SA_SC_PK14AudioTimeStampjPK28AudioStreamPacketDescriptionEN10applesauce8dispatch2v15blockIFvSA_SC_EEENSQ_IFvSA_SC_SH_jSK_EEEEEELNS0_6_TraitE1EE9__destroyB8ne200100EvEUlRT_E_JRNS0_6__baseILSW_1EJSE_SM_SS_SU_EEEEEEDcSY_DpT0_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm3EEE10__dispatchB8ne200100IOZNS0_6__ctorINS0_8__traitsIJPFvPvP16OpaqueAudioQueueP16AudioQueueBufferEPFvS8_SA_SC_PK14AudioTimeStampjPK28AudioStreamPacketDescriptionEN10applesauce8dispatch2v15blockIFvSA_SC_EEENSQ_IFvSA_SC_SH_jSK_EEEEEEE19__generic_constructB8ne200100IRKNS0_18__copy_constructorISV_LNS0_6_TraitE1EEEEEvRSW_OT_EUlS15_E_JRKNS0_6__baseILSZ_1EJSE_SM_SS_SU_EEEEEEDcS14_DpT0_
+ __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm3EEE10__dispatchB8ne200100IOZNS0_6__dtorINS0_8__traitsIJPFvPvP16OpaqueAudioQueueP16AudioQueueBufferEPFvS8_SA_SC_PK14AudioTimeStampjPK28AudioStreamPacketDescriptionEN10applesauce8dispatch2v15blockIFvSA_SC_EEENSQ_IFvSA_SC_SH_jSK_EEEEEELNS0_6_TraitE1EE9__destroyB8ne200100EvEUlRT_E_JRNS0_6__baseILSW_1EJSE_SM_SS_SU_EEEEEEDcSY_DpT0_
+ __ZNSt3__116__variant_detail18__copy_constructorINS0_8__traitsIJPFvPvP16OpaqueAudioQueueP16AudioQueueBufferEPFvS3_S5_S7_PK14AudioTimeStampjPK28AudioStreamPacketDescriptionEN10applesauce8dispatch2v15blockIFvS5_S7_EEENSL_IFvS5_S7_SC_jSF_EEEEEELNS0_6_TraitE1EEC2B8ne200100ERKSS_
+ __ZNSt3__116__variant_detail6__dtorINS0_8__traitsIJNS_9monostateEN15AQProcessingTap10DirectImplEEEELNS0_6_TraitE1EE9__destroyB8ne200100Ev
+ __ZNSt3__116__variant_detail6__dtorINS0_8__traitsIJNS_9monostateEN2AQ6Server11XPCListenerENS5_9IPCBypassEEEELNS0_6_TraitE1EE9__destroyB8ne200100Ev
+ __ZNSt3__116__variant_detail6__dtorINS0_8__traitsIJPFvPvP16OpaqueAudioQueueP16AudioQueueBufferEPFvS3_S5_S7_PK14AudioTimeStampjPK28AudioStreamPacketDescriptionEN10applesauce8dispatch2v15blockIFvS5_S7_EEENSL_IFvS5_S7_SC_jSF_EEEEEELNS0_6_TraitE1EE9__destroyB8ne200100Ev
+ __ZNSt3__116allocator_traitsIN5caulk12rt_allocatorI11VolumeEventEEE17allocate_at_leastB8ne200100IS4_EENS_17allocation_resultIPS3_mEERT_m
+ __ZNSt3__116allocator_traitsIN5caulk12rt_allocatorINS_4pairIPFiPvPjPK14AudioTimeStampjjP15AudioBufferListES4_EEEEE17allocate_at_leastB8ne200100ISE_EENS_17allocation_resultIPSD_mEERT_m
+ __ZNSt3__116allocator_traitsIN5caulk12rt_allocatorINS_4pairIffEEEEE17allocate_at_leastB8ne200100IS5_EENS_17allocation_resultIPS4_mEERT_m
+ __ZNSt3__116allocator_traitsINS_9allocatorI11AQMESessionEEE7destroyB8ne200100IS2_vLi0EEEvRS3_PT_
+ __ZNSt3__116allocator_traitsINS_9allocatorI15MEVADIdentifierEEE9constructB8ne200100IS2_J14MEDeviceTypeID3$_1RPK10__CFStringEvLi0EEEvRS3_PT_DpOT0_
+ __ZNSt3__116allocator_traitsINS_9allocatorI9TapSourceEEE7destroyB8ne200100IS2_vLi0EEEvRS3_PT_
+ __ZNSt3__116allocator_traitsINS_9allocatorI9TapSourceEEE9constructB8ne200100IS2_JS2_EvLi0EEEvRS3_PT_DpOT0_
+ __ZNSt3__116allocator_traitsINS_9allocatorIN10applesauce2CF11TypeRefPairEEEE7destroyB8ne200100IS4_vLi0EEEvRS5_PT_
+ __ZNSt3__116allocator_traitsINS_9allocatorIN10applesauce2CF11TypeRefPairEEEE9constructB8ne200100IS4_JRKNS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEERKNS3_7TypeRefEEvLi0EEEvRS5_PT_DpOT0_
+ __ZNSt3__116allocator_traitsINS_9allocatorIN10applesauce2CF7TypeRefEEEE9constructB8ne200100IS4_JdEvLi0EEEvRS5_PT_DpOT0_
+ __ZNSt3__116allocator_traitsINS_9allocatorIN10applesauce2CF9NumberRefEEEE9constructB8ne200100IS4_JjEvLi0EEEvRS5_PT_DpOT0_
+ __ZNSt3__116allocator_traitsINS_9allocatorIN21IPCAUSharedMemoryBase7ElementEEEE7destroyB8ne200100IS3_vLi0EEEvRS4_PT_
+ __ZNSt3__116allocator_traitsINS_9allocatorINS_4pairIN2OS2CF6StringEN10applesauce8dispatch2v15blockIFv13CAOrientationEEEEEEEE7destroyB8ne200100ISD_vLi0EEEvRSE_PT_
+ __ZNSt3__116allocator_traitsINS_9allocatorINS_4pairIN2OS2CF6StringEN10applesauce8dispatch2v15blockIFv13CAOrientationEEEEEEEE9constructB8ne200100ISD_JSD_EvLi0EEEvRSE_PT_DpOT0_
+ __ZNSt3__117__assoc_sub_state10__sub_waitERNS_11unique_lockINS_5mutexEEE
+ __ZNSt3__117__assoc_sub_state13set_exceptionESt13exception_ptr
+ __ZNSt3__117__assoc_sub_state9__executeEv
+ __ZNSt3__117__call_once_proxyB8ne200100INS_5tupleIJOZ31SetupSystemSoundClientLogScopesvE3$_0EEEEEvPv
+ __ZNSt3__117__call_once_proxyB8ne200100INS_5tupleIJOZL12logSubsystemvE3$_0EEEEEvPv
+ __ZNSt3__117__call_once_proxyB8ne200100INS_5tupleIJOZN11AQAC3IONodeC1ERK14AQMEIO_Binding14MEStreamTypeIDRidE3$_0EEEEEvPv
+ __ZNSt3__117__call_once_proxyB8ne200100INS_5tupleIJOZN11SSServerIPCC1EvE3$_0EEEEEvPv
+ __ZNSt3__117__call_once_proxyB8ne200100INS_5tupleIJOZN12CADeprecated10TSingletonI11SSClientIPCE8instanceEvEUlvE_EEEEEvPv
+ __ZNSt3__117__call_once_proxyB8ne200100INS_5tupleIJOZN12CADeprecated10TSingletonI13HapticMetricsE8instanceEvEUlvE_EEEEEvPv
+ __ZNSt3__117__call_once_proxyB8ne200100INS_5tupleIJOZN12CADeprecated10TSingletonI14RemoteIOServerE8instanceEvEUlvE_EEEEEvPv
+ __ZNSt3__117__call_once_proxyB8ne200100INS_5tupleIJOZN12CADeprecated10TSingletonI15ActiveSoundListE8instanceEvEUlvE_EEEEEvPv
+ __ZNSt3__117__call_once_proxyB8ne200100INS_5tupleIJOZN12CADeprecated10TSingletonI18SSClientCompletionE8instanceEvEUlvE_EEEEEvPv
+ __ZNSt3__117__call_once_proxyB8ne200100INS_5tupleIJOZN12CADeprecated10TSingletonI19HapticServerManagerE8instanceEvEUlvE_EEEEEvPv
+ __ZNSt3__117__call_once_proxyB8ne200100INS_5tupleIJOZN12CADeprecated10TSingletonI20SSSCallbackMessengerE8instanceEvEUlvE_EEEEEvPv
+ __ZNSt3__117__call_once_proxyB8ne200100INS_5tupleIJOZN12CADeprecated10TSingletonI21CAExternalLockJanitorE8instanceEvEUlvE_EEEEEvPv
+ __ZNSt3__117__call_once_proxyB8ne200100INS_5tupleIJOZN12CADeprecated10TSingletonI8SSServerE8instanceEvEUlvE_EEEEEvPv
+ __ZNSt3__117__call_once_proxyB8ne200100INS_5tupleIJOZN12CADeprecated10TSingletonIN12_GLOBAL__N_118CoreMotionSoftlinkEE8instanceEvEUlvE_EEEEEvPv
+ __ZNSt3__117__call_once_proxyB8ne200100INS_5tupleIJOZN12CADeprecated10TSingletonIN15CAListenerProxy13ZombieJanitorEE8instanceEvEUlvE_EEEEEvPv
+ __ZNSt3__117__call_once_proxyB8ne200100INS_5tupleIJOZN12CADeprecated10TSingletonIN20AudioImpulseInjector4Impl20NotificationListenerEE8instanceEvEUlvE_EEEEEvPv
+ __ZNSt3__117__call_once_proxyB8ne200100INS_5tupleIJOZN18AQOfflineMixerBaseC1ER15AQIONodeManageriRK27AudioStreamBasicDescriptionRKN2CA13ChannelLayoutERiE3$_0EEEEEvPv
+ __ZNSt3__117__call_once_proxyB8ne200100INS_5tupleIJOZN20CA_UISoundClientBaseC1EdjPK14__CFDictionaryjN10applesauce2CF7TypeRefEibE3$_0EEEEEvPv
+ __ZNSt3__118__set_intersectionB8ne200100INS_17_ClassicAlgPolicyENS_6__lessIvvEENS_21__hash_const_iteratorIPNS_11__hash_nodeIjPvEEEES9_S9_S9_NS_20back_insert_iteratorINS_6vectorIjNS_9allocatorIjEEEEEEEENS_25__set_intersection_resultIT1_T3_T5_EESH_T2_SI_T4_SJ_OT0_NS_20forward_iterator_tagESP_
+ __ZNSt3__118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B8ne200100Ev
+ __ZNSt3__118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEED2Ev
+ __ZNSt3__119__shared_weak_count16__release_sharedB8ne200100Ev
+ __ZNSt3__119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B8ne200100Ev
+ __ZNSt3__119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEED2Ev
+ __ZNSt3__120__optional_copy_baseIN2CA13ChannelLayoutELb0EEC2B8ne200100ERKS3_
+ __ZNSt3__120__optional_copy_baseIN4swix14timeout_configELb0EEC2B8ne200100ERKS3_
+ __ZNSt3__120__optional_copy_baseINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEELb0EEC2B8ne200100ERKS7_
+ __ZNSt3__120__shared_ptr_emplaceI14MixTapToUplinkNS_9allocatorIS1_EEE16__on_zero_sharedEv
+ __ZNSt3__120__shared_ptr_emplaceI14MixTapToUplinkNS_9allocatorIS1_EEE21__on_zero_shared_weakEv
+ __ZNSt3__120__shared_ptr_emplaceI14MixTapToUplinkNS_9allocatorIS1_EEED0Ev
+ __ZNSt3__120__shared_ptr_emplaceI14MixTapToUplinkNS_9allocatorIS1_EEED1Ev
+ __ZNSt3__120__shared_ptr_emplaceI16MCProcessingNodeNS_9allocatorIS1_EEE16__on_zero_sharedEv
+ __ZNSt3__120__shared_ptr_emplaceI16MCProcessingNodeNS_9allocatorIS1_EEE21__on_zero_shared_weakEv
+ __ZNSt3__120__shared_ptr_emplaceI16MCProcessingNodeNS_9allocatorIS1_EEED0Ev
+ __ZNSt3__120__shared_ptr_emplaceI16MCProcessingNodeNS_9allocatorIS1_EEED1Ev
+ __ZNSt3__120__shared_ptr_emplaceIN5caulk12synchronizedIN2AQ6Server16ProcessingTapIPCENS1_22pooled_semaphore_mutexENS1_22empty_atomic_interfaceIS5_EEEENS_9allocatorIS9_EEE16__on_zero_sharedEv
+ __ZNSt3__120__shared_ptr_emplaceIN5caulk12synchronizedIN2AQ6Server16ProcessingTapIPCENS1_22pooled_semaphore_mutexENS1_22empty_atomic_interfaceIS5_EEEENS_9allocatorIS9_EEE21__on_zero_shared_weakEv
+ __ZNSt3__120__shared_ptr_emplaceIN5caulk12synchronizedIN2AQ6Server16ProcessingTapIPCENS1_22pooled_semaphore_mutexENS1_22empty_atomic_interfaceIS5_EEEENS_9allocatorIS9_EEED0Ev
+ __ZNSt3__120__shared_ptr_emplaceIN5caulk12synchronizedIN2AQ6Server16ProcessingTapIPCENS1_22pooled_semaphore_mutexENS1_22empty_atomic_interfaceIS5_EEEENS_9allocatorIS9_EEED1Ev
+ __ZNSt3__120__shared_ptr_emplaceIN5caulk7details19lifetime_guard_baseIN2AT11Translation16TranslatorClientEE13control_blockENS_9allocatorIS8_EEE16__on_zero_sharedEv
+ __ZNSt3__120__shared_ptr_emplaceIN5caulk7details19lifetime_guard_baseIN2AT11Translation16TranslatorClientEE13control_blockENS_9allocatorIS8_EEE21__on_zero_shared_weakEv
+ __ZNSt3__120__shared_ptr_emplaceIN5caulk7details19lifetime_guard_baseIN2AT11Translation16TranslatorClientEE13control_blockENS_9allocatorIS8_EEED0Ev
+ __ZNSt3__120__shared_ptr_emplaceIN5caulk7details19lifetime_guard_baseIN2AT11Translation16TranslatorClientEE13control_blockENS_9allocatorIS8_EEED1Ev
+ __ZNSt3__120__shared_ptr_pointerIPN2AT11Translation14CallTranslatorENS_10shared_ptrIS3_E27__shared_ptr_default_deleteIS3_S3_EENS_9allocatorIS3_EEE16__on_zero_sharedEv
+ __ZNSt3__120__shared_ptr_pointerIPN2AT11Translation14CallTranslatorENS_10shared_ptrIS3_E27__shared_ptr_default_deleteIS3_S3_EENS_9allocatorIS3_EEE21__on_zero_shared_weakEv
+ __ZNSt3__120__shared_ptr_pointerIPN2AT11Translation14CallTranslatorENS_10shared_ptrIS3_E27__shared_ptr_default_deleteIS3_S3_EENS_9allocatorIS3_EEED0Ev
+ __ZNSt3__120__shared_ptr_pointerIPN2AT11Translation14CallTranslatorENS_10shared_ptrIS3_E27__shared_ptr_default_deleteIS3_S3_EENS_9allocatorIS3_EEED1Ev
+ __ZNSt3__120__shared_ptr_pointerIPxZN14MixTapToUplink16AQMETapConnector22getCAReporterIDForCallEvEUlS1_E_NS_9allocatorIxEEE16__on_zero_sharedEv
+ __ZNSt3__120__shared_ptr_pointerIPxZN14MixTapToUplink16AQMETapConnector22getCAReporterIDForCallEvEUlS1_E_NS_9allocatorIxEEE21__on_zero_shared_weakEv
+ __ZNSt3__120__shared_ptr_pointerIPxZN14MixTapToUplink16AQMETapConnector22getCAReporterIDForCallEvEUlS1_E_NS_9allocatorIxEEED0Ev
+ __ZNSt3__120__shared_ptr_pointerIPxZN14MixTapToUplink16AQMETapConnector22getCAReporterIDForCallEvEUlS1_E_NS_9allocatorIxEEED1Ev
+ __ZNSt3__120__throw_bad_weak_ptrB8ne200100Ev
+ __ZNSt3__120__throw_future_errorB8ne200100ENS_11future_errcE
+ __ZNSt3__120__throw_length_errorB8ne200100EPKc
+ __ZNSt3__120__throw_out_of_rangeB8ne200100EPKc
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEPvEEEEEclB8ne200100EPS9_
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEE26STSPerLabelControllerStateEEPvEEEEEclB8ne200100EPSC_
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEbEEPvEEEEEclB8ne200100EPSB_
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIPvN10applesauce8dispatch2v15blockIFv28AUVoiceIOSpeechActivityEventEEEEES4_EEEEEclB8ne200100EPSD_
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIjNS_10unique_ptrI27SSClientCompletionBlockInfoNS_14default_deleteIS5_EEEEEEPvEEEEEclB8ne200100EPSB_
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIjNS_6vectorIhNS1_IhEEEEEEPvEEEEEclB8ne200100EPS9_
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeImNS_10shared_ptrI14HapticSequenceEEEEPvEEEEEclB8ne200100EPS9_
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeImNS_10shared_ptrIN18PowerUsageWatchdog17ClientDescriptionEEEEEPvEEEEEclB8ne200100EPSA_
+ __ZNSt3__122__lower_bound_onesidedB8ne200100INS_17_ClassicAlgPolicyENS_21__hash_const_iteratorIPNS_11__hash_nodeIjPvEEEES7_jKNS_10__identityENS_6__lessIvvEEEET0_SC_T1_RKT2_RT4_RT3_
+ __ZNSt3__122__tree_node_destructorINS_9allocatorINS_11__tree_nodeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEN10applesauce2CF7TypeRefEEEPvEEEEEclB8ne200100EPSE_
+ __ZNSt3__122__tree_node_destructorINS_9allocatorINS_11__tree_nodeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEPK14__CFDictionaryEEPvEEEEEclB8ne200100EPSE_
+ __ZNSt3__123__optional_storage_baseI14AQMEIO_BindingLb0EE13__assign_fromB8ne200100IRKNS_27__optional_copy_assign_baseIS1_Lb0EEEEEvOT_
+ __ZNSt3__123__optional_storage_baseIN10applesauce2CF9StringRefELb0EE13__assign_fromB8ne200100INS_27__optional_move_assign_baseIS3_Lb0EEEEEvOT_
+ __ZNSt3__123__optional_storage_baseIN10applesauce2CF9StringRefELb0EE13__assign_fromB8ne200100IRKNS_27__optional_copy_assign_baseIS3_Lb0EEEEEvOT_
+ __ZNSt3__123__optional_storage_baseIN2AT9IOBindingELb0EE13__assign_fromB8ne200100IRKNS_27__optional_copy_assign_baseIS2_Lb0EEEEEvOT_
+ __ZNSt3__123__optional_storage_baseIN2CA13ChannelLayoutELb0EE13__assign_fromB8ne200100INS_27__optional_move_assign_baseIS2_Lb0EEEEEvOT_
+ __ZNSt3__124__optional_destruct_baseIN2CA16AudioBuffersBaseELb0EE5resetB8ne200100Ev
+ __ZNSt3__124__optional_destruct_baseIN5caulk5alloc23guarded_edges_allocatorINS2_16tiered_allocatorIJNS2_15size_range_tierILm0ELm409599ENS2_22consolidating_free_mapIN2AQ19SharedPageAllocatorELm10485760EEEEENS2_18tracking_allocatorIS8_EEEEELm2EEELb0EE5resetB8ne200100Ev
+ __ZNSt3__124__optional_destruct_baseIN9TapSubmix10InputState14BufferingStateELb0EE5resetB8ne200100Ev
+ __ZNSt3__124__put_character_sequenceB8ne200100IcNS_11char_traitsIcEEEERNS_13basic_ostreamIT_T0_EES7_PKS4_m
+ __ZNSt3__125__bucket_list_deallocatorIN5caulk12rt_allocatorIPNS_16__hash_node_baseIPNS_11__hash_nodeINS_17__hash_value_typeImbEEPvEEEEEEEclB8ne200100EPSB_
+ __ZNSt3__125__throw_bad_function_callB8ne200100Ev
+ __ZNSt3__126__throw_bad_variant_accessB8ne200100Ev
+ __ZNSt3__127__insertion_sort_incompleteB8ne200100INS_17_ClassicAlgPolicyERNS_6__lessIvvEEP10MusicEventEEbT1_S7_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne200100INS_17_ClassicAlgPolicyERNS_6__lessIvvEEP11VolumeEventEEbT1_S7_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne200100INS_17_ClassicAlgPolicyERNS_6__lessIvvEEP15MEVADIdentifierEEbT1_S7_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne200100INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPN14NoteOffManager11NoteOffInfoEEEbT1_S8_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne200100INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEEbT1_SC_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne200100INS_17_ClassicAlgPolicyERZN17AudioTapSpecifierC1ENS_6vectorIjNS_9allocatorIjEEEE22ATAudioTapMuteBehaviorEUlRK11AQMESessionSA_E_PS8_EEbT1_SE_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne200100INS_17_ClassicAlgPolicyERZZZN2AT11Translation19AUAsyncRendererHost9ConfigureEvENK3$_0clENS_6chrono10time_pointINS6_12steady_clockENS6_8durationIxNS_5ratioILl1ELl1000000000EEEEEEERK15AudioBufferListiENKUlRT_E_clINS_6vectorINS4_34TemporallyOrdereredAudioBufferListENS_9allocatorISM_EEEEEEDaSI_EUlRKSM_SS_E_PSM_EEbT1_SW_T0_
+ __ZNSt3__127__throw_bad_optional_accessB8ne200100Ev
+ __ZNSt3__127__tree_balance_after_insertB8ne200100IPNS_16__tree_node_baseIPvEEEEvT_S5_
+ __ZNSt3__133lexicographical_compare_three_wayB8ne200100INS_11__wrap_iterIPKiEES4_NS_17__synth_three_wayMUlTyTyRKT_RKT0_E_EEEDTclfp3_defp_defp1_EES5_S5_S8_S8_T1_
+ __ZNSt3__134__uninitialized_allocator_relocateB8ne200100INS_9allocatorI10MusicEventEEPS2_EEvRT_T0_S7_S7_
+ __ZNSt3__134__uninitialized_allocator_relocateB8ne200100INS_9allocatorI11AQMESessionEEPS2_EEvRT_T0_S7_S7_
+ __ZNSt3__134__uninitialized_allocator_relocateB8ne200100INS_9allocatorI9TapSourceEEPS2_EEvRT_T0_S7_S7_
+ __ZNSt3__134__uninitialized_allocator_relocateB8ne200100INS_9allocatorIN10applesauce2CF11TypeRefPairEEEPS4_EEvRT_T0_S9_S9_
+ __ZNSt3__134__uninitialized_allocator_relocateB8ne200100INS_9allocatorIN8InfoList9InfoEntryEEEPS3_EEvRT_T0_S8_S8_
+ __ZNSt3__134__uninitialized_allocator_relocateB8ne200100INS_9allocatorIN8audioipc18SharedAudioBuffers7ElementEEEPS4_EEvRT_T0_S9_S9_
+ __ZNSt3__134__uninitialized_allocator_relocateB8ne200100INS_9allocatorINS_4pairIN2OS2CF6StringEN10applesauce8dispatch2v15blockIFv13CAOrientationEEEEEEEPSD_EEvRT_T0_SI_SI_
+ __ZNSt3__135__uninitialized_allocator_copy_implB8ne200100INS_9allocatorI10MusicEventEEPS2_S4_S4_EET2_RT_T0_T1_S5_
+ __ZNSt3__135__uninitialized_allocator_copy_implB8ne200100INS_9allocatorI11AQMESessionEEPKS2_S5_PS2_EET2_RT_T0_T1_S7_
+ __ZNSt3__135__uninitialized_allocator_copy_implB8ne200100INS_9allocatorI11AQMESessionEEPS2_S4_S4_EET2_RT_T0_T1_S5_
+ __ZNSt3__135__uninitialized_allocator_copy_implB8ne200100INS_9allocatorINS_10shared_ptrI9TapSubmixEEEEPS4_S6_S6_EET2_RT_T0_T1_S7_
+ __ZNSt3__13mapIjP15ActiveSoundInfoNS_4lessIjEENS_9allocatorINS_4pairIKjS2_EEEEE2atERS7_
+ __ZNSt3__13setIP10XAudioUnitNS_4lessIS2_EENS_9allocatorIS2_EEEC2B8ne200100ERKS7_
+ __ZNSt3__14__fs10filesystem4pathC2B8ne200100INS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEvEERKT_NS2_6formatE
+ __ZNSt3__14listIN13ServerManager12SynthCommandEN5caulk12rt_allocatorIS2_EEE9pop_frontEv
+ __ZNSt3__14pairIKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEN10applesauce2CF7TypeRefEED2Ev
+ __ZNSt3__14pairIKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI29NewNotificationCenterObserverEEED2Ev
+ __ZNSt3__14pairIKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI29OldNotificationCenterObserverEEED2Ev
+ __ZNSt3__14pairIN2OS2CF6StringEN10applesauce8dispatch2v15blockIFv13CAOrientationEEEEaSB8ne200100EOSB_
+ __ZNSt3__14swapB8ne200100I11AQMESessionEENS_9enable_ifIXaasr21is_move_constructibleIT_EE5valuesr18is_move_assignableIS3_EE5valueEvE4typeERS3_S6_
+ __ZNSt3__14swapB8ne200100IU8__strongU13block_pointerFvPK15AudioBufferListjEEENS_9enable_ifIXaasr21is_move_constructibleIT_EE5valuesr18is_move_assignableIS8_EE5valueEvE4typeERS8_SB_
+ __ZNSt3__15arrayIN5Phase13ServerManager12IONodeClientELm2EED2Ev
+ __ZNSt3__15dequeIN5boost8functionIFNS1_3msm4back11HandledEnumEvEEENS_9allocatorIS7_EEED2B8ne200100Ev
+ __ZNSt3__15dequeINS_4pairIN5boost8functionIFNS2_3msm4back11HandledEnumEvEEEbEENS_9allocatorIS9_EEE26__maybe_remove_front_spareB8ne200100Eb
+ __ZNSt3__15dequeINS_4pairIN5boost8functionIFNS2_3msm4back11HandledEnumEvEEEbEENS_9allocatorIS9_EEED2B8ne200100Ev
+ __ZNSt3__15dequeIjNS_9allocatorIjEEE26__maybe_remove_front_spareB8ne200100Eb
+ __ZNSt3__15dequeIjNS_9allocatorIjEEED2B8ne200100Ev
+ __ZNSt3__15tupleIJN10applesauce3xpc6objectEN4swix6stringEjEEC1ERKS6_
+ __ZNSt3__15tupleIJN10applesauce3xpc6objectEN4swix6stringEjEED2Ev
+ __ZNSt3__15tupleIJN10applesauce3xpc6objectEjjbNS_6vectorIjNS_9allocatorIjEEEEEED2Ev
+ __ZNSt3__15tupleIJN4swix4dataEEEC1ERKS3_
+ __ZNSt3__15tupleIJjj27AudioStreamBasicDescriptionN10applesauce3xpc6objectES4_EEC1ERKS5_
+ __ZNSt3__15tupleIJjj27AudioStreamBasicDescriptionN10applesauce3xpc6objectES4_EED2Ev
+ __ZNSt3__16__lerpB8ne200100IdEET_S1_S1_S1_
+ __ZNSt3__16__treeINS_12__value_typeIPK14AQIONodeClientZN2AT13SessionFacadeL34PopulateSourceFormatInfoDictionaryEP14__CFDictionaryPKvRS3_RN2CA17StreamDescriptionEbbbE16SourceFormatInfoEENS_19__map_value_compareIS4_SG_NS_4lessIS4_EELb1EEENS_9allocatorISG_EEE7destroyEPNS_11__tree_nodeISG_PvEE
+ __ZNSt3__16any_ofB8ne200100INS_11__wrap_iterIPPK10__CFStringEEZN16AudioQueueObject11SetPropertyEjR14CADeserializerE3$_0EEbT_SB_T0_
+ __ZNSt3__16localeC1Ev
+ __ZNSt3__16vectorI10ChaseEventN5caulk12rt_allocatorIS1_EEE16__destroy_vectorclB8ne200100Ev
+ __ZNSt3__16vectorI10ChaseEventN5caulk12rt_allocatorIS1_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorI10ChaseEventN5caulk12rt_allocatorIS1_EEE5eraseENS_11__wrap_iterIPKS1_EES9_
+ __ZNSt3__16vectorI10MusicEventNS_9allocatorIS1_EEE16__destroy_vectorclB8ne200100Ev
+ __ZNSt3__16vectorI10MusicEventNS_9allocatorIS1_EEE18__assign_with_sizeB8ne200100IPS1_S6_EEvT_T0_l
+ __ZNSt3__16vectorI10MusicEventNS_9allocatorIS1_EEE18__insert_with_sizeB8ne200100INS_11__wrap_iterIPS1_EES8_EES8_NS6_IPKS1_EET_T0_l
+ __ZNSt3__16vectorI10MusicEventNS_9allocatorIS1_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorI10MusicEventNS_9allocatorIS1_EEE9push_backB8ne200100ERKS1_
+ __ZNSt3__16vectorI10PowerMeterNS_9allocatorIS1_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorI11AQMESessionNS_9allocatorIS1_EEE11__vallocateB8ne200100Em
+ __ZNSt3__16vectorI11AQMESessionNS_9allocatorIS1_EEE13__vdeallocateEv
+ __ZNSt3__16vectorI11AQMESessionNS_9allocatorIS1_EEE16__destroy_vectorclB8ne200100Ev
+ __ZNSt3__16vectorI11AQMESessionNS_9allocatorIS1_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorI11TrackChaserNS_9allocatorIS1_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorI11VolumeEventN5caulk12rt_allocatorIS1_EEE16__destroy_vectorclB8ne200100Ev
+ __ZNSt3__16vectorI11VolumeEventN5caulk12rt_allocatorIS1_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorI13ChaseInstInfoNS_9allocatorIS1_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorI13RootQueueInfoNS_9allocatorIS1_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorI14MEStreamTypeIDNS_9allocatorIS1_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorI15MEVADIdentifierNS_9allocatorIS1_EEE11__vallocateB8ne200100Em
+ __ZNSt3__16vectorI15MEVADIdentifierNS_9allocatorIS1_EEE16__destroy_vectorclB8ne200100Ev
+ __ZNSt3__16vectorI15MEVADIdentifierNS_9allocatorIS1_EEE16__init_with_sizeB8ne200100IPS1_S6_EEvT_T0_m
+ __ZNSt3__16vectorI15MEVADIdentifierNS_9allocatorIS1_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorI15MeterTrackEntryNS_9allocatorIS1_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorI15MeterTrackEntryNS_9allocatorIS1_EEE9push_backB8ne200100ERKS1_
+ __ZNSt3__16vectorI16AURateRampStructNS_9allocatorIS1_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorI18AudioMetadataEventNS_9allocatorIS1_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorI18AudioMetadataEventNS_9allocatorIS1_EEE9push_backB8ne200100ERKS1_
+ __ZNSt3__16vectorI20AUNodeRenderCallbackNS_9allocatorIS1_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorI22AUGraphLiveUpdateEventNS_9allocatorIS1_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorI22AUGraphLiveUpdateEventNS_9allocatorIS1_EEE9push_backB8ne200100ERKS1_
+ __ZNSt3__16vectorI23AudioUnitNodeConnectionNS_9allocatorIS1_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorI23AudioUnitParameterEventN5caulk12rt_allocatorIS1_EEE16__destroy_vectorclB8ne200100Ev
+ __ZNSt3__16vectorI23AudioUnitParameterEventN5caulk12rt_allocatorIS1_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorI23AudioUnitParameterEventNS_9allocatorIS1_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorI24AudioQueueParameterEventNS_9allocatorIS1_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorI25AudioQueueLevelMeterStateNS_9allocatorIS1_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorI26AQBufferCreateDestroyEventNS_9allocatorIS1_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorI26AudioObjectPropertyAddressNS_9allocatorIS1_EEE11__vallocateB8ne200100Em
+ __ZNSt3__16vectorI26AudioObjectPropertyAddressNS_9allocatorIS1_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorI27AudioQueueChannelAssignmentNS_9allocatorIS1_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorI28AudioStreamPacketDescriptionNS_9allocatorIS1_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorI30AQProcessingNodeImmediateEventNS_9allocatorIS1_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorI32AudioSessionPropertyListenerInfoNS_9allocatorIS1_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorI9TapSourceNS_9allocatorIS1_EEE16__destroy_vectorclB8ne200100Ev
+ __ZNSt3__16vectorI9TapSourceNS_9allocatorIS1_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN10applesauce2CF11TypeRefPairENS_9allocatorIS3_EEE16__destroy_vectorclB8ne200100Ev
+ __ZNSt3__16vectorIN10applesauce2CF11TypeRefPairENS_9allocatorIS3_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN10applesauce2CF11TypeRefPairENS_9allocatorIS3_EEE9push_backB8ne200100EOS3_
+ __ZNSt3__16vectorIN10applesauce2CF7TypeRefENS_9allocatorIS3_EEE16__destroy_vectorclB8ne200100Ev
+ __ZNSt3__16vectorIN10applesauce2CF7TypeRefENS_9allocatorIS3_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN10applesauce2CF9NumberRefENS_9allocatorIS3_EEE16__destroy_vectorclB8ne200100Ev
+ __ZNSt3__16vectorIN10applesauce2CF9NumberRefENS_9allocatorIS3_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN14AudioUnitGraph14RenderCallbackENS_9allocatorIS2_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN14NoteOffManager14ControlMessageENS_9allocatorIS2_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN14NoteOffManager14ControlMessageENS_9allocatorIS2_EEE9push_backB8ne200100EOS2_
+ __ZNSt3__16vectorIN16AudioQueueObject12AQRateChangeENS_9allocatorIS2_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN18AQOfflineMixerBase10MixerQueueENS_9allocatorIS2_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN18AQOfflineMixerBase15StartQueueEventENS_9allocatorIS2_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN18PlayerSynchronizer6PlayerENS_9allocatorIS2_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN19SequenceDestination14TrackPlayStateENS_9allocatorIS2_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN19SequenceDestination14TrackPlayStateENS_9allocatorIS2_EEE9push_backB8ne200100ERKS2_
+ __ZNSt3__16vectorIN21IPCAUSharedMemoryBase7ElementENS_9allocatorIS2_EEE16__destroy_vectorclB8ne200100Ev
+ __ZNSt3__16vectorIN21VibeToHapticConverter11SegmentInfoENS_9allocatorIS2_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN21VibeToHapticConverter11SegmentInfoENS_9allocatorIS2_EEE9push_backB8ne200100EOS2_
+ __ZNSt3__16vectorIN25AUNodeSequenceDestination18RampTrackPlayStateENS_9allocatorIS2_EEE16__destroy_vectorclB8ne200100Ev
+ __ZNSt3__16vectorIN25AUNodeSequenceDestination18RampTrackPlayStateENS_9allocatorIS2_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN2AQ6Server12RemoteClient18ProcessingTapStateENS_9allocatorIS4_EEE16__destroy_vectorclB8ne200100Ev
+ __ZNSt3__16vectorIN2AQ6Server12RemoteClient18ProcessingTapStateENS_9allocatorIS4_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN2AQ6Server12RemoteClient5QueueENS_9allocatorIS4_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN2AT11Translation19AUAsyncRendererHost34TemporallyOrdereredAudioBufferListENS_9allocatorIS4_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN2AU8Property10Attributes7details15AUPresetWrapperENS_9allocatorIS5_EEE16__destroy_vectorclB8ne200100Ev
+ __ZNSt3__16vectorIN2AU8Property10Attributes7details15AUPresetWrapperENS_9allocatorIS5_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN5boost8functionIFvRN11SequenceFSM25PostRenderFlushingVisitorEP14SequenceActiondEEENS_9allocatorIS9_EEE16__destroy_vectorclB8ne200100Ev
+ __ZNSt3__16vectorIN5boost8functionIFvRN11SequenceFSM25PostRenderFlushingVisitorEP14SequenceActiondEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN8InfoList9InfoEntryENS_9allocatorIS2_EEE16__destroy_vectorclB8ne200100Ev
+ __ZNSt3__16vectorIN8InfoList9InfoEntryENS_9allocatorIS2_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN8TempoMap10TempoEntryENS_9allocatorIS2_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN8XAUMixer11EInputStateENS_9allocatorIS2_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN8audioipc18SharedAudioBuffers7ElementENS_9allocatorIS3_EEE16__destroy_vectorclB8ne200100Ev
+ __ZNSt3__16vectorIN8audioipc18SharedAudioBuffers7ElementENS_9allocatorIS3_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorINS_10shared_ptrI14HapticSequenceEEN5caulk12rt_allocatorIS3_EEE16__destroy_vectorclB8ne200100Ev
+ __ZNSt3__16vectorINS_10shared_ptrI14HapticSequenceEEN5caulk12rt_allocatorIS3_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorINS_10shared_ptrI14HapticSequenceEEN5caulk12rt_allocatorIS3_EEE5clearB8ne200100Ev
+ __ZNSt3__16vectorINS_10shared_ptrI16MCProcessingNodeEENS_9allocatorIS3_EEE16__destroy_vectorclB8ne200100Ev
+ __ZNSt3__16vectorINS_10shared_ptrI16MCProcessingNodeEENS_9allocatorIS3_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorINS_10shared_ptrI16MCProcessingNodeEENS_9allocatorIS3_EEE9push_backB8ne200100ERKS3_
+ __ZNSt3__16vectorINS_10shared_ptrI8AQIONodeEENS_9allocatorIS3_EEE16__destroy_vectorclB8ne200100Ev
+ __ZNSt3__16vectorINS_10shared_ptrI8AQIONodeEENS_9allocatorIS3_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorINS_10shared_ptrI9TapSubmixEENS_9allocatorIS3_EEE11__vallocateB8ne200100Em
+ __ZNSt3__16vectorINS_10shared_ptrI9TapSubmixEENS_9allocatorIS3_EEE16__destroy_vectorclB8ne200100Ev
+ __ZNSt3__16vectorINS_10shared_ptrI9TapSubmixEENS_9allocatorIS3_EEE16__init_with_sizeB8ne200100IPS3_S8_EEvT_T0_m
+ __ZNSt3__16vectorINS_10shared_ptrI9TapSubmixEENS_9allocatorIS3_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorINS_10shared_ptrI9TapSubmixEENS_9allocatorIS3_EEE5clearB8ne200100Ev
+ __ZNSt3__16vectorINS_10shared_ptrIN10AQMEIO_HAL8IOStreamEEENS_9allocatorIS4_EEE16__destroy_vectorclB8ne200100Ev
+ __ZNSt3__16vectorINS_10shared_ptrIN10AQMEIO_HAL8IOStreamEEENS_9allocatorIS4_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorINS_10shared_ptrIN10AQMEIO_HAL8IOStreamEEENS_9allocatorIS4_EEE5clearB8ne200100Ev
+ __ZNSt3__16vectorINS_10shared_ptrIN18PowerUsageWatchdog17ClientDescriptionEEENS_9allocatorIS4_EEE16__destroy_vectorclB8ne200100Ev
+ __ZNSt3__16vectorINS_10shared_ptrIN18PowerUsageWatchdog17ClientDescriptionEEENS_9allocatorIS4_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorINS_10shared_ptrIN2AQ3API9SubmixTapEEENS_9allocatorIS5_EEE16__destroy_vectorclB8ne200100Ev
+ __ZNSt3__16vectorINS_10shared_ptrIN2AQ3API9SubmixTapEEENS_9allocatorIS5_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorINS_10unique_ptrI11IAQMEDeviceNS_14default_deleteIS2_EEEENS_9allocatorIS5_EEE16__destroy_vectorclB8ne200100Ev
+ __ZNSt3__16vectorINS_10unique_ptrI11IAQMEDeviceNS_14default_deleteIS2_EEEENS_9allocatorIS5_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorINS_10unique_ptrI14AQClientBufferN2AQ3API13BufferDeleterEEENS_9allocatorIS6_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorINS_10unique_ptrI14AQOfflineMixerNS_14default_deleteIS2_EEEENS_9allocatorIS5_EEE16__destroy_vectorclB8ne200100Ev
+ __ZNSt3__16vectorINS_10unique_ptrI14AQOfflineMixerNS_14default_deleteIS2_EEEENS_9allocatorIS5_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorINS_10unique_ptrI14AQOfflineMixerNS_14default_deleteIS2_EEEENS_9allocatorIS5_EEE5clearB8ne200100Ev
+ __ZNSt3__16vectorINS_10unique_ptrI15SubmixTapObjectNS_14default_deleteIS2_EEEENS_9allocatorIS5_EEE16__destroy_vectorclB8ne200100Ev
+ __ZNSt3__16vectorINS_10unique_ptrI15SubmixTapObjectNS_14default_deleteIS2_EEEENS_9allocatorIS5_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorINS_10unique_ptrI16AQProcessingNodeNS_14default_deleteIS2_EEEENS_9allocatorIS5_EEE16__destroy_vectorclB8ne200100Ev
+ __ZNSt3__16vectorINS_10unique_ptrI16AQProcessingNodeNS_14default_deleteIS2_EEEENS_9allocatorIS5_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorINS_10unique_ptrI16SSSVibrationDataNS_14default_deleteIS2_EEEENS_9allocatorIS5_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorINS_10unique_ptrIN18PowerUsageWatchdog12ClientLoggerENS_14default_deleteIS3_EEEENS_9allocatorIS6_EEE16__destroy_vectorclB8ne200100Ev
+ __ZNSt3__16vectorINS_10unique_ptrIN18PowerUsageWatchdog12ClientLoggerENS_14default_deleteIS3_EEEENS_9allocatorIS6_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorINS_10unique_ptrIN2AQ6Server12RemoteClientENS_14default_deleteIS4_EEEENS_9allocatorIS7_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE16__destroy_vectorclB8ne200100Ev
+ __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorINS_13unordered_mapINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEbNS_4hashIS7_EENS_8equal_toIS7_EENS5_INS_4pairIKS7_bEEEEEENS5_ISG_EEE16__destroy_vectorclB8ne200100Ev
+ __ZNSt3__16vectorINS_4pairIN2OS2CF6StringEN10applesauce8dispatch2v15blockIFv13CAOrientationEEEEENS_9allocatorISC_EEE16__destroy_vectorclB8ne200100Ev
+ __ZNSt3__16vectorINS_4pairIN2OS2CF6StringEN10applesauce8dispatch2v15blockIFv13CAOrientationEEEEENS_9allocatorISC_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorINS_4pairINS_10unique_ptrI11SynthOutputNS_14default_deleteIS3_EEEEbEENS_9allocatorIS7_EEE16__destroy_vectorclB8ne200100Ev
+ __ZNSt3__16vectorINS_4pairINS_10unique_ptrI11SynthOutputNS_14default_deleteIS3_EEEEbEENS_9allocatorIS7_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorINS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEES7_EENS5_IS8_EEE16__destroy_vectorclB8ne200100Ev
+ __ZNSt3__16vectorINS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEES7_EENS5_IS8_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorINS_4pairIPFiPvPjPK14AudioTimeStampjjP15AudioBufferListES2_EEN5caulk12rt_allocatorISB_EEE16__destroy_vectorclB8ne200100Ev
+ __ZNSt3__16vectorINS_4pairIPFiPvPjPK14AudioTimeStampjjP15AudioBufferListES2_EEN5caulk12rt_allocatorISB_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorINS_4pairIffEEN5caulk12rt_allocatorIS2_EEE16__destroy_vectorclB8ne200100Ev
+ __ZNSt3__16vectorINS_4pairIffEEN5caulk12rt_allocatorIS2_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorINS_4pairIjNS_10shared_ptrIN2AQ3API11BufferOwnerEEEEENS_9allocatorIS7_EEE16__destroy_vectorclB8ne200100Ev
+ __ZNSt3__16vectorINS_4pairIjNS_10shared_ptrIN2AQ3API11BufferOwnerEEEEENS_9allocatorIS7_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorINS_4pairIjNS_10shared_ptrIN2AQ3API11BufferOwnerEEEEENS_9allocatorIS7_EEE5clearB8ne200100Ev
+ __ZNSt3__16vectorINS_4pairIjNS_8optionalIjEEEENS_9allocatorIS4_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorINS_4pairIjNS_8optionalIjEEEENS_9allocatorIS4_EEE9push_backB8ne200100EOS4_
+ __ZNSt3__16vectorINS_5tupleIJjNS_10shared_ptrIN2AQ3API5QueueEEEEEENS_9allocatorIS7_EEE16__destroy_vectorclB8ne200100Ev
+ __ZNSt3__16vectorINS_5tupleIJjNS_10shared_ptrIN2AQ3API5QueueEEEEEENS_9allocatorIS7_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorINS_5tupleIJjNS_10shared_ptrIN2AQ3API9SubmixTapEEEEEENS_9allocatorIS7_EEE16__destroy_vectorclB8ne200100Ev
+ __ZNSt3__16vectorINS_5tupleIJjNS_10shared_ptrIN2AQ3API9SubmixTapEEEEEENS_9allocatorIS7_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorINS_5tupleIJjPFvPvP16OpaqueAudioQueuejES2_EEENS_9allocatorIS7_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorINS_8weak_ptrI8AQIONodeEENS_9allocatorIS3_EEE16__destroy_vectorclB8ne200100Ev
+ __ZNSt3__16vectorINS_8weak_ptrI8AQIONodeEENS_9allocatorIS3_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorINS_8weak_ptrIN5caulk17lifetime_observedINS_10unique_ptrI16AQMEIO_InterfaceNS_14default_deleteIS5_EEEENS2_23shared_instance_managerIS5_E8observerEEEEENS_9allocatorISD_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIP10AUNodeInfoNS_9allocatorIS2_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIP10AUNodeInfoNS_9allocatorIS2_EEE9push_backB8ne200100ERKS2_
+ __ZNSt3__16vectorIP10ClientInfoNS_9allocatorIS2_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIP10ClientInfoNS_9allocatorIS2_EEE20__throw_out_of_rangeB8ne200100Ev
+ __ZNSt3__16vectorIP11MCAudioUnitNS_9allocatorIS2_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIP11MCAudioUnitNS_9allocatorIS2_EEE9push_backB8ne200100EOS2_
+ __ZNSt3__16vectorIP11MEConnectorNS_9allocatorIS2_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIP11MEConnectorNS_9allocatorIS2_EEE9push_backB8ne200100ERKS2_
+ __ZNSt3__16vectorIP12SSSAudioDataNS_9allocatorIS2_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIP13AudioTapMixerNS_9allocatorIS2_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIP13AudioTapMixerNS_9allocatorIS2_EEE9push_backB8ne200100ERKS2_
+ __ZNSt3__16vectorIP13MESubmixGraphNS_9allocatorIS2_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIP13SequenceTrackNS_9allocatorIS2_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIP14AQIONodeClientNS_9allocatorIS2_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIP14AudioTapObjectNS_9allocatorIS2_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIP14CAExternalLockNS_9allocatorIS2_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIP14MEMixerChannelNS_9allocatorIS2_EEE16__init_with_sizeB8ne200100IPS2_S7_EEvT_T0_m
+ __ZNSt3__16vectorIP14MEMixerChannelNS_9allocatorIS2_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIP14MEMixerChannelNS_9allocatorIS2_EEE9push_backB8ne200100ERKS2_
+ __ZNSt3__16vectorIP14MixTapToUplinkNS_9allocatorIS2_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIP14__CFDictionaryNS_9allocatorIS2_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIP15InputDispatcherNS_9allocatorIS2_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIP15XProcessingBaseNS_9allocatorIS2_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIP15XProcessingBaseNS_9allocatorIS2_EEE9push_backB8ne200100EOS2_
+ __ZNSt3__16vectorIP16AudioQueueObjectNS_9allocatorIS2_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIP19MEInputStreamClientNS_9allocatorIS2_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIP19SSSActionPlayerBaseNS_9allocatorIS2_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIP19SSSActionPlayerBaseNS_9allocatorIS2_EEE9push_backB8ne200100ERKS2_
+ __ZNSt3__16vectorIP20MEOutputStreamClientNS_9allocatorIS2_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIP20MEOutputStreamClientNS_9allocatorIS2_EEE9push_backB8ne200100ERKS2_
+ __ZNSt3__16vectorIP25AQMEIO_NotificationClientNS_9allocatorIS2_EEE16__init_with_sizeB8ne200100IPS2_S7_EEvT_T0_m
+ __ZNSt3__16vectorIP25AQMEIO_NotificationClientNS_9allocatorIS2_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIP25AUNodeSequenceDestinationNS_9allocatorIS2_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIP31MIDIEndpointSequenceDestinationNS_9allocatorIS2_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIP8AQIONodeNS_9allocatorIS2_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIP8UserInfoNS_9allocatorIS2_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIP8UserInfoNS_9allocatorIS2_EEE20__throw_out_of_rangeB8ne200100Ev
+ __ZNSt3__16vectorIPK10__CFStringNS_9allocatorIS3_EEE16__init_with_sizeB8ne200100IPKS3_S9_EEvT_T0_m
+ __ZNSt3__16vectorIPKvNS_9allocatorIS2_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIPKvNS_9allocatorIS2_EEEC2B8ne200100Em
+ __ZNSt3__16vectorIPN11DSP_Routing15PublishedStreamENS_9allocatorIS3_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIPN11DSP_Routing6StreamENS_9allocatorIS3_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIPN15CAListenerProxy8ListenerENS_9allocatorIS3_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIPN15CAListenerProxy8ListenerENS_9allocatorIS3_EEE9push_backB8ne200100EOS3_
+ __ZNSt3__16vectorIPN16AudioQueueObject23ScheduledSliceAllocatorENS_9allocatorIS3_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIPN2AQ3API12OfflineMixerENS_9allocatorIS4_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIPvNS_9allocatorIS1_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorISt4byteNS_9allocatorIS1_EEEC2B8ne200100Em
+ __ZNSt3__16vectorIU8__strongP24ATAudioSessionClientImplNS_9allocatorIS3_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIU8__strongP24ATAudioSessionClientImplNS_9allocatorIS3_EEE9push_backB8ne200100ERU8__strongKS2_
+ __ZNSt3__16vectorIcN5caulk12rt_allocatorIcEEE16__destroy_vectorclB8ne200100Ev
+ __ZNSt3__16vectorIcN5caulk12rt_allocatorIcEEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIcNS_9allocatorIcEEE11__vallocateB8ne200100Em
+ __ZNSt3__16vectorIcNS_9allocatorIcEEE16__init_with_sizeB8ne200100IPcS5_EEvT_T0_m
+ __ZNSt3__16vectorIcNS_9allocatorIcEEE18__assign_with_sizeB8ne200100IPcS5_EEvT_T0_l
+ __ZNSt3__16vectorIcNS_9allocatorIcEEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIcNS_9allocatorIcEEEC2B8ne200100Em
+ __ZNSt3__16vectorIcNS_9allocatorIcEEEC2B8ne200100EmRKc
+ __ZNSt3__16vectorIfNS_9allocatorIfEEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIhNS_9allocatorIhEEE11__vallocateB8ne200100Em
+ __ZNSt3__16vectorIhNS_9allocatorIhEEE18__assign_with_sizeB8ne200100IPhS5_EEvT_T0_l
+ __ZNSt3__16vectorIhNS_9allocatorIhEEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIhNS_9allocatorIhEEEC2B8ne200100Em
+ __ZNSt3__16vectorIiNS_9allocatorIiEEE11__vallocateB8ne200100Em
+ __ZNSt3__16vectorIiNS_9allocatorIiEEE16__init_with_sizeB8ne200100IPKiS6_EEvT_T0_m
+ __ZNSt3__16vectorIiNS_9allocatorIiEEE16__init_with_sizeB8ne200100IPiS5_EEvT_T0_m
+ __ZNSt3__16vectorIiNS_9allocatorIiEEE18__assign_with_sizeB8ne200100IPKiS6_EEvT_T0_l
+ __ZNSt3__16vectorIiNS_9allocatorIiEEE18__assign_with_sizeB8ne200100IPiS5_EEvT_T0_l
+ __ZNSt3__16vectorIiNS_9allocatorIiEEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIiNS_9allocatorIiEEE9push_backB8ne200100EOi
+ __ZNSt3__16vectorIjNS_9allocatorIjEEE11__vallocateB8ne200100Em
+ __ZNSt3__16vectorIjNS_9allocatorIjEEE16__init_with_sizeB8ne200100INS_11__wrap_iterIPKjEES8_EEvT_T0_m
+ __ZNSt3__16vectorIjNS_9allocatorIjEEE16__init_with_sizeB8ne200100IPKjS6_EEvT_T0_m
+ __ZNSt3__16vectorIjNS_9allocatorIjEEE16__init_with_sizeB8ne200100IPjS5_EEvT_T0_m
+ __ZNSt3__16vectorIjNS_9allocatorIjEEE18__assign_with_sizeB8ne200100IPKjS6_EEvT_T0_l
+ __ZNSt3__16vectorIjNS_9allocatorIjEEE18__assign_with_sizeB8ne200100IPjS5_EEvT_T0_l
+ __ZNSt3__16vectorIjNS_9allocatorIjEEE18__insert_with_sizeB8ne200100INS_11__wrap_iterIPjEES7_EES7_NS5_IPKjEET_T0_l
+ __ZNSt3__16vectorIjNS_9allocatorIjEEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIjNS_9allocatorIjEEE20__throw_out_of_rangeB8ne200100Ev
+ __ZNSt3__16vectorIjNS_9allocatorIjEEE9push_backB8ne200100EOj
+ __ZNSt3__16vectorIjNS_9allocatorIjEEE9push_backB8ne200100ERKj
+ __ZNSt3__16vectorIjNS_9allocatorIjEEEC2B8ne200100Em
+ __ZNSt3__16vectorImNS_9allocatorImEEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIxNS_9allocatorIxEEE11__vallocateB8ne200100Em
+ __ZNSt3__16vectorIxNS_9allocatorIxEEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__17__sort3B8ne200100INS_17_ClassicAlgPolicyERNS_6__lessIvvEEP15MEVADIdentifierLi0EEEbT1_S7_S7_T0_
+ __ZNSt3__17__sort3B8ne200100INS_17_ClassicAlgPolicyERZN17AudioTapSpecifierC1ENS_6vectorIjNS_9allocatorIjEEEE22ATAudioTapMuteBehaviorEUlRK11AQMESessionSA_E_PS8_Li0EEEbT1_SE_SE_T0_
+ __ZNSt3__17__sort4B8ne200100INS_17_ClassicAlgPolicyERNS_6__lessIvvEEP10MusicEventLi0EEEvT1_S7_S7_S7_T0_
+ __ZNSt3__17__sort4B8ne200100INS_17_ClassicAlgPolicyERNS_6__lessIvvEEP11VolumeEventLi0EEEvT1_S7_S7_S7_T0_
+ __ZNSt3__17__sort4B8ne200100INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEELi0EEEvT1_SC_SC_SC_T0_
+ __ZNSt3__17__sort4B8ne200100INS_17_ClassicAlgPolicyERZN17AudioTapSpecifierC1ENS_6vectorIjNS_9allocatorIjEEEE22ATAudioTapMuteBehaviorEUlRK11AQMESessionSA_E_PS8_Li0EEEvT1_SE_SE_SE_T0_
+ __ZNSt3__17__sort5B8ne200100INS_17_ClassicAlgPolicyERNS_6__lessIvvEEP15MEVADIdentifierLi0EEEvT1_S7_S7_S7_S7_T0_
+ __ZNSt3__17__sort5B8ne200100INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPN14NoteOffManager11NoteOffInfoELi0EEEvT1_S8_S8_S8_S8_T0_
+ __ZNSt3__17__sort5B8ne200100INS_17_ClassicAlgPolicyERZN17AudioTapSpecifierC1ENS_6vectorIjNS_9allocatorIjEEEE22ATAudioTapMuteBehaviorEUlRK11AQMESessionSA_E_PS8_Li0EEEvT1_SE_SE_SE_SE_T0_
+ __ZNSt3__17__sort5B8ne200100INS_17_ClassicAlgPolicyERZZZN2AT11Translation19AUAsyncRendererHost9ConfigureEvENK3$_0clENS_6chrono10time_pointINS6_12steady_clockENS6_8durationIxNS_5ratioILl1ELl1000000000EEEEEEERK15AudioBufferListiENKUlRT_E_clINS_6vectorINS4_34TemporallyOrdereredAudioBufferListENS_9allocatorISM_EEEEEEDaSI_EUlRKSM_SS_E_PSM_Li0EEEvT1_SW_SW_SW_SW_T0_
+ __ZNSt3__17find_ifB8ne200100INS_11__wrap_iterIP10MusicEventEEZN13TrackIterator4SeekEdE3$_0EET_S7_S7_T0_
+ __ZNSt3__17find_ifB8ne200100INS_16reverse_iteratorINS_11__wrap_iterIP10MusicEventEEEEZN13TrackIterator4SeekEdE3$_0EET_S9_S9_T0_
+ __ZNSt3__17promiseIU8__strongP13AVAudioFormatED2Ev
+ __ZNSt3__18_IterOpsINS_17_ClassicAlgPolicyEE9iter_swapB8ne200100IRP10MusicEventS6_EEvOT_OT0_
+ __ZNSt3__18functionIFvN2AT11Translation14CallTranslator5ScopeENS2_17AudioInjectorModeEEEaSERKS7_
+ __ZNSt3__18functionIFvNS_6chrono10time_pointINS1_12steady_clockENS1_8durationIxNS_5ratioILl1ELl1000000000EEEEEEERK15AudioBufferListiEEaSERKSD_
+ __ZNSt3__18functionIFvvEEaSERKS2_
+ __ZNSt3__18optionalI14AQMEIO_BindingE7emplaceB8ne200100IJR15AQIONodeManagerRPK10__CFStringEvEERS1_DpOT_
+ __ZNSt3__18optionalI14AQMEIO_BindingEaSB8ne200100IRKS1_vEERS2_OT_
+ __ZNSt3__18optionalIN10applesauce2CF7DataRefEED1Ev
+ __ZNSt3__18optionalIN10applesauce2CF7TypeRefEED2Ev
+ __ZNSt3__18optionalIN10applesauce2CF9StringRefEED2Ev
+ __ZNSt3__18optionalIN16AudioQueueObject15InputRingBufferEED2Ev
+ __ZNSt3__18optionalIN2CA16AudioBuffersBaseEED2Ev
+ __ZNSt3__18optionalIN2CA22AudioBuffersDeprecatedEED2Ev
+ __ZNSt3__18optionalIN4swix17connection_configEEC1B8ne200100EOS3_
+ __ZNSt3__18optionalIN4swix17connection_configEED1Ev
+ __ZNSt3__18optionalIN4swix17connection_configEED2Ev
+ __ZNSt3__18optionalIN4swix6resultIJNS1_4dataEEEEEaSB8ne200100IS4_vEERS5_OT_
+ __ZNSt3__18optionalIN5caulk10concurrent25guarded_lookup_hash_tableIjP16BaseOpaqueObjectLNS2_33guarded_lookup_hash_table_optionsE0E24OpaqueObjectIdentityHashE13scoped_lookupEE7emplaceB8ne200100IJRS8_RKjEvEERS9_DpOT_
+ __ZNSt3__18optionalIN5caulk9semaphoreEE7emplaceB8ne200100IJEvEERS2_DpOT_
+ __ZNSt3__18optionalIN8audioipc18SharedAudioBuffersEE7emplaceB8ne200100IJRjNS_4spanIKNS1_14ExtendedFormatELm18446744073709551615EEENS6_IhLm18446744073709551615EEEEvEERS2_DpOT_
+ __ZNSt3__19allocatorI10MusicEventE17allocate_at_leastB8ne200100Em
+ __ZNSt3__19allocatorI11AQMESessionE17allocate_at_leastB8ne200100Em
+ __ZNSt3__19allocatorI13ChaseInstInfoE17allocate_at_leastB8ne200100Em
+ __ZNSt3__19allocatorI14MEStreamTypeIDE17allocate_at_leastB8ne200100Em
+ __ZNSt3__19allocatorI15MEVADIdentifierE17allocate_at_leastB8ne200100Em
+ __ZNSt3__19allocatorI15MeterTrackEntryE17allocate_at_leastB8ne200100Em
+ __ZNSt3__19allocatorI16AURateRampStructE17allocate_at_leastB8ne200100Em
+ __ZNSt3__19allocatorI18AudioMetadataEventE17allocate_at_leastB8ne200100Em
+ __ZNSt3__19allocatorI24AudioQueueParameterEventE17allocate_at_leastB8ne200100Em
+ __ZNSt3__19allocatorI26AQBufferCreateDestroyEventE17allocate_at_leastB8ne200100Em
+ __ZNSt3__19allocatorI26AudioObjectPropertyAddressE17allocate_at_leastB8ne200100Em
+ __ZNSt3__19allocatorI30AQProcessingNodeImmediateEventE17allocate_at_leastB8ne200100Em
+ __ZNSt3__19allocatorI32AudioSessionPropertyListenerInfoE17allocate_at_leastB8ne200100Em
+ __ZNSt3__19allocatorI9TapSourceE17allocate_at_leastB8ne200100Em
+ __ZNSt3__19allocatorIN10applesauce2CF11TypeRefPairEE17allocate_at_leastB8ne200100Em
+ __ZNSt3__19allocatorIN10applesauce2CF7TypeRefEE17allocate_at_leastB8ne200100Em
+ __ZNSt3__19allocatorIN10applesauce2CF9NumberRefEE17allocate_at_leastB8ne200100Em
+ __ZNSt3__19allocatorIN14NoteOffManager14ControlMessageEE17allocate_at_leastB8ne200100Em
+ __ZNSt3__19allocatorIN16AudioQueueObject12AQRateChangeEE17allocate_at_leastB8ne200100Em
+ __ZNSt3__19allocatorIN18AQOfflineMixerBase15StartQueueEventEE17allocate_at_leastB8ne200100Em
+ __ZNSt3__19allocatorIN21VibeToHapticConverter11SegmentInfoEE17allocate_at_leastB8ne200100Em
+ __ZNSt3__19allocatorIN2AQ6Server12RemoteClient5QueueEE17allocate_at_leastB8ne200100Em
+ __ZNSt3__19allocatorIN8TempoMap10TempoEntryEE17allocate_at_leastB8ne200100Em
+ __ZNSt3__19allocatorIN8audioipc18SharedAudioBuffers7ElementEE17allocate_at_leastB8ne200100Em
+ __ZNSt3__19allocatorINS_10shared_ptrI9TapSubmixEEE17allocate_at_leastB8ne200100Em
+ __ZNSt3__19allocatorINS_10shared_ptrIN10AQMEIO_HAL8IOStreamEEEE17allocate_at_leastB8ne200100Em
+ __ZNSt3__19allocatorINS_10unique_ptrI11IAQMEDeviceNS_14default_deleteIS2_EEEEE17allocate_at_leastB8ne200100Em
+ __ZNSt3__19allocatorINS_10unique_ptrIN18PowerUsageWatchdog12ClientLoggerENS_14default_deleteIS3_EEEEE17allocate_at_leastB8ne200100Em
+ __ZNSt3__19allocatorINS_12basic_stringIcNS_11char_traitsIcEENS0_IcEEEEE17allocate_at_leastB8ne200100Em
+ __ZNSt3__19allocatorINS_4pairIN2OS2CF6StringEN10applesauce8dispatch2v15blockIFv13CAOrientationEEEEEE17allocate_at_leastB8ne200100Em
+ __ZNSt3__19allocatorINS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS0_IcEEEES6_EEE17allocate_at_leastB8ne200100Em
+ __ZNSt3__19allocatorINS_5tupleIJjPFvPvP16OpaqueAudioQueuejES2_EEEE17allocate_at_leastB8ne200100Em
+ __ZNSt3__19allocatorIP10AUNodeInfoE17allocate_at_leastB8ne200100Em
+ __ZNSt3__19allocatorIP11MCAudioUnitE17allocate_at_leastB8ne200100Em
+ __ZNSt3__19allocatorIP11MEConnectorE17allocate_at_leastB8ne200100Em
+ __ZNSt3__19allocatorIP14AQIONodeClientE17allocate_at_leastB8ne200100Em
+ __ZNSt3__19allocatorIP14MEMixerChannelE17allocate_at_leastB8ne200100Em
+ __ZNSt3__19allocatorIP15InputDispatcherE17allocate_at_leastB8ne200100Em
+ __ZNSt3__19allocatorIP15XProcessingBaseE17allocate_at_leastB8ne200100Em
+ __ZNSt3__19allocatorIP19SSSActionPlayerBaseE17allocate_at_leastB8ne200100Em
+ __ZNSt3__19allocatorIP20MEOutputStreamClientE17allocate_at_leastB8ne200100Em
+ __ZNSt3__19allocatorIP25AQMEIO_NotificationClientE17allocate_at_leastB8ne200100Em
+ __ZNSt3__19allocatorIPKvE17allocate_at_leastB8ne200100Em
+ __ZNSt3__19allocatorIPN5boost8functionIFNS1_3msm4back11HandledEnumEvEEEE17allocate_at_leastB8ne200100Em
+ __ZNSt3__19allocatorIPNS_4pairIN5boost8functionIFNS2_3msm4back11HandledEnumEvEEEbEEE17allocate_at_leastB8ne200100Em
+ __ZNSt3__19allocatorIPjE17allocate_at_leastB8ne200100Em
+ __ZNSt3__19allocatorIPmE17allocate_at_leastB8ne200100Em
+ __ZNSt3__19allocatorIfE17allocate_at_leastB8ne200100Em
+ __ZNSt3__19allocatorIiE17allocate_at_leastB8ne200100Em
+ __ZNSt3__19allocatorIjE17allocate_at_leastB8ne200100Em
+ __ZNSt3__19allocatorImE17allocate_at_leastB8ne200100Em
+ __ZNSt3__19allocatorIxE17allocate_at_leastB8ne200100Em
+ __ZNSt3__19remove_ifB8ne200100INS_11__wrap_iterIPNS_8weak_ptrIN5caulk17lifetime_observedINS_10unique_ptrI16AQMEIO_InterfaceNS_14default_deleteIS6_EEEENS3_23shared_instance_managerIS6_E8observerEEEEEEEZNSB_14remove_expiredEvEUlRKT_E_EESH_SH_SH_T0_
+ __ZNSt3__1plB8ne200100IcNS_11char_traitsIcEENS_9allocatorIcEEEENS_12basic_stringIT_T0_T1_EEOS9_PKS6_
+ __ZNSt3__1plB8ne200100IcNS_11char_traitsIcEENS_9allocatorIcEEEENS_12basic_stringIT_T0_T1_EEPKS6_OS9_
+ __ZNSt3__1ssB8ne200100IcNS_11char_traitsIcEENS_9allocatorIcEEEEDaRKNS_12basic_stringIT_T0_T1_EESC_
+ __ZSt17__throw_bad_allocv
+ __ZSt17current_exceptionv
+ __ZSt17rethrow_exceptionSt13exception_ptr
+ __ZSt19uncaught_exceptionsv
+ __ZSt28__throw_bad_array_new_lengthB8ne200100v
+ __ZTINSt3__112future_errorE
+ __ZTSNSt3__112future_errorE
+ __ZTV10AQMEWaiter
+ __ZTV13MESubmixGraph
+ __ZTV14MixTapToUplink
+ __ZTV16RTCountedDataRef
+ __ZTV16TArrayMarshallerIyE
+ __ZTV17AQMECaptureInsert
+ __ZTV17IONodeSessionStub
+ __ZTV17TCFDictionaryBase
+ __ZTV18MCSpatialAudioUnit
+ __ZTV18RemoteIOServerBase
+ __ZTV18TCFDictionary_CF2CIPK10__CFStringPN18AQConverterManager17AQConverterThreadEE
+ __ZTV19IONodeSessionLegacy
+ __ZTV21ScheduledSlicePlayer2
+ __ZTV24AVVoiceTriggerServerImpl
+ __ZTV24MEEnhanceableSubmixGraph
+ __ZTV27ScheduledSlicePlayer_Legacy
+ __ZTVN21ScheduledSlicePlayer220XScheduledAudioSliceE
+ __ZTVN27ScheduledSlicePlayer_Legacy20XScheduledAudioSliceE
+ __ZTVN2AT11Translation13AudioInjectorE
+ __ZTVN2AT11Translation18CallTranslatorBaseE
+ __ZTVN2AT11Translation21AudioStreamTranslatorE
+ __ZTVN2AT11Translation24AudioTranslationInjectorE
+ __ZTVN2AT11Translation25AsyncAudioStreamProcessorE
+ __ZTVN2AT11Translation27TranslationFeedbackInjectorE
+ __ZTVN2AT17AudioTapClientHALE
+ __ZTVN5caulk10concurrent7details12message_callIRZN11ClientEntry19handleSequenceEndedEmNS_16inplace_functionIFvmELm32ELm8ENS_23inplace_function_detail6vtableEEEE3$_0JEEE
+ __ZTVN5caulk10concurrent7details15rt_message_callIRZN11ClientEntry19handleSequenceEndedEmNS_16inplace_functionIFvmELm32ELm8ENS_23inplace_function_detail6vtableEEEE3$_0JEEE
+ __ZTVNSt3__110__function6__funcIN5caulk16inplace_functionIFvmELm32ELm8ENS2_23inplace_function_detail6vtableEEENS_9allocatorIS7_EES4_EE
+ __ZTVNSt3__110__function6__funcINS_6__bindIMN2AT11Translation14CallTranslatorEFvNS5_5ScopeENS4_17AudioInjectorModeEEJPS5_RKNS_12placeholders4__phILi1EEERKNSC_ILi2EEEEEENS_9allocatorISJ_EEFvS6_S7_EEE
+ __ZTVNSt3__110__function6__funcINS_6__bindIMN2AT11Translation24AudioTranslationInjectorEFvvEJPS5_EEENS_9allocatorIS9_EEFvvEEE
+ __ZTVNSt3__110__function6__funcINS_6__bindIRFN5caulk8expectedINS_10unique_ptrIN14MixTapToUplink19TappedAudioProducerENS_14default_deleteIS7_EEEEiEERKN2CA17StreamDescriptionERKNSC_13ChannelLayoutEiRKNS_13unordered_setIjNS_4hashIjEENS_8equal_toIjEENS_9allocatorIjEEEEEJRKNS_12placeholders4__phILi1EEERKNSW_ILi2EEERKNSW_ILi3EEERKNSW_ILi4EEEEEENSO_IS19_EEST_EE
+ __ZTVNSt3__110__function6__funcINS_6__bindIRFN5caulk8expectedINS_10unique_ptrIN2AT11Translation25AsyncAudioStreamProcessorENS_14default_deleteIS8_EEEEiEENS7_14CallTranslator5ScopeERKNS7_24TranslationConfigurationEEJRKNS_12placeholders4__phILi1EEERKNSL_ILi2EEEEEENS_9allocatorISS_EESI_EE
+ __ZTVNSt3__110__function6__funcINS_6__bindIRFNS_13unordered_mapIjiNS_4hashIjEENS_8equal_toIjEENS_9allocatorINS_4pairIKjiEEEEEEvEJEEENS8_ISG_EESE_EE
+ __ZTVNSt3__110__function6__funcIZ24AQMEIOManager_FindIOUnitRK14AQMEIO_BindingE3$_0NS_9allocatorIS5_EEFNS_10unique_ptrI16AQMEIO_InterfaceNS_14default_deleteIS9_EEEES4_RiEEE
+ __ZTVNSt3__110__function6__funcIZ25AudioSessionSetCMPropertyE3$_1NS_9allocatorIS2_EEFNS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS3_IcEEEESA_EEN10applesauce2CF7TypeRefESE_EEE
+ __ZTVNSt3__110__function6__funcIZ27TranslateCMSessionErrorCodePKcRKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEiiE3$_1NS7_ISC_EEFNS_4pairIS9_S9_EEN10applesauce2CF7TypeRefESI_EEE
+ __ZTVNSt3__110__function6__funcIZ29SystemSoundServerPlayActionIDE3$_1NS_9allocatorIS2_EEFvvEEE
+ __ZTVNSt3__110__function6__funcIZ62-[AVHapticServer incrementRunningCountForAudio:haptics:entry:]E3$_3NS_9allocatorIS2_EEFivEEE
+ __ZTVNSt3__110__function6__funcIZN10AQMEIO_HAL13UpdateStreamsEvE3$_0NS_9allocatorIS3_EEFbRK26AudioObjectPropertyAddressEEE
+ __ZTVNSt3__110__function6__funcIZN11ClientEntry17doPrepareSequenceENS_10shared_ptrI14HapticSequenceEEN5caulk16inplace_functionIFvmELm32ELm8ENS6_23inplace_function_detail6vtableEEEE3$_0NS_9allocatorISC_EES8_EE
+ __ZTVNSt3__110__function6__funcIZN13MESubmixGraph19attach1MixerChannelEP14MEMixerChannelE3$_0NS_9allocatorIS5_EEFvvEEE
+ __ZTVNSt3__110__function6__funcIZN13ServerManager12DoRenderProcERK14AudioTimeStampjE3$_0NS_9allocatorIS6_EEFKNS2_12SynthCommandEvEEE
+ __ZTVNSt3__110__function6__funcIZN14DSP_Routing_VP28SetCallTranslationPropertiesEPK14__CFDictionaryRbE3$_0NS_9allocatorIS7_EEFvvEEE
+ __ZTVNSt3__110__function6__funcIZN15AQMixEngine_VAD17maintainVADevicesEbE3$_0NS_9allocatorIS3_EEFbR14AQIONodeClientEEE
+ __ZTVNSt3__110__function6__funcIZN15AQMixEngine_VAD28routeSupportsEnhanceDialogueEvE3$_0NS_9allocatorIS3_EEFvR11IAQMEDeviceEEE
+ __ZTVNSt3__110__function6__funcIZN15AQMixEngine_VAD31IsOwnerOfAudioObject_DeprecatedEjEUlR11IAQMEDeviceE_NS_9allocatorIS5_EEFvS4_EEE
+ __ZTVNSt3__110__function6__funcIZN15AQMixEngine_VAD37SetAudioObjectPropertyData_DeprecatedEjRK26AudioObjectPropertyAddressjPKvjS7_EUlR11IAQMEDeviceE_NS_9allocatorISA_EEFvS9_EEE
+ __ZTVNSt3__110__function6__funcIZN16AQMixEngine_Base12maintainTapsEbEUlR11IAQMEDeviceE_NS_9allocatorIS5_EEFvS4_EEE
+ __ZTVNSt3__110__function6__funcIZN16AQMixEngine_Base13silenceOutputERK11AQMESessionjEUlR11IAQMEDeviceE_NS_9allocatorIS8_EEFvS7_EEE
+ __ZTVNSt3__110__function6__funcIZN16AQMixEngine_Base14DebugPrintFromEP7__sFILEPKcE3$_0NS_9allocatorIS7_EEFvR11IAQMEDeviceEEE
+ __ZTVNSt3__110__function6__funcIZN16AQMixEngine_Base16StopFreewheelingEvEUlR11IAQMEDeviceE_NS_9allocatorIS5_EEFvS4_EEE
+ __ZTVNSt3__110__function6__funcIZN16AQMixEngine_Base17SoundCheckChangedEvEUlR11IAQMEDeviceE_NS_9allocatorIS5_EEFvS4_EEE
+ __ZTVNSt3__110__function6__funcIZN16AQMixEngine_Base18setDynamicsEnabledE15EDynamicsEnableEUlR11IAQMEDeviceE_NS_9allocatorIS6_EEFvS5_EEE
+ __ZTVNSt3__110__function6__funcIZN16AQMixEngine_Base22updateTapsForSessionIDEjEUlR11IAQMEDeviceE_NS_9allocatorIS5_EEFvS4_EEE
+ __ZTVNSt3__110__function6__funcIZN16AQMixEngine_Base23MonoAudioSettingChangedEvEUlR11IAQMEDeviceE_NS_9allocatorIS5_EEFvS4_EEE
+ __ZTVNSt3__110__function6__funcIZN16AQMixEngine_Base25AccessibilityPrefsChangedEvEUlR11IAQMEDeviceE_NS_9allocatorIS5_EEFvS4_EEE
+ __ZTVNSt3__110__function6__funcIZN16AQMixEngine_Base25ScreenSharingStateChangedEyEUlR11IAQMEDeviceE_NS_9allocatorIS5_EEFvS4_EEE
+ __ZTVNSt3__110__function6__funcIZN16AQMixEngine_Base27DistributeProcessorPropertyE13MEProcessorIDjRjPvEUlR11IAQMEDeviceE_NS_9allocatorIS8_EEFvS7_EEE
+ __ZTVNSt3__110__function6__funcIZN16AQMixEngine_Base29RestartIOFollowingRouteChangeEvEUlR11IAQMEDeviceE_NS_9allocatorIS5_EEFvS4_EEE
+ __ZTVNSt3__110__function6__funcIZN17LegacyHapticSynth19handleRunModeChangeEjE3$_0NS_9allocatorIS3_EEFivEEE
+ __ZTVNSt3__110__function6__funcIZN21AVVoiceTriggerManager10InitializeEvE3$_0NS_9allocatorIS3_EEFbjRKN15CAListenerProxy15HALNotificationEEEE
+ __ZTVNSt3__110__function6__funcIZN22MultiOutputHapticSynth12startRunningEbbjNS_8functionIFivEEEjE3$_0NS_9allocatorIS6_EES4_EE
+ __ZTVNSt3__110__function6__funcIZN22MultiOutputHapticSynth19handleRunModeChangeEjE3$_0NS_9allocatorIS3_EEFivEEE
+ __ZTVNSt3__110__function6__funcIZN24AVVoiceTriggerServerImpl27enableVoiceTriggerListeningEbbU13block_pointerFvP7NSErrorEEUljRKN15CAListenerProxy15HALNotificationEE_NS_9allocatorISB_EEFbjSA_EEE
+ __ZTVNSt3__110__function6__funcIZN24AVVoiceTriggerServerImpl31updateVoiceTriggerConfigurationEPK14__CFDictionaryU13block_pointerFvP7NSErrorEEUljRKN15CAListenerProxy15HALNotificationEE_NS_9allocatorISE_EEFbjSD_EEE
+ __ZTVNSt3__110__function6__funcIZN24AVVoiceTriggerServerImpl40registerStateChangedNotificationHandlersEbEUljRKN15CAListenerProxy15HALNotificationEE_NS_9allocatorIS7_EEFbjS6_EEE
+ __ZTVNSt3__110__function6__funcIZN24AVVoiceTriggerServerImpl42registerAOPVoiceTriggerNotificationHandlerEjbEUljRKN15CAListenerProxy15HALNotificationEE_NS_9allocatorIS7_EEFbjS6_EEE
+ __ZTVNSt3__110__function6__funcIZN24AVVoiceTriggerServerImpl43registerAOPEnableChangedNotificationHandlerEbEUljRKN15CAListenerProxy15HALNotificationEE_NS_9allocatorIS7_EEFbjS6_EEE
+ __ZTVNSt3__110__function6__funcIZN2AQ3API7ManagerC1EbRNS3_11CaptureBaseEN5caulk19lifetime_erased_ptrI23AudioQueueXPC_InterfaceEEE3$_0NS_9allocatorISB_EEFvRN4swix12ipc_endpointERKN10applesauce3xpc6objectEEEE
+ __ZTVNSt3__110__function6__funcIZN2AQ3API7ManagerC1EbRNS3_11CaptureBaseEN5caulk19lifetime_erased_ptrI23AudioQueueXPC_InterfaceEEE3$_1NS_9allocatorISB_EEFiN10applesauce3xpc6objectEEEE
+ __ZTVNSt3__110__function6__funcIZN2AT11Translation19AUAsyncRendererHost9ConfigureEvE3$_0NS_9allocatorIS5_EEFvNS_6chrono10time_pointINS8_12steady_clockENS8_8durationIxNS_5ratioILl1ELl1000000000EEEEEEERK15AudioBufferListiEEE
+ __ZTVNSt3__110__function6__funcIZN30AudioSessionPropertyMarshaller15GetPropertyInfoEjE5$_127NS_9allocatorIS3_EEFP10MarshallervEEE
+ __ZTVNSt3__110__function6__funcIZZN13MESubmixGraph19attach1MixerChannelEP14MEMixerChannelENK3$_1clI9TapSubmixEEDaRT_EUlvE_NS_9allocatorISB_EEFvvEEE
+ __ZTVNSt3__110__function6__funcIZZN14RemoteIOClient20IONode_FormatChangedEjEUb_E3$_1NS_9allocatorIS3_EEFvvEEE
+ __ZTVNSt3__110__function6__funcIZZN22MultiOutputHapticSynth11stopRunningEbbjENK3$_0clERNS_10unique_ptrI11SynthOutputNS_14default_deleteIS5_EEEEEUlvE_NS_9allocatorISA_EEFvvEEE
+ __ZTVNSt3__112future_errorE
+ __ZTVNSt3__113__assoc_stateIU8__strongP13AVAudioFormatEE
+ __ZTVNSt3__115basic_streambufIcNS_11char_traitsIcEEEE
+ __ZTVNSt3__117__assoc_sub_stateE
+ __ZTVNSt3__120__shared_ptr_emplaceI14MixTapToUplinkNS_9allocatorIS1_EEEE
+ __ZTVNSt3__120__shared_ptr_emplaceI16MCProcessingNodeNS_9allocatorIS1_EEEE
+ __ZTVNSt3__120__shared_ptr_emplaceIN5caulk12synchronizedIN2AQ6Server16ProcessingTapIPCENS1_22pooled_semaphore_mutexENS1_22empty_atomic_interfaceIS5_EEEENS_9allocatorIS9_EEEE
+ __ZTVNSt3__120__shared_ptr_emplaceIN5caulk7details19lifetime_guard_baseIN2AT11Translation16TranslatorClientEE13control_blockENS_9allocatorIS8_EEEE
+ __ZTVNSt3__120__shared_ptr_pointerIPN2AT11Translation14CallTranslatorENS_10shared_ptrIS3_E27__shared_ptr_default_deleteIS3_S3_EENS_9allocatorIS3_EEEE
+ __ZTVNSt3__120__shared_ptr_pointerIPxZN14MixTapToUplink16AQMETapConnector22getCAReporterIDForCallEvEUlS1_E_NS_9allocatorIxEEEE
+ __ZThn176_N14RemoteIOServerD0Ev
+ __ZThn176_N14RemoteIOServerD1Ev
+ __ZThn272_N16AudioQueueObject18ToAudioQueueObjectEv
+ __ZThn272_N16AudioQueueObjectD0Ev
+ __ZThn272_N16AudioQueueObjectD1Ev
+ __ZThn272_N17ZenAQIONodeClient11PrintObjectEP7__sFILE
+ __ZThn272_N17ZenAQIONodeClientD0Ev
+ __ZThn272_N17ZenAQIONodeClientD1Ev
+ __ZThn288_N16AudioQueueObject21SSP_StartTimeResolvedEx15XAudioTimeStamp
+ __ZThn288_N16AudioQueueObject30SSP_ScaledToUnscaledSampleTimeEx
+ __ZThn288_N16AudioQueueObjectD0Ev
+ __ZThn288_N16AudioQueueObjectD1Ev
+ __ZThn392_N14AQOfflineMixer11PrintObjectEP7__sFILE
+ __ZThn392_N14AQOfflineMixerD0Ev
+ __ZThn392_N14AQOfflineMixerD1Ev
+ __ZThn48_N15AudioQueueOwner11PrintObjectEP7__sFILE
+ __ZThn48_N15AudioQueueOwnerD0Ev
+ __ZThn48_N15AudioQueueOwnerD1Ev
+ __ZThn48_N18MCSpatialAudioUnit19setSpatialParameterE35SpatialExperienceRenderingParameterPKvj
+ __ZThn48_N18MCSpatialAudioUnitD0Ev
+ __ZThn48_N18MCSpatialAudioUnitD1Ev
+ __ZThn8_N14MEMixerChannel11SetSTSLabelERKN10applesauce2CF9StringRefEb
+ __ZThn8_N14MEMixerChannel17AddProcessingNodeER16AQProcessingNode
+ __ZThn96_N14RemoteIOServer10ClientDiedEPN12CADeprecated11XMachServer6ClientE
+ __ZThn96_N14RemoteIOServerD0Ev
+ __ZThn96_N14RemoteIOServerD1Ev
+ __ZZ12gEDSubmixLogvE6global
+ __ZZ15gEDProcessorLogvE6global
+ __ZZ17initAQMEMessengervE9onceToken
+ __ZZ20gEDParallelSubmixLogvE6global
+ __ZZ21IONodeSessionLogScopevE6global
+ __ZZ32AQMEIOManager_FindOrCreateIOUnitRK14AQMEIO_BindingR13IOUnitCreatorE15sharedInstances
+ __ZZL12logSubsystemvE5scope
+ __ZZL12logSubsystemvE8onceflag
+ __ZZL13GetAcousticIDvE13optionalValue.5356
+ __ZZL13GetAcousticIDvENKUlvE_clEv.5355
+ __ZZL15CPMSLibraryCorePPcE16frameworkLibrary.0.10449
+ __ZZL15CPMSLibraryCorePPcE16frameworkLibrary.0.3477
+ __ZZL15CPMSLibraryCorePPcE16frameworkLibrary.0.6303
+ __ZZL17getCPMSAgentClassvE9softClass.0.3449
+ __ZZL17getCPMSAgentClassvE9softClass.0.6301
+ __ZZL19AVFAudioLibraryCorePPcE16frameworkLibrary.0.12629
+ __ZZL20CoreMediaLibraryCorePPcE16frameworkLibrary.0.5036
+ __ZZL20CoreMediaLibraryCorePPcE16frameworkLibrary.0.7060
+ __ZZL21GetSpatialMetadataSPIvE19sSpatialMetadataSPI
+ __ZZL21GetSpatialMetadataSPIvE19sSpatialMetadataSPI.11535
+ __ZZL21GetSpatialMetadataSPIvE23sSpatialMetadataSPIOnce
+ __ZZL21GetSpatialMetadataSPIvE23sSpatialMetadataSPIOnce.11534
+ __ZZL21getAVAudioFormatClassvE9softClass.0.11882
+ __ZZL23MediaToolboxLibraryCorePPcE16frameworkLibrary.0.7052
+ __ZZL24getAVAudioPCMBufferClassvE9softClass.0
+ __ZZL26ACQContextAssertionEnabledvE7enabled
+ __ZZL27getRBSProcessPredicateClassvE9softClass.0
+ __ZZL28SpeechTranslationLibraryCorePPcE16frameworkLibrary.0
+ __ZZL29AudioSessionServerLibraryCorePPcE16frameworkLibrary.0.8295
+ __ZZL29getCPMSClientDescriptionClassvE9softClass.0.3458
+ __ZZL30gAudioTapHALReferenceStreamLogvE6global
+ __ZZL32getSTSpeechTranslatorClientClassvE9softClass.0
+ __ZZL33getCMBaseObjectGetVTableSymbolLocvE3ptr.0.5032
+ __ZZL33getCMBaseObjectGetVTableSymbolLocvE3ptr.0.7057
+ __ZZL58getFigCPECryptorCreateCryptorFromSerializedRecipeSymbolLocvE3ptr.0.7048
+ __ZZN13ServerManager16playAlertPatternENSt3__110shared_ptrI11ClientEntryEEPKvfP20SSPlayerSynchronizerjU13block_pointerFvvEEN3$_0D1Ev
+ __ZZN14DSP_Routing_VP28SetCallTranslationPropertiesEPK14__CFDictionaryRbENK3$_1clEv
+ __ZZN14MEMixerChannel33ConfigureLMLoudnessNormalizerUnitERKN2CA17StreamDescriptionEE27kLMLoudnessNormalizerParams
+ __ZZN14MixTapToUplinkC1ERKN2CA17StreamDescriptionERKNS0_13ChannelLayoutEE5gOnce
+ __ZZN15AQMixEngine_VAD17maintainVADevicesEbENK3$_3clER11IAQMEDeviceR17MEConnectorVector
+ __ZZN16AQMixEngine_Base14DebugPrintFromEP7__sFILEPKcE14sLogEntryIndex
+ __ZZN16AQMixEngine_Base14DebugPrintFromEP7__sFILEPKcE5mutex
+ __ZZN18SlicePlayerFactory8instanceEvE7factory.0
+ __ZZN20CA_UISoundClientBaseC1EdjPK14__CFDictionaryjN10applesauce2CF7TypeRefEibE11gSRCQuality
+ __ZZN20CA_UISoundClientBaseC1EdjPK14__CFDictionaryjN10applesauce2CF7TypeRefEibE6inited
+ __ZZN20CA_UISoundClientBaseC1EdjPK14__CFDictionaryjN10applesauce2CF7TypeRefEibE8onceflag
+ __ZZN21AVVoiceTriggerManager10InitializeEvENK3$_1clEv
+ __ZZN21AVVoiceTriggerManager18hasVoiceTriggerXPCEvE4once
+ __ZZN21AVVoiceTriggerManager8instanceEvE8instance
+ __ZZN22MultiOutputHapticSynth11stopRunningEbbjENK3$_2clERNSt3__110unique_ptrI11SynthOutputNS1_14default_deleteIS3_EEEE
+ __ZZN24AVVoiceTriggerServerImpl17enableBargeInModeEbU13block_pointerFvP7NSErrorEE6sCount
+ __ZZN24AVVoiceTriggerServerImpl33fetchHardwareSupportsVoiceTriggerEvE9checkonce
+ __ZZN29AudioSessionPropertyListeners13GetStateMutexEvE6global
+ __ZZN2AQ3API9SubmixTap41CreateDestinationAQProcessingTap_CMClientEP29OpaqueAudioQueueProcessingTapEN3$_08__invokeEPvS3_jP14AudioTimeStampPjS8_P15AudioBufferList
+ __ZZN2AT11Translation16TranslatorClientC1ERNS0_21AudioStreamTranslatorERKNS0_24TranslationConfigurationEE5gOnce
+ __ZZN2AT11Translation18CallTranslatorBase17injectable_globalEvE16injectableGlobal
+ __ZZN2AT11Translation18CallTranslatorBase17injectable_globalEvEN3$_08__invokeEv
+ __ZZN2AT11Translation24TranslationConfiguration6CreateEPK14__CFDictionaryE4once
+ __ZZN2AT13SessionFacadeL34PopulateSourceFormatInfoDictionaryEP14__CFDictionaryPKvRK14AQIONodeClientRN2CA17StreamDescriptionEbbbE10sessionMap
+ __ZZN5caulk23inplace_function_detail6vtableIvJmEEC1EvENUlPvE_8__invokeES3_
+ __ZZN5caulk23inplace_function_detail6vtableIvJmEEC1EvENUlPvOmE_8__invokeES3_S4_
+ __ZZN5caulk23inplace_function_detail6vtableIvJmEEC1EvENUlPvS3_E0_8__invokeES3_S3_
+ __ZZN5caulk23inplace_function_detail6vtableIvJmEEC1EvENUlPvS3_E_8__invokeES3_S3_
+ __ZZN5caulk23inplace_function_detail6vtableIvJmEEC1INSt3__18functionIFvmEEEEENS0_7wrapperIT_EEENUlPvE_8__invokeESB_
+ __ZZN5caulk23inplace_function_detail6vtableIvJmEEC1INSt3__18functionIFvmEEEEENS0_7wrapperIT_EEENUlPvOmE_8__invokeESB_SC_
+ __ZZN5caulk23inplace_function_detail6vtableIvJmEEC1INSt3__18functionIFvmEEEEENS0_7wrapperIT_EEENUlPvSB_E0_8__invokeESB_SB_
+ __ZZN5caulk23inplace_function_detail6vtableIvJmEEC1INSt3__18functionIFvmEEEEENS0_7wrapperIT_EEENUlPvSB_E_8__invokeESB_SB_
+ __ZZN5caulk23inplace_function_detail6vtableIvJmEEC1IZ54-[AVHapticServerInstance prepareHapticSequence:reply:]E3$_1EENS0_7wrapperIT_EEENUlPvE_8__invokeES8_
+ __ZZN5caulk23inplace_function_detail6vtableIvJmEEC1IZ54-[AVHapticServerInstance prepareHapticSequence:reply:]E3$_1EENS0_7wrapperIT_EEENUlPvOmE_8__invokeES8_S9_
+ __ZZN5caulk23inplace_function_detail6vtableIvJmEEC1IZ54-[AVHapticServerInstance prepareHapticSequence:reply:]E3$_1EENS0_7wrapperIT_EEENUlPvS8_E0_8__invokeES8_S8_
+ __ZZN5caulk23inplace_function_detail6vtableIvJmEEC1IZ54-[AVHapticServerInstance prepareHapticSequence:reply:]E3$_1EENS0_7wrapperIT_EEENUlPvS8_E_8__invokeES8_S8_
+ __ZZN5caulk23inplace_function_detail6vtableIvJmEEC1IZN13ServerManager16playAlertPatternENSt3__110shared_ptrI11ClientEntryEEPKvfP20SSPlayerSynchronizerjU13block_pointerFvvEE3$_0EENS0_7wrapperIT_EEENUlPvE_8__invokeESJ_
+ __ZZN5caulk23inplace_function_detail6vtableIvJmEEC1IZN13ServerManager16playAlertPatternENSt3__110shared_ptrI11ClientEntryEEPKvfP20SSPlayerSynchronizerjU13block_pointerFvvEE3$_0EENS0_7wrapperIT_EEENUlPvOmE_8__invokeESJ_SK_
+ __ZZN5caulk23inplace_function_detail6vtableIvJmEEC1IZN13ServerManager16playAlertPatternENSt3__110shared_ptrI11ClientEntryEEPKvfP20SSPlayerSynchronizerjU13block_pointerFvvEE3$_0EENS0_7wrapperIT_EEENUlPvSJ_E0_8__invokeESJ_SJ_
+ __ZZN5caulk23inplace_function_detail6vtableIvJmEEC1IZN13ServerManager16playAlertPatternENSt3__110shared_ptrI11ClientEntryEEPKvfP20SSPlayerSynchronizerjU13block_pointerFvvEE3$_0EENS0_7wrapperIT_EEENUlPvSJ_E_8__invokeESJ_SJ_
+ __ZZN5caulk23inplace_function_detail9rt_vtableIvJRKNS_10concurrent7details13skiplist_nodeIPvNS_5alloc6detail13tracked_blockEE9layout_vkEEEC1EvENUlS5_E_8__invokeES5_
+ __ZZN5caulk23inplace_function_detail9rt_vtableIvJRKNS_10concurrent7details13skiplist_nodeIPvNS_5alloc6detail13tracked_blockEE9layout_vkEEEC1EvENUlS5_S5_E0_8__invokeES5_S5_
+ __ZZN5caulk23inplace_function_detail9rt_vtableIvJRKNS_10concurrent7details13skiplist_nodeIPvNS_5alloc6detail13tracked_blockEE9layout_vkEEEC1EvENUlS5_S5_E_8__invokeES5_S5_
+ __ZZN5caulk23inplace_function_detail9rt_vtableIvJRKNS_10concurrent7details13skiplist_nodeIPvNS_5alloc6detail13tracked_blockEE9layout_vkEEEC1EvENUlS5_SC_E_8__invokeES5_SC_
+ __ZZNK15AQMixEngine_VAD24includeDeviceInSystemTapERK11IAQMEDeviceENK3$_0clEjRj
+ __ZZZN2AT11Translation18CallTranslatorBase17injectable_globalEvENK3$_0clEvE4impl
+ ___100-[AVHapticServer(VibeSynthEngine) playVibePattern:gain:synchronizer:flags:atTime:completionHandler:]_block_invoke.321
+ ___100-[AVHapticServer(VibeSynthEngine) playVibePattern:gain:synchronizer:flags:atTime:completionHandler:]_block_invoke.324
+ ___22-[AVHapticServer init]_block_invoke.377
+ ___27-[ATBlurMixer processBlock]_block_invoke
+ ___27-[ATBlurMixer processBlock]_block_invoke_2
+ ___28-[AVVoiceTriggerServer init]_block_invoke
+ ___41-[AVVoiceTriggerServer portsActiveReply:]_block_invoke
+ ___48-[AVVoiceTriggerServer speakerStateActiveReply:]_block_invoke
+ ___52-[AVVoiceTriggerServerHysteresisNotifier sendState:]_block_invoke
+ ___53-[AVHapticServer listener:shouldAcceptNewConnection:]_block_invoke.451
+ ___53-[AVHapticServer listener:shouldAcceptNewConnection:]_block_invoke.455
+ ___53-[AVHapticServer listener:shouldAcceptNewConnection:]_block_invoke.456
+ ___53-[AVVoiceTriggerServer enableListeningOnPorts:reply:]_block_invoke
+ ___53-[AVVoiceTriggerServer siriClientRecordStateChanged:]_block_invoke
+ ___58-[AVVoiceTriggerServer enableSpeakerStateListening:reply:]_block_invoke
+ ___59-[AVVoiceTriggerServer listener:shouldAcceptNewConnection:]_block_invoke
+ ___59-[AVVoiceTriggerServer listener:shouldAcceptNewConnection:]_block_invoke.169
+ ___59-[AVVoiceTriggerServer listener:shouldAcceptNewConnection:]_block_invoke.170
+ ___59-[AVVoiceTriggerServer listener:shouldAcceptNewConnection:]_block_invoke_2
+ ___59-[AVVoiceTriggerServer listener:shouldAcceptNewConnection:]_block_invoke_2.171
+ ___62-[AVVoiceTriggerServerPortManager notifyStateChanged:onQueue:]_block_invoke
+ ___62-[AVVoiceTriggerServerPortManager notifyStateChanged:onQueue:]_block_invoke_2
+ ___65-[AVHapticServerInstance setupAudioSessionFromID:isShared:error:]_block_invoke.40
+ ___72-[AVVoiceTriggerServer sendVoiceTriggerOccuredNotification:triggerTime:]_block_invoke
+ ___Block_byref_object_copy_.11998
+ ___Block_byref_object_copy_.12713
+ ___Block_byref_object_copy_.14135
+ ___Block_byref_object_copy_.1724
+ ___Block_byref_object_copy_.1861
+ ___Block_byref_object_copy_.3638
+ ___Block_byref_object_copy_.4323
+ ___Block_byref_object_copy_.5672
+ ___Block_byref_object_copy_.7388
+ ___Block_byref_object_dispose_.11999
+ ___Block_byref_object_dispose_.12714
+ ___Block_byref_object_dispose_.14136
+ ___Block_byref_object_dispose_.1725
+ ___Block_byref_object_dispose_.1862
+ ___Block_byref_object_dispose_.3639
+ ___Block_byref_object_dispose_.4324
+ ___Block_byref_object_dispose_.5673
+ ___Block_byref_object_dispose_.7389
+ ____Z16NewAudioCapturer20AudioCapturerOptionsPKcS1_jPK27AudioStreamBasicDescriptionRS3__block_invoke.12560
+ ____Z16NewAudioCapturer20AudioCapturerOptionsPKcS1_jPK27AudioStreamBasicDescriptionRS3__block_invoke.12699
+ ____Z16NewAudioCapturer20AudioCapturerOptionsPKcS1_jPK27AudioStreamBasicDescriptionRS3__block_invoke.12849
+ ____Z16NewAudioCapturer20AudioCapturerOptionsPKcS1_jPK27AudioStreamBasicDescriptionRS3__block_invoke.13769
+ ____Z16NewAudioCapturer20AudioCapturerOptionsPKcS1_jPK27AudioStreamBasicDescriptionRS3__block_invoke.2028
+ ____Z16NewAudioCapturer20AudioCapturerOptionsPKcS1_jPK27AudioStreamBasicDescriptionRS3__block_invoke.2608
+ ____Z16NewAudioCapturer20AudioCapturerOptionsPKcS1_jPK27AudioStreamBasicDescriptionRS3__block_invoke.3775
+ ____Z16NewAudioCapturer20AudioCapturerOptionsPKcS1_jPK27AudioStreamBasicDescriptionRS3__block_invoke.5106
+ ____Z16NewAudioCapturer20AudioCapturerOptionsPKcS1_jPK27AudioStreamBasicDescriptionRS3__block_invoke.5927
+ ____Z16NewAudioCapturer20AudioCapturerOptionsPKcS1_jPK27AudioStreamBasicDescriptionRS3__block_invoke.6336
+ ____Z16NewAudioCapturer20AudioCapturerOptionsPKcS1_jPK27AudioStreamBasicDescriptionRS3__block_invoke.8491
+ ____Z16NewAudioCapturer20AudioCapturerOptionsPKcS1_jPK27AudioStreamBasicDescriptionRS3__block_invoke.9321
+ ____Z17initAQMEMessengerv_block_invoke
+ ____Z28AudioStatisticsLibraryLoaderv_block_invoke.12150
+ ____Z28AudioStatisticsLibraryLoaderv_block_invoke.2632
+ ____Z28AudioStatisticsLibraryLoaderv_block_invoke.8853
+ ____Z28CMClientNotificationCallbackP26opaqueCMNotificationCenterPKvPK10__CFStringS2_S2__block_invoke.36
+ ____ZL15CPMSLibraryCorePPc_block_invoke.10450
+ ____ZL15CPMSLibraryCorePPc_block_invoke.3478
+ ____ZL15CPMSLibraryCorePPc_block_invoke.6304
+ ____ZL17getCPMSAgentClassv_block_invoke.3450
+ ____ZL17getCPMSAgentClassv_block_invoke.6302
+ ____ZL19AVFAudioLibraryCorePPc_block_invoke.12630
+ ____ZL20CoreMediaLibraryCorePPc_block_invoke.5037
+ ____ZL20CoreMediaLibraryCorePPc_block_invoke.7061
+ ____ZL21GetSpatialMetadataSPIv_block_invoke
+ ____ZL21GetSpatialMetadataSPIv_block_invoke.11542
+ ____ZL21getAVAudioFormatClassv_block_invoke.11883
+ ____ZL23MediaToolboxLibraryCorePPc_block_invoke.7053
+ ____ZL24getAVAudioPCMBufferClassv_block_invoke
+ ____ZL27getRBSProcessPredicateClassv_block_invoke
+ ____ZL28SpeechTranslationLibraryCorePPc_block_invoke
+ ____ZL29AudioSessionServerLibraryCorePPc_block_invoke.8296
+ ____ZL29getCPMSClientDescriptionClassv_block_invoke.3459
+ ____ZL32getSTSpeechTranslatorClientClassv_block_invoke
+ ____ZL33getCMBaseObjectGetVTableSymbolLocv_block_invoke.5033
+ ____ZL33getCMBaseObjectGetVTableSymbolLocv_block_invoke.7058
+ ____ZL58getFigCPECryptorCreateCryptorFromSerializedRecipeSymbolLocv_block_invoke.7049
+ ____ZN14DSP_Routing_VP28SetCallTranslationPropertiesEPK14__CFDictionaryRb_block_invoke
+ ____ZN14DSP_Routing_VPC2ER10AQMEIO_DSPN11DSP_Routing12ERoutingTypeERKNSt3__16vectorI14MEStreamTypeIDNS4_9allocatorIS6_EEEEb_block_invoke.10
+ ____ZN14DSP_Routing_VPC2ER10AQMEIO_DSPN11DSP_Routing12ERoutingTypeERKNSt3__16vectorI14MEStreamTypeIDNS4_9allocatorIS6_EEEEb_block_invoke_2.13
+ ____ZN14MEMixerChannel24ConfigureSpatializerHostEv_block_invoke
+ ____ZN14MixTapToUplinkC2ERKN2CA17StreamDescriptionERKNS0_13ChannelLayoutE_block_invoke
+ ____ZN16SSSHapticsPlayer17playHapticPatternEPK14__CFDictionaryP20SSPlayerSynchronizerbbNSt3__18functionIFvvEEE_block_invoke_3
+ ____ZN16SSSHapticsPlayer19cancelHapticPatternEb_block_invoke
+ ____ZN16SSSystemListener28MXSessionNotificationHandlerEP26opaqueCMNotificationCenterPKvPK10__CFStringS3_S3__block_invoke.24
+ ____ZN16SSSystemListener28MXSessionNotificationHandlerEP26opaqueCMNotificationCenterPKvPK10__CFStringS3_S3__block_invoke.30
+ ____ZN18MixTapToUplinkHost30RefreshMixTapToUplinkInstancesERKNSt3__113unordered_mapIjiNS0_4hashIjEENS0_8equal_toIjEENS0_9allocatorINS0_4pairIKjiEEEEEE_block_invoke
+ ____ZN20HapticEventConverter11loadPatternEP7NSArrayRbS2__block_invoke
+ ____ZN20HapticEventConverter11loadPatternEP7NSArrayRbS2__block_invoke_2
+ ____ZN20HapticEventConverter36consolidateAndPublishParameterCurvesEP14NSMutableArrayIP13AVHapticEventES4__block_invoke
+ ____ZN20HapticEventConverter36consolidateAndPublishParameterCurvesEP14NSMutableArrayIP13AVHapticEventES4__block_invoke_2
+ ____ZN20MEOutputStreamClientC2ER11IAQMEDevice14MEStreamTypeID15EDynamicsEnable_block_invoke
+ ____ZN21AVVoiceTriggerManager18hasVoiceTriggerXPCEv_block_invoke
+ ____ZN24AVVoiceTriggerServerImpl10InitializeEv_block_invoke
+ ____ZN24AVVoiceTriggerServerImpl10InitializeEv_block_invoke.310
+ ____ZN24AVVoiceTriggerServerImpl10InitializeEv_block_invoke.312
+ ____ZN24AVVoiceTriggerServerImpl10InitializeEv_block_invoke_2
+ ____ZN24AVVoiceTriggerServerImpl10InitializeEv_block_invoke_2.313
+ ____ZN24AVVoiceTriggerServerImpl12isPortActiveEmU13block_pointerFvbP7NSErrorE_block_invoke
+ ____ZN24AVVoiceTriggerServerImpl12speakerMutedEU13block_pointerFvbP7NSErrorE_block_invoke
+ ____ZN24AVVoiceTriggerServerImpl17enableBargeInModeEbU13block_pointerFvP7NSErrorE_block_invoke
+ ____ZN24AVVoiceTriggerServerImpl21activateSecureSessionEbU13block_pointerFvP7NSErrorE_block_invoke
+ ____ZN24AVVoiceTriggerServerImpl21listeningEnabledReplyEU13block_pointerFvbP7NSErrorE_block_invoke
+ ____ZN24AVVoiceTriggerServerImpl25siriClientsRecordingReplyEU13block_pointerFvmP7NSErrorE_block_invoke
+ ____ZN24AVVoiceTriggerServerImpl25speechDetectionVADCreatedEv_block_invoke
+ ____ZN24AVVoiceTriggerServerImpl33fetchHardwareSupportsVoiceTriggerEv_block_invoke
+ ____ZN24AVVoiceTriggerServerImpl40registerStateChangedNotificationHandlersEb_block_invoke
+ ____ZN24AVVoiceTriggerServerImplC2EP20AVVoiceTriggerServer_block_invoke
+ ____ZN24AVVoiceTriggerServerImplC2EP20AVVoiceTriggerServer_block_invoke_2
+ ____ZN24AVVoiceTriggerServerImplC2EP20AVVoiceTriggerServer_block_invoke_3
+ ____ZN26MutedSpeechActivityManager4Impl35GetProxyMutedSpeechActivityListenerEm_block_invoke
+ ____ZN2AT11Translation14CallTranslator17ReleaseAfterDelayENSt3__110shared_ptrIS1_EE_block_invoke
+ ____ZN2AT11Translation16TranslatorClient53getSTSpeechTranslatorClientsPreferredInputAudioFormatEv_block_invoke
+ ____ZN2AT11Translation16TranslatorClientC2ERNS0_21AudioStreamTranslatorERKNS0_24TranslationConfigurationE_block_invoke
+ ____ZN2AT11Translation19AUAsyncRendererHost9ConfigureEv_block_invoke
+ ____ZN2AT11Translation19AUAsyncRendererHost9ConfigureEv_block_invoke.2
+ ____ZN2AT11Translation24TranslationConfiguration6CreateEPK14__CFDictionary_block_invoke
+ ____ZN2AT13DispatchBlockEP16dispatch_queue_sU13block_pointerFvvEbPKcS5_iyy_block_invoke.10725
+ ____ZN2AT13DispatchBlockEP16dispatch_queue_sU13block_pointerFvvEbPKcS5_iyy_block_invoke.11531
+ ____ZN2AT13DispatchBlockEP16dispatch_queue_sU13block_pointerFvvEbPKcS5_iyy_block_invoke.13493
+ ____ZN2AT13DispatchBlockEP16dispatch_queue_sU13block_pointerFvvEbPKcS5_iyy_block_invoke.2911
+ ____ZN2AT13DispatchBlockEP16dispatch_queue_sU13block_pointerFvvEbPKcS5_iyy_block_invoke.3267
+ ____ZN2AT13DispatchBlockEP16dispatch_queue_sU13block_pointerFvvEbPKcS5_iyy_block_invoke.4861
+ ____ZN2AT13DispatchBlockEP16dispatch_queue_sU13block_pointerFvvEbPKcS5_iyy_block_invoke.6996
+ ____ZN2AT13DispatchBlockEP16dispatch_queue_sU13block_pointerFvvEbPKcS5_iyy_block_invoke.7522
+ ____ZN2AT13DispatchBlockEP16dispatch_queue_sU13block_pointerFvvEbPKcS5_iyy_block_invoke.8692
+ ____ZN2AT13DispatchBlockEP16dispatch_queue_sU13block_pointerFvvEbPKcS5_iyy_block_invoke.9711
+ ____ZN2AT13DispatchBlockEPU28objcproto17OS_dispatch_queue8NSObjectU13block_pointerFvvEbPKcS6_iyy_block_invoke.7012
+ ____ZZ54-[AVHapticServerInstance prepareHapticSequence:reply:]ENK3$_1clEm_block_invoke
+ ____ZZN14DSP_Routing_VP28SetCallTranslationPropertiesEPK14__CFDictionaryRbENK3$_1clEv_block_invoke
+ ____ZZN21AVVoiceTriggerManager10InitializeEvENK3$_1clEv_block_invoke
+ ____ZZN24AVVoiceTriggerServerImpl27enableVoiceTriggerListeningEbbU13block_pointerFvP7NSErrorEENKUljRKN15CAListenerProxy15HALNotificationEE_clEjS7__block_invoke
+ ____ZZN24AVVoiceTriggerServerImpl31updateVoiceTriggerConfigurationEPK14__CFDictionaryU13block_pointerFvP7NSErrorEENKUljRKN15CAListenerProxy15HALNotificationEE_clEjSA__block_invoke
+ ____ZZN24AVVoiceTriggerServerImpl40registerStateChangedNotificationHandlersEbENKUljRKN15CAListenerProxy15HALNotificationEE_clEjS3__block_invoke
+ ____ZZN24AVVoiceTriggerServerImpl42registerAOPVoiceTriggerNotificationHandlerEjbENKUljRKN15CAListenerProxy15HALNotificationEE_clEjS3__block_invoke
+ ___block_descriptor_120_ea8_32s40s48s56r64r72c25_ZTS19SSClientPlayOptions_e17_v16?0"NSError"8l
+ ___block_descriptor_32_e40_B24?0"AVHapticEvent"8"NSDictionary"16l
+ ___block_descriptor_32_e41_q24?0"AVHapticEvent"8"AVHapticEvent"16l
+ ___block_descriptor_40_e230_i52?0r^{AudioTimeStamp=dQdQ{SMPTETime=ssIIIssss}II}8I16r^{AudioBufferList=I[1{AudioBuffer=II^v}]}20r^{AudioBufferList=I[1{AudioBuffer=II^v}]}28^{AudioBufferList=I[1{AudioBuffer=II^v}]}36^{AudioBufferList=I[1{AudioBuffer=II^v}]}44l
+ ___block_descriptor_40_e49_v16?0r^{AudioBufferList=I[1{AudioBuffer=II^v}]}8l
+ ___block_descriptor_40_e52_v20?0r^{AudioBufferList=I[1{AudioBuffer=II^v}]}8B16l
+ ___block_descriptor_40_ea8_32r_e23_v16?0"AVAudioFormat"8lr32l8
+ ___block_descriptor_41_e230_i52?0r^{AudioTimeStamp=dQdQ{SMPTETime=ssIIIssss}II}8I16r^{AudioBufferList=I[1{AudioBuffer=II^v}]}20r^{AudioBufferList=I[1{AudioBuffer=II^v}]}28^{AudioBufferList=I[1{AudioBuffer=II^v}]}36^{AudioBufferList=I[1{AudioBuffer=II^v}]}44l
+ ___block_descriptor_48_ea8_32s40r_e5_v8?0lr40l8s32l8
+ ___block_descriptor_92_ea8_32r56c27_ZTSNSt3__18functionIFvvEEE_e5_v8?0l
+ ___block_descriptor_tmp.1.12740
+ ___block_descriptor_tmp.10.10743
+ ___block_descriptor_tmp.10.12834
+ ___block_descriptor_tmp.10.4956
+ ___block_descriptor_tmp.102.14144
+ ___block_descriptor_tmp.104
+ ___block_descriptor_tmp.10533
+ ___block_descriptor_tmp.107.14143
+ ___block_descriptor_tmp.10722
+ ___block_descriptor_tmp.108.14142
+ ___block_descriptor_tmp.109
+ ___block_descriptor_tmp.11.10748
+ ___block_descriptor_tmp.11.11688
+ ___block_descriptor_tmp.11.4862
+ ___block_descriptor_tmp.110
+ ___block_descriptor_tmp.111.13767
+ ___block_descriptor_tmp.111.14141
+ ___block_descriptor_tmp.111.8694
+ ___block_descriptor_tmp.112.14140
+ ___block_descriptor_tmp.113.14139
+ ___block_descriptor_tmp.11396
+ ___block_descriptor_tmp.1159
+ ___block_descriptor_tmp.12.13494
+ ___block_descriptor_tmp.12350
+ ___block_descriptor_tmp.12494
+ ___block_descriptor_tmp.12558
+ ___block_descriptor_tmp.12729
+ ___block_descriptor_tmp.12868
+ ___block_descriptor_tmp.13091
+ ___block_descriptor_tmp.13490
+ ___block_descriptor_tmp.1389
+ ___block_descriptor_tmp.14146
+ ___block_descriptor_tmp.142
+ ___block_descriptor_tmp.15
+ ___block_descriptor_tmp.15.11668
+ ___block_descriptor_tmp.1555
+ ___block_descriptor_tmp.168
+ ___block_descriptor_tmp.169
+ ___block_descriptor_tmp.170
+ ___block_descriptor_tmp.171
+ ___block_descriptor_tmp.172
+ ___block_descriptor_tmp.173
+ ___block_descriptor_tmp.174
+ ___block_descriptor_tmp.175
+ ___block_descriptor_tmp.177
+ ___block_descriptor_tmp.178
+ ___block_descriptor_tmp.179
+ ___block_descriptor_tmp.181
+ ___block_descriptor_tmp.1863
+ ___block_descriptor_tmp.200
+ ___block_descriptor_tmp.201
+ ___block_descriptor_tmp.2041
+ ___block_descriptor_tmp.2051
+ ___block_descriptor_tmp.209
+ ___block_descriptor_tmp.23.10726
+ ___block_descriptor_tmp.23.2859
+ ___block_descriptor_tmp.232
+ ___block_descriptor_tmp.24
+ ___block_descriptor_tmp.256
+ ___block_descriptor_tmp.2589
+ ___block_descriptor_tmp.26
+ ___block_descriptor_tmp.26.5194
+ ___block_descriptor_tmp.26.9712
+ ___block_descriptor_tmp.276
+ ___block_descriptor_tmp.29
+ ___block_descriptor_tmp.2909
+ ___block_descriptor_tmp.3.1857
+ ___block_descriptor_tmp.3.5190
+ ___block_descriptor_tmp.3.5892
+ ___block_descriptor_tmp.3.6952
+ ___block_descriptor_tmp.303
+ ___block_descriptor_tmp.3198
+ ___block_descriptor_tmp.3280
+ ___block_descriptor_tmp.3773
+ ___block_descriptor_tmp.38
+ ___block_descriptor_tmp.38.5352
+ ___block_descriptor_tmp.4.4886
+ ___block_descriptor_tmp.41
+ ___block_descriptor_tmp.45
+ ___block_descriptor_tmp.485
+ ___block_descriptor_tmp.4868
+ ___block_descriptor_tmp.490
+ ___block_descriptor_tmp.494
+ ___block_descriptor_tmp.498
+ ___block_descriptor_tmp.5.10737
+ ___block_descriptor_tmp.5.5138
+ ___block_descriptor_tmp.5.8967
+ ___block_descriptor_tmp.5017
+ ___block_descriptor_tmp.502
+ ___block_descriptor_tmp.5104
+ ___block_descriptor_tmp.5187
+ ___block_descriptor_tmp.52.11417
+ ___block_descriptor_tmp.52.12847
+ ___block_descriptor_tmp.5375
+ ___block_descriptor_tmp.58
+ ___block_descriptor_tmp.5881
+ ___block_descriptor_tmp.6.10739
+ ___block_descriptor_tmp.6.3272
+ ___block_descriptor_tmp.6.5139
+ ___block_descriptor_tmp.6016
+ ___block_descriptor_tmp.6334
+ ___block_descriptor_tmp.64
+ ___block_descriptor_tmp.6688
+ ___block_descriptor_tmp.6834
+ ___block_descriptor_tmp.69
+ ___block_descriptor_tmp.6948
+ ___block_descriptor_tmp.6993
+ ___block_descriptor_tmp.7.10740
+ ___block_descriptor_tmp.7.11685
+ ___block_descriptor_tmp.7.3265
+ ___block_descriptor_tmp.7.4858
+ ___block_descriptor_tmp.7.8969
+ ___block_descriptor_tmp.7062
+ ___block_descriptor_tmp.7390
+ ___block_descriptor_tmp.7520
+ ___block_descriptor_tmp.786
+ ___block_descriptor_tmp.7862
+ ___block_descriptor_tmp.8.10741
+ ___block_descriptor_tmp.8.12833
+ ___block_descriptor_tmp.8.3283
+ ___block_descriptor_tmp.8.6032
+ ___block_descriptor_tmp.8028
+ ___block_descriptor_tmp.81
+ ___block_descriptor_tmp.81.5392
+ ___block_descriptor_tmp.8690
+ ___block_descriptor_tmp.8965
+ ___block_descriptor_tmp.9.10742
+ ___block_descriptor_tmp.9.6997
+ ___block_descriptor_tmp.9381
+ ___block_descriptor_tmp.9728
+ ___block_descriptor_tmp.99.14145
+ ___block_literal_global.10087
+ ___block_literal_global.10529
+ ___block_literal_global.11394
+ ___block_literal_global.11974
+ ___block_literal_global.12147
+ ___block_literal_global.12348
+ ___block_literal_global.12554
+ ___block_literal_global.12694
+ ___block_literal_global.12727
+ ___block_literal_global.12864
+ ___block_literal_global.13084
+ ___block_literal_global.13764
+ ___block_literal_global.175
+ ___block_literal_global.176
+ ___block_literal_global.183
+ ___block_literal_global.203
+ ___block_literal_global.2038
+ ___block_literal_global.236
+ ___block_literal_global.258
+ ___block_literal_global.2629
+ ___block_literal_global.278
+ ___block_literal_global.28
+ ___block_literal_global.3.12738
+ ___block_literal_global.3.6018
+ ___block_literal_global.3158
+ ___block_literal_global.334
+ ___block_literal_global.3386
+ ___block_literal_global.3453
+ ___block_literal_global.3770
+ ___block_literal_global.3821
+ ___block_literal_global.453
+ ___block_literal_global.47
+ ___block_literal_global.4857
+ ___block_literal_global.487
+ ___block_literal_global.492
+ ___block_literal_global.496
+ ___block_literal_global.500
+ ___block_literal_global.5012
+ ___block_literal_global.504
+ ___block_literal_global.5058
+ ___block_literal_global.5101
+ ___block_literal_global.5188
+ ___block_literal_global.5281
+ ___block_literal_global.54
+ ___block_literal_global.5450
+ ___block_literal_global.5479
+ ___block_literal_global.5515
+ ___block_literal_global.561
+ ___block_literal_global.5923
+ ___block_literal_global.6.9057
+ ___block_literal_global.6014
+ ___block_literal_global.6113
+ ___block_literal_global.617
+ ___block_literal_global.6329
+ ___block_literal_global.6828
+ ___block_literal_global.6946
+ ___block_literal_global.701
+ ___block_literal_global.7283
+ ___block_literal_global.729
+ ___block_literal_global.7413
+ ___block_literal_global.7858
+ ___block_literal_global.7992
+ ___block_literal_global.83
+ ___block_literal_global.8486
+ ___block_literal_global.855
+ ___block_literal_global.9
+ ___block_literal_global.9047
+ ___block_literal_global.9313
+ ___block_literal_global.96
+ ___block_literal_global.9790
+ ___block_literal_global.9957
+ ___copy_helper_block_e8_32c60_ZTSNSt3__110shared_ptrIN2AT11Translation14CallTranslatorEEE
+ ___copy_helper_block_e8_40c60_ZTSNSt3__110shared_ptrIN2AT11Translation14CallTranslatorEEE
+ ___copy_helper_block_ea8_56c27_ZTSNSt3__18functionIFvvEEE
+ ___copy_helper_block_ea8_72c25_ZTS19SSClientPlayOptions
+ ___destroy_helper_block_e8_32c60_ZTSNSt3__110shared_ptrIN2AT11Translation14CallTranslatorEEE
+ ___destroy_helper_block_e8_40c60_ZTSNSt3__110shared_ptrIN2AT11Translation14CallTranslatorEEE
+ ___destroy_helper_block_ea8_56c27_ZTSNSt3__18functionIFvvEEE
+ ___destroy_helper_block_ea8_72c25_ZTS19SSClientPlayOptions
+ ___swift_reflection_version
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftCoreFoundation_$_AudioToolbox
+ __swift_FORCE_LOAD_$_swiftCoreMIDI
+ __swift_FORCE_LOAD_$_swiftCoreMIDI_$_AudioToolbox
+ __swift_FORCE_LOAD_$_swiftDarwin
+ __swift_FORCE_LOAD_$_swiftDarwin_$_AudioToolbox
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftDispatch_$_AudioToolbox
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftFoundation_$_AudioToolbox
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftObjectiveC_$_AudioToolbox
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swiftXPC_$_AudioToolbox
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_Builtin_float_$_AudioToolbox
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_AudioToolbox
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_AudioToolbox
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_AudioToolbox
+ __swift_FORCE_LOAD_$_swiftos
+ __swift_FORCE_LOAD_$_swiftos_$_AudioToolbox
+ _dlopenHelper$VoiceProcessor
+ _dlopenHelperFlag$VoiceProcessor
+ _gAQMEMessenger
+ _gMixTapToUplinkDeferredLog
+ _kAudioServicesPlaySystemSoundOptionPrefersToPlayAudioToHeadphonesOnlyKey
+ _kAudioTranslationKey_Enabled
+ _kAudioTranslationKey_InputConfiguration
+ _kAudioTranslationKey_OriginalSignalMaskingMode
+ _kAudioTranslationKey_OutputConfiguration
+ _kAudioTranslationKey_SignalMaskingMode
+ _kAudioTranslationKey_TranslationConfiguration
+ _kAudioTranslationKey_TranslationFeedbackOptions
+ _kAudioTranslationKey_TranslationMode
+ _kAudioTranslationKey_TranslatorToken
+ _kCFPreferencesAnyApplication
+ _kCMSession_InSystemSoundDetailsKey_SuppressAudio
+ _kCMSession_InSystemSoundDetailsKey_SuppressVibe
+ _kLoudnessInfoDictionary_AlbumLoudnessParametersKey
+ _kLoudnessInfoDictionary_MainLoudnessParametersKey
+ _kLoudnessInfoDictionary_MediaKindKey
+ _kLoudnessInfoDictionary_PrecalculatedSCAdjustmentKey
+ _kLoudnessInfoDictionary_SoundCheckInfoKey
+ _kLoudnessInfoDictionary_SoundCheckLoudnessTargetOverrideKey
+ _kLoudnessInfoDictionary_SoundCheckMaxPeakLevelOverrideKey
+ _kMXSession_InSystemSoundDetailsKey_PrefersToDisallowExternalPlayback
+ _kMXSession_InSystemSoundDetailsKey_PrefersToPlayAudioToHeadphonesOnly
+ _kMXSystemControllerNotification_ActiveAudioRouteDidChange
+ _kMediaKind_MusicValue
+ _kMediaKind_MusicVideoValue
+ _objc_moveWeak
+ _objc_msgSend$allowEnhanceDialogue:
+ _objc_msgSend$array
+ _objc_msgSend$arrayByAddingObjectsFromArray:
+ _objc_msgSend$arrayWithArray:
+ _objc_msgSend$audioBufferList
+ _objc_msgSend$audioUnit
+ _objc_msgSend$blurHoldTimeSec
+ _objc_msgSend$configure
+ _objc_msgSend$filterUsingPredicate:
+ _objc_msgSend$frameLength
+ _objc_msgSend$getAUStripPath
+ _objc_msgSend$getBusCountForScope:
+ _objc_msgSend$getDSPGraphPath
+ _objc_msgSend$getPropStripPath
+ _objc_msgSend$handleForPredicate:error:
+ _objc_msgSend$hostProcess
+ _objc_msgSend$initDownlinkWithFormat:maxFrames:error:
+ _objc_msgSend$initInternalWithFormat:maxFrames:isUplink:error:
+ _objc_msgSend$initUplinkWithFormat:maxFrames:error:
+ _objc_msgSend$initWithPCMFormat:frameCapacity:
+ _objc_msgSend$initWithRateLimit:detectPredictionAnchor:userContext:factory:execution:finalizer:useSleepWakeDetector:
+ _objc_msgSend$initWithTime:value:
+ _objc_msgSend$initWithTranslatorIdentifier:delegate:delegateQueue:
+ _objc_msgSend$initWithType:relativeTime:shape:controlPoints:
+ _objc_msgSend$initWithUUIDBytes:
+ _objc_msgSend$initWithUUIDString:
+ _objc_msgSend$initWithWeakImpl:scope:
+ _objc_msgSend$initializeAU
+ _objc_msgSend$isXPCService
+ _objc_msgSend$keyEnumerator
+ _objc_msgSend$lastObject
+ _objc_msgSend$lookUpPreferredInputAudioFormatWithCompletionHandler:
+ _objc_msgSend$mutableAudioBufferList
+ _objc_msgSend$nextObject
+ _objc_msgSend$predicateMatchingBundleIdentifier:
+ _objc_msgSend$predicateWithBlock:
+ _objc_msgSend$produceAudio
+ _objc_msgSend$setAUStrip:propertyStrip:
+ _objc_msgSend$setDSPGraph:
+ _objc_msgSend$setElementCount:
+ _objc_msgSend$setFormat:
+ _objc_msgSend$setFrameLength:
+ _objc_msgSend$setMaxFramesPerSlice
+ _objc_msgSend$setProduceAudio:
+ _objc_msgSend$setTime:
+ _objc_msgSend$setupAU
+ _objc_msgSend$sortedArrayUsingComparator:
+ _objc_msgSend$taskTokenDictionary
+ _objc_msgSend$translateAudioSamples:
+ _objc_msgSend$uninitializeAU
+ _objc_msgSend$updateFormat:error:
+ _objc_msgSend$updateFormats
+ _os_unfair_lock_assert_owner
+ _pthread_threadid_np
+ _vdprintf
+ _xpc_bool_create
+ _xpc_double_create
+ _xpc_int64_create
- -[ATThreadSafeHeadTracker initWithRateLimit:detectPredictionAnchor:userContext:factory:execution:finalizer:]
- -[AVBorealisServer .cxx_destruct]
- -[AVBorealisServer activateSecureSession:reply:]
- -[AVBorealisServer afSiriActivationBuiltInMicVoiceFuncPtr]
- -[AVBorealisServer clientConnections]
- -[AVBorealisServer clsVTStateManager]
- -[AVBorealisServer dealloc]
- -[AVBorealisServer enableBargeInMode:reply:]
- -[AVBorealisServer enableListeningOnPorts:reply:]
- -[AVBorealisServer enableSpeakerStateListening:reply:]
- -[AVBorealisServer enableVoiceTriggerListening:reply:]
- -[AVBorealisServer getInputChannelInfoCompletion:]
- -[AVBorealisServer hardwareSupportsVoiceTrigger]
- -[AVBorealisServer init]
- -[AVBorealisServer initializeWithReply:]
- -[AVBorealisServer isAssistantVoiceTriggerEnabled]
- -[AVBorealisServer listener:shouldAcceptNewConnection:]
- -[AVBorealisServer listeningEnabledReply:]
- -[AVBorealisServer mobileAssistantDylib]
- -[AVBorealisServer notificationQueue]
- -[AVBorealisServer portsActiveReply:]
- -[AVBorealisServer sendActiveStateChangedNotificationForPort:isActive:]
- -[AVBorealisServer sendSpeakerMuteStateChangedNotification:]
- -[AVBorealisServer sendVoiceTriggerOccuredNotification:triggerTime:]
- -[AVBorealisServer serverListener]
- -[AVBorealisServer setAfSiriActivationBuiltInMicVoiceFuncPtr:]
- -[AVBorealisServer setAggressiveECMode:reply:]
- -[AVBorealisServer setClientConnections:]
- -[AVBorealisServer setClsVTStateManager:]
- -[AVBorealisServer setListeningProperty:reply:]
- -[AVBorealisServer setMobileAssistantDylib:]
- -[AVBorealisServer setNotificationQueue:]
- -[AVBorealisServer setServerListener:]
- -[AVBorealisServer setVoiceTriggerDylib:]
- -[AVBorealisServer setVtStateManager:]
- -[AVBorealisServer siriClientRecordStateChanged:]
- -[AVBorealisServer siriClientsRecordingReply:]
- -[AVBorealisServer speakerStateActiveReply:]
- -[AVBorealisServer speakerStateMutedReply:]
- -[AVBorealisServer speechDetectionVADCreated]
- -[AVBorealisServer updateVoiceTriggerConfiguration:reply:]
- -[AVBorealisServer voiceTriggerDylib]
- -[AVBorealisServer voiceTriggerPastDataFramesAvailable:]
- -[AVBorealisServer vtStateManager]
- -[AVBorealisServerHysteresisNotifier .cxx_destruct]
- -[AVBorealisServerHysteresisNotifier addPortToMonitor:hysteresisDurationSeconds:notificationBlock:]
- -[AVBorealisServerHysteresisNotifier dealloc]
- -[AVBorealisServerHysteresisNotifier getPortManagerForType:]
- -[AVBorealisServerHysteresisNotifier initWithSerialQueue:]
- -[AVBorealisServerHysteresisNotifier isPortActive:activePortsToken:]
- -[AVBorealisServerHysteresisNotifier portsToMonitor]
- -[AVBorealisServerHysteresisNotifier processState:]
- -[AVBorealisServerHysteresisNotifier queue]
- -[AVBorealisServerHysteresisNotifier removePortToMonitor:]
- -[AVBorealisServerHysteresisNotifier sendState:]
- -[AVBorealisServerHysteresisNotifier setPortsToMonitor:]
- -[AVBorealisServerHysteresisNotifier setQueue:]
- -[AVBorealisServerHysteresisNotifier stateChanged:]
- -[AVBorealisServerHysteresisNotifier stateChanged:forPort:]
- -[AVBorealisServerPortManager .cxx_destruct]
- -[AVBorealisServerPortManager callNotificationBlock:]
- -[AVBorealisServerPortManager generation]
- -[AVBorealisServerPortManager hysteresisDurationSeconds]
- -[AVBorealisServerPortManager initWithPortType:hysteresisDurationSeconds:notificationBlock:]
- -[AVBorealisServerPortManager lastStateSent]
- -[AVBorealisServerPortManager listeningEnabled]
- -[AVBorealisServerPortManager notificationBlock]
- -[AVBorealisServerPortManager notifyStateChanged:onQueue:]
- -[AVBorealisServerPortManager portType]
- -[AVBorealisServerPortManager setGeneration:]
- -[AVBorealisServerPortManager setHysteresisDurationSeconds:]
- -[AVBorealisServerPortManager setLastStateSent:]
- -[AVBorealisServerPortManager setListeningEnabled:]
- -[AVBorealisServerPortManager setNotificationBlock:]
- -[AVBorealisServerPortManager setPortType:]
- GCC_except_table1000
- GCC_except_table1001
- GCC_except_table1007
- GCC_except_table1010
- GCC_except_table1019
- GCC_except_table104
- GCC_except_table1047
- GCC_except_table1051
- GCC_except_table1053
- GCC_except_table1057
- GCC_except_table1058
- GCC_except_table1059
- GCC_except_table1060
- GCC_except_table1062
- GCC_except_table1064
- GCC_except_table1066
- GCC_except_table1070
- GCC_except_table1075
- GCC_except_table1085
- GCC_except_table1087
- GCC_except_table1088
- GCC_except_table1089
- GCC_except_table109
- GCC_except_table11
- GCC_except_table110
- GCC_except_table112
- GCC_except_table1123
- GCC_except_table1124
- GCC_except_table1125
- GCC_except_table1129
- GCC_except_table1133
- GCC_except_table1134
- GCC_except_table1135
- GCC_except_table114
- GCC_except_table1143
- GCC_except_table1146
- GCC_except_table1147
- GCC_except_table1148
- GCC_except_table1149
- GCC_except_table115
- GCC_except_table1152
- GCC_except_table1153
- GCC_except_table1159
- GCC_except_table1160
- GCC_except_table1162
- GCC_except_table117
- GCC_except_table1176
- GCC_except_table1178
- GCC_except_table1179
- GCC_except_table1181
- GCC_except_table1182
- GCC_except_table1186
- GCC_except_table1187
- GCC_except_table1188
- GCC_except_table1189
- GCC_except_table1191
- GCC_except_table1192
- GCC_except_table1195
- GCC_except_table1198
- GCC_except_table12
- GCC_except_table1200
- GCC_except_table1204
- GCC_except_table1205
- GCC_except_table1206
- GCC_except_table1209
- GCC_except_table1211
- GCC_except_table122
- GCC_except_table1222
- GCC_except_table123
- GCC_except_table1238
- GCC_except_table124
- GCC_except_table1240
- GCC_except_table1241
- GCC_except_table1244
- GCC_except_table1245
- GCC_except_table1247
- GCC_except_table1252
- GCC_except_table1253
- GCC_except_table1254
- GCC_except_table1255
- GCC_except_table126
- GCC_except_table1265
- GCC_except_table1268
- GCC_except_table127
- GCC_except_table1283
- GCC_except_table1284
- GCC_except_table1285
- GCC_except_table1287
- GCC_except_table1289
- GCC_except_table1290
- GCC_except_table1293
- GCC_except_table1294
- GCC_except_table1295
- GCC_except_table1300
- GCC_except_table1301
- GCC_except_table1309
- GCC_except_table1311
- GCC_except_table1316
- GCC_except_table132
- GCC_except_table1342
- GCC_except_table1345
- GCC_except_table135
- GCC_except_table1354
- GCC_except_table1360
- GCC_except_table1370
- GCC_except_table1371
- GCC_except_table1373
- GCC_except_table1374
- GCC_except_table1389
- GCC_except_table1393
- GCC_except_table1394
- GCC_except_table1395
- GCC_except_table1402
- GCC_except_table1405
- GCC_except_table1408
- GCC_except_table1409
- GCC_except_table141
- GCC_except_table1410
- GCC_except_table1414
- GCC_except_table1415
- GCC_except_table1416
- GCC_except_table142
- GCC_except_table1425
- GCC_except_table1448
- GCC_except_table1449
- GCC_except_table1453
- GCC_except_table1455
- GCC_except_table1460
- GCC_except_table1467
- GCC_except_table1473
- GCC_except_table1475
- GCC_except_table1476
- GCC_except_table1481
- GCC_except_table1482
- GCC_except_table1483
- GCC_except_table1484
- GCC_except_table15
- GCC_except_table1508
- GCC_except_table1511
- GCC_except_table1512
- GCC_except_table1532
- GCC_except_table1533
- GCC_except_table1537
- GCC_except_table1538
- GCC_except_table1539
- GCC_except_table1540
- GCC_except_table1548
- GCC_except_table1552
- GCC_except_table1559
- GCC_except_table1582
- GCC_except_table1584
- GCC_except_table16
- GCC_except_table1601
- GCC_except_table161
- GCC_except_table1624
- GCC_except_table1625
- GCC_except_table1626
- GCC_except_table164
- GCC_except_table1640
- GCC_except_table1643
- GCC_except_table1647
- GCC_except_table1649
- GCC_except_table167
- GCC_except_table168
- GCC_except_table1704
- GCC_except_table1705
- GCC_except_table1707
- GCC_except_table1708
- GCC_except_table1713
- GCC_except_table1720
- GCC_except_table1722
- GCC_except_table1723
- GCC_except_table1724
- GCC_except_table1725
- GCC_except_table1726
- GCC_except_table1727
- GCC_except_table1728
- GCC_except_table1729
- GCC_except_table173
- GCC_except_table1731
- GCC_except_table1732
- GCC_except_table1733
- GCC_except_table1734
- GCC_except_table1737
- GCC_except_table1738
- GCC_except_table1752
- GCC_except_table1753
- GCC_except_table1754
- GCC_except_table1756
- GCC_except_table1757
- GCC_except_table1758
- GCC_except_table1759
- GCC_except_table176
- GCC_except_table1760
- GCC_except_table1761
- GCC_except_table1766
- GCC_except_table1768
- GCC_except_table1769
- GCC_except_table1770
- GCC_except_table1771
- GCC_except_table1772
- GCC_except_table1773
- GCC_except_table1777
- GCC_except_table1779
- GCC_except_table1781
- GCC_except_table1782
- GCC_except_table1783
- GCC_except_table1786
- GCC_except_table179
- GCC_except_table1790
- GCC_except_table1792
- GCC_except_table1795
- GCC_except_table1796
- GCC_except_table1797
- GCC_except_table1798
- GCC_except_table1799
- GCC_except_table1800
- GCC_except_table1803
- GCC_except_table1805
- GCC_except_table1806
- GCC_except_table1808
- GCC_except_table1809
- GCC_except_table1810
- GCC_except_table1811
- GCC_except_table1818
- GCC_except_table1821
- GCC_except_table1833
- GCC_except_table1835
- GCC_except_table1836
- GCC_except_table1838
- GCC_except_table1848
- GCC_except_table1849
- GCC_except_table1852
- GCC_except_table1854
- GCC_except_table1866
- GCC_except_table187
- GCC_except_table1874
- GCC_except_table1876
- GCC_except_table188
- GCC_except_table1897
- GCC_except_table19
- GCC_except_table1901
- GCC_except_table1906
- GCC_except_table1908
- GCC_except_table1910
- GCC_except_table1914
- GCC_except_table1919
- GCC_except_table1925
- GCC_except_table193
- GCC_except_table194
- GCC_except_table1958
- GCC_except_table1959
- GCC_except_table1971
- GCC_except_table1989
- GCC_except_table1999
- GCC_except_table20
- GCC_except_table200
- GCC_except_table2000
- GCC_except_table2003
- GCC_except_table2005
- GCC_except_table2007
- GCC_except_table2014
- GCC_except_table2016
- GCC_except_table2026
- GCC_except_table2027
- GCC_except_table2029
- GCC_except_table2030
- GCC_except_table2034
- GCC_except_table2038
- GCC_except_table2044
- GCC_except_table2045
- GCC_except_table2046
- GCC_except_table2048
- GCC_except_table2050
- GCC_except_table2052
- GCC_except_table2053
- GCC_except_table2054
- GCC_except_table2055
- GCC_except_table2064
- GCC_except_table2065
- GCC_except_table2070
- GCC_except_table2090
- GCC_except_table2095
- GCC_except_table2097
- GCC_except_table2098
- GCC_except_table2102
- GCC_except_table2112
- GCC_except_table2114
- GCC_except_table2117
- GCC_except_table2119
- GCC_except_table2122
- GCC_except_table2138
- GCC_except_table215
- GCC_except_table2168
- GCC_except_table2170
- GCC_except_table2176
- GCC_except_table2194
- GCC_except_table2219
- GCC_except_table2222
- GCC_except_table2225
- GCC_except_table2240
- GCC_except_table2246
- GCC_except_table2250
- GCC_except_table2253
- GCC_except_table2254
- GCC_except_table2255
- GCC_except_table2264
- GCC_except_table2265
- GCC_except_table2267
- GCC_except_table2268
- GCC_except_table2269
- GCC_except_table2279
- GCC_except_table2280
- GCC_except_table2281
- GCC_except_table2283
- GCC_except_table2285
- GCC_except_table2291
- GCC_except_table2296
- GCC_except_table23
- GCC_except_table2302
- GCC_except_table2306
- GCC_except_table2307
- GCC_except_table2314
- GCC_except_table2326
- GCC_except_table2328
- GCC_except_table2333
- GCC_except_table2334
- GCC_except_table2335
- GCC_except_table2337
- GCC_except_table2338
- GCC_except_table2339
- GCC_except_table2347
- GCC_except_table235
- GCC_except_table2350
- GCC_except_table236
- GCC_except_table2361
- GCC_except_table2363
- GCC_except_table2364
- GCC_except_table2369
- GCC_except_table2370
- GCC_except_table2371
- GCC_except_table2374
- GCC_except_table2375
- GCC_except_table2379
- GCC_except_table2383
- GCC_except_table2384
- GCC_except_table2393
- GCC_except_table2399
- GCC_except_table2400
- GCC_except_table2402
- GCC_except_table2404
- GCC_except_table2406
- GCC_except_table2410
- GCC_except_table2419
- GCC_except_table2427
- GCC_except_table2428
- GCC_except_table2429
- GCC_except_table2430
- GCC_except_table2432
- GCC_except_table2434
- GCC_except_table2437
- GCC_except_table2442
- GCC_except_table2443
- GCC_except_table2446
- GCC_except_table2450
- GCC_except_table2452
- GCC_except_table2453
- GCC_except_table2455
- GCC_except_table2456
- GCC_except_table2457
- GCC_except_table2458
- GCC_except_table2459
- GCC_except_table247
- GCC_except_table2476
- GCC_except_table2479
- GCC_except_table2499
- GCC_except_table250
- GCC_except_table2500
- GCC_except_table2508
- GCC_except_table2521
- GCC_except_table2522
- GCC_except_table2534
- GCC_except_table2535
- GCC_except_table2536
- GCC_except_table2538
- GCC_except_table2587
- GCC_except_table2588
- GCC_except_table2589
- GCC_except_table2590
- GCC_except_table2591
- GCC_except_table2592
- GCC_except_table2596
- GCC_except_table2597
- GCC_except_table26
- GCC_except_table2600
- GCC_except_table2602
- GCC_except_table2603
- GCC_except_table2604
- GCC_except_table2607
- GCC_except_table2608
- GCC_except_table2620
- GCC_except_table2621
- GCC_except_table2623
- GCC_except_table2624
- GCC_except_table2626
- GCC_except_table2627
- GCC_except_table2628
- GCC_except_table2630
- GCC_except_table2635
- GCC_except_table2643
- GCC_except_table2644
- GCC_except_table2648
- GCC_except_table2649
- GCC_except_table2657
- GCC_except_table2658
- GCC_except_table2659
- GCC_except_table2660
- GCC_except_table2662
- GCC_except_table2664
- GCC_except_table2665
- GCC_except_table2666
- GCC_except_table2667
- GCC_except_table2668
- GCC_except_table2669
- GCC_except_table2670
- GCC_except_table2671
- GCC_except_table2672
- GCC_except_table2694
- GCC_except_table2695
- GCC_except_table2697
- GCC_except_table2698
- GCC_except_table2700
- GCC_except_table2702
- GCC_except_table2705
- GCC_except_table2707
- GCC_except_table2708
- GCC_except_table2709
- GCC_except_table2711
- GCC_except_table2713
- GCC_except_table2727
- GCC_except_table2729
- GCC_except_table2730
- GCC_except_table2731
- GCC_except_table2732
- GCC_except_table2733
- GCC_except_table2736
- GCC_except_table2740
- GCC_except_table2741
- GCC_except_table2742
- GCC_except_table2743
- GCC_except_table2745
- GCC_except_table2753
- GCC_except_table2755
- GCC_except_table2756
- GCC_except_table2757
- GCC_except_table2789
- GCC_except_table2792
- GCC_except_table2793
- GCC_except_table28
- GCC_except_table2803
- GCC_except_table2804
- GCC_except_table2806
- GCC_except_table2816
- GCC_except_table2819
- GCC_except_table2821
- GCC_except_table2837
- GCC_except_table2838
- GCC_except_table2839
- GCC_except_table2840
- GCC_except_table2844
- GCC_except_table2846
- GCC_except_table2848
- GCC_except_table2849
- GCC_except_table2850
- GCC_except_table2851
- GCC_except_table2855
- GCC_except_table2856
- GCC_except_table2857
- GCC_except_table2858
- GCC_except_table2860
- GCC_except_table2864
- GCC_except_table2865
- GCC_except_table2876
- GCC_except_table2877
- GCC_except_table2880
- GCC_except_table2881
- GCC_except_table2883
- GCC_except_table289
- GCC_except_table2893
- GCC_except_table2895
- GCC_except_table29
- GCC_except_table2911
- GCC_except_table2912
- GCC_except_table2914
- GCC_except_table2917
- GCC_except_table2918
- GCC_except_table2919
- GCC_except_table292
- GCC_except_table2920
- GCC_except_table293
- GCC_except_table2930
- GCC_except_table2932
- GCC_except_table2933
- GCC_except_table2934
- GCC_except_table2939
- GCC_except_table295
- GCC_except_table2954
- GCC_except_table2959
- GCC_except_table2961
- GCC_except_table2965
- GCC_except_table2967
- GCC_except_table2968
- GCC_except_table2969
- GCC_except_table297
- GCC_except_table2970
- GCC_except_table2971
- GCC_except_table2981
- GCC_except_table2982
- GCC_except_table2991
- GCC_except_table2992
- GCC_except_table2993
- GCC_except_table2996
- GCC_except_table30
- GCC_except_table3000
- GCC_except_table3001
- GCC_except_table3002
- GCC_except_table301
- GCC_except_table306
- GCC_except_table3060
- GCC_except_table307
- GCC_except_table308
- GCC_except_table309
- GCC_except_table31
- GCC_except_table3115
- GCC_except_table3117
- GCC_except_table312
- GCC_except_table3123
- GCC_except_table3130
- GCC_except_table3140
- GCC_except_table3141
- GCC_except_table315
- GCC_except_table3150
- GCC_except_table3190
- GCC_except_table3194
- GCC_except_table3198
- GCC_except_table3200
- GCC_except_table3202
- GCC_except_table3204
- GCC_except_table3207
- GCC_except_table3209
- GCC_except_table3214
- GCC_except_table3219
- GCC_except_table3224
- GCC_except_table3226
- GCC_except_table3228
- GCC_except_table3229
- GCC_except_table3230
- GCC_except_table3231
- GCC_except_table3232
- GCC_except_table3233
- GCC_except_table3252
- GCC_except_table3253
- GCC_except_table3254
- GCC_except_table3256
- GCC_except_table3259
- GCC_except_table3260
- GCC_except_table3262
- GCC_except_table3272
- GCC_except_table3274
- GCC_except_table3275
- GCC_except_table3277
- GCC_except_table3280
- GCC_except_table3281
- GCC_except_table3282
- GCC_except_table3284
- GCC_except_table3285
- GCC_except_table3286
- GCC_except_table3287
- GCC_except_table3289
- GCC_except_table3290
- GCC_except_table3291
- GCC_except_table3292
- GCC_except_table3293
- GCC_except_table3296
- GCC_except_table3298
- GCC_except_table33
- GCC_except_table3308
- GCC_except_table3312
- GCC_except_table3313
- GCC_except_table3316
- GCC_except_table3317
- GCC_except_table332
- GCC_except_table3324
- GCC_except_table3326
- GCC_except_table3327
- GCC_except_table3331
- GCC_except_table3336
- GCC_except_table3338
- GCC_except_table3340
- GCC_except_table3342
- GCC_except_table3357
- GCC_except_table3359
- GCC_except_table3361
- GCC_except_table3362
- GCC_except_table3364
- GCC_except_table3366
- GCC_except_table3373
- GCC_except_table3380
- GCC_except_table3381
- GCC_except_table3382
- GCC_except_table3383
- GCC_except_table3384
- GCC_except_table3385
- GCC_except_table3386
- GCC_except_table3387
- GCC_except_table3389
- GCC_except_table339
- GCC_except_table3392
- GCC_except_table3404
- GCC_except_table3406
- GCC_except_table341
- GCC_except_table3412
- GCC_except_table3413
- GCC_except_table3415
- GCC_except_table3416
- GCC_except_table3417
- GCC_except_table3429
- GCC_except_table3434
- GCC_except_table3435
- GCC_except_table3436
- GCC_except_table3437
- GCC_except_table3440
- GCC_except_table3441
- GCC_except_table3442
- GCC_except_table3444
- GCC_except_table3445
- GCC_except_table3446
- GCC_except_table3449
- GCC_except_table3459
- GCC_except_table3464
- GCC_except_table3473
- GCC_except_table3474
- GCC_except_table3496
- GCC_except_table3498
- GCC_except_table3501
- GCC_except_table3504
- GCC_except_table351
- GCC_except_table3519
- GCC_except_table3525
- GCC_except_table3526
- GCC_except_table3527
- GCC_except_table3535
- GCC_except_table3546
- GCC_except_table3568
- GCC_except_table3571
- GCC_except_table3576
- GCC_except_table3578
- GCC_except_table3579
- GCC_except_table3585
- GCC_except_table3588
- GCC_except_table3593
- GCC_except_table3622
- GCC_except_table3623
- GCC_except_table3625
- GCC_except_table3626
- GCC_except_table3628
- GCC_except_table3630
- GCC_except_table366
- GCC_except_table3702
- GCC_except_table3714
- GCC_except_table3725
- GCC_except_table3728
- GCC_except_table3731
- GCC_except_table3734
- GCC_except_table3745
- GCC_except_table3765
- GCC_except_table3767
- GCC_except_table3775
- GCC_except_table3776
- GCC_except_table3777
- GCC_except_table3778
- GCC_except_table3779
- GCC_except_table3780
- GCC_except_table3782
- GCC_except_table3783
- GCC_except_table3787
- GCC_except_table3790
- GCC_except_table3792
- GCC_except_table3794
- GCC_except_table3797
- GCC_except_table38
- GCC_except_table3804
- GCC_except_table3805
- GCC_except_table3807
- GCC_except_table3810
- GCC_except_table3816
- GCC_except_table3818
- GCC_except_table3825
- GCC_except_table3826
- GCC_except_table3827
- GCC_except_table3829
- GCC_except_table3833
- GCC_except_table3834
- GCC_except_table3835
- GCC_except_table3837
- GCC_except_table3838
- GCC_except_table3839
- GCC_except_table3840
- GCC_except_table3842
- GCC_except_table3843
- GCC_except_table3844
- GCC_except_table3845
- GCC_except_table3851
- GCC_except_table3852
- GCC_except_table3859
- GCC_except_table386
- GCC_except_table3860
- GCC_except_table3861
- GCC_except_table3862
- GCC_except_table3863
- GCC_except_table3864
- GCC_except_table3865
- GCC_except_table3866
- GCC_except_table3867
- GCC_except_table3868
- GCC_except_table3870
- GCC_except_table3872
- GCC_except_table3873
- GCC_except_table3874
- GCC_except_table3879
- GCC_except_table388
- GCC_except_table3880
- GCC_except_table3884
- GCC_except_table3896
- GCC_except_table39
- GCC_except_table3905
- GCC_except_table3909
- GCC_except_table391
- GCC_except_table3911
- GCC_except_table3917
- GCC_except_table392
- GCC_except_table393
- GCC_except_table394
- GCC_except_table395
- GCC_except_table396
- GCC_except_table3971
- GCC_except_table3974
- GCC_except_table398
- GCC_except_table3985
- GCC_except_table3986
- GCC_except_table3987
- GCC_except_table399
- GCC_except_table3997
- GCC_except_table3998
- GCC_except_table4000
- GCC_except_table4001
- GCC_except_table4002
- GCC_except_table4003
- GCC_except_table4004
- GCC_except_table4005
- GCC_except_table4008
- GCC_except_table4009
- GCC_except_table4011
- GCC_except_table4022
- GCC_except_table403
- GCC_except_table4043
- GCC_except_table4056
- GCC_except_table406
- GCC_except_table4071
- GCC_except_table4072
- GCC_except_table4073
- GCC_except_table4077
- GCC_except_table41
- GCC_except_table4105
- GCC_except_table4106
- GCC_except_table4107
- GCC_except_table4118
- GCC_except_table4127
- GCC_except_table413
- GCC_except_table414
- GCC_except_table4140
- GCC_except_table4141
- GCC_except_table4142
- GCC_except_table4144
- GCC_except_table4148
- GCC_except_table415
- GCC_except_table4155
- GCC_except_table416
- GCC_except_table4167
- GCC_except_table417
- GCC_except_table4170
- GCC_except_table4172
- GCC_except_table4173
- GCC_except_table4175
- GCC_except_table4176
- GCC_except_table419
- GCC_except_table4196
- GCC_except_table4199
- GCC_except_table42
- GCC_except_table4201
- GCC_except_table4204
- GCC_except_table4207
- GCC_except_table4214
- GCC_except_table4227
- GCC_except_table4229
- GCC_except_table4230
- GCC_except_table4232
- GCC_except_table4234
- GCC_except_table4235
- GCC_except_table424
- GCC_except_table4240
- GCC_except_table4247
- GCC_except_table4259
- GCC_except_table426
- GCC_except_table4265
- GCC_except_table427
- GCC_except_table428
- GCC_except_table4285
- GCC_except_table4287
- GCC_except_table4288
- GCC_except_table4289
- GCC_except_table429
- GCC_except_table4290
- GCC_except_table4297
- GCC_except_table4298
- GCC_except_table4300
- GCC_except_table431
- GCC_except_table4330
- GCC_except_table4363
- GCC_except_table439
- GCC_except_table442
- GCC_except_table4423
- GCC_except_table443
- GCC_except_table444
- GCC_except_table4440
- GCC_except_table4445
- GCC_except_table4449
- GCC_except_table4452
- GCC_except_table4453
- GCC_except_table4463
- GCC_except_table4468
- GCC_except_table447
- GCC_except_table448
- GCC_except_table451
- GCC_except_table4582
- GCC_except_table4583
- GCC_except_table4585
- GCC_except_table4587
- GCC_except_table4588
- GCC_except_table4589
- GCC_except_table4590
- GCC_except_table4591
- GCC_except_table4592
- GCC_except_table4593
- GCC_except_table4594
- GCC_except_table4596
- GCC_except_table4597
- GCC_except_table4598
- GCC_except_table4599
- GCC_except_table460
- GCC_except_table4606
- GCC_except_table4607
- GCC_except_table4608
- GCC_except_table4610
- GCC_except_table4613
- GCC_except_table4614
- GCC_except_table4619
- GCC_except_table462
- GCC_except_table4620
- GCC_except_table4626
- GCC_except_table463
- GCC_except_table4635
- GCC_except_table4638
- GCC_except_table464
- GCC_except_table4641
- GCC_except_table4649
- GCC_except_table465
- GCC_except_table4650
- GCC_except_table4656
- GCC_except_table4670
- GCC_except_table4671
- GCC_except_table4672
- GCC_except_table4673
- GCC_except_table4674
- GCC_except_table4677
- GCC_except_table4683
- GCC_except_table4684
- GCC_except_table4686
- GCC_except_table4688
- GCC_except_table469
- GCC_except_table4692
- GCC_except_table4698
- GCC_except_table470
- GCC_except_table4701
- GCC_except_table4702
- GCC_except_table4703
- GCC_except_table4709
- GCC_except_table471
- GCC_except_table4711
- GCC_except_table4714
- GCC_except_table472
- GCC_except_table4723
- GCC_except_table4729
- GCC_except_table473
- GCC_except_table4730
- GCC_except_table4736
- GCC_except_table4741
- GCC_except_table4742
- GCC_except_table4743
- GCC_except_table4745
- GCC_except_table4747
- GCC_except_table4748
- GCC_except_table4749
- GCC_except_table4756
- GCC_except_table4760
- GCC_except_table4761
- GCC_except_table4763
- GCC_except_table4770
- GCC_except_table4771
- GCC_except_table4772
- GCC_except_table4774
- GCC_except_table4776
- GCC_except_table478
- GCC_except_table4780
- GCC_except_table4781
- GCC_except_table4783
- GCC_except_table4784
- GCC_except_table4790
- GCC_except_table4791
- GCC_except_table4797
- GCC_except_table4801
- GCC_except_table4805
- GCC_except_table4806
- GCC_except_table4809
- GCC_except_table4814
- GCC_except_table4816
- GCC_except_table4819
- GCC_except_table4821
- GCC_except_table4826
- GCC_except_table4827
- GCC_except_table4835
- GCC_except_table4839
- GCC_except_table4859
- GCC_except_table4861
- GCC_except_table4863
- GCC_except_table4864
- GCC_except_table4881
- GCC_except_table4884
- GCC_except_table5
- GCC_except_table50
- GCC_except_table51
- GCC_except_table511
- GCC_except_table512
- GCC_except_table539
- GCC_except_table540
- GCC_except_table542
- GCC_except_table543
- GCC_except_table544
- GCC_except_table553
- GCC_except_table555
- GCC_except_table575
- GCC_except_table576
- GCC_except_table5784
- GCC_except_table5785
- GCC_except_table5786
- GCC_except_table579
- GCC_except_table5809
- GCC_except_table581
- GCC_except_table5810
- GCC_except_table5815
- GCC_except_table5816
- GCC_except_table5817
- GCC_except_table5819
- GCC_except_table582
- GCC_except_table5821
- GCC_except_table5823
- GCC_except_table5825
- GCC_except_table5827
- GCC_except_table5829
- GCC_except_table583
- GCC_except_table5831
- GCC_except_table5833
- GCC_except_table5834
- GCC_except_table5835
- GCC_except_table5837
- GCC_except_table584
- GCC_except_table5843
- GCC_except_table585
- GCC_except_table5855
- GCC_except_table586
- GCC_except_table587
- GCC_except_table588
- GCC_except_table589
- GCC_except_table590
- GCC_except_table591
- GCC_except_table5917
- GCC_except_table592
- GCC_except_table5923
- GCC_except_table5924
- GCC_except_table5927
- GCC_except_table5928
- GCC_except_table5932
- GCC_except_table5934
- GCC_except_table5938
- GCC_except_table5940
- GCC_except_table5941
- GCC_except_table5943
- GCC_except_table5945
- GCC_except_table5947
- GCC_except_table5955
- GCC_except_table5956
- GCC_except_table5957
- GCC_except_table5958
- GCC_except_table5960
- GCC_except_table5965
- GCC_except_table5969
- GCC_except_table5971
- GCC_except_table5976
- GCC_except_table5981
- GCC_except_table5986
- GCC_except_table5988
- GCC_except_table5990
- GCC_except_table5992
- GCC_except_table5993
- GCC_except_table5998
- GCC_except_table6
- GCC_except_table6000
- GCC_except_table6001
- GCC_except_table6003
- GCC_except_table6004
- GCC_except_table6007
- GCC_except_table6009
- GCC_except_table6015
- GCC_except_table604
- GCC_except_table6041
- GCC_except_table6043
- GCC_except_table6044
- GCC_except_table6045
- GCC_except_table6046
- GCC_except_table6047
- GCC_except_table6048
- GCC_except_table605
- GCC_except_table6052
- GCC_except_table6054
- GCC_except_table6059
- GCC_except_table6063
- GCC_except_table6072
- GCC_except_table6074
- GCC_except_table6079
- GCC_except_table6082
- GCC_except_table6083
- GCC_except_table6088
- GCC_except_table6089
- GCC_except_table6091
- GCC_except_table6096
- GCC_except_table6097
- GCC_except_table610
- GCC_except_table6118
- GCC_except_table612
- GCC_except_table6122
- GCC_except_table6126
- GCC_except_table613
- GCC_except_table6136
- GCC_except_table6138
- GCC_except_table6141
- GCC_except_table6142
- GCC_except_table6145
- GCC_except_table6149
- GCC_except_table615
- GCC_except_table6151
- GCC_except_table6153
- GCC_except_table6156
- GCC_except_table6158
- GCC_except_table6160
- GCC_except_table6161
- GCC_except_table6164
- GCC_except_table6169
- GCC_except_table6170
- GCC_except_table6172
- GCC_except_table6173
- GCC_except_table6174
- GCC_except_table6175
- GCC_except_table6177
- GCC_except_table618
- GCC_except_table6180
- GCC_except_table6184
- GCC_except_table6185
- GCC_except_table6186
- GCC_except_table6187
- GCC_except_table6188
- GCC_except_table6189
- GCC_except_table6193
- GCC_except_table6197
- GCC_except_table6198
- GCC_except_table6199
- GCC_except_table6200
- GCC_except_table6203
- GCC_except_table6204
- GCC_except_table6206
- GCC_except_table6207
- GCC_except_table6208
- GCC_except_table6209
- GCC_except_table621
- GCC_except_table6211
- GCC_except_table6212
- GCC_except_table6213
- GCC_except_table6215
- GCC_except_table6219
- GCC_except_table622
- GCC_except_table6220
- GCC_except_table6221
- GCC_except_table6222
- GCC_except_table6224
- GCC_except_table6228
- GCC_except_table623
- GCC_except_table6242
- GCC_except_table6244
- GCC_except_table6248
- GCC_except_table625
- GCC_except_table6250
- GCC_except_table6251
- GCC_except_table6252
- GCC_except_table6253
- GCC_except_table6261
- GCC_except_table6274
- GCC_except_table6288
- GCC_except_table6289
- GCC_except_table6297
- GCC_except_table6298
- GCC_except_table6301
- GCC_except_table6304
- GCC_except_table6308
- GCC_except_table6310
- GCC_except_table6315
- GCC_except_table6318
- GCC_except_table6326
- GCC_except_table6340
- GCC_except_table6341
- GCC_except_table6343
- GCC_except_table6353
- GCC_except_table6354
- GCC_except_table6358
- GCC_except_table6361
- GCC_except_table6367
- GCC_except_table6368
- GCC_except_table6374
- GCC_except_table6392
- GCC_except_table6393
- GCC_except_table6395
- GCC_except_table6396
- GCC_except_table6405
- GCC_except_table6406
- GCC_except_table6409
- GCC_except_table641
- GCC_except_table6410
- GCC_except_table6412
- GCC_except_table6415
- GCC_except_table6420
- GCC_except_table6423
- GCC_except_table6424
- GCC_except_table6425
- GCC_except_table6426
- GCC_except_table6437
- GCC_except_table6440
- GCC_except_table6456
- GCC_except_table6459
- GCC_except_table6460
- GCC_except_table6461
- GCC_except_table6462
- GCC_except_table6464
- GCC_except_table6465
- GCC_except_table6466
- GCC_except_table6472
- GCC_except_table6473
- GCC_except_table6491
- GCC_except_table6494
- GCC_except_table6495
- GCC_except_table6497
- GCC_except_table6498
- GCC_except_table6502
- GCC_except_table6516
- GCC_except_table6531
- GCC_except_table6537
- GCC_except_table6558
- GCC_except_table6559
- GCC_except_table656
- GCC_except_table6560
- GCC_except_table6561
- GCC_except_table6562
- GCC_except_table6563
- GCC_except_table6580
- GCC_except_table6585
- GCC_except_table6603
- GCC_except_table661
- GCC_except_table6610
- GCC_except_table6611
- GCC_except_table663
- GCC_except_table6652
- GCC_except_table6655
- GCC_except_table6658
- GCC_except_table6659
- GCC_except_table666
- GCC_except_table6660
- GCC_except_table6661
- GCC_except_table6662
- GCC_except_table6665
- GCC_except_table6667
- GCC_except_table6682
- GCC_except_table6691
- GCC_except_table6692
- GCC_except_table6695
- GCC_except_table6698
- GCC_except_table6699
- GCC_except_table670
- GCC_except_table6701
- GCC_except_table6702
- GCC_except_table6704
- GCC_except_table6707
- GCC_except_table6708
- GCC_except_table6709
- GCC_except_table6710
- GCC_except_table6712
- GCC_except_table6714
- GCC_except_table6720
- GCC_except_table6722
- GCC_except_table6724
- GCC_except_table6726
- GCC_except_table6735
- GCC_except_table6748
- GCC_except_table6749
- GCC_except_table6750
- GCC_except_table6751
- GCC_except_table6752
- GCC_except_table6758
- GCC_except_table6759
- GCC_except_table6760
- GCC_except_table6761
- GCC_except_table6762
- GCC_except_table6783
- GCC_except_table6797
- GCC_except_table6811
- GCC_except_table6825
- GCC_except_table6826
- GCC_except_table6839
- GCC_except_table6855
- GCC_except_table6876
- GCC_except_table6879
- GCC_except_table6880
- GCC_except_table6881
- GCC_except_table6906
- GCC_except_table6908
- GCC_except_table6912
- GCC_except_table6913
- GCC_except_table6915
- GCC_except_table6920
- GCC_except_table6923
- GCC_except_table6924
- GCC_except_table6925
- GCC_except_table693
- GCC_except_table6934
- GCC_except_table6942
- GCC_except_table6947
- GCC_except_table6948
- GCC_except_table6949
- GCC_except_table6950
- GCC_except_table6951
- GCC_except_table6952
- GCC_except_table6953
- GCC_except_table6954
- GCC_except_table6964
- GCC_except_table6966
- GCC_except_table6967
- GCC_except_table6968
- GCC_except_table6969
- GCC_except_table6972
- GCC_except_table6973
- GCC_except_table6974
- GCC_except_table6975
- GCC_except_table6979
- GCC_except_table6981
- GCC_except_table6984
- GCC_except_table6985
- GCC_except_table6986
- GCC_except_table6992
- GCC_except_table6995
- GCC_except_table6996
- GCC_except_table6999
- GCC_except_table7
- GCC_except_table7002
- GCC_except_table7004
- GCC_except_table7007
- GCC_except_table7008
- GCC_except_table7009
- GCC_except_table7017
- GCC_except_table7018
- GCC_except_table7019
- GCC_except_table7020
- GCC_except_table7024
- GCC_except_table7034
- GCC_except_table7035
- GCC_except_table7037
- GCC_except_table7039
- GCC_except_table7040
- GCC_except_table7042
- GCC_except_table7043
- GCC_except_table7044
- GCC_except_table7045
- GCC_except_table7047
- GCC_except_table7051
- GCC_except_table7052
- GCC_except_table7053
- GCC_except_table7071
- GCC_except_table7073
- GCC_except_table7076
- GCC_except_table7081
- GCC_except_table7087
- GCC_except_table7116
- GCC_except_table7121
- GCC_except_table7122
- GCC_except_table7126
- GCC_except_table7128
- GCC_except_table713
- GCC_except_table7130
- GCC_except_table7131
- GCC_except_table7133
- GCC_except_table7134
- GCC_except_table7136
- GCC_except_table7147
- GCC_except_table715
- GCC_except_table716
- GCC_except_table7160
- GCC_except_table7168
- GCC_except_table7177
- GCC_except_table7178
- GCC_except_table7179
- GCC_except_table7192
- GCC_except_table7193
- GCC_except_table7196
- GCC_except_table7200
- GCC_except_table7202
- GCC_except_table7220
- GCC_except_table7223
- GCC_except_table7233
- GCC_except_table7250
- GCC_except_table7251
- GCC_except_table7252
- GCC_except_table7253
- GCC_except_table7254
- GCC_except_table7256
- GCC_except_table7257
- GCC_except_table7264
- GCC_except_table7265
- GCC_except_table7267
- GCC_except_table7268
- GCC_except_table7270
- GCC_except_table7271
- GCC_except_table7273
- GCC_except_table7276
- GCC_except_table7280
- GCC_except_table7282
- GCC_except_table7283
- GCC_except_table7285
- GCC_except_table7287
- GCC_except_table7291
- GCC_except_table7293
- GCC_except_table7295
- GCC_except_table7299
- GCC_except_table7301
- GCC_except_table7303
- GCC_except_table7308
- GCC_except_table7309
- GCC_except_table731
- GCC_except_table7315
- GCC_except_table7319
- GCC_except_table732
- GCC_except_table7321
- GCC_except_table7323
- GCC_except_table7326
- GCC_except_table733
- GCC_except_table7331
- GCC_except_table7332
- GCC_except_table7334
- GCC_except_table734
- GCC_except_table7340
- GCC_except_table7344
- GCC_except_table7349
- GCC_except_table7350
- GCC_except_table7359
- GCC_except_table7361
- GCC_except_table7364
- GCC_except_table7365
- GCC_except_table7367
- GCC_except_table7375
- GCC_except_table7376
- GCC_except_table7383
- GCC_except_table7385
- GCC_except_table7394
- GCC_except_table7395
- GCC_except_table7403
- GCC_except_table7415
- GCC_except_table7417
- GCC_except_table7418
- GCC_except_table7419
- GCC_except_table7420
- GCC_except_table7421
- GCC_except_table743
- GCC_except_table7434
- GCC_except_table7435
- GCC_except_table7443
- GCC_except_table7446
- GCC_except_table7456
- GCC_except_table7464
- GCC_except_table7466
- GCC_except_table7468
- GCC_except_table7471
- GCC_except_table7472
- GCC_except_table7473
- GCC_except_table7474
- GCC_except_table7475
- GCC_except_table7481
- GCC_except_table7482
- GCC_except_table7487
- GCC_except_table7489
- GCC_except_table7493
- GCC_except_table7495
- GCC_except_table7503
- GCC_except_table7506
- GCC_except_table7513
- GCC_except_table7516
- GCC_except_table7520
- GCC_except_table7521
- GCC_except_table7523
- GCC_except_table7525
- GCC_except_table7526
- GCC_except_table7544
- GCC_except_table7549
- GCC_except_table7555
- GCC_except_table7556
- GCC_except_table7557
- GCC_except_table7558
- GCC_except_table7559
- GCC_except_table7560
- GCC_except_table7561
- GCC_except_table7562
- GCC_except_table7566
- GCC_except_table7568
- GCC_except_table7569
- GCC_except_table7572
- GCC_except_table7573
- GCC_except_table7574
- GCC_except_table758
- GCC_except_table7581
- GCC_except_table7582
- GCC_except_table7583
- GCC_except_table759
- GCC_except_table7593
- GCC_except_table7609
- GCC_except_table761
- GCC_except_table7611
- GCC_except_table7613
- GCC_except_table7615
- GCC_except_table7616
- GCC_except_table7622
- GCC_except_table7624
- GCC_except_table7651
- GCC_except_table7653
- GCC_except_table7654
- GCC_except_table7655
- GCC_except_table7657
- GCC_except_table7658
- GCC_except_table7659
- GCC_except_table7660
- GCC_except_table7661
- GCC_except_table7668
- GCC_except_table769
- GCC_except_table7695
- GCC_except_table7699
- GCC_except_table7704
- GCC_except_table7706
- GCC_except_table7708
- GCC_except_table771
- GCC_except_table7712
- GCC_except_table7730
- GCC_except_table7731
- GCC_except_table7732
- GCC_except_table774
- GCC_except_table7798
- GCC_except_table7799
- GCC_except_table7800
- GCC_except_table7812
- GCC_except_table7815
- GCC_except_table7816
- GCC_except_table7823
- GCC_except_table7830
- GCC_except_table7831
- GCC_except_table7832
- GCC_except_table7833
- GCC_except_table7834
- GCC_except_table7846
- GCC_except_table7859
- GCC_except_table7862
- GCC_except_table7874
- GCC_except_table7876
- GCC_except_table7877
- GCC_except_table7881
- GCC_except_table7882
- GCC_except_table7883
- GCC_except_table7891
- GCC_except_table7897
- GCC_except_table7898
- GCC_except_table7899
- GCC_except_table7900
- GCC_except_table7903
- GCC_except_table7917
- GCC_except_table7919
- GCC_except_table7920
- GCC_except_table7921
- GCC_except_table7925
- GCC_except_table7927
- GCC_except_table7928
- GCC_except_table7929
- GCC_except_table7932
- GCC_except_table7937
- GCC_except_table7938
- GCC_except_table7944
- GCC_except_table7962
- GCC_except_table7964
- GCC_except_table7965
- GCC_except_table7966
- GCC_except_table7967
- GCC_except_table7969
- GCC_except_table7970
- GCC_except_table7971
- GCC_except_table7972
- GCC_except_table7973
- GCC_except_table7986
- GCC_except_table8
- GCC_except_table8010
- GCC_except_table8018
- GCC_except_table8019
- GCC_except_table8026
- GCC_except_table803
- GCC_except_table8035
- GCC_except_table8053
- GCC_except_table8055
- GCC_except_table806
- GCC_except_table8062
- GCC_except_table8063
- GCC_except_table8065
- GCC_except_table8067
- GCC_except_table8068
- GCC_except_table8069
- GCC_except_table807
- GCC_except_table8071
- GCC_except_table8073
- GCC_except_table8074
- GCC_except_table8075
- GCC_except_table809
- GCC_except_table8093
- GCC_except_table8095
- GCC_except_table8100
- GCC_except_table8106
- GCC_except_table8107
- GCC_except_table8109
- GCC_except_table811
- GCC_except_table8110
- GCC_except_table812
- GCC_except_table8122
- GCC_except_table8125
- GCC_except_table8127
- GCC_except_table8128
- GCC_except_table8140
- GCC_except_table8141
- GCC_except_table8142
- GCC_except_table8159
- GCC_except_table8160
- GCC_except_table8179
- GCC_except_table8198
- GCC_except_table8202
- GCC_except_table8203
- GCC_except_table8204
- GCC_except_table8241
- GCC_except_table8243
- GCC_except_table8244
- GCC_except_table8247
- GCC_except_table8248
- GCC_except_table8249
- GCC_except_table825
- GCC_except_table8252
- GCC_except_table8257
- GCC_except_table8266
- GCC_except_table8269
- GCC_except_table827
- GCC_except_table8271
- GCC_except_table8275
- GCC_except_table8276
- GCC_except_table8281
- GCC_except_table8284
- GCC_except_table8290
- GCC_except_table831
- GCC_except_table8314
- GCC_except_table8315
- GCC_except_table8318
- GCC_except_table8319
- GCC_except_table8321
- GCC_except_table8322
- GCC_except_table8324
- GCC_except_table833
- GCC_except_table8330
- GCC_except_table8333
- GCC_except_table8337
- GCC_except_table8340
- GCC_except_table8345
- GCC_except_table8346
- GCC_except_table8362
- GCC_except_table8363
- GCC_except_table8366
- GCC_except_table8370
- GCC_except_table8371
- GCC_except_table8373
- GCC_except_table8376
- GCC_except_table8377
- GCC_except_table8378
- GCC_except_table8379
- GCC_except_table8380
- GCC_except_table8381
- GCC_except_table8384
- GCC_except_table8385
- GCC_except_table8387
- GCC_except_table8388
- GCC_except_table8392
- GCC_except_table8393
- GCC_except_table8397
- GCC_except_table8398
- GCC_except_table8399
- GCC_except_table840
- GCC_except_table8401
- GCC_except_table8404
- GCC_except_table8410
- GCC_except_table8413
- GCC_except_table8414
- GCC_except_table8415
- GCC_except_table8416
- GCC_except_table8419
- GCC_except_table8422
- GCC_except_table8438
- GCC_except_table8441
- GCC_except_table8442
- GCC_except_table8446
- GCC_except_table8447
- GCC_except_table8464
- GCC_except_table8482
- GCC_except_table8483
- GCC_except_table8485
- GCC_except_table85
- GCC_except_table8505
- GCC_except_table8506
- GCC_except_table8540
- GCC_except_table8543
- GCC_except_table8552
- GCC_except_table8553
- GCC_except_table8554
- GCC_except_table8564
- GCC_except_table8565
- GCC_except_table8578
- GCC_except_table8579
- GCC_except_table8581
- GCC_except_table8582
- GCC_except_table8605
- GCC_except_table8606
- GCC_except_table8612
- GCC_except_table8627
- GCC_except_table8632
- GCC_except_table8638
- GCC_except_table867
- GCC_except_table868
- GCC_except_table8681
- GCC_except_table8683
- GCC_except_table869
- GCC_except_table8690
- GCC_except_table8695
- GCC_except_table8696
- GCC_except_table8697
- GCC_except_table8700
- GCC_except_table8701
- GCC_except_table8707
- GCC_except_table8710
- GCC_except_table8713
- GCC_except_table8714
- GCC_except_table8716
- GCC_except_table8718
- GCC_except_table8719
- GCC_except_table8721
- GCC_except_table8722
- GCC_except_table8728
- GCC_except_table8729
- GCC_except_table8730
- GCC_except_table8731
- GCC_except_table8732
- GCC_except_table8733
- GCC_except_table8735
- GCC_except_table8739
- GCC_except_table8740
- GCC_except_table8741
- GCC_except_table8742
- GCC_except_table8743
- GCC_except_table8744
- GCC_except_table8746
- GCC_except_table8747
- GCC_except_table8748
- GCC_except_table8749
- GCC_except_table8750
- GCC_except_table8751
- GCC_except_table8752
- GCC_except_table8753
- GCC_except_table8756
- GCC_except_table8757
- GCC_except_table8758
- GCC_except_table8759
- GCC_except_table8760
- GCC_except_table8761
- GCC_except_table8762
- GCC_except_table8763
- GCC_except_table8765
- GCC_except_table8767
- GCC_except_table8768
- GCC_except_table8769
- GCC_except_table8770
- GCC_except_table8771
- GCC_except_table8774
- GCC_except_table8775
- GCC_except_table8780
- GCC_except_table8782
- GCC_except_table8783
- GCC_except_table8784
- GCC_except_table8785
- GCC_except_table8786
- GCC_except_table8787
- GCC_except_table8789
- GCC_except_table8792
- GCC_except_table8793
- GCC_except_table8797
- GCC_except_table8798
- GCC_except_table8799
- GCC_except_table8800
- GCC_except_table8803
- GCC_except_table8805
- GCC_except_table8807
- GCC_except_table8819
- GCC_except_table882
- GCC_except_table8820
- GCC_except_table8821
- GCC_except_table8822
- GCC_except_table8823
- GCC_except_table8824
- GCC_except_table8825
- GCC_except_table8826
- GCC_except_table8827
- GCC_except_table8828
- GCC_except_table8829
- GCC_except_table8830
- GCC_except_table8831
- GCC_except_table8833
- GCC_except_table8836
- GCC_except_table8837
- GCC_except_table8841
- GCC_except_table8842
- GCC_except_table8844
- GCC_except_table8845
- GCC_except_table8846
- GCC_except_table8847
- GCC_except_table8848
- GCC_except_table8849
- GCC_except_table8853
- GCC_except_table8854
- GCC_except_table8857
- GCC_except_table8858
- GCC_except_table8863
- GCC_except_table8865
- GCC_except_table8867
- GCC_except_table887
- GCC_except_table8872
- GCC_except_table8875
- GCC_except_table8876
- GCC_except_table8879
- GCC_except_table889
- GCC_except_table8894
- GCC_except_table8902
- GCC_except_table8903
- GCC_except_table8905
- GCC_except_table8906
- GCC_except_table8907
- GCC_except_table8908
- GCC_except_table8909
- GCC_except_table8922
- GCC_except_table8923
- GCC_except_table8937
- GCC_except_table8938
- GCC_except_table894
- GCC_except_table895
- GCC_except_table8954
- GCC_except_table8955
- GCC_except_table896
- GCC_except_table8966
- GCC_except_table897
- GCC_except_table898
- GCC_except_table899
- GCC_except_table901
- GCC_except_table904
- GCC_except_table9042
- GCC_except_table9046
- GCC_except_table905
- GCC_except_table9071
- GCC_except_table9076
- GCC_except_table9078
- GCC_except_table9081
- GCC_except_table9099
- GCC_except_table9100
- GCC_except_table911
- GCC_except_table9116
- GCC_except_table9117
- GCC_except_table9120
- GCC_except_table9121
- GCC_except_table9125
- GCC_except_table9126
- GCC_except_table9129
- GCC_except_table9131
- GCC_except_table9133
- GCC_except_table9134
- GCC_except_table9135
- GCC_except_table9136
- GCC_except_table9138
- GCC_except_table9139
- GCC_except_table9142
- GCC_except_table9145
- GCC_except_table9146
- GCC_except_table9147
- GCC_except_table9148
- GCC_except_table9149
- GCC_except_table9153
- GCC_except_table916
- GCC_except_table9161
- GCC_except_table917
- GCC_except_table9176
- GCC_except_table9179
- GCC_except_table918
- GCC_except_table9181
- GCC_except_table9183
- GCC_except_table9185
- GCC_except_table9186
- GCC_except_table9187
- GCC_except_table919
- GCC_except_table9191
- GCC_except_table9193
- GCC_except_table9194
- GCC_except_table9195
- GCC_except_table9196
- GCC_except_table9198
- GCC_except_table920
- GCC_except_table9200
- GCC_except_table9202
- GCC_except_table9205
- GCC_except_table9206
- GCC_except_table9208
- GCC_except_table9210
- GCC_except_table9211
- GCC_except_table9212
- GCC_except_table9213
- GCC_except_table9214
- GCC_except_table9215
- GCC_except_table9216
- GCC_except_table9223
- GCC_except_table9226
- GCC_except_table9228
- GCC_except_table923
- GCC_except_table9230
- GCC_except_table9234
- GCC_except_table9236
- GCC_except_table9238
- GCC_except_table9240
- GCC_except_table9242
- GCC_except_table9244
- GCC_except_table9248
- GCC_except_table9252
- GCC_except_table9254
- GCC_except_table9256
- GCC_except_table9258
- GCC_except_table926
- GCC_except_table9260
- GCC_except_table9262
- GCC_except_table9264
- GCC_except_table9266
- GCC_except_table9268
- GCC_except_table9270
- GCC_except_table9274
- GCC_except_table9276
- GCC_except_table9278
- GCC_except_table9282
- GCC_except_table9284
- GCC_except_table9286
- GCC_except_table929
- GCC_except_table9292
- GCC_except_table9293
- GCC_except_table9299
- GCC_except_table9301
- GCC_except_table9306
- GCC_except_table9307
- GCC_except_table9310
- GCC_except_table9311
- GCC_except_table9313
- GCC_except_table932
- GCC_except_table9320
- GCC_except_table9370
- GCC_except_table9373
- GCC_except_table9374
- GCC_except_table9376
- GCC_except_table9382
- GCC_except_table9387
- GCC_except_table940
- GCC_except_table9403
- GCC_except_table9407
- GCC_except_table941
- GCC_except_table943
- GCC_except_table9439
- GCC_except_table944
- GCC_except_table945
- GCC_except_table9469
- GCC_except_table9471
- GCC_except_table95
- GCC_except_table951
- GCC_except_table957
- GCC_except_table958
- GCC_except_table959
- GCC_except_table966
- GCC_except_table971
- GCC_except_table974
- GCC_except_table979
- GCC_except_table986
- GCC_except_table988
- GCC_except_table99
- GCC_except_table991
- GCC_except_table993
- GCC_except_table995
- GCC_except_table996
- GCC_except_table998
- GCC_except_table999
- _AQCallbackReceiver_AudioQueueCallbacks_subsystem
- _AQCallbackSender_CallbackNotificationsAvailable
- _AQClient_EnqueueBuffer
- _AQClient_MixerSetProperty
- _AQClient_ProcessingTapInit
- _AQClient_ProcessingTapNew
- _AQClient_ScaleOrUnscaleSampleTime
- _AQClient_SetProperty
- _AQServer_AudioQueueIPC_subsystem
- _AQServer_EnqueueBuffer
- _AQServer_MixerNew
- _AQServer_MixerSetProperty
- _AQServer_NewQueue
- _AQServer_ProcessingTapInit
- _AQServer_ScheduleParameters
- _AQServer_SetOfflineRenderFormat
- _AQServer_SetProperty
- _AUIOServer_StopIO
- _AudioConverterFillComplexBufferWithPacketDependencyInfo
- _AudioQueueCallbacks_server
- _AudioQueueCallbacks_server_routine
- _AudioQueueIPC_server
- _AudioQueueIPC_server_routine
- _AudioSessionRequestApplyInputMute
- _GetAudioDSPManager
- _IOAllowPowerChange
- _IONotificationPortSetDispatchQueue
- _IORegisterForSystemPower
- _MSHCreateMIGServerSource
- _MSHMIGReceiveAndDispatchMessage
- _OBJC_CLASS_$_AVBorealisServer
- _OBJC_CLASS_$_AVBorealisServerHysteresisNotifier
- _OBJC_CLASS_$_AVBorealisServerPortManager
- _OBJC_IVAR_$_AVBorealisServer._afSiriActivationBuiltInMicVoiceFuncPtr
- _OBJC_IVAR_$_AVBorealisServer._clientConnections
- _OBJC_IVAR_$_AVBorealisServer._clsVTStateManager
- _OBJC_IVAR_$_AVBorealisServer._mobileAssistantDylib
- _OBJC_IVAR_$_AVBorealisServer._notificationQueue
- _OBJC_IVAR_$_AVBorealisServer._serverListener
- _OBJC_IVAR_$_AVBorealisServer._voiceTriggerDylib
- _OBJC_IVAR_$_AVBorealisServer._vtStateManager
- _OBJC_IVAR_$_AVBorealisServer.serverImpl
- _OBJC_IVAR_$_AVBorealisServerHysteresisNotifier._portsToMonitor
- _OBJC_IVAR_$_AVBorealisServerHysteresisNotifier._queue
- _OBJC_IVAR_$_AVBorealisServerPortManager._generation
- _OBJC_IVAR_$_AVBorealisServerPortManager._hysteresisDurationSeconds
- _OBJC_IVAR_$_AVBorealisServerPortManager._lastStateSent
- _OBJC_IVAR_$_AVBorealisServerPortManager._listeningEnabled
- _OBJC_IVAR_$_AVBorealisServerPortManager._notificationBlock
- _OBJC_IVAR_$_AVBorealisServerPortManager._portType
- _OBJC_METACLASS_$_AVBorealisServer
- _OBJC_METACLASS_$_AVBorealisServerHysteresisNotifier
- _OBJC_METACLASS_$_AVBorealisServerPortManager
- __OBJC_$_INSTANCE_METHODS_AVBorealisServer
- __OBJC_$_INSTANCE_METHODS_AVBorealisServerHysteresisNotifier
- __OBJC_$_INSTANCE_METHODS_AVBorealisServerPortManager
- __OBJC_$_INSTANCE_VARIABLES_AVBorealisServer
- __OBJC_$_INSTANCE_VARIABLES_AVBorealisServerHysteresisNotifier
- __OBJC_$_INSTANCE_VARIABLES_AVBorealisServerPortManager
- __OBJC_$_PROP_LIST_AVBorealisServer
- __OBJC_$_PROP_LIST_AVBorealisServerHysteresisNotifier
- __OBJC_$_PROP_LIST_AVBorealisServerPortManager
- __OBJC_CLASS_PROTOCOLS_$_AVBorealisServer
- __OBJC_CLASS_RO_$_AVBorealisServer
- __OBJC_CLASS_RO_$_AVBorealisServerHysteresisNotifier
- __OBJC_CLASS_RO_$_AVBorealisServerPortManager
- __OBJC_METACLASS_RO_$_AVBorealisServer
- __OBJC_METACLASS_RO_$_AVBorealisServerHysteresisNotifier
- __OBJC_METACLASS_RO_$_AVBorealisServerPortManager
- __XAddPropertyListener
- __XAllocateBuffer
- __XCallbackNotificationsAvailable
- __XCreateTimeline
- __XDeviceGetCurrentTime
- __XDeviceGetNearestStartTime
- __XDeviceTranslateTime
- __XDisposeQueue
- __XDisposeTimeline
- __XEnqueueBuffer
- __XEnqueueSilence
- __XFlush
- __XFreeBuffer
- __XGetParameter
- __XGetPendingCallbackMessages
- __XGetProperty.13161
- __XGetPropertySize
- __XMixerConnectQueue
- __XMixerDispose
- __XMixerGetProperty
- __XMixerGetPropertySize
- __XMixerNew
- __XMixerRender
- __XMixerReset
- __XMixerSetProperty
- __XNewQueue
- __XOfflineRender
- __XPause
- __XPerformTap
- __XPrime
- __XProcessingTapDispose
- __XProcessingTapGetSourceAudio
- __XProcessingTapInit
- __XProcessingTapNew
- __XProcessingTapPerformReply
- __XProcessingTapRetrieveInfo
- __XQueryServer
- __XQueueGetCurrentTime
- __XRemovePropertyListener
- __XReset
- __XScaleOrUnscaleSampleTime
- __XScheduleParameters
- __XSetOfflineRenderFormat
- __XSetParameter
- __XSetProperty.13160
- __XStart
- __XStop
- __XTerminateTapThread
- __Z13AQMEMessengerv
- __Z13CASIsDarwinOSv
- __Z20CAIsDebuggerAttachedv
- __Z24AudioMetadataFrame_ClearP18AudioMetadataFrame
- __Z24GetBehaviorForSSIDAndPIDjibbPPK14__CFDictionaryj
- __Z24checkNewQueuePermissions13audit_token_tbRK27AudioStreamBasicDescriptionjj
- __Z25AudioSessionCreateSessioniRKNSt3__18optionalI13audit_token_tEE16AudioSessionTypePP15opaqueCMSessionPj
- __Z27AudioMetadataFrame_BeginNewP18AudioMetadataFramePK24AudioMetadataFrameHeader
- __Z28AudioMetadataFrame_GetHeaderPK18AudioMetadataFrame
- __Z30AudioMetadataFrame_AppendEventP18AudioMetadataFramePK18AudioMetadataEvent
- __Z30AudioQueueDefaultDeviceChangedPv
- __Z32AudioBufferList_GetMetadataFramePK15AudioBufferList
- __Z32FeatureFlags_IsOffloadACQEnabledv
- __Z37AQInternalGetOfflineBufferCompletionsjRNSt3__16vectorIjNS_9allocatorIjEEEE
- __Z38AudioQueueSiriListeningPropertyChangedj
- __ZGVZ13AQMEMessengervE6global
- __ZGVZ32FeatureFlags_IsOffloadACQEnabledvE20sIsOffloadACQEnabled
- __ZGVZL34PopulateSourceFormatInfoDictionaryP14__CFDictionaryPKvRK14AQIONodeClientRN2CA17StreamDescriptionEbbbE10sessionMap
- __ZGVZN10AQMEIO_HAL6IOProcEPK15AudioBufferListPK14AudioTimeStampPS0_S5_E14isVirtualAudio
- __ZGVZN17BorealisManagerV28instanceEvE8instance
- __ZGVZN2AQ6Server4Base15defaultInstanceEiRN2AT9MixServer4BaseEE6legacy
- __ZL11CPMSLibraryv.3102
- __ZL11CPMSLibraryv.9547
- __ZL11getAQServerv
- __ZL12GetClientPIDR13audit_token_t
- __ZL12_CreateLocksv
- __ZL14kBorealisScope
- __ZL15gHasBorealisXPC
- __ZL15sBorealisServer
- __ZL16audit_stringCPMS.3120
- __ZL16audit_stringCPMS.5574
- __ZL16audit_stringCPMS.9562
- __ZL16gBorealisCapture
- __ZL17kNewBorealisScope
- __ZL18gAhapForSSSEnabled
- __ZL18gCaptureRecordings
- __ZL18gIOBufferFrameSize
- __ZL19Impl_AllocateBuffer13audit_token_tjRPvjRP28AudioStreamPacketDescriptionjPjS5_
- __ZL19gBufferSerialNumber
- __ZL19gOfflineMixerClient
- __ZL19gWorkThreadPriority
- __ZL20AudioQueueClientInitv
- __ZL20CoreMediaLibraryCorePPc.6317
- __ZL20gLinkedBeforeCAS_492
- __ZL20getBundleIDOrDefaultjPKc
- __ZL21audit_stringCoreMedia.4378
- __ZL21audit_stringCoreMedia.6326
- __ZL21gAQClientCaptureInput
- __ZL22gAQClientCaptureOutput
- __ZL23MediaToolboxLibraryCorePPc.6307
- __ZL24audit_stringMediaToolbox.6316
- __ZL26gRingBufferCapacitySeconds
- __ZL29gAQClientCaptureOfflineRender
- __ZL30audit_stringAudioSessionServer.7538
- __ZL30gBorealisCaptureRingBufferMode
- __ZL33getCMBaseObjectGetVTableSymbolLocv.6318
- __ZL58getFigCPECryptorCreateCryptorFromSerializedRecipeSymbolLocv.6308
- __ZL7gAQOnce.11557
- __ZL8sSSSOnce
- __ZL9PlaySoundjP19SSClientPlayOptionsPhjj
- __ZN10AQMEIO_DSP14AdaptToVARouteEPK14__CFDictionarybb
- __ZN10AQMEIO_DSP23AccessProcessorPropertyE13MEProcessorIDjbRjPv
- __ZN10CACFStringaSEPK10__CFString
- __ZN10applesauce2CF10BooleanRefD1Ev
- __ZN10applesauce2CF11TypeRefPairC2IRA5_KcNS0_7DataRefEEEOT_OT0_
- __ZN10applesauce2CF11TypeRefPairC2IRKNSt3__112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEERKNS0_7TypeRefEEEOT_OT0_
- __ZN10applesauce2CF13DataRef_proxy15get_byte_lengthEv
- __ZN10applesauce2CF13DictionaryRefaSERKS1_
- __ZN10applesauce2CF6URLRefD1Ev
- __ZN10applesauce2CF7DataRefaSEDn
- __ZN10applesauce2CF9ObjectRefIPK10__CFNumberED1Ev
- __ZN10applesauce2CF9ObjectRefIPK11__CFBooleanED1Ev
- __ZN10applesauce2CF9ObjectRefIPK14__CFDictionaryED1Ev
- __ZN10applesauce2CF9ObjectRefIPK7__CFURLED1Ev
- __ZN10applesauce2CF9ObjectRefIPK8__CFDataED1Ev
- __ZN10applesauce2CF9ObjectRefIPK9__CFArrayED1Ev
- __ZN10applesauce2CF9StringRef9from_copyEPK10__CFString
- __ZN10applesauce2CF9StringRefC1ENSt3__117basic_string_viewIcNS2_11char_traitsIcEEEE
- __ZN10applesauce2CF9StringRefC1ERKS1_
- __ZN10applesauce3xpc5array8iteratorC2ES1_m
- __ZN10applesauce3xpc8endpointC1ERKS1_
- __ZN10applesauce8dispatch2v15queueD1Ev
- __ZN10applesauce8dispatch2v1eqERKNS1_5blockIFiPK15AudioBufferListS5_PS3_jEEESA_
- __ZN11AQClientMgr10ServerDiedEi
- __ZN11AQClientMgr10ServerPortEv
- __ZN11AQClientMgr6Server14ServerPortDiedEi
- __ZN11AQClientMgr6ServerD0Ev
- __ZN11AQClientMgr6ServerD1Ev
- __ZN11AQMESessionC1ERKS_
- __ZN11AQTapIONode15BorealisToggledEv
- __ZN11CAFormatterC1EPKvi
- __ZN11ClientEntry17doPrepareSequenceENSt3__110shared_ptrI14HapticSequenceEENS0_8functionIFvmEEE
- __ZN11ClientEntry19handleSequenceEndedEmNSt3__18functionIFvmEEE
- __ZN11DSP_RoutingC2ER10AQMEIO_DSPNS_12ERoutingTypeE
- __ZN11HapticMutex3TryERb
- __ZN11HapticMutex4LockEv
- __ZN11HapticMutex6UnlockEv
- __ZN11HapticMutexD0Ev
- __ZN11HapticMutexD1Ev
- __ZN11MEConnector11SetSTSLabelERKN10applesauce2CF9StringRefE
- __ZN11MidiDataRef18CountedMidiDataRefD0Ev
- __ZN11MidiDataRef18CountedMidiDataRefD1Ev
- __ZN11MidiDataRef18CountedMidiDataRefnwEmm
- __ZN11MidiDataRefaSERKS_
- __ZN11SSClientIPC13PlayWithFlagsEjP19SSClientPlayOptionsPhjbj
- __ZN11TOpaqueRTTII14AQRemoteClientE5sRTTIE
- __ZN11TOpaqueRTTII16ClientAudioQueueE5sRTTIE
- __ZN11TOpaqueRTTII19ClientProcessingTapE5sRTTIE
- __ZN11TOpaqueRTTII20ClientAQOfflineMixerE5sRTTIE
- __ZN11TOpaqueRTTII20DSP_Routing_BorealisE5sRTTIE
- __ZN12CADeprecated10TSingletonI11AQClientMgrE5sOnceE
- __ZN12CADeprecated10TSingletonI11AQClientMgrE8instanceEv
- __ZN12CADeprecated10TSingletonI11AQClientMgrE9sInstanceE
- __ZN12CADeprecated10TSingletonI13HapticMetricsE8instanceEv
- __ZN12CADeprecated10TSingletonI15BorealisManagerE5sOnceE
- __ZN12CADeprecated10TSingletonI15BorealisManagerE8instanceEv
- __ZN12CADeprecated10TSingletonI15BorealisManagerE9sInstanceE
- __ZN12CADeprecated10TSingletonI15SSSPowerManagerE5sOnceE
- __ZN12CADeprecated10TSingletonI15SSSPowerManagerE8instanceEv
- __ZN12CADeprecated10TSingletonI15SSSPowerManagerE9sInstanceE
- __ZN12CADeprecated10TSingletonI26ClientProcessingTapManagerE5sOnceE
- __ZN12CADeprecated10TSingletonI26ClientProcessingTapManagerE8instanceEv
- __ZN12CADeprecated10TSingletonI26ClientProcessingTapManagerE9sInstanceE
- __ZN12CADeprecated12CABufferList28VerifyNotTrashingOwnedBufferEv
- __ZN12CADeprecated15XBasicMIGServer16GetRunLoopSourceEv
- __ZN12CADeprecated16XMachReceivePort11SetMachPortEj
- __ZN12CADeprecated16XMachReceivePort14CreateMachPortEi
- __ZN12CADeprecated16XMachReceivePortD1Ev
- __ZN12CADeprecated17RealtimeMessenger12PerformAsyncERNS0_7MessageE
- __ZN12CADeprecated17RealtimeMessengerC2EN10applesauce8dispatch2v15queueE
- __ZN12CADeprecated17XMachPortServicer11RunLoopImplD0Ev
- __ZN12CADeprecated17XMachPortServicer11RunLoopImplD1Ev
- __ZN12CADeprecated17XMachPortServicer11RunLoopImplD2Ev
- __ZN12CADeprecated17XRemoteMachServer12GetDebugNameEv
- __ZN12CADeprecated17XRemoteMachServer13SetServerPortEji
- __ZN12CADeprecated17XRemoteMachServer8PortDiedEj
- __ZN12CADeprecated17XRemoteMachServerC2EPKcS2_
- __ZN12CADeprecated17XRemoteMachServerD2Ev
- __ZN12CADeprecated18XMachPortRefCounts4cstrEv
- __ZN12CADeprecated18XMachPortRefCountsC2Ej
- __ZN12CADeprecated18XMachPortSendRight11SetMachPortEj
- __ZN12CADeprecated20GenericRunLoopThread13PerformSourceEPv
- __ZN12CADeprecated20GenericRunLoopThread5EntryEPv
- __ZN12CADeprecated20GenericRunLoopThread5StartEv
- __ZN12CADeprecated20GenericRunLoopThreadD0Ev
- __ZN12CADeprecated20GenericRunLoopThreadD1Ev
- __ZN12CADeprecated20GenericRunLoopThreadD2Ev
- __ZN12CADeprecated22XMachPortDeathListenerC2Ev
- __ZN12CADeprecated7CAMutex5TryerD2Ev
- __ZN12CADeprecated7CAMutexC2EPKc
- __ZN12CADeprecated7CAMutexD2Ev
- __ZN12CADeprecated9CAPThread11SetPriorityEjb
- __ZN12CADeprecated9CAPThreadC1EPFPvS1_ES1_jbbPKc
- __ZN13MESubmixGraph20_connectInputChannelERS_S0_bP14MEMixerChannelb
- __ZN13MESubmixGraphC2ERK17AudioTapSpecifieriR10AQMEDeviceR20MEOutputStreamClientb
- __ZN13QueueAccessor40SetSessionPlayStateToStopped_PreDeletionEv
- __ZN13QueueAccessorD2Ev
- __ZN13SSSPlayerList9AddPlayerEP19SSSActionPlayerBase
- __ZN13ServerManager15prepareSequenceENSt3__110shared_ptrI11ClientEntryEEmNS0_8functionIFvmEEE
- __ZN13ServerManager34cancelFutureParameterCurveOfSameIDENSt3__110shared_ptrI11ClientEntryEERK13HapticCommand
- __ZN13TOpaqueObjectI14RemoteIOClientjN12CADeprecated11XMachServer6ClientEED2Ev
- __ZN13TOpaqueObjectI16ClientAudioQueueP16OpaqueAudioQueue16BaseOpaqueObjectED0Ev
- __ZN13TOpaqueObjectI16ClientAudioQueueP16OpaqueAudioQueue16BaseOpaqueObjectED1Ev
- __ZN14AQIONodeClient15setOwnerSessionERK11AQMESession
- __ZN14AQIONodeClient25MovieModeMuteStateChangedEv
- __ZN14AQInputChunkerC2EPFvPvP12AQInputChunkES0_
- __ZN14AQRemoteClient13queueDisposedEj
- __ZN14AQRemoteClient35IssueNotificationsAvailableCallbackEj
- __ZN14AQRemoteClient36InvokeSubmixTapFormatChangedCallbackEj
- __ZN14AQRemoteClientD0Ev
- __ZN14AQRemoteClientD1Ev
- __ZN14AQRemoteClientD2Ev
- __ZN14AudioUnitGraph12AddLiveEventERK22AUGraphLiveUpdateEvent
- __ZN14CAExternalLockD0Ev
- __ZN14CAExternalLockD1Ev
- __ZN14DSP_Routing_VP8UpstreamD1Ev
- __ZN14MEMixerChannel11SetSTSLabelERKN10applesauce2CF9StringRefE
- __ZN14MEMixerChannel14TimePitchStateD1Ev
- __ZN14MEMixerChannel15_CombineVolumesExRb
- __ZN14MEMixerChannel16ForEachTapSubmixEN5caulk12function_refIFvR9TapSubmixibEEE
- __ZN14MEMixerChannel17AddProcessingNodeERK16AQProcessingNode
- __ZN14MEMixerChannel31RegisterSpatializerWithSTSLabelEv
- __ZN14MixTapToUplink16AQMETapConnector6CreateERS_NSt3__113unordered_mapIjiNS2_4hashIjEENS2_8equal_toIjEENS2_9allocatorINS2_4pairIKjiEEEEEE
- __ZN14MixTapToUplink37UnregisterMutedSpeechActivityListenerEv
- __ZN14MixTapToUplink9CreateTapERKNSt3__113unordered_mapIjiNS0_4hashIjEENS0_8equal_toIjEENS0_9allocatorINS0_4pairIKjiEEEEEE
- __ZN14ReferenceCount13releaseObjectEv
- __ZN14RemoteIOClient18OutputIONodeClient25MovieModeMuteStateChangedEv
- __ZN14SSSClientEntry19handleSequenceEndedEmNSt3__18functionIFvmEEE
- __ZN14SequenceChaserD1Ev
- __ZN15AQIONodeManager15BorealisToggledEv
- __ZN15AQMixEngine_VAD13ForAllDevicesERKNSt3__18functionIFvR10AQMEDeviceEEE
- __ZN15AQMixEngine_VAD15BorealisToggledEv
- __ZN15AQProcessingTap17PortDeathListener12GetDebugNameEv
- __ZN15AQProcessingTap17PortDeathListener8PortDiedEj
- __ZN15AQProcessingTap17PortDeathListenerD0Ev
- __ZN15AQProcessingTap17PortDeathListenerD1Ev
- __ZN15AQProcessingTapC2ER16AudioQueueObjectN2AQ20ProcessingTapIPCTypeEji13MEProcessorIDjbRK24CAStreamBasicDescription
- __ZN15ActiveSoundList23RegisterSoundCompletionEj27ActiveSoundCompletedPortion
- __ZN15BorealisManager13_shouldRunNowEv
- __ZN15BorealisManager14heySiriEnabledEv
- __ZN15BorealisManager17_fetchSiriEnabledEb
- __ZN15BorealisManager20_fetchHeySiriEnabledEv
- __ZN15BorealisManager28hardwareSupportsVoiceTriggerEv
- __ZN15CACFPreferences15CopyStringValueEPK10__CFStringbb
- __ZN15CACFPreferences18CopyMultipleValuesEPK9__CFArraybb
- __ZN15InputDispatcher13DispatchInputERK14AudioTimeStampjRK15AudioBufferList
- __ZN15InputDispatcher17AddProcessingNodeERK16AQProcessingNode
- __ZN15SSSPowerManager14sDispatchQueueE
- __ZN15SSSPowerManager20sPowerManagementPortE
- __ZN15SSSPowerManager23PowerManagementCallbackEPvjjS0_
- __ZN15SSSPowerManager34sPendingPowerChangeNotificationIDsE
- __ZN16AQMixEngine_Base10DebugPrintEP7__sFILEPKc
- __ZN16AQMixEngine_Base17AddProcessingNodeER14AQIONodeClientRK16AQProcessingNode
- __ZN16AQMixEngine_Base17AsAQMixEngine_VADEv
- __ZN16AudioQueueObject13EnqueueBufferEP16AudioQueueBufferjPK28AudioStreamPacketDescriptioniijP24AudioQueueParameterEventRK15XAudioTimeStampPS7_
- __ZN16AudioQueueObject13OfflineRenderERK15XAudioTimeStampP16AudioQueueBufferjRNSt3__16vectorIjNS5_9allocatorIjEEEE
- __ZN16AudioQueueObject13ScheduleFlushEv
- __ZN16AudioQueueObject15GetPropertySizeEjRj
- __ZN16AudioQueueObject16ScheduleDisposalEb
- __ZN16AudioQueueObject17PlaySliceCompleteEPvPN20ScheduledSlicePlayer20XScheduledAudioSliceE
- __ZN16AudioQueueObject19AddPropertyListenerEj
- __ZN16AudioQueueObject19CreateProcessingTapEN2AQ20ProcessingTapIPCTypeEjiRjS2_R27AudioStreamBasicDescription
- __ZN16AudioQueueObject19DeviceTranslateTimeERK15XAudioTimeStampRS0_
- __ZN16AudioQueueObject19GetCurrentQueueTimeEiR15XAudioTimeStampRb
- __ZN16AudioQueueObject19ResetSubsessionMuteEv
- __ZN16AudioQueueObject20DisposeProcessingTapEP15AQProcessingTap
- __ZN16AudioQueueObject20GetCurrentDeviceTimeER15XAudioTimeStamp
- __ZN16AudioQueueObject22RemovePropertyListenerEj
- __ZN16AudioQueueObject23InitializeProcessingTapEP15AQProcessingTapyjRjS2_R27AudioStreamBasicDescriptionPjPN19SharableMemoryBlock15MachServerTokenEPN10applesauce3xpc6objectERNSt3__18optionalIN5caulk4mach20os_workgroup_managedEEE
- __ZN16AudioQueueObject23ScheduledSliceAllocator9FreeSliceEPNS_14ScheduledSliceE
- __ZN16AudioQueueObject23ScheduledSliceAllocatorC2ERKN2CA17StreamDescriptionEj
- __ZN16AudioQueueObject24ScaleOrUnscaleSampleTimeEbd
- __ZN16AudioQueueObject25DeviceGetNearestStartTimeER15XAudioTimeStampj
- __ZN16AudioQueueObject25MovieModeMuteStateChangedEv
- __ZN16AudioQueueObject26SetCodecLoudnessParametersEPNS_19ConverterConnectionE
- __ZN16AudioQueueObject4StopEbbPi
- __ZN16AudioQueueObjectC1ER15AQIONodeManagerbRK27AudioStreamBasicDescriptionjNSt3__110shared_ptrIN2AQ6Server16RemoteClientBaseEEEP15AudioQueueOwnerRK11AQMESession13audit_token_tRi
- __ZN16ClientAudioQueue11PrintObjectEP7__sFILE
- __ZN16ClientAudioQueue16CheckStopCaptureEb
- __ZN16ClientAudioQueue18CallOutputCallbackEP16AudioQueueBuffer
- __ZN16ClientAudioQueue24AwaitAllPendingCallbacksEb
- __ZN16ClientAudioQueue24ChangeBufferEnqueueCountEi
- __ZN16ClientAudioQueue31FetchAndDeliverPendingCallbacksEj
- __ZN16ClientAudioQueueD0Ev
- __ZN16ClientAudioQueueD1Ev
- __ZN16ClientAudioQueueD2Ev
- __ZN16TCustomAllocatedI16XAtomicAllocator9AQCommandEdlEPv
- __ZN16XAtomicAllocator5allocEv
- __ZN16XAtomicAllocator7reserveEi
- __ZN17AudioTapInterface23setupScreenSharingStateEv
- __ZN17AudioTapInterfaceD1Ev
- __ZN17AudioTapSpecifierC2Ev
- __ZN17BorealisManagerV210InitializeEv
- __ZN17BorealisManagerV210initializeEv
- __ZN17BorealisManagerV214HeySiriEnabledEv
- __ZN17BorealisManagerV214hasBorealisXPCEv
- __ZN17BorealisManagerV216useBorealisRouteEv
- __ZN17BorealisManagerV225SpeechDetectionVADCreatedEv
- __ZN17BorealisManagerV228SiriClientRecordStateChangedEb
- __ZN17BorealisManagerV228hardwareSupportsVoiceTriggerEv
- __ZN17BorealisManagerV28instanceEv
- __ZN17BorealisManagerV2C1Ev
- __ZN17BorealisManagerV2C2Ev
- __ZN18AQMixEngine_Single13ForAllDevicesERKNSt3__18functionIFvR10AQMEDeviceEEE
- __ZN18AQOfflineMixerBase11GetPropertyEjR12CASerializer
- __ZN18AQOfflineMixerBase11SetPropertyEjR14CADeserializer
- __ZN18AQOfflineMixerBase12ConnectQueueEjb
- __ZN18AQOfflineMixerBase15GetPropertySizeEjRj
- __ZN18AQOfflineMixerBase18ScheduleQueueStartEjRK15XAudioTimeStamp
- __ZN18AQOfflineMixerBase5ResetEx
- __ZN18AQOfflineMixerBaseC2ER15AQIONodeManageriRK27AudioStreamBasicDescriptionRKN2CA13ChannelLayoutERi
- __ZN18BorealisServerImpl10InitializeEv
- __ZN18BorealisServerImpl15isAOPConfiguredEv
- __ZN18BorealisServerImpl17enableBargeInModeEbU13block_pointerFvP7NSErrorE
- __ZN18BorealisServerImpl21enableListeningOnPortEmb
- __ZN18BorealisServerImpl21fetchAssistantEnabledEb
- __ZN18BorealisServerImpl22getCachedPortStateInfoEv
- __ZN18BorealisServerImpl22safeUpdatePrefWithLockEU13block_pointerFvvERbS2_S2_S2_
- __ZN18BorealisServerImpl26GetSpeechDetectionDeviceIDE33BorealisServerSpeechDeviceUIDTypePi
- __ZN18BorealisServerImpl27assistantPrefsChangedNoLockEbb
- __ZN18BorealisServerImpl27enableVoiceTriggerListeningEbbU13block_pointerFvP7NSErrorE
- __ZN18BorealisServerImpl30notifyAOPListeningStateChangedEj
- __ZN18BorealisServerImpl32getDictionaryForPropertySelectorEj33BorealisServerSpeechDeviceUIDTypePi
- __ZN18BorealisServerImpl33fetchAssistantVoiceTriggerEnabledEv
- __ZN18BorealisServerImpl38createAndActivateSecureSessionIfNeededEv
- __ZN18BorealisServerImpl40registerStateChangedNotificationHandlersEb
- __ZN18BorealisServerImpl41deactivateAndDestroySecureSessionIfExistsEv
- __ZN18BorealisServerImpl42registerAOPVoiceTriggerNotificationHandlerEjb
- __ZN18BorealisServerImpl43registerAOPEnableChangedNotificationHandlerEb
- __ZN18BorealisServerImplD0Ev
- __ZN18BorealisServerImplD1Ev
- __ZN18BorealisServerImplD2Ev
- __ZN18CAReferenceCounted8RetainerD2Ev
- __ZN18CAReferenceCountedD0Ev
- __ZN18CAReferenceCountedD1Ev
- __ZN18MixTapToUplinkHost29EnableMixTapToTelephonyUplinkERKNSt3__113unordered_mapIjiNS0_4hashIjEENS0_8equal_toIjEENS0_9allocatorINS0_4pairIKjiEEEEEE
- __ZN18MixTapToUplinkHost30DisableMixTapToTelephonyUplinkENSt3__18optionalIbEE
- __ZN18MixTapToUplinkHost48IsMixTapToTelephonyUplinkDisabledByScreenSharingEv
- __ZN18MixTapToUplinkHost71SetProxyMutedSpeechActivityListenerOnMutedSpeechActivityManagerProviderEv
- __ZN18ParameterFormatterC2EjPK24AudioQueueParameterEvent
- __ZN18SSSCallbackMessage25RealtimeMessenger_PerformEv
- __ZN18SharableMemoryBase3SetEPvm
- __ZN19ClientProcessingTap11PrintObjectEP7__sFILE
- __ZN19ClientProcessingTap7InitTapER27AudioStreamBasicDescriptionjRN19SharableMemoryBlock11ClientTokenEj
- __ZN19ClientProcessingTapC2EjjjRK27AudioStreamBasicDescriptionPFvPvP29OpaqueAudioQueueProcessingTapjP14AudioTimeStampPjS8_P15AudioBufferListES3_
- __ZN19ClientProcessingTapD0Ev
- __ZN19ClientProcessingTapD1Ev
- __ZN19ClientProcessingTapD2Ev
- __ZN19MEInputStreamClient21MaintainBorealisStateEbi
- __ZN19MESchedulingVectorsD1Ev
- __ZN19SequenceDestination18FinishTrackChasingEP13SequenceTrack
- __ZN19SharableMemoryBlock15MachClientToken5ResetEv
- __ZN19SharableMemoryBlock15MachClientTokenD0Ev
- __ZN19SharableMemoryBlock15MachClientTokenD1Ev
- __ZN19SharableMemoryBlock15MachClientTokenD2Ev
- __ZN20AudioPriorityManager34getActiveMediumPriorityClientCountEv
- __ZN20CA_UISoundClientBaseC2EdjPK14__CFDictionaryj
- __ZN20ClientAQOfflineMixer11PrintObjectEP7__sFILE
- __ZN20ClientAQOfflineMixerD0Ev
- __ZN20ClientAQOfflineMixerD1Ev
- __ZN20ClientMessageHandler14FindBufferByIDEj
- __ZN20ClientMessageHandler15PropertyChangedEj
- __ZN20ClientMessageHandler19InputBufferCompleteEjjRK15XAudioTimeStampjPK28AudioStreamPacketDescription
- __ZN20ClientMessageHandler20OutputBufferCompleteEj
- __ZN20ClientMessageHandlerD0Ev
- __ZN20ClientMessageHandlerD1Ev
- __ZN20DSP_Routing_Borealis10DebugPrintEP7__sFILE
- __ZN20DSP_Routing_Borealis10InitializeEv
- __ZN20DSP_Routing_Borealis11PrintObjectEP7__sFILE
- __ZN20DSP_Routing_Borealis12CheckStartIOEv
- __ZN20DSP_Routing_Borealis13SpeakerStream16IO_PerformOutputEiR15AudioBufferListRK14AudioTimeStamp
- __ZN20DSP_Routing_Borealis13SpeakerStreamD0Ev
- __ZN20DSP_Routing_Borealis13SpeakerStreamD1Ev
- __ZN20DSP_Routing_Borealis16uninitializeImplEv
- __ZN20DSP_Routing_Borealis20VTStateManagerChangeEb
- __ZN20DSP_Routing_Borealis23AccessProcessorPropertyE13MEProcessorIDjbRjPv
- __ZN20DSP_Routing_Borealis23ChangeIOBufferFrameSizeEi
- __ZN20DSP_Routing_Borealis34IsVoiceTriggerAvailablePropertySetEv
- __ZN20DSP_Routing_Borealis3AOP21enableAOPVoiceTriggerEb
- __ZN20DSP_Routing_Borealis3AOP35registerAOPVoiceTriggerNotificationEb
- __ZN20DSP_Routing_Borealis9MicStream15IO_PerformInputEiRK15AudioBufferListRK14AudioTimeStamp
- __ZN20DSP_Routing_Borealis9MicStreamD0Ev
- __ZN20DSP_Routing_Borealis9MicStreamD1Ev
- __ZN20DSP_Routing_BorealisD0Ev
- __ZN20DSP_Routing_BorealisD1Ev
- __ZN20DSP_Routing_BorealisD2Ev
- __ZN20MEDeviceStreamClientC2ER10AQMEDevice14MEStreamTypeID
- __ZN20MEOutputStreamClient21MaintainBorealisStateEbi
- __ZN20ScheduledSlicePlayer13ClearScheduleEv
- __ZN20ScheduledSlicePlayer13ReleaseBufferEPNS_20XScheduledAudioSliceEi
- __ZN20ScheduledSlicePlayer14BufferCompleteEPNS_20XScheduledAudioSliceEx
- __ZN20ScheduledSlicePlayer18DoResolveStartTimeERK15XAudioTimeStampi
- __ZN20ScheduledSlicePlayer20CurrentEndOfTimelineEv
- __ZN20ScheduledSlicePlayer6RenderERK15XAudioTimeStampiR15AudioBufferListb
- __ZN20ScheduledSlicePlayer9CopySliceExPNS_20XScheduledAudioSliceEiR15AudioBufferListiib
- __ZN20ScheduledSlicePlayer9ZeroSliceER15AudioBufferListii
- __ZN20ScheduledSlicePlayerD0Ev
- __ZN20ScheduledSlicePlayerD1Ev
- __ZN20ScheduledSlicePlayerD2Ev
- __ZN21HapticPriorityManager34getActiveMediumPriorityClientCountEv
- __ZN21IPCAUSharedMemoryBase10InitClientEPK27AudioStreamBasicDescriptionjjRN19SharableMemoryBlock11ClientTokenE
- __ZN21MIGVariableLengthVarsD0Ev
- __ZN21MIGVariableLengthVarsD1Ev
- __ZN21PlatformUtilities_iOS13ProductIsiPadEv
- __ZN21PlatformUtilities_iOS15IsInternalBuildEv
- __ZN21PlatformUtilities_iOS15ProductIsAPhoneEv
- __ZN21PlatformUtilities_iOS16ProductIsAppleTVEv
- __ZN21PlatformUtilities_iOS16ProductIsHomePodEv
- __ZN21PlatformUtilities_iOS19ProductIsAppleWatchEv
- __ZN21PlatformUtilities_iOS32ProductSupportsClosedLoopHapticsEv
- __ZN21ResourcePathUtilitiesL14CFDictFromPathERKN10applesauce2CF9StringRefE.2365
- __ZN21ResourcePathUtilitiesL19ResolveResourcePathERKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEES8_.2364
- __ZN21SharedAudioBufferList13ForClientOnlyEPKc
- __ZN21SharedAudioBufferList13ForServerOnlyEPKc
- __ZN21SharedAudioBufferList14PrepareToWriteERK24CAStreamBasicDescriptionjjRP15AudioBufferListRP28AudioStreamPacketDescriptionjRN19SharableMemoryBlock11ServerTokenE
- __ZN21SharedAudioBufferList20GetABLAndPacketDescsERP15AudioBufferListRjRP28AudioStreamPacketDescription
- __ZN22MIGVariableLengthVars2IA1024_hED0Ev
- __ZN22MIGVariableLengthVars2IA1024_hED1Ev
- __ZN22SpatializationLoggerV1D1Ev
- __ZN22SpatializationLoggerV2D1Ev
- __ZN25AUNodeSequenceDestination18FinishTrackChasingEP13SequenceTrack
- __ZN26MutedSpeechActivityManager35SetProxyMutedSpeechActivityListenerERKNSt3__110unique_ptrI14MixTapToUplinkNS0_14default_deleteIS2_EEEE
- __ZN26MutedSpeechActivityManager4Impl35GetProxyMutedSpeechActivityListenerENS0_10ClientTypeE
- __ZN26SSClientCompletionProcInfoD2Ev
- __ZN28AQClientCallbackMessageQueue26GetPendingCallbackMessagesEP21MIGVariableLengthRefsPN4swix4dataE
- __ZN29AQClientCallbackMessageReader17DispatchCallbacksEPKvm
- __ZN29AudioSessionPropertyListeners11sStateMutexE
- __ZN29AudioSessionPropertyListeners13GetStateMutexEv
- __ZN2AQ3API10LegacyImpl13AudioQueueNewEbPK27AudioStreamBasicDescriptionRKNS0_13QueueCallbackERK16CACallbackTargetjjPP16OpaqueAudioQueue
- __ZN2AQ3API10LegacyImpl14ATSubmixTapNewEPFvPvP17OpaqueATSubmixTapjP14AudioTimeStampPjS7_P15AudioBufferListEPFvS2_S4_j27AudioStreamBasicDescriptionES2_jS7_PSC_PS4_
- __ZN2AQ3API10LegacyImpl14AllocateBufferEP16OpaqueAudioQueuePvjP28AudioStreamPacketDescriptionjPP16AudioQueueBuffer
- __ZN2AQ3API10LegacyImpl14AudioQueueStopEP16OpaqueAudioQueueh
- __ZN2AQ3API10LegacyImpl15AudioQueueFlushEP16OpaqueAudioQueue
- __ZN2AQ3API10LegacyImpl15AudioQueuePauseEP16OpaqueAudioQueue
- __ZN2AQ3API10LegacyImpl15AudioQueuePrimeEP16OpaqueAudioQueuejPj
- __ZN2AQ3API10LegacyImpl15AudioQueueResetEP16OpaqueAudioQueue
- __ZN2AQ3API10LegacyImpl17AQOfflineMixerNewEPK27AudioStreamBasicDescriptionPK18AudioChannelLayoutjPP20OpaqueAQOfflineMixer
- __ZN2AQ3API10LegacyImpl17AudioQueueDisposeEP16OpaqueAudioQueueh
- __ZN2AQ3API10LegacyImpl18ATSubmixTapDisposeEP17OpaqueATSubmixTap
- __ZN2AQ3API10LegacyImpl18ATSubmixTapGetTimeEP17OpaqueATSubmixTapPdPjS4_S5_PvS5_
- __ZN2AQ3API10LegacyImpl19AQOfflineMixerResetEP20OpaqueAQOfflineMixerx
- __ZN2AQ3API10LegacyImpl19ATAssignToSubmixTapEP16OpaqueAudioQueueP17OpaqueATSubmixTap
- __ZN2AQ3API10LegacyImpl20AQOfflineMixerRenderEP20OpaqueAQOfflineMixerjPjP15AudioBufferListP28AudioStreamPacketDescriptionP31AudioStreamPacketDependencyInfoPh
- __ZN2AQ3API10LegacyImpl20AudioQueueFreeBufferEP16OpaqueAudioQueueP16AudioQueueBuffer
- __ZN2AQ3API10LegacyImpl21AQOfflineMixerDisposeEP20OpaqueAQOfflineMixer
- __ZN2AQ3API10LegacyImpl21AudioQueueGetPropertyEP16OpaqueAudioQueuejPvPj
- __ZN2AQ3API10LegacyImpl21AudioQueueSetPropertyEP16OpaqueAudioQueuejPKvj
- __ZN2AQ3API10LegacyImpl22AudioQueueGetParameterEP16OpaqueAudioQueuejPf
- __ZN2AQ3API10LegacyImpl22AudioQueueSetParameterEP16OpaqueAudioQueuejf
- __ZN2AQ3API10LegacyImpl23ATSubmixTapNew_CMClientEP33OpaqueATSubmixDestinationQueueTapPFvPvP17OpaqueATSubmixTapjP14AudioTimeStampPjS9_P15AudioBufferListEPFvS4_S6_j27AudioStreamBasicDescriptionES4_jS9_PSE_PS6_
- __ZN2AQ3API10LegacyImpl23ATSubmixTapNew_CMServerEijP27AudioStreamBasicDescriptionPP33OpaqueATSubmixDestinationQueueTapPP17OpaqueATSubmixTap
- __ZN2AQ3API10LegacyImpl23AudioQueueOfflineRenderEP16OpaqueAudioQueuePK14AudioTimeStampP16AudioQueueBufferj
- __ZN2AQ3API10LegacyImpl24AudioQueueCreateTimelineEP16OpaqueAudioQueuePP24OpaqueAudioQueueTimeline
- __ZN2AQ3API10LegacyImpl24AudioQueueEnqueueSilenceEP16OpaqueAudioQueuejx
- __ZN2AQ3API10LegacyImpl24AudioQueueGetCurrentTimeEP16OpaqueAudioQueueP24OpaqueAudioQueueTimelineP14AudioTimeStampPh
- __ZN2AQ3API10LegacyImpl24AudioQueueStartWithFlagsEP16OpaqueAudioQueuePK14AudioTimeStampj
- __ZN2AQ3API10LegacyImpl25AQOfflineMixerGetPropertyEP20OpaqueAQOfflineMixerjPvPj
- __ZN2AQ3API10LegacyImpl25AQOfflineMixerSetPropertyEP20OpaqueAQOfflineMixerjPKvj
- __ZN2AQ3API10LegacyImpl25ATSubmixTapGetSourceAudioEP17OpaqueATSubmixTapjP14AudioTimeStampPjS6_P15AudioBufferList
- __ZN2AQ3API10LegacyImpl25AudioQueueDisposeTimelineEP16OpaqueAudioQueueP24OpaqueAudioQueueTimeline
- __ZN2AQ3API10LegacyImpl25AudioQueueGetPropertySizeEP16OpaqueAudioQueuejPj
- __ZN2AQ3API10LegacyImpl26ATSubmixTapSetTimelineInfoEP17OpaqueATSubmixTapPvj
- __ZN2AQ3API10LegacyImpl26AudioQueueProcessingTapNewEP16OpaqueAudioQueuePFvPvP29OpaqueAudioQueueProcessingTapjP14AudioTimeStampPjS9_P15AudioBufferListES4_jS9_P27AudioStreamBasicDescriptionPS6_
- __ZN2AQ3API10LegacyImpl28ATAudioProcessingNodeDisposeEP27OpaqueATAudioProcessingNode
- __ZN2AQ3API10LegacyImpl28AudioQueueScheduleParametersEP16OpaqueAudioQueuePK14AudioTimeStampjPKjPKf
- __ZN2AQ3API10LegacyImpl29AQOfflineMixerGetPropertySizeEP20OpaqueAQOfflineMixerjPj
- __ZN2AQ3API10LegacyImpl29AudioQueueAddPropertyListenerEP16OpaqueAudioQueuejPFvPvS3_jES4_
- __ZN2AQ3API10LegacyImpl29AudioQueueDeviceTranslateTimeEP16OpaqueAudioQueuePK14AudioTimeStampPS4_
- __ZN2AQ3API10LegacyImpl30AudioQueueDeviceGetCurrentTimeEP16OpaqueAudioQueueP14AudioTimeStamp
- __ZN2AQ3API10LegacyImpl30AudioQueueProcessingTapDisposeEP29OpaqueAudioQueueProcessingTap
- __ZN2AQ3API10LegacyImpl31AQOfflineMixerConnectAudioQueueEP20OpaqueAQOfflineMixerP16OpaqueAudioQueueb
- __ZN2AQ3API10LegacyImpl32ATAudioProcessingNodeGetPropertyEP27OpaqueATAudioProcessingNodeP31ATAudioProcessingNodePropertyIDPvPj
- __ZN2AQ3API10LegacyImpl32ATAudioProcessingNodeInstantiateEP16OpaqueAudioQueuePK25AudioComponentDescriptionjPP27OpaqueATAudioProcessingNode
- __ZN2AQ3API10LegacyImpl32ATAudioProcessingNodeSetPropertyEP27OpaqueATAudioProcessingNodeP31ATAudioProcessingNodePropertyIDPKvj
- __ZN2AQ3API10LegacyImpl32AudioQueueRemovePropertyListenerEP16OpaqueAudioQueuejPFvPvS3_jES4_
- __ZN2AQ3API10LegacyImpl32AudioQueueSetOfflineRenderFormatEP16OpaqueAudioQueuePK27AudioStreamBasicDescriptionPK18AudioChannelLayout
- __ZN2AQ3API10LegacyImpl33ATAudioProcessingNodeGetParameterEP27OpaqueATAudioProcessingNodeP32ATAudioProcessingNodeParameterIDPf
- __ZN2AQ3API10LegacyImpl33ATAudioProcessingNodeSetParameterEP27OpaqueATAudioProcessingNodeP32ATAudioProcessingNodeParameterIDf
- __ZN2AQ3API10LegacyImpl35AudioQueueConvertToScaledSampleTimeEP16OpaqueAudioQueuedPd
- __ZN2AQ3API10LegacyImpl35AudioQueueDeviceGetNearestStartTimeEP16OpaqueAudioQueueP14AudioTimeStampj
- __ZN2AQ3API10LegacyImpl35AudioQueueProcessingTapGetQueueTimeEP29OpaqueAudioQueueProcessingTapPdPj
- __ZN2AQ3API10LegacyImpl35AudioQueueProcessingTapNew_CMClientEP29OpaqueAudioQueueProcessingTapPFvPvS3_jP14AudioTimeStampPjS7_P15AudioBufferListES4_S7_S7_P27AudioStreamBasicDescriptionPS3_
- __ZN2AQ3API10LegacyImpl35AudioQueueProcessingTapNew_CMServerEP16OpaqueAudioQueuejiPjP27AudioStreamBasicDescriptionPP29OpaqueAudioQueueProcessingTap
- __ZN2AQ3API10LegacyImpl36ATAudioProcessingNodeGetPropertyInfoEP27OpaqueATAudioProcessingNodeP31ATAudioProcessingNodePropertyIDPjPh
- __ZN2AQ3API10LegacyImpl37AudioQueueConvertToUnscaledSampleTimeEP16OpaqueAudioQueuedPd
- __ZN2AQ3API10LegacyImpl37AudioQueueEnqueueBufferWithParametersEP16OpaqueAudioQueueP16AudioQueueBufferjPK28AudioStreamPacketDescriptionjjjPK24AudioQueueParameterEventPK14AudioTimeStampPSC_
- __ZN2AQ3API10LegacyImpl37AudioQueueProcessingTapGetSourceAudioEP29OpaqueAudioQueueProcessingTapjP14AudioTimeStampPjS6_P15AudioBufferList
- __ZN2AQ3API10LegacyImpl38ATAudioProcessingNodeScheduleParameterEP27OpaqueATAudioProcessingNodePK14AudioTimeStampPK32ATAudioProcessingNodeParameterIDf
- __ZN2AQ3API10LegacyImpl38AudioQueueProcessingTapGetQueueTime_CMEP29OpaqueAudioQueueProcessingTapPdPjPvS5_
- __ZN2AQ3API10LegacyImpl39ATAudioProcessingNodeScheduleParametersEP27OpaqueATAudioProcessingNodePK14AudioTimeStampjPK32ATAudioProcessingNodeParameterIDPKf
- __ZN2AQ3API10LegacyImpl39AudioQueueProcessingTapGetQueueTime_CM2EP29OpaqueAudioQueueProcessingTapPdPjS4_S5_PvS5_
- __ZN2AQ3API10LegacyImpl46ATAudioProcessingNodeCancelScheduledParametersEP27OpaqueATAudioProcessingNode
- __ZN2AQ3API10LegacyImplD0Ev
- __ZN2AQ3API10LegacyImplD1Ev
- __ZN2AQ3API6V2Impl20AQOfflineMixerRenderEP20OpaqueAQOfflineMixerjPjP15AudioBufferListP28AudioStreamPacketDescriptionP31AudioStreamPacketDependencyInfoPh
- __ZN2AQ3API9Interface13QueueDisposedEj
- __ZN2AQ3API9Interface22SubmixTapFormatChangedEj
- __ZN2AQ3API9Interface28ClientNotificationsAvailableEj
- __ZN2AQ6Server12RemoteClient18ProcessingTapStateD1Ev
- __ZN2AQ6Server4Base8asV2ImplEv
- __ZN2AQ6Server4BaseD0Ev
- __ZN2AQ6Server4BaseD1Ev
- __ZN2CA12AudioBuffers7PrepareEjj
- __ZN2CA12AudioBuffersC1ERK27AudioStreamBasicDescriptionj
- __ZN2CA12AudioBuffersC2EP23ExtendedAudioBufferListj
- __ZN2CA12AudioBuffersD1Ev
- __ZN2OS2CF4DataD0Ev
- __ZN2OS2CF4DataD1Ev
- __ZN34MCProcessingNodeInputChunkerInsert14RenderCallbackEPvPjPK14AudioTimeStampjjP15AudioBufferList
- __ZN34MCProcessingNodeInputChunkerInsert20AllocateInputBuffersEj
- __ZN34MCProcessingNodeInputChunkerInsert9SetFormatEbRK27AudioStreamBasicDescription
- __ZN34MCProcessingNodeInputChunkerInsertD0Ev
- __ZN34MCProcessingNodeInputChunkerInsertD1Ev
- __ZN35ATAudioProcessingNodeConnectionInfoC2EN10applesauce3xpc8endpointENS0_2CF9StringRefE
- __ZN4brls10AOPRunningD0Ev
- __ZN4brls10AOPRunningD1Ev
- __ZN4brls10AOPRunningD2Ev
- __ZN4brls11PSAnalyzingD0Ev
- __ZN4brls11PSAnalyzingD1Ev
- __ZN4brls11PSAnalyzingD2Ev
- __ZN4brls11PSRecordingD0Ev
- __ZN4brls11PSRecordingD1Ev
- __ZN4brls11PSRecordingD2Ev
- __ZN4brls12EvtPSTriggerD0Ev
- __ZN4brls12EvtPSTriggerD1Ev
- __ZN4brls13EvtAOPTriggerD0Ev
- __ZN4brls13EvtAOPTriggerD1Ev
- __ZN4brls13PSAwaitRecordD0Ev
- __ZN4brls13PSAwaitRecordD1Ev
- __ZN4brls13PSAwaitRecordD2Ev
- __ZN4brls14EvtVTSMEnabledD0Ev
- __ZN4brls14EvtVTSMEnabledD1Ev
- __ZN4brls14PSPreRecordingD0Ev
- __ZN4brls14PSPreRecordingD1Ev
- __ZN4brls14PSPreRecordingD2Ev
- __ZN4brls15EvtVTSMDisabledD0Ev
- __ZN4brls15EvtVTSMDisabledD1Ev
- __ZN4brls16EvtInternalResetD0Ev
- __ZN4brls16EvtInternalResetD1Ev
- __ZN4brls16EvtStopRecordingD0Ev
- __ZN4brls16EvtStopRecordingD1Ev
- __ZN4brls17EvtPSCheckStartIOD0Ev
- __ZN4brls17EvtPSCheckStartIOD1Ev
- __ZN4brls17EvtStartRecordingD0Ev
- __ZN4brls17EvtStartRecordingD1Ev
- __ZN4brls18RecordingWithoutPSD0Ev
- __ZN4brls18RecordingWithoutPSD1Ev
- __ZN4brls18RecordingWithoutPSD2Ev
- __ZN4brls19EvtPSStopSecondPassD0Ev
- __ZN4brls19EvtPSStopSecondPassD1Ev
- __ZN4brls20EvtPreStartRecordingD0Ev
- __ZN4brls20EvtPreStartRecordingD1Ev
- __ZN4brls20PhraseSpotterRunning15workThreadEntryEPv
- __ZN4brls20PhraseSpotterRunning20fillComplexInputProcEP20OpaqueAudioConverterPjP15AudioBufferListPP28AudioStreamPacketDescriptionPv
- __ZN4brls20PhraseSpotterRunning7startIOEbb
- __ZN4brls20PhraseSpotterRunningD0Ev
- __ZN4brls20PhraseSpotterRunningD1Ev
- __ZN4brls20PhraseSpotterRunningD2Ev
- __ZN4brls21EvtStartRecordTimeoutD0Ev
- __ZN4brls21EvtStartRecordTimeoutD1Ev
- __ZN4brls3FSMD0Ev
- __ZN4brls3FSMD1Ev
- __ZN4brls5ResetD0Ev
- __ZN4brls5ResetD1Ev
- __ZN4brls5ResetD2Ev
- __ZN4brls7PSResetD0Ev
- __ZN4brls7PSResetD1Ev
- __ZN4brls7PSResetD2Ev
- __ZN4brls9QuiescentD0Ev
- __ZN4brls9QuiescentD1Ev
- __ZN4brls9QuiescentD2Ev
- __ZN4swix4dataC2EON10applesauce3xpc6objectE
- __ZN4swix5coderIiE6decodeERKNS_14decode_messageEPKc
- __ZN4swix5coderIjE6decodeERKNS_14decode_messageEPKc
- __ZN5boost10statechart12simple_stateIN4brls10AOPRunningENS2_3FSMENS_3mpl4listIN4mpl_2naES8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_EELNS0_12history_modeE0EE10react_implERKNS0_10event_baseEPKv
- __ZN5boost10statechart12simple_stateIN4brls10AOPRunningENS2_3FSMENS_3mpl4listIN4mpl_2naES8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_EELNS0_12history_modeE0EE9exit_implERNS_13intrusive_ptrINS0_6detail10leaf_stateINSt3__19allocatorINS0_4noneEEENSD_11rtti_policyEEEEERNSC_INSD_15node_state_baseISI_SJ_EEEEb
- __ZN5boost10statechart12simple_stateIN4brls10AOPRunningENS2_3FSMENS_3mpl4listIN4mpl_2naES8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_EELNS0_12history_modeE0EED0Ev
- __ZN5boost10statechart12simple_stateIN4brls10AOPRunningENS2_3FSMENS_3mpl4listIN4mpl_2naES8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_EELNS0_12history_modeE0EED1Ev
- __ZN5boost10statechart12simple_stateIN4brls10AOPRunningENS2_3FSMENS_3mpl4listIN4mpl_2naES8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_EELNS0_12history_modeE0EED2Ev
- __ZN5boost10statechart12simple_stateIN4brls11PSAnalyzingENS2_20PhraseSpotterRunningENS_3mpl4listIN4mpl_2naES8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_EELNS0_12history_modeE0EE10react_implERKNS0_10event_baseEPKv
- __ZN5boost10statechart12simple_stateIN4brls11PSAnalyzingENS2_20PhraseSpotterRunningENS_3mpl4listIN4mpl_2naES8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_EELNS0_12history_modeE0EE12transit_implINS2_7PSResetENS2_3FSMENS0_6detail22no_transition_functionEEENSF_15reaction_resultERKT1_
- __ZN5boost10statechart12simple_stateIN4brls11PSAnalyzingENS2_20PhraseSpotterRunningENS_3mpl4listIN4mpl_2naES8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_EELNS0_12history_modeE0EE9exit_implERNS_13intrusive_ptrINS0_6detail10leaf_stateINSt3__19allocatorINS0_4noneEEENSD_11rtti_policyEEEEERNSC_INSD_15node_state_baseISI_SJ_EEEEb
- __ZN5boost10statechart12simple_stateIN4brls11PSAnalyzingENS2_20PhraseSpotterRunningENS_3mpl4listIN4mpl_2naES8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_EELNS0_12history_modeE0EED0Ev
- __ZN5boost10statechart12simple_stateIN4brls11PSAnalyzingENS2_20PhraseSpotterRunningENS_3mpl4listIN4mpl_2naES8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_EELNS0_12history_modeE0EED1Ev
- __ZN5boost10statechart12simple_stateIN4brls11PSAnalyzingENS2_20PhraseSpotterRunningENS_3mpl4listIN4mpl_2naES8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_EELNS0_12history_modeE0EED2Ev
- __ZN5boost10statechart12simple_stateIN4brls11PSRecordingENS2_20PhraseSpotterRunningENS_3mpl4listIN4mpl_2naES8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_EELNS0_12history_modeE0EE10react_implERKNS0_10event_baseEPKv
- __ZN5boost10statechart12simple_stateIN4brls11PSRecordingENS2_20PhraseSpotterRunningENS_3mpl4listIN4mpl_2naES8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_EELNS0_12history_modeE0EE9exit_implERNS_13intrusive_ptrINS0_6detail10leaf_stateINSt3__19allocatorINS0_4noneEEENSD_11rtti_policyEEEEERNSC_INSD_15node_state_baseISI_SJ_EEEEb
- __ZN5boost10statechart12simple_stateIN4brls11PSRecordingENS2_20PhraseSpotterRunningENS_3mpl4listIN4mpl_2naES8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_EELNS0_12history_modeE0EED0Ev
- __ZN5boost10statechart12simple_stateIN4brls11PSRecordingENS2_20PhraseSpotterRunningENS_3mpl4listIN4mpl_2naES8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_EELNS0_12history_modeE0EED1Ev
- __ZN5boost10statechart12simple_stateIN4brls11PSRecordingENS2_20PhraseSpotterRunningENS_3mpl4listIN4mpl_2naES8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_EELNS0_12history_modeE0EED2Ev
- __ZN5boost10statechart12simple_stateIN4brls13PSAwaitRecordENS2_20PhraseSpotterRunningENS_3mpl4listIN4mpl_2naES8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_EELNS0_12history_modeE0EE10react_implERKNS0_10event_baseEPKv
- __ZN5boost10statechart12simple_stateIN4brls13PSAwaitRecordENS2_20PhraseSpotterRunningENS_3mpl4listIN4mpl_2naES8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_EELNS0_12history_modeE0EE9exit_implERNS_13intrusive_ptrINS0_6detail10leaf_stateINSt3__19allocatorINS0_4noneEEENSD_11rtti_policyEEEEERNSC_INSD_15node_state_baseISI_SJ_EEEEb
- __ZN5boost10statechart12simple_stateIN4brls13PSAwaitRecordENS2_20PhraseSpotterRunningENS_3mpl4listIN4mpl_2naES8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_EELNS0_12history_modeE0EED0Ev
- __ZN5boost10statechart12simple_stateIN4brls13PSAwaitRecordENS2_20PhraseSpotterRunningENS_3mpl4listIN4mpl_2naES8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_EELNS0_12history_modeE0EED1Ev
- __ZN5boost10statechart12simple_stateIN4brls13PSAwaitRecordENS2_20PhraseSpotterRunningENS_3mpl4listIN4mpl_2naES8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_EELNS0_12history_modeE0EED2Ev
- __ZN5boost10statechart12simple_stateIN4brls14PSPreRecordingENS2_20PhraseSpotterRunningENS_3mpl4listIN4mpl_2naES8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_EELNS0_12history_modeE0EE10react_implERKNS0_10event_baseEPKv
- __ZN5boost10statechart12simple_stateIN4brls14PSPreRecordingENS2_20PhraseSpotterRunningENS_3mpl4listIN4mpl_2naES8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_EELNS0_12history_modeE0EE9exit_implERNS_13intrusive_ptrINS0_6detail10leaf_stateINSt3__19allocatorINS0_4noneEEENSD_11rtti_policyEEEEERNSC_INSD_15node_state_baseISI_SJ_EEEEb
- __ZN5boost10statechart12simple_stateIN4brls14PSPreRecordingENS2_20PhraseSpotterRunningENS_3mpl4listIN4mpl_2naES8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_EELNS0_12history_modeE0EED0Ev
- __ZN5boost10statechart12simple_stateIN4brls14PSPreRecordingENS2_20PhraseSpotterRunningENS_3mpl4listIN4mpl_2naES8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_EELNS0_12history_modeE0EED1Ev
- __ZN5boost10statechart12simple_stateIN4brls14PSPreRecordingENS2_20PhraseSpotterRunningENS_3mpl4listIN4mpl_2naES8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_EELNS0_12history_modeE0EED2Ev
- __ZN5boost10statechart12simple_stateIN4brls18RecordingWithoutPSENS2_3FSMENS_3mpl4listIN4mpl_2naES8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_EELNS0_12history_modeE0EE10react_implERKNS0_10event_baseEPKv
- __ZN5boost10statechart12simple_stateIN4brls18RecordingWithoutPSENS2_3FSMENS_3mpl4listIN4mpl_2naES8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_EELNS0_12history_modeE0EE9exit_implERNS_13intrusive_ptrINS0_6detail10leaf_stateINSt3__19allocatorINS0_4noneEEENSD_11rtti_policyEEEEERNSC_INSD_15node_state_baseISI_SJ_EEEEb
- __ZN5boost10statechart12simple_stateIN4brls18RecordingWithoutPSENS2_3FSMENS_3mpl4listIN4mpl_2naES8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_EELNS0_12history_modeE0EED0Ev
- __ZN5boost10statechart12simple_stateIN4brls18RecordingWithoutPSENS2_3FSMENS_3mpl4listIN4mpl_2naES8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_EELNS0_12history_modeE0EED1Ev
- __ZN5boost10statechart12simple_stateIN4brls18RecordingWithoutPSENS2_3FSMENS_3mpl4listIN4mpl_2naES8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_EELNS0_12history_modeE0EED2Ev
- __ZN5boost10statechart12simple_stateIN4brls20PhraseSpotterRunningENS2_3FSMENS2_11PSAnalyzingELNS0_12history_modeE0EE10react_implERKNS0_10event_baseEPKv
- __ZN5boost10statechart12simple_stateIN4brls20PhraseSpotterRunningENS2_3FSMENS2_11PSAnalyzingELNS0_12history_modeE0EE9exit_implERNS_13intrusive_ptrINS0_6detail15node_state_baseINSt3__19allocatorINS0_4noneEEENS9_11rtti_policyEEEEESI_b
- __ZN5boost10statechart12simple_stateIN4brls20PhraseSpotterRunningENS2_3FSMENS2_11PSAnalyzingELNS0_12history_modeE0EE9exit_implERNS_13intrusive_ptrIS3_EERNS8_INS0_6detail15node_state_baseINSt3__19allocatorINS0_4noneEEENSB_11rtti_policyEEEEEb
- __ZN5boost10statechart12simple_stateIN4brls20PhraseSpotterRunningENS2_3FSMENS2_11PSAnalyzingELNS0_12history_modeE0EED0Ev
- __ZN5boost10statechart12simple_stateIN4brls20PhraseSpotterRunningENS2_3FSMENS2_11PSAnalyzingELNS0_12history_modeE0EED1Ev
- __ZN5boost10statechart12simple_stateIN4brls20PhraseSpotterRunningENS2_3FSMENS2_11PSAnalyzingELNS0_12history_modeE0EED2Ev
- __ZN5boost10statechart12simple_stateIN4brls5ResetENS2_3FSMENS_3mpl4listIN4mpl_2naES8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_EELNS0_12history_modeE0EE10react_implERKNS0_10event_baseEPKv
- __ZN5boost10statechart12simple_stateIN4brls5ResetENS2_3FSMENS_3mpl4listIN4mpl_2naES8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_EELNS0_12history_modeE0EE9exit_implERNS_13intrusive_ptrINS0_6detail10leaf_stateINSt3__19allocatorINS0_4noneEEENSD_11rtti_policyEEEEERNSC_INSD_15node_state_baseISI_SJ_EEEEb
- __ZN5boost10statechart12simple_stateIN4brls5ResetENS2_3FSMENS_3mpl4listIN4mpl_2naES8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_EELNS0_12history_modeE0EED0Ev
- __ZN5boost10statechart12simple_stateIN4brls5ResetENS2_3FSMENS_3mpl4listIN4mpl_2naES8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_EELNS0_12history_modeE0EED1Ev
- __ZN5boost10statechart12simple_stateIN4brls5ResetENS2_3FSMENS_3mpl4listIN4mpl_2naES8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_EELNS0_12history_modeE0EED2Ev
- __ZN5boost10statechart12simple_stateIN4brls7PSResetENS2_20PhraseSpotterRunningENS_3mpl4listIN4mpl_2naES8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_EELNS0_12history_modeE0EE10react_implERKNS0_10event_baseEPKv
- __ZN5boost10statechart12simple_stateIN4brls7PSResetENS2_20PhraseSpotterRunningENS_3mpl4listIN4mpl_2naES8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_EELNS0_12history_modeE0EE9exit_implERNS_13intrusive_ptrINS0_6detail10leaf_stateINSt3__19allocatorINS0_4noneEEENSD_11rtti_policyEEEEERNSC_INSD_15node_state_baseISI_SJ_EEEEb
- __ZN5boost10statechart12simple_stateIN4brls7PSResetENS2_20PhraseSpotterRunningENS_3mpl4listIN4mpl_2naES8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_EELNS0_12history_modeE0EED0Ev
- __ZN5boost10statechart12simple_stateIN4brls7PSResetENS2_20PhraseSpotterRunningENS_3mpl4listIN4mpl_2naES8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_EELNS0_12history_modeE0EED1Ev
- __ZN5boost10statechart12simple_stateIN4brls7PSResetENS2_20PhraseSpotterRunningENS_3mpl4listIN4mpl_2naES8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_EELNS0_12history_modeE0EED2Ev
- __ZN5boost10statechart12simple_stateIN4brls9QuiescentENS2_3FSMENS_3mpl4listIN4mpl_2naES8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_EELNS0_12history_modeE0EE10react_implERKNS0_10event_baseEPKv
- __ZN5boost10statechart12simple_stateIN4brls9QuiescentENS2_3FSMENS_3mpl4listIN4mpl_2naES8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_EELNS0_12history_modeE0EE9exit_implERNS_13intrusive_ptrINS0_6detail10leaf_stateINSt3__19allocatorINS0_4noneEEENSD_11rtti_policyEEEEERNSC_INSD_15node_state_baseISI_SJ_EEEEb
- __ZN5boost10statechart12simple_stateIN4brls9QuiescentENS2_3FSMENS_3mpl4listIN4mpl_2naES8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_EELNS0_12history_modeE0EED0Ev
- __ZN5boost10statechart12simple_stateIN4brls9QuiescentENS2_3FSMENS_3mpl4listIN4mpl_2naES8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_EELNS0_12history_modeE0EED1Ev
- __ZN5boost10statechart12simple_stateIN4brls9QuiescentENS2_3FSMENS_3mpl4listIN4mpl_2naES8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_EELNS0_12history_modeE0EED2Ev
- __ZN5boost10statechart13state_machineIN4brls3FSMENS2_5ResetENSt3__19allocatorINS0_4noneEEENS0_25null_exception_translatorEE10send_eventERKNS0_10event_baseE
- __ZN5boost10statechart13state_machineIN4brls3FSMENS2_5ResetENSt3__19allocatorINS0_4noneEEENS0_25null_exception_translatorEE10terminatorD2Ev
- __ZN5boost10statechart13state_machineIN4brls3FSMENS2_5ResetENSt3__19allocatorINS0_4noneEEENS0_25null_exception_translatorEE13process_eventERKNS0_10event_baseE
- __ZN5boost10statechart13state_machineIN4brls3FSMENS2_5ResetENSt3__19allocatorINS0_4noneEEENS0_25null_exception_translatorEE14release_eventsEv
- __ZN5boost10statechart13state_machineIN4brls3FSMENS2_5ResetENSt3__19allocatorINS0_4noneEEENS0_25null_exception_translatorEE14terminate_implERNS0_6detail10state_baseIS8_NSB_11rtti_policyEEEb
- __ZN5boost10statechart13state_machineIN4brls3FSMENS2_5ResetENSt3__19allocatorINS0_4noneEEENS0_25null_exception_translatorEE14terminate_implEb
- __ZN5boost10statechart13state_machineIN4brls3FSMENS2_5ResetENSt3__19allocatorINS0_4noneEEENS0_25null_exception_translatorEE15post_event_implERKNS0_10event_baseE
- __ZN5boost10statechart13state_machineIN4brls3FSMENS2_5ResetENSt3__19allocatorINS0_4noneEEENS0_25null_exception_translatorEE21process_queued_eventsEv
- __ZN5boost10statechart13state_machineIN4brls3FSMENS2_5ResetENSt3__19allocatorINS0_4noneEEENS0_25null_exception_translatorEE8add_implERKNS_13intrusive_ptrINS0_6detail10leaf_stateIS8_NSC_11rtti_policyEEEEERSF_
- __ZN5boost10statechart13state_machineIN4brls3FSMENS2_5ResetENSt3__19allocatorINS0_4noneEEENS0_25null_exception_translatorEE9terminateEv
- __ZN5boost10statechart13state_machineIN4brls3FSMENS2_5ResetENSt3__19allocatorINS0_4noneEEENS0_25null_exception_translatorEED0Ev
- __ZN5boost10statechart13state_machineIN4brls3FSMENS2_5ResetENSt3__19allocatorINS0_4noneEEENS0_25null_exception_translatorEED1Ev
- __ZN5boost10statechart13state_machineIN4brls3FSMENS2_5ResetENSt3__19allocatorINS0_4noneEEENS0_25null_exception_translatorEED2Ev
- __ZN5boost10statechart5stateIN4brls10AOPRunningENS2_3FSMENS_3mpl4listIN4mpl_2naES8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_EELNS0_12history_modeE0EE14deep_constructERKPNS0_13state_machineIS4_NS2_5ResetENSt3__19allocatorINS0_4noneEEENS0_25null_exception_translatorEEERSJ_
- __ZN5boost10statechart5stateIN4brls11PSAnalyzingENS2_20PhraseSpotterRunningENS_3mpl4listIN4mpl_2naES8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_EELNS0_12history_modeE0EE14deep_constructERKNS_13intrusive_ptrIS4_EERNS0_13state_machineINS2_3FSMENS2_5ResetENSt3__19allocatorINS0_4noneEEENS0_25null_exception_translatorEEE
- __ZN5boost10statechart5stateIN4brls11PSAnalyzingENS2_20PhraseSpotterRunningENS_3mpl4listIN4mpl_2naES8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_EELNS0_12history_modeE0EED0Ev
- __ZN5boost10statechart5stateIN4brls11PSAnalyzingENS2_20PhraseSpotterRunningENS_3mpl4listIN4mpl_2naES8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_EELNS0_12history_modeE0EED1Ev
- __ZN5boost10statechart5stateIN4brls11PSRecordingENS2_20PhraseSpotterRunningENS_3mpl4listIN4mpl_2naES8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_EELNS0_12history_modeE0EE14deep_constructERKNS_13intrusive_ptrIS4_EERNS0_13state_machineINS2_3FSMENS2_5ResetENSt3__19allocatorINS0_4noneEEENS0_25null_exception_translatorEEE
- __ZN5boost10statechart5stateIN4brls11PSRecordingENS2_20PhraseSpotterRunningENS_3mpl4listIN4mpl_2naES8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_EELNS0_12history_modeE0EED0Ev
- __ZN5boost10statechart5stateIN4brls11PSRecordingENS2_20PhraseSpotterRunningENS_3mpl4listIN4mpl_2naES8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_EELNS0_12history_modeE0EED1Ev
- __ZN5boost10statechart5stateIN4brls13PSAwaitRecordENS2_20PhraseSpotterRunningENS_3mpl4listIN4mpl_2naES8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_EELNS0_12history_modeE0EED0Ev
- __ZN5boost10statechart5stateIN4brls13PSAwaitRecordENS2_20PhraseSpotterRunningENS_3mpl4listIN4mpl_2naES8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_EELNS0_12history_modeE0EED1Ev
- __ZN5boost10statechart5stateIN4brls14PSPreRecordingENS2_20PhraseSpotterRunningENS_3mpl4listIN4mpl_2naES8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_EELNS0_12history_modeE0EE14deep_constructERKNS_13intrusive_ptrIS4_EERNS0_13state_machineINS2_3FSMENS2_5ResetENSt3__19allocatorINS0_4noneEEENS0_25null_exception_translatorEEE
- __ZN5boost10statechart5stateIN4brls14PSPreRecordingENS2_20PhraseSpotterRunningENS_3mpl4listIN4mpl_2naES8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_EELNS0_12history_modeE0EED0Ev
- __ZN5boost10statechart5stateIN4brls14PSPreRecordingENS2_20PhraseSpotterRunningENS_3mpl4listIN4mpl_2naES8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_EELNS0_12history_modeE0EED1Ev
- __ZN5boost10statechart5stateIN4brls20PhraseSpotterRunningENS2_3FSMENS2_11PSAnalyzingELNS0_12history_modeE0EE14deep_constructERKPNS0_13state_machineIS4_NS2_5ResetENSt3__19allocatorINS0_4noneEEENS0_25null_exception_translatorEEERSF_
- __ZN5boost10statechart5stateIN4brls5ResetENS2_3FSMENS_3mpl4listIN4mpl_2naES8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_EELNS0_12history_modeE0EE14deep_constructERKPNS0_13state_machineIS4_S3_NSt3__19allocatorINS0_4noneEEENS0_25null_exception_translatorEEERSI_
- __ZN5boost10statechart5stateIN4brls7PSResetENS2_20PhraseSpotterRunningENS_3mpl4listIN4mpl_2naES8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_EELNS0_12history_modeE0EE14deep_constructERKNS_13intrusive_ptrIS4_EERNS0_13state_machineINS2_3FSMENS2_5ResetENSt3__19allocatorINS0_4noneEEENS0_25null_exception_translatorEEE
- __ZN5boost10statechart5stateIN4brls7PSResetENS2_20PhraseSpotterRunningENS_3mpl4listIN4mpl_2naES8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_EELNS0_12history_modeE0EED0Ev
- __ZN5boost10statechart5stateIN4brls7PSResetENS2_20PhraseSpotterRunningENS_3mpl4listIN4mpl_2naES8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_EELNS0_12history_modeE0EED1Ev
- __ZN5boost10statechart5stateIN4brls9QuiescentENS2_3FSMENS_3mpl4listIN4mpl_2naES8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_EELNS0_12history_modeE0EE14deep_constructERKPNS0_13state_machineIS4_NS2_5ResetENSt3__19allocatorINS0_4noneEEENS0_25null_exception_translatorEEERSJ_
- __ZN5boost10statechart6detail10leaf_stateINSt3__19allocatorINS0_4noneEEENS1_11rtti_policyEE22remove_from_state_listERNS3_15__list_iteratorINS_13intrusive_ptrIS8_EEPvEERNSA_INS1_15node_state_baseIS6_S7_EEEEb
- __ZN5boost10statechart6detail10node_stateIN4mpl_5long_ILl1EEENSt3__19allocatorINS0_4noneEEENS1_11rtti_policyEE22remove_from_state_listERNS6_15__list_iteratorINS_13intrusive_ptrINS1_10leaf_stateIS9_SA_EEEEPvEERNSD_INS1_15node_state_baseIS9_SA_EEEEb
- __ZN5boost10statechart6detail9id_holderIN4brls10AOPRunningEE11idProvider_E
- __ZN5boost10statechart6detail9id_holderIN4brls11PSAnalyzingEE11idProvider_E
- __ZN5boost10statechart6detail9id_holderIN4brls11PSRecordingEE11idProvider_E
- __ZN5boost10statechart6detail9id_holderIN4brls12EvtPSTriggerEE11idProvider_E
- __ZN5boost10statechart6detail9id_holderIN4brls13EvtAOPTriggerEE11idProvider_E
- __ZN5boost10statechart6detail9id_holderIN4brls13PSAwaitRecordEE11idProvider_E
- __ZN5boost10statechart6detail9id_holderIN4brls14EvtVTSMEnabledEE11idProvider_E
- __ZN5boost10statechart6detail9id_holderIN4brls14PSPreRecordingEE11idProvider_E
- __ZN5boost10statechart6detail9id_holderIN4brls15EvtVTSMDisabledEE11idProvider_E
- __ZN5boost10statechart6detail9id_holderIN4brls16EvtInternalResetEE11idProvider_E
- __ZN5boost10statechart6detail9id_holderIN4brls16EvtStopRecordingEE11idProvider_E
- __ZN5boost10statechart6detail9id_holderIN4brls17EvtPSCheckStartIOEE11idProvider_E
- __ZN5boost10statechart6detail9id_holderIN4brls17EvtStartRecordingEE11idProvider_E
- __ZN5boost10statechart6detail9id_holderIN4brls18RecordingWithoutPSEE11idProvider_E
- __ZN5boost10statechart6detail9id_holderIN4brls19EvtPSStopSecondPassEE11idProvider_E
- __ZN5boost10statechart6detail9id_holderIN4brls20EvtPreStartRecordingEE11idProvider_E
- __ZN5boost10statechart6detail9id_holderIN4brls20PhraseSpotterRunningEE11idProvider_E
- __ZN5boost10statechart6detail9id_holderIN4brls21EvtStartRecordTimeoutEE11idProvider_E
- __ZN5boost10statechart6detail9id_holderIN4brls5ResetEE11idProvider_E
- __ZN5boost10statechart6detail9id_holderIN4brls7PSResetEE11idProvider_E
- __ZN5boost10statechart6detail9id_holderIN4brls9QuiescentEE11idProvider_E
- __ZN5boost13intrusive_ptrIN4brls20PhraseSpotterRunningEEaSERKS3_
- __ZN5boost3msm4back13state_machineIN11SequenceFSM10StateFront11ActiveFrontENS_9parameter5void_ES7_S7_S7_E25deferred_msg_queue_helperIS8_iE5clearEv
- __ZN5boost3msm4back13state_machineIN11SequenceFSM10StateFrontENS_9parameter5void_ES6_S6_S6_ED1Ev
- __ZN5boost6fusion3setIJNS_3msm5front4euml10func_stateIN11SequenceFSM10StateFront12PausingNamerENS7_12PausingEntryENS7_11PausingExitENS0_6vectorIJEEENS_3mpl6vectorINS6_9IsRunningENS6_9IsPausingEN4mpl_2naESI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_EENSE_INS6_6ResumeENS6_4PlayENS6_4SeekENS6_4StopENS6_13EnableLoopingESI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_EENS6_9NamedBaseIS8_EEEENS5_INS7_13FinishedNamerENS7_12DefaultEntryENS7_11DefaultExitESC_NSE_INS6_10IsFinishedESI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_EENSD_7vector0ISI_EENSQ_IST_EEEENS2_4back13state_machineINS7_11ActiveFrontENS_9parameter5void_ES16_S16_S16_EENS5_INS7_13StartingNamerENS7_13StartingEntryENS7_12StartingExitESC_NSE_INS6_10IsStartingESI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_SI_EESZ_NSQ_IS18_EEEENS5_INS7_20StartingForPlayNamerENS7_20StartingForPlayEntryENS7_19StartingForPlayExitESC_S1C_SZ_NSQ_IS1F_EEEENS5_INS7_13PreparedNamerESU_SV_SC_SX_SZ_NSQ_IS1K_EEEENS5_INS7_11LoadedNamerESU_SV_SC_SZ_SZ_NSQ_IS1N_EEEENS5_INS7_18UninitializedNamerESU_SV_SC_SZ_SZ_NSQ_IS1Q_EEEEEED1Ev
- __ZN5boost9container3dtl9flat_treeINS1_4pairIjNSt3__110unique_ptrI8AQBufferNS4_14default_deleteIS6_EEEEEENS1_9select1stIjEENS4_4lessIjEENS0_13new_allocatorISA_EEE19emplace_hint_uniqueIJSA_EEENS0_12vec_iteratorIPSA_Lb0EEENSJ_ISK_Lb1EEEDpOT_
- __ZN5boost9container6vectorINS0_3dtl4pairIjNSt3__110unique_ptrI8AQBufferNS4_14default_deleteIS6_EEEEEENS0_13new_allocatorISA_EEvE5eraseENS0_12vec_iteratorIPSA_Lb1EEE
- __ZN5boost9typeindex6detailL23ctti_skip_until_runtimeE.8571
- __ZN5caulk10concurrent26lf_read_synchronized_writeINSt3__110unique_ptrI14MixTapToUplinkNS2_14default_deleteIS4_EEEEEaSES7_
- __ZN5caulk10concurrent7details12message_callIRZN11ClientEntry19handleSequenceEndedEmNSt3__18functionIFvmEEEE3$_0JEE7performEv
- __ZN5caulk10concurrent7details12message_callIRZN11ClientEntry19handleSequenceEndedEmNSt3__18functionIFvmEEEE3$_0JEED0Ev
- __ZN5caulk10concurrent7details12message_callIRZN11ClientEntry19handleSequenceEndedEmNSt3__18functionIFvmEEEE3$_0JEED1Ev
- __ZN5caulk10concurrent7details15rt_message_callIRZN11ClientEntry19handleSequenceEndedEmNSt3__18functionIFvmEEEE3$_0JEE10rt_cleanupD1Ev
- __ZN5caulk10concurrent7details15rt_message_callIRZN11ClientEntry19handleSequenceEndedEmNSt3__18functionIFvmEEEE3$_0JEE7performEv
- __ZN5caulk10concurrent7details15rt_message_callIRZN11ClientEntry19handleSequenceEndedEmNSt3__18functionIFvmEEEE3$_0JEED0Ev
- __ZN5caulk10concurrent7details15rt_message_callIRZN11ClientEntry19handleSequenceEndedEmNSt3__18functionIFvmEEEE3$_0JEED1Ev
- __ZN5caulk10concurrent9messenger12enqueue_callIRZN10XAudioUnit6RenderEPjPK14AudioTimeStampjjP15AudioBufferListEUlvE_JEEEvOT_DpOT0_
- __ZN5caulk12function_refIFvR9TapSubmixEE15functor_invokerIZN13MESubmixGraph19attach1MixerChannelEP14MEMixerChannelE3$_0EEvRKNS_7details15erased_callableIS3_EES2_
- __ZN5caulk12function_refIFvR9TapSubmixibEE15functor_invokerIZN12_GLOBAL__N_131GetNumberOfTapSubmixConnectionsER14MEMixerChannelRK17AudioTapSpecifierE3$_0EEvRKNS_7details15erased_callableIS3_EES2_ib
- __ZN5caulk12function_refIFvR9TapSubmixibEE15functor_invokerIZN14MEMixerChannel15ResetMixerInputEjE3$_0EEvRKNS_7details15erased_callableIS3_EES2_ib
- __ZN5caulk12function_refIFvR9TapSubmixibEE15functor_invokerIZN14MEMixerChannel16SetMixerInputPanEjfE3$_0EEvRKNS_7details15erased_callableIS3_EES2_ib
- __ZN5caulk12function_refIFvR9TapSubmixibEE15functor_invokerIZN14MEMixerChannel23ScheduleMixerParametersEjRNSt3__16vectorI23AudioUnitParameterEventNS7_9allocatorIS9_EEEEE3$_0EEvRKNS_7details15erased_callableIS3_EES2_ib
- __ZN5caulk12function_refIFvR9TapSubmixibEE15functor_invokerIZN14MEMixerChannel24SetMixerInputBalanceModeEj20AudioBalanceFadeTypeE3$_0EEvRKNS_7details15erased_callableIS3_EES2_ib
- __ZN5caulk12synchronizedIN10applesauce2CF7DataRefENS_4mach11unfair_lockENS_22empty_atomic_interfaceIS3_EEED1Ev
- __ZN5caulk12synchronizedIN2AQ3API7Manager12GuardedStateENS_4mach11unfair_lockENS_22empty_atomic_interfaceIS4_EEED1Ev
- __ZN5caulk12thread_proxyINSt3__15tupleIJNS_6thread10attributesEZN26ClientProcessingTapManager6AddTapEjjRK27AudioStreamBasicDescriptionEUlvE_NS2_IJEEEEEEEEPvSC_
- __ZN5caulk17__expected_detail4baseINSt3__15tupleIJN4swix4dataEEEEiEC2EOS7_
- __ZN5caulk17__expected_detail7destroyI11AQMESessionLPv0EEEvRT_
- __ZN5caulk17__expected_detail7destroyI35ATAudioProcessingNodeConnectionInfoLPv0EEEvRT_
- __ZN5caulk23inplace_function_detail6vtableIvJRKNS_10concurrent7details13skiplist_nodeIPvNS_5alloc6detail13tracked_blockEE9layout_vkEEE5emptyE
- __ZN5caulk5alloc22realtime_safe_resourceE
- __ZN5caulk7numeric15exceptional_addIjEET_S2_S2_
- __ZN6WaiterD0Ev
- __ZN6WaiterD1Ev
- __ZN8AQBufferD2Ev
- __ZN8AQIONode15BorealisToggledEv
- __ZN8AQIONode17AddProcessingNodeER14AQIONodeClientRK16AQProcessingNode
- __ZN8AQServer10ClientDiedEPN12CADeprecated11XMachServer6ClientE
- __ZN8AQServer12asLegacyImplEv
- __ZN8AQServer13QueueDisposedEP14AQRemoteClientP15AudioQueueOwner
- __ZN8AQServer17forEachQueueTokenEbRKN5caulk12function_refIFvjEEE
- __ZN8AQServer24QueueOfflineStateChangedERN2AQ6Server16RemoteClientBaseEP15AudioQueueOwnerb
- __ZN8AQServer24SetAQServerDispatchQueueERKN10applesauce8dispatch2v15queueE
- __ZN8AQServerC1ERN2AT9MixServer4BaseE
- __ZN8AQServerD0Ev
- __ZN8AQServerD1Ev
- __ZN8AQServerD2Ev
- __ZN8RTLockedINSt3__13mapEKjJjEED2Ev
- __ZN8RTLockedINSt3__13mapEmJNS0_10shared_ptrI11ClientEntryEEEED2Ev
- __ZN8RTLockedINSt3__13mapEmJjEED2Ev
- __ZN8audioipc13ipc_node_baseILNS_15ipcnode_optionsE0ENS_19eventlink_primitiveEN5caulk3ipc13mapped_memoryEE11signal_waitEv
- __ZN8audioipc13ipc_node_baseILNS_15ipcnode_optionsE0ENS_19eventlink_primitiveEN5caulk3ipc13mapped_memoryEE8can_sendEv
- __ZN9TapSourceD1Ev
- __ZNK10applesauce2CF7DataRefptEv
- __ZNK11DSP_Routing22IsMuteControlledByAVSCEv
- __ZNK12CAXException11FormatErrorEPcm
- __ZNK13MESubmixGraph10activePortEv
- __ZNK13TOpaqueObjectI14AQRemoteClientjN12CADeprecated11XMachServer6ClientEE3isaERKN16BaseOpaqueObject4RTTIE
- __ZNK13TOpaqueObjectI16ClientAudioQueueP16OpaqueAudioQueue16BaseOpaqueObjectE3isaERKNS3_4RTTIE
- __ZNK13TOpaqueObjectI19ClientProcessingTapP29OpaqueAudioQueueProcessingTap16BaseOpaqueObjectE3isaERKNS3_4RTTIE
- __ZNK13TOpaqueObjectI20ClientAQOfflineMixerP20OpaqueAQOfflineMixer16BaseOpaqueObjectE3isaERKNS3_4RTTIE
- __ZNK13TOpaqueObjectI20DSP_Routing_Borealisj16BaseOpaqueObjectE3isaERKNS1_4RTTIE
- __ZNK14AQIONodeClient25EnhanceDialogueIsSelectedEP8AQIONode
- __ZNK14CACFDictionary9GetUInt64EPK10__CFStringRy
- __ZNK14DSP_Routing_VP22IsMuteControlledByAVSCEv
- __ZNK16AudioQueueObject14BytesToPacketsEj
- __ZNK18ClientInfoAccessorptEv
- __ZNK19SharableMemoryBlock15MachClientToken7IsValidEv
- __ZNK20DSP_Routing_Borealis30ControlsSampleRateAndBlockSizeEv
- __ZNK2OS2CF4Data13GetByteLengthEv
- __ZNK2OS2CF4Data7GetDataEv
- __ZNK5boost10statechart12simple_stateIN4brls10AOPRunningENS2_3FSMENS_3mpl4listIN4mpl_2naES8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_EELNS0_12history_modeE0EE15outer_state_ptrEv
- __ZNK5boost10statechart12simple_stateIN4brls11PSAnalyzingENS2_20PhraseSpotterRunningENS_3mpl4listIN4mpl_2naES8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_EELNS0_12history_modeE0EE15outer_state_ptrEv
- __ZNK5boost10statechart12simple_stateIN4brls11PSRecordingENS2_20PhraseSpotterRunningENS_3mpl4listIN4mpl_2naES8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_EELNS0_12history_modeE0EE15outer_state_ptrEv
- __ZNK5boost10statechart12simple_stateIN4brls13PSAwaitRecordENS2_20PhraseSpotterRunningENS_3mpl4listIN4mpl_2naES8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_EELNS0_12history_modeE0EE15outer_state_ptrEv
- __ZNK5boost10statechart12simple_stateIN4brls14PSPreRecordingENS2_20PhraseSpotterRunningENS_3mpl4listIN4mpl_2naES8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_EELNS0_12history_modeE0EE15outer_state_ptrEv
- __ZNK5boost10statechart12simple_stateIN4brls18RecordingWithoutPSENS2_3FSMENS_3mpl4listIN4mpl_2naES8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_EELNS0_12history_modeE0EE15outer_state_ptrEv
- __ZNK5boost10statechart12simple_stateIN4brls20PhraseSpotterRunningENS2_3FSMENS2_11PSAnalyzingELNS0_12history_modeE0EE15outer_state_ptrEv
- __ZNK5boost10statechart12simple_stateIN4brls5ResetENS2_3FSMENS_3mpl4listIN4mpl_2naES8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_EELNS0_12history_modeE0EE15outer_state_ptrEv
- __ZNK5boost10statechart12simple_stateIN4brls7PSResetENS2_20PhraseSpotterRunningENS_3mpl4listIN4mpl_2naES8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_EELNS0_12history_modeE0EE15outer_state_ptrEv
- __ZNK5boost10statechart12simple_stateIN4brls9QuiescentENS2_3FSMENS_3mpl4listIN4mpl_2naES8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_EELNS0_12history_modeE0EE15outer_state_ptrEv
- __ZNK5boost10statechart5eventIN4brls12EvtPSTriggerENSt3__19allocatorINS0_4noneEEEE5cloneEv
- __ZNK5boost10statechart5eventIN4brls13EvtAOPTriggerENSt3__19allocatorINS0_4noneEEEE5cloneEv
- __ZNK5boost10statechart5eventIN4brls14EvtVTSMEnabledENSt3__19allocatorINS0_4noneEEEE5cloneEv
- __ZNK5boost10statechart5eventIN4brls15EvtVTSMDisabledENSt3__19allocatorINS0_4noneEEEE5cloneEv
- __ZNK5boost10statechart5eventIN4brls16EvtInternalResetENSt3__19allocatorINS0_4noneEEEE5cloneEv
- __ZNK5boost10statechart5eventIN4brls16EvtStopRecordingENSt3__19allocatorINS0_4noneEEEE5cloneEv
- __ZNK5boost10statechart5eventIN4brls17EvtPSCheckStartIOENSt3__19allocatorINS0_4noneEEEE5cloneEv
- __ZNK5boost10statechart5eventIN4brls17EvtStartRecordingENSt3__19allocatorINS0_4noneEEEE5cloneEv
- __ZNK5boost10statechart5eventIN4brls19EvtPSStopSecondPassENSt3__19allocatorINS0_4noneEEEE5cloneEv
- __ZNK5boost10statechart5eventIN4brls20EvtPreStartRecordingENSt3__19allocatorINS0_4noneEEEE5cloneEv
- __ZNK5boost10statechart5eventIN4brls21EvtStartRecordTimeoutENSt3__19allocatorINS0_4noneEEEE5cloneEv
- __ZNKSt3__110__function6__funcINS_6__bindIRFN5caulk8expectedINS_10unique_ptrIN14MixTapToUplink12TapConnectorENS_14default_deleteIS7_EEEEiEERS6_NS_13unordered_mapIjiNS_4hashIjEENS_8equal_toIjEENS_9allocatorINS_4pairIKjiEEEEEEEJRKNS_12placeholders4__phILi1EEERKNSR_ILi2EEEEEENSI_ISY_EEFSB_SC_RKSN_EE7__cloneEPNS0_6__baseIS12_EE
- __ZNKSt3__110__function6__funcINS_6__bindIRFN5caulk8expectedINS_10unique_ptrIN14MixTapToUplink12TapConnectorENS_14default_deleteIS7_EEEEiEERS6_NS_13unordered_mapIjiNS_4hashIjEENS_8equal_toIjEENS_9allocatorINS_4pairIKjiEEEEEEEJRKNS_12placeholders4__phILi1EEERKNSR_ILi2EEEEEENSI_ISY_EEFSB_SC_RKSN_EE7__cloneEv
- __ZNKSt3__110__function6__funcIU8__strongU13block_pointerFvmENS_9allocatorIS4_EES2_E7__cloneEPNS0_6__baseIS2_EE
- __ZNKSt3__110__function6__funcIU8__strongU13block_pointerFvmENS_9allocatorIS4_EES2_E7__cloneEv
- __ZNKSt3__110__function6__funcIU8__strongU13block_pointerFvvENS_9allocatorIS4_EES2_E7__cloneEPNS0_6__baseIS2_EE
- __ZNKSt3__110__function6__funcIU8__strongU13block_pointerFvvENS_9allocatorIS4_EES2_E7__cloneEv
- __ZNKSt3__110__function6__funcIZ25AudioSessionSetCMPropertyE3$_0NS_9allocatorIS2_EEFNS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS3_IcEEEESA_EEN10applesauce2CF7TypeRefESE_EE7__cloneEPNS0_6__baseISF_EE
- __ZNKSt3__110__function6__funcIZ25AudioSessionSetCMPropertyE3$_0NS_9allocatorIS2_EEFNS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS3_IcEEEESA_EEN10applesauce2CF7TypeRefESE_EE7__cloneEv
- __ZNKSt3__110__function6__funcIZ27TranslateCMSessionErrorCodePKcRKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEiiE3$_0NS7_ISC_EEFNS_4pairIS9_S9_EEN10applesauce2CF7TypeRefESI_EE7__cloneEPNS0_6__baseISJ_EE
- __ZNKSt3__110__function6__funcIZ27TranslateCMSessionErrorCodePKcRKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEiiE3$_0NS7_ISC_EEFNS_4pairIS9_S9_EEN10applesauce2CF7TypeRefESI_EE7__cloneEv
- __ZNKSt3__110__function6__funcIZ29SystemSoundServerPlayActionIDE3$_0NS_9allocatorIS2_EEFvvEE7__cloneEPNS0_6__baseIS5_EE
- __ZNKSt3__110__function6__funcIZ29SystemSoundServerPlayActionIDE3$_0NS_9allocatorIS2_EEFvvEE7__cloneEv
- __ZNKSt3__110__function6__funcIZ62-[AVHapticServer incrementRunningCountForAudio:haptics:entry:]E3$_1NS_9allocatorIS2_EEFivEE7__cloneEPNS0_6__baseIS5_EE
- __ZNKSt3__110__function6__funcIZ62-[AVHapticServer incrementRunningCountForAudio:haptics:entry:]E3$_1NS_9allocatorIS2_EEFivEE7__cloneEv
- __ZNKSt3__110__function6__funcIZN10AQMEIO_HAL13UpdateStreamsEvE3$_1NS_9allocatorIS3_EEFbRK26AudioObjectPropertyAddressEE7__cloneEPNS0_6__baseIS9_EE
- __ZNKSt3__110__function6__funcIZN10AQMEIO_HAL13UpdateStreamsEvE3$_1NS_9allocatorIS3_EEFbRK26AudioObjectPropertyAddressEE7__cloneEv
- __ZNKSt3__110__function6__funcIZN11ClientEntry17doPrepareSequenceENS_10shared_ptrI14HapticSequenceEENS_8functionIFvmEEEE3$_0NS_9allocatorIS9_EES7_E7__cloneEPNS0_6__baseIS7_EE
- __ZNKSt3__110__function6__funcIZN11ClientEntry17doPrepareSequenceENS_10shared_ptrI14HapticSequenceEENS_8functionIFvmEEEE3$_0NS_9allocatorIS9_EES7_E7__cloneEv
- __ZNKSt3__110__function6__funcIZN13MESubmixGraph19attach1MixerChannelEP14MEMixerChannelE3$_1NS_9allocatorIS5_EEFvvEE7__cloneEPNS0_6__baseIS8_EE
- __ZNKSt3__110__function6__funcIZN13MESubmixGraph19attach1MixerChannelEP14MEMixerChannelE3$_1NS_9allocatorIS5_EEFvvEE7__cloneEv
- __ZNKSt3__110__function6__funcIZN13ServerManager12DoRenderProcERK14AudioTimeStampjE3$_1NS_9allocatorIS6_EEFKNS2_12SynthCommandEvEE7__cloneEPNS0_6__baseISB_EE
- __ZNKSt3__110__function6__funcIZN13ServerManager12DoRenderProcERK14AudioTimeStampjE3$_1NS_9allocatorIS6_EEFKNS2_12SynthCommandEvEE7__cloneEv
- __ZNKSt3__110__function6__funcIZN13ServerManager16playAlertPatternENS_10shared_ptrI11ClientEntryEEPKvfP20SSPlayerSynchronizerjNS_8functionIFvvEEEE3$_0NS_9allocatorISD_EEFvmEE7__cloneEPNS0_6__baseISG_EE
- __ZNKSt3__110__function6__funcIZN13ServerManager16playAlertPatternENS_10shared_ptrI11ClientEntryEEPKvfP20SSPlayerSynchronizerjNS_8functionIFvvEEEE3$_0NS_9allocatorISD_EEFvmEE7__cloneEv
- __ZNKSt3__110__function6__funcIZN15AQMixEngine_VAD17maintainVADevicesEbE3$_2NS_9allocatorIS3_EEFbR14AQIONodeClientEE7__cloneEPNS0_6__baseIS8_EE
- __ZNKSt3__110__function6__funcIZN15AQMixEngine_VAD17maintainVADevicesEbE3$_2NS_9allocatorIS3_EEFbR14AQIONodeClientEE7__cloneEv
- __ZNKSt3__110__function6__funcIZN15AQMixEngine_VAD28routeSupportsEnhanceDialogueEvE3$_0NS_9allocatorIS3_EEFvR10AQMEDeviceEE7__cloneEPNS0_6__baseIS8_EE
- __ZNKSt3__110__function6__funcIZN15AQMixEngine_VAD28routeSupportsEnhanceDialogueEvE3$_0NS_9allocatorIS3_EEFvR10AQMEDeviceEE7__cloneEv
- __ZNKSt3__110__function6__funcIZN15AQMixEngine_VAD31IsOwnerOfAudioObject_DeprecatedEjEUlR10AQMEDeviceE_NS_9allocatorIS5_EEFvS4_EE7__cloneEPNS0_6__baseIS8_EE
- __ZNKSt3__110__function6__funcIZN15AQMixEngine_VAD31IsOwnerOfAudioObject_DeprecatedEjEUlR10AQMEDeviceE_NS_9allocatorIS5_EEFvS4_EE7__cloneEv
- __ZNKSt3__110__function6__funcIZN15AQMixEngine_VAD37SetAudioObjectPropertyData_DeprecatedEjRK26AudioObjectPropertyAddressjPKvjS7_EUlR10AQMEDeviceE_NS_9allocatorISA_EEFvS9_EE7__cloneEPNS0_6__baseISD_EE
- __ZNKSt3__110__function6__funcIZN15AQMixEngine_VAD37SetAudioObjectPropertyData_DeprecatedEjRK26AudioObjectPropertyAddressjPKvjS7_EUlR10AQMEDeviceE_NS_9allocatorISA_EEFvS9_EE7__cloneEv
- __ZNKSt3__110__function6__funcIZN16AQMixEngine_Base10DebugPrintEP7__sFILEPKcE3$_0NS_9allocatorIS7_EEFvR10AQMEDeviceEE7__cloneEPNS0_6__baseISC_EE
- __ZNKSt3__110__function6__funcIZN16AQMixEngine_Base10DebugPrintEP7__sFILEPKcE3$_0NS_9allocatorIS7_EEFvR10AQMEDeviceEE7__cloneEv
- __ZNKSt3__110__function6__funcIZN16AQMixEngine_Base12maintainTapsEbEUlR10AQMEDeviceE_NS_9allocatorIS5_EEFvS4_EE7__cloneEPNS0_6__baseIS8_EE
- __ZNKSt3__110__function6__funcIZN16AQMixEngine_Base12maintainTapsEbEUlR10AQMEDeviceE_NS_9allocatorIS5_EEFvS4_EE7__cloneEv
- __ZNKSt3__110__function6__funcIZN16AQMixEngine_Base13silenceOutputERK11AQMESessionjEUlR10AQMEDeviceE_NS_9allocatorIS8_EEFvS7_EE7__cloneEPNS0_6__baseISB_EE
- __ZNKSt3__110__function6__funcIZN16AQMixEngine_Base13silenceOutputERK11AQMESessionjEUlR10AQMEDeviceE_NS_9allocatorIS8_EEFvS7_EE7__cloneEv
- __ZNKSt3__110__function6__funcIZN16AQMixEngine_Base16StopFreewheelingEvEUlR10AQMEDeviceE_NS_9allocatorIS5_EEFvS4_EE7__cloneEPNS0_6__baseIS8_EE
- __ZNKSt3__110__function6__funcIZN16AQMixEngine_Base16StopFreewheelingEvEUlR10AQMEDeviceE_NS_9allocatorIS5_EEFvS4_EE7__cloneEv
- __ZNKSt3__110__function6__funcIZN16AQMixEngine_Base17SoundCheckChangedEvEUlR10AQMEDeviceE_NS_9allocatorIS5_EEFvS4_EE7__cloneEPNS0_6__baseIS8_EE
- __ZNKSt3__110__function6__funcIZN16AQMixEngine_Base17SoundCheckChangedEvEUlR10AQMEDeviceE_NS_9allocatorIS5_EEFvS4_EE7__cloneEv
- __ZNKSt3__110__function6__funcIZN16AQMixEngine_Base18setDynamicsEnabledE15EDynamicsEnableEUlR10AQMEDeviceE_NS_9allocatorIS6_EEFvS5_EE7__cloneEPNS0_6__baseIS9_EE
- __ZNKSt3__110__function6__funcIZN16AQMixEngine_Base18setDynamicsEnabledE15EDynamicsEnableEUlR10AQMEDeviceE_NS_9allocatorIS6_EEFvS5_EE7__cloneEv
- __ZNKSt3__110__function6__funcIZN16AQMixEngine_Base23MonoAudioSettingChangedEvEUlR10AQMEDeviceE_NS_9allocatorIS5_EEFvS4_EE7__cloneEPNS0_6__baseIS8_EE
- __ZNKSt3__110__function6__funcIZN16AQMixEngine_Base23MonoAudioSettingChangedEvEUlR10AQMEDeviceE_NS_9allocatorIS5_EEFvS4_EE7__cloneEv
- __ZNKSt3__110__function6__funcIZN16AQMixEngine_Base25AccessibilityPrefsChangedEvEUlR10AQMEDeviceE_NS_9allocatorIS5_EEFvS4_EE7__cloneEPNS0_6__baseIS8_EE
- __ZNKSt3__110__function6__funcIZN16AQMixEngine_Base25AccessibilityPrefsChangedEvEUlR10AQMEDeviceE_NS_9allocatorIS5_EEFvS4_EE7__cloneEv
- __ZNKSt3__110__function6__funcIZN16AQMixEngine_Base25ScreenSharingStateChangedEyEUlR10AQMEDeviceE_NS_9allocatorIS5_EEFvS4_EE7__cloneEPNS0_6__baseIS8_EE
- __ZNKSt3__110__function6__funcIZN16AQMixEngine_Base25ScreenSharingStateChangedEyEUlR10AQMEDeviceE_NS_9allocatorIS5_EEFvS4_EE7__cloneEv
- __ZNKSt3__110__function6__funcIZN16AQMixEngine_Base27DistributeProcessorPropertyE13MEProcessorIDjRjPvEUlR10AQMEDeviceE_NS_9allocatorIS8_EEFvS7_EE7__cloneEPNS0_6__baseISB_EE
- __ZNKSt3__110__function6__funcIZN16AQMixEngine_Base27DistributeProcessorPropertyE13MEProcessorIDjRjPvEUlR10AQMEDeviceE_NS_9allocatorIS8_EEFvS7_EE7__cloneEv
- __ZNKSt3__110__function6__funcIZN16AQMixEngine_Base29RestartIOFollowingRouteChangeEvEUlR10AQMEDeviceE_NS_9allocatorIS5_EEFvS4_EE7__cloneEPNS0_6__baseIS8_EE
- __ZNKSt3__110__function6__funcIZN16AQMixEngine_Base29RestartIOFollowingRouteChangeEvEUlR10AQMEDeviceE_NS_9allocatorIS5_EEFvS4_EE7__cloneEv
- __ZNKSt3__110__function6__funcIZN17BorealisManagerV210InitializeEvE3$_1NS_9allocatorIS3_EEFbjRKN15CAListenerProxy15HALNotificationEEE7__cloneEPNS0_6__baseISA_EE
- __ZNKSt3__110__function6__funcIZN17BorealisManagerV210InitializeEvE3$_1NS_9allocatorIS3_EEFbjRKN15CAListenerProxy15HALNotificationEEE7__cloneEv
- __ZNKSt3__110__function6__funcIZN17LegacyHapticSynth19handleRunModeChangeEjE3$_1NS_9allocatorIS3_EEFivEE7__cloneEPNS0_6__baseIS6_EE
- __ZNKSt3__110__function6__funcIZN17LegacyHapticSynth19handleRunModeChangeEjE3$_1NS_9allocatorIS3_EEFivEE7__cloneEv
- __ZNKSt3__110__function6__funcIZN18BorealisServerImpl27enableVoiceTriggerListeningEbbU13block_pointerFvP7NSErrorEEUljRKN15CAListenerProxy15HALNotificationEE_NS_9allocatorISB_EEFbjSA_EE7__cloneEPNS0_6__baseISE_EE
- __ZNKSt3__110__function6__funcIZN18BorealisServerImpl27enableVoiceTriggerListeningEbbU13block_pointerFvP7NSErrorEEUljRKN15CAListenerProxy15HALNotificationEE_NS_9allocatorISB_EEFbjSA_EE7__cloneEv
- __ZNKSt3__110__function6__funcIZN18BorealisServerImpl31updateVoiceTriggerConfigurationEPK14__CFDictionaryU13block_pointerFvP7NSErrorEEUljRKN15CAListenerProxy15HALNotificationEE_NS_9allocatorISE_EEFbjSD_EE7__cloneEPNS0_6__baseISH_EE
- __ZNKSt3__110__function6__funcIZN18BorealisServerImpl31updateVoiceTriggerConfigurationEPK14__CFDictionaryU13block_pointerFvP7NSErrorEEUljRKN15CAListenerProxy15HALNotificationEE_NS_9allocatorISE_EEFbjSD_EE7__cloneEv
- __ZNKSt3__110__function6__funcIZN18BorealisServerImpl40registerStateChangedNotificationHandlersEbEUljRKN15CAListenerProxy15HALNotificationEE_NS_9allocatorIS7_EEFbjS6_EE7__cloneEPNS0_6__baseISA_EE
- __ZNKSt3__110__function6__funcIZN18BorealisServerImpl40registerStateChangedNotificationHandlersEbEUljRKN15CAListenerProxy15HALNotificationEE_NS_9allocatorIS7_EEFbjS6_EE7__cloneEv
- __ZNKSt3__110__function6__funcIZN18BorealisServerImpl42registerAOPVoiceTriggerNotificationHandlerEjbEUljRKN15CAListenerProxy15HALNotificationEE_NS_9allocatorIS7_EEFbjS6_EE7__cloneEPNS0_6__baseISA_EE
- __ZNKSt3__110__function6__funcIZN18BorealisServerImpl42registerAOPVoiceTriggerNotificationHandlerEjbEUljRKN15CAListenerProxy15HALNotificationEE_NS_9allocatorIS7_EEFbjS6_EE7__cloneEv
- __ZNKSt3__110__function6__funcIZN18BorealisServerImpl43registerAOPEnableChangedNotificationHandlerEbEUljRKN15CAListenerProxy15HALNotificationEE_NS_9allocatorIS7_EEFbjS6_EE7__cloneEPNS0_6__baseISA_EE
- __ZNKSt3__110__function6__funcIZN18BorealisServerImpl43registerAOPEnableChangedNotificationHandlerEbEUljRKN15CAListenerProxy15HALNotificationEE_NS_9allocatorIS7_EEFbjS6_EE7__cloneEv
- __ZNKSt3__110__function6__funcIZN20DSP_Routing_Borealis3AOP35registerAOPVoiceTriggerNotificationEbE3$_0NS_9allocatorIS4_EEFbjRKN15CAListenerProxy15HALNotificationEEE7__cloneEPNS0_6__baseISB_EE
- __ZNKSt3__110__function6__funcIZN20DSP_Routing_Borealis3AOP35registerAOPVoiceTriggerNotificationEbE3$_0NS_9allocatorIS4_EEFbjRKN15CAListenerProxy15HALNotificationEEE7__cloneEv
- __ZNKSt3__110__function6__funcIZN20DSP_Routing_Borealis3AOP45updateFirstPassModelOnAOPAndWaitForCompletionEvE3$_0NS_9allocatorIS4_EEFbjRKN15CAListenerProxy15HALNotificationEEE7__cloneEPNS0_6__baseISB_EE
- __ZNKSt3__110__function6__funcIZN20DSP_Routing_Borealis3AOP45updateFirstPassModelOnAOPAndWaitForCompletionEvE3$_0NS_9allocatorIS4_EEFbjRKN15CAListenerProxy15HALNotificationEEE7__cloneEv
- __ZNKSt3__110__function6__funcIZN22MultiOutputHapticSynth12startRunningEbbjNS_8functionIFivEEEjE3$_1NS_9allocatorIS6_EES4_E7__cloneEPNS0_6__baseIS4_EE
- __ZNKSt3__110__function6__funcIZN22MultiOutputHapticSynth12startRunningEbbjNS_8functionIFivEEEjE3$_1NS_9allocatorIS6_EES4_E7__cloneEv
- __ZNKSt3__110__function6__funcIZN22MultiOutputHapticSynth19handleRunModeChangeEjE3$_3NS_9allocatorIS3_EEFivEE7__cloneEPNS0_6__baseIS6_EE
- __ZNKSt3__110__function6__funcIZN22MultiOutputHapticSynth19handleRunModeChangeEjE3$_3NS_9allocatorIS3_EEFivEE7__cloneEv
- __ZNKSt3__110__function6__funcIZN2AQ3API7ManagerC1EbRNS3_11CaptureBaseEN5caulk19lifetime_erased_ptrI23AudioQueueXPC_InterfaceEEE3$_0NS_9allocatorISB_EEFiN10applesauce3xpc6objectEEE7__cloneEPNS0_6__baseISH_EE
- __ZNKSt3__110__function6__funcIZN2AQ3API7ManagerC1EbRNS3_11CaptureBaseEN5caulk19lifetime_erased_ptrI23AudioQueueXPC_InterfaceEEE3$_0NS_9allocatorISB_EEFiN10applesauce3xpc6objectEEE7__cloneEv
- __ZNKSt3__110__function6__funcIZN2AQ3API7ManagerC1EbRNS3_11CaptureBaseEN5caulk19lifetime_erased_ptrI23AudioQueueXPC_InterfaceEEE3$_1NS_9allocatorISB_EEFvRN4swix12ipc_endpointERKN10applesauce3xpc6objectEEE7__cloneEPNS0_6__baseISM_EE
- __ZNKSt3__110__function6__funcIZN2AQ3API7ManagerC1EbRNS3_11CaptureBaseEN5caulk19lifetime_erased_ptrI23AudioQueueXPC_InterfaceEEE3$_1NS_9allocatorISB_EEFvRN4swix12ipc_endpointERKN10applesauce3xpc6objectEEE7__cloneEv
- __ZNKSt3__110__function6__funcIZZN13MESubmixGraph19attach1MixerChannelEP14MEMixerChannelENK3$_0clI9TapSubmixEEDaRT_EUlvE_NS_9allocatorISB_EEFvvEE7__cloneEPNS0_6__baseISE_EE
- __ZNKSt3__110__function6__funcIZZN13MESubmixGraph19attach1MixerChannelEP14MEMixerChannelENK3$_0clI9TapSubmixEEDaRT_EUlvE_NS_9allocatorISB_EEFvvEE7__cloneEv
- __ZNKSt3__110__function6__funcIZZN14RemoteIOClient20IONode_FormatChangedEjEUb_E3$_0NS_9allocatorIS3_EEFvvEE7__cloneEPNS0_6__baseIS6_EE
- __ZNKSt3__110__function6__funcIZZN14RemoteIOClient20IONode_FormatChangedEjEUb_E3$_0NS_9allocatorIS3_EEFvvEE7__cloneEv
- __ZNKSt3__110__function6__funcIZZN22MultiOutputHapticSynth11stopRunningEbbjENK3$_3clERNS_10unique_ptrI11SynthOutputNS_14default_deleteIS5_EEEEEUlvE_NS_9allocatorISA_EEFvvEE7__cloneEPNS0_6__baseISD_EE
- __ZNKSt3__110__function6__funcIZZN22MultiOutputHapticSynth11stopRunningEbbjENK3$_3clERNS_10unique_ptrI11SynthOutputNS_14default_deleteIS5_EEEEEUlvE_NS_9allocatorISA_EEFvvEE7__cloneEv
- __ZNKSt3__111__copy_implINS_17_ClassicAlgPolicyEEclB8ne190102IP15MEVADIdentifierS5_S5_EENS_4pairIT_T1_EES7_T0_S8_
- __ZNKSt3__111__move_implINS_17_ClassicAlgPolicyEEclB8ne190102IPNS_4pairIN5boost8functionIFNS5_3msm4back11HandledEnumEvEEEbEENS_16__deque_iteratorISC_SD_RSC_PSD_lLl102EEELi0EEENS4_IT_T0_EESI_SI_SJ_
- __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_out_of_rangeB8ne190102Ev
- __ZNKSt3__113__string_hashIcNS_9allocatorIcEEEclB8ne190102ERKNS_12basic_stringIcNS_11char_traitsIcEES2_EE
- __ZNKSt3__114default_deleteI13XOSTransactorEclB8ne190102EPS1_
- __ZNKSt3__114default_deleteI14CAMemoryStreamEclB8ne190102EPS1_
- __ZNKSt3__114default_deleteI15AudioTapManagerEclB8ne190102EPS1_
- __ZNKSt3__114default_deleteI16SSSVibrationDataEclB8ne190102EPS1_
- __ZNKSt3__114default_deleteI18AudioRingAllocatorEclB8ne190102EPS1_
- __ZNKSt3__114default_deleteI19MESchedulingVectorsEclB8ne190102EPS1_
- __ZNKSt3__114default_deleteI20SSSBufferClickFilterEclB8ne190102EPS1_
- __ZNKSt3__114default_deleteI29AudioSessionPropertyListenersEclB8ne190102EPS1_
- __ZNKSt3__114default_deleteIN11HeadTracker18HeadTrackerSessionEEclB8ne190102EPS2_
- __ZNKSt3__114default_deleteIN12CADeprecated12CABufferListEEclB8ne190102EPS2_
- __ZNKSt3__114default_deleteIN14MixTapToUplink27UplinkSpeechMixerCPPWrapperEEclB8ne190102EPS2_
- __ZNKSt3__114default_deleteIN18PowerUsageWatchdog23AudioSessionDescriptionEEclB8ne190102EPS2_
- __ZNKSt3__114default_deleteIN2CA12AudioBuffersEEclB8ne190102EPS2_
- __ZNKSt3__114default_deleteINS_5tupleIJN5caulk6thread10attributesEZN26ClientProcessingTapManager6AddTapEjjRK27AudioStreamBasicDescriptionEUlvE_NS1_IJEEEEEEEclB8ne190102EPSB_
- __ZNKSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE3strB8ne190102IS4_EENS_12basic_stringIcS2_T_EERKS8_
- __ZNKSt3__120__move_backward_implINS_17_ClassicAlgPolicyEEclB8ne190102IPNS_4pairIN5boost8functionIFNS5_3msm4back11HandledEnumEvEEEbEENS_16__deque_iteratorISC_SD_RSC_PSD_lLl102EEELi0EEENS4_IT_T0_EESI_SI_SJ_
- __ZNKSt3__16vectorI10ChaseEventNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorI10MusicEventNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorI10PowerMeterNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorI11AQMESessionNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorI11TrackChaserNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorI11VolumeEventNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorI13ChaseInstInfoNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorI13RootQueueInfoNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorI14MEStreamTypeIDNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorI15MEVADIdentifierNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorI15MeterTrackEntryNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorI16AURateRampStructNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorI18AudioMetadataEventNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorI20AUNodeRenderCallbackNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorI22AUGraphLiveUpdateEventNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorI23AudioUnitNodeConnectionNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorI23AudioUnitParameterEventNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorI24AudioQueueParameterEventNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorI25AudioQueueLevelMeterStateNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorI26AQBufferCreateDestroyEventNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorI26AudioObjectPropertyAddressNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorI27AudioQueueChannelAssignmentNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorI28AudioStreamPacketDescriptionNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorI30AQProcessingNodeImmediateEventNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorI32AudioSessionPropertyListenerInfoNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorI9TapSourceNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN10applesauce2CF11TypeRefPairENS_9allocatorIS3_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN10applesauce2CF7TypeRefENS_9allocatorIS3_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN10applesauce2CF9NumberRefENS_9allocatorIS3_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN11AQClientMgr17ClientServerQueueENS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN14AudioUnitGraph14RenderCallbackENS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN14NoteOffManager14ControlMessageENS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN16AudioQueueObject12AQRateChangeENS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN16ClientAudioQueue16PropertyListenerENS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN18AQOfflineMixerBase10MixerQueueENS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN18AQOfflineMixerBase15StartQueueEventENS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN18PlayerSynchronizer6PlayerENS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN19SequenceDestination14TrackPlayStateENS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN21VibeToHapticConverter11SegmentInfoENS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN25AUNodeSequenceDestination18RampTrackPlayStateENS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN2AQ6Server12RemoteClient18ProcessingTapStateENS_9allocatorIS4_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN2AQ6Server12RemoteClient5QueueENS_9allocatorIS4_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN2AU8Property10Attributes7details15AUPresetWrapperENS_9allocatorIS5_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN5boost8functionIFvRN11SequenceFSM25PostRenderFlushingVisitorEP14SequenceActiondEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN8InfoList9InfoEntryENS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN8TempoMap10TempoEntryENS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN8XAUMixer11EInputStateENS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN8audioipc18SharedAudioBuffers7ElementENS_9allocatorIS3_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN8audioipc18SharedAudioBuffers7ElementENS_9allocatorIS3_EEE20__throw_out_of_rangeB8ne190102Ev
- __ZNKSt3__16vectorINS_10shared_ptrI14HapticSequenceEEN5caulk12rt_allocatorIS3_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorINS_10shared_ptrI8AQIONodeEENS_9allocatorIS3_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorINS_10shared_ptrI9TapSubmixEENS_9allocatorIS3_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorINS_10shared_ptrIN10AQMEIO_HAL8IOStreamEEENS_9allocatorIS4_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorINS_10shared_ptrIN18PowerUsageWatchdog17ClientDescriptionEEENS_9allocatorIS4_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorINS_10unique_ptrI14AQClientBufferN2AQ3API13BufferDeleterEEENS_9allocatorIS6_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorINS_10unique_ptrI14AQOfflineMixerNS_14default_deleteIS2_EEEENS_9allocatorIS5_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorINS_10unique_ptrI15SubmixTapObjectNS_14default_deleteIS2_EEEENS_9allocatorIS5_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorINS_10unique_ptrI16AQProcessingNodeNS_14default_deleteIS2_EEEENS_9allocatorIS5_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorINS_10unique_ptrI16MCProcessingNodeNS_14default_deleteIS2_EEEENS_9allocatorIS5_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorINS_10unique_ptrI16SSSVibrationDataNS_14default_deleteIS2_EEEENS_9allocatorIS5_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorINS_10unique_ptrIN15AQMixEngine_VAD10MEVADeviceENS_14default_deleteIS3_EEEENS_9allocatorIS6_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorINS_10unique_ptrIN18PowerUsageWatchdog12ClientLoggerENS_14default_deleteIS3_EEEENS_9allocatorIS6_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorINS_10unique_ptrIN2AQ6Server12RemoteClientENS_14default_deleteIS4_EEEENS_9allocatorIS7_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorINS_4pairIN2OS2CF6StringEN10applesauce8dispatch2v15blockIFv13CAOrientationEEEEENS_9allocatorISC_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorINS_4pairINS_10unique_ptrI11SynthOutputNS_14default_deleteIS3_EEEEbEENS_9allocatorIS7_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorINS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEES7_EENS5_IS8_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorINS_4pairIPFiPvPjPK14AudioTimeStampjjP15AudioBufferListES2_EEN5caulk12rt_allocatorISB_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorINS_4pairIjNS_10shared_ptrIN2AQ3API11BufferOwnerEEEEENS_9allocatorIS7_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorINS_4pairIjNS_8optionalIjEEEENS_9allocatorIS4_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorINS_5tupleIJjNS_10shared_ptrIN2AQ3API5QueueEEEEEENS_9allocatorIS7_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorINS_5tupleIJjNS_10shared_ptrIN2AQ3API9SubmixTapEEEEEENS_9allocatorIS7_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorINS_5tupleIJjPFvPvP16OpaqueAudioQueuejES2_EEENS_9allocatorIS7_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorINS_8weak_ptrI8AQIONodeEENS_9allocatorIS3_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorINS_8weak_ptrIN5caulk17lifetime_observedINS_10unique_ptrI16AQMEIO_InterfaceNS_14default_deleteIS5_EEEENS2_23shared_instance_managerIS5_E8observerEEEEENS_9allocatorISD_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIP10AUNodeInfoNS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIP10ClientInfoNS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIP10ClientInfoNS_9allocatorIS2_EEE20__throw_out_of_rangeB8ne190102Ev
- __ZNKSt3__16vectorIP11MCAudioUnitNS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIP11MEConnectorNS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIP12SSSAudioDataNS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIP13AudioTapMixerNS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIP13SequenceTrackNS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIP14AQIONodeClientNS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIP14AQOfflineMixerNS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIP14AQRemoteClientNS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIP14AudioTapObjectNS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIP14CAExternalLockNS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIP14MEMixerChannelNS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIP15InputDispatcherNS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIP15XProcessingBaseNS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIP19MEInputStreamClientNS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIP19SSSActionPlayerBaseNS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIP20DSP_Routing_BorealisNS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIP20MEOutputStreamClientNS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIP25AQMEIO_NotificationClientNS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIP25AUNodeSequenceDestinationNS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIP31MIDIEndpointSequenceDestinationNS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIP8AQIONodeNS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIP8UserInfoNS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIP8UserInfoNS_9allocatorIS2_EEE20__throw_out_of_rangeB8ne190102Ev
- __ZNKSt3__16vectorIPKvNS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIPN11DSP_Routing15PublishedStreamENS_9allocatorIS3_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIPN11DSP_Routing6StreamENS_9allocatorIS3_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIPN15CAListenerProxy8ListenerENS_9allocatorIS3_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIPN16AudioQueueObject23ScheduledSliceAllocatorENS_9allocatorIS3_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIPN16ClientAudioQueue14AQClientBufferENS_9allocatorIS3_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIPN2AQ3API12OfflineMixerENS_9allocatorIS4_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIPvNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIU8__strongP24ATAudioSessionClientImplNS_9allocatorIS3_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIcN5caulk12rt_allocatorIcEEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIcNS_9allocatorIcEEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIfNS_9allocatorIfEEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIhNS_9allocatorIhEEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIiNS_9allocatorIiEEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIjNS_9allocatorIjEEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIjNS_9allocatorIjEEE20__throw_out_of_rangeB8ne190102Ev
- __ZNKSt3__16vectorImNS_9allocatorImEEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIxNS_9allocatorIxEEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__18equal_toINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEclB8ne190102ERKS6_S9_
- __ZNSt12length_errorC1B8ne190102EPKc
- __ZNSt12out_of_rangeC1B8ne190102EPKc
- __ZNSt14overflow_errorC1B8ne190102EPKc
- __ZNSt3__110__function12__alloc_funcIZN13ServerManager16playAlertPatternENS_10shared_ptrI11ClientEntryEEPKvfP20SSPlayerSynchronizerjNS_8functionIFvvEEEE3$_0NS_9allocatorISD_EEFvmEE7destroyB8ne190102Ev
- __ZNSt3__110__function12__value_funcIFKN13ServerManager12SynthCommandEvEED2B8ne190102Ev
- __ZNSt3__110__function12__value_funcIFN5caulk8expectedINS_10unique_ptrIN14MixTapToUplink12TapConnectorENS_14default_deleteIS6_EEEEiEERS5_RKNS_13unordered_mapIjiNS_4hashIjEENS_8equal_toIjEENS_9allocatorINS_4pairIKjiEEEEEEEEC2B8ne190102ERKSQ_
- __ZNSt3__110__function12__value_funcIFN5caulk8expectedINS_10unique_ptrIN14MixTapToUplink12TapConnectorENS_14default_deleteIS6_EEEEiEERS5_RKNS_13unordered_mapIjiNS_4hashIjEENS_8equal_toIjEENS_9allocatorINS_4pairIKjiEEEEEEEED2B8ne190102Ev
- __ZNSt3__110__function12__value_funcIFN5caulk8expectedIbiEEjEEC2B8ne190102ERKS6_
- __ZNSt3__110__function12__value_funcIFN5caulk8expectedIbiEEjEED2B8ne190102Ev
- __ZNSt3__110__function12__value_funcIFNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEvEED2B8ne190102Ev
- __ZNSt3__110__function12__value_funcIFNS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEES8_EEN10applesauce2CF7TypeRefESC_EEC2B8ne190102ERKSE_
- __ZNSt3__110__function12__value_funcIFNS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEES8_EEN10applesauce2CF7TypeRefESC_EED2B8ne190102Ev
- __ZNSt3__110__function12__value_funcIFP10MarshallervEEC2B8ne190102ERKS5_
- __ZNSt3__110__function12__value_funcIFP10MarshallervEED2B8ne190102Ev
- __ZNSt3__110__function12__value_funcIFPK10__CFStringS4_EEC2B8ne190102ERKS6_
- __ZNSt3__110__function12__value_funcIFPK10__CFStringS4_EED2B8ne190102Ev
- __ZNSt3__110__function12__value_funcIFR26MutedSpeechActivityManagervEED2B8ne190102Ev
- __ZNSt3__110__function12__value_funcIFbNS_10shared_ptrI11ClientEntryEEEED2B8ne190102Ev
- __ZNSt3__110__function12__value_funcIFbPKN17ParameterSchedule5EventEEED2B8ne190102Ev
- __ZNSt3__110__function12__value_funcIFbPKvEED2B8ne190102Ev
- __ZNSt3__110__function12__value_funcIFbR14AQIONodeClientEED2B8ne190102Ev
- __ZNSt3__110__function12__value_funcIFbRK26AudioObjectPropertyAddressEED2B8ne190102Ev
- __ZNSt3__110__function12__value_funcIFbRmbEED2B8ne190102Ev
- __ZNSt3__110__function12__value_funcIFbjRKN15CAListenerProxy15HALNotificationEEEC2B8ne190102ERKS7_
- __ZNSt3__110__function12__value_funcIFbjRKN15CAListenerProxy15HALNotificationEEED2B8ne190102Ev
- __ZNSt3__110__function12__value_funcIFbjiEEC2B8ne190102ERKS3_
- __ZNSt3__110__function12__value_funcIFbjiEED2B8ne190102Ev
- __ZNSt3__110__function12__value_funcIFbvEEC2B8ne190102ERKS3_
- __ZNSt3__110__function12__value_funcIFbvEED2B8ne190102Ev
- __ZNSt3__110__function12__value_funcIFiN10applesauce3xpc6objectEEED2B8ne190102Ev
- __ZNSt3__110__function12__value_funcIFiP7__sFILEEED2B8ne190102Ev
- __ZNSt3__110__function12__value_funcIFivEEC2B8ne190102ERKS3_
- __ZNSt3__110__function12__value_funcIFivEED2B8ne190102Ev
- __ZNSt3__110__function12__value_funcIFvPK14MIDIPacketListEED2B8ne190102Ev
- __ZNSt3__110__function12__value_funcIFvR10AQMEDeviceEED2B8ne190102Ev
- __ZNSt3__110__function12__value_funcIFvRN4swix12ipc_endpointERKN10applesauce3xpc6objectEEED2B8ne190102Ev
- __ZNSt3__110__function12__value_funcIFvbEEC2B8ne190102EOS3_
- __ZNSt3__110__function12__value_funcIFvbEEC2B8ne190102ERKS3_
- __ZNSt3__110__function12__value_funcIFvbEED2B8ne190102Ev
- __ZNSt3__110__function12__value_funcIFvdEEC2B8ne190102ERKS3_
- __ZNSt3__110__function12__value_funcIFvdEED2B8ne190102Ev
- __ZNSt3__110__function12__value_funcIFviEEC2B8ne190102ERKS3_
- __ZNSt3__110__function12__value_funcIFviEED2B8ne190102Ev
- __ZNSt3__110__function12__value_funcIFvmEEC2B8ne190102ERKS3_
- __ZNSt3__110__function12__value_funcIFvmEED2B8ne190102Ev
- __ZNSt3__110__function12__value_funcIFvvEEC2B8ne190102EOS3_
- __ZNSt3__110__function12__value_funcIFvvEEC2B8ne190102ERKS3_
- __ZNSt3__110__function12__value_funcIFvvEED2B8ne190102Ev
- __ZNSt3__110__function12__value_funcIFvxEEC2B8ne190102ERKS3_
- __ZNSt3__110__function12__value_funcIFvxEED2B8ne190102Ev
- __ZNSt3__110__function6__funcINS_6__bindIRFN5caulk8expectedINS_10unique_ptrIN14MixTapToUplink12TapConnectorENS_14default_deleteIS7_EEEEiEERS6_NS_13unordered_mapIjiNS_4hashIjEENS_8equal_toIjEENS_9allocatorINS_4pairIKjiEEEEEEEJRKNS_12placeholders4__phILi1EEERKNSR_ILi2EEEEEENSI_ISY_EEFSB_SC_RKSN_EE18destroy_deallocateEv
- __ZNSt3__110__function6__funcINS_6__bindIRFN5caulk8expectedINS_10unique_ptrIN14MixTapToUplink12TapConnectorENS_14default_deleteIS7_EEEEiEERS6_NS_13unordered_mapIjiNS_4hashIjEENS_8equal_toIjEENS_9allocatorINS_4pairIKjiEEEEEEEJRKNS_12placeholders4__phILi1EEERKNSR_ILi2EEEEEENSI_ISY_EEFSB_SC_RKSN_EE7destroyEv
- __ZNSt3__110__function6__funcINS_6__bindIRFN5caulk8expectedINS_10unique_ptrIN14MixTapToUplink12TapConnectorENS_14default_deleteIS7_EEEEiEERS6_NS_13unordered_mapIjiNS_4hashIjEENS_8equal_toIjEENS_9allocatorINS_4pairIKjiEEEEEEEJRKNS_12placeholders4__phILi1EEERKNSR_ILi2EEEEEENSI_ISY_EEFSB_SC_RKSN_EED0Ev
- __ZNSt3__110__function6__funcINS_6__bindIRFN5caulk8expectedINS_10unique_ptrIN14MixTapToUplink12TapConnectorENS_14default_deleteIS7_EEEEiEERS6_NS_13unordered_mapIjiNS_4hashIjEENS_8equal_toIjEENS_9allocatorINS_4pairIKjiEEEEEEEJRKNS_12placeholders4__phILi1EEERKNSR_ILi2EEEEEENSI_ISY_EEFSB_SC_RKSN_EED1Ev
- __ZNSt3__110__function6__funcINS_6__bindIRFN5caulk8expectedINS_10unique_ptrIN14MixTapToUplink12TapConnectorENS_14default_deleteIS7_EEEEiEERS6_NS_13unordered_mapIjiNS_4hashIjEENS_8equal_toIjEENS_9allocatorINS_4pairIKjiEEEEEEEJRKNS_12placeholders4__phILi1EEERKNSR_ILi2EEEEEENSI_ISY_EEFSB_SC_RKSN_EEclESC_S11_
- __ZNSt3__110__function6__funcIU8__strongU13block_pointerFvmENS_9allocatorIS4_EES2_E18destroy_deallocateEv
- __ZNSt3__110__function6__funcIU8__strongU13block_pointerFvmENS_9allocatorIS4_EES2_E7destroyEv
- __ZNSt3__110__function6__funcIU8__strongU13block_pointerFvmENS_9allocatorIS4_EES2_ED0Ev
- __ZNSt3__110__function6__funcIU8__strongU13block_pointerFvmENS_9allocatorIS4_EES2_ED1Ev
- __ZNSt3__110__function6__funcIU8__strongU13block_pointerFvmENS_9allocatorIS4_EES2_EclEOm
- __ZNSt3__110__function6__funcIU8__strongU13block_pointerFvvENS_9allocatorIS4_EES2_E18destroy_deallocateEv
- __ZNSt3__110__function6__funcIU8__strongU13block_pointerFvvENS_9allocatorIS4_EES2_E7destroyEv
- __ZNSt3__110__function6__funcIU8__strongU13block_pointerFvvENS_9allocatorIS4_EES2_ED0Ev
- __ZNSt3__110__function6__funcIU8__strongU13block_pointerFvvENS_9allocatorIS4_EES2_ED1Ev
- __ZNSt3__110__function6__funcIU8__strongU13block_pointerFvvENS_9allocatorIS4_EES2_EclEv
- __ZNSt3__110__function6__funcIZ25AudioSessionSetCMPropertyE3$_0NS_9allocatorIS2_EEFNS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS3_IcEEEESA_EEN10applesauce2CF7TypeRefESE_EE18destroy_deallocateEv
- __ZNSt3__110__function6__funcIZ25AudioSessionSetCMPropertyE3$_0NS_9allocatorIS2_EEFNS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS3_IcEEEESA_EEN10applesauce2CF7TypeRefESE_EE7destroyEv
- __ZNSt3__110__function6__funcIZ25AudioSessionSetCMPropertyE3$_0NS_9allocatorIS2_EEFNS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS3_IcEEEESA_EEN10applesauce2CF7TypeRefESE_EED0Ev
- __ZNSt3__110__function6__funcIZ25AudioSessionSetCMPropertyE3$_0NS_9allocatorIS2_EEFNS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS3_IcEEEESA_EEN10applesauce2CF7TypeRefESE_EED1Ev
- __ZNSt3__110__function6__funcIZ25AudioSessionSetCMPropertyE3$_0NS_9allocatorIS2_EEFNS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS3_IcEEEESA_EEN10applesauce2CF7TypeRefESE_EEclEOSE_SH_
- __ZNSt3__110__function6__funcIZ27TranslateCMSessionErrorCodePKcRKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEiiE3$_0NS7_ISC_EEFNS_4pairIS9_S9_EEN10applesauce2CF7TypeRefESI_EE18destroy_deallocateEv
- __ZNSt3__110__function6__funcIZ27TranslateCMSessionErrorCodePKcRKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEiiE3$_0NS7_ISC_EEFNS_4pairIS9_S9_EEN10applesauce2CF7TypeRefESI_EE7destroyEv
- __ZNSt3__110__function6__funcIZ27TranslateCMSessionErrorCodePKcRKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEiiE3$_0NS7_ISC_EEFNS_4pairIS9_S9_EEN10applesauce2CF7TypeRefESI_EED0Ev
- __ZNSt3__110__function6__funcIZ27TranslateCMSessionErrorCodePKcRKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEiiE3$_0NS7_ISC_EEFNS_4pairIS9_S9_EEN10applesauce2CF7TypeRefESI_EED1Ev
- __ZNSt3__110__function6__funcIZ27TranslateCMSessionErrorCodePKcRKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEiiE3$_0NS7_ISC_EEFNS_4pairIS9_S9_EEN10applesauce2CF7TypeRefESI_EEclEOSI_SL_
- __ZNSt3__110__function6__funcIZ29SystemSoundServerPlayActionIDE3$_0NS_9allocatorIS2_EEFvvEE18destroy_deallocateEv
- __ZNSt3__110__function6__funcIZ29SystemSoundServerPlayActionIDE3$_0NS_9allocatorIS2_EEFvvEE7destroyEv
- __ZNSt3__110__function6__funcIZ29SystemSoundServerPlayActionIDE3$_0NS_9allocatorIS2_EEFvvEED0Ev
- __ZNSt3__110__function6__funcIZ29SystemSoundServerPlayActionIDE3$_0NS_9allocatorIS2_EEFvvEED1Ev
- __ZNSt3__110__function6__funcIZ29SystemSoundServerPlayActionIDE3$_0NS_9allocatorIS2_EEFvvEEclEv
- __ZNSt3__110__function6__funcIZ62-[AVHapticServer incrementRunningCountForAudio:haptics:entry:]E3$_1NS_9allocatorIS2_EEFivEE18destroy_deallocateEv
- __ZNSt3__110__function6__funcIZ62-[AVHapticServer incrementRunningCountForAudio:haptics:entry:]E3$_1NS_9allocatorIS2_EEFivEE7destroyEv
- __ZNSt3__110__function6__funcIZ62-[AVHapticServer incrementRunningCountForAudio:haptics:entry:]E3$_1NS_9allocatorIS2_EEFivEED0Ev
- __ZNSt3__110__function6__funcIZ62-[AVHapticServer incrementRunningCountForAudio:haptics:entry:]E3$_1NS_9allocatorIS2_EEFivEED1Ev
- __ZNSt3__110__function6__funcIZ62-[AVHapticServer incrementRunningCountForAudio:haptics:entry:]E3$_1NS_9allocatorIS2_EEFivEEclEv
- __ZNSt3__110__function6__funcIZN10AQMEIO_HAL13UpdateStreamsEvE3$_1NS_9allocatorIS3_EEFbRK26AudioObjectPropertyAddressEE18destroy_deallocateEv
- __ZNSt3__110__function6__funcIZN10AQMEIO_HAL13UpdateStreamsEvE3$_1NS_9allocatorIS3_EEFbRK26AudioObjectPropertyAddressEE7destroyEv
- __ZNSt3__110__function6__funcIZN10AQMEIO_HAL13UpdateStreamsEvE3$_1NS_9allocatorIS3_EEFbRK26AudioObjectPropertyAddressEED0Ev
- __ZNSt3__110__function6__funcIZN10AQMEIO_HAL13UpdateStreamsEvE3$_1NS_9allocatorIS3_EEFbRK26AudioObjectPropertyAddressEED1Ev
- __ZNSt3__110__function6__funcIZN10AQMEIO_HAL13UpdateStreamsEvE3$_1NS_9allocatorIS3_EEFbRK26AudioObjectPropertyAddressEEclES8_
- __ZNSt3__110__function6__funcIZN11ClientEntry17doPrepareSequenceENS_10shared_ptrI14HapticSequenceEENS_8functionIFvmEEEE3$_0NS_9allocatorIS9_EES7_E18destroy_deallocateEv
- __ZNSt3__110__function6__funcIZN11ClientEntry17doPrepareSequenceENS_10shared_ptrI14HapticSequenceEENS_8functionIFvmEEEE3$_0NS_9allocatorIS9_EES7_E7destroyEv
- __ZNSt3__110__function6__funcIZN11ClientEntry17doPrepareSequenceENS_10shared_ptrI14HapticSequenceEENS_8functionIFvmEEEE3$_0NS_9allocatorIS9_EES7_ED0Ev
- __ZNSt3__110__function6__funcIZN11ClientEntry17doPrepareSequenceENS_10shared_ptrI14HapticSequenceEENS_8functionIFvmEEEE3$_0NS_9allocatorIS9_EES7_ED1Ev
- __ZNSt3__110__function6__funcIZN11ClientEntry17doPrepareSequenceENS_10shared_ptrI14HapticSequenceEENS_8functionIFvmEEEE3$_0NS_9allocatorIS9_EES7_EclEOm
- __ZNSt3__110__function6__funcIZN13MESubmixGraph19attach1MixerChannelEP14MEMixerChannelE3$_1NS_9allocatorIS5_EEFvvEE18destroy_deallocateEv
- __ZNSt3__110__function6__funcIZN13MESubmixGraph19attach1MixerChannelEP14MEMixerChannelE3$_1NS_9allocatorIS5_EEFvvEE7destroyEv
- __ZNSt3__110__function6__funcIZN13MESubmixGraph19attach1MixerChannelEP14MEMixerChannelE3$_1NS_9allocatorIS5_EEFvvEED0Ev
- __ZNSt3__110__function6__funcIZN13MESubmixGraph19attach1MixerChannelEP14MEMixerChannelE3$_1NS_9allocatorIS5_EEFvvEED1Ev
- __ZNSt3__110__function6__funcIZN13MESubmixGraph19attach1MixerChannelEP14MEMixerChannelE3$_1NS_9allocatorIS5_EEFvvEEclEv
- __ZNSt3__110__function6__funcIZN13ServerManager12DoRenderProcERK14AudioTimeStampjE3$_1NS_9allocatorIS6_EEFKNS2_12SynthCommandEvEE18destroy_deallocateEv
- __ZNSt3__110__function6__funcIZN13ServerManager12DoRenderProcERK14AudioTimeStampjE3$_1NS_9allocatorIS6_EEFKNS2_12SynthCommandEvEE7destroyEv
- __ZNSt3__110__function6__funcIZN13ServerManager12DoRenderProcERK14AudioTimeStampjE3$_1NS_9allocatorIS6_EEFKNS2_12SynthCommandEvEED0Ev
- __ZNSt3__110__function6__funcIZN13ServerManager12DoRenderProcERK14AudioTimeStampjE3$_1NS_9allocatorIS6_EEFKNS2_12SynthCommandEvEED1Ev
- __ZNSt3__110__function6__funcIZN13ServerManager12DoRenderProcERK14AudioTimeStampjE3$_1NS_9allocatorIS6_EEFKNS2_12SynthCommandEvEEclEv
- __ZNSt3__110__function6__funcIZN13ServerManager16playAlertPatternENS_10shared_ptrI11ClientEntryEEPKvfP20SSPlayerSynchronizerjNS_8functionIFvvEEEE3$_0NS_9allocatorISD_EEFvmEE18destroy_deallocateEv
- __ZNSt3__110__function6__funcIZN13ServerManager16playAlertPatternENS_10shared_ptrI11ClientEntryEEPKvfP20SSPlayerSynchronizerjNS_8functionIFvvEEEE3$_0NS_9allocatorISD_EEFvmEE7destroyEv
- __ZNSt3__110__function6__funcIZN13ServerManager16playAlertPatternENS_10shared_ptrI11ClientEntryEEPKvfP20SSPlayerSynchronizerjNS_8functionIFvvEEEE3$_0NS_9allocatorISD_EEFvmEED0Ev
- __ZNSt3__110__function6__funcIZN13ServerManager16playAlertPatternENS_10shared_ptrI11ClientEntryEEPKvfP20SSPlayerSynchronizerjNS_8functionIFvvEEEE3$_0NS_9allocatorISD_EEFvmEED1Ev
- __ZNSt3__110__function6__funcIZN13ServerManager16playAlertPatternENS_10shared_ptrI11ClientEntryEEPKvfP20SSPlayerSynchronizerjNS_8functionIFvvEEEE3$_0NS_9allocatorISD_EEFvmEEclEOm
- __ZNSt3__110__function6__funcIZN15AQMixEngine_VAD17maintainVADevicesEbE3$_2NS_9allocatorIS3_EEFbR14AQIONodeClientEE18destroy_deallocateEv
- __ZNSt3__110__function6__funcIZN15AQMixEngine_VAD17maintainVADevicesEbE3$_2NS_9allocatorIS3_EEFbR14AQIONodeClientEE7destroyEv
- __ZNSt3__110__function6__funcIZN15AQMixEngine_VAD17maintainVADevicesEbE3$_2NS_9allocatorIS3_EEFbR14AQIONodeClientEED0Ev
- __ZNSt3__110__function6__funcIZN15AQMixEngine_VAD17maintainVADevicesEbE3$_2NS_9allocatorIS3_EEFbR14AQIONodeClientEED1Ev
- __ZNSt3__110__function6__funcIZN15AQMixEngine_VAD17maintainVADevicesEbE3$_2NS_9allocatorIS3_EEFbR14AQIONodeClientEEclES7_
- __ZNSt3__110__function6__funcIZN15AQMixEngine_VAD28routeSupportsEnhanceDialogueEvE3$_0NS_9allocatorIS3_EEFvR10AQMEDeviceEE18destroy_deallocateEv
- __ZNSt3__110__function6__funcIZN15AQMixEngine_VAD28routeSupportsEnhanceDialogueEvE3$_0NS_9allocatorIS3_EEFvR10AQMEDeviceEE7destroyEv
- __ZNSt3__110__function6__funcIZN15AQMixEngine_VAD28routeSupportsEnhanceDialogueEvE3$_0NS_9allocatorIS3_EEFvR10AQMEDeviceEED0Ev
- __ZNSt3__110__function6__funcIZN15AQMixEngine_VAD28routeSupportsEnhanceDialogueEvE3$_0NS_9allocatorIS3_EEFvR10AQMEDeviceEED1Ev
- __ZNSt3__110__function6__funcIZN15AQMixEngine_VAD28routeSupportsEnhanceDialogueEvE3$_0NS_9allocatorIS3_EEFvR10AQMEDeviceEEclES7_
- __ZNSt3__110__function6__funcIZN15AQMixEngine_VAD31IsOwnerOfAudioObject_DeprecatedEjEUlR10AQMEDeviceE_NS_9allocatorIS5_EEFvS4_EE18destroy_deallocateEv
- __ZNSt3__110__function6__funcIZN15AQMixEngine_VAD31IsOwnerOfAudioObject_DeprecatedEjEUlR10AQMEDeviceE_NS_9allocatorIS5_EEFvS4_EE7destroyEv
- __ZNSt3__110__function6__funcIZN15AQMixEngine_VAD31IsOwnerOfAudioObject_DeprecatedEjEUlR10AQMEDeviceE_NS_9allocatorIS5_EEFvS4_EED0Ev
- __ZNSt3__110__function6__funcIZN15AQMixEngine_VAD31IsOwnerOfAudioObject_DeprecatedEjEUlR10AQMEDeviceE_NS_9allocatorIS5_EEFvS4_EED1Ev
- __ZNSt3__110__function6__funcIZN15AQMixEngine_VAD31IsOwnerOfAudioObject_DeprecatedEjEUlR10AQMEDeviceE_NS_9allocatorIS5_EEFvS4_EEclES4_
- __ZNSt3__110__function6__funcIZN15AQMixEngine_VAD37SetAudioObjectPropertyData_DeprecatedEjRK26AudioObjectPropertyAddressjPKvjS7_EUlR10AQMEDeviceE_NS_9allocatorISA_EEFvS9_EE18destroy_deallocateEv
- __ZNSt3__110__function6__funcIZN15AQMixEngine_VAD37SetAudioObjectPropertyData_DeprecatedEjRK26AudioObjectPropertyAddressjPKvjS7_EUlR10AQMEDeviceE_NS_9allocatorISA_EEFvS9_EE7destroyEv
- __ZNSt3__110__function6__funcIZN15AQMixEngine_VAD37SetAudioObjectPropertyData_DeprecatedEjRK26AudioObjectPropertyAddressjPKvjS7_EUlR10AQMEDeviceE_NS_9allocatorISA_EEFvS9_EED0Ev
- __ZNSt3__110__function6__funcIZN15AQMixEngine_VAD37SetAudioObjectPropertyData_DeprecatedEjRK26AudioObjectPropertyAddressjPKvjS7_EUlR10AQMEDeviceE_NS_9allocatorISA_EEFvS9_EED1Ev
- __ZNSt3__110__function6__funcIZN15AQMixEngine_VAD37SetAudioObjectPropertyData_DeprecatedEjRK26AudioObjectPropertyAddressjPKvjS7_EUlR10AQMEDeviceE_NS_9allocatorISA_EEFvS9_EEclES9_
- __ZNSt3__110__function6__funcIZN16AQMixEngine_Base10DebugPrintEP7__sFILEPKcE3$_0NS_9allocatorIS7_EEFvR10AQMEDeviceEE18destroy_deallocateEv
- __ZNSt3__110__function6__funcIZN16AQMixEngine_Base10DebugPrintEP7__sFILEPKcE3$_0NS_9allocatorIS7_EEFvR10AQMEDeviceEE7destroyEv
- __ZNSt3__110__function6__funcIZN16AQMixEngine_Base10DebugPrintEP7__sFILEPKcE3$_0NS_9allocatorIS7_EEFvR10AQMEDeviceEED0Ev
- __ZNSt3__110__function6__funcIZN16AQMixEngine_Base10DebugPrintEP7__sFILEPKcE3$_0NS_9allocatorIS7_EEFvR10AQMEDeviceEED1Ev
- __ZNSt3__110__function6__funcIZN16AQMixEngine_Base10DebugPrintEP7__sFILEPKcE3$_0NS_9allocatorIS7_EEFvR10AQMEDeviceEEclESB_
- __ZNSt3__110__function6__funcIZN16AQMixEngine_Base12maintainTapsEbEUlR10AQMEDeviceE_NS_9allocatorIS5_EEFvS4_EE18destroy_deallocateEv
- __ZNSt3__110__function6__funcIZN16AQMixEngine_Base12maintainTapsEbEUlR10AQMEDeviceE_NS_9allocatorIS5_EEFvS4_EE7destroyEv
- __ZNSt3__110__function6__funcIZN16AQMixEngine_Base12maintainTapsEbEUlR10AQMEDeviceE_NS_9allocatorIS5_EEFvS4_EED0Ev
- __ZNSt3__110__function6__funcIZN16AQMixEngine_Base12maintainTapsEbEUlR10AQMEDeviceE_NS_9allocatorIS5_EEFvS4_EED1Ev
- __ZNSt3__110__function6__funcIZN16AQMixEngine_Base12maintainTapsEbEUlR10AQMEDeviceE_NS_9allocatorIS5_EEFvS4_EEclES4_
- __ZNSt3__110__function6__funcIZN16AQMixEngine_Base13silenceOutputERK11AQMESessionjEUlR10AQMEDeviceE_NS_9allocatorIS8_EEFvS7_EE18destroy_deallocateEv
- __ZNSt3__110__function6__funcIZN16AQMixEngine_Base13silenceOutputERK11AQMESessionjEUlR10AQMEDeviceE_NS_9allocatorIS8_EEFvS7_EE7destroyEv
- __ZNSt3__110__function6__funcIZN16AQMixEngine_Base13silenceOutputERK11AQMESessionjEUlR10AQMEDeviceE_NS_9allocatorIS8_EEFvS7_EED0Ev
- __ZNSt3__110__function6__funcIZN16AQMixEngine_Base13silenceOutputERK11AQMESessionjEUlR10AQMEDeviceE_NS_9allocatorIS8_EEFvS7_EED1Ev
- __ZNSt3__110__function6__funcIZN16AQMixEngine_Base13silenceOutputERK11AQMESessionjEUlR10AQMEDeviceE_NS_9allocatorIS8_EEFvS7_EEclES7_
- __ZNSt3__110__function6__funcIZN16AQMixEngine_Base16StopFreewheelingEvEUlR10AQMEDeviceE_NS_9allocatorIS5_EEFvS4_EE18destroy_deallocateEv
- __ZNSt3__110__function6__funcIZN16AQMixEngine_Base16StopFreewheelingEvEUlR10AQMEDeviceE_NS_9allocatorIS5_EEFvS4_EE7destroyEv
- __ZNSt3__110__function6__funcIZN16AQMixEngine_Base16StopFreewheelingEvEUlR10AQMEDeviceE_NS_9allocatorIS5_EEFvS4_EED0Ev
- __ZNSt3__110__function6__funcIZN16AQMixEngine_Base16StopFreewheelingEvEUlR10AQMEDeviceE_NS_9allocatorIS5_EEFvS4_EED1Ev
- __ZNSt3__110__function6__funcIZN16AQMixEngine_Base16StopFreewheelingEvEUlR10AQMEDeviceE_NS_9allocatorIS5_EEFvS4_EEclES4_
- __ZNSt3__110__function6__funcIZN16AQMixEngine_Base17SoundCheckChangedEvEUlR10AQMEDeviceE_NS_9allocatorIS5_EEFvS4_EE18destroy_deallocateEv
- __ZNSt3__110__function6__funcIZN16AQMixEngine_Base17SoundCheckChangedEvEUlR10AQMEDeviceE_NS_9allocatorIS5_EEFvS4_EE7destroyEv
- __ZNSt3__110__function6__funcIZN16AQMixEngine_Base17SoundCheckChangedEvEUlR10AQMEDeviceE_NS_9allocatorIS5_EEFvS4_EED0Ev
- __ZNSt3__110__function6__funcIZN16AQMixEngine_Base17SoundCheckChangedEvEUlR10AQMEDeviceE_NS_9allocatorIS5_EEFvS4_EED1Ev
- __ZNSt3__110__function6__funcIZN16AQMixEngine_Base17SoundCheckChangedEvEUlR10AQMEDeviceE_NS_9allocatorIS5_EEFvS4_EEclES4_
- __ZNSt3__110__function6__funcIZN16AQMixEngine_Base18setDynamicsEnabledE15EDynamicsEnableEUlR10AQMEDeviceE_NS_9allocatorIS6_EEFvS5_EE18destroy_deallocateEv
- __ZNSt3__110__function6__funcIZN16AQMixEngine_Base18setDynamicsEnabledE15EDynamicsEnableEUlR10AQMEDeviceE_NS_9allocatorIS6_EEFvS5_EE7destroyEv
- __ZNSt3__110__function6__funcIZN16AQMixEngine_Base18setDynamicsEnabledE15EDynamicsEnableEUlR10AQMEDeviceE_NS_9allocatorIS6_EEFvS5_EED0Ev
- __ZNSt3__110__function6__funcIZN16AQMixEngine_Base18setDynamicsEnabledE15EDynamicsEnableEUlR10AQMEDeviceE_NS_9allocatorIS6_EEFvS5_EED1Ev
- __ZNSt3__110__function6__funcIZN16AQMixEngine_Base18setDynamicsEnabledE15EDynamicsEnableEUlR10AQMEDeviceE_NS_9allocatorIS6_EEFvS5_EEclES5_
- __ZNSt3__110__function6__funcIZN16AQMixEngine_Base23MonoAudioSettingChangedEvEUlR10AQMEDeviceE_NS_9allocatorIS5_EEFvS4_EE18destroy_deallocateEv
- __ZNSt3__110__function6__funcIZN16AQMixEngine_Base23MonoAudioSettingChangedEvEUlR10AQMEDeviceE_NS_9allocatorIS5_EEFvS4_EE7destroyEv
- __ZNSt3__110__function6__funcIZN16AQMixEngine_Base23MonoAudioSettingChangedEvEUlR10AQMEDeviceE_NS_9allocatorIS5_EEFvS4_EED0Ev
- __ZNSt3__110__function6__funcIZN16AQMixEngine_Base23MonoAudioSettingChangedEvEUlR10AQMEDeviceE_NS_9allocatorIS5_EEFvS4_EED1Ev
- __ZNSt3__110__function6__funcIZN16AQMixEngine_Base23MonoAudioSettingChangedEvEUlR10AQMEDeviceE_NS_9allocatorIS5_EEFvS4_EEclES4_
- __ZNSt3__110__function6__funcIZN16AQMixEngine_Base25AccessibilityPrefsChangedEvEUlR10AQMEDeviceE_NS_9allocatorIS5_EEFvS4_EE18destroy_deallocateEv
- __ZNSt3__110__function6__funcIZN16AQMixEngine_Base25AccessibilityPrefsChangedEvEUlR10AQMEDeviceE_NS_9allocatorIS5_EEFvS4_EE7destroyEv
- __ZNSt3__110__function6__funcIZN16AQMixEngine_Base25AccessibilityPrefsChangedEvEUlR10AQMEDeviceE_NS_9allocatorIS5_EEFvS4_EED0Ev
- __ZNSt3__110__function6__funcIZN16AQMixEngine_Base25AccessibilityPrefsChangedEvEUlR10AQMEDeviceE_NS_9allocatorIS5_EEFvS4_EED1Ev
- __ZNSt3__110__function6__funcIZN16AQMixEngine_Base25AccessibilityPrefsChangedEvEUlR10AQMEDeviceE_NS_9allocatorIS5_EEFvS4_EEclES4_
- __ZNSt3__110__function6__funcIZN16AQMixEngine_Base25ScreenSharingStateChangedEyEUlR10AQMEDeviceE_NS_9allocatorIS5_EEFvS4_EE18destroy_deallocateEv
- __ZNSt3__110__function6__funcIZN16AQMixEngine_Base25ScreenSharingStateChangedEyEUlR10AQMEDeviceE_NS_9allocatorIS5_EEFvS4_EE7destroyEv
- __ZNSt3__110__function6__funcIZN16AQMixEngine_Base25ScreenSharingStateChangedEyEUlR10AQMEDeviceE_NS_9allocatorIS5_EEFvS4_EED0Ev
- __ZNSt3__110__function6__funcIZN16AQMixEngine_Base25ScreenSharingStateChangedEyEUlR10AQMEDeviceE_NS_9allocatorIS5_EEFvS4_EED1Ev
- __ZNSt3__110__function6__funcIZN16AQMixEngine_Base25ScreenSharingStateChangedEyEUlR10AQMEDeviceE_NS_9allocatorIS5_EEFvS4_EEclES4_
- __ZNSt3__110__function6__funcIZN16AQMixEngine_Base27DistributeProcessorPropertyE13MEProcessorIDjRjPvEUlR10AQMEDeviceE_NS_9allocatorIS8_EEFvS7_EE18destroy_deallocateEv
- __ZNSt3__110__function6__funcIZN16AQMixEngine_Base27DistributeProcessorPropertyE13MEProcessorIDjRjPvEUlR10AQMEDeviceE_NS_9allocatorIS8_EEFvS7_EE7destroyEv
- __ZNSt3__110__function6__funcIZN16AQMixEngine_Base27DistributeProcessorPropertyE13MEProcessorIDjRjPvEUlR10AQMEDeviceE_NS_9allocatorIS8_EEFvS7_EED0Ev
- __ZNSt3__110__function6__funcIZN16AQMixEngine_Base27DistributeProcessorPropertyE13MEProcessorIDjRjPvEUlR10AQMEDeviceE_NS_9allocatorIS8_EEFvS7_EED1Ev
- __ZNSt3__110__function6__funcIZN16AQMixEngine_Base27DistributeProcessorPropertyE13MEProcessorIDjRjPvEUlR10AQMEDeviceE_NS_9allocatorIS8_EEFvS7_EEclES7_
- __ZNSt3__110__function6__funcIZN16AQMixEngine_Base29RestartIOFollowingRouteChangeEvEUlR10AQMEDeviceE_NS_9allocatorIS5_EEFvS4_EE18destroy_deallocateEv
- __ZNSt3__110__function6__funcIZN16AQMixEngine_Base29RestartIOFollowingRouteChangeEvEUlR10AQMEDeviceE_NS_9allocatorIS5_EEFvS4_EE7destroyEv
- __ZNSt3__110__function6__funcIZN16AQMixEngine_Base29RestartIOFollowingRouteChangeEvEUlR10AQMEDeviceE_NS_9allocatorIS5_EEFvS4_EED0Ev
- __ZNSt3__110__function6__funcIZN16AQMixEngine_Base29RestartIOFollowingRouteChangeEvEUlR10AQMEDeviceE_NS_9allocatorIS5_EEFvS4_EED1Ev
- __ZNSt3__110__function6__funcIZN16AQMixEngine_Base29RestartIOFollowingRouteChangeEvEUlR10AQMEDeviceE_NS_9allocatorIS5_EEFvS4_EEclES4_
- __ZNSt3__110__function6__funcIZN17BorealisManagerV210InitializeEvE3$_1NS_9allocatorIS3_EEFbjRKN15CAListenerProxy15HALNotificationEEE18destroy_deallocateEv
- __ZNSt3__110__function6__funcIZN17BorealisManagerV210InitializeEvE3$_1NS_9allocatorIS3_EEFbjRKN15CAListenerProxy15HALNotificationEEE7destroyEv
- __ZNSt3__110__function6__funcIZN17BorealisManagerV210InitializeEvE3$_1NS_9allocatorIS3_EEFbjRKN15CAListenerProxy15HALNotificationEEED0Ev
- __ZNSt3__110__function6__funcIZN17BorealisManagerV210InitializeEvE3$_1NS_9allocatorIS3_EEFbjRKN15CAListenerProxy15HALNotificationEEED1Ev
- __ZNSt3__110__function6__funcIZN17BorealisManagerV210InitializeEvE3$_1NS_9allocatorIS3_EEFbjRKN15CAListenerProxy15HALNotificationEEEclEOjS9_
- __ZNSt3__110__function6__funcIZN17LegacyHapticSynth19handleRunModeChangeEjE3$_1NS_9allocatorIS3_EEFivEE18destroy_deallocateEv
- __ZNSt3__110__function6__funcIZN17LegacyHapticSynth19handleRunModeChangeEjE3$_1NS_9allocatorIS3_EEFivEE7destroyEv
- __ZNSt3__110__function6__funcIZN17LegacyHapticSynth19handleRunModeChangeEjE3$_1NS_9allocatorIS3_EEFivEED0Ev
- __ZNSt3__110__function6__funcIZN17LegacyHapticSynth19handleRunModeChangeEjE3$_1NS_9allocatorIS3_EEFivEED1Ev
- __ZNSt3__110__function6__funcIZN17LegacyHapticSynth19handleRunModeChangeEjE3$_1NS_9allocatorIS3_EEFivEEclEv
- __ZNSt3__110__function6__funcIZN18BorealisServerImpl27enableVoiceTriggerListeningEbbU13block_pointerFvP7NSErrorEEUljRKN15CAListenerProxy15HALNotificationEE_NS_9allocatorISB_EEFbjSA_EE18destroy_deallocateEv
- __ZNSt3__110__function6__funcIZN18BorealisServerImpl27enableVoiceTriggerListeningEbbU13block_pointerFvP7NSErrorEEUljRKN15CAListenerProxy15HALNotificationEE_NS_9allocatorISB_EEFbjSA_EE7destroyEv
- __ZNSt3__110__function6__funcIZN18BorealisServerImpl27enableVoiceTriggerListeningEbbU13block_pointerFvP7NSErrorEEUljRKN15CAListenerProxy15HALNotificationEE_NS_9allocatorISB_EEFbjSA_EED0Ev
- __ZNSt3__110__function6__funcIZN18BorealisServerImpl27enableVoiceTriggerListeningEbbU13block_pointerFvP7NSErrorEEUljRKN15CAListenerProxy15HALNotificationEE_NS_9allocatorISB_EEFbjSA_EED1Ev
- __ZNSt3__110__function6__funcIZN18BorealisServerImpl27enableVoiceTriggerListeningEbbU13block_pointerFvP7NSErrorEEUljRKN15CAListenerProxy15HALNotificationEE_NS_9allocatorISB_EEFbjSA_EEclEOjSA_
- __ZNSt3__110__function6__funcIZN18BorealisServerImpl31updateVoiceTriggerConfigurationEPK14__CFDictionaryU13block_pointerFvP7NSErrorEEUljRKN15CAListenerProxy15HALNotificationEE_NS_9allocatorISE_EEFbjSD_EE18destroy_deallocateEv
- __ZNSt3__110__function6__funcIZN18BorealisServerImpl31updateVoiceTriggerConfigurationEPK14__CFDictionaryU13block_pointerFvP7NSErrorEEUljRKN15CAListenerProxy15HALNotificationEE_NS_9allocatorISE_EEFbjSD_EE7destroyEv
- __ZNSt3__110__function6__funcIZN18BorealisServerImpl31updateVoiceTriggerConfigurationEPK14__CFDictionaryU13block_pointerFvP7NSErrorEEUljRKN15CAListenerProxy15HALNotificationEE_NS_9allocatorISE_EEFbjSD_EED0Ev
- __ZNSt3__110__function6__funcIZN18BorealisServerImpl31updateVoiceTriggerConfigurationEPK14__CFDictionaryU13block_pointerFvP7NSErrorEEUljRKN15CAListenerProxy15HALNotificationEE_NS_9allocatorISE_EEFbjSD_EED1Ev
- __ZNSt3__110__function6__funcIZN18BorealisServerImpl31updateVoiceTriggerConfigurationEPK14__CFDictionaryU13block_pointerFvP7NSErrorEEUljRKN15CAListenerProxy15HALNotificationEE_NS_9allocatorISE_EEFbjSD_EEclEOjSD_
- __ZNSt3__110__function6__funcIZN18BorealisServerImpl40registerStateChangedNotificationHandlersEbEUljRKN15CAListenerProxy15HALNotificationEE_NS_9allocatorIS7_EEFbjS6_EE18destroy_deallocateEv
- __ZNSt3__110__function6__funcIZN18BorealisServerImpl40registerStateChangedNotificationHandlersEbEUljRKN15CAListenerProxy15HALNotificationEE_NS_9allocatorIS7_EEFbjS6_EE7destroyEv
- __ZNSt3__110__function6__funcIZN18BorealisServerImpl40registerStateChangedNotificationHandlersEbEUljRKN15CAListenerProxy15HALNotificationEE_NS_9allocatorIS7_EEFbjS6_EED0Ev
- __ZNSt3__110__function6__funcIZN18BorealisServerImpl40registerStateChangedNotificationHandlersEbEUljRKN15CAListenerProxy15HALNotificationEE_NS_9allocatorIS7_EEFbjS6_EED1Ev
- __ZNSt3__110__function6__funcIZN18BorealisServerImpl40registerStateChangedNotificationHandlersEbEUljRKN15CAListenerProxy15HALNotificationEE_NS_9allocatorIS7_EEFbjS6_EEclEOjS6_
- __ZNSt3__110__function6__funcIZN18BorealisServerImpl42registerAOPVoiceTriggerNotificationHandlerEjbEUljRKN15CAListenerProxy15HALNotificationEE_NS_9allocatorIS7_EEFbjS6_EE18destroy_deallocateEv
- __ZNSt3__110__function6__funcIZN18BorealisServerImpl42registerAOPVoiceTriggerNotificationHandlerEjbEUljRKN15CAListenerProxy15HALNotificationEE_NS_9allocatorIS7_EEFbjS6_EE7destroyEv
- __ZNSt3__110__function6__funcIZN18BorealisServerImpl42registerAOPVoiceTriggerNotificationHandlerEjbEUljRKN15CAListenerProxy15HALNotificationEE_NS_9allocatorIS7_EEFbjS6_EED0Ev
- __ZNSt3__110__function6__funcIZN18BorealisServerImpl42registerAOPVoiceTriggerNotificationHandlerEjbEUljRKN15CAListenerProxy15HALNotificationEE_NS_9allocatorIS7_EEFbjS6_EED1Ev
- __ZNSt3__110__function6__funcIZN18BorealisServerImpl42registerAOPVoiceTriggerNotificationHandlerEjbEUljRKN15CAListenerProxy15HALNotificationEE_NS_9allocatorIS7_EEFbjS6_EEclEOjS6_
- __ZNSt3__110__function6__funcIZN18BorealisServerImpl43registerAOPEnableChangedNotificationHandlerEbEUljRKN15CAListenerProxy15HALNotificationEE_NS_9allocatorIS7_EEFbjS6_EE18destroy_deallocateEv
- __ZNSt3__110__function6__funcIZN18BorealisServerImpl43registerAOPEnableChangedNotificationHandlerEbEUljRKN15CAListenerProxy15HALNotificationEE_NS_9allocatorIS7_EEFbjS6_EE7destroyEv
- __ZNSt3__110__function6__funcIZN18BorealisServerImpl43registerAOPEnableChangedNotificationHandlerEbEUljRKN15CAListenerProxy15HALNotificationEE_NS_9allocatorIS7_EEFbjS6_EED0Ev
- __ZNSt3__110__function6__funcIZN18BorealisServerImpl43registerAOPEnableChangedNotificationHandlerEbEUljRKN15CAListenerProxy15HALNotificationEE_NS_9allocatorIS7_EEFbjS6_EED1Ev
- __ZNSt3__110__function6__funcIZN18BorealisServerImpl43registerAOPEnableChangedNotificationHandlerEbEUljRKN15CAListenerProxy15HALNotificationEE_NS_9allocatorIS7_EEFbjS6_EEclEOjS6_
- __ZNSt3__110__function6__funcIZN20DSP_Routing_Borealis3AOP35registerAOPVoiceTriggerNotificationEbE3$_0NS_9allocatorIS4_EEFbjRKN15CAListenerProxy15HALNotificationEEE18destroy_deallocateEv
- __ZNSt3__110__function6__funcIZN20DSP_Routing_Borealis3AOP35registerAOPVoiceTriggerNotificationEbE3$_0NS_9allocatorIS4_EEFbjRKN15CAListenerProxy15HALNotificationEEE7destroyEv
- __ZNSt3__110__function6__funcIZN20DSP_Routing_Borealis3AOP35registerAOPVoiceTriggerNotificationEbE3$_0NS_9allocatorIS4_EEFbjRKN15CAListenerProxy15HALNotificationEEED0Ev
- __ZNSt3__110__function6__funcIZN20DSP_Routing_Borealis3AOP35registerAOPVoiceTriggerNotificationEbE3$_0NS_9allocatorIS4_EEFbjRKN15CAListenerProxy15HALNotificationEEED1Ev
- __ZNSt3__110__function6__funcIZN20DSP_Routing_Borealis3AOP35registerAOPVoiceTriggerNotificationEbE3$_0NS_9allocatorIS4_EEFbjRKN15CAListenerProxy15HALNotificationEEEclEOjSA_
- __ZNSt3__110__function6__funcIZN20DSP_Routing_Borealis3AOP45updateFirstPassModelOnAOPAndWaitForCompletionEvE3$_0NS_9allocatorIS4_EEFbjRKN15CAListenerProxy15HALNotificationEEE18destroy_deallocateEv
- __ZNSt3__110__function6__funcIZN20DSP_Routing_Borealis3AOP45updateFirstPassModelOnAOPAndWaitForCompletionEvE3$_0NS_9allocatorIS4_EEFbjRKN15CAListenerProxy15HALNotificationEEE7destroyEv
- __ZNSt3__110__function6__funcIZN20DSP_Routing_Borealis3AOP45updateFirstPassModelOnAOPAndWaitForCompletionEvE3$_0NS_9allocatorIS4_EEFbjRKN15CAListenerProxy15HALNotificationEEED0Ev
- __ZNSt3__110__function6__funcIZN20DSP_Routing_Borealis3AOP45updateFirstPassModelOnAOPAndWaitForCompletionEvE3$_0NS_9allocatorIS4_EEFbjRKN15CAListenerProxy15HALNotificationEEED1Ev
- __ZNSt3__110__function6__funcIZN20DSP_Routing_Borealis3AOP45updateFirstPassModelOnAOPAndWaitForCompletionEvE3$_0NS_9allocatorIS4_EEFbjRKN15CAListenerProxy15HALNotificationEEEclEOjSA_
- __ZNSt3__110__function6__funcIZN22MultiOutputHapticSynth12startRunningEbbjNS_8functionIFivEEEjE3$_1NS_9allocatorIS6_EES4_E18destroy_deallocateEv
- __ZNSt3__110__function6__funcIZN22MultiOutputHapticSynth12startRunningEbbjNS_8functionIFivEEEjE3$_1NS_9allocatorIS6_EES4_E7destroyEv
- __ZNSt3__110__function6__funcIZN22MultiOutputHapticSynth12startRunningEbbjNS_8functionIFivEEEjE3$_1NS_9allocatorIS6_EES4_ED0Ev
- __ZNSt3__110__function6__funcIZN22MultiOutputHapticSynth12startRunningEbbjNS_8functionIFivEEEjE3$_1NS_9allocatorIS6_EES4_ED1Ev
- __ZNSt3__110__function6__funcIZN22MultiOutputHapticSynth12startRunningEbbjNS_8functionIFivEEEjE3$_1NS_9allocatorIS6_EES4_EclEv
- __ZNSt3__110__function6__funcIZN22MultiOutputHapticSynth19handleRunModeChangeEjE3$_3NS_9allocatorIS3_EEFivEE18destroy_deallocateEv
- __ZNSt3__110__function6__funcIZN22MultiOutputHapticSynth19handleRunModeChangeEjE3$_3NS_9allocatorIS3_EEFivEE7destroyEv
- __ZNSt3__110__function6__funcIZN22MultiOutputHapticSynth19handleRunModeChangeEjE3$_3NS_9allocatorIS3_EEFivEED0Ev
- __ZNSt3__110__function6__funcIZN22MultiOutputHapticSynth19handleRunModeChangeEjE3$_3NS_9allocatorIS3_EEFivEED1Ev
- __ZNSt3__110__function6__funcIZN22MultiOutputHapticSynth19handleRunModeChangeEjE3$_3NS_9allocatorIS3_EEFivEEclEv
- __ZNSt3__110__function6__funcIZN2AQ3API7ManagerC1EbRNS3_11CaptureBaseEN5caulk19lifetime_erased_ptrI23AudioQueueXPC_InterfaceEEE3$_0NS_9allocatorISB_EEFiN10applesauce3xpc6objectEEE18destroy_deallocateEv
- __ZNSt3__110__function6__funcIZN2AQ3API7ManagerC1EbRNS3_11CaptureBaseEN5caulk19lifetime_erased_ptrI23AudioQueueXPC_InterfaceEEE3$_0NS_9allocatorISB_EEFiN10applesauce3xpc6objectEEE7destroyEv
- __ZNSt3__110__function6__funcIZN2AQ3API7ManagerC1EbRNS3_11CaptureBaseEN5caulk19lifetime_erased_ptrI23AudioQueueXPC_InterfaceEEE3$_0NS_9allocatorISB_EEFiN10applesauce3xpc6objectEEED0Ev
- __ZNSt3__110__function6__funcIZN2AQ3API7ManagerC1EbRNS3_11CaptureBaseEN5caulk19lifetime_erased_ptrI23AudioQueueXPC_InterfaceEEE3$_0NS_9allocatorISB_EEFiN10applesauce3xpc6objectEEED1Ev
- __ZNSt3__110__function6__funcIZN2AQ3API7ManagerC1EbRNS3_11CaptureBaseEN5caulk19lifetime_erased_ptrI23AudioQueueXPC_InterfaceEEE3$_0NS_9allocatorISB_EEFiN10applesauce3xpc6objectEEEclEOSG_
- __ZNSt3__110__function6__funcIZN2AQ3API7ManagerC1EbRNS3_11CaptureBaseEN5caulk19lifetime_erased_ptrI23AudioQueueXPC_InterfaceEEE3$_1NS_9allocatorISB_EEFvRN4swix12ipc_endpointERKN10applesauce3xpc6objectEEE18destroy_deallocateEv
- __ZNSt3__110__function6__funcIZN2AQ3API7ManagerC1EbRNS3_11CaptureBaseEN5caulk19lifetime_erased_ptrI23AudioQueueXPC_InterfaceEEE3$_1NS_9allocatorISB_EEFvRN4swix12ipc_endpointERKN10applesauce3xpc6objectEEE7destroyEv
- __ZNSt3__110__function6__funcIZN2AQ3API7ManagerC1EbRNS3_11CaptureBaseEN5caulk19lifetime_erased_ptrI23AudioQueueXPC_InterfaceEEE3$_1NS_9allocatorISB_EEFvRN4swix12ipc_endpointERKN10applesauce3xpc6objectEEED0Ev
- __ZNSt3__110__function6__funcIZN2AQ3API7ManagerC1EbRNS3_11CaptureBaseEN5caulk19lifetime_erased_ptrI23AudioQueueXPC_InterfaceEEE3$_1NS_9allocatorISB_EEFvRN4swix12ipc_endpointERKN10applesauce3xpc6objectEEED1Ev
- __ZNSt3__110__function6__funcIZN2AQ3API7ManagerC1EbRNS3_11CaptureBaseEN5caulk19lifetime_erased_ptrI23AudioQueueXPC_InterfaceEEE3$_1NS_9allocatorISB_EEFvRN4swix12ipc_endpointERKN10applesauce3xpc6objectEEEclESG_SL_
- __ZNSt3__110__function6__funcIZZN13MESubmixGraph19attach1MixerChannelEP14MEMixerChannelENK3$_0clI9TapSubmixEEDaRT_EUlvE_NS_9allocatorISB_EEFvvEE18destroy_deallocateEv
- __ZNSt3__110__function6__funcIZZN13MESubmixGraph19attach1MixerChannelEP14MEMixerChannelENK3$_0clI9TapSubmixEEDaRT_EUlvE_NS_9allocatorISB_EEFvvEE7destroyEv
- __ZNSt3__110__function6__funcIZZN13MESubmixGraph19attach1MixerChannelEP14MEMixerChannelENK3$_0clI9TapSubmixEEDaRT_EUlvE_NS_9allocatorISB_EEFvvEED0Ev
- __ZNSt3__110__function6__funcIZZN13MESubmixGraph19attach1MixerChannelEP14MEMixerChannelENK3$_0clI9TapSubmixEEDaRT_EUlvE_NS_9allocatorISB_EEFvvEED1Ev
- __ZNSt3__110__function6__funcIZZN13MESubmixGraph19attach1MixerChannelEP14MEMixerChannelENK3$_0clI9TapSubmixEEDaRT_EUlvE_NS_9allocatorISB_EEFvvEEclEv
- __ZNSt3__110__function6__funcIZZN14RemoteIOClient20IONode_FormatChangedEjEUb_E3$_0NS_9allocatorIS3_EEFvvEE18destroy_deallocateEv
- __ZNSt3__110__function6__funcIZZN14RemoteIOClient20IONode_FormatChangedEjEUb_E3$_0NS_9allocatorIS3_EEFvvEE7destroyEv
- __ZNSt3__110__function6__funcIZZN14RemoteIOClient20IONode_FormatChangedEjEUb_E3$_0NS_9allocatorIS3_EEFvvEED0Ev
- __ZNSt3__110__function6__funcIZZN14RemoteIOClient20IONode_FormatChangedEjEUb_E3$_0NS_9allocatorIS3_EEFvvEED1Ev
- __ZNSt3__110__function6__funcIZZN14RemoteIOClient20IONode_FormatChangedEjEUb_E3$_0NS_9allocatorIS3_EEFvvEEclEv
- __ZNSt3__110__function6__funcIZZN22MultiOutputHapticSynth11stopRunningEbbjENK3$_3clERNS_10unique_ptrI11SynthOutputNS_14default_deleteIS5_EEEEEUlvE_NS_9allocatorISA_EEFvvEE18destroy_deallocateEv
- __ZNSt3__110__function6__funcIZZN22MultiOutputHapticSynth11stopRunningEbbjENK3$_3clERNS_10unique_ptrI11SynthOutputNS_14default_deleteIS5_EEEEEUlvE_NS_9allocatorISA_EEFvvEE7destroyEv
- __ZNSt3__110__function6__funcIZZN22MultiOutputHapticSynth11stopRunningEbbjENK3$_3clERNS_10unique_ptrI11SynthOutputNS_14default_deleteIS5_EEEEEUlvE_NS_9allocatorISA_EEFvvEED0Ev
- __ZNSt3__110__function6__funcIZZN22MultiOutputHapticSynth11stopRunningEbbjENK3$_3clERNS_10unique_ptrI11SynthOutputNS_14default_deleteIS5_EEEEEUlvE_NS_9allocatorISA_EEFvvEED1Ev
- __ZNSt3__110__function6__funcIZZN22MultiOutputHapticSynth11stopRunningEbbjENK3$_3clERNS_10unique_ptrI11SynthOutputNS_14default_deleteIS5_EEEEEUlvE_NS_9allocatorISA_EEFvvEEclEv
- __ZNSt3__110__list_impI15SystemSoundInfoNS_9allocatorIS1_EEE13__create_nodeB8ne190102IJRKS1_EEEPNS_11__list_nodeIS1_PvEEPNS_16__list_node_baseIS1_S9_EESE_DpOT_
- __ZNSt3__110__list_impIN13ServerManager12SynthCommandEN5caulk12rt_allocatorIS2_EEE13__create_nodeB8ne190102IJRKS2_EEEPNS_11__list_nodeIS2_PvEEPNS_16__list_node_baseIS2_SB_EESG_DpOT_
- __ZNSt3__110__list_impIN5boost13intrusive_ptrIKNS1_10statechart10event_baseEEENS_9allocatorIS6_EEE13__delete_nodeB8ne190102EPNS_11__list_nodeIS6_PvEE
- __ZNSt3__110__list_impIN5boost13intrusive_ptrIKNS1_10statechart10event_baseEEENS_9allocatorIS6_EEE5clearEv
- __ZNSt3__110shared_ptrI11AQTapIONodeEC2B8ne190102IS1_PFvP8AQIONodeELi0EEEPT_T0_
- __ZNSt3__110shared_ptrI11ClientEntryEC2B8ne190102IS1_Li0EEERKNS_8weak_ptrIT_EE
- __ZNSt3__110shared_ptrI12SequenceImplEC2B8ne190102IS1_Li0EEERKNS_8weak_ptrIT_EE
- __ZNSt3__110shared_ptrI14HapticSequenceEC2B8ne190102IS1_Li0EEEPT_
- __ZNSt3__110shared_ptrI18AQMixEngine_SingleEC2B8ne190102IS1_PFvP8AQIONodeELi0EEEPT_T0_
- __ZNSt3__110shared_ptrI19AQMixEngine_OfflineEC2B8ne190102IS1_PFvP8AQIONodeELi0EEEPT_T0_
- __ZNSt3__110shared_ptrI21ThreadSafeHeadTrackerE18__enable_weak_thisB8ne190102IS1_S1_Li0EEEvPKNS_23enable_shared_from_thisIT_EEPT0_
- __ZNSt3__110shared_ptrIN18PowerUsageWatchdog4ImplEEC2B8ne190102IS2_Li0EEERKNS_8weak_ptrIT_EE
- __ZNSt3__110shared_ptrIN2AQ3API5QueueEEC2B8ne190102IS3_Li0EEERKNS_8weak_ptrIT_EE
- __ZNSt3__110shared_ptrIN2AQ3API9SubmixTapEEC2B8ne190102IS3_Li0EEERKNS_8weak_ptrIT_EE
- __ZNSt3__110shared_ptrIN2AT9IOBinding4ImplEE18__enable_weak_thisB8ne190102IS3_S3_Li0EEEvPKNS_23enable_shared_from_thisIT_EEPT0_
- __ZNSt3__110unique_ptrI10AQMEIO_DSPNS_14default_deleteIS1_EEE5resetB8ne190102EPS1_
- __ZNSt3__110unique_ptrI11AQAC3IONodeNS_14default_deleteIS1_EEE5resetB8ne190102EPS1_
- __ZNSt3__110unique_ptrI11AQTapIONodeNS_14default_deleteIS1_EEE5resetB8ne190102EPS1_
- __ZNSt3__110unique_ptrI11SynthOutputNS_14default_deleteIS1_EEE5resetB8ne190102EPS1_
- __ZNSt3__110unique_ptrI12CASerializerNS_14default_deleteIS1_EEE5resetB8ne190102EPS1_
- __ZNSt3__110unique_ptrI13MESubmixGraphNS_14default_deleteIS1_EEE5resetB8ne190102EPS1_
- __ZNSt3__110unique_ptrI14AQClientBufferN2AQ3API13BufferDeleterEE5resetB8ne190102EPS1_
- __ZNSt3__110unique_ptrI14CADeserializerNS_14default_deleteIS1_EEE5resetB8ne190102EPS1_
- __ZNSt3__110unique_ptrI14InputConverterNS_14default_deleteIS1_EEE5resetB8ne190102EPS1_
- __ZNSt3__110unique_ptrI14MixTapToUplinkNS_14default_deleteIS1_EEE5resetB8ne190102EPS1_
- __ZNSt3__110unique_ptrI14__CFReadStreamN10applesauce4raii2v16detail23opaque_deletion_functorIPS1_XadL_Z9CFReleaseEEEEE5resetB8ne190102ES7_
- __ZNSt3__110unique_ptrI15AQMixEngine_VADNS_14default_deleteIS1_EEE5resetB8ne190102EPS1_
- __ZNSt3__110unique_ptrI17AudioEventManagerNS_14default_deleteIS1_EEE5resetB8ne190102EPS1_
- __ZNSt3__110unique_ptrI17AudioTapInterfaceNS_14default_deleteIS1_EEE5resetB8ne190102EPS1_
- __ZNSt3__110unique_ptrI17AudioTapSpecifierNS_14default_deleteIS1_EEE5resetB8ne190102EPS1_
- __ZNSt3__110unique_ptrI17ZenAQIONodeClientNS_14default_deleteIS1_EEE5resetB8ne190102EPS1_
- __ZNSt3__110unique_ptrI18AQHapticOutputNodeNS_14default_deleteIS1_EEE5resetB8ne190102EPS1_
- __ZNSt3__110unique_ptrI18VADPropertyManagerNS_14default_deleteIS1_EEE5resetB8ne190102EPS1_
- __ZNSt3__110unique_ptrI19AQMixEngine_OfflineNS_14default_deleteIS1_EEE5resetB8ne190102EPS1_
- __ZNSt3__110unique_ptrI20AudioImpulseInjectorNS_14default_deleteIS1_EEE5resetB8ne190102EPS1_
- __ZNSt3__110unique_ptrI22WorkThreadSynchronizerNS_14default_deleteIS1_EEE5resetB8ne190102EPS1_
- __ZNSt3__110unique_ptrI26SSClientCompletionProcInfoNS_14default_deleteIS1_EEE5resetB8ne190102EPS1_
- __ZNSt3__110unique_ptrI27SpatialTrackingServiceProxyNS_14default_deleteIS1_EEE5resetB8ne190102EPS1_
- __ZNSt3__110unique_ptrI30ProductTuningAdjustmentManagerNS_14default_deleteIS1_EEE5resetB8ne190102EPS1_
- __ZNSt3__110unique_ptrI7__sFILENS_8functionIFiPS1_EEEE5resetB8ne190102ES3_
- __ZNSt3__110unique_ptrI8AQBufferNS_14default_deleteIS1_EEE5resetB8ne190102EPS1_
- __ZNSt3__110unique_ptrI8XPromiseNS_14default_deleteIS1_EEE5resetB8ne190102EPS1_
- __ZNSt3__110unique_ptrIKvN10applesauce4raii2v16detail23opaque_deletion_functorIPS1_XadL_Z9CFReleaseEEEEE5resetB8ne190102ES7_
- __ZNSt3__110unique_ptrIN11AQMEIO_Base12IOSuspensionENS_14default_deleteIS2_EEE5resetB8ne190102EPS2_
- __ZNSt3__110unique_ptrIN14SpeechDetector18SpeechDetectorImplENS_14default_deleteIS2_EEE5resetB8ne190102EPS2_
- __ZNSt3__110unique_ptrIN17AudioTapInterface4ImplENS_14default_deleteIS2_EEE5resetB8ne190102EPS2_
- __ZNSt3__110unique_ptrIN18ATSecureVADManager4ImplENS_14default_deleteIS2_EEE5resetB8ne190102EPS2_
- __ZNSt3__110unique_ptrIN18PowerUsageWatchdog4ImplENS_14default_deleteIS2_EEE5resetB8ne190102EPS2_
- __ZNSt3__110unique_ptrIN2AQ6Server12RemoteClientENS_14default_deleteIS3_EEE5resetB8ne190102EPS3_
- __ZNSt3__110unique_ptrIN2AT10RingBufferENS_14default_deleteIS2_EEE5resetB8ne190102EPS2_
- __ZNSt3__110unique_ptrIN2AT14AudioTapClient4ImplENS_14default_deleteIS3_EEE5resetB8ne190102EPS3_
- __ZNSt3__110unique_ptrIN5Phase13ServerManagerENS_14default_deleteIS2_EEE5resetB8ne190102EPS2_
- __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEN20AudioImpulseInjector4Impl20NotificationListener17NotificationStateEEEPvEENS_22__hash_node_destructorINS6_ISF_EEEEE5resetB8ne190102EPSF_
- __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIjNS0_I26SSClientCompletionProcInfoNS_14default_deleteIS3_EEEEEEPvEENS_22__hash_node_destructorINS_9allocatorIS9_EEEEE5resetB8ne190102EPS9_
- __ZNSt3__110unique_ptrINS_11__tree_nodeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE8LocalityEEPvEENS_22__tree_node_destructorINS6_ISC_EEEEE5resetB8ne190102EPSC_
- __ZNSt3__110unique_ptrINS_11__tree_nodeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEN10applesauce2CF7TypeRefEEEPvEENS_22__tree_node_destructorINS6_ISE_EEEEE5resetB8ne190102EPSE_
- __ZNSt3__110unique_ptrINS_11__tree_nodeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI29NewNotificationCenterObserverEEEEPvEENS_22__tree_node_destructorINS6_ISE_EEEEE5resetB8ne190102EPSE_
- __ZNSt3__110unique_ptrINS_11__tree_nodeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI29OldNotificationCenterObserverEEEEPvEENS_22__tree_node_destructorINS6_ISE_EEEEE5resetB8ne190102EPSE_
- __ZNSt3__110unique_ptrINS_11__tree_nodeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEES8_EEPvEENS_22__tree_node_destructorINS6_ISB_EEEEE5resetB8ne190102EPSB_
- __ZNSt3__110unique_ptrINS_5tupleIJN5caulk6thread10attributesEZN2AQ3API20ProcessingTapManager7RTStateC1ERKN10applesauce3xpc6objectERNS6_23ProcessingTapAttributesERiE3$_0NS1_IJEEEEEENS_14default_deleteISJ_EEED1B8ne190102Ev
- __ZNSt3__110unique_ptrIZN20CAOrientationManager14UpdateHandlersENS1_11HandlerTypeEE3$_0NS_14default_deleteIS3_EEED1B8ne190102Ev
- __ZNSt3__110unique_ptrIZN20CAOrientationManager23AddUIOrientationHandlerEPK10__CFStringU13block_pointerFv13CAOrientationEE3$_0NS_14default_deleteIS8_EEED1B8ne190102Ev
- __ZNSt3__110unique_ptrIZN20CAOrientationManager27AddDeviceOrientationHandlerEPK10__CFStringU13block_pointerFv13CAOrientationEE3$_0NS_14default_deleteIS8_EEED1B8ne190102Ev
- __ZNSt3__111make_uniqueB8ne190102I17AudioTapInterfaceJ17AudioTapSpecifierEEENS_11__unique_ifIT_E15__unique_singleEDpOT0_
- __ZNSt3__111make_uniqueB8ne190102I17AudioTapInterfaceJPK8__CFDataEEENS_11__unique_ifIT_E15__unique_singleEDpOT0_
- __ZNSt3__111make_uniqueB8ne190102IN2CA12AudioBuffersEJRNS1_17StreamDescriptionERjEEENS_11__unique_ifIT_E15__unique_singleEDpOT0_
- __ZNSt3__111shared_lockIN5caulk10concurrent16shared_spin_lockEED2B8ne190102Ev
- __ZNSt3__111shared_lockINS_12shared_mutexEED2B8ne190102Ev
- __ZNSt3__111this_thread9sleep_forB8ne190102IxNS_5ratioILl1ELl1000EEEEEvRKNS_6chrono8durationIT_T0_EE
- __ZNSt3__111unique_lockIN5caulk10concurrent16shared_spin_lockEED2B8ne190102Ev
- __ZNSt3__111unique_lockIN5caulk22pooled_semaphore_mutexEED2B8ne190102Ev
- __ZNSt3__111unique_lockIN5caulk4mach21unfair_recursive_lockEE4lockEv
- __ZNSt3__111unique_lockIN5caulk4mach21unfair_recursive_lockEE6unlockEv
- __ZNSt3__111unique_lockINS_12shared_mutexEED2B8ne190102Ev
- __ZNSt3__112__destroy_atB8ne190102I11AQMESessionLi0EEEvPT_
- __ZNSt3__112__destroy_atB8ne190102I15MEVADIdentifierLi0EEEvPT_
- __ZNSt3__112__destroy_atB8ne190102I9TapSourceLi0EEEvPT_
- __ZNSt3__112__destroy_atB8ne190102IN10applesauce2CF11TypeRefPairELi0EEEvPT_
- __ZNSt3__112__destroy_atB8ne190102IN10applesauce2CF7TypeRefELi0EEEvPT_
- __ZNSt3__112__destroy_atB8ne190102IN10applesauce2CF9NumberRefELi0EEEvPT_
- __ZNSt3__112__destroy_atB8ne190102IN21IPCAUSharedMemoryBase7ElementELi0EEEvPT_
- __ZNSt3__112__destroy_atB8ne190102IN2AQ6Server12RemoteClient18ProcessingTapStateELi0EEEvPT_
- __ZNSt3__112__destroy_atB8ne190102IN2AU8Property10Attributes7details15AUPresetWrapperELi0EEEvPT_
- __ZNSt3__112__destroy_atB8ne190102IN8audioipc18SharedAudioBuffers7ElementELi0EEEvPT_
- __ZNSt3__112__destroy_atB8ne190102INS_4pairIKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE8LocalityEELi0EEEvPT_
- __ZNSt3__112__destroy_atB8ne190102INS_4pairIKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEN10applesauce2CF7TypeRefEEELi0EEEvPT_
- __ZNSt3__112__destroy_atB8ne190102INS_4pairIKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEN20AudioImpulseInjector4Impl20NotificationListener17NotificationStateEEELi0EEEvPT_
- __ZNSt3__112__destroy_atB8ne190102INS_4pairIKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI29NewNotificationCenterObserverEEEELi0EEEvPT_
- __ZNSt3__112__destroy_atB8ne190102INS_4pairIKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI29OldNotificationCenterObserverEEEELi0EEEvPT_
- __ZNSt3__112__destroy_atB8ne190102INS_4pairIKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEES7_EELi0EEEvPT_
- __ZNSt3__112__destroy_atB8ne190102INS_4pairIN2OS2CF6StringEN10applesauce8dispatch2v15blockIFv13CAOrientationEEEEELi0EEEvPT_
- __ZNSt3__112__destroy_atB8ne190102INS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEES7_EELi0EEEvPT_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIjNS_10unique_ptrI26SSClientCompletionProcInfoNS_14default_deleteIS3_EEEEEENS_22__unordered_map_hasherIjS7_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS7_SC_SA_Lb1EEENS_9allocatorIS7_EEED2Ev
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIjNS_10unique_ptrI27SSClientCompletionBlockInfoNS_14default_deleteIS3_EEEEEENS_22__unordered_map_hasherIjS7_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS7_SC_SA_Lb1EEENS_9allocatorIS7_EEE17__deallocate_nodeEPNS_16__hash_node_baseIPNS_11__hash_nodeIS7_PvEEEE
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIjNS_10unique_ptrI27SSClientCompletionBlockInfoNS_14default_deleteIS3_EEEEEENS_22__unordered_map_hasherIjS7_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS7_SC_SA_Lb1EEENS_9allocatorIS7_EEED2Ev
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIjiEENS_22__unordered_map_hasherIjS2_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS2_S7_S5_Lb1EEENS_9allocatorIS2_EEE13__move_assignERSD_NS_17integral_constantIbLb1EEE
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIjiEENS_22__unordered_map_hasherIjS2_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS2_S7_S5_Lb1EEENS_9allocatorIS2_EEE27__node_insert_multi_performEPNS_11__hash_nodeIS2_PvEEPNS_16__hash_node_baseISH_EE
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIjiEENS_22__unordered_map_hasherIjS2_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS2_S7_S5_Lb1EEENS_9allocatorIS2_EEE27__node_insert_multi_prepareEmRS2_
- __ZNSt3__112__tuple_leafILm0EN10applesauce3xpc6objectELb0EEC2B8ne190102ERKS4_
- __ZNSt3__112__tuple_leafILm0EN4swix4dataELb0EEC2B8ne190102ERKS3_
- __ZNSt3__112__tuple_leafILm1EN4swix6stringELb0EEC2B8ne190102ERKS3_
- __ZNSt3__112__tuple_leafILm3EN10applesauce3xpc6objectELb0EEC2B8ne190102ERKS4_
- __ZNSt3__112__tuple_leafILm4EN10applesauce3xpc6objectELb0EEC2B8ne190102ERKS4_
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne190102ENS_24__uninitialized_size_tagEmRKS4_
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne190102EPKcm
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne190102Emc
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne190102ILi0EEEPKc
- __ZNSt3__112construct_atB8ne190102I11AQMESessionJRKS1_EPS1_EEPT_S6_DpOT0_
- __ZNSt3__112construct_atB8ne190102I15MEVADIdentifierJR14MEDeviceTypeIDRjRN10applesauce2CF9StringRefEEPS1_EEPT_SB_DpOT0_
- __ZNSt3__112construct_atB8ne190102I15MEVADIdentifierJRKS1_EPS1_EEPT_S6_DpOT0_
- __ZNSt3__112construct_atB8ne190102I15MEVADIdentifierJRS1_EPS1_EEPT_S5_DpOT0_
- __ZNSt3__112construct_atB8ne190102I9TapSourceJS1_EPS1_EEPT_S4_DpOT0_
- __ZNSt3__112construct_atB8ne190102IN10applesauce2CF7TypeRefEJdEPS3_EEPT_S6_DpOT0_
- __ZNSt3__112construct_atB8ne190102IN10applesauce2CF9NumberRefEJjEPS3_EEPT_S6_DpOT0_
- __ZNSt3__112construct_atB8ne190102IN10applesauce2CF9StringRefEJRKS3_EPS3_EEPT_S8_DpOT0_
- __ZNSt3__112construct_atB8ne190102IN4swix17connection_configEJS2_EPS2_EEPT_S5_DpOT0_
- __ZNSt3__113__fill_n_boolB8ne190102ILb0ENS_8__bitsetILm1ELm13EEEEEvNS_14__bit_iteratorIT0_Lb0EXLi0EEEENS4_9size_typeE
- __ZNSt3__113__tree_removeB8ne190102IPNS_16__tree_node_baseIPvEEEEvT_S5_
- __ZNSt3__113unordered_mapIjiNS_4hashIjEENS_8equal_toIjEENS_9allocatorINS_4pairIKjiEEEEEC2ERKSA_
- __ZNSt3__114__split_bufferI10ChaseEventRNS_9allocatorIS1_EEED2Ev
- __ZNSt3__114__split_bufferINS_10unique_ptrIN15AQMixEngine_VAD10MEVADeviceENS_14default_deleteIS3_EEEERNS_9allocatorIS6_EEED2Ev
- __ZNSt3__115allocate_sharedB8ne190102I14HapticSequenceNS_9allocatorIS1_EEJNS_10shared_ptrI11MuteManagerEEELi0EEENS4_IT_EERKT0_DpOT1_
- __ZNSt3__115allocate_sharedB8ne190102I8TFileBSDNS_9allocatorIS1_EEJRPK7__CFURLELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
- __ZNSt3__115allocate_sharedB8ne190102IN2AQ3API9SubmixTapENS_9allocatorIS3_EEJRNS2_7ManagerERjELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
- __ZNSt3__115allocate_sharedB8ne190102IN2AT9IOBinding4ImplENS_9allocatorIS3_EEJN10applesauce2CF9StringRefEELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
- __ZNSt3__115allocate_sharedB8ne190102IN2AT9IOBinding4ImplENS_9allocatorIS3_EEJR24ATIsolatedAudioUseCaseIDELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
- __ZNSt3__115allocate_sharedB8ne190102IN5caulk7details19lifetime_guard_baseIN2AQ6Server12RemoteClientEE13control_blockENS_9allocatorIS8_EEJRS7_ELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
- __ZNSt3__115basic_streambufIcNS_11char_traitsIcEEEC2Ev
- __ZNSt3__115basic_streambufIcNS_11char_traitsIcEEED2Ev
- __ZNSt3__116__deque_iteratorINS_4pairIN5boost8functionIFNS2_3msm4back11HandledEnumEvEEEbEEPS9_RS9_PSA_lLl102EEpLB8ne190102El
- __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm0EEE10__dispatchB8ne190102IOZNS0_6__ctorINS0_8__traitsIJPFvPvP16OpaqueAudioQueueP16AudioQueueBufferEPFvS8_SA_SC_PK14AudioTimeStampjPK28AudioStreamPacketDescriptionEN10applesauce8dispatch2v15blockIFvSA_SC_EEENSQ_IFvSA_SC_SH_jSK_EEEEEEE19__generic_constructB8ne190102IRKNS0_18__copy_constructorISV_LNS0_6_TraitE1EEEEEvRSW_OT_EUlS15_E_JRKNS0_6__baseILSZ_1EJSE_SM_SS_SU_EEEEEEDcS14_DpT0_
- __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm0EEE10__dispatchB8ne190102IOZNS0_6__dtorINS0_8__traitsIJNS_9monostateEN15AQProcessingTap7MIGImplENS9_10DirectImplEEEELNS0_6_TraitE1EE9__destroyB8ne190102EvEUlRT_E_JRNS0_6__baseILSD_1EJS8_SA_SB_EEEEEEDcSF_DpT0_
- __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm0EEE10__dispatchB8ne190102IOZNS0_6__dtorINS0_8__traitsIJNS_9monostateEN2AQ6Server11XPCListenerENSA_9IPCBypassEEEELNS0_6_TraitE1EE9__destroyB8ne190102EvEUlRT_E_JRNS0_6__baseILSE_1EJS8_SB_SC_EEEEEEDcSG_DpT0_
- __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm0EEE10__dispatchB8ne190102IOZNS0_6__dtorINS0_8__traitsIJNS_9monostateEN2AT13SessionFacade7ManagerENSA_11ManagerBaseEEEELNS0_6_TraitE1EE9__destroyB8ne190102EvEUlRT_E_JRNS0_6__baseILSE_1EJS8_SB_SC_EEEEEEDcSG_DpT0_
- __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm0EEE10__dispatchB8ne190102IOZNS0_6__dtorINS0_8__traitsIJPFvPvP16OpaqueAudioQueueP16AudioQueueBufferEPFvS8_SA_SC_PK14AudioTimeStampjPK28AudioStreamPacketDescriptionEN10applesauce8dispatch2v15blockIFvSA_SC_EEENSQ_IFvSA_SC_SH_jSK_EEEEEELNS0_6_TraitE1EE9__destroyB8ne190102EvEUlRT_E_JRNS0_6__baseILSW_1EJSE_SM_SS_SU_EEEEEEDcSY_DpT0_
- __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm1EEE10__dispatchB8ne190102IOZNS0_6__ctorINS0_8__traitsIJPFvPvP16OpaqueAudioQueueP16AudioQueueBufferEPFvS8_SA_SC_PK14AudioTimeStampjPK28AudioStreamPacketDescriptionEN10applesauce8dispatch2v15blockIFvSA_SC_EEENSQ_IFvSA_SC_SH_jSK_EEEEEEE19__generic_constructB8ne190102IRKNS0_18__copy_constructorISV_LNS0_6_TraitE1EEEEEvRSW_OT_EUlS15_E_JRKNS0_6__baseILSZ_1EJSE_SM_SS_SU_EEEEEEDcS14_DpT0_
- __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm1EEE10__dispatchB8ne190102IOZNS0_6__dtorINS0_8__traitsIJNS_9monostateEN15AQProcessingTap7MIGImplENS9_10DirectImplEEEELNS0_6_TraitE1EE9__destroyB8ne190102EvEUlRT_E_JRNS0_6__baseILSD_1EJS8_SA_SB_EEEEEEDcSF_DpT0_
- __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm1EEE10__dispatchB8ne190102IOZNS0_6__dtorINS0_8__traitsIJNS_9monostateEN2AQ6Server11XPCListenerENSA_9IPCBypassEEEELNS0_6_TraitE1EE9__destroyB8ne190102EvEUlRT_E_JRNS0_6__baseILSE_1EJS8_SB_SC_EEEEEEDcSG_DpT0_
- __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm1EEE10__dispatchB8ne190102IOZNS0_6__dtorINS0_8__traitsIJNS_9monostateEN2AT13SessionFacade7ManagerENSA_11ManagerBaseEEEELNS0_6_TraitE1EE9__destroyB8ne190102EvEUlRT_E_JRNS0_6__baseILSE_1EJS8_SB_SC_EEEEEEDcSG_DpT0_
- __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm1EEE10__dispatchB8ne190102IOZNS0_6__dtorINS0_8__traitsIJPFvPvP16OpaqueAudioQueueP16AudioQueueBufferEPFvS8_SA_SC_PK14AudioTimeStampjPK28AudioStreamPacketDescriptionEN10applesauce8dispatch2v15blockIFvSA_SC_EEENSQ_IFvSA_SC_SH_jSK_EEEEEELNS0_6_TraitE1EE9__destroyB8ne190102EvEUlRT_E_JRNS0_6__baseILSW_1EJSE_SM_SS_SU_EEEEEEDcSY_DpT0_
- __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm2EEE10__dispatchB8ne190102IOZNS0_6__ctorINS0_8__traitsIJPFvPvP16OpaqueAudioQueueP16AudioQueueBufferEPFvS8_SA_SC_PK14AudioTimeStampjPK28AudioStreamPacketDescriptionEN10applesauce8dispatch2v15blockIFvSA_SC_EEENSQ_IFvSA_SC_SH_jSK_EEEEEEE19__generic_constructB8ne190102IRKNS0_18__copy_constructorISV_LNS0_6_TraitE1EEEEEvRSW_OT_EUlS15_E_JRKNS0_6__baseILSZ_1EJSE_SM_SS_SU_EEEEEEDcS14_DpT0_
- __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm2EEE10__dispatchB8ne190102IOZNS0_6__dtorINS0_8__traitsIJNS_9monostateEN15AQProcessingTap7MIGImplENS9_10DirectImplEEEELNS0_6_TraitE1EE9__destroyB8ne190102EvEUlRT_E_JRNS0_6__baseILSD_1EJS8_SA_SB_EEEEEEDcSF_DpT0_
- __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm2EEE10__dispatchB8ne190102IOZNS0_6__dtorINS0_8__traitsIJNS_9monostateEN2AQ6Server11XPCListenerENSA_9IPCBypassEEEELNS0_6_TraitE1EE9__destroyB8ne190102EvEUlRT_E_JRNS0_6__baseILSE_1EJS8_SB_SC_EEEEEEDcSG_DpT0_
- __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm2EEE10__dispatchB8ne190102IOZNS0_6__dtorINS0_8__traitsIJNS_9monostateEN2AT13SessionFacade7ManagerENSA_11ManagerBaseEEEELNS0_6_TraitE1EE9__destroyB8ne190102EvEUlRT_E_JRNS0_6__baseILSE_1EJS8_SB_SC_EEEEEEDcSG_DpT0_
- __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm2EEE10__dispatchB8ne190102IOZNS0_6__dtorINS0_8__traitsIJPFvPvP16OpaqueAudioQueueP16AudioQueueBufferEPFvS8_SA_SC_PK14AudioTimeStampjPK28AudioStreamPacketDescriptionEN10applesauce8dispatch2v15blockIFvSA_SC_EEENSQ_IFvSA_SC_SH_jSK_EEEEEELNS0_6_TraitE1EE9__destroyB8ne190102EvEUlRT_E_JRNS0_6__baseILSW_1EJSE_SM_SS_SU_EEEEEEDcSY_DpT0_
- __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm3EEE10__dispatchB8ne190102IOZNS0_6__ctorINS0_8__traitsIJPFvPvP16OpaqueAudioQueueP16AudioQueueBufferEPFvS8_SA_SC_PK14AudioTimeStampjPK28AudioStreamPacketDescriptionEN10applesauce8dispatch2v15blockIFvSA_SC_EEENSQ_IFvSA_SC_SH_jSK_EEEEEEE19__generic_constructB8ne190102IRKNS0_18__copy_constructorISV_LNS0_6_TraitE1EEEEEvRSW_OT_EUlS15_E_JRKNS0_6__baseILSZ_1EJSE_SM_SS_SU_EEEEEEDcS14_DpT0_
- __ZNSt3__116__variant_detail12__visitation6__base12__dispatcherIJLm3EEE10__dispatchB8ne190102IOZNS0_6__dtorINS0_8__traitsIJPFvPvP16OpaqueAudioQueueP16AudioQueueBufferEPFvS8_SA_SC_PK14AudioTimeStampjPK28AudioStreamPacketDescriptionEN10applesauce8dispatch2v15blockIFvSA_SC_EEENSQ_IFvSA_SC_SH_jSK_EEEEEELNS0_6_TraitE1EE9__destroyB8ne190102EvEUlRT_E_JRNS0_6__baseILSW_1EJSE_SM_SS_SU_EEEEEEDcSY_DpT0_
- __ZNSt3__116__variant_detail18__copy_constructorINS0_8__traitsIJPFvPvP16OpaqueAudioQueueP16AudioQueueBufferEPFvS3_S5_S7_PK14AudioTimeStampjPK28AudioStreamPacketDescriptionEN10applesauce8dispatch2v15blockIFvS5_S7_EEENSL_IFvS5_S7_SC_jSF_EEEEEELNS0_6_TraitE1EEC2B8ne190102ERKSS_
- __ZNSt3__116__variant_detail6__dtorINS0_8__traitsIJNS_9monostateEN15AQProcessingTap7MIGImplENS4_10DirectImplEEEELNS0_6_TraitE1EE9__destroyB8ne190102Ev
- __ZNSt3__116__variant_detail6__dtorINS0_8__traitsIJNS_9monostateEN2AQ6Server11XPCListenerENS5_9IPCBypassEEEELNS0_6_TraitE1EE9__destroyB8ne190102Ev
- __ZNSt3__116__variant_detail6__dtorINS0_8__traitsIJPFvPvP16OpaqueAudioQueueP16AudioQueueBufferEPFvS3_S5_S7_PK14AudioTimeStampjPK28AudioStreamPacketDescriptionEN10applesauce8dispatch2v15blockIFvS5_S7_EEENSL_IFvS5_S7_SC_jSF_EEEEEELNS0_6_TraitE1EE9__destroyB8ne190102Ev
- __ZNSt3__116allocator_traitsIN5caulk12rt_allocatorINS_10shared_ptrI14HapticSequenceEEEEE10deallocateB8ne190102ERS6_PS5_m
- __ZNSt3__116allocator_traitsIN5caulk12rt_allocatorINS_11__hash_nodeINS_17__hash_value_typeImbEEPvEEEEE10deallocateB8ne190102ERS8_PS7_m
- __ZNSt3__116allocator_traitsIN5caulk12rt_allocatorINS_11__list_nodeIN13ServerManager12SynthCommandEPvEEEEE10deallocateB8ne190102ERS8_PS7_m
- __ZNSt3__116allocator_traitsIN5caulk12rt_allocatorINS_11__tree_nodeINS_12__value_typeImjEEPvEEEEE10deallocateB8ne190102ERS8_PS7_m
- __ZNSt3__116allocator_traitsIN5caulk12rt_allocatorINS_4pairIPFiPvPjPK14AudioTimeStampjjP15AudioBufferListES4_EEEEE10deallocateB8ne190102ERSE_PSD_m
- __ZNSt3__116allocator_traitsIN5caulk12rt_allocatorIPNS_16__hash_node_baseIPNS_11__hash_nodeINS_17__hash_value_typeImbEEPvEEEEEEE10deallocateB8ne190102ERSC_PSB_m
- __ZNSt3__116allocator_traitsIN5caulk12rt_allocatorIcEEE10deallocateB8ne190102ERS3_Pcm
- __ZNSt3__117__call_once_proxyB8ne190102INS_5tupleIJOZ31SetupSystemSoundClientLogScopesvE3$_0EEEEEvPv
- __ZNSt3__117__call_once_proxyB8ne190102INS_5tupleIJOZN11AQAC3IONodeC1ERK14AQMEIO_Binding14MEStreamTypeIDRidE3$_0EEEEEvPv
- __ZNSt3__117__call_once_proxyB8ne190102INS_5tupleIJOZN11SSServerIPCC1EvE3$_0EEEEEvPv
- __ZNSt3__117__call_once_proxyB8ne190102INS_5tupleIJOZN12CADeprecated10TSingletonI11AQClientMgrE8instanceEvEUlvE_EEEEEvPv
- __ZNSt3__117__call_once_proxyB8ne190102INS_5tupleIJOZN12CADeprecated10TSingletonI11SSClientIPCE8instanceEvEUlvE_EEEEEvPv
- __ZNSt3__117__call_once_proxyB8ne190102INS_5tupleIJOZN12CADeprecated10TSingletonI13HapticMetricsE8instanceEvEUlvE_EEEEEvPv
- __ZNSt3__117__call_once_proxyB8ne190102INS_5tupleIJOZN12CADeprecated10TSingletonI14RemoteIOServerE8instanceEvEUlvE_EEEEEvPv
- __ZNSt3__117__call_once_proxyB8ne190102INS_5tupleIJOZN12CADeprecated10TSingletonI15ActiveSoundListE8instanceEvEUlvE_EEEEEvPv
- __ZNSt3__117__call_once_proxyB8ne190102INS_5tupleIJOZN12CADeprecated10TSingletonI15BorealisManagerE8instanceEvEUlvE_EEEEEvPv
- __ZNSt3__117__call_once_proxyB8ne190102INS_5tupleIJOZN12CADeprecated10TSingletonI15SSSPowerManagerE8instanceEvEUlvE_EEEEEvPv
- __ZNSt3__117__call_once_proxyB8ne190102INS_5tupleIJOZN12CADeprecated10TSingletonI18SSClientCompletionE8instanceEvEUlvE_EEEEEvPv
- __ZNSt3__117__call_once_proxyB8ne190102INS_5tupleIJOZN12CADeprecated10TSingletonI19HapticServerManagerE8instanceEvEUlvE_EEEEEvPv
- __ZNSt3__117__call_once_proxyB8ne190102INS_5tupleIJOZN12CADeprecated10TSingletonI20SSSCallbackMessengerE8instanceEvEUlvE_EEEEEvPv
- __ZNSt3__117__call_once_proxyB8ne190102INS_5tupleIJOZN12CADeprecated10TSingletonI21CAExternalLockJanitorE8instanceEvEUlvE_EEEEEvPv
- __ZNSt3__117__call_once_proxyB8ne190102INS_5tupleIJOZN12CADeprecated10TSingletonI26ClientProcessingTapManagerE8instanceEvEUlvE_EEEEEvPv
- __ZNSt3__117__call_once_proxyB8ne190102INS_5tupleIJOZN12CADeprecated10TSingletonI8SSServerE8instanceEvEUlvE_EEEEEvPv
- __ZNSt3__117__call_once_proxyB8ne190102INS_5tupleIJOZN12CADeprecated10TSingletonIN12_GLOBAL__N_118CoreMotionSoftlinkEE8instanceEvEUlvE_EEEEEvPv
- __ZNSt3__117__call_once_proxyB8ne190102INS_5tupleIJOZN12CADeprecated10TSingletonIN15CAListenerProxy13ZombieJanitorEE8instanceEvEUlvE_EEEEEvPv
- __ZNSt3__117__call_once_proxyB8ne190102INS_5tupleIJOZN12CADeprecated10TSingletonIN20AudioImpulseInjector4Impl20NotificationListenerEE8instanceEvEUlvE_EEEEEvPv
- __ZNSt3__117__call_once_proxyB8ne190102INS_5tupleIJOZN18AQOfflineMixerBaseC1ER15AQIONodeManageriRK27AudioStreamBasicDescriptionRKN2CA13ChannelLayoutERiE3$_0EEEEEvPv
- __ZNSt3__117__call_once_proxyB8ne190102INS_5tupleIJOZN20CA_UISoundClientBaseC1EdjPK14__CFDictionaryjE3$_0EEEEEvPv
- __ZNSt3__118__set_intersectionB8ne190102INS_17_ClassicAlgPolicyENS_6__lessIvvEENS_21__hash_const_iteratorIPNS_11__hash_nodeIjPvEEEES9_S9_S9_NS_20back_insert_iteratorINS_6vectorIjNS_9allocatorIjEEEEEEEENS_25__set_intersection_resultIT1_T3_T5_EESH_T2_SI_T4_SJ_OT0_NS_20forward_iterator_tagESP_
- __ZNSt3__118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B8ne190102Ev
- __ZNSt3__119__allocate_at_leastB8ne190102IN5caulk12rt_allocatorINS_4pairIPFiPvPjPK14AudioTimeStampjjP15AudioBufferListES4_EEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSH_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorI10MusicEventEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorI11VolumeEventEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorI13ChaseInstInfoEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorI14MEStreamTypeIDEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorI15MEVADIdentifierEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorI15MeterTrackEntryEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorI16AURateRampStructEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorI18AudioMetadataEventEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorI22AUGraphLiveUpdateEventEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorI23AudioUnitParameterEventEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorI24AudioQueueParameterEventEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorI26AQBufferCreateDestroyEventEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorI26AudioObjectPropertyAddressEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorI30AQProcessingNodeImmediateEventEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorI32AudioSessionPropertyListenerInfoEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorI9TapSourceEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN10applesauce2CF11TypeRefPairEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN10applesauce2CF7TypeRefEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN10applesauce2CF9NumberRefEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN14NoteOffManager14ControlMessageEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN16AudioQueueObject12AQRateChangeEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN16ClientAudioQueue16PropertyListenerEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN18AQOfflineMixerBase15StartQueueEventEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN19SequenceDestination14TrackPlayStateEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN21VibeToHapticConverter11SegmentInfoEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN2AQ6Server12RemoteClient5QueueEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS9_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN8TempoMap10TempoEntryEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN8audioipc18SharedAudioBuffers7ElementEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorINS_10shared_ptrI9TapSubmixEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorINS_10shared_ptrIN10AQMEIO_HAL8IOStreamEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS9_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorINS_10unique_ptrI16MCProcessingNodeNS_14default_deleteIS3_EEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSA_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorINS_10unique_ptrIN15AQMixEngine_VAD10MEVADeviceENS_14default_deleteIS4_EEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSB_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorINS_10unique_ptrIN18PowerUsageWatchdog12ClientLoggerENS_14default_deleteIS4_EEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSB_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSA_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorINS_4pairIN2OS2CF6StringEN10applesauce8dispatch2v15blockIFv13CAOrientationEEEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSH_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorINS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEES7_EEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSC_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorINS_4pairIjNS_8optionalIjEEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS9_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorINS_5tupleIJjPFvPvP16OpaqueAudioQueuejES3_EEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSC_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIP10AUNodeInfoEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIP11MCAudioUnitEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIP11MEConnectorEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIP13AudioTapMixerEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIP14AQIONodeClientEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIP14MEMixerChannelEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIP15InputDispatcherEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIP15XProcessingBaseEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIP19SSSActionPlayerBaseEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIP20MEOutputStreamClientEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIP25AQMEIO_NotificationClientEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIPKvEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIPN15CAListenerProxy8ListenerEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIPN5boost8functionIFNS2_3msm4back11HandledEnumEvEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSD_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIPNS_4pairIN5boost8functionIFNS3_3msm4back11HandledEnumEvEEEbEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSF_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIPjEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIPmEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIfEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIiEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIjEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorImEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIxEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__119__shared_weak_count16__release_sharedB8ne190102Ev
- __ZNSt3__119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B8ne190102Ev
- __ZNSt3__120__optional_copy_baseIN2CA13ChannelLayoutELb0EEC2B8ne190102ERKS3_
- __ZNSt3__120__optional_copy_baseIN4swix14timeout_configELb0EEC2B8ne190102ERKS3_
- __ZNSt3__120__optional_copy_baseINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEELb0EEC2B8ne190102ERKS7_
- __ZNSt3__120__shared_ptr_emplaceIN12CADeprecated16XMachReceivePortENS_9allocatorIS2_EEE16__on_zero_sharedEv
- __ZNSt3__120__shared_ptr_emplaceIN12CADeprecated16XMachReceivePortENS_9allocatorIS2_EEE21__on_zero_shared_weakEv
- __ZNSt3__120__shared_ptr_emplaceIN12CADeprecated16XMachReceivePortENS_9allocatorIS2_EEED0Ev
- __ZNSt3__120__shared_ptr_emplaceIN12CADeprecated16XMachReceivePortENS_9allocatorIS2_EEED1Ev
- __ZNSt3__120__shared_ptr_emplaceIN5caulk12synchronizedIN2AQ6Server16ProcessingTapIPCENS1_4mach11unfair_lockENS1_22empty_atomic_interfaceIS5_EEEENS_9allocatorISA_EEE16__on_zero_sharedEv
- __ZNSt3__120__shared_ptr_emplaceIN5caulk12synchronizedIN2AQ6Server16ProcessingTapIPCENS1_4mach11unfair_lockENS1_22empty_atomic_interfaceIS5_EEEENS_9allocatorISA_EEE21__on_zero_shared_weakEv
- __ZNSt3__120__shared_ptr_emplaceIN5caulk12synchronizedIN2AQ6Server16ProcessingTapIPCENS1_4mach11unfair_lockENS1_22empty_atomic_interfaceIS5_EEEENS_9allocatorISA_EEED0Ev
- __ZNSt3__120__shared_ptr_emplaceIN5caulk12synchronizedIN2AQ6Server16ProcessingTapIPCENS1_4mach11unfair_lockENS1_22empty_atomic_interfaceIS5_EEEENS_9allocatorISA_EEED1Ev
- __ZNSt3__120__shared_ptr_pointerIP14AQRemoteClientNS1_11NoOpDeleterENS_9allocatorIS1_EEE16__on_zero_sharedEv
- __ZNSt3__120__shared_ptr_pointerIP14AQRemoteClientNS1_11NoOpDeleterENS_9allocatorIS1_EEE21__on_zero_shared_weakEv
- __ZNSt3__120__shared_ptr_pointerIP14AQRemoteClientNS1_11NoOpDeleterENS_9allocatorIS1_EEED0Ev
- __ZNSt3__120__shared_ptr_pointerIP14AQRemoteClientNS1_11NoOpDeleterENS_9allocatorIS1_EEED1Ev
- __ZNSt3__120__shared_ptr_pointerIPxZL22getCAReporterIDForCallvE3$_0NS_9allocatorIxEEE16__on_zero_sharedEv
- __ZNSt3__120__shared_ptr_pointerIPxZL22getCAReporterIDForCallvE3$_0NS_9allocatorIxEEE21__on_zero_shared_weakEv
- __ZNSt3__120__shared_ptr_pointerIPxZL22getCAReporterIDForCallvE3$_0NS_9allocatorIxEEED0Ev
- __ZNSt3__120__shared_ptr_pointerIPxZL22getCAReporterIDForCallvE3$_0NS_9allocatorIxEEED1Ev
- __ZNSt3__120__throw_bad_weak_ptrB8ne190102Ev
- __ZNSt3__120__throw_length_errorB8ne190102EPKc
- __ZNSt3__120__throw_out_of_rangeB8ne190102EPKc
- __ZNSt3__120back_insert_iteratorINS_6vectorIjNS_9allocatorIjEEEEEaSB8ne190102ERKj
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEPvEEEEEclB8ne190102EPS9_
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEE26STSPerLabelControllerStateEEPvEEEEEclB8ne190102EPSC_
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEbEEPvEEEEEclB8ne190102EPSB_
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIPvN10applesauce8dispatch2v15blockIFv28AUVoiceIOSpeechActivityEventEEEEES4_EEEEEclB8ne190102EPSD_
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIjNS_10unique_ptrI27SSClientCompletionBlockInfoNS_14default_deleteIS5_EEEEEEPvEEEEEclB8ne190102EPSB_
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIjNS_6vectorIhNS1_IhEEEEEEPvEEEEEclB8ne190102EPS9_
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeImNS_10shared_ptrI14HapticSequenceEEEEPvEEEEEclB8ne190102EPS9_
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeImNS_10shared_ptrIN18PowerUsageWatchdog17ClientDescriptionEEEEEPvEEEEEclB8ne190102EPSA_
- __ZNSt3__122__lower_bound_onesidedB8ne190102INS_17_ClassicAlgPolicyENS_21__hash_const_iteratorIPNS_11__hash_nodeIjPvEEEES7_jKNS_10__identityENS_6__lessIvvEEEET0_SC_T1_RKT2_RT4_RT3_
- __ZNSt3__122__tree_node_destructorINS_9allocatorINS_11__tree_nodeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEPK14__CFDictionaryEEPvEEEEEclB8ne190102EPSE_
- __ZNSt3__123__optional_storage_baseI14AQMEIO_BindingLb0EE13__assign_fromB8ne190102IRKNS_27__optional_copy_assign_baseIS1_Lb0EEEEEvOT_
- __ZNSt3__123__optional_storage_baseIN10applesauce2CF9StringRefELb0EE13__assign_fromB8ne190102INS_27__optional_move_assign_baseIS3_Lb0EEEEEvOT_
- __ZNSt3__123__optional_storage_baseIN10applesauce2CF9StringRefELb0EE13__assign_fromB8ne190102IRKNS_27__optional_copy_assign_baseIS3_Lb0EEEEEvOT_
- __ZNSt3__123__optional_storage_baseIN2AT9IOBindingELb0EE13__assign_fromB8ne190102IRKNS_27__optional_copy_assign_baseIS2_Lb0EEEEEvOT_
- __ZNSt3__123__optional_storage_baseIN2CA13ChannelLayoutELb0EE13__assign_fromB8ne190102INS_27__optional_move_assign_baseIS2_Lb0EEEEEvOT_
- __ZNSt3__124__optional_destruct_baseIN10applesauce2CF7DataRefELb0EED2B8ne190102Ev
- __ZNSt3__124__optional_destruct_baseIN10applesauce2CF9StringRefELb0EE5resetB8ne190102Ev
- __ZNSt3__124__optional_destruct_baseIN10applesauce2CF9StringRefELb0EED2B8ne190102Ev
- __ZNSt3__124__optional_destruct_baseIN12CADeprecated11XMachServer6ClientELb0EED2B8ne190102Ev
- __ZNSt3__124__optional_destruct_baseIN16AudioQueueObject15InputRingBufferELb0EED2B8ne190102Ev
- __ZNSt3__124__optional_destruct_baseIN2CA12AudioBuffersELb0EE5resetB8ne190102Ev
- __ZNSt3__124__optional_destruct_baseIN2CA12AudioBuffersELb0EED2B8ne190102Ev
- __ZNSt3__124__optional_destruct_baseIN4swix17connection_configELb0EED2B8ne190102Ev
- __ZNSt3__124__optional_destruct_baseIN5caulk5alloc23guarded_edges_allocatorINS2_16tiered_allocatorIJNS2_15size_range_tierILm0ELm409599ENS2_22consolidating_free_mapIN2AQ19SharedPageAllocatorELm10485760EEEEENS2_18tracking_allocatorIS8_EEEEELm2EEELb0EE5resetB8ne190102Ev
- __ZNSt3__124__optional_destruct_baseIN9TapSubmix10InputState14BufferingStateELb0EE5resetB8ne190102Ev
- __ZNSt3__124__optional_destruct_baseIN9TapSubmix10InputState14BufferingStateELb0EED2B8ne190102Ev
- __ZNSt3__124__put_character_sequenceB8ne190102IcNS_11char_traitsIcEEEERNS_13basic_ostreamIT_T0_EES7_PKS4_m
- __ZNSt3__125__throw_bad_function_callB8ne190102Ev
- __ZNSt3__126__throw_bad_variant_accessB8ne190102Ev
- __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERNS_6__lessIvvEEP10MusicEventEEbT1_S7_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERNS_6__lessIvvEEP11VolumeEventEEbT1_S7_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERNS_6__lessIvvEEP15MEVADIdentifierEEbT1_S7_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPN14NoteOffManager11NoteOffInfoEEEbT1_S8_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEEbT1_SC_T0_
- __ZNSt3__127__throw_bad_optional_accessB8ne190102Ev
- __ZNSt3__127__tree_balance_after_insertB8ne190102IPNS_16__tree_node_baseIPvEEEEvT_S5_
- __ZNSt3__133lexicographical_compare_three_wayB8ne190102INS_11__wrap_iterIPKiEES4_NS_17__synth_three_wayMUlTyTyRKT_RKT0_E_EEEDTclfp3_defp_defp1_EES5_S5_S8_S8_T1_
- __ZNSt3__133lexicographical_compare_three_wayB8ne190102INS_11__wrap_iterIPKjEES4_NS_17__synth_three_wayMUlTyTyRKT_RKT0_E_EEEDTclfp3_defp_defp1_EES5_S5_S8_S8_T1_
- __ZNSt3__134__uninitialized_allocator_relocateB8ne190102INS_9allocatorI10MusicEventEES2_EEvRT_PT0_S7_S7_
- __ZNSt3__134__uninitialized_allocator_relocateB8ne190102INS_9allocatorI9TapSourceEES2_EEvRT_PT0_S7_S7_
- __ZNSt3__134__uninitialized_allocator_relocateB8ne190102INS_9allocatorIN10applesauce2CF11TypeRefPairEEES4_EEvRT_PT0_S9_S9_
- __ZNSt3__134__uninitialized_allocator_relocateB8ne190102INS_9allocatorIN8InfoList9InfoEntryEEES3_EEvRT_PT0_S8_S8_
- __ZNSt3__134__uninitialized_allocator_relocateB8ne190102INS_9allocatorIN8audioipc18SharedAudioBuffers7ElementEEES4_EEvRT_PT0_S9_S9_
- __ZNSt3__134__uninitialized_allocator_relocateB8ne190102INS_9allocatorINS_4pairIN2OS2CF6StringEN10applesauce8dispatch2v15blockIFv13CAOrientationEEEEEEESD_EEvRT_PT0_SI_SI_
- __ZNSt3__135__uninitialized_allocator_copy_implB8ne190102INS_9allocatorI10MusicEventEEPS2_S4_S4_EET2_RT_T0_T1_S5_
- __ZNSt3__135__uninitialized_allocator_copy_implB8ne190102INS_9allocatorINS_10shared_ptrI9TapSubmixEEEEPS4_S6_S6_EET2_RT_T0_T1_S7_
- __ZNSt3__13setIP10XAudioUnitNS_4lessIS2_EENS_9allocatorIS2_EEEC2B8ne190102ERKS7_
- __ZNSt3__14__fs10filesystem4pathC2B8ne190102INS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEvEERKT_NS2_6formatE
- __ZNSt3__14listIN5boost13intrusive_ptrIKNS1_10statechart10event_baseEEENS_9allocatorIS6_EEE9push_backERKS6_
- __ZNSt3__14pairIKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEN10applesauce2CF7TypeRefEED1Ev
- __ZNSt3__14pairIKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI29NewNotificationCenterObserverEEED1Ev
- __ZNSt3__14pairIKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI29OldNotificationCenterObserverEEED1Ev
- __ZNSt3__14pairIN2OS2CF6StringEN10applesauce8dispatch2v15blockIFv13CAOrientationEEEEC2B8ne190102EOSB_
- __ZNSt3__14pairIN2OS2CF6StringEN10applesauce8dispatch2v15blockIFv13CAOrientationEEEEaSB8ne190102EOSB_
- __ZNSt3__14pairINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEES6_EC2B8ne190102ERKS7_
- __ZNSt3__15arrayIN5Phase13ServerManager12IONodeClientELm2EED1Ev
- __ZNSt3__15dequeIN5boost8functionIFNS1_3msm4back11HandledEnumEvEEENS_9allocatorIS7_EEED2B8ne190102Ev
- __ZNSt3__15dequeINS_4pairIN5boost8functionIFNS2_3msm4back11HandledEnumEvEEEbEENS_9allocatorIS9_EEE26__maybe_remove_front_spareB8ne190102Eb
- __ZNSt3__15dequeINS_4pairIN5boost8functionIFNS2_3msm4back11HandledEnumEvEEEbEENS_9allocatorIS9_EEED2B8ne190102Ev
- __ZNSt3__15dequeIjNS_9allocatorIjEEE26__maybe_remove_front_spareB8ne190102Eb
- __ZNSt3__15dequeIjNS_9allocatorIjEEED2B8ne190102Ev
- __ZNSt3__15tupleIJN10applesauce3xpc6objectEN4swix6stringEjEED1Ev
- __ZNSt3__15tupleIJN10applesauce3xpc6objectEjjbNS_6vectorIjNS_9allocatorIjEEEEEED1Ev
- __ZNSt3__15tupleIJjj27AudioStreamBasicDescriptionN10applesauce3xpc6objectES4_EED1Ev
- __ZNSt3__16__sortIRNS_6__lessIjjEEPjEEvT0_S5_T_
- __ZNSt3__16__treeINS_12__value_typeIN5boost10statechart6detail11history_keyINS4_11rtti_policyEEEPFvvEEENS_19__map_value_compareIS7_SA_NS_4lessIS7_EELb1EEENS_9allocatorISA_EEE7destroyEPNS_11__tree_nodeISA_PvEE
- __ZNSt3__16__treeINS_12__value_typeIPK14AQIONodeClientZL34PopulateSourceFormatInfoDictionaryP14__CFDictionaryPKvRS3_RN2CA17StreamDescriptionEbbbE16SourceFormatInfoEENS_19__map_value_compareIS4_SE_NS_4lessIS4_EELb1EEENS_9allocatorISE_EEE7destroyEPNS_11__tree_nodeISE_PvEE
- __ZNSt3__16vectorI10ChaseEventNS_9allocatorIS1_EEE16__destroy_vectorclB8ne190102Ev
- __ZNSt3__16vectorI10ChaseEventNS_9allocatorIS1_EEE21__push_back_slow_pathIS1_EEPS1_OT_
- __ZNSt3__16vectorI10ChaseEventNS_9allocatorIS1_EEE5eraseENS_11__wrap_iterIPKS1_EES8_
- __ZNSt3__16vectorI10ChaseEventNS_9allocatorIS1_EEE9push_backB8ne190102EOS1_
- __ZNSt3__16vectorI10MusicEventNS_9allocatorIS1_EEE16__destroy_vectorclB8ne190102Ev
- __ZNSt3__16vectorI10MusicEventNS_9allocatorIS1_EEE18__assign_with_sizeB8ne190102IPS1_S6_EEvT_T0_l
- __ZNSt3__16vectorI10MusicEventNS_9allocatorIS1_EEE18__insert_with_sizeB8ne190102INS_11__wrap_iterIPS1_EES8_EES8_NS6_IPKS1_EET_T0_l
- __ZNSt3__16vectorI10MusicEventNS_9allocatorIS1_EEE21__push_back_slow_pathIRKS1_EEPS1_OT_
- __ZNSt3__16vectorI15MEVADIdentifierNS_9allocatorIS1_EEE11__vallocateB8ne190102Em
- __ZNSt3__16vectorI15MEVADIdentifierNS_9allocatorIS1_EEE16__destroy_vectorclB8ne190102Ev
- __ZNSt3__16vectorI15MEVADIdentifierNS_9allocatorIS1_EEE16__init_with_sizeB8ne190102IPS1_S6_EEvT_T0_m
- __ZNSt3__16vectorI23AudioUnitParameterEventNS_9allocatorIS1_EEE7reserveEm
- __ZNSt3__16vectorI26AudioObjectPropertyAddressNS_9allocatorIS1_EEE11__vallocateB8ne190102Em
- __ZNSt3__16vectorI9TapSourceNS_9allocatorIS1_EEE16__destroy_vectorclB8ne190102Ev
- __ZNSt3__16vectorIN10applesauce2CF11TypeRefPairENS_9allocatorIS3_EEE16__destroy_vectorclB8ne190102Ev
- __ZNSt3__16vectorIN10applesauce2CF7TypeRefENS_9allocatorIS3_EEE16__destroy_vectorclB8ne190102Ev
- __ZNSt3__16vectorIN10applesauce2CF9NumberRefENS_9allocatorIS3_EEE16__destroy_vectorclB8ne190102Ev
- __ZNSt3__16vectorIN21IPCAUSharedMemoryBase7ElementENS_9allocatorIS2_EEE16__destroy_vectorclB8ne190102Ev
- __ZNSt3__16vectorIN21VibeToHapticConverter11SegmentInfoENS_9allocatorIS2_EEE9push_backB8ne190102EOS2_
- __ZNSt3__16vectorIN25AUNodeSequenceDestination18RampTrackPlayStateENS_9allocatorIS2_EEE16__destroy_vectorclB8ne190102Ev
- __ZNSt3__16vectorIN2AQ6Server12RemoteClient18ProcessingTapStateENS_9allocatorIS4_EEE16__destroy_vectorclB8ne190102Ev
- __ZNSt3__16vectorIN2AU8Property10Attributes7details15AUPresetWrapperENS_9allocatorIS5_EEE16__destroy_vectorclB8ne190102Ev
- __ZNSt3__16vectorIN5boost8functionIFvRN11SequenceFSM25PostRenderFlushingVisitorEP14SequenceActiondEEENS_9allocatorIS9_EEE16__destroy_vectorclB8ne190102Ev
- __ZNSt3__16vectorIN8InfoList9InfoEntryENS_9allocatorIS2_EEE16__destroy_vectorclB8ne190102Ev
- __ZNSt3__16vectorIN8audioipc18SharedAudioBuffers7ElementENS_9allocatorIS3_EEE16__destroy_vectorclB8ne190102Ev
- __ZNSt3__16vectorINS_10shared_ptrI14HapticSequenceEEN5caulk12rt_allocatorIS3_EEE16__destroy_vectorclB8ne190102Ev
- __ZNSt3__16vectorINS_10shared_ptrI14HapticSequenceEEN5caulk12rt_allocatorIS3_EEE7__clearB8ne190102Ev
- __ZNSt3__16vectorINS_10shared_ptrI8AQIONodeEENS_9allocatorIS3_EEE16__destroy_vectorclB8ne190102Ev
- __ZNSt3__16vectorINS_10shared_ptrI9TapSubmixEENS_9allocatorIS3_EEE11__vallocateB8ne190102Em
- __ZNSt3__16vectorINS_10shared_ptrI9TapSubmixEENS_9allocatorIS3_EEE16__destroy_vectorclB8ne190102Ev
- __ZNSt3__16vectorINS_10shared_ptrI9TapSubmixEENS_9allocatorIS3_EEE16__init_with_sizeB8ne190102IPS3_S8_EEvT_T0_m
- __ZNSt3__16vectorINS_10shared_ptrI9TapSubmixEENS_9allocatorIS3_EEE7__clearB8ne190102Ev
- __ZNSt3__16vectorINS_10shared_ptrIN10AQMEIO_HAL8IOStreamEEENS_9allocatorIS4_EEE16__destroy_vectorclB8ne190102Ev
- __ZNSt3__16vectorINS_10shared_ptrIN10AQMEIO_HAL8IOStreamEEENS_9allocatorIS4_EEE7__clearB8ne190102Ev
- __ZNSt3__16vectorINS_10shared_ptrIN18PowerUsageWatchdog17ClientDescriptionEEENS_9allocatorIS4_EEE16__destroy_vectorclB8ne190102Ev
- __ZNSt3__16vectorINS_10unique_ptrI14AQOfflineMixerNS_14default_deleteIS2_EEEENS_9allocatorIS5_EEE16__destroy_vectorclB8ne190102Ev
- __ZNSt3__16vectorINS_10unique_ptrI14AQOfflineMixerNS_14default_deleteIS2_EEEENS_9allocatorIS5_EEE7__clearB8ne190102Ev
- __ZNSt3__16vectorINS_10unique_ptrI15SubmixTapObjectNS_14default_deleteIS2_EEEENS_9allocatorIS5_EEE16__destroy_vectorclB8ne190102Ev
- __ZNSt3__16vectorINS_10unique_ptrI16AQProcessingNodeNS_14default_deleteIS2_EEEENS_9allocatorIS5_EEE16__destroy_vectorclB8ne190102Ev
- __ZNSt3__16vectorINS_10unique_ptrI16MCProcessingNodeNS_14default_deleteIS2_EEEENS_9allocatorIS5_EEE16__destroy_vectorclB8ne190102Ev
- __ZNSt3__16vectorINS_10unique_ptrIN15AQMixEngine_VAD10MEVADeviceENS_14default_deleteIS3_EEEENS_9allocatorIS6_EEE16__destroy_vectorclB8ne190102Ev
- __ZNSt3__16vectorINS_10unique_ptrIN18PowerUsageWatchdog12ClientLoggerENS_14default_deleteIS3_EEEENS_9allocatorIS6_EEE16__destroy_vectorclB8ne190102Ev
- __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE16__destroy_vectorclB8ne190102Ev
- __ZNSt3__16vectorINS_13unordered_mapINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEbNS_4hashIS7_EENS_8equal_toIS7_EENS5_INS_4pairIKS7_bEEEEEENS5_ISG_EEE16__destroy_vectorclB8ne190102Ev
- __ZNSt3__16vectorINS_4pairIN2OS2CF6StringEN10applesauce8dispatch2v15blockIFv13CAOrientationEEEEENS_9allocatorISC_EEE16__destroy_vectorclB8ne190102Ev
- __ZNSt3__16vectorINS_4pairINS_10unique_ptrI11SynthOutputNS_14default_deleteIS3_EEEEbEENS_9allocatorIS7_EEE16__destroy_vectorclB8ne190102Ev
- __ZNSt3__16vectorINS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEES7_EENS5_IS8_EEE16__destroy_vectorclB8ne190102Ev
- __ZNSt3__16vectorINS_4pairIjNS_10shared_ptrIN2AQ3API11BufferOwnerEEEEENS_9allocatorIS7_EEE16__destroy_vectorclB8ne190102Ev
- __ZNSt3__16vectorINS_4pairIjNS_10shared_ptrIN2AQ3API11BufferOwnerEEEEENS_9allocatorIS7_EEE7__clearB8ne190102Ev
- __ZNSt3__16vectorINS_5tupleIJjNS_10shared_ptrIN2AQ3API5QueueEEEEEENS_9allocatorIS7_EEE16__destroy_vectorclB8ne190102Ev
- __ZNSt3__16vectorINS_5tupleIJjNS_10shared_ptrIN2AQ3API9SubmixTapEEEEEENS_9allocatorIS7_EEE16__destroy_vectorclB8ne190102Ev
- __ZNSt3__16vectorINS_8weak_ptrI8AQIONodeEENS_9allocatorIS3_EEE16__destroy_vectorclB8ne190102Ev
- __ZNSt3__16vectorIP14MEMixerChannelNS_9allocatorIS2_EEE16__init_with_sizeB8ne190102IPS2_S7_EEvT_T0_m
- __ZNSt3__16vectorIP25AQMEIO_NotificationClientNS_9allocatorIS2_EEE16__init_with_sizeB8ne190102IPS2_S7_EEvT_T0_m
- __ZNSt3__16vectorIPKvNS_9allocatorIS2_EEEC2B8ne190102Em
- __ZNSt3__16vectorISt4byteNS_9allocatorIS1_EEEC2B8ne190102Em
- __ZNSt3__16vectorIU8__strongP24ATAudioSessionClientImplNS_9allocatorIS3_EEE9push_backB8ne190102ERU8__strongKS2_
- __ZNSt3__16vectorIcN5caulk12rt_allocatorIcEEE8__appendEm
- __ZNSt3__16vectorIcNS_9allocatorIcEEE11__vallocateB8ne190102Em
- __ZNSt3__16vectorIcNS_9allocatorIcEEE16__init_with_sizeB8ne190102IPcS5_EEvT_T0_m
- __ZNSt3__16vectorIcNS_9allocatorIcEEE18__assign_with_sizeB8ne190102IPcS5_EEvT_T0_l
- __ZNSt3__16vectorIcNS_9allocatorIcEEEC2B8ne190102Em
- __ZNSt3__16vectorIcNS_9allocatorIcEEEC2B8ne190102EmRKc
- __ZNSt3__16vectorIhNS_9allocatorIhEEE11__vallocateB8ne190102Em
- __ZNSt3__16vectorIhNS_9allocatorIhEEE18__assign_with_sizeB8ne190102IPhS5_EEvT_T0_l
- __ZNSt3__16vectorIhNS_9allocatorIhEEEC2B8ne190102Em
- __ZNSt3__16vectorIiNS_9allocatorIiEEE11__vallocateB8ne190102Em
- __ZNSt3__16vectorIiNS_9allocatorIiEEE16__init_with_sizeB8ne190102IPiS5_EEvT_T0_m
- __ZNSt3__16vectorIiNS_9allocatorIiEEE18__assign_with_sizeB8ne190102IPKiS6_EEvT_T0_l
- __ZNSt3__16vectorIjNS_9allocatorIjEEE11__vallocateB8ne190102Em
- __ZNSt3__16vectorIjNS_9allocatorIjEEE16__init_with_sizeB8ne190102INS_11__wrap_iterIPKjEES8_EEvT_T0_m
- __ZNSt3__16vectorIjNS_9allocatorIjEEE16__init_with_sizeB8ne190102IPjS5_EEvT_T0_m
- __ZNSt3__16vectorIjNS_9allocatorIjEEE18__assign_with_sizeB8ne190102IPKjS6_EEvT_T0_l
- __ZNSt3__16vectorIjNS_9allocatorIjEEE18__assign_with_sizeB8ne190102IPjS5_EEvT_T0_l
- __ZNSt3__16vectorIjNS_9allocatorIjEEE18__insert_with_sizeB8ne190102INS_11__wrap_iterIPjEES7_EES7_NS5_IPKjEET_T0_l
- __ZNSt3__16vectorIjNS_9allocatorIjEEEC2B8ne190102Em
- __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERNS_6__lessIvvEEP10MusicEventEEjT1_S7_S7_T0_
- __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERNS_6__lessIvvEEP11VolumeEventEEjT1_S7_S7_T0_
- __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERNS_6__lessIvvEEP15MEVADIdentifierEEjT1_S7_S7_T0_
- __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPN14NoteOffManager11NoteOffInfoEEEjT1_S8_S8_T0_
- __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEEjT1_SC_SC_T0_
- __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERNS_6__lessIvvEEP10MusicEventEEvT1_S7_S7_S7_T0_
- __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERNS_6__lessIvvEEP11VolumeEventEEvT1_S7_S7_S7_T0_
- __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERNS_6__lessIvvEEP15MEVADIdentifierEEvT1_S7_S7_S7_T0_
- __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPN14NoteOffManager11NoteOffInfoEEEvT1_S8_S8_S8_T0_
- __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEEvT1_SC_SC_SC_T0_
- __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERNS_6__lessIvvEEP10MusicEventEEvT1_S7_S7_S7_S7_T0_
- __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERNS_6__lessIvvEEP11VolumeEventEEvT1_S7_S7_S7_S7_T0_
- __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERNS_6__lessIvvEEP15MEVADIdentifierEEvT1_S7_S7_S7_S7_T0_
- __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPN14NoteOffManager11NoteOffInfoEEEvT1_S8_S8_S8_S8_T0_
- __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEEvT1_SC_SC_SC_SC_T0_
- __ZNSt3__18_IterOpsINS_17_ClassicAlgPolicyEE9iter_swapB8ne190102IRP10MusicEventS6_EEvOT_OT0_
- __ZNSt3__18optionalI14AQMEIO_BindingE7emplaceB8ne190102IJR15AQIONodeManagerRPK10__CFStringEvEERS1_DpOT_
- __ZNSt3__18optionalI14AQMEIO_BindingEaSB8ne190102IRKS1_vEERS2_OT_
- __ZNSt3__18optionalIN4swix6resultIJNS1_4dataEEEEEaSB8ne190102IS4_vEERS5_OT_
- __ZNSt3__18optionalIN5caulk10concurrent25guarded_lookup_hash_tableIjP16BaseOpaqueObjectLNS2_33guarded_lookup_hash_table_optionsE0ENS_8functionIFjjEEEE13scoped_lookupEE7emplaceB8ne190102IJRSA_RKjEvEERSB_DpOT_
- __ZNSt3__18optionalIN8audioipc18SharedAudioBuffersEE7emplaceB8ne190102IJRjNS_4spanIKNS1_14ExtendedFormatELm18446744073709551615EEENS6_IhLm18446744073709551615EEEEvEERS2_DpOT_
- __ZNSt3__18optionalIN8audioipc19os_workgroup_joinerEE7emplaceB8ne190102IJRN5caulk4mach20os_workgroup_managedEEvEERS2_DpOT_
- __ZNSt3__19remove_ifB8ne190102INS_11__wrap_iterIPNS_8weak_ptrIN5caulk17lifetime_observedINS_10unique_ptrI16AQMEIO_InterfaceNS_14default_deleteIS6_EEEENS3_23shared_instance_managerIS6_E8observerEEEEEEEZNSB_14remove_expiredEvEUlRKT_E_EESH_SH_SH_T0_
- __ZNSt3__1plB8ne190102IcNS_11char_traitsIcEENS_9allocatorIcEEEENS_12basic_stringIT_T0_T1_EEOS9_PKS6_
- __ZNSt3__1plB8ne190102IcNS_11char_traitsIcEENS_9allocatorIcEEEENS_12basic_stringIT_T0_T1_EEPKS6_OS9_
- __ZNSt3__1ssB8ne190102IcNS_11char_traitsIcEENS_9allocatorIcEEEEDaRKNS_12basic_stringIT_T0_T1_EESC_
- __ZSt28__throw_bad_array_new_lengthB8ne190102v
- __ZTV11HapticMutex
- __ZTV13TOpaqueObjectI16ClientAudioQueueP16OpaqueAudioQueue16BaseOpaqueObjectE
- __ZTV14AQRemoteClient
- __ZTV14CAExternalLock
- __ZTV16ClientAudioQueue
- __ZTV18BorealisServerImpl
- __ZTV18CAReferenceCounted
- __ZTV19ClientProcessingTap
- __ZTV20ClientAQOfflineMixer
- __ZTV20ClientMessageHandler
- __ZTV20DSP_Routing_Borealis
- __ZTV20ScheduledSlicePlayer
- __ZTV21MIGVariableLengthVars
- __ZTV22MIGVariableLengthVars2IA1024_hE
- __ZTV34MCProcessingNodeInputChunkerInsert
- __ZTV6Waiter
- __ZTV8AQServer
- __ZTVN11AQClientMgr6ServerE
- __ZTVN11MidiDataRef18CountedMidiDataRefE
- __ZTVN12CADeprecated17XMachPortServicer11RunLoopImplE
- __ZTVN12CADeprecated20GenericRunLoopThreadE
- __ZTVN15AQProcessingTap17PortDeathListenerE
- __ZTVN19SharableMemoryBlock15MachClientTokenE
- __ZTVN20DSP_Routing_Borealis13SpeakerStreamE
- __ZTVN20DSP_Routing_Borealis9MicStreamE
- __ZTVN2AQ3API10LegacyImplE
- __ZTVN2AQ6Server4BaseE
- __ZTVN2OS2CF4DataE
- __ZTVN4brls10AOPRunningE
- __ZTVN4brls11PSAnalyzingE
- __ZTVN4brls11PSRecordingE
- __ZTVN4brls12EvtPSTriggerE
- __ZTVN4brls13EvtAOPTriggerE
- __ZTVN4brls13PSAwaitRecordE
- __ZTVN4brls14EvtVTSMEnabledE
- __ZTVN4brls14PSPreRecordingE
- __ZTVN4brls15EvtVTSMDisabledE
- __ZTVN4brls16EvtInternalResetE
- __ZTVN4brls16EvtStopRecordingE
- __ZTVN4brls17EvtPSCheckStartIOE
- __ZTVN4brls17EvtStartRecordingE
- __ZTVN4brls18RecordingWithoutPSE
- __ZTVN4brls19EvtPSStopSecondPassE
- __ZTVN4brls20EvtPreStartRecordingE
- __ZTVN4brls20PhraseSpotterRunningE
- __ZTVN4brls21EvtStartRecordTimeoutE
- __ZTVN4brls3FSME
- __ZTVN4brls5ResetE
- __ZTVN4brls7PSResetE
- __ZTVN4brls9QuiescentE
- __ZTVN5boost10statechart12simple_stateIN4brls10AOPRunningENS2_3FSMENS_3mpl4listIN4mpl_2naES8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_EELNS0_12history_modeE0EEE
- __ZTVN5boost10statechart12simple_stateIN4brls11PSAnalyzingENS2_20PhraseSpotterRunningENS_3mpl4listIN4mpl_2naES8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_EELNS0_12history_modeE0EEE
- __ZTVN5boost10statechart12simple_stateIN4brls11PSRecordingENS2_20PhraseSpotterRunningENS_3mpl4listIN4mpl_2naES8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_EELNS0_12history_modeE0EEE
- __ZTVN5boost10statechart12simple_stateIN4brls13PSAwaitRecordENS2_20PhraseSpotterRunningENS_3mpl4listIN4mpl_2naES8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_EELNS0_12history_modeE0EEE
- __ZTVN5boost10statechart12simple_stateIN4brls14PSPreRecordingENS2_20PhraseSpotterRunningENS_3mpl4listIN4mpl_2naES8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_EELNS0_12history_modeE0EEE
- __ZTVN5boost10statechart12simple_stateIN4brls18RecordingWithoutPSENS2_3FSMENS_3mpl4listIN4mpl_2naES8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_EELNS0_12history_modeE0EEE
- __ZTVN5boost10statechart12simple_stateIN4brls20PhraseSpotterRunningENS2_3FSMENS2_11PSAnalyzingELNS0_12history_modeE0EEE
- __ZTVN5boost10statechart12simple_stateIN4brls5ResetENS2_3FSMENS_3mpl4listIN4mpl_2naES8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_EELNS0_12history_modeE0EEE
- __ZTVN5boost10statechart12simple_stateIN4brls7PSResetENS2_20PhraseSpotterRunningENS_3mpl4listIN4mpl_2naES8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_EELNS0_12history_modeE0EEE
- __ZTVN5boost10statechart12simple_stateIN4brls9QuiescentENS2_3FSMENS_3mpl4listIN4mpl_2naES8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_EELNS0_12history_modeE0EEE
- __ZTVN5boost10statechart13state_machineIN4brls3FSMENS2_5ResetENSt3__19allocatorINS0_4noneEEENS0_25null_exception_translatorEEE
- __ZTVN5boost10statechart5stateIN4brls11PSAnalyzingENS2_20PhraseSpotterRunningENS_3mpl4listIN4mpl_2naES8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_EELNS0_12history_modeE0EEE
- __ZTVN5boost10statechart5stateIN4brls11PSRecordingENS2_20PhraseSpotterRunningENS_3mpl4listIN4mpl_2naES8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_EELNS0_12history_modeE0EEE
- __ZTVN5boost10statechart5stateIN4brls13PSAwaitRecordENS2_20PhraseSpotterRunningENS_3mpl4listIN4mpl_2naES8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_EELNS0_12history_modeE0EEE
- __ZTVN5boost10statechart5stateIN4brls14PSPreRecordingENS2_20PhraseSpotterRunningENS_3mpl4listIN4mpl_2naES8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_EELNS0_12history_modeE0EEE
- __ZTVN5boost10statechart5stateIN4brls7PSResetENS2_20PhraseSpotterRunningENS_3mpl4listIN4mpl_2naES8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_S8_EELNS0_12history_modeE0EEE
- __ZTVN5caulk10concurrent7details12message_callIRZN11ClientEntry19handleSequenceEndedEmNSt3__18functionIFvmEEEE3$_0JEEE
- __ZTVN5caulk10concurrent7details15rt_message_callIRZN11ClientEntry19handleSequenceEndedEmNSt3__18functionIFvmEEEE3$_0JEEE
- __ZTVNSt3__110__function6__funcINS_6__bindIRFN5caulk8expectedINS_10unique_ptrIN14MixTapToUplink12TapConnectorENS_14default_deleteIS7_EEEEiEERS6_NS_13unordered_mapIjiNS_4hashIjEENS_8equal_toIjEENS_9allocatorINS_4pairIKjiEEEEEEEJRKNS_12placeholders4__phILi1EEERKNSR_ILi2EEEEEENSI_ISY_EEFSB_SC_RKSN_EEE
- __ZTVNSt3__110__function6__funcIU8__strongU13block_pointerFvmENS_9allocatorIS4_EES2_EE
- __ZTVNSt3__110__function6__funcIU8__strongU13block_pointerFvvENS_9allocatorIS4_EES2_EE
- __ZTVNSt3__110__function6__funcIZ25AudioSessionSetCMPropertyE3$_0NS_9allocatorIS2_EEFNS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS3_IcEEEESA_EEN10applesauce2CF7TypeRefESE_EEE
- __ZTVNSt3__110__function6__funcIZ27TranslateCMSessionErrorCodePKcRKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEiiE3$_0NS7_ISC_EEFNS_4pairIS9_S9_EEN10applesauce2CF7TypeRefESI_EEE
- __ZTVNSt3__110__function6__funcIZ29SystemSoundServerPlayActionIDE3$_0NS_9allocatorIS2_EEFvvEEE
- __ZTVNSt3__110__function6__funcIZ62-[AVHapticServer incrementRunningCountForAudio:haptics:entry:]E3$_1NS_9allocatorIS2_EEFivEEE
- __ZTVNSt3__110__function6__funcIZN10AQMEIO_HAL13UpdateStreamsEvE3$_1NS_9allocatorIS3_EEFbRK26AudioObjectPropertyAddressEEE
- __ZTVNSt3__110__function6__funcIZN11ClientEntry17doPrepareSequenceENS_10shared_ptrI14HapticSequenceEENS_8functionIFvmEEEE3$_0NS_9allocatorIS9_EES7_EE
- __ZTVNSt3__110__function6__funcIZN13MESubmixGraph19attach1MixerChannelEP14MEMixerChannelE3$_1NS_9allocatorIS5_EEFvvEEE
- __ZTVNSt3__110__function6__funcIZN13ServerManager12DoRenderProcERK14AudioTimeStampjE3$_1NS_9allocatorIS6_EEFKNS2_12SynthCommandEvEEE
- __ZTVNSt3__110__function6__funcIZN13ServerManager16playAlertPatternENS_10shared_ptrI11ClientEntryEEPKvfP20SSPlayerSynchronizerjNS_8functionIFvvEEEE3$_0NS_9allocatorISD_EEFvmEEE
- __ZTVNSt3__110__function6__funcIZN15AQMixEngine_VAD17maintainVADevicesEbE3$_2NS_9allocatorIS3_EEFbR14AQIONodeClientEEE
- __ZTVNSt3__110__function6__funcIZN15AQMixEngine_VAD28routeSupportsEnhanceDialogueEvE3$_0NS_9allocatorIS3_EEFvR10AQMEDeviceEEE
- __ZTVNSt3__110__function6__funcIZN15AQMixEngine_VAD31IsOwnerOfAudioObject_DeprecatedEjEUlR10AQMEDeviceE_NS_9allocatorIS5_EEFvS4_EEE
- __ZTVNSt3__110__function6__funcIZN15AQMixEngine_VAD37SetAudioObjectPropertyData_DeprecatedEjRK26AudioObjectPropertyAddressjPKvjS7_EUlR10AQMEDeviceE_NS_9allocatorISA_EEFvS9_EEE
- __ZTVNSt3__110__function6__funcIZN16AQMixEngine_Base10DebugPrintEP7__sFILEPKcE3$_0NS_9allocatorIS7_EEFvR10AQMEDeviceEEE
- __ZTVNSt3__110__function6__funcIZN16AQMixEngine_Base12maintainTapsEbEUlR10AQMEDeviceE_NS_9allocatorIS5_EEFvS4_EEE
- __ZTVNSt3__110__function6__funcIZN16AQMixEngine_Base13silenceOutputERK11AQMESessionjEUlR10AQMEDeviceE_NS_9allocatorIS8_EEFvS7_EEE
- __ZTVNSt3__110__function6__funcIZN16AQMixEngine_Base16StopFreewheelingEvEUlR10AQMEDeviceE_NS_9allocatorIS5_EEFvS4_EEE
- __ZTVNSt3__110__function6__funcIZN16AQMixEngine_Base17SoundCheckChangedEvEUlR10AQMEDeviceE_NS_9allocatorIS5_EEFvS4_EEE
- __ZTVNSt3__110__function6__funcIZN16AQMixEngine_Base18setDynamicsEnabledE15EDynamicsEnableEUlR10AQMEDeviceE_NS_9allocatorIS6_EEFvS5_EEE
- __ZTVNSt3__110__function6__funcIZN16AQMixEngine_Base23MonoAudioSettingChangedEvEUlR10AQMEDeviceE_NS_9allocatorIS5_EEFvS4_EEE
- __ZTVNSt3__110__function6__funcIZN16AQMixEngine_Base25AccessibilityPrefsChangedEvEUlR10AQMEDeviceE_NS_9allocatorIS5_EEFvS4_EEE
- __ZTVNSt3__110__function6__funcIZN16AQMixEngine_Base25ScreenSharingStateChangedEyEUlR10AQMEDeviceE_NS_9allocatorIS5_EEFvS4_EEE
- __ZTVNSt3__110__function6__funcIZN16AQMixEngine_Base27DistributeProcessorPropertyE13MEProcessorIDjRjPvEUlR10AQMEDeviceE_NS_9allocatorIS8_EEFvS7_EEE
- __ZTVNSt3__110__function6__funcIZN16AQMixEngine_Base29RestartIOFollowingRouteChangeEvEUlR10AQMEDeviceE_NS_9allocatorIS5_EEFvS4_EEE
- __ZTVNSt3__110__function6__funcIZN17BorealisManagerV210InitializeEvE3$_1NS_9allocatorIS3_EEFbjRKN15CAListenerProxy15HALNotificationEEEE
- __ZTVNSt3__110__function6__funcIZN17LegacyHapticSynth19handleRunModeChangeEjE3$_1NS_9allocatorIS3_EEFivEEE
- __ZTVNSt3__110__function6__funcIZN18BorealisServerImpl27enableVoiceTriggerListeningEbbU13block_pointerFvP7NSErrorEEUljRKN15CAListenerProxy15HALNotificationEE_NS_9allocatorISB_EEFbjSA_EEE
- __ZTVNSt3__110__function6__funcIZN18BorealisServerImpl31updateVoiceTriggerConfigurationEPK14__CFDictionaryU13block_pointerFvP7NSErrorEEUljRKN15CAListenerProxy15HALNotificationEE_NS_9allocatorISE_EEFbjSD_EEE
- __ZTVNSt3__110__function6__funcIZN18BorealisServerImpl40registerStateChangedNotificationHandlersEbEUljRKN15CAListenerProxy15HALNotificationEE_NS_9allocatorIS7_EEFbjS6_EEE
- __ZTVNSt3__110__function6__funcIZN18BorealisServerImpl42registerAOPVoiceTriggerNotificationHandlerEjbEUljRKN15CAListenerProxy15HALNotificationEE_NS_9allocatorIS7_EEFbjS6_EEE
- __ZTVNSt3__110__function6__funcIZN18BorealisServerImpl43registerAOPEnableChangedNotificationHandlerEbEUljRKN15CAListenerProxy15HALNotificationEE_NS_9allocatorIS7_EEFbjS6_EEE
- __ZTVNSt3__110__function6__funcIZN20DSP_Routing_Borealis3AOP35registerAOPVoiceTriggerNotificationEbE3$_0NS_9allocatorIS4_EEFbjRKN15CAListenerProxy15HALNotificationEEEE
- __ZTVNSt3__110__function6__funcIZN20DSP_Routing_Borealis3AOP45updateFirstPassModelOnAOPAndWaitForCompletionEvE3$_0NS_9allocatorIS4_EEFbjRKN15CAListenerProxy15HALNotificationEEEE
- __ZTVNSt3__110__function6__funcIZN22MultiOutputHapticSynth12startRunningEbbjNS_8functionIFivEEEjE3$_1NS_9allocatorIS6_EES4_EE
- __ZTVNSt3__110__function6__funcIZN22MultiOutputHapticSynth19handleRunModeChangeEjE3$_3NS_9allocatorIS3_EEFivEEE
- __ZTVNSt3__110__function6__funcIZN2AQ3API7ManagerC1EbRNS3_11CaptureBaseEN5caulk19lifetime_erased_ptrI23AudioQueueXPC_InterfaceEEE3$_0NS_9allocatorISB_EEFiN10applesauce3xpc6objectEEEE
- __ZTVNSt3__110__function6__funcIZN2AQ3API7ManagerC1EbRNS3_11CaptureBaseEN5caulk19lifetime_erased_ptrI23AudioQueueXPC_InterfaceEEE3$_1NS_9allocatorISB_EEFvRN4swix12ipc_endpointERKN10applesauce3xpc6objectEEEE
- __ZTVNSt3__110__function6__funcIZZN13MESubmixGraph19attach1MixerChannelEP14MEMixerChannelENK3$_0clI9TapSubmixEEDaRT_EUlvE_NS_9allocatorISB_EEFvvEEE
- __ZTVNSt3__110__function6__funcIZZN14RemoteIOClient20IONode_FormatChangedEjEUb_E3$_0NS_9allocatorIS3_EEFvvEEE
- __ZTVNSt3__110__function6__funcIZZN22MultiOutputHapticSynth11stopRunningEbbjENK3$_3clERNS_10unique_ptrI11SynthOutputNS_14default_deleteIS5_EEEEEUlvE_NS_9allocatorISA_EEFvvEEE
- __ZTVNSt3__120__shared_ptr_emplaceIN12CADeprecated16XMachReceivePortENS_9allocatorIS2_EEEE
- __ZTVNSt3__120__shared_ptr_emplaceIN5caulk12synchronizedIN2AQ6Server16ProcessingTapIPCENS1_4mach11unfair_lockENS1_22empty_atomic_interfaceIS5_EEEENS_9allocatorISA_EEEE
- __ZTVNSt3__120__shared_ptr_pointerIP14AQRemoteClientNS1_11NoOpDeleterENS_9allocatorIS1_EEEE
- __ZTVNSt3__120__shared_ptr_pointerIPxZL22getCAReporterIDForCallvE3$_0NS_9allocatorIxEEEE
- __ZThn112_N15AudioQueueOwner11PrintObjectEP7__sFILE
- __ZThn112_N15AudioQueueOwnerD0Ev
- __ZThn112_N15AudioQueueOwnerD1Ev
- __ZThn144_N20DSP_Routing_Borealis11PrintObjectEP7__sFILE
- __ZThn144_N20DSP_Routing_BorealisD0Ev
- __ZThn144_N20DSP_Routing_BorealisD1Ev
- __ZThn16_N14AQRemoteClient13queueDisposedEj
- __ZThn16_N14AQRemoteClient35IssueNotificationsAvailableCallbackEj
- __ZThn16_N14AQRemoteClient36InvokeSubmixTapFormatChangedCallbackEj
- __ZThn16_N14AQRemoteClientD0Ev
- __ZThn16_N14AQRemoteClientD1Ev
- __ZThn16_N16ClientAudioQueueD0Ev
- __ZThn16_N16ClientAudioQueueD1Ev
- __ZThn16_N8AQServer10ClientDiedEPN12CADeprecated11XMachServer6ClientE
- __ZThn16_N8AQServerD0Ev
- __ZThn16_N8AQServerD1Ev
- __ZThn32_N16ClientAudioQueueD0Ev
- __ZThn32_N16ClientAudioQueueD1Ev
- __ZThn344_N16AudioQueueObject18ToAudioQueueObjectEv
- __ZThn344_N16AudioQueueObjectD0Ev
- __ZThn344_N16AudioQueueObjectD1Ev
- __ZThn344_N17ZenAQIONodeClient11PrintObjectEP7__sFILE
- __ZThn344_N17ZenAQIONodeClientD0Ev
- __ZThn344_N17ZenAQIONodeClientD1Ev
- __ZThn360_N16AudioQueueObject21SSP_StartTimeResolvedEx15XAudioTimeStamp
- __ZThn360_N16AudioQueueObject30SSP_ScaledToUnscaledSampleTimeEx
- __ZThn360_N16AudioQueueObjectD0Ev
- __ZThn360_N16AudioQueueObjectD1Ev
- __ZThn400_N14AQOfflineMixer11PrintObjectEP7__sFILE
- __ZThn400_N14AQOfflineMixerD0Ev
- __ZThn400_N14AQOfflineMixerD1Ev
- __ZThn80_N14RemoteIOServerD0Ev
- __ZThn80_N14RemoteIOServerD1Ev
- __ZThn8_N14MEMixerChannel11SetSTSLabelERKN10applesauce2CF9StringRefE
- __ZThn8_N14MEMixerChannel17AddProcessingNodeERK16AQProcessingNode
- __ZThn96_N8AQServerD0Ev
- __ZThn96_N8AQServerD1Ev
- __ZZ13AQMEMessengervE6global
- __ZZ13AQMEMessengervENK3$_0clEv
- __ZZ24AQMEIOManager_FindIOUnitRK14AQMEIO_BindingE15sharedInstances
- __ZZ32FeatureFlags_IsOffloadACQEnabledvE20sIsOffloadACQEnabled
- __ZZL15CPMSLibraryCorePPcE16frameworkLibrary.0.3113
- __ZZL15CPMSLibraryCorePPcE16frameworkLibrary.0.5559
- __ZZL15CPMSLibraryCorePPcE16frameworkLibrary.0.9555
- __ZZL17getCPMSAgentClassvE9softClass.0.3084
- __ZZL17getCPMSAgentClassvE9softClass.0.5557
- __ZZL20CoreMediaLibraryCorePPcE16frameworkLibrary.0.4375
- __ZZL20CoreMediaLibraryCorePPcE16frameworkLibrary.0.6322
- __ZZL21getAVAudioFormatClassvE9softClass.0.10939
- __ZZL23MediaToolboxLibraryCorePPcE16frameworkLibrary.0.6314
- __ZZL29AudioSessionServerLibraryCorePPcE16frameworkLibrary.0.7525
- __ZZL29getCPMSClientDescriptionClassvE9softClass.0.3093
- __ZZL33SetOwnerSessionAndUpdatePlayStateR16AudioQueueObjectRK11AQMESessionENK3$_0clE29AVAudioSessionClientPlayState
- __ZZL33getCMBaseObjectGetVTableSymbolLocvE3ptr.0.4371
- __ZZL33getCMBaseObjectGetVTableSymbolLocvE3ptr.0.6319
- __ZZL34PopulateSourceFormatInfoDictionaryP14__CFDictionaryPKvRK14AQIONodeClientRN2CA17StreamDescriptionEbbbE10sessionMap
- __ZZL58getFigCPECryptorCreateCryptorFromSerializedRecipeSymbolLocvE3ptr.0.6310
- __ZZN10AQMEIO_HAL6IOProcEPK15AudioBufferListPK14AudioTimeStampPS0_S5_E14isVirtualAudio
- __ZZN13ServerManager16playAlertPatternENSt3__110shared_ptrI11ClientEntryEEPKvfP20SSPlayerSynchronizerjNS0_8functionIFvvEEEEN3$_0D1Ev
- __ZZN14MixTapToUplink9CreateTapERKNSt3__113unordered_mapIjiNS0_4hashIjEENS0_8equal_toIjEENS0_9allocatorINS0_4pairIKjiEEEEEEE5gOnce
- __ZZN15AQMixEngine_VAD17maintainVADevicesEbENK3$_3clERNS_10MEVADeviceER17MEConnectorVector
- __ZZN15BorealisManager19checkEnabledEffectsEvE4once
- __ZZN15BorealisManager28hardwareSupportsVoiceTriggerEvE9checkonce
- __ZZN16AQMixEngine_Base10DebugPrintEP7__sFILEPKcE14sLogEntryIndex
- __ZZN16AQMixEngine_Base10DebugPrintEP7__sFILEPKcE5mutex
- __ZZN16ClientAudioQueueC1EbRKN2AQ3API13QueueCallbackERK16CACallbackTargetRK27AudioStreamBasicDescriptionE14callbackThread
- __ZZN17BorealisManagerV210InitializeEvENK3$_0clEv
- __ZZN17BorealisManagerV214hasBorealisXPCEvE4once
- __ZZN17BorealisManagerV28instanceEvE8instance
- __ZZN18BorealisServerImpl17enableBargeInModeEbU13block_pointerFvP7NSErrorEE6sCount
- __ZZN18BorealisServerImpl33fetchHardwareSupportsVoiceTriggerEvE9checkonce
- __ZZN20CA_UISoundClientBaseC1EdjPK14__CFDictionaryjE11gSRCQuality
- __ZZN20CA_UISoundClientBaseC1EdjPK14__CFDictionaryjE6inited
- __ZZN20CA_UISoundClientBaseC1EdjPK14__CFDictionaryjE8onceflag
- __ZZN20DSP_Routing_BorealisC1ER10AQMEIO_DSPE29borealisCaptureRingBufferMode
- __ZZN22MultiOutputHapticSynth11stopRunningEbbjENK3$_1clERNSt3__110unique_ptrI11SynthOutputNS1_14default_deleteIS3_EEEE
- __ZZN2AQ3API9Interface15defaultInstanceEiE6legacy
- __ZZN2AQ3API9SubmixTap41CreateDestinationAQProcessingTap_CMClientEvEN3$_08__invokeEPvP29OpaqueAudioQueueProcessingTapjP14AudioTimeStampPjS8_P15AudioBufferList
- __ZZN2AQ6Server4Base15defaultInstanceEiRN2AT9MixServer4BaseEE6legacy
- __ZZN5caulk23inplace_function_detail6vtableIvJRKNS_10concurrent7details13skiplist_nodeIPvNS_5alloc6detail13tracked_blockEE9layout_vkEEEC1EvENUlS5_E_8__invokeES5_
- __ZZN5caulk23inplace_function_detail6vtableIvJRKNS_10concurrent7details13skiplist_nodeIPvNS_5alloc6detail13tracked_blockEE9layout_vkEEEC1EvENUlS5_S5_E0_8__invokeES5_S5_
- __ZZN5caulk23inplace_function_detail6vtableIvJRKNS_10concurrent7details13skiplist_nodeIPvNS_5alloc6detail13tracked_blockEE9layout_vkEEEC1EvENUlS5_S5_E_8__invokeES5_S5_
- __ZZN5caulk23inplace_function_detail6vtableIvJRKNS_10concurrent7details13skiplist_nodeIPvNS_5alloc6detail13tracked_blockEE9layout_vkEEEC1EvENUlS5_SC_E_8__invokeES5_SC_
- __ZZNK15AQMixEngine_VAD24includeDeviceInSystemTapERK10AQMEDeviceENK3$_0clEjRj
- __ZZZN11SSServerIPCC1EvENK3$_0clEvENKUlyPKcS2_S2_E_clEyS2_S2_S2_
- __ZZZN14MEInputManager22DetachInputDispatchersER17MEConnectorVectorRK17MEDetachSpecifierENK3$_0clERNSt3__16vectorIP15InputDispatcherNS6_9allocatorIS9_EEEEENKUlPT_E_clIS8_EEDaSF_
- ___100-[AVHapticServer(VibeSynthEngine) playVibePattern:gain:synchronizer:flags:atTime:completionHandler:]_block_invoke.316
- ___100-[AVHapticServer(VibeSynthEngine) playVibePattern:gain:synchronizer:flags:atTime:completionHandler:]_block_invoke.319
- ___22-[AVHapticServer init]_block_invoke.372
- ___24-[AVBorealisServer init]_block_invoke
- ___37-[AVBorealisServer portsActiveReply:]_block_invoke
- ___44-[AVBorealisServer speakerStateActiveReply:]_block_invoke
- ___48-[AVBorealisServerHysteresisNotifier sendState:]_block_invoke
- ___49-[AVBorealisServer enableListeningOnPorts:reply:]_block_invoke
- ___49-[AVBorealisServer siriClientRecordStateChanged:]_block_invoke
- ___53-[AVHapticServer listener:shouldAcceptNewConnection:]_block_invoke.437
- ___53-[AVHapticServer listener:shouldAcceptNewConnection:]_block_invoke.441
- ___53-[AVHapticServer listener:shouldAcceptNewConnection:]_block_invoke.442
- ___54-[AVBorealisServer enableSpeakerStateListening:reply:]_block_invoke
- ___54-[AVHapticServerInstance prepareHapticSequence:reply:]_block_invoke
- ___54-[AVHapticServerInstance prepareHapticSequence:reply:]_block_invoke_2
- ___55-[AVBorealisServer listener:shouldAcceptNewConnection:]_block_invoke
- ___55-[AVBorealisServer listener:shouldAcceptNewConnection:]_block_invoke.169
- ___55-[AVBorealisServer listener:shouldAcceptNewConnection:]_block_invoke.170
- ___55-[AVBorealisServer listener:shouldAcceptNewConnection:]_block_invoke_2
- ___55-[AVBorealisServer listener:shouldAcceptNewConnection:]_block_invoke_2.171
- ___58-[AVBorealisServerPortManager notifyStateChanged:onQueue:]_block_invoke
- ___58-[AVBorealisServerPortManager notifyStateChanged:onQueue:]_block_invoke_2
- ___65-[AVHapticServerInstance setupAudioSessionFromID:isShared:error:]_block_invoke.39
- ___68-[AVBorealisServer sendVoiceTriggerOccuredNotification:triggerTime:]_block_invoke
- ___AQServer_DisposeQueue_block_invoke
- ___AQServer_MixerConnectQueue_block_invoke
- ___AQServer_Pause_block_invoke
- ___AQServer_Prime_block_invoke
- ___AQServer_SetOfflineRenderFormat_block_invoke
- ___AQServer_Start_block_invoke
- ___AQServer_Stop_block_invoke
- ___AudioSessionCreateCoreMXSession_block_invoke
- ___AudioSessionGetPrimaryAudioSessionIDForAuditToken_block_invoke
- ___Block_byref_object_copy_.11062
- ___Block_byref_object_copy_.13279
- ___Block_byref_object_copy_.1407
- ___Block_byref_object_copy_.1560
- ___Block_byref_object_copy_.3167
- ___Block_byref_object_copy_.3725
- ___Block_byref_object_copy_.4960
- ___Block_byref_object_copy_.6645
- ___Block_byref_object_dispose_.11063
- ___Block_byref_object_dispose_.13280
- ___Block_byref_object_dispose_.1408
- ___Block_byref_object_dispose_.1561
- ___Block_byref_object_dispose_.3168
- ___Block_byref_object_dispose_.3726
- ___Block_byref_object_dispose_.4961
- ___Block_byref_object_dispose_.6646
- ____Z16NewAudioCapturer20AudioCapturerOptionsPKcS1_jPK27AudioStreamBasicDescriptionRS3__block_invoke.11518
- ____Z16NewAudioCapturer20AudioCapturerOptionsPKcS1_jPK27AudioStreamBasicDescriptionRS3__block_invoke.11640
- ____Z16NewAudioCapturer20AudioCapturerOptionsPKcS1_jPK27AudioStreamBasicDescriptionRS3__block_invoke.11874
- ____Z16NewAudioCapturer20AudioCapturerOptionsPKcS1_jPK27AudioStreamBasicDescriptionRS3__block_invoke.12013
- ____Z16NewAudioCapturer20AudioCapturerOptionsPKcS1_jPK27AudioStreamBasicDescriptionRS3__block_invoke.1722
- ____Z16NewAudioCapturer20AudioCapturerOptionsPKcS1_jPK27AudioStreamBasicDescriptionRS3__block_invoke.3289
- ____Z16NewAudioCapturer20AudioCapturerOptionsPKcS1_jPK27AudioStreamBasicDescriptionRS3__block_invoke.5592
- ____Z16NewAudioCapturer20AudioCapturerOptionsPKcS1_jPK27AudioStreamBasicDescriptionRS3__block_invoke.7756
- ____Z16NewAudioCapturer20AudioCapturerOptionsPKcS1_jPK27AudioStreamBasicDescriptionRS3__block_invoke.8469
- ____Z28AudioStatisticsLibraryLoaderv_block_invoke.2302
- ____Z28AudioStatisticsLibraryLoaderv_block_invoke.7992
- ____Z28CMClientNotificationCallbackP26opaqueCMNotificationCenterPKvPK10__CFStringS2_S2__block_invoke.35
- ____Z29AQServer_Local_AllocateBufferjRPvjRP28AudioStreamPacketDescriptionjPj_block_invoke
- ____ZL15CPMSLibraryCorePPc_block_invoke.3114
- ____ZL15CPMSLibraryCorePPc_block_invoke.5560
- ____ZL15CPMSLibraryCorePPc_block_invoke.9556
- ____ZL17OnAudioQueueQueueU13block_pointerFivE_block_invoke
- ____ZL17getCPMSAgentClassv_block_invoke.3085
- ____ZL17getCPMSAgentClassv_block_invoke.5558
- ____ZL20CoreMediaLibraryCorePPc_block_invoke.4376
- ____ZL20CoreMediaLibraryCorePPc_block_invoke.6323
- ____ZL21getAVAudioFormatClassv_block_invoke.10940
- ____ZL23MediaToolboxLibraryCorePPc_block_invoke.6315
- ____ZL29AudioSessionServerLibraryCorePPc_block_invoke.7526
- ____ZL29getCPMSClientDescriptionClassv_block_invoke.3094
- ____ZL33getCMBaseObjectGetVTableSymbolLocv_block_invoke.4372
- ____ZL33getCMBaseObjectGetVTableSymbolLocv_block_invoke.6320
- ____ZL58getFigCPECryptorCreateCryptorFromSerializedRecipeSymbolLocv_block_invoke.6311
- ____ZN14DSP_Routing_VPC2ER10AQMEIO_DSPN11DSP_Routing12ERoutingTypeERKNSt3__16vectorI14MEStreamTypeIDNS4_9allocatorIS6_EEEEb_block_invoke.12
- ____ZN14DSP_Routing_VPC2ER10AQMEIO_DSPN11DSP_Routing12ERoutingTypeERKNSt3__16vectorI14MEStreamTypeIDNS4_9allocatorIS6_EEEEb_block_invoke.8
- ____ZN14DSP_Routing_VPC2ER10AQMEIO_DSPN11DSP_Routing12ERoutingTypeERKNSt3__16vectorI14MEStreamTypeIDNS4_9allocatorIS6_EEEEb_block_invoke_2.15
- ____ZN14MEMixerChannel11SetSTSLabelERKN10applesauce2CF9StringRefE_block_invoke
- ____ZN14MixTapToUplink9CreateTapERKNSt3__113unordered_mapIjiNS0_4hashIjEENS0_8equal_toIjEENS0_9allocatorINS0_4pairIKjiEEEEEE_block_invoke
- ____ZN15BorealisManager19checkEnabledEffectsEv_block_invoke
- ____ZN15BorealisManager19checkEnabledEffectsEv_block_invoke.87
- ____ZN15BorealisManager19checkEnabledEffectsEv_block_invoke_2
- ____ZN15BorealisManager28hardwareSupportsVoiceTriggerEv_block_invoke
- ____ZN15BorealisManagerC2Ev_block_invoke
- ____ZN15BorealisManagerC2Ev_block_invoke.71
- ____ZN16SSSystemListener28MXSessionNotificationHandlerEP26opaqueCMNotificationCenterPKvPK10__CFStringS3_S3__block_invoke.23
- ____ZN17BorealisManagerV214hasBorealisXPCEv_block_invoke
- ____ZN18BorealisServerImpl10InitializeEv_block_invoke
- ____ZN18BorealisServerImpl10InitializeEv_block_invoke.310
- ____ZN18BorealisServerImpl10InitializeEv_block_invoke.312
- ____ZN18BorealisServerImpl10InitializeEv_block_invoke_2
- ____ZN18BorealisServerImpl10InitializeEv_block_invoke_2.313
- ____ZN18BorealisServerImpl12isPortActiveEmU13block_pointerFvbP7NSErrorE_block_invoke
- ____ZN18BorealisServerImpl12speakerMutedEU13block_pointerFvbP7NSErrorE_block_invoke
- ____ZN18BorealisServerImpl17enableBargeInModeEbU13block_pointerFvP7NSErrorE_block_invoke
- ____ZN18BorealisServerImpl21activateSecureSessionEbU13block_pointerFvP7NSErrorE_block_invoke
- ____ZN18BorealisServerImpl21listeningEnabledReplyEU13block_pointerFvbP7NSErrorE_block_invoke
- ____ZN18BorealisServerImpl25siriClientsRecordingReplyEU13block_pointerFvmP7NSErrorE_block_invoke
- ____ZN18BorealisServerImpl25speechDetectionVADCreatedEv_block_invoke
- ____ZN18BorealisServerImpl33fetchHardwareSupportsVoiceTriggerEv_block_invoke
- ____ZN18BorealisServerImpl40registerStateChangedNotificationHandlersEb_block_invoke
- ____ZN18BorealisServerImplC2EP16AVBorealisServer_block_invoke
- ____ZN18BorealisServerImplC2EP16AVBorealisServer_block_invoke_2
- ____ZN18BorealisServerImplC2EP16AVBorealisServer_block_invoke_3
- ____ZN18MixTapToUplinkHost29EnableMixTapToTelephonyUplinkERKNSt3__113unordered_mapIjiNS0_4hashIjEENS0_8equal_toIjEENS0_9allocatorINS0_4pairIKjiEEEEEE_block_invoke
- ____ZN20MEOutputStreamClientC2ER10AQMEDevice14MEStreamTypeID15EDynamicsEnable_block_invoke
- ____ZN26MutedSpeechActivityManager4Impl35GetProxyMutedSpeechActivityListenerENS0_10ClientTypeE_block_invoke
- ____ZN2AQ3API10LegacyImpl13AudioQueueNewEbPK27AudioStreamBasicDescriptionRKNS0_13QueueCallbackERK16CACallbackTargetjjPP16OpaqueAudioQueue_block_invoke
- ____ZN2AT13DispatchBlockEP16dispatch_queue_sU13block_pointerFvvEbPKcS5_iyy_block_invoke.12541
- ____ZN2AT13DispatchBlockEP16dispatch_queue_sU13block_pointerFvvEbPKcS5_iyy_block_invoke.2559
- ____ZN2AT13DispatchBlockEP16dispatch_queue_sU13block_pointerFvvEbPKcS5_iyy_block_invoke.2914
- ____ZN2AT13DispatchBlockEP16dispatch_queue_sU13block_pointerFvvEbPKcS5_iyy_block_invoke.4191
- ____ZN2AT13DispatchBlockEP16dispatch_queue_sU13block_pointerFvvEbPKcS5_iyy_block_invoke.6259
- ____ZN2AT13DispatchBlockEP16dispatch_queue_sU13block_pointerFvvEbPKcS5_iyy_block_invoke.6775
- ____ZN2AT13DispatchBlockEP16dispatch_queue_sU13block_pointerFvvEbPKcS5_iyy_block_invoke.7840
- ____ZN2AT13DispatchBlockEP16dispatch_queue_sU13block_pointerFvvEbPKcS5_iyy_block_invoke.8818
- ____ZN2AT13DispatchBlockEP16dispatch_queue_sU13block_pointerFvvEbPKcS5_iyy_block_invoke.9844
- ____ZN2AT13DispatchBlockEPU28objcproto17OS_dispatch_queue8NSObjectU13block_pointerFvvEbPKcS6_iyy_block_invoke.6274
- ____ZN4brls20PhraseSpotterRunning22checkInitPhraseSpotterEv_block_invoke
- ____ZN4brls3FSM10asyncEventINS_19EvtPSStopSecondPassEEEvjT__block_invoke
- ____ZN4brls3FSM10asyncEventINS_21EvtStartRecordTimeoutEEEvjT__block_invoke
- ____ZZN17BorealisManagerV210InitializeEvENK3$_0clEv_block_invoke
- ____ZZN18BorealisServerImpl27enableVoiceTriggerListeningEbbU13block_pointerFvP7NSErrorEENKUljRKN15CAListenerProxy15HALNotificationEE_clEjS7__block_invoke
- ____ZZN18BorealisServerImpl31updateVoiceTriggerConfigurationEPK14__CFDictionaryU13block_pointerFvP7NSErrorEENKUljRKN15CAListenerProxy15HALNotificationEE_clEjSA__block_invoke
- ____ZZN18BorealisServerImpl40registerStateChangedNotificationHandlersEbENKUljRKN15CAListenerProxy15HALNotificationEE_clEjS3__block_invoke
- ____ZZN18BorealisServerImpl42registerAOPVoiceTriggerNotificationHandlerEjbENKUljRKN15CAListenerProxy15HALNotificationEE_clEjS3__block_invoke
- ___block_descriptor_104_ea8_32s40s48s56r64r_e17_v16?0"NSError"8ls32l8r56l8s40l8r64l8s48l8
- ___block_descriptor_32_e9_v16?0^v8l
- ___block_descriptor_40_e11_v24?0q8Q16l
- ___block_descriptor_41_e9_v16?0^v8l
- ___block_descriptor_42_e9_v16?0^v8l
- ___block_descriptor_48_ea8_32w_e8_v16?0Q8lw32l8
- ___block_descriptor_49_e8_32r_e9_v16?0^v8lr32l8
- ___block_descriptor_53_e8_32r_e9_v16?0^v8lr32l8
- ___block_descriptor_56_e8_32r_e9_v16?0^v8lr32l8
- ___block_descriptor_60_e8_32c32_ZTSN4brls19EvtPSStopSecondPassE_e5_v8?0l
- ___block_descriptor_60_e8_32c34_ZTSN4brls21EvtStartRecordTimeoutE_e5_v8?0l
- ___block_descriptor_64_e9_v16?0^v8l
- ___block_descriptor_68_ea8_32r_e5_v8?0lr32l8
- ___block_descriptor_tmp.1.11706
- ___block_descriptor_tmp.10.10758
- ___block_descriptor_tmp.10.11997
- ___block_descriptor_tmp.10.4297
- ___block_descriptor_tmp.10.9853
- ___block_descriptor_tmp.101.13285
- ___block_descriptor_tmp.103
- ___block_descriptor_tmp.10500
- ___block_descriptor_tmp.1082
- ___block_descriptor_tmp.11.12542
- ___block_descriptor_tmp.11.4202
- ___block_descriptor_tmp.11.8816
- ___block_descriptor_tmp.11308
- ___block_descriptor_tmp.11454
- ___block_descriptor_tmp.11516
- ___block_descriptor_tmp.11584
- ___block_descriptor_tmp.11698
- ___block_descriptor_tmp.12.4294
- ___block_descriptor_tmp.12.4419
- ___block_descriptor_tmp.12.9860
- ___block_descriptor_tmp.12032
- ___block_descriptor_tmp.12248
- ___block_descriptor_tmp.1246
- ___block_descriptor_tmp.12538
- ___block_descriptor_tmp.13.10760
- ___block_descriptor_tmp.13291
- ___block_descriptor_tmp.151.13282
- ___block_descriptor_tmp.156.13281
- ___block_descriptor_tmp.1562
- ___block_descriptor_tmp.16
- ___block_descriptor_tmp.16.10762
- ___block_descriptor_tmp.17.10740
- ___block_descriptor_tmp.1735
- ___block_descriptor_tmp.1745
- ___block_descriptor_tmp.18
- ___block_descriptor_tmp.186
- ___block_descriptor_tmp.21.8116
- ___block_descriptor_tmp.21.8819
- ___block_descriptor_tmp.22
- ___block_descriptor_tmp.227
- ___block_descriptor_tmp.25
- ___block_descriptor_tmp.2511
- ___block_descriptor_tmp.2557
- ___block_descriptor_tmp.270
- ___block_descriptor_tmp.274
- ___block_descriptor_tmp.28
- ___block_descriptor_tmp.2847
- ___block_descriptor_tmp.2925
- ___block_descriptor_tmp.3.5175
- ___block_descriptor_tmp.3.6214
- ___block_descriptor_tmp.311
- ___block_descriptor_tmp.315
- ___block_descriptor_tmp.319
- ___block_descriptor_tmp.3287
- ___block_descriptor_tmp.37
- ___block_descriptor_tmp.4.2848
- ___block_descriptor_tmp.4.4438
- ___block_descriptor_tmp.4.9842
- ___block_descriptor_tmp.4189
- ___block_descriptor_tmp.4356
- ___block_descriptor_tmp.44
- ___block_descriptor_tmp.4422
- ___block_descriptor_tmp.4497
- ___block_descriptor_tmp.46
- ___block_descriptor_tmp.46.4192
- ___block_descriptor_tmp.4668
- ___block_descriptor_tmp.49
- ___block_descriptor_tmp.5.8143
- ___block_descriptor_tmp.5.9847
- ___block_descriptor_tmp.51
- ___block_descriptor_tmp.51.6776
- ___block_descriptor_tmp.51.7834
- ___block_descriptor_tmp.5164
- ___block_descriptor_tmp.5289
- ___block_descriptor_tmp.54.2915
- ___block_descriptor_tmp.5590
- ___block_descriptor_tmp.57
- ___block_descriptor_tmp.582
- ___block_descriptor_tmp.5949
- ___block_descriptor_tmp.6.9848
- ___block_descriptor_tmp.6096
- ___block_descriptor_tmp.6210
- ___block_descriptor_tmp.6256
- ___block_descriptor_tmp.6324
- ___block_descriptor_tmp.6647
- ___block_descriptor_tmp.67
- ___block_descriptor_tmp.67.11638
- ___block_descriptor_tmp.6773
- ___block_descriptor_tmp.7.10756
- ___block_descriptor_tmp.7.1248
- ___block_descriptor_tmp.7.2912
- ___block_descriptor_tmp.7.8145
- ___block_descriptor_tmp.7.9849
- ___block_descriptor_tmp.7115
- ___block_descriptor_tmp.7266
- ___block_descriptor_tmp.75
- ___block_descriptor_tmp.78
- ___block_descriptor_tmp.7837
- ___block_descriptor_tmp.8.11996
- ___block_descriptor_tmp.8.2928
- ___block_descriptor_tmp.8.4198
- ___block_descriptor_tmp.8.5303
- ___block_descriptor_tmp.8.9850
- ___block_descriptor_tmp.80.13290
- ___block_descriptor_tmp.8141
- ___block_descriptor_tmp.82
- ___block_descriptor_tmp.8496
- ___block_descriptor_tmp.86
- ___block_descriptor_tmp.865
- ___block_descriptor_tmp.88.13289
- ___block_descriptor_tmp.88.7838
- ___block_descriptor_tmp.8835
- ___block_descriptor_tmp.89.13288
- ___block_descriptor_tmp.9.2562
- ___block_descriptor_tmp.9.2936
- ___block_descriptor_tmp.9.4200
- ___block_descriptor_tmp.9.6260
- ___block_descriptor_tmp.9.9851
- ___block_descriptor_tmp.90.13287
- ___block_descriptor_tmp.91
- ___block_descriptor_tmp.92
- ___block_descriptor_tmp.93.13286
- ___block_descriptor_tmp.9642
- ___block_descriptor_tmp.98
- ___block_descriptor_tmp.9833
- ___block_literal_global.10498
- ___block_literal_global.110
- ___block_literal_global.11028
- ___block_literal_global.11281
- ___block_literal_global.11512
- ___block_literal_global.11553
- ___block_literal_global.11696
- ___block_literal_global.11853
- ___block_literal_global.12028
- ___block_literal_global.12241
- ___block_literal_global.136
- ___block_literal_global.14
- ___block_literal_global.158
- ___block_literal_global.160
- ___block_literal_global.1732
- ___block_literal_global.229
- ___block_literal_global.2299
- ___block_literal_global.2822
- ___block_literal_global.3.11704
- ___block_literal_global.3021
- ___block_literal_global.3088
- ___block_literal_global.309
- ___block_literal_global.313
- ___block_literal_global.317
- ___block_literal_global.321
- ___block_literal_global.3284
- ___block_literal_global.329
- ___block_literal_global.3342
- ___block_literal_global.39
- ___block_literal_global.4195
- ___block_literal_global.429
- ___block_literal_global.4351
- ___block_literal_global.439
- ___block_literal_global.4498
- ___block_literal_global.4580
- ___block_literal_global.46
- ___block_literal_global.4739
- ___block_literal_global.4769
- ___block_literal_global.4805
- ___block_literal_global.51
- ___block_literal_global.51.12006
- ___block_literal_global.510
- ___block_literal_global.5287
- ___block_literal_global.538
- ___block_literal_global.5585
- ___block_literal_global.6090
- ___block_literal_global.6208
- ___block_literal_global.6543
- ___block_literal_global.663
- ___block_literal_global.6670
- ___block_literal_global.69
- ___block_literal_global.7111
- ___block_literal_global.7750
- ___block_literal_global.8189
- ___block_literal_global.82
- ___block_literal_global.8461
- ___block_literal_global.8897
- ___block_literal_global.9071
- ___block_literal_global.9192
- ___block_literal_global.9638
- ___copy_helper_block_e8_32c32_ZTSN4brls19EvtPSStopSecondPassE
- ___copy_helper_block_e8_32c34_ZTSN4brls21EvtStartRecordTimeoutE
- ___destroy_helper_block_e8_32c32_ZTSN4brls19EvtPSStopSecondPassE
- ___destroy_helper_block_e8_32c34_ZTSN4brls21EvtStartRecordTimeoutE
- ___memcpy_chk
- _audiomxd_enabled
- _bootstrap_look_up
- _gAQClientTraceScope
- _gMediaServerTimeout
- _getenv
- _kCFPreferencesCurrentHost
- _mach_port_get_refs
- _mach_port_mod_refs
- _objc_msgSend$addEntriesFromDictionary:
- _objc_msgSend$analyzeBufferList:
- _objc_msgSend$dictionaryWithCapacity:
- _objc_msgSend$getAdjustedDeviceStartTime:
- _objc_msgSend$getBytes:length:
- _objc_msgSend$getModel
- _objc_msgSend$getPhraseSpotter
- _objc_msgSend$initWithRateLimit:detectPredictionAnchor:userContext:factory:execution:finalizer:
- _objc_msgSend$notifyVoiceTrigger
- _objc_msgSend$numberWithLongLong:
- _objc_msgSend$numberWithUnsignedLongLong:
- _objc_msgSend$prepareWithProperty:readyCompletion:
- _objc_msgSend$sampleCount
- _objc_msgSend$sampleCountAtEndOfTrigger
- _objc_msgSend$sampleCountAtStartOfTrigger
- _objc_msgSend$setStartSampleHostTime:
- _objc_msgSend$sharedPreferences
- _objc_msgSend$voiceTriggerEnabled
- _sleep
- _task_get_special_port
- _wmemchr
CStrings:
+ "\tGlobal: mVibrationDisabled: %d mPhoneCallActive: %d mMicIsActive: %d mContinuityScreenOn: %d highest priority client count: %d, high priority client count: %d\n"
+ "\tNum Events: %d, Track Length: %.2f beats, Loop Region End: %.2f beats\n"
+ "  %s: %p\n"
+ "  EnhanceDialogueProcessor: (%s) "
+ " with microphoneInjectionMode "
+ "!\"Attempted to add same channel ID twice\""
+ "!\"Attempted to add same instance ID twice\""
+ "!\"Bad property size\""
+ "!\"SHOULD NOT BE RECEIVING REC-STATE-DID-CHANGE NOTIFICATIONS\""
+ "!\"Unexpected Property ID\""
+ "!\"Unknown property\""
+ "!BypassAudioSession()"
+ "!BypassAudioSession() || IsTap()"
+ "!audio || _audioPrewarmCount > 0"
+ "!audio || _audioRunningCount > 0"
+ "!haptics || _hapticsPrewarmCount > 0"
+ "!haptics || _hapticsRunningCount > 0"
+ "!isRunning()"
+ "!mInitialized"
+ "!mIsTapSubmix"
+ "!mIsTapSubmix && channel->GetSubmixGraph() == nullptr"
+ "!mIsTapSubmix && channel->GetSubmixGraph() == this"
+ "!running()"
+ "!stopping()"
+ "!submixToConnect.mIsTapSubmix && !mainSubmix.mIsTapSubmix"
+ "%25s:%-5d      AudioSessionIsEnhanceable: allowEnhanceDialogue = true for client %s"
+ "%25s:%-5d      ERROR: xau@%p is initialized when mix format is set!"
+ "%25s:%-5d      EnhanceDialogue submix old fmt:%s -> new fmt:%s %s"
+ "%25s:%-5d      EnhanceDialogue submix using layout mixer channel %p with layout:%s"
+ "%25s:%-5d      MEEnhanceableSubmixGraph: MEMixerChannel@%p %sconnection triggering enhanceDialogueModeChanged (%s)"
+ "%25s:%-5d      MEParallelPathSubmixGraph(%p)::isUsingAirPlayMusicPort() = %s"
+ "%25s:%-5d      closing the EnhanceDialogue Processor"
+ "%25s:%-5d      connectEnhancedRenderProc using fmt %s for EnhanceDialogue"
+ "%25s:%-5d      getEnhanceableSessionType: AQIONodeClient %p sessionID 0x%x has an Enhanceable or Movie Mode audio session %s"
+ "%25s:%-5d      getEnhanceableSessionType: AQIONodeClient %p sessionID 0x%x is not running (%d clients total)"
+ "%25s:%-5d      getEnhanceableSessionType: AQIONodeClient %p sessionID 0x%x with audio session mode %s has disconnected MEMixerChannel@%p"
+ "%25s:%-5d      getEnhanceableSessionType: AQIONodeClient %p sessionID 0x%x with audio session mode %s prevents Enhance Dialogue"
+ "%25s:%-5d      initializing the EnhanceDialogue processor"
+ "%25s:%-5d      main submix and EnhanceDialogue submix formats matched: %s"
+ "%25s:%-5d      nothing is connected to the EnhanceDialogue submix"
+ "%25s:%-5d      opening the EnhanceDialogue Processor"
+ "%25s:%-5d      shouldMigrateChannel(%s) = true (EnhanceDialogue)"
+ "%25s:%-5d  CACFPreferences::CopyNumberValue: not a CFNumber"
+ "%25s:%-5d  CACFPreferences::CopyStringValue: not a CFString"
+ "%25s:%-5d !!! getEnhanceableSessionType() - Atmos metadata decode detected !!!"
+ "%25s:%-5d !!! getEnhanceableSessionType() - suppressing EDP off to bypass !!!"
+ "%25s:%-5d %p mixer bus %d volume=%g"
+ "%25s:%-5d %s: %s audio on client ID 0x%lx due to player behaviors: MuteAudio %d, HapticsOnly %d"
+ "%25s:%-5d %s: %s format changed for clientID 0x%x"
+ "%25s:%-5d %s: %s haptics on client ID 0x%lx due to player behaviors: MuteHaptics %d, AudioOnly %d"
+ "%25s:%-5d %s: %s route changed for clientID 0x%x - handling async"
+ "%25s:%-5d %s: %s volume changed for clientID 0x%x"
+ "%25s:%-5d %s: AQ Time-stretcher: ionc@%p TimePitchProperty accessed; error %d"
+ "%25s:%-5d %s: AQ Time-stretcher: ionc@%p TimePitchProperty set %s: %d"
+ "%25s:%-5d %s: Active high priority client count -> 0; no highest priority clients; so ummuting all low priority clients"
+ "%25s:%-5d %s: Active high priority client count -> 1 so muting other low priority clients"
+ "%25s:%-5d %s: Active highest priority client count -> 0; active high priority client: %u; so ummuting all %@clients"
+ "%25s:%-5d %s: Active highest priority client count -> 1 so muting other low/high priority clients"
+ "%25s:%-5d %s: Added minimal ramp event (time %.3f) with default value %.3f to track %p (parameter type %u)"
+ "%25s:%-5d %s: Added preservation point (t=%.3f) with interpolated value %.3f to track %p (parameter type %u)"
+ "%25s:%-5d %s: Added source parameter curve %p (effective start time %.3f, %u point(s)) to state map for type %u%s"
+ "%25s:%-5d %s: Added zero-time event with default value %.3f to track %p (parameter type %u)"
+ "%25s:%-5d %s: Added zero-time event with user value %.3f to track %p (parameter type %u)"
+ "%25s:%-5d %s: Adding raw audio sample %p, size %u bytes. Raw audio has %u channels, %u frames, %u Bytes per frame, clientProcessTaskToken: %u"
+ "%25s:%-5d %s: AudioQueueSetProperty: %s not supported on this platform"
+ "%25s:%-5d %s: Automation track %p for type %u: publishing control point (time %.3f, value %f) from source curve %p"
+ "%25s:%-5d %s: Automation track %p for type %u: publishing flat segment extension control point (time %.3f, value %f) for non-overlapping source curve %p"
+ "%25s:%-5d %s: Automation track %p for type %u: skipping processing for source curve %p entirely because first point (time %.3f, value %f) coincides exactly with start time of next curve"
+ "%25s:%-5d %s: Automation track %p for type %u: terminating processing for source curve %p by publishing interpolated control point (time %.3f, value %f), as a later curve starts at %.3f. Linear interpolation is based on prior valid point (time %.3f, value %f) and first overextended point (time %.3f, value %f)"
+ "%25s:%-5d %s: Cannot guarantee preservation point at time %.3f, length %.3f of track %p is too short"
+ "%25s:%-5d %s: Capturing AQ(%p) output on decode: %s"
+ "%25s:%-5d %s: Capturing AQ(%p) output on enqueue: %s"
+ "%25s:%-5d %s: Capturing offline AQ(%p): %s"
+ "%25s:%-5d %s: Consolidating source parameter curve %p (effective start time %.3f, %u points) into automation track %p for type %u"
+ "%25s:%-5d %s: CoreAudioServices/LoudnessManagerV2 feature flag is off, LM AULN disabled"
+ "%25s:%-5d %s: Could not add processing node err: %ld"
+ "%25s:%-5d %s: Created new automation track %p for parameter type %u"
+ "%25s:%-5d %s: Created new entry for parameter type %u in consolidation state map that holds automation track and source curves"
+ "%25s:%-5d %s: DRC capability from decoder: %s (0x%x)\n"
+ "%25s:%-5d %s: Dynamic parameter event with Haptic Synth parameter type (%u) marked for conversion to parameter curve"
+ "%25s:%-5d %s: ERROR: mach_port_deallocate of client process task token %u failed with %d"
+ "%25s:%-5d %s: Error making parameter event: %s"
+ "%25s:%-5d %s: Error: could not insert into parameter type state map"
+ "%25s:%-5d %s: Error: could not set automation property on on new track %p"
+ "%25s:%-5d %s: GetProposedIOFormat: aq@%p: Before: streamLayout (%s), mChannelLayout (%s), mCodecChannelLayout (%s), maximumDecodeChannels=%d"
+ "%25s:%-5d %s: Got error %d while writing packets for AQ output enqueue"
+ "%25s:%-5d %s: Highest priority clients always play haptics in Continuity Screen mode"
+ "%25s:%-5d %s: LM disabled, not looking for SC overrides"
+ "%25s:%-5d %s: LoudnessManager::GetSettings() returned %d (%s): %s"
+ "%25s:%-5d %s: LoudnessManager::GetSettings() returned %d (%s): disabling LM-AULN"
+ "%25s:%-5d %s: Making parameter event for curve control point: ID=%d time=%.3f value=%f"
+ "%25s:%-5d %s: MusicPlayerSetPlayRateScalar returned %d"
+ "%25s:%-5d %s: Preservation point (t=%.3f) already exists on track %p (parameter type %u), exiting"
+ "%25s:%-5d %s: SSP::Render: CopySlice returned %d"
+ "%25s:%-5d %s: ScheduledSlicePlayer2::ClearSchedule: %d frame imbalance"
+ "%25s:%-5d %s: ScheduledSlicePlayer_Legacy::ClearSchedule: %d frame imbalance"
+ "%25s:%-5d %s: SequenceRTAccessor::getEventInfo returned %d"
+ "%25s:%-5d %s: SequenceRTAccessor::nextEvent returned %d"
+ "%25s:%-5d %s: Set automation track %u t=0 point value to %.3f, based on calculated value at t=iterationEndTime (%.2f beats)"
+ "%25s:%-5d %s: SetProperty(kAudioQueueProperty_LoudnessData)"
+ "%25s:%-5d %s: Specified ramp duration is sub-minimal (provided %.3f, requiring %.3f) - pushing new event forward to time %.3f. Warning: ramp might be too fast for some watches"
+ "%25s:%-5d %s: Value delta %.3f requires a minimal ramp duration of %.3f"
+ "%25s:%-5d %s: WARNING: Illegal AddParamCurve (adjusted time %.3lf, type %u) -- has different paramID %u than expected paramID %u! Skipping"
+ "%25s:%-5d %s: addInitialAutomationEvents returned %d"
+ "%25s:%-5d %s: adding set loudness command to work queue"
+ "%25s:%-5d %s: apply-custom-aqme-lm-auln-settings is on, configuring LM-AULN from preferences"
+ "%25s:%-5d %s: aq@%p: Decoder channel layout set to (%s), maximumDecodeChannels=%d"
+ "%25s:%-5d %s: aq@%p: Error in AudioFormatGetProperty (err=%d, %s), tag=0x%x"
+ "%25s:%-5d %s: aq@%p: Forcing 7.1.4 decoder for Atmos (mChannelLayout (%s), streamLayout(%s))"
+ "%25s:%-5d %s: aq@%p: Got err %d while getting IO node"
+ "%25s:%-5d %s: aq@%p: New %s; format %s (passthrough? %s)"
+ "%25s:%-5d %s: aq@%p: Setting Atmos decoder to client requested channel layout"
+ "%25s:%-5d %s: aq@%p: Setting Atmos decoder to output stream channel layout"
+ "%25s:%-5d %s: aq@%p: Using (%s) layout for Atmos decoder, streamLayout(%s)"
+ "%25s:%-5d %s: aq@%p: cinematic audio: %s"
+ "%25s:%-5d %s: cinematic mode is on with no codec"
+ "%25s:%-5d %s: cinematic remix: gaindb = %f, capture loudness = %f, setting linear gain = %f"
+ "%25s:%-5d %s: com.apple.coreaudio/apply-custom-loudness-settings|drc-capable is on, configuring codec from preferences"
+ "%25s:%-5d %s: could not get DRC output params from codec, error %d (%s)"
+ "%25s:%-5d %s: could not get SourceLoudness from DRC output params dictionary"
+ "%25s:%-5d %s: could not init the converter connection, err = %d (%s)"
+ "%25s:%-5d %s: could not set kMELMLoudnessNormalizerProperty_AlgorithmVersion, error %d (%s)"
+ "%25s:%-5d %s: could not set kMELMLoudnessNormalizerProperty_DownwardCompressionRange, error %d (%s)"
+ "%25s:%-5d %s: could not set kMELMLoudnessNormalizerProperty_DownwardCompressionRatio, error %d (%s)"
+ "%25s:%-5d %s: could not set kMELMLoudnessNormalizerProperty_EnableCompressor, error %d (%s)"
+ "%25s:%-5d %s: could not set kMELMLoudnessNormalizerProperty_EnableOutputCeiling, error %d (%s)"
+ "%25s:%-5d %s: could not set kMELMLoudnessNormalizerProperty_InputGain, error %d (%s)"
+ "%25s:%-5d %s: could not set kMELMLoudnessNormalizerProperty_LookaheadDelayMS, error %d (%s)"
+ "%25s:%-5d %s: could not set kMELMLoudnessNormalizerProperty_LoudnessAfterReset, error %d (%s)"
+ "%25s:%-5d %s: could not set kMELMLoudnessNormalizerProperty_LoudnessTarget, error %d (%s)"
+ "%25s:%-5d %s: could not set kMELMLoudnessNormalizerProperty_MaxGain, error %d (%s)"
+ "%25s:%-5d %s: could not set kMELMLoudnessNormalizerProperty_OutputCeiling, error %d (%s)"
+ "%25s:%-5d %s: could not set kMELMLoudnessNormalizerProperty_OutputGain, error %d (%s)"
+ "%25s:%-5d %s: could not set kMELMLoudnessNormalizerProperty_PeakLevelOffset, error %d (%s)"
+ "%25s:%-5d %s: could not set kMELMLoudnessNormalizerProperty_RenderQuality, error %d (%s)"
+ "%25s:%-5d %s: could not set kMELMLoudnessNormalizerProperty_ResetMode, error %d (%s)"
+ "%25s:%-5d %s: could not set kMELMLoudnessNormalizerProperty_ResetTimeout, error %d (%s)"
+ "%25s:%-5d %s: could not set kMELMLoudnessNormalizerProperty_SideChainHighPassFrequency, error %d (%s)"
+ "%25s:%-5d %s: could not set kMELMLoudnessNormalizerProperty_UpwardCompressionRange, error %d (%s)"
+ "%25s:%-5d %s: could not set kMELMLoudnessNormalizerProperty_UseDownwardCompressionRateio, error %d (%s)"
+ "%25s:%-5d %s: could not set kMELMLoudnessNormalizerProperty_WeightingFilter, error %d (%s)"
+ "%25s:%-5d %s: deallocating client process task token: %u"
+ "%25s:%-5d %s: decoder does not handle DRC, looking for SC overrides"
+ "%25s:%-5d %s: decoder handles DRC, not looking for SC overrides"
+ "%25s:%-5d %s: found override SC max peak level in plist: %f"
+ "%25s:%-5d %s: found override SC target loudness in plist: %f"
+ "%25s:%-5d %s: getAutomationValueAtTime returned %d"
+ "%25s:%-5d %s: got LM AULN config, configuring LM-AULN"
+ "%25s:%-5d %s: got session category of '%s'"
+ "%25s:%-5d %s: got session mode of '%s'"
+ "%25s:%-5d %s: guaranteePreservationPoint returned %d"
+ "%25s:%-5d %s: hardware not supported, Loudness Manager disabled"
+ "%25s:%-5d %s: highest priority client count: %u, high priority client count: %u, exclusive priority client count: %u"
+ "%25s:%-5d %s: input queue, returning immediately"
+ "%25s:%-5d %s: is CoreAudioServices/LoudnessManager enabled? %s"
+ "%25s:%-5d %s: is CoreAudioServices/LoudnessManagerV2 enabled? %s"
+ "%25s:%-5d %s: is CoreAudioServices/lm-disable-hardware-check on? %s"
+ "%25s:%-5d %s: is hardware supported? %s"
+ "%25s:%-5d %s: is sound check enabled? %s"
+ "%25s:%-5d %s: loudness-manager-disable is on, resetting codec and disabling LM-AULN"
+ "%25s:%-5d %s: no LM-AULN settings found, disabling LM-AULN"
+ "%25s:%-5d %s: no codec settings found, resetting codec config"
+ "%25s:%-5d %s: no codec, can't configure from preferences"
+ "%25s:%-5d %s: no ionode, can't configure LM-AULN from preferences"
+ "%25s:%-5d %s: no ionode, unable to configure LM-AULN"
+ "%25s:%-5d %s: no loudness info available, can't override SC properties"
+ "%25s:%-5d %s: null LID passed in, using cached: %p"
+ "%25s:%-5d %s: offline queue, resetting codec and disabling LM-AULN"
+ "%25s:%-5d %s: passthrough queue, returning immediately"
+ "%25s:%-5d %s: pre-tuned session category, resetting codec and disabling LM-AULN"
+ "%25s:%-5d %s: pre-tuned session mode, resetting codec and disabling LM-AULN"
+ "%25s:%-5d %s: queue is playing, not configuring codec"
+ "%25s:%-5d %s: queue is playing, not configuring codec or AULN"
+ "%25s:%-5d %s: setEventInfo returned %d"
+ "%25s:%-5d %s: setting LM AULN algorithm version to %f"
+ "%25s:%-5d %s: setting LM AULN downward compression range to %f"
+ "%25s:%-5d %s: setting LM AULN downward compression ratio to %f"
+ "%25s:%-5d %s: setting LM AULN enable compressor to %f"
+ "%25s:%-5d %s: setting LM AULN enable output ceiling to %f"
+ "%25s:%-5d %s: setting LM AULN input gain to %f"
+ "%25s:%-5d %s: setting LM AULN lookahead delay ms to %f"
+ "%25s:%-5d %s: setting LM AULN loudness after reset to %f"
+ "%25s:%-5d %s: setting LM AULN loudness target to %f"
+ "%25s:%-5d %s: setting LM AULN max gain to %f"
+ "%25s:%-5d %s: setting LM AULN output ceiling to %f"
+ "%25s:%-5d %s: setting LM AULN output gain to %f"
+ "%25s:%-5d %s: setting LM AULN peak level offset to %f"
+ "%25s:%-5d %s: setting LM AULN render quality to %f"
+ "%25s:%-5d %s: setting LM AULN reset mode to %f"
+ "%25s:%-5d %s: setting LM AULN reset timeout to %f"
+ "%25s:%-5d %s: setting LM AULN sidechain highpass frequency to %f"
+ "%25s:%-5d %s: setting LM AULN upward compression range to %f"
+ "%25s:%-5d %s: setting LM AULN use downward compression ratio (not range) to %d"
+ "%25s:%-5d %s: setting LM AULN weighting filter to %f"
+ "%25s:%-5d %s: taskToken: %u"
+ "%25s:%-5d %s::setEnhanceDialogueEnabled: %d (no change)"
+ "%25s:%-5d %s::setEnhanceDialogueEnabled: %d -> %d"
+ "%25s:%-5d %s::updateEnhanceDialogueRoute: route capable = %s for %s [%s] - disconnecting client(s) from enhanceable submix"
+ "%25s:%-5d %s::updateEnhanceDialogueRoute: route capable = %s for %s [%s] - disconnecting enhanceable client(s) from the main mixer"
+ "%25s:%-5d %s::updateEnhanceDialogueRoute: route supported = %s for %s [%s, %s]"
+ "%25s:%-5d %s@%p: maintainTaps (tapAdded = %d)"
+ "%25s:%-5d (mPrefersToPlayAudioToHeadphonesOnly == true) - calling StopPlaying for active SSID"
+ "%25s:%-5d <On SSS Worker Queue> calling haptic completion callback"
+ "%25s:%-5d AQ Time-stretcher: ionc@%p Enabled the time-stretcher as (%s)"
+ "%25s:%-5d AQ Time-stretcher: ionc@%p Forced the time-stretcher as (%s)"
+ "%25s:%-5d AQ Time-stretcher: ionc@%p SchedTimePitchAddRateChange %.3f @ %lld"
+ "%25s:%-5d AQ Time-stretcher: ionc@%p SchedTimePitchTrackedRateChange %.3f %lld %lld"
+ "%25s:%-5d AQ Time-stretcher: ionc@%p Set parameter %d as %f"
+ "%25s:%-5d AQ Time-stretcher: ionc@%p TimePitchPitch %.3f"
+ "%25s:%-5d AQ Time-stretcher: ionc@%p TimePitchRate(%s) %.3f"
+ "%25s:%-5d AQ Time-stretcher: ionc@%p TimePitchRate(immediate) %.3f"
+ "%25s:%-5d AQ Time-stretcher: ionc@%p TimePitchReset"
+ "%25s:%-5d AQIONodeClient %p: LS Database not available"
+ "%25s:%-5d AQIONodeClient %p: can record: %d"
+ "%25s:%-5d AQIONodeClient::AudioSessionIsEnhanceable: client %s: could not fetch audio session allowEnhanceDialogue (err = %d)"
+ "%25s:%-5d AQME %s: client: %s; %s audit token, error %d"
+ "%25s:%-5d AQMEDevice(%p)::RestartIOFollowingRouteChange called before IO Unit was initialized"
+ "%25s:%-5d AQMEIO_DSP(%p)::Begin AdaptToVARoute(%p%s)"
+ "%25s:%-5d AQMEIO_DSP::End AdaptToVARoute(%s)"
+ "%25s:%-5d AQMETapConnector::Create; created tap of session(s) %s with microphoneInjectionMode %i and format: %s."
+ "%25s:%-5d AQMixEngine_VAD(%p)::RouteChanged - EnhanceDialogue is not implemented on this platform"
+ "%25s:%-5d AQMixEngine_VAD(%p)::RouteChanged() - triggering enhanceDialogueModeChanged"
+ "%25s:%-5d ATBlurMixer@%p(%s): Error initializing AUDSPGraph, err = %d"
+ "%25s:%-5d ATBlurMixer@%p(%s): Error opening AUDSPGraph, err = %d"
+ "%25s:%-5d ATBlurMixer@%p(%s): Error setting %s stream format (%s) on element = %d, err = %d"
+ "%25s:%-5d ATBlurMixer@%p(%s): Error setting kAUDSPGraphProperty_AUStrip, err = %d"
+ "%25s:%-5d ATBlurMixer@%p(%s): Error setting kAUDSPGraphProperty_GraphTextFilePath, err = %d"
+ "%25s:%-5d ATBlurMixer@%p(%s): Error setting kAUDSPGraphProperty_PropertyStrip, err = %d"
+ "%25s:%-5d ATBlurMixer@%p(%s): Error setting kAudioUnitProperty_ElementCount on %s to %d, err = %d"
+ "%25s:%-5d ATBlurMixer@%p(%s): Error setting kAudioUnitProperty_MaximumFramesPerSlice = %d, err = %d"
+ "%25s:%-5d ATBlurMixer@%p(%s): Error setting parameter BlurBlendTimeMs, err = %d"
+ "%25s:%-5d ATBlurMixer@%p(%s): Error uninitializing AUDSPGraph, err = %d"
+ "%25s:%-5d ATBlurMixer@%p(%s): Tuning directory does not exist"
+ "%25s:%-5d AUAsyncRendererHost@%p(%s): Error finding AudioComponent for AUAsyncRenderer"
+ "%25s:%-5d AUAsyncRendererHost@%p(%s): Error getting kAudioUnitProperty_AsyncRendererOutputBufferBlock, err = %d"
+ "%25s:%-5d AUAsyncRendererHost@%p(%s): Error initializing AUAsyncRenderer, err = %d"
+ "%25s:%-5d AUAsyncRendererHost@%p(%s): Error opening AUAsyncRenderer, err = %d"
+ "%25s:%-5d AUAsyncRendererHost@%p(%s): Error setting input stream format (%s), err = %d"
+ "%25s:%-5d AUAsyncRendererHost@%p(%s): Error setting kAudioUnitProperty_AsyncRendererClientFormat (%s) on input scope, err = %d"
+ "%25s:%-5d AUAsyncRendererHost@%p(%s): Error setting kAudioUnitProperty_AsyncRendererClientFormat (%s) on output scope (err = %d"
+ "%25s:%-5d AUAsyncRendererHost@%p(%s): Error setting kAudioUnitProperty_AsyncRendererEnableIO = %d on output scope, err = %d"
+ "%25s:%-5d AUAsyncRendererHost@%p(%s): Error setting kAudioUnitProperty_AsyncRendererInputBufferBlock, err = %d"
+ "%25s:%-5d AUAsyncRendererHost@%p(%s): Error setting kAudioUnitProperty_AsyncRendererInputBufferSize = %d, err = %d"
+ "%25s:%-5d AUAsyncRendererHost@%p(%s): Error setting kAudioUnitProperty_AsyncRendererOutputBufferCompleteBlock, err = %d"
+ "%25s:%-5d AUAsyncRendererHost@%p(%s): Error setting kAudioUnitProperty_MaximumFramesPerSlice = %d, err = %d"
+ "%25s:%-5d AUAsyncRendererHost@%p(%s): Error setting output stream format (%s), err = %d"
+ "%25s:%-5d AUAsyncRendererHost@%p(%s): Error uninitializing AUAsyncRenderer, err = %d"
+ "%25s:%-5d AUAsyncRendererHost@%p(%s): Error updating stream formats, err = %d"
+ "%25s:%-5d AUAsyncRendererHost@%p(%s): updating stream format. Old format <%s>. New format <%s>."
+ "%25s:%-5d An error occurred creating the call translator. Error=%i"
+ "%25s:%-5d An error occurred parsing the translation configuration"
+ "%25s:%-5d AudioSessionAllowsEnhanceDialogue returned error %i for session 0x%x"
+ "%25s:%-5d AudioTap: including device %d (%@) in system tap (main device %d)"
+ "%25s:%-5d AudioToolboxServerSetIOPropertiesForSession; gAQME's call session=0x%x != inSessionID=0x%x"
+ "%25s:%-5d AudioToolboxServerSetIOPropertiesForSession; session id: 0x%x"
+ "%25s:%-5d AudioToolboxServerSetIOPropertiesForSession; set call translation properties. status: %i"
+ "%25s:%-5d AudioTranslationInjector@%p: DuckingHoldTime = %f, Scope = %s"
+ "%25s:%-5d AudioTranslationInjector@%p: TranslationServiceProducesAudio = %d, Scope = %s"
+ "%25s:%-5d BlurringMixerDSPGraphHost@%p(%s): Error updating formats (%s), err = %d"
+ "%25s:%-5d BlurringMixerDSPGraphHost@%p(%s): Error updating stream formats, err = %d"
+ "%25s:%-5d BlurringMixerDSPGraphHost@%p: Error instantiating ATBlurMixer, err = %d"
+ "%25s:%-5d Buffer complete, abl: %lu, did render = %d"
+ "%25s:%-5d Caching CallTranslator(%p)"
+ "%25s:%-5d Call translation disabled by translation configuration"
+ "%25s:%-5d CallTranslator(%p)"
+ "%25s:%-5d CallTranslator(%p)::HandleInjectionEndedCallback; invoking mReleaseCallTranslatorCallback"
+ "%25s:%-5d CallTranslator(%p)::HandleInjectionEndedCallback; releasing the input stream translator"
+ "%25s:%-5d CallTranslator(%p)::HandleInjectionEndedCallback; releasing the output stream translator"
+ "%25s:%-5d CallTranslator: isRemoteFeedbackEnabled = %d"
+ "%25s:%-5d CallTranslator: isRemoteFeedbackEnabled = %d by default"
+ "%25s:%-5d CallTranslator::Create; CAException caught in log: %d"
+ "%25s:%-5d CallTranslator::Create; Unknown exception caught in log"
+ "%25s:%-5d CallTranslator::Create; an error (%i) occurred creating the translator for the stream!"
+ "%25s:%-5d CallTranslator::Create; an error (%i) occurred creating the translator injector for the stream!"
+ "%25s:%-5d CallTranslator::Create; cached CallTranslator(%p) matches translation configuration? %i"
+ "%25s:%-5d CallTranslator::Create; existing CallTranslator(%p) matches translation configuration"
+ "%25s:%-5d CallTranslator::Create; releasing reference to cached CallTranslator(%p) which does not match translation configuration"
+ "%25s:%-5d CallTranslator::Create; releasing reference to cached CallTranslator(%p) which matches translation configuration but could not be restored"
+ "%25s:%-5d CallTranslator::Create; std::exception caught in log: %s"
+ "%25s:%-5d CallTranslator::Create; using cached CallTranslator(%p) matching translation configuration"
+ "%25s:%-5d Can not enable AQMEIO_HAL captures at this time due to VP."
+ "%25s:%-5d Can not enable MEMixerChannel captures at this time due to VP."
+ "%25s:%-5d Cannot get valid telelphony or VP input client session when reinitializing VP. Skip overriding host application ID."
+ "%25s:%-5d Capturing %s"
+ "%25s:%-5d Clearing the cache's reference to CallTranslator(%p)"
+ "%25s:%-5d Could not get spatial experience for audio session 0x%x, err %d"
+ "%25s:%-5d Could not start vibe for actionID %d, error %d. Vibe format: %s"
+ "%25s:%-5d CreateTappedAudioProducer; CAException caught in log: %d"
+ "%25s:%-5d CreateTappedAudioProducer; Unknown exception caught in log"
+ "%25s:%-5d CreateTappedAudioProducer; invalid audio format provided. format=%s"
+ "%25s:%-5d CreateTappedAudioProducer; no audio session ids provided."
+ "%25s:%-5d CreateTappedAudioProducer; std::exception caught in log: %s"
+ "%25s:%-5d Creating a legacy IONodeSession for session ID: 0x%x with description %s"
+ "%25s:%-5d Delete buffer, abl: %lu"
+ "%25s:%-5d Detected exception starting vibe, registering vibe completion without client completion"
+ "%25s:%-5d Device in phone call with other remote routes. Play original haptics pattern"
+ "%25s:%-5d Device in phone call with receiver or builtin speaker. Replacing haptics pattern with '%@'"
+ "%25s:%-5d Device will not vibe as AHAP playback for System Sounds is not supported"
+ "%25s:%-5d DisableMixTapToTelephonyUplink(%p); gInstance is not initialized!"
+ "%25s:%-5d Disabling call translation b/c translation ended."
+ "%25s:%-5d EXCEPTION (%d): \"\""
+ "%25s:%-5d EnableMixTapToTelephonyUplink(%p); CAException caught in log: %d"
+ "%25s:%-5d EnableMixTapToTelephonyUplink(%p); Unknown exception caught in log"
+ "%25s:%-5d EnableMixTapToTelephonyUplink(%p); failed to start tap"
+ "%25s:%-5d EnableMixTapToTelephonyUplink(%p); std::exception caught in log: %s"
+ "%25s:%-5d Enabled CallTranslator(%p)"
+ "%25s:%-5d EnhanceDialogue could not set mixer channel layout on mixer@%p: scope %d, element %d, %s: error %d"
+ "%25s:%-5d EnhanceDialogueProcessor() - Product does not have valid tuning"
+ "%25s:%-5d EnhanceDialogueProcessor() - Product does not support Enhance Dialogue"
+ "%25s:%-5d EnhanceDialogueProcessor::Initialize: processor invalid, return"
+ "%25s:%-5d EnhanceDialogueProcessor::MixLayoutChanged: Failed to get channel layout for DSPGraph, err = %d"
+ "%25s:%-5d EnhanceDialogueProcessor::MixLayoutChanged: Failed to get channel layout for mExternalACL, err = %d"
+ "%25s:%-5d EnhanceDialogueProcessor::MixLayoutChanged: externalACL: %s, graphACL: %s"
+ "%25s:%-5d EnhanceDialogueProcessor::SetBypass: Setting %s"
+ "%25s:%-5d EnhanceDialogueProcessor::SetBypass: Setting bypass: %d"
+ "%25s:%-5d EnhanceDialogueProcessor::SetBypass: processor invalid, return"
+ "%25s:%-5d EnhanceDialogueProcessor::SetChannelMap with mChannelMap, size = %lu"
+ "%25s:%-5d EnhanceDialogueProcessor::SetChannelMap: clear DSP channel maps"
+ "%25s:%-5d EnhanceDialogueProcessor::SetChannelMap: mChannelMap.size() = 0, return"
+ "%25s:%-5d EnhanceDialogueProcessor::SetChannelMap: processor invalid, return"
+ "%25s:%-5d EnhanceDialogueProcessor::Uninitialize: processor invalid, return"
+ "%25s:%-5d EnhanceDialogueProcessor::UpdateEnhanceDialogueLevel: Setting %s"
+ "%25s:%-5d EnhanceDialogueProcessor::WetDryMixPercent - Failed to get %s from graph, err = %s"
+ "%25s:%-5d EnhanceDialogue_submixer attach1MixerChannel bus %d client:%s)"
+ "%25s:%-5d EnhanceDialogue_submixer detach1MixerChannel %p (client=%s), bus %d"
+ "%25s:%-5d Error %d in attempt to play actionID %d, sending immediate completion message to client"
+ "%25s:%-5d Error: Failed to set CATapDescription for HAL tap ID %d : only system taps are supported on this platform"
+ "%25s:%-5d Error: only system taps are supported on this platform. (aggregate: %@)"
+ "%25s:%-5d Error: unable to find system tap aggregate: %@"
+ "%25s:%-5d Failed to create STSpeechTranslatorClient from UUID %s"
+ "%25s:%-5d Failed to get kVirtualAudioDevicePropertyCallType for device %d with error %d"
+ "%25s:%-5d Failed to read stream config for scope %s"
+ "%25s:%-5d Failed to set kVPProperty_AirPodsOffloadMode with error: %d"
+ "%25s:%-5d Feature disabled"
+ "%25s:%-5d FireSpeechDetectedNotificationIfChanged; speech activity event %s"
+ "%25s:%-5d GetAudioSessionsWithMixToUplinkPreferenceInternal; Ignoring invalid audioSessionToTap = 0x%x"
+ "%25s:%-5d GetDataSize failed with status=%i and size=%i"
+ "%25s:%-5d GetHardwarePlatformKey(): cannot get acoustic ID"
+ "%25s:%-5d GetHardwarePlatformKey(): found acoustic ID: %d"
+ "%25s:%-5d GetHardwarePlatformKey(): hardware platform key is %s"
+ "%25s:%-5d GetHardwarePlatformKey(): unrecognised embedded platform type: %d"
+ "%25s:%-5d GetIndexOfSupportedMicrophoneInjectionMode; unsupported microphoneInjectionMode = %i"
+ "%25s:%-5d GetMediaTypeAndEncoderOSKeys(): can not determine content source"
+ "%25s:%-5d GetMediaTypeAndEncoderOSKeys(): can't get audio mode from session"
+ "%25s:%-5d GetMediaTypeAndEncoderOSKeys(): got audio mode from session: %s"
+ "%25s:%-5d GetSettings(): could not find top level key %s in plist"
+ "%25s:%-5d GetSettings(): found default dictionary for encoder OS type"
+ "%25s:%-5d GetSettings(): found default dictionary for hardware platform"
+ "%25s:%-5d GetSettings(): found default dictionary for late night / sound check"
+ "%25s:%-5d GetSettings(): found default dictionary for media format"
+ "%25s:%-5d GetSettings(): found default dictionary for media type"
+ "%25s:%-5d GetSettings(): looking for late night / soundcheck key: %s"
+ "%25s:%-5d GetSettings(): looking for media type and encoder OS and version: %d (%s) %s %d.%d"
+ "%25s:%-5d GetSettings(): no dictionary (or default) for encoder OS version: %s %d.%d"
+ "%25s:%-5d GetSpatialMetadata Create failed with status = %i"
+ "%25s:%-5d GetSpatialMetadata SetData failed with status = %i, outDataSize = %i"
+ "%25s:%-5d Ignoring downlink mute state %d set while mMuteControlledByAVSC is enabled"
+ "%25s:%-5d Ignoring uplink mute state %d set while mMuteControlledByAVSC is enabled"
+ "%25s:%-5d InferActiveAudioChannel; GetProperty status = %i"
+ "%25s:%-5d InferActiveAudioChannel; setting active audio channel to %i"
+ "%25s:%-5d InputConverter: AudioBufferList sizes don't match: %u != %u"
+ "%25s:%-5d IsHardwareSupported(): no plist loaded, returning false"
+ "%25s:%-5d MEEnhanceableSubmixGraph::_changeMixFormat: graph=%p, mixer=%p, fmt=%s (EnhanceDialogue)"
+ "%25s:%-5d MEEnhanceableSubmixGraph::initialize() - will connect EnhanceDialogue submix"
+ "%25s:%-5d MEEnhanceableSubmixGraph::rebuildChain() - EnhanceDialogueProcessor %p added to ParallelPath"
+ "%25s:%-5d MEInputManager: Error invoking InputDispatcher %s"
+ "%25s:%-5d MEInputManager: Unknown Error invoking InputDispatcher"
+ "%25s:%-5d MEMixerChannel::AddProcessingNode: failed to set OfflineRender: %d"
+ "%25s:%-5d MEOutputStreamClient(%p)::RemoveRunningClient_IO(%s, awaitIOCycle = %s): unable to get submix graph for channel %p"
+ "%25s:%-5d MEParallelPathSubmixGraph::MEParallelPathSubmixGraph() - EnhanceDialogueProcessor::IsOnParallelPath() == %s"
+ "%25s:%-5d MEParallelPathSubmixGraph::attachEnhanceDialogueSubmixGraph() could not allocate mixer bus (err = %d)"
+ "%25s:%-5d MEParallelPathSubmixGraph::attachEnhanceDialogueSubmixGraph() using mixer bus %u"
+ "%25s:%-5d MEParallelPathSubmixGraph::connectEnhanceDialogueSubmixGraph(%s) - EnhanceDialogue submix on bus %u"
+ "%25s:%-5d MEParallelPathSubmixGraph::connectEnhanceDialogueSubmixGraph() - main graph doesn't have a valid format yet"
+ "%25s:%-5d MEParallelPathSubmixGraph::detachEnhanceDialogueSubmixGraph() freed mixer bus %u"
+ "%25s:%-5d MESubmixGraph::rebuildChain() - EnhanceDialogueProcessor added to main mixer"
+ "%25s:%-5d MixTapToUplink@%p::FetchAndMix; discontinuityOccurredInMicTimeline. Expected = %lld. Actual = %lld"
+ "%25s:%-5d MixTapToUplink@%p::StopAudioTap;  released tap of session %s with microphoneInjectionMode %i"
+ "%25s:%-5d MixTapToUplinkGroupedByMicrophoneInjectionModeBuilder::build; %s"
+ "%25s:%-5d MixTapToUplinkGroupedByMicrophoneInjectionModeBuilder; new buildStates for microphoneInjectionModes: %s"
+ "%25s:%-5d New active audio route: %@"
+ "%25s:%-5d No built-in haptic pattern found for action ID or key %@"
+ "%25s:%-5d Phone call is %s now"
+ "%25s:%-5d Received buffer we did not enqueue, abl:  %lu"
+ "%25s:%-5d Recording implicitly allowed for AQIONodeClient %p hosted in audiomxd with no client audit token."
+ "%25s:%-5d Requested offload AirPods noise suppression mode is updated to = %s"
+ "%25s:%-5d Rescheduling buffer, abl: %lu"
+ "%25s:%-5d Restarting IO following route change"
+ "%25s:%-5d Route changed"
+ "%25s:%-5d SSID %d not eligible for pattern replacement on a phone call"
+ "%25s:%-5d STSpeechTranslatorClient@%p: Received %d number of samples, abl %lu"
+ "%25s:%-5d STSpeechTranslatorClient@%p: Translate %d number of samples"
+ "%25s:%-5d STSpeechTranslatorClient@%p: created client for scope %s"
+ "%25s:%-5d STSpeechTranslatorClient@%p: lookUpPreferredInputAudioFormatWithCompletionHandler succeeded but format is null!"
+ "%25s:%-5d STSpeechTranslatorClient@%p: lookUpPreferredInputAudioFormatWithCompletionHandler succeeded with format: %s"
+ "%25s:%-5d STSpeechTranslatorClient@%p: lookUpPreferredInputAudioFormatWithCompletionHandler timed out!"
+ "%25s:%-5d STSpeechTranslatorClient@%p: server disconnected"
+ "%25s:%-5d STSpeechTranslatorClient@%p: set state %d"
+ "%25s:%-5d STSpeechTranslatorClient@%p: setting client's produceAudio value to %i for scope %s"
+ "%25s:%-5d STSpeechTranslatorClient@%p: translation did stop with error: %d"
+ "%25s:%-5d SetCallTranslationProperties; could not create translator. gInstance is null!"
+ "%25s:%-5d SetCallTranslationProperties; gInstance is not initialized!"
+ "%25s:%-5d SetMixResolution: %d"
+ "%25s:%-5d SetMixTapToTelephonyUplinkAllowedByUser(%p); allowedByUser=%i"
+ "%25s:%-5d SetProperty %d : media chat [%s], VP mode %d (no-op)"
+ "%25s:%-5d Setting VP host application ID to %s"
+ "%25s:%-5d Sound check changed: %s"
+ "%25s:%-5d Starting vibe now, actionID %d. Vibe format: %s"
+ "%25s:%-5d Stopping vibe for ssid %d for pid %d. Vibe format: %s"
+ "%25s:%-5d Stopping vibe for ssid %d. Vibe format: %s"
+ "%25s:%-5d TapSubmix@%p: mute local playback on channel@%p"
+ "%25s:%-5d TapSubmix@%p: mute local playback on channel@%p "
+ "%25s:%-5d TapSubmix@%p: unmute local playback on channel@%p"
+ "%25s:%-5d TapSubmix@%p: unmute local playback on channel@%p "
+ "%25s:%-5d TranslationConfiguration::Create; callTranslationProperties: %s"
+ "%25s:%-5d TranslationConfiguration::create; dictionary could not be parsed."
+ "%25s:%-5d TranslationConfiguration::createAudioStreamTranslationConfiguration; stream configuration given incorrectly formatted translator token!"
+ "%25s:%-5d TranslationConfiguration::createAudioStreamTranslationConfiguration; stream configuration is missing translator token!"
+ "%25s:%-5d TranslationFeedbackInjector@%p: audio format converter not needed for target scope %s"
+ "%25s:%-5d TranslationFeedbackInjector@%p: created audio format converter from source format <%s> to destination format <%s> for source scope %s"
+ "%25s:%-5d TranslationFeedbackInjector@%p: inputMuted %i for target scope %s"
+ "%25s:%-5d TranslationFeedbackInjector@%p: translation feedback enabled of %s to %s"
+ "%25s:%-5d TranslatorClient@%p: sEnableCapture = %d"
+ "%25s:%-5d TranslatorClient@%p::StartCapture; Failed to start audio capturer"
+ "%25s:%-5d TranslatorClient@%p::StartCapture; Starting capture to %s with format %s"
+ "%25s:%-5d TranslatorClient@%p::StopCapture; Stopping audio capturer %s"
+ "%25s:%-5d TranslatorClientDelegate::didGenerateTranslatedAudio; scope: %s"
+ "%25s:%-5d Using hardware volume for AID6002"
+ "%25s:%-5d VoiceProcessor does not have SpatialMetadata. status=%i, outDataSize=%i"
+ "%25s:%-5d VoiceTrigger XPC is not supported"
+ "%25s:%-5d [ATAudioTapDescription initProcessTapWithFormat:PID:deviceUID] not implemented yet!"
+ "%25s:%-5d _changeMixFormat:graph=%p, mixer=%p, fmt=%s"
+ "%25s:%-5d allowEnhanceDialogue called on platform where gCASUseMediaExperience is false"
+ "%25s:%-5d aq@%p: EnhanceableMuteStateChanged, setting kMESubmixProperty_EnhanceDialogueRouteChanged"
+ "%25s:%-5d aqmeio@%p: deviceID %d, could not %s audit token, error %d"
+ "%25s:%-5d checkForceLPCMForEnhanceDialogue: Error %d (%s) getting force LPCM state for device ID %d"
+ "%25s:%-5d checkForceLPCMForEnhanceDialogue: Error %d (%s) setting force LPCM for Enhance Dialogue for device ID %d"
+ "%25s:%-5d checkForceLPCMForEnhanceDialogue: Keeping force LPCM = %s for device ID %x"
+ "%25s:%-5d checkForceLPCMForEnhanceDialogue: Setting force LPCM = %s for device ID %x"
+ "%25s:%-5d client %s: using STS with mSTSLabel=%@ and AU=%p"
+ "%25s:%-5d co-listen is %s, VP media chat %d, VP mode %d, VP as external volume handler = %d"
+ "%25s:%-5d codec.GetProperty(kAudioCodecPrivatePropertyContentOrigin) returns unknown OS type: %d, defaulting"
+ "%25s:%-5d codec.GetProperty(kAudioCodecPrivatePropertyContentOrigin) returns unknown source: %d, defaulting"
+ "%25s:%-5d device %s persisted = %d across a route change"
+ "%25s:%-5d device persisted initial state %d, persistedReason %d"
+ "%25s:%-5d error %d setting mLMLoudnessNormalizerUnit ParameterID %d with ParameterValue %f"
+ "%25s:%-5d error %d setting mLMLoudnessNormalizerUnit input format"
+ "%25s:%-5d error %d setting mLMLoudnessNormalizerUnit kAudioUnitProperty_AudioChannelLayout"
+ "%25s:%-5d error %d setting mLMLoudnessNormalizerUnit output format"
+ "%25s:%-5d found media kind in LID: %s"
+ "%25s:%-5d hasPermissionToMixTapToUplink; audioSessionToTap=0x%x does not have permission to bypass the mic mute. Has entitlement? %i Feature is enabled? %i microphoneInjectionMode? %i"
+ "%25s:%-5d ionc@%p offline %s, Sound Check %s%s, flags 0x%x, err %d, scalar %.3f"
+ "%25s:%-5d ionc@%p: currentVolume %5.3f, mVolume[%d] %5.3f, outAnyRamping %d, anyTaps %d"
+ "%25s:%-5d mAudioStreamTranslationProvider is null? %i"
+ "%25s:%-5d mSpatializationUnit is not valid, using inputformat"
+ "%25s:%-5d not %s the voice processor, session id: 0x%x does not match the voice processor's session id: 0x%x"
+ "%25s:%-5d parse of LoudnessManager plist failed: error %d: no reason available"
+ "%25s:%-5d return dictionary is null"
+ "%25s:%-5d rio@%p: EnhanceableMuteStateChanged, setting kMESubmixProperty_EnhanceDialogueRouteChanged"
+ "%25s:%-5d rio@%p: input mute %d"
+ "%25s:%-5d setting kMELMLoudnessNormalizerProperty_AlgorithmVersion failed with error: %d"
+ "%25s:%-5d setting kMELMLoudnessNormalizerProperty_DownwardCompressionRange failed with error: %d"
+ "%25s:%-5d setting kMELMLoudnessNormalizerProperty_DownwardCompressionRatio failed with error: %d"
+ "%25s:%-5d setting kMELMLoudnessNormalizerProperty_EnableCompressor failed with error: %d"
+ "%25s:%-5d setting kMELMLoudnessNormalizerProperty_EnableOutputCeiling failed with error: %d"
+ "%25s:%-5d setting kMELMLoudnessNormalizerProperty_ExpectedLoudnessAfterReset failed with error: %d"
+ "%25s:%-5d setting kMELMLoudnessNormalizerProperty_InputGain failed with error: %d"
+ "%25s:%-5d setting kMELMLoudnessNormalizerProperty_LookaheadDelayMS failed with error: %d"
+ "%25s:%-5d setting kMELMLoudnessNormalizerProperty_LoudnessTarget failed with error: %d"
+ "%25s:%-5d setting kMELMLoudnessNormalizerProperty_MaxGain failed with error: %d"
+ "%25s:%-5d setting kMELMLoudnessNormalizerProperty_OutputCeiling failed with error: %d"
+ "%25s:%-5d setting kMELMLoudnessNormalizerProperty_PeakLevelOffset failed with error: %d"
+ "%25s:%-5d setting kMELMLoudnessNormalizerProperty_RenderQuality failed with error: %d"
+ "%25s:%-5d setting kMELMLoudnessNormalizerProperty_ResetMode failed with error: %d"
+ "%25s:%-5d setting kMELMLoudnessNormalizerProperty_ResetTimeout failed with error: %d"
+ "%25s:%-5d setting kMELMLoudnessNormalizerProperty_SideChainHighPassFrequency failed with error: %d"
+ "%25s:%-5d setting kMELMLoudnessNormalizerProperty_UpwardCompressionRange failed with error: %d"
+ "%25s:%-5d setting kMELMLoudnessNormalizerProperty_WeightingFilter failed with error: %d"
+ "%25s:%-5d setting mLMLoudnessNormalizerUnit input format to %s"
+ "%25s:%-5d setting mLMLoudnessNormalizerUnit output format to %s"
+ "%25s:%-5d setting unknown property '%s' on kMEProcessor_LM_LoudnessNormalizer"
+ "%25s:%-5d started analytics (%p) with CAReporterID (%lld) with config %s"
+ "%25s:%-5d unable to make URL for LoudnessManager plist file path"
+ "%25s:%-5d ~CallTranslator(%p)"
+ "%p stopping after freewheeling"
+ "%s: Abandoning I/O cycle because we were requested to render more frames: %dthan the maximum frame count: %d."
+ "%s: IOProc expected %d, got %d frames"
+ "%sAUAudioMix: "
+ "%sLoudnessManagerAULNUnit: "
+ "'%s' | %sData{%d} | %d bytes\n"
+ "'%s' | <unknown type id: %d)>\n"
+ "'%s' | Array{%d} | %d ordered objects\n"
+ "'%s' | Dictionary{%d} | %d key/value pairs\n"
+ "'%s' | Number(SInt16){%d} | 0x%04x\n"
+ "'%s' | Number(SInt32){%d} | %-6d 0x%08x %c%c%c%c\n"
+ "'%s' | Number(SInt8){%d} | 0x%02x\n"
+ "'%s' | Number(float){%d} | %f\n"
+ "'%s' | String{%d} | \"%s\"\n"
+ "(((1 && !0) && !0 && !0) && !CASIsDarwinOS())"
+ "(AudioObjectGetPropertyData(kAudioObjectSystemObject, &addr, 0, __null, &dataSize, &avt)) == 0"
+ "(AudioUnitSetProperty(mUnit.AU(), kAudioUnitProperty_ScheduleRateRamps, kAudioUnitScope_Global, 0, mSavedRateRamps.mRamps->data(), static_cast<UInt32>(mSavedRateRamps.mRamps->size() * sizeof(AURateRampStruct)))) == 0"
+ "(EDP initialized)"
+ "(client.GetTopologyFlags() & kAudioQueueFlag_HardwarePassthrough) != 0"
+ "(err = AudioFormatGetProperty(kAudioFormatProperty_OutputFormatList, sizeof(afi), &afi, &formatListSize, mCodecOutputFormats.get())) == 0"
+ "(err = AudioFormatGetPropertyInfo(kAudioFormatProperty_OutputFormatList, sizeof(afi), &afi, &formatListSize)) == 0"
+ "(err = This->mProcessingChain.back()->Render(ioActionFlags, inTimeStamp, 0, inNumberFrames, ioData)) == 0"
+ "(m)"
+ "(mDeferredRenderer.Render(&actionFlags, &outputTime, busIndex, numFrames, upstr.mABL)) == 0"
+ "(mDestinationGraph == nullptr || mIsParallelPathSubmix) && !mIsTapSubmix"
+ "(mIONode.AddIOClient(*this)) == 0"
+ "(mwt)"
+ "(notify_register_dispatch(\"com.apple.accessibility.hac.status\", &token, AudioControlQueue(), ^(int token) { AT::ScopedACQBlock scopedACQBlock(\"notify_register_dispatch\", __func__, \"DSP_Routing_VP.cpp\" , 456); do { auto logobj = CALog::LogObjIfEnabled(5, gAQMELogScope); if (logobj) __extension__({ os_log_t _log_tmp = ((logobj)); os_log_type_t _type_tmp = (OS_LOG_TYPE_DEBUG); if (os_log_type_enabled(_log_tmp, _type_tmp)) { __extension__({ _Pragma(\"clang diagnostic push\") _Pragma(\"clang diagnostic ignored \\\"-Wvla\\\"\") _Pragma(\"clang diagnostic error \\\"-Wformat\\\"\") _Static_assert(__builtin_constant_p(\"%25s:%-5d \" \"HACStatusChanged %p\"), \"format/label/description argument must be a string constant\"); __attribute__((section(\"__TEXT,__oslogstring,cstring_literals\"),internal_linkage)) static const char _os_fmt_str[] __asm(\"LOS_LOG877\") = \"%25s:%-5d \" \"HACStatusChanged %p\"; uint8_t _Alignas(16) __attribute__((uninitialized)) _os_fmt_buf[__builtin_os_log_format_buffer_size(\"%25s:%-5d \" \"HACStatusChanged %p\", \"DSP_Routing_VP.cpp\", 457, gInstance.load())]; _os_log_impl(&__dso_handle, _log_tmp, _type_tmp, _os_fmt_str, (uint8_t *)__builtin_os_log_format(_os_fmt_buf, \"%25s:%-5d \" \"HACStatusChanged %p\", \"DSP_Routing_VP.cpp\", 457, gInstance.load()), (uint32_t)sizeof(_os_fmt_buf)) _Pragma(\"clang diagnostic pop\"); }); } }); } while (0); std::unique_lock locker1(mgr.GetMutex()); if (gInstance) { gInstance.load()->mParent.TriggerAdaptToDevice(); } })) == 0"
+ "*** done.\n"
+ ". Curve has one point and would receive flat segment extension to a later curve"
+ ".plist"
+ "/Library/Audio/Tunings/Generic/Haptics/SystemSounds/Library/systemsoundhapticpatterns.plist"
+ "/Library/Audio/Tunings/Generic/SpeechTranslation"
+ "/System/Library/PrivateFrameworks/VoiceProcessor.framework/VoiceProcessor"
+ "0 != (client.GetTopologyFlags() & kAudioQueueFlag_IsPhaseAQIONodeClient)"
+ "2A$0"
+ "<%@@%p: process tap - pids:%@, name:%@, UUID:%@, format:%@, excluded pids:%@"
+ "<AudioQueueObject@%p; %s; %s; %s>"
+ "="
+ "=null) "
+ "@\"NSDictionary\"28@0:8I16@\"NSDictionary\"20"
+ "@28@0:8I16@20"
+ "@36@0:8@16i24@28"
+ "@36@0:8r^{AudioStreamBasicDescription=dIIIIIIII}16I24^@28"
+ "@36@0:8{weak_ptr<AT::Translation::TranslatorClient>=^{TranslatorClient}^{__shared_weak_count}}16i32"
+ "@40@0:8r^{AudioStreamBasicDescription=dIIIIIIII}16I24B28^@32"
+ "@60@0:8f16B20^v24^?32^?40^?48B56"
+ "@@ Strips May 28 2025 04:45:26"
+ "ACQContextAssertion"
+ "AID%d"
+ "AQME.h"
+ "AQMEDevice_Init_block_invoke"
+ "AQMEIO: %s stream %d: %u b, %u b/fr => %u fr"
+ "AQME_LoudnessManager_AULN"
+ "ASSERTION FAILED: default AU still set to one that will be destroyed"
+ "ASSERTION FAILED: sequence was not previously unregistered"
+ "ATBlurMixer"
+ "ATBlurMixer.mm"
+ "ATBlurMixer@%p(%s): Error getting parameter BlurOnOff, err = %d"
+ "ATBlurMixer@%p(%s): Error setting parameter BlurOnOff, err = %d"
+ "ATHALREF"
+ "AUAsyncRendererHost.mm"
+ "AUAsyncRendererHost@%p: ProcessAudio scope = input, error: %d"
+ "AUAsyncRendererHost@%p: ProcessAudio scope = output, error: %d"
+ "AUIOServer_StopIO"
+ "AULN_AlgorithmVersion"
+ "AULN_DownwardCompressionRange"
+ "AULN_DownwardCompressionRatio"
+ "AULN_EnableCompressor"
+ "AULN_EnableOutputCeiling"
+ "AULN_InputGain"
+ "AULN_LookaheadDelayMS"
+ "AULN_LoudnessAfterReset"
+ "AULN_LoudnessTarget"
+ "AULN_MaxGain"
+ "AULN_OutputCeiling"
+ "AULN_OutputGain"
+ "AULN_PeakLevelOffset"
+ "AULN_RenderQuality"
+ "AULN_ResetMode"
+ "AULN_ResetTimeout"
+ "AULN_SideChainHighPassFrequency"
+ "AULN_UpwardCompressionRange"
+ "AULN_UseDownwardCompressionRatio"
+ "AULN_WeightingFilter"
+ "AUPreset"
+ "AVAudioPCMBuffer"
+ "AVHapticServerInstance_createCustomAudioEvent"
+ "AVVoiceTriggerManager.mm"
+ "AVVoiceTriggerServer"
+ "AVVoiceTriggerServer.mm"
+ "AVVoiceTriggerServer.notification"
+ "AVVoiceTriggerServerHysteresisNotifier"
+ "AVVoiceTriggerServerPortManager"
+ "AV_Spatial_Live"
+ "AV_Spatial_Offline"
+ "AV_Traditional_Live"
+ "AV_Traditional_Offline"
+ "Atmos_9_1_6_Decoder"
+ "AudioBuffersBase.PrepareNull failed"
+ "AudioCallTranslation"
+ "AudioCallTranslationLocalFeedback"
+ "AudioCallTranslationRemoteFeedback"
+ "AudioDSPGraph"
+ "AudioDSPGraphFramework_AudioDSP"
+ "AudioFormatChanged"
+ "AudioIPCUtility.h"
+ "AudioQueueIOBindingChanged"
+ "AudioStreamTranslator.mm"
+ "AudioTapHALReferenceStream.mm"
+ "AudioTapUtilities::CanTapPhase(tapSpecifier())"
+ "AudioTranslationInjector.mm"
+ "AudioTranslationInjector@%p: AUAsyncRenderer returned error = %d"
+ "AudioTranslationInjector@%p: BlurredMixed ABL is null"
+ "AudioTranslationInjector@%p: Translated ABL is null"
+ "Automation track did not have intra-event seeking enabled"
+ "B24@?0@\"AVHapticEvent\"8@\"NSDictionary\"16"
+ "B32@0:8r^{AudioStreamBasicDescription=dIIIIIIII}16^@24"
+ "Bluetooth"
+ "BlurringMixerDSPGraphHost.mm"
+ "BlurringMixerDSPGraphHost@%p(%s): Error setting parameter BlurOnOff, err = %d"
+ "BlurringMixerDSPGraphHost@%p(%s): ProcessAudio returned error: %d"
+ "CACFPreferences.cpp"
+ "CallTranslator.mm"
+ "CallTranslatorBase"
+ "Called without a sequence"
+ "Capture_Spatial"
+ "Capture_Spatial_Enhanced"
+ "Capture_Traditional"
+ "Class getAVAudioPCMBufferClass()_block_invoke"
+ "Class getRBSProcessPredicateClass()_block_invoke"
+ "Class getSTSpeechTranslatorClientClass()_block_invoke"
+ "ClientCapture"
+ "ClientProcessTaskToken"
+ "ConnectToIONodeEffects"
+ "Copy"
+ "Create"
+ "DEBUG_FRAMESIZE: expected %d, got %d frames"
+ "Data"
+ "DecoderHandlesDRC"
+ "DefaultShort_ReceiverActive"
+ "DefaultShort_SpeakerphoneActive"
+ "Delete"
+ "Disabled"
+ "DuckingHoldTimeSeconds"
+ "EnableTelephonyMonitor"
+ "Enabled"
+ "EnhanceDialogue"
+ "EnhanceDialogueParallel"
+ "EnhanceDialogueProcessor"
+ "EnhanceDialogue_sidechain"
+ "EnhanceDialogue_visionos"
+ "Error loading plist file "
+ "Event track not found, earlier code should have added one"
+ "GetBlurHoldTimeSec"
+ "GetUpdatedAudioChannelLayoutTagFromDescriptionsOrBitmap"
+ "I20@0:8I16"
+ "IONodeClientCount() < 2"
+ "IONodeSession.mm"
+ "LateNightMode+SoundCheck"
+ "LoudnessManagerV2"
+ "MEEnhanceableSubmixGraph"
+ "MEEnhanceableSubmixGraph@%p couldn't get mInitializationLock"
+ "MEParallelPathSubmixGraph.cpp"
+ "MEParallelPathSubmixGraph.h"
+ "MESubmixGraph"
+ "MixTapToUplink("
+ "MixTapToUplink@%p::FetchAndMix failed. Read from timeStamp = %lld returned error %i. Buffer has %lld samples from %lld to %lld. mSampleToStartRead = %lld. nFrames = %i. mSampleToStartRead is %lld samples ahead. outNumValidFrames=%i, outNumLeadingZeroes=%i outNumTrailingZeroes=%i"
+ "MixTapToUplink@%p::Store; discontinuity occurred in tap timeline. Setting mSampleTimeForStartOfTimeline = %lld"
+ "MixTapToUplinkHost.h"
+ "Music_Spatial"
+ "Music_Traditional"
+ "Muting"
+ "New graph creation should not fail"
+ "No event tracks in sequence! This is not a valid sequence"
+ "Noise Suppression"
+ "Noise Suppression Studio"
+ "Old track to be replaced not found in sequence"
+ "PlaySystemSoundOption_CallerIdentifier"
+ "PlaySystemSoundOption_PrefersToPlayAudioToHeadphonesOnly"
+ "PreDSPSpeakerTap.aggregate"
+ "PushMicInput allocated %d fr, trying to render %d"
+ "PushTapInput allocated %d fr, trying to render %d"
+ "RBSProcessPredicate"
+ "Recreate"
+ "RefreshMixTapToUplinkInstances"
+ "RemoteIOServerBase dummy lock"
+ "SC_LoudnessTarget"
+ "SC_MaxPeakLevel"
+ "SSID"
+ "STSpeechTranslatorClient"
+ "STSpeechTranslatorClientDelegate"
+ "ScheduledSlicePlayer2.cpp"
+ "ScheduledSlicePlayerV2"
+ "Seeked to t=0 on automation track %u but returned event was at t=%f"
+ "Sequence shouldn't be gone!"
+ "SessionRoutingInfoIsolationSupport"
+ "SetCallTranslationProperties"
+ "SetDecoderChannelLayout"
+ "SetTimeConstraints: thread_policy_set failed, Error: %d (%s)"
+ "SharePlayInCalls"
+ "SoundCheck"
+ "SourceLoudness"
+ "SpeakerAndMicrophone"
+ "SpeechTranslator-Downlink-WithRemoteFeedback.austrip"
+ "SpeechTranslator-Downlink-WithRemoteFeedback.dspg"
+ "SpeechTranslator-Downlink-WithRemoteFeedback.propstrip"
+ "SpeechTranslator-Downlink.austrip"
+ "SpeechTranslator-Downlink.dspg"
+ "SpeechTranslator-Downlink.propstrip"
+ "SpeechTranslator-Host.plist"
+ "SpeechTranslator-Uplink.austrip"
+ "SpeechTranslator-Uplink.dspg"
+ "SpeechTranslator-Uplink.propstrip"
+ "SpokenAudioBypassesMicMuteAndLocalPlayback"
+ "Supported_Hardware"
+ "Synchonized looping sequence should have a synchronizer here!"
+ "T@?,R,N"
+ "TB,N,GisBlurEnabled"
+ "TB,R,N,V_isUplink"
+ "TPLM"
+ "Tap of session(s) "
+ "Temp track should exist during edit!"
+ "Temp track should not already exist!"
+ "Tf,N"
+ "TimePitch"
+ "Tq,N,V_muteBehavior"
+ "TranscriptTranslation"
+ "Translation"
+ "TranslationConfiguration.mm"
+ "TranslationFeedbackInjector.mm"
+ "TranslatorClientDelegate"
+ "TuningPListMgr.cpp"
+ "UInt32"
+ "Unmuting"
+ "UpdateFormats"
+ "XPC_ProcessTaskToken"
+ "Zero-velocity note on should not be here"
+ "[%u]"
+ "\\\""
+ "\\\\"
+ "\\b"
+ "\\f"
+ "\\n"
+ "\\r"
+ "\\t"
+ "\\u"
+ "^{AVVoiceTriggerServerImpl=^^?I^{HALListener}^{HALListener}^{HALListener}i**BBBBB@@i^{unfair_recursive_lock}@BI@}"
+ "^{OpaqueAudioComponentInstance=}16@0:8"
+ "_IDBeingStarted == kNoSequenceID"
+ "_IDBeingStarted == kNoSequenceID || _IDBeingStarted == inID"
+ "__null != gUserList"
+ "__null != mCPMSSharedInstanceForHaptics"
+ "__objc_no != success"
+ "_channelIDsToBeDetached.size() == 0"
+ "_initCount > 0"
+ "_isUplink"
+ "_muteBehavior"
+ "_startCount == 0"
+ "_startCount > 0 && _startCount < 3"
+ "_state != Uninitialized || inState == Stopped"
+ "_state == Uninitialized"
+ "_stoppedDuringFlush == false"
+ "abl->mNumberBuffers == outputBuffers->mNumberBuffers"
+ "activeSoundInfo != nullptr"
+ "add"
+ "addBeginningEvents"
+ "addInitialAutomationEvents"
+ "airpods noise suppression for studio mic"
+ "allocated %d fr, trying to render %d"
+ "allowEnhanceDialogue:"
+ "apply-custom-aqme-lm-auln-settings"
+ "aq"
+ "aq@%p: %s using invalid anchor time"
+ "aq_captureofflinerender"
+ "aq_captureoutput_decode"
+ "aq_captureoutput_enqueue"
+ "aq_decode"
+ "aq_enq"
+ "aq_offline"
+ "aqaudiocodec_in"
+ "aqaudiocodec_out"
+ "aqclient_capturetap"
+ "aqcodec_captureinput"
+ "aqcodec_captureoutput"
+ "aqme_captureclient"
+ "aqme_capturetimepitch"
+ "aqme_capturetranslation"
+ "aqmeio_captureoutput"
+ "array"
+ "arrayByAddingObjectsFromArray:"
+ "arrayWithArray:"
+ "at_ionodesession"
+ "audioBufferList"
+ "audioGenerationDidFinishForClient:"
+ "audioUnit"
+ "aupreset"
+ "avvoicetrigger"
+ "blendTimeMs"
+ "blurHoldTimeSec"
+ "buf->mBufferList->mNumberBuffers >= 1 && buf->mBufferList->mNumberBuffers <= 64"
+ "bufs.mNumberBuffers >= 1 && bufs.mNumberBuffers <= 64"
+ "bypass mode"
+ "bytesPerBuffer.has_value()"
+ "cancelHapticPattern"
+ "client-%p"
+ "client:didGenerateTranslatedAudio:"
+ "client:didPauseTranslationWithReason:"
+ "client:didReceiveTranscriptionResult:"
+ "client:didReceiveTranslationResult:"
+ "client:didStopTranslationWithError:"
+ "client:willStartTranslatedAudioWithMetadata:"
+ "clientAudioOutput != nullptr"
+ "clientID != 9999999"
+ "clientsWithProcess != _processIndexMap.end()"
+ "cm == __null"
+ "com.apple.coreaudio.utility"
+ "configure"
+ "consolidateAndPublishParameterCurves"
+ "currentBufferOffset <= int(inNumberFrames)"
+ "destABL.mBuffers[0].mDataByteSize >= inNumberFrames * mOutputFormat.mBytesPerFrame"
+ "doing nothing"
+ "donwlink"
+ "downlink"
+ "downlink-"
+ "downlinkTranslationEnabled"
+ "e < mElements.size()"
+ "e->mNumberParameters == 1"
+ "e->mParams[i].mID != kAudioQueueParam_PlayRate2"
+ "edp != nullptr"
+ "enableBlur"
+ "ended"
+ "entry->stopped()"
+ "err %d"
+ "err == noErr"
+ "error %d from VP"
+ "filterUsingPredicate:"
+ "force_headphone_output_type"
+ "forcedAQTimeStretcher"
+ "foundUserEvent == true"
+ "frameLength"
+ "frameOffset < (SInt32)numFrames"
+ "gAQMEMessenger != nullptr"
+ "gSpatialMetadataSPI"
+ "getAUStripPath"
+ "getAutomationValueAtTime"
+ "getBusCountForScope:"
+ "getDSPGraphPath"
+ "getMinimalRampDurationForValueDelta"
+ "getPropStripPath"
+ "guaranteePreservationPoint"
+ "handleForPredicate:error:"
+ "high priority "
+ "hostProcess"
+ "i24@0:8^{__CFString=}16"
+ "i32@0:8^{__CFDictionary=}16^{__CFDictionary=}24"
+ "i52@?0r^{AudioTimeStamp=dQdQ{SMPTETime=ssIIIssss}II}8I16r^{AudioBufferList=I[1{AudioBuffer=II^v}]}20r^{AudioBufferList=I[1{AudioBuffer=II^v}]}28^{AudioBufferList=I[1{AudioBuffer=II^v}]}36^{AudioBufferList=I[1{AudioBuffer=II^v}]}44"
+ "id < (1UL << 31)"
+ "inAudioToken"
+ "inChannels.size() <= mChannelStatus.size()"
+ "inID != kAudioQueueParam_PlayRate2"
+ "inState != Starting || _state == Stopped"
+ "initDownlinkWithFormat:maxFrames:error:"
+ "initInternalWithFormat:maxFrames:isUplink:error:"
+ "initProcessTapWithFormat:PID:deviceUID:"
+ "initUplinkWithFormat:maxFrames:error:"
+ "initWithPCMFormat:frameCapacity:"
+ "initWithRateLimit:detectPredictionAnchor:userContext:factory:execution:finalizer:useSleepWakeDetector:"
+ "initWithTime:value:"
+ "initWithTranslatorIdentifier:delegate:delegateQueue:"
+ "initWithType:relativeTime:shape:controlPoints:"
+ "initWithUUIDBytes:"
+ "initWithUUIDString:"
+ "initWithWeakImpl:scope:"
+ "initializeAU"
+ "input-"
+ "ioBufferList.mNumberBuffers == mRampBufferList->GetNumberBuffers()"
+ "ioByteSize <= mInputNumBytes"
+ "ioPackets <= mInputNumPackets"
+ "ioSize == sizeof(double)"
+ "ios%d"
+ "isBlurEnabled"
+ "isUplink"
+ "isXPCService"
+ "it != mInputStates.end()"
+ "it != mMixerChannels.end()"
+ "it != mSubmixGraph->mMixerChannels.end()"
+ "it != mainGraph.mSourceGraphs.end()"
+ "kEnhanceDialogueOptInBypass"
+ "kEnhanceDialogueOptInDisable"
+ "kEnhanceDialogueOptInEnable"
+ "kEnhanceableSessionMuted"
+ "kEnhanceableSessionNone"
+ "kEnhanceableSessionPlaying"
+ "keyEnumerator"
+ "keyrange.mHigh == keyrange.mLow"
+ "lastObject"
+ "legacy plist"
+ "lm-auln-algorithm-version"
+ "lm-auln-downward-compression-range"
+ "lm-auln-enable-compressor"
+ "lm-auln-look-ahead-delay-ms"
+ "lm-auln-loudness-after-reset"
+ "lm-auln-loudness-target"
+ "lm-auln-max-gain"
+ "lm-auln-output-ceiling"
+ "lm-auln-peak-level-offset"
+ "lm-auln-render-quality"
+ "lm-auln-reset-mode"
+ "lm-auln-reset-timeout"
+ "lm-auln-sidechain-highpass-frequency"
+ "lm-auln-upward-compression-range"
+ "lm-auln-weighting-filter"
+ "lm-disable-hardware-check"
+ "lookUpPreferredInputAudioFormatWithCompletionHandler:"
+ "loudness-manager-disable"
+ "loudness-manager-plist-path"
+ "mAUDSPGraph"
+ "mActiveHighPowerHapticsClients >= 0"
+ "mActivePriorityClientCountMap[HapticPlayerPriority::ExclusivePriority] != 0"
+ "mActivePriorityClientCountMap[HapticPlayerPriority::HighPriority] != 0"
+ "mActivePriorityClientCountMap[HapticPlayerPriority::HighestPriority] != 0"
+ "mAsyncRenderer.get() != nullptr"
+ "mAudioOutput != nullptr"
+ "mBlurHoldTimeSec"
+ "mBlurMixer != nil"
+ "mBlurMixer != nullptr"
+ "mBlurMixer->mAU != nullptr"
+ "mBlurMixer->mImpl != nullptr"
+ "mBufferCapacity == 0 || nBytes <= mBufferCapacity"
+ "mBufferMemory == __null"
+ "mCapturer->SetCookie(CFDataGetBytePtr(mMagicCookie), ToUInt32(CFDataGetLength(mMagicCookie))) == noErr"
+ "mCapturer->WriteBufferList(framesToRender, &abl) == noErr"
+ "mCapturer->WriteBufferList(playSlice->mSlice->mNumberFrames, playSlice->mSlice->mBufferList) == noErr"
+ "mClientInfo != __null"
+ "mClientRunMode != kRunMode_NotRunning"
+ "mDestinationTaps.empty()"
+ "mHapticOutput != nullptr"
+ "mIsInitialized"
+ "mMaxFrames"
+ "mMicInputCache already has value (indicates unexpected order of operations)"
+ "mNumAllocatedSlices == 0"
+ "mPowerManager != nullptr"
+ "mRemoteFeedbackFeatureEnabled"
+ "mSSSClientEntryRunningCount != 0"
+ "mScope"
+ "mStreamDescription"
+ "mSynthRingBuffer != nullptr"
+ "mTapSources.empty()"
+ "mTapStreamProcessed already true (indicates unexpected order of operations)"
+ "mTuningDirectory"
+ "mixerBus.has_value()"
+ "mutableAudioBufferList"
+ "muteBehavior"
+ "nextObject"
+ "nullptr == propertyValue"
+ "outPreferences"
+ "output-"
+ "output2 != nullptr"
+ "paramEvents.size() == mTapVolumes.size()"
+ "playHapticPattern"
+ "pos < Base::size()"
+ "pos <= int(inNumberFrames)"
+ "predicateMatchingBundleIdentifier:"
+ "predicateWithBlock:"
+ "proc != nullptr"
+ "produceAudio"
+ "publishControlPointToAutomationTrack"
+ "q24@?0@\"AVHapticEvent\"8@\"AVHapticEvent\"16"
+ "reachedOffset0"
+ "remove"
+ "removing"
+ "resetting codec"
+ "serverDidDisconnectForClient:"
+ "setAUStrip:propertyStrip:"
+ "setBlendTimeMs:"
+ "setDSPGraph:"
+ "setElementCount:"
+ "setEnableBlur:"
+ "setFormat:"
+ "setFrameLength:"
+ "setIOPropertiesForSession:values:"
+ "setIntendedSpatialExperience:reply:"
+ "setLMAULNAlgorithmVersion"
+ "setLMAULNDownwardCompressionRange"
+ "setLMAULNDownwardCompressionRatio"
+ "setLMAULNEnableCompressor"
+ "setLMAULNEnableOutputCeiling"
+ "setLMAULNInputGain"
+ "setLMAULNLookaheadDelayMS"
+ "setLMAULNLoudnessAfterReset"
+ "setLMAULNLoudnessTarget"
+ "setLMAULNMaxGain"
+ "setLMAULNOutputCeiling"
+ "setLMAULNOutputGain"
+ "setLMAULNPeakLevelOffset"
+ "setLMAULNRenderQuality"
+ "setLMAULNResetMode"
+ "setLMAULNResetTimeout"
+ "setLMAULNSideChainHighPassFrequency"
+ "setLMAULNUpwardCompressionRange"
+ "setLMAULNUseDownwardCompressionRatio"
+ "setLMAULNWeightingFilter"
+ "setMaxFramesPerSlice"
+ "setMuteBehavior:"
+ "setProduceAudio:"
+ "setTime:"
+ "setVersion:"
+ "setupAU"
+ "softlink:r:path:/System/Library/PrivateFrameworks/SpeechTranslation.framework/SpeechTranslation"
+ "sortedArrayUsingComparator:"
+ "srcFormat.mSampleRate == destFormat.mSampleRate || mTimestampGenerator != __null"
+ "started"
+ "startingInterrupt"
+ "success == false"
+ "tapConnection.has_value()"
+ "tapout"
+ "tapsrc"
+ "taskTokenDictionary"
+ "timepitch-%p"
+ "track != 0"
+ "translateAudioSamples:"
+ "translation-"
+ "translationDidResumeForClient:"
+ "translationDidStartForClient:"
+ "translationMode"
+ "translation_ducking_hold_time"
+ "translation_remote_feedback"
+ "ts2.mFlags & kAudioTimeStampHostTimeValid"
+ "uninitializeAU"
+ "unordered_map::at: key not found"
+ "updateFormat:error:"
+ "updateFormats"
+ "uplink"
+ "uplink-"
+ "uplinkTranslationEnabled"
+ "v16@?0@\"AVAudioFormat\"8"
+ "v16@?0r^{AudioBufferList=I[1{AudioBuffer=II^v}]}8"
+ "v20@?0r^{AudioBufferList=I[1{AudioBuffer=II^v}]}8B16"
+ "v24@0:8@\"STSpeechTranslatorClient\"16"
+ "v32@0:8@\"CASpatialAudioExperience\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"STSpeechTranslatorClient\"16@\"AVAudioPCMBuffer\"24"
+ "v32@0:8@\"STSpeechTranslatorClient\"16@\"NSError\"24"
+ "v32@0:8@\"STSpeechTranslatorClient\"16@\"NSString\"24"
+ "v32@0:8@\"STSpeechTranslatorClient\"16@\"STGeneratedAudioMetadata\"24"
+ "v32@0:8@\"STSpeechTranslatorClient\"16@\"STTranscriptionResult\"24"
+ "v32@0:8@\"STSpeechTranslatorClient\"16@\"STTranslationResult\"24"
+ "v32@0:8@16@24"
+ "vector.h"
+ "version"
+ "voiceisolation_all_apps"
+ "void *SpeechTranslationLibrary()"
+ "{AQMESession=\"mProcessID\"i\"mSessionID\"I\"mSourceSessionID\"{optional<unsigned int>=\"\"(?=\"__null_state_\"c\"__val_\"I)\"__engaged_\"B}\"mSubsessionRef\"{ObjectRef<const void *>=\"mCFObject\"^v}\"mSubsessionID\"Q\"mDescription\"{basic_string<char, std::char_traits<char>, std::allocator<char>>=\"__rep_\"(__rep=\"__s\"{__short=\"__data_\"[23c]\"__size_\"b7\"__is_long_\"b1}\"__l\"{__long=\"__data_\"*\"__size_\"Q\"__cap_\"b63\"__is_long_\"b1})}\"mOneWordID\"i\"mBundleID\"{optional<applesauce::CF::StringRef>=\"\"(?=\"__null_state_\"c\"__val_\"{StringRef=\"mObject\"{ObjectRef<const __CFString *>=\"mCFObject\"^{__CFString}}})\"__engaged_\"B}}"
+ "{StreamDescription=\"mSampleRate\"d\"mFormatID\"I\"mFormatFlags\"I\"mBytesPerPacket\"I\"mFramesPerPacket\"I\"mBytesPerFrame\"I\"mChannelsPerFrame\"I\"mBitsPerChannel\"I\"mReserved\"I}"
+ "{StringRef={ObjectRef<const __CFString *>=^{__CFString}}}16@0:8"
+ "{basic_string<char, std::char_traits<char>, std::allocator<char>>=\"__rep_\"(__rep=\"__s\"{__short=\"__data_\"[23c]\"__size_\"b7\"__is_long_\"b1}\"__l\"{__long=\"__data_\"*\"__size_\"Q\"__cap_\"b63\"__is_long_\"b1})}"
+ "{map<int, std::bitset<255>, std::less<int>, std::allocator<std::pair<const int, std::bitset<255>>>>=\"__tree_\"{__tree<std::__value_type<int, std::bitset<255>>, std::__map_value_compare<int, std::__value_type<int, std::bitset<255>>, std::less<int>>, std::allocator<std::__value_type<int, std::bitset<255>>>>=\"__begin_node_\"^v\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}\"__size_\"Q}}"
+ "{map<std::string, std::shared_ptr<NewNotificationCenterObserver>, std::less<std::string>, std::allocator<std::pair<const std::string, std::shared_ptr<NewNotificationCenterObserver>>>>=\"__tree_\"{__tree<std::__value_type<std::string, std::shared_ptr<NewNotificationCenterObserver>>, std::__map_value_compare<std::string, std::__value_type<std::string, std::shared_ptr<NewNotificationCenterObserver>>, std::less<std::string>>, std::allocator<std::__value_type<std::string, std::shared_ptr<NewNotificationCenterObserver>>>>=\"__begin_node_\"^v\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}\"__size_\"Q}}"
+ "{map<std::string, std::shared_ptr<OldNotificationCenterObserver>, std::less<std::string>, std::allocator<std::pair<const std::string, std::shared_ptr<OldNotificationCenterObserver>>>>=\"__tree_\"{__tree<std::__value_type<std::string, std::shared_ptr<OldNotificationCenterObserver>>, std::__map_value_compare<std::string, std::__value_type<std::string, std::shared_ptr<OldNotificationCenterObserver>>, std::less<std::string>>, std::allocator<std::__value_type<std::string, std::shared_ptr<OldNotificationCenterObserver>>>>=\"__begin_node_\"^v\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}\"__size_\"Q}}"
+ "{map<unsigned int, NSMutableArray<AVServerWrapper *> *, std::less<unsigned int>, std::allocator<std::pair<const unsigned int, NSMutableArray<AVServerWrapper *> *>>>=\"__tree_\"{__tree<std::__value_type<unsigned int, NSMutableArray<AVServerWrapper *> *>, std::__map_value_compare<unsigned int, std::__value_type<unsigned int, NSMutableArray<AVServerWrapper *> *>, std::less<unsigned int>>, std::allocator<std::__value_type<unsigned int, NSMutableArray<AVServerWrapper *> *>>>=\"__begin_node_\"^v\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}\"__size_\"Q}}"
+ "{stack<unsigned long, std::deque<unsigned long>>=\"c\"{deque<unsigned long, std::allocator<unsigned long>>=\"__map_\"{__split_buffer<unsigned long *, std::allocator<unsigned long *>>=\"__first_\"^^Q\"__begin_\"^^Q\"__end_\"^^Q\"__cap_\"^^Q}\"__start_\"Q\"__size_\"Q}}"
+ "{unique_ptr<AudioSessionPropertyListeners, std::default_delete<AudioSessionPropertyListeners>>=\"__ptr_\"^{AudioSessionPropertyListeners}}"
+ "{unique_ptr<OpaqueAudioComponentInstance, applesauce::raii::detail::opaque_deletion_functor<OpaqueAudioComponentInstance *, &AudioComponentInstanceDispose>>=\"__ptr_\"^{OpaqueAudioComponentInstance}}"
+ "{unique_ptr<Phase::ServerManager, std::default_delete<Phase::ServerManager>>=\"__ptr_\"^{ServerManager}}"
+ "{unordered_map<std::string, STSPerLabelControllerState, std::hash<std::string>, std::equal_to<std::string>, std::allocator<std::pair<const std::string, STSPerLabelControllerState>>>=\"__table_\"{__hash_table<std::__hash_value_type<std::string, STSPerLabelControllerState>, std::__unordered_map_hasher<std::string, std::__hash_value_type<std::string, STSPerLabelControllerState>, std::hash<std::string>, std::equal_to<std::string>>, std::__unordered_map_equal<std::string, std::__hash_value_type<std::string, STSPerLabelControllerState>, std::equal_to<std::string>, std::hash<std::string>>, std::allocator<std::__hash_value_type<std::string, STSPerLabelControllerState>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, STSPerLabelControllerState>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, STSPerLabelControllerState>, void *> *> *>>>=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, STSPerLabelControllerState>, void *> *> *>>=\"__size_\"Q}}\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, STSPerLabelControllerState>, void *> *>=\"__next_\"^v}\"__size_\"Q\"__max_load_factor_\"f}}"
+ "{unordered_map<unsigned int, std::unordered_set<void *>, std::hash<unsigned int>, std::equal_to<unsigned int>, std::allocator<std::pair<const unsigned int, std::unordered_set<void *>>>>=\"__table_\"{__hash_table<std::__hash_value_type<unsigned int, std::unordered_set<void *>>, std::__unordered_map_hasher<unsigned int, std::__hash_value_type<unsigned int, std::unordered_set<void *>>, std::hash<unsigned int>, std::equal_to<unsigned int>>, std::__unordered_map_equal<unsigned int, std::__hash_value_type<unsigned int, std::unordered_set<void *>>, std::equal_to<unsigned int>, std::hash<unsigned int>>, std::allocator<std::__hash_value_type<unsigned int, std::unordered_set<void *>>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, std::unordered_set<void *>>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, std::unordered_set<void *>>, void *> *> *>>>=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, std::unordered_set<void *>>, void *> *> *>>=\"__size_\"Q}}\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, std::unordered_set<void *>>, void *> *>=\"__next_\"^v}\"__size_\"Q\"__max_load_factor_\"f}}"
+ "{weak_ptr<AT::Translation::TranslatorClient>=\"__ptr_\"^{TranslatorClient}\"__cntrl_\"^{__shared_weak_count}}"
+ "|"
- "\tGlobal: mVibrationDisabled: %d mPhoneCallActive: %d mMicIsActive: %d mContinuityScreenOn: %d mActiveHighPriorityClientCount: %d, mActiveMediumPriorityClientCount: %d\n"
- "\tNum Events: %d, Track Length: %.2f beats\n"
- "   *** removed, skipping"
- "  Attached to AQMEIO_HAL below:\n"
- "  DSP_Routing_Borealis @ %p:\n"
- "  EnhanceDialog: "
- "  MESubmixGraph: %p\n"
- "  Published upwards:\n"
- " (post-trigger)"
- "%25s:%-5d "
- "%25s:%-5d      MESubmixGraph(%p)::isUsingAirPlayMusicPort() = %s"
- "%25s:%-5d      checkForceLPCMForEnhanceDialogue: Error %d (%s) getting force LPCM state for device ID %d"
- "%25s:%-5d      checkForceLPCMForEnhanceDialogue: Error %d (%s) setting force LPCM for Enhance Dialogue for device ID %d"
- "%25s:%-5d      checkForceLPCMForEnhanceDialogue: Keeping force LPCM = %s for device ID %x"
- "%25s:%-5d      checkForceLPCMForEnhanceDialogue: Setting force LPCM = %s for device ID %x"
- "%25s:%-5d      checkForceLPCMForEnhanceDialogue: outputPorts[0] = %s"
- "%25s:%-5d      getEnhanceDialogueMovieModeSessionType: AQIONodeClient %p sessionID 0x%x has Movie Mode audio session %s"
- "%25s:%-5d      getEnhanceDialogueMovieModeSessionType: AQIONodeClient %p sessionID 0x%x is not running (%d clients total)"
- "%25s:%-5d      getEnhanceDialogueMovieModeSessionType: AQIONodeClient %p sessionID 0x%x with audio session mode %s prevents Enhance Dialogue"
- "%25s:%-5d  %s: %s"
- "%25s:%-5d  *** running trigger on AOP"
- "%25s:%-5d  *** running trigger on AOP - PSReset"
- "%25s:%-5d  *** running trigger on AP"
- "%25s:%-5d  *** running trigger on AP - PSReset"
- "%25s:%-5d  ASSERTION FAILED: %s, line %d: %s"
- "%25s:%-5d  ASSERTION FAILED: default AU still set to one that will be destroyed"
- "%25s:%-5d  ASSERTION FAILED: sequence was not previously unregistered"
- "%25s:%-5d  Called without a sequence"
- "%25s:%-5d  CopyDataTo: packet desc mismatch: %d produced, %d in receiver's buff"
- "%25s:%-5d  IORegisterForSystemPower() failed to return a notification port"
- "%25s:%-5d  IORegisterForSystemPower() failed to return the connection"
- "%25s:%-5d  IORegisterForSystemPower() failed to return the notifier"
- "%25s:%-5d  New graph creation should not fail"
- "%25s:%-5d  No event tracks in sequence! This is not a valid sequence"
- "%25s:%-5d  Old track to be replaced not found in sequence"
- "%25s:%-5d  STACK_ABL: invalid number of buffers"
- "%25s:%-5d  Sequence shouldn't be gone!"
- "%25s:%-5d  SetTimeConstraints: thread_policy_set failed, Error: %d (%s)"
- "%25s:%-5d  Synchonized looping sequence should have a synchronizer here!"
- "%25s:%-5d  Temp track should exist during edit!"
- "%25s:%-5d  Temp track should not already exist!"
- "%25s:%-5d  Zero-velocity note on should not be here"
- "%25s:%-5d !!! getEnhanceDialogueMovieModeSessionType() - Atmos metadata decode detected !!!"
- "%25s:%-5d !!! getEnhanceDialogueMovieModeSessionType() - suppressing EDP off to bypass !!!"
- "%25s:%-5d ### Creating legacy VoiceTrigger Manager ### "
- "%25s:%-5d %p 0x%x: ServerDied"
- "%25s:%-5d %p created; Borealis VAD: %d"
- "%25s:%-5d %p destroyed"
- "%25s:%-5d %p stopping after freewheeling"
- "%25s:%-5d %p: done"
- "%25s:%-5d %p: enabled %d"
- "%25s:%-5d %s for VoiceTrigger Occurred notification on device %@"
- "%25s:%-5d %s voice trigger : error (%d) on device %@"
- "%25s:%-5d %s: \t\tinBeats < lastEventTime -- curloop set to 0"
- "%25s:%-5d %s: \t\tinBeats < loopEnd -- curloop set to 0"
- "%25s:%-5d %s: \t\tinBeats >= lastEventTime -- curloop set to %d"
- "%25s:%-5d %s: \t\tinBeats >= loopEnd -- curloop set to %d"
- "%25s:%-5d %s: \tloopLength %f, lastEventTime is %f"
- "%25s:%-5d %s: \tloopLength %f, loopEnd is %f"
- "%25s:%-5d %s: \"MusicTrackSetProperty\" returned %d"
- "%25s:%-5d %s: %s format changed"
- "%25s:%-5d %s: %s route changed - handling async"
- "%25s:%-5d %s: %s volume changed"
- "%25s:%-5d %s: ---> this=%p"
- "%25s:%-5d %s: <--- inBeats: %.2f, loop count: %d\n"
- "%25s:%-5d %s: Active high priority client count -> 0; active medium priority client: %u; so ummuting all %@clients"
- "%25s:%-5d %s: Active high priority client count -> 1 so muting other low/medium priority clients"
- "%25s:%-5d %s: Active medium priority client count -> 0; no high priority clients; so ummuting all low priority clients"
- "%25s:%-5d %s: Active medium priority client count -> 1 so muting other low priority clients"
- "%25s:%-5d %s: Adding raw audio sample %p, size %u bytes. Raw audio has %u channels, %u frames, %u Bytes per frame"
- "%25s:%-5d %s: AudioQueueSetProperty: %s not supported for %s"
- "%25s:%-5d %s: AudioQueueSetProperty: null cryptor for %s (%s)"
- "%25s:%-5d %s: Current adjusted beat %.3f past or at loop region end (%.3f): Seeking to beat %.3f"
- "%25s:%-5d %s: DispatchEvent failed with %d"
- "%25s:%-5d %s: Error attempting to set out of bounds channel %u in use: %d, mChannelStatus.size() = %u"
- "%25s:%-5d %s: High priority clients always play haptics in Continuity Screen mode"
- "%25s:%-5d %s: Including parameter automation event from curve: ID %d value %f time:%.3f"
- "%25s:%-5d %s: Including parameter event: ID %d value %f time:%.3f"
- "%25s:%-5d %s: LoudnessManager::GetSettings() returned %d (%s): %sapplying loudness defaults"
- "%25s:%-5d %s: Point time: %.3f  Delta value: %.3f"
- "%25s:%-5d %s: ScheduledSlicePlayer::ClearSchedule: %d frame imbalance"
- "%25s:%-5d %s: Storing bank selects msb 0x%x lsb 0x%x plus program change %d into chaseEventList"
- "%25s:%-5d %s: TEMP FIX: Required time incr=%.3f - pushing event forward to time %.3f"
- "%25s:%-5d %s: TimePitchProperty accessed; error %d"
- "%25s:%-5d %s: aq@%p: %s using invalid anchor time"
- "%25s:%-5d %s: aq@%p: ***** end of stream at t=%lld *****"
- "%25s:%-5d %s: aq@%p: New %s; format %s"
- "%25s:%-5d %s: aq@%p: ptr %p, size 0x%x%s => ID %d"
- "%25s:%-5d %s: aq@%p: ptr %p, size 0x%x, ID %d"
- "%25s:%-5d %s: com.apple.coreaudio/apply-custom-loudness-settings|drc-capable is on, applying DRC from preferences"
- "%25s:%-5d %s: could not get gain from codec, error %d (%s)"
- "%25s:%-5d %s: inBeats: %.2f.  Current adjusted beat %.f past or at loop region end (%.2f): Seek to beat %.2f"
- "%25s:%-5d %s: mActiveHighPriorityClientCount: %u, mActiveMediumPriorityClientCount: %u, mActiveExclusivePriorityClientCount: %u"
- "%25s:%-5d %s: scaled %.f = unscaled %lld"
- "%25s:%-5d %s: this=%p ---> inBeats = %f"
- "%25s:%-5d %s: this=%p EOT (inEndBeat = %.3f)"
- "%25s:%-5d %s: this=%p Edit seed changed -- seek to beat %.2f"
- "%25s:%-5d %s: this=%p Legacy loop endpoint: Seeking back to beat %.3f"
- "%25s:%-5d %s: this=%p Next event time (%.3f) past loop region end (%.3f): Seeking to beat %.3f"
- "%25s:%-5d %s: this=%p adjusted beat %.3f is less than loop region end (%.3f)"
- "%25s:%-5d %s: this=%p curLoop %d, mCurrentLoopOffset now %.2f"
- "%25s:%-5d %s: unscaled %lld = scaled %.f"
- "%25s:%-5d ->"
- "%25s:%-5d ->%p %d"
- "%25s:%-5d ->%p %d %d %08x"
- "%25s:%-5d ->%p %lld"
- "%25s:%-5d ->%p %p"
- "%25s:%-5d ->%s serverQueue=0x%x, clientQueue=%p"
- "%25s:%-5d ->0x%x"
- "%25s:%-5d ->0x%x %d %d"
- "%25s:%-5d ->0x%x %d %d %08x"
- "%25s:%-5d ->0x%x %d fr"
- "%25s:%-5d ->0x%x %s"
- "%25s:%-5d ->0x%x %s (now: 0x%llx)"
- "%25s:%-5d ->0x%x %s, %s"
- "%25s:%-5d ->0x%x %u bytes, %u packets"
- "%25s:%-5d ->0x%x buffer %d; %d bytes, %d packets; trim %d/%d; new enqueue count=%d; %s"
- "%25s:%-5d ->0x%x buffer %d; %d bytes, %d packets; trim %d/%d; new enqueue count=%d; %s; %s"
- "%25s:%-5d ->0x%x flags=0x%x, t=%lld"
- "%25s:%-5d ->0x%x time: %s (now: %.6f)"
- "%25s:%-5d ->0x%x: buffer %d"
- "%25s:%-5d ->0x%x: buffer %d, ptr %p, size %d, %d packets"
- "%25s:%-5d ->AudioQueueNew%s %s 0x%x"
- "%25s:%-5d ...run loop handled a source"
- "%25s:%-5d 0x%x: %d %p/%p%s"
- "%25s:%-5d 0x%x: complete buffer %d %p"
- "%25s:%-5d 0x%x: destroyed, not waiting for %d buffer callbacks"
- "%25s:%-5d 0x%x: destroyed, skipping %d buffer callbacks"
- "%25s:%-5d 0x%x: destroyed, skipping %d buffer callbacks, buffer@%p"
- "%25s:%-5d 0x%x: has %d pending offline buffers, not waiting"
- "%25s:%-5d 0x%x: waiting for %d buffer callbacks"
- "%25s:%-5d 0x%x: waiting for buffer callbacks timed out!"
- "%25s:%-5d <- pauseSampleTime %lld"
- "%25s:%-5d <-%d"
- "%25s:%-5d <-%d fr, err %d"
- "%25s:%-5d <-%p %d fr, %d"
- "%25s:%-5d <-%p (%d)"
- "%25s:%-5d <-%s"
- "%25s:%-5d <-%s; err=%d"
- "%25s:%-5d <-(%.6f s)"
- "%25s:%-5d <-(%d)"
- "%25s:%-5d <-(err %d) %d bytes"
- "%25s:%-5d <-(err=%d, %.6f s)"
- "%25s:%-5d <->0x%x buffer %d"
- "%25s:%-5d <-AudioQueueNew failed %d"
- "%25s:%-5d <-AudioQueueNew%s serverQueue=0x%x, clientQueue=%p"
- "%25s:%-5d <-buffer %d; enqueue count=%d"
- "%25s:%-5d <-err=%d, buffer=%d"
- "%25s:%-5d <-failed (%d); enqueue count=%d"
- "%25s:%-5d <On SSS worker queue> calling haptic completion callback"
- "%25s:%-5d === AQMixEngine_VAD(%p)::enhanceDialogueModeChanged: setting route supported = %d ==="
- "%25s:%-5d AQIONodeClient %p: %d"
- "%25s:%-5d AQMEIO: %s stream %d: %u b, %u b/fr => %u fr"
- "%25s:%-5d AQMEIO_DSP(%p)::Begin AdaptToVARoute(%p%s%s)"
- "%25s:%-5d AQMEIO_DSP::End AdaptToVARoute(%s%s)"
- "%25s:%-5d AQMixEngine_VAD(%p)::routeSupportsEnhanceDialogue() = %s"
- "%25s:%-5d AQServer creating a new remote client %p %s"
- "%25s:%-5d AQServer: Reusing existing remote client %p %s"
- "%25s:%-5d AQServer: deleting remote client %p %s"
- "%25s:%-5d AQServer::QueueDisposed deleting unused rcp %p"
- "%25s:%-5d ASSERTION FAILURE (error %d): "
- "%25s:%-5d ASSERTION FAILURE [(!\"Attempted to add same channel ID twice\") != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(!\"Attempted to add same instance ID twice\") != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(!\"Bad property size\") != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(!\"SHOULD NOT BE RECEIVING REC-STATE-DID-CHANGE NOTIFICATIONS\") != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(!\"Unexpected Property ID\") != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(!\"Unknown property\") != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(!BypassAudioSession() || IsTap()) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(!BypassAudioSession()) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(!audio || _audioPrewarmCount > 0) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(!audio || _audioRunningCount > 0) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(!haptics || _hapticsPrewarmCount > 0) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(!haptics || _hapticsRunningCount > 0) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(!isRunning()) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(!mInitialized) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(!mIsServer) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(!mIsTapSubmix && channel->GetSubmixGraph() == nullptr) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(!mIsTapSubmix && channel->GetSubmixGraph() == this) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(!mIsTapSubmix) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(!running()) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(!stopping()) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(!submixToConnect.mIsTapSubmix && !mainSubmix.mIsTapSubmix) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [((((1 && !0) && !0 && !0) && !CASIsDarwinOS())) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [((client.GetTopologyFlags() & kAudioQueueFlag_HardwarePassthrough) != 0) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(0 != (client.GetTopologyFlags() & kAudioQueueFlag_IsPhaseAQIONodeClient)) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(AudioTapUtilities::CanTapPhase(tapSpecifier())) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(IONodeClientCount() < 2) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(IsInput()) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(_IDBeingStarted == kNoSequenceID || _IDBeingStarted == inID) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(_IDBeingStarted == kNoSequenceID) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(__null != gUserList) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(__null != mCPMSSharedInstanceForHaptics) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(__objc_no != success) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(_channelIDsToBeDetached.size() == 0) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(_initCount > 0) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(_startCount == 0) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(_startCount > 0 && _startCount < 3) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(_state != Uninitialized || inState == Stopped) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(_state == Uninitialized) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(_stoppedDuringFlush == false) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(abl->mNumberBuffers == outputBuffers->mNumberBuffers) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(activeSoundInfo != nullptr) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(clientAudioOutput != nullptr) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(clientID != 9999999) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(clientsWithProcess != _processIndexMap.end()) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(cm == __null) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(currentBufferOffset <= int(inNumberFrames)) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(destABL.mBuffers[0].mDataByteSize >= inNumberFrames * mOutputFormat.mBytesPerFrame) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(e->mNumberParameters == 1) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(e->mParams[i].mID != kAudioQueueParam_PlayRate2) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(entry->stopped()) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(err == noErr) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(false) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(foundUserEvent == true) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(frameOffset < (SInt32)numFrames) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(id < (1UL << 31)) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(inAudioToken) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(inChannels.size() <= mChannelStatus.size()) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(inID != kAudioQueueParam_PlayRate2) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(inState != Starting || _state == Stopped) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(ioBufferList.mNumberBuffers == mRampBufferList->GetNumberBuffers()) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(ioByteSize <= mInputNumBytes) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(ioPackets <= mInputNumPackets) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(ioSize == sizeof(double)) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(it != mInputStates.end()) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(it != mMixerChannels.end()) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(it != mSubmixGraph->mMixerChannels.end()) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(keyrange.mHigh == keyrange.mLow) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(mActiveHighPowerHapticsClients >= 0) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(mActivePriorityClientCountMap[HapticPlayerPriority::ExclusivePriority] != 0) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(mActivePriorityClientCountMap[HapticPlayerPriority::HighPriority] != 0) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(mActivePriorityClientCountMap[HapticPlayerPriority::MediumPriority] != 0) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(mAudioOutput != nullptr) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(mBufferCapacity == 0 || nBytes <= mBufferCapacity) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(mBufferMemory == __null) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(mClientInfo != __null) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(mClientRunMode != kRunMode_NotRunning) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(mDestinationGraph == nullptr && !mIsTapSubmix) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(mDestinationTaps.empty()) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(mHapticOutput != nullptr) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(mIsServer) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(mNumAllocatedSlices == 0) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(mSSSClientEntryRunningCount != 0) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(mSynthRingBuffer != nullptr) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(mTapSources.empty()) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(mixerBus.has_value()) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(nullptr == propertyValue) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(outPreferences) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(pos <= int(inNumberFrames)) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(proc != nullptr) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(reachedOffset0) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(srcFormat.mSampleRate == destFormat.mSampleRate || mTimestampGenerator != __null) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(startingInterrupt) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(success == false) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(tapConnection.has_value()) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(track != 0) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(track != nullptr) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(ts2.mFlags & kAudioTimeStampHostTimeValid) != 0 is false]: "
- "%25s:%-5d Allocating borealis ring buffer"
- "%25s:%-5d Borealis runningClientCount: %d"
- "%25s:%-5d Client has called AudioQueueDispose while a property listener is in flight. Sleeping briefly."
- "%25s:%-5d ClientAudioQueue %p 0x%x: destructing"
- "%25s:%-5d Could not start %s for actionID %d, error %d"
- "%25s:%-5d Couldn't connect to %s; AudioQueue will not be usable"
- "%25s:%-5d DEBUG_FRAMESIZE: expected %d, got %d frames"
- "%25s:%-5d Deallocating borealis ring buffer"
- "%25s:%-5d EXCEPTION (%d) [error != noErr is false]: \"\""
- "%25s:%-5d EnableMixTapToTelephonyUplink(%p); Ignoring invalid audioSessionToTap = 0x%x"
- "%25s:%-5d EnableMixTapToTelephonyUplink(%p); cannot be enabled while screen sharing!"
- "%25s:%-5d Failed IOBufferFrameSizeListener callback with error = %d"
- "%25s:%-5d Failed IOBufferFrameSizeListener callback with unknown error"
- "%25s:%-5d Failed to get %s from graph, err = %s"
- "%25s:%-5d Failed to get channel layout for DSPGraph, err = %d"
- "%25s:%-5d Failed to get channel layout for mExternalACL, err = %d"
- "%25s:%-5d Failed to retrieve tap info err: %d"
- "%25s:%-5d Failed to set kVPProperty_OffloadAirPodsNoiseSuppression with error: %d"
- "%25s:%-5d Failed to set tap object <-(%d)"
- "%25s:%-5d Failed to set up power manager"
- "%25s:%-5d Finished draining ring buffer; elapsed %lld fr / %.3fs; max utilization %u fr / %.3fs"
- "%25s:%-5d FireSpeechDetectedNotificationIfChanged; speechActivityEvent=%i"
- "%25s:%-5d First pass model update returned error : %d on device %@"
- "%25s:%-5d GetSettings(): looking for late night: %s"
- "%25s:%-5d GetSettings(): looking for media type and encoder OS: %s %s %d.%d"
- "%25s:%-5d GetSettings(): no Format key in plist file"
- "%25s:%-5d Hey Siri enabled: %d (%s)"
- "%25s:%-5d IOProc expected %d, got %d frames"
- "%25s:%-5d Initialize: processor invalid, return"
- "%25s:%-5d Invalid SSClientPlayOptions data for SystemSoundServerAction::PlayWithFlags"
- "%25s:%-5d MESubmixGraph@%p: maintainTaps (tapAdded = %d)"
- "%25s:%-5d MixLayoutChanged: externalACL: %s, graphACL: %s"
- "%25s:%-5d MixTapToUplink@%p::CreateAQMETapConnector; AddRunningClient returned error = %i"
- "%25s:%-5d MixTapToUplink@%p::CreateAQMETapConnector; created tap of session(s) %s with format: %s."
- "%25s:%-5d MixTapToUplink@%p::CreateAQMETapConnector; creating tap of session(s) %s with format: %s"
- "%25s:%-5d MixTapToUplink@%p::CreateTap; CAException caught in log: %d"
- "%25s:%-5d MixTapToUplink@%p::CreateTap; Unknown exception caught in log"
- "%25s:%-5d MixTapToUplink@%p::CreateTap; do any audio sessions bypass input mute? %i"
- "%25s:%-5d MixTapToUplink@%p::CreateTap; invalid audio format provided. format=%s"
- "%25s:%-5d MixTapToUplink@%p::CreateTap; no audio session ids provided."
- "%25s:%-5d MixTapToUplink@%p::CreateTap; std::exception caught in log: %s"
- "%25s:%-5d MixTapToUplink@%p::FetchAndMix timeStamp = %lld returned error %i. Buffer has samples from %lld to %lld. mSampleToStartRead = %lld. , nFrames = %i. outNumValidFrames=%i, outNumLeadingZeroes=%i outNumTrailingZeroes=%i"
- "%25s:%-5d MixTapToUplink@%p::StopAudioTap;  released tap of session %s"
- "%25s:%-5d MixTapToUplink@%p::Store; discontinuity occurred in tap timeline. Setting mSampleTimeForStartOfTimeline = %lld"
- "%25s:%-5d MixTapToUplinkHost@%p IsMixTapToTelephonyUplinkDisabledByScreenSharing; mScreenSharingEnabledProvider is not set."
- "%25s:%-5d NSData Model data : %s"
- "%25s:%-5d No built-in haptic pattern found for action ID %u"
- "%25s:%-5d Over %.1f seconds of audio (%.3f, %lld:%lld) in ring buffer awaiting PhraseSpotter"
- "%25s:%-5d PhraseSpotter (%p) ready"
- "%25s:%-5d PhraseSpotter triggered! %@; %.3fs ago"
- "%25s:%-5d Power manager initialized"
- "%25s:%-5d Product does not have valid tuning"
- "%25s:%-5d Product does not support Enhance Dialogue"
- "%25s:%-5d PushMicInput allocated %d fr, trying to render %d"
- "%25s:%-5d PushTapInput allocated %d fr, trying to render %d"
- "%25s:%-5d Recording implicitly allowed for AQIONodeClient %p hosted in mediaserverd with no client audit token."
- "%25s:%-5d Requested offload AirPods noise suppression state is updated to = %s"
- "%25s:%-5d Set %s"
- "%25s:%-5d SetBypass: processor invalid, return"
- "%25s:%-5d SetChannelMap with mChannelMap, size = %lu"
- "%25s:%-5d SetChannelMap: mChannelMap.size() = 0, return"
- "%25s:%-5d SetChannelMap: processor invalid, return"
- "%25s:%-5d SetMixTapToTelephonyUplinkAllowedByUser(%p); cannot be enabled while screen sharing!"
- "%25s:%-5d SetMixToTelephonyUplink(%p) cannot be enabled while screen sharing!"
- "%25s:%-5d SetMixToTelephonyUplink; list of audio sessions to tap is empty. Not creating tap."
- "%25s:%-5d SetProperty %d : media chat [%s]"
- "%25s:%-5d Setting %s"
- "%25s:%-5d Setting bypass: %d"
- "%25s:%-5d Siri Notification received %d"
- "%25s:%-5d Siri enabled %d (%s)"
- "%25s:%-5d Starting %s now, actionID %d"
- "%25s:%-5d Starting/continuing Hey Siri%s"
- "%25s:%-5d Stopped Hey Siri"
- "%25s:%-5d Stopping vibe for ssid %d"
- "%25s:%-5d Stopping vibe for ssid %d for pid %d"
- "%25s:%-5d This platform does not support AHAP playback for SSS"
- "%25s:%-5d TranslateTime failed(%d) or invalid sample time : now(%lld) - hosttime(%lld) = %.6f secs"
- "%25s:%-5d TranslateTime returned %s (err=%d), now=%.6f, ring buffer range %lld:%lld"
- "%25s:%-5d Uninitialize: processor invalid, return"
- "%25s:%-5d Updating AOP with new model"
- "%25s:%-5d VoiceTrigger Model is not configured: %d"
- "%25s:%-5d VoiceTrigger Occurred : setting start time %lld / %s (%lld) ; current time %0.6f"
- "%25s:%-5d VoiceTrigger model configuration callback - context flags Locked, defering the notification handling"
- "%25s:%-5d VoiceTrigger model configuration callback received"
- "%25s:%-5d VoiceTrigger model configuration update complete"
- "%25s:%-5d VoiceTrigger was not disabled by update model. So NOT enabling it back"
- "%25s:%-5d Will await PhraseSpotter ready callback - isSecondPass : %d"
- "%25s:%-5d allocated %d fr, trying to render %d"
- "%25s:%-5d already in a callback on the client run loop"
- "%25s:%-5d aq@%p: MovieModeMuteStateChanged, setting kMESubmixProperty_EnhanceDialogueRouteChanged"
- "%25s:%-5d bounds %lld-%lld, readTime %lld"
- "%25s:%-5d checking ShouldRun() : %d"
- "%25s:%-5d client=%p port=0x%x pid=%d"
- "%25s:%-5d client=%p queueOwner=%p, newState=%d"
- "%25s:%-5d co-listen is disabled"
- "%25s:%-5d co-listen is enabled"
- "%25s:%-5d codec.GetProperty('cori') returns %d (%s), defaulting origin information"
- "%25s:%-5d codec.GetProperty('cori') returns unknown OS type: %d, defaulting"
- "%25s:%-5d codec.GetProperty('cori') returns unknown source: %d, defaulting"
- "%25s:%-5d converted %d fr (err %d)"
- "%25s:%-5d deleting isolated rcp %p"
- "%25s:%-5d device %s is persisting across a route change"
- "%25s:%-5d disabling VoiceTrigger before updating model"
- "%25s:%-5d dropped %d frames (%.3fs)"
- "%25s:%-5d enabling VoiceTrigger after updating the model"
- "%25s:%-5d error %d from VP"
- "%25s:%-5d error %d setting cinematic audio unit austrip."
- "%25s:%-5d error %d setting cinematic audio unit dsp graph text path."
- "%25s:%-5d error %d setting cinematic audio unit property strip resource path."
- "%25s:%-5d error %d setting cinematic audio unit property strip."
- "%25s:%-5d error messaging the server; reconnecting."
- "%25s:%-5d feeding %lld"
- "%25s:%-5d fetched trigger dictionary"
- "%25s:%-5d first pass model nil"
- "%25s:%-5d getEnhanceDialogueMovieModeSessionType(notifyOnClientFormatMismatch = %s) = %s [lastMovieModeClient = %p, %d clients]"
- "%25s:%-5d hasPermissionToMixTapToUplink; audioSessionToTap=0x%x does not have permission to bypass the mic mute. Has entitlement? %i Feature is enabled? %i"
- "%25s:%-5d ionc@%p SchedTimePitchAddRateChange %.3f @ %lld"
- "%25s:%-5d ionc@%p SchedTimePitchTrackedRateChange %.3f %lld %lld"
- "%25s:%-5d ionc@%p TimePitchRate(%s) %.3f"
- "%25s:%-5d ionc@%p TimePitchRate(immediate) %.3f"
- "%25s:%-5d ionc@%p TimePitchReset"
- "%25s:%-5d ionc@%p offline %s, SC %s%s, flags 0x%x, err %d, scalar %.3f"
- "%25s:%-5d ionc@%p: currentVolume %5.3f, mVolume[%d] %5.3f, outAnyRamping %d"
- "%25s:%-5d kAOPAudioDriverVoiceTriggerAvailable: %d (err=%d)"
- "%25s:%-5d mAVVCReadTime : %lld --- mPhraseSpotterReadTime : %lld"
- "%25s:%-5d mAVVCReadTime == kInvalidSampleTime. reason: %s"
- "%25s:%-5d mMicInputCache already has value (indicates unexpected order of operations)"
- "%25s:%-5d mTapStreamProcessed already true (indicates unexpected order of operations)"
- "%25s:%-5d mediaserverd starting"
- "%25s:%-5d mixer=%p, fmt=%s"
- "%25s:%-5d past data available frames from ring buffer %lld:%lld = %d"
- "%25s:%-5d pref changed, so calling BorealisToggled()"
- "%25s:%-5d rio@%p: MovieModeMuteStateChanged, setting kMESubmixProperty_EnhanceDialogueRouteChanged"
- "%25s:%-5d rio@%p: input mute %d applied to VP, not locally."
- "%25s:%-5d sample rates hw %.f Hz, analysis %.f Hz, I/O frame size %u"
- "%25s:%-5d secondPassStop triggered : %@;"
- "%25s:%-5d set kMEBorealisProperty_ClientRunning %d"
- "%25s:%-5d setEnhanceDialogueEnabled: %d (no change)"
- "%25s:%-5d setEnhanceDialogueEnabled: %d -> %d"
- "%25s:%-5d setEnhanceDialogueEnabled: opening Enhance Dialogue Processor"
- "%25s:%-5d shouldRunNow: %d"
- "%25s:%-5d siri enabled %d, borealis enabled %d, should run now %d"
- "%25s:%-5d starting%s"
- "%25s:%-5d t=%.f, n=%d"
- "%25s:%-5d t=%.f, n=%d, st=%.f, sn=%d"
- "%25s:%-5d updateEnhanceDialogueRoute: route supported = %s for default VAD active port %s"
- "%25s:%-5d we are on the client run loop, running it"
- "%s: %s: Abandoning I/O cycle because we were requested to render more frames: %dthan the maximum frame count: %d."
- "%sAUDSPGraph_CinematicAudio: "
- ", following route change"
- ", user"
- "-[AVHapticServerInstance prepareHapticSequence:reply:]_block_invoke"
- "-[AVHapticServerInstance prepareHapticSequence:reply:]_block_invoke_2"
- "/AppleInternal/Library/Audio/Tunings/Generic/Haptics/SystemSounds/Library/systemsoundhapticpatterns.plist"
- "/Library/Audio/Tunings/Generic/CinematicSeparation/Tunings"
- "/Library/Audio/Tunings/Generic/CinematicSeparation/shared"
- "/Library/Caches/com.apple.xbs/Sources/CoreAudioServices/Source/CAServices/DLS/DlsFileBase.cpp"
- "/Library/Caches/com.apple.xbs/Sources/CoreAudioServices/Source/CAServices/Sequencer/AudioUnitGraph.cpp"
- "/Library/Caches/com.apple.xbs/Sources/CoreAudioServices/Source/CAServices/Sequencer/TempoMap.cpp"
- "; "
- "<%@@%p: process tap - pids:%@, name:%@, UUID:%@, format:%@, excluded pids:%@>"
- "<AudioQueueObject@%p; %s%s; %s>"
- "<ClientAQOfflineMixer@%p>\n"
- "<DSP_Routing_Borealis@%p>"
- "@56@0:8f16B20^v24^?32^?40^?48"
- "AOPRunning"
- "AOPVoiceTriggerData"
- "AQ.mPropertyListenerMutex"
- "AQ::WorkQueue::mLock"
- "AQClient.cpp"
- "AQConverterManager.mConverterThreadStartStopLock"
- "AQInternalGetOfflineBufferCompletions"
- "AQInternalPreflightOfflineRender"
- "AQInternalScheduledStart"
- "AQMEIO.mStateGuard"
- "AQOfflineMixerConnectAudioQueue"
- "AQOfflineMixerDispose"
- "AQOfflineMixerGetProperty"
- "AQOfflineMixerGetPropertySize"
- "AQOfflineMixerNew"
- "AQProcessingTap.cpp"
- "AQProcessingTap::PortDeathListener"
- "AQServer.mServerLock"
- "AQServer_AddPropertyListener"
- "AQServer_CheckStopFromPause"
- "AQServer_CreateTimeline"
- "AQServer_DeviceGetCurrentTime"
- "AQServer_DeviceGetNearestStartTime"
- "AQServer_DeviceTranslateTime"
- "AQServer_DisposeQueue"
- "AQServer_DisposeQueue_block_invoke"
- "AQServer_DisposeTimeline"
- "AQServer_EnqueueBuffer"
- "AQServer_EnqueueSilence"
- "AQServer_Flush"
- "AQServer_FreeBuffer"
- "AQServer_GetParameter"
- "AQServer_GetPendingCallbackMessages"
- "AQServer_GetProperty"
- "AQServer_GetPropertySize"
- "AQServer_MixerConnectQueue"
- "AQServer_MixerConnectQueue_block_invoke"
- "AQServer_MixerDispose"
- "AQServer_MixerGetProperty"
- "AQServer_MixerGetPropertySize"
- "AQServer_MixerNew"
- "AQServer_MixerReset"
- "AQServer_MixerSetProperty"
- "AQServer_NewQueue"
- "AQServer_OfflineRender"
- "AQServer_Pause"
- "AQServer_Pause_block_invoke"
- "AQServer_Prime"
- "AQServer_Prime_block_invoke"
- "AQServer_ProcessingTapDispose"
- "AQServer_ProcessingTapInit"
- "AQServer_ProcessingTapNew"
- "AQServer_ProcessingTapPerformReply"
- "AQServer_ProcessingTapRetrieveInfo"
- "AQServer_QueueGetCurrentTime"
- "AQServer_RemovePropertyListener"
- "AQServer_Reset"
- "AQServer_ScaleOrUnscaleSampleTime"
- "AQServer_ScheduleParameters"
- "AQServer_SetOfflineRenderFormat"
- "AQServer_SetOfflineRenderFormat_block_invoke"
- "AQServer_SetParameter"
- "AQServer_SetProperty"
- "AQServer_Start"
- "AQServer_Start_block_invoke"
- "AQServer_Stop"
- "AQServer_Stop_block_invoke"
- "AVBorealisServer"
- "AVBorealisServer.mm"
- "AVBorealisServerHysteresisNotifier"
- "AVBorealisServerPortManager"
- "ActiveSoundListLock"
- "AddEventToChaseState"
- "AddPropertyListener"
- "Advance"
- "AllocateBuffer"
- "AssignToSubmixTap_block_invoke"
- "AudioBuffers.PrepareNull failed"
- "AudioQueueAddPropertyListener"
- "AudioQueueCheckSpatializationAfterRouteChange"
- "AudioQueueClient"
- "AudioQueueConvertToScaledSampleTime"
- "AudioQueueConvertToUnscaledSampleTime"
- "AudioQueueCreateTimeline"
- "AudioQueueDeassignFromSubmixTap_block_invoke"
- "AudioQueueDefaultDeviceChanged"
- "AudioQueueDeviceGetCurrentTime"
- "AudioQueueDeviceGetNearestStartTime"
- "AudioQueueDeviceTranslateTime"
- "AudioQueueDisposeTimeline"
- "AudioQueueFreeBuffer"
- "AudioQueueGetParameter"
- "AudioQueueGetProperty"
- "AudioQueueGetPropertySize"
- "AudioQueueInternalDeliverProcessingNodeEvents"
- "AudioQueueInternalNotifyRunning"
- "AudioQueueInternalPause"
- "AudioQueueInternalReleasePlayResources"
- "AudioQueueInternalStop_Sync_block_invoke"
- "AudioQueueNotifyReadyToRestart"
- "AudioQueueObject::mConverterResetMutex"
- "AudioQueueObject::mIOResetMutex"
- "AudioQueueObject::mTrimQueueMutex"
- "AudioQueueProcessingTapGetSourceAudio"
- "AudioQueueProcessingTapNew_CMClient"
- "AudioQueueProcessingTapNew_CMServer"
- "AudioQueueRemovePropertyListener"
- "AudioQueueSetOfflineRenderFormat"
- "AudioQueueSetProperty"
- "AudioQueueSiriListeningPropertyChanged_block_invoke"
- "AudioQueueXPC"
- "AudioSession.PropertyListenersStateMutex"
- "AudioSessionCreateCMSession"
- "AudioSessionCreateCoreMXSession"
- "AudioSessionGetPrimaryAudioSessionIDForAuditToken"
- "AudioToolbox_AudioQueueVersion"
- "BlueTooth"
- "BorealisCapacity"
- "BorealisCapture"
- "BorealisIOBufferFrameSize"
- "BorealisManager"
- "BorealisManager.mm"
- "BorealisManager.notification"
- "BorealisPriority"
- "CA Orientation Manager"
- "CancelPlayer"
- "CheckLoop"
- "CheckReadyToPlay"
- "ConvertToScaled"
- "ConvertToUnscaled"
- "CorealisRTModel"
- "CreateTimeline"
- "DSP_Routing_Borealis"
- "DSP_Routing_Borealis.mm"
- "DSP_Routing_VP_block_invoke"
- "DebugPrint"
- "DeviceGetCurrentTime"
- "DeviceGetNearestStartTime"
- "DeviceIsRunning"
- "DeviceTranslateTime"
- "DispatchChaseState"
- "DispatchMIDIChannelMessage"
- "DispatchMIDINoteMessage"
- "DisposeQueue_block_invoke"
- "DisposeTimeline"
- "EnableMixTapToTelephonyUplink"
- "Flush"
- "GetAnchorIOSampleTimeWarnIfInvalid"
- "GetCurrentTime"
- "GetMaxIOBufferFrameSize"
- "GetNearestStartTime"
- "GetNumberBuffers"
- "GetParameter"
- "GetPendingCallbackMessages"
- "GetProperty"
- "GetPropertySize"
- "GetSampleRate"
- "GetStreamFormat"
- "GetTotalNumberChannels"
- "HandleAQGetParameter"
- "HandleAQGetProperty"
- "HandleAQScheduledParameters"
- "HandleAQSetParameter"
- "HandleAQSetProperty"
- "Haptic Synth Lock"
- "Haptic Synth Start Lock"
- "HapticSynth AU Mutex"
- "HapticSynth IO Mutex"
- "HapticSynth render lock"
- "Impl_AllocateBuffer"
- "Impl_MixerRender"
- "Impl_ProcessingTapGetSourceAudio"
- "LatencySamples"
- "MCProcessingNodeInputInsert"
- "MIGAllocateBuffer"
- "MIGFreeBuffer"
- "MapSharedBuffers"
- "MixServer"
- "MixTapToUplink.Waiter"
- "MixerConnectQueue_block_invoke"
- "MixerDispose"
- "MixerGetProperty"
- "MixerGetPropertySize"
- "MixerNew"
- "MixerRender"
- "MixerReset"
- "MixerSetProperty"
- "NewQueue"
- "OffloadACQ"
- "Option_CallerIdentifier"
- "PSAnalyzing"
- "PSAwaitRecord"
- "PSPreRecording"
- "PSRecording"
- "PSReset"
- "Pause_block_invoke"
- "PhraseSpotterRunning"
- "PlayerReachedLoopPoint"
- "PrefersToDisallowExternalPlayback"
- "Prime_block_invoke"
- "ProcessingNodeDispose"
- "ProcessingNodeInstantiate"
- "ProcessingTapDispose"
- "ProcessingTapInit"
- "ProcessingTapNew"
- "QueueGetCurrentTime"
- "Quiescent"
- "RecordingWithoutPS"
- "RemovePropertyListener"
- "ReseekIfNeeded"
- "SSClientCompletion"
- "SSSPowerManager"
- "SSSPowerManager.cpp"
- "SSSServer.sCMCallbackSerializationLock"
- "SSSServer.sInitializeSSSLock"
- "ScaleOrUnscaleSampleTime"
- "Schedule"
- "ScheduledSlicePlayer.h"
- "SeekReadPos"
- "SequencePlayer::Playing Guard"
- "SetAudioQueue_block_invoke"
- "SetCurrentLoop"
- "SetOfflineRenderFormat_block_invoke"
- "SetParameter"
- "SetPlayerLatency"
- "SetRoutingBehavior"
- "SetTopologyFlags"
- "SharedAudioBufferList.h"
- "SlicePlayed"
- "StartIO_Primitive"
- "Start_block_invoke"
- "Stop_block_invoke"
- "SuppressAudio"
- "SuppressVibe"
- "TranslateTime"
- "VTPreferences"
- "WorkThreadSynchronizer.h"
- "^{BorealisServerImpl=^^?I^{HALListener}^{HALListener}^{HALListener}i**BBBBB@@i^{unfair_recursive_lock}@BI@}"
- "_InternalDispose_block_invoke"
- "addEntriesFromDictionary:"
- "additive_routing_voice_over"
- "analyzeBufferList:"
- "bluetoothAlternateTransportMode"
- "bluetoothUserHeadTrackingModeForBundleID"
- "bluetoothUserSpatialModeForBundleID"
- "borealis"
- "borealis-postsrc"
- "borealis-presrc"
- "borealis.hardwareVoiceTriggerAvailable()"
- "borealis3"
- "borealis_capture"
- "borealis_capture_ring_buffer_mode"
- "buf == NULL"
- "calibrationData"
- "channelIDsToBeDetached container lock"
- "cinematic-audio-enabled"
- "client sequence lock"
- "client uninitialize lock"
- "com.apple.coreaudio.AQClient"
- "cq == NULL"
- "currentHostTime"
- "customHRTFMode"
- "dictionaryWithCapacity:"
- "direct"
- "dynamicLatency"
- "enableHeadTrackingMode"
- "getAdjustedDeviceStartTime:"
- "getBytes:length:"
- "getHeadTracker"
- "getHeadTrackingSupport"
- "getModel"
- "getPhraseSpotter"
- "hasDefaultOutputSpeakerPort"
- "have AOP"
- "i8@?0"
- "inMixer == NULL"
- "inTimestamp == NULL"
- "initWithRateLimit:detectPredictionAnchor:userContext:factory:execution:finalizer:"
- "ioBuffer == NULL"
- "ioOutputData == NULL"
- "ioOutputData->mBuffers[0].mDataByteSize == 0"
- "isRTSTriggerEvent"
- "isSecondPass"
- "isTriggerEvent"
- "kMovieModeNoSession"
- "kMovieModeSessionMuted"
- "kMovieModeSessionPlaying"
- "mCallbackGuard"
- "mGlobalLock"
- "mState == kStopped"
- "medium priority "
- "no start host time"
- "notifyVoiceTrigger"
- "numFramesFromPreTrigger"
- "numberWithLongLong:"
- "numberWithUnsignedLongLong:"
- "outPacketDependencyInfos != NULL"
- "port 0x%x: %d send, %d rcv, %d sendonce, %d dead name refs"
- "prepareWithProperty:readyCompletion:"
- "rtsNumberSecondsToBackUp"
- "rtsTriggerLength"
- "sampleCount"
- "sampleCountAtEndOfTrigger"
- "sampleCountAtStartOfTrigger"
- "secondPassCompletionHostTime"
- "secondPassStop"
- "separate_and_remix.austrip"
- "separate_and_remix.dspg"
- "separate_and_remix.propstrip"
- "setChannelUsed"
- "setClockDevice"
- "setSpatialStreamInfo"
- "setStartSampleHostTime:"
- "setVolumeScalar"
- "sharedPreferences"
- "triggerEndSeconds"
- "triggerSPENOnAlternateTransportChange"
- "triggerStartSeconds"
- "via VTPreferences"
- "vibe"
- "voiceTriggerEnabled"
- "volumeScalar"
- "volumeScalarMappedToHWCurve"
- "{AQMESession=\"mProcessID\"i\"mSessionID\"I\"mSourceSessionID\"{optional<unsigned int>=\"\"(?=\"__null_state_\"c\"__val_\"I)\"__engaged_\"B}\"mSubsessionRef\"{ObjectRef<const void *>=\"mCFObject\"^v}\"mSubsessionID\"Q\"mDescription\"{basic_string<char, std::char_traits<char>, std::allocator<char>>=\"__r_\"{__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=\"__value_\"(__rep=\"__s\"{__short=\"__data_\"[23c]\"__padding_\"[0C]\"__size_\"b7\"__is_long_\"b1}\"__l\"{__long=\"__data_\"*\"__size_\"Q\"__cap_\"b63\"__is_long_\"b1})}}\"mOneWordID\"i\"mBundleID\"{optional<applesauce::CF::StringRef>=\"\"(?=\"__null_state_\"c\"__val_\"{StringRef=\"mObject\"{ObjectRef<const __CFString *>=\"mCFObject\"^{__CFString}}})\"__engaged_\"B}}"
- "{map<int, std::bitset<255>, std::less<int>, std::allocator<std::pair<const int, std::bitset<255>>>>=\"__tree_\"{__tree<std::__value_type<int, std::bitset<255>>, std::__map_value_compare<int, std::__value_type<int, std::bitset<255>>, std::less<int>>, std::allocator<std::__value_type<int, std::bitset<255>>>>=\"__begin_node_\"^v\"__pair1_\"{__compressed_pair<std::__tree_end_node<std::__tree_node_base<void *> *>, std::allocator<std::__tree_node<std::__value_type<int, std::bitset<255>>, void *>>>=\"__value_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}}\"__pair3_\"{__compressed_pair<unsigned long, std::__map_value_compare<int, std::__value_type<int, std::bitset<255>>, std::less<int>>>=\"__value_\"Q}}}"
- "{map<std::string, std::shared_ptr<NewNotificationCenterObserver>, std::less<std::string>, std::allocator<std::pair<const std::string, std::shared_ptr<NewNotificationCenterObserver>>>>=\"__tree_\"{__tree<std::__value_type<std::string, std::shared_ptr<NewNotificationCenterObserver>>, std::__map_value_compare<std::string, std::__value_type<std::string, std::shared_ptr<NewNotificationCenterObserver>>, std::less<std::string>>, std::allocator<std::__value_type<std::string, std::shared_ptr<NewNotificationCenterObserver>>>>=\"__begin_node_\"^v\"__pair1_\"{__compressed_pair<std::__tree_end_node<std::__tree_node_base<void *> *>, std::allocator<std::__tree_node<std::__value_type<std::string, std::shared_ptr<NewNotificationCenterObserver>>, void *>>>=\"__value_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}}\"__pair3_\"{__compressed_pair<unsigned long, std::__map_value_compare<std::string, std::__value_type<std::string, std::shared_ptr<NewNotificationCenterObserver>>, std::less<std::string>>>=\"__value_\"Q}}}"
- "{map<std::string, std::shared_ptr<OldNotificationCenterObserver>, std::less<std::string>, std::allocator<std::pair<const std::string, std::shared_ptr<OldNotificationCenterObserver>>>>=\"__tree_\"{__tree<std::__value_type<std::string, std::shared_ptr<OldNotificationCenterObserver>>, std::__map_value_compare<std::string, std::__value_type<std::string, std::shared_ptr<OldNotificationCenterObserver>>, std::less<std::string>>, std::allocator<std::__value_type<std::string, std::shared_ptr<OldNotificationCenterObserver>>>>=\"__begin_node_\"^v\"__pair1_\"{__compressed_pair<std::__tree_end_node<std::__tree_node_base<void *> *>, std::allocator<std::__tree_node<std::__value_type<std::string, std::shared_ptr<OldNotificationCenterObserver>>, void *>>>=\"__value_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}}\"__pair3_\"{__compressed_pair<unsigned long, std::__map_value_compare<std::string, std::__value_type<std::string, std::shared_ptr<OldNotificationCenterObserver>>, std::less<std::string>>>=\"__value_\"Q}}}"
- "{map<unsigned int, NSMutableArray<AVServerWrapper *> *, std::less<unsigned int>, std::allocator<std::pair<const unsigned int, NSMutableArray<AVServerWrapper *> *>>>=\"__tree_\"{__tree<std::__value_type<unsigned int, NSMutableArray<AVServerWrapper *> *>, std::__map_value_compare<unsigned int, std::__value_type<unsigned int, NSMutableArray<AVServerWrapper *> *>, std::less<unsigned int>>, std::allocator<std::__value_type<unsigned int, NSMutableArray<AVServerWrapper *> *>>>=\"__begin_node_\"^v\"__pair1_\"{__compressed_pair<std::__tree_end_node<std::__tree_node_base<void *> *>, std::allocator<std::__tree_node<std::__value_type<unsigned int, NSMutableArray<AVServerWrapper *> *>, void *>>>=\"__value_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}}\"__pair3_\"{__compressed_pair<unsigned long, std::__map_value_compare<unsigned int, std::__value_type<unsigned int, NSMutableArray<AVServerWrapper *> *>, std::less<unsigned int>>>=\"__value_\"Q}}}"
- "{stack<unsigned long, std::deque<unsigned long>>=\"c\"{deque<unsigned long, std::allocator<unsigned long>>=\"__map_\"{__split_buffer<unsigned long *, std::allocator<unsigned long *>>=\"__first_\"^^Q\"__begin_\"^^Q\"__end_\"^^Q\"__end_cap_\"{__compressed_pair<unsigned long **, std::allocator<unsigned long *>>=\"__value_\"^^Q}}\"__start_\"Q\"__size_\"{__compressed_pair<unsigned long, std::allocator<unsigned long>>=\"__value_\"Q}}}"
- "{unique_ptr<AudioSessionPropertyListeners, std::default_delete<AudioSessionPropertyListeners>>=\"__ptr_\"{__compressed_pair<AudioSessionPropertyListeners *, std::default_delete<AudioSessionPropertyListeners>>=\"__value_\"^{AudioSessionPropertyListeners}}}"
- "{unique_ptr<Phase::ServerManager, std::default_delete<Phase::ServerManager>>=\"__ptr_\"{__compressed_pair<Phase::ServerManager *, std::default_delete<Phase::ServerManager>>=\"__value_\"^{ServerManager}}}"
- "{unordered_map<std::string, STSPerLabelControllerState, std::hash<std::string>, std::equal_to<std::string>, std::allocator<std::pair<const std::string, STSPerLabelControllerState>>>=\"__table_\"{__hash_table<std::__hash_value_type<std::string, STSPerLabelControllerState>, std::__unordered_map_hasher<std::string, std::__hash_value_type<std::string, STSPerLabelControllerState>, std::hash<std::string>, std::equal_to<std::string>>, std::__unordered_map_equal<std::string, std::__hash_value_type<std::string, STSPerLabelControllerState>, std::equal_to<std::string>, std::hash<std::string>>, std::allocator<std::__hash_value_type<std::string, STSPerLabelControllerState>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, STSPerLabelControllerState>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, STSPerLabelControllerState>, void *> *> *>>>=\"__ptr_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, STSPerLabelControllerState>, void *> *> **, std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, STSPerLabelControllerState>, void *> *> *>>>=\"__value_\"^^v\"__value_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, STSPerLabelControllerState>, void *> *> *>>=\"__data_\"{__compressed_pair<unsigned long, std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, STSPerLabelControllerState>, void *> *> *>>=\"__value_\"Q}}}}\"__p1_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, STSPerLabelControllerState>, void *> *>, std::allocator<std::__hash_node<std::__hash_value_type<std::string, STSPerLabelControllerState>, void *>>>=\"__value_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, STSPerLabelControllerState>, void *> *>=\"__next_\"^v}}\"__p2_\"{__compressed_pair<unsigned long, std::__unordered_map_hasher<std::string, std::__hash_value_type<std::string, STSPerLabelControllerState>, std::hash<std::string>, std::equal_to<std::string>>>=\"__value_\"Q}\"__p3_\"{__compressed_pair<float, std::__unordered_map_equal<std::string, std::__hash_value_type<std::string, STSPerLabelControllerState>, std::equal_to<std::string>, std::hash<std::string>>>=\"__value_\"f}}}"
- "{unordered_map<unsigned int, std::unordered_set<void *>, std::hash<unsigned int>, std::equal_to<unsigned int>, std::allocator<std::pair<const unsigned int, std::unordered_set<void *>>>>=\"__table_\"{__hash_table<std::__hash_value_type<unsigned int, std::unordered_set<void *>>, std::__unordered_map_hasher<unsigned int, std::__hash_value_type<unsigned int, std::unordered_set<void *>>, std::hash<unsigned int>, std::equal_to<unsigned int>>, std::__unordered_map_equal<unsigned int, std::__hash_value_type<unsigned int, std::unordered_set<void *>>, std::equal_to<unsigned int>, std::hash<unsigned int>>, std::allocator<std::__hash_value_type<unsigned int, std::unordered_set<void *>>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, std::unordered_set<void *>>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, std::unordered_set<void *>>, void *> *> *>>>=\"__ptr_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, std::unordered_set<void *>>, void *> *> **, std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, std::unordered_set<void *>>, void *> *> *>>>=\"__value_\"^^v\"__value_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, std::unordered_set<void *>>, void *> *> *>>=\"__data_\"{__compressed_pair<unsigned long, std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, std::unordered_set<void *>>, void *> *> *>>=\"__value_\"Q}}}}\"__p1_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, std::unordered_set<void *>>, void *> *>, std::allocator<std::__hash_node<std::__hash_value_type<unsigned int, std::unordered_set<void *>>, void *>>>=\"__value_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, std::unordered_set<void *>>, void *> *>=\"__next_\"^v}}\"__p2_\"{__compressed_pair<unsigned long, std::__unordered_map_hasher<unsigned int, std::__hash_value_type<unsigned int, std::unordered_set<void *>>, std::hash<unsigned int>, std::equal_to<unsigned int>>>=\"__value_\"Q}\"__p3_\"{__compressed_pair<float, std::__unordered_map_equal<unsigned int, std::__hash_value_type<unsigned int, std::unordered_set<void *>>, std::equal_to<unsigned int>, std::hash<unsigned int>>>=\"__value_\"f}}}"
- "~AQRemoteClient"
- "~WorkThreadSynchronizer"

```
