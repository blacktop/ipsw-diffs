## CoreUtils

> `/System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils`

```diff

-800.15.0.0.0
-  __TEXT.__text: 0x118f2c
+810.16.0.0.0
+  __TEXT.__text: 0x1196a8
   __TEXT.__auth_stubs: 0x2fd0
-  __TEXT.__objc_methlist: 0x9e00
-  __TEXT.__cstring: 0x226a2
-  __TEXT.__const: 0x2208
-  __TEXT.__gcc_except_tab: 0x1d68
-  __TEXT.__oslogstring: 0xe44
-  __TEXT.__unwind_info: 0x3928
-  __TEXT.__eh_frame: 0x50
+  __TEXT.__objc_methlist: 0x9ec8
+  __TEXT.__cstring: 0x22922
+  __TEXT.__const: 0x215c
+  __TEXT.__gcc_except_tab: 0x1de0
+  __TEXT.__oslogstring: 0xe2a
+  __TEXT.__unwind_info: 0x3960
   __TEXT.__objc_classname: 0xcd5
-  __TEXT.__objc_methname: 0x1621b
-  __TEXT.__objc_methtype: 0x46ec
-  __TEXT.__objc_stubs: 0xa540
-  __DATA_CONST.__got: 0x690
-  __DATA_CONST.__const: 0x29c0
+  __TEXT.__objc_methname: 0x1648c
+  __TEXT.__objc_methtype: 0x46a4
+  __TEXT.__objc_stubs: 0xa700
+  __DATA_CONST.__got: 0x698
+  __DATA_CONST.__const: 0x29b8
   __DATA_CONST.__objc_classlist: 0x360
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x148
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4d68
+  __DATA_CONST.__objc_selrefs: 0x4df0
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x248
   __DATA_CONST.__objc_arraydata: 0x8
   __AUTH_CONST.__auth_got: 0x17f8
-  __AUTH_CONST.__const: 0x2730
-  __AUTH_CONST.__cfstring: 0x42e0
-  __AUTH_CONST.__objc_const: 0x13f20
+  __AUTH_CONST.__const: 0x2748
+  __AUTH_CONST.__cfstring: 0x43c0
+  __AUTH_CONST.__objc_const: 0x13ff0
   __AUTH_CONST.__objc_intobj: 0x258
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x1f40
-  __AUTH.__data: 0xa18
-  __DATA.__objc_ivar: 0x1570
-  __DATA.__data: 0x2fe0
-  __DATA.__bss: 0x12a0
+  __AUTH.__data: 0xa28
+  __DATA.__objc_ivar: 0x1580
+  __DATA.__data: 0x30c0
+  __DATA.__bss: 0x12e0
   __DATA.__common: 0x2a
   __DATA_DIRTY.__objc_data: 0x280
   __DATA_DIRTY.__data: 0x178

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: BA1BDC83-8B01-3087-89C6-71533CB02FA3
-  Functions: 5740
-  Symbols:   16701
-  CStrings:  10166
+  UUID: 76F6F3E2-E646-3CE5-9499-70331C049DFA
+  Functions: 5762
+  Symbols:   16778
+  CStrings:  10215
 
Symbols:
+ +[CUFile fileIODispatchQueue]
+ +[CUFile resolveRelativePath:rootPath:dispatchQueue:completionHandler:]
+ +[CUFile resolveRelativePath:rootPath:error:]
+ +[CUUserNotificationSession addMockSession:mockID:]
+ +[CUUserNotificationSession removeMockSession:mockID:]
+ +[CUUserNotificationSession reportAction:error:mockID:]
+ -[CUNANDataSession pairingBundleID]
+ -[CUNANDataSession setPairingBundleID:]
+ -[CUNANPublisher _scheduleRetry]
+ -[CUNANPublisher pairingBundleID]
+ -[CUNANPublisher scheduleRetry]
+ -[CUNANPublisher setPairingBundleID:]
+ -[CUUserNotificationSession icon]
+ -[CUUserNotificationSession mockID]
+ -[CUUserNotificationSession setIcon:]
+ -[CUUserNotificationSession setMockID:]
+ GCC_except_table1007
+ GCC_except_table1360
+ GCC_except_table1395
+ GCC_except_table1400
+ GCC_except_table1401
+ GCC_except_table1477
+ GCC_except_table1478
+ GCC_except_table1509
+ GCC_except_table1518
+ GCC_except_table1523
+ GCC_except_table1574
+ GCC_except_table1575
+ GCC_except_table1612
+ GCC_except_table1643
+ GCC_except_table1666
+ GCC_except_table1668
+ GCC_except_table1672
+ GCC_except_table1684
+ GCC_except_table1686
+ GCC_except_table1698
+ GCC_except_table2338
+ GCC_except_table2339
+ GCC_except_table2362
+ GCC_except_table2402
+ GCC_except_table2477
+ GCC_except_table2501
+ GCC_except_table2538
+ GCC_except_table2542
+ GCC_except_table2605
+ GCC_except_table2606
+ GCC_except_table2609
+ GCC_except_table2616
+ GCC_except_table2619
+ GCC_except_table2622
+ GCC_except_table2625
+ GCC_except_table2628
+ GCC_except_table2635
+ GCC_except_table2638
+ GCC_except_table2707
+ GCC_except_table3027
+ GCC_except_table3028
+ GCC_except_table3116
+ GCC_except_table3138
+ GCC_except_table3172
+ GCC_except_table3176
+ GCC_except_table3220
+ GCC_except_table3223
+ GCC_except_table3224
+ GCC_except_table3226
+ GCC_except_table3524
+ GCC_except_table3945
+ GCC_except_table4203
+ GCC_except_table4258
+ GCC_except_table4265
+ GCC_except_table4273
+ GCC_except_table4425
+ GCC_except_table4429
+ GCC_except_table4431
+ GCC_except_table4433
+ GCC_except_table4456
+ GCC_except_table4530
+ GCC_except_table4532
+ GCC_except_table4535
+ GCC_except_table4537
+ GCC_except_table4539
+ GCC_except_table4541
+ GCC_except_table4547
+ GCC_except_table4568
+ GCC_except_table4569
+ GCC_except_table4571
+ GCC_except_table4572
+ GCC_except_table4577
+ GCC_except_table4578
+ GCC_except_table4600
+ GCC_except_table4604
+ GCC_except_table4606
+ GCC_except_table4607
+ GCC_except_table4608
+ GCC_except_table4609
+ GCC_except_table4610
+ GCC_except_table4611
+ GCC_except_table4612
+ GCC_except_table4613
+ GCC_except_table4614
+ GCC_except_table4615
+ GCC_except_table4617
+ GCC_except_table4618
+ GCC_except_table4619
+ GCC_except_table4621
+ GCC_except_table5237
+ GCC_except_table5242
+ GCC_except_table5246
+ GCC_except_table5314
+ GCC_except_table5325
+ GCC_except_table5335
+ GCC_except_table5344
+ GCC_except_table5607
+ GCC_except_table5608
+ GCC_except_table5621
+ GCC_except_table696
+ GCC_except_table789
+ GCC_except_table804
+ GCC_except_table806
+ _ACAccountStoreFunction.8215
+ _AKAccountManagerFunction.8204
+ _AVAudioSessionFunction.9476
+ _AVFoundationLibrary.sLib.9480
+ _AVFoundationLibrary.sOnce.9472
+ _AccountsLibrary.sLib.8218
+ _AccountsLibrary.sOnce.8212
+ _AppleAccountLibrary.sLib.8221
+ _AppleAccountLibrary.sOnce.8208
+ _AuthKitLibrary.sLib.8207
+ _AuthKitLibrary.sOnce.8201
+ _BTServiceSpecificEventToString.1984
+ _CBCentralManagerFunction.1373
+ _CBCentralManagerFunction.2084
+ _CBManagerIsPrivilegedDaemonKeyFunction.1351
+ _CBManagerNeedsRestrictedStateOperationFunction.1368
+ _CBPeripheralManagerFunction.1535
+ _CBPeripheralManagerFunction.2076
+ _CULocalizedString
+ _CULocalizedString.bundle
+ _CULocalizedString.sOnce
+ _CoreAnalyticsLibrary.sLib.8651
+ _CoreAnalyticsLibrary.sOnce.8649
+ _CoreBluetoothLibrary.sLib.1146
+ _CoreBluetoothLibrary.sLib.1324
+ _CoreBluetoothLibrary.sLib.1540
+ _CoreBluetoothLibrary.sLib.2079
+ _CoreBluetoothLibrary.sLib.2329
+ _CoreBluetoothLibrary.sOnce.1144
+ _CoreBluetoothLibrary.sOnce.1322
+ _CoreBluetoothLibrary.sOnce.1530
+ _CoreBluetoothLibrary.sOnce.2073
+ _CoreBluetoothLibrary.sOnce.2327
+ _CoreHAPLibrary.sLib.5802
+ _CoreHAPLibrary.sOnce.5796
+ _HAPSystemKeychainStoreFunction.5799
+ _MobileBluetoothLibrary.sLib.1943
+ _MobileBluetoothLibrary.sOnce.1942
+ _MobileCoreServicesLibrary.sLib.13634
+ _MobileCoreServicesLibrary.sLib.792
+ _MobileCoreServicesLibrary.sOnce.13633
+ _MobileCoreServicesLibrary.sOnce.791
+ _OBJC_IVAR_$_CUNANDataSession._pairingBundleID
+ _OBJC_IVAR_$_CUNANPublisher._pairingBundleID
+ _OBJC_IVAR_$_CUNANPublisher._retryPending
+ _OBJC_IVAR_$_CUUserNotificationSession._icon
+ _OBJC_IVAR_$_CUUserNotificationSession._mockID
+ _RapportLibrary.sLib.5818
+ _RapportLibrary.sOnce.5813
+ _WiFiAwareInternetSharingConfigurationFunction.4925
+ _WiFiAwarePairingMetadataFunction
+ _WiFiAwarePairingMetadataFunction.4915
+ _WiFiPeerToPeerLibrary.sLib.4871
+ _WiFiPeerToPeerLibrary.sLib.5205
+ _WiFiPeerToPeerLibrary.sLib.9907
+ _WiFiPeerToPeerLibrary.sOnce.4866
+ _WiFiPeerToPeerLibrary.sOnce.5200
+ _WiFiPeerToPeerLibrary.sOnce.9906
+ __AddAppInfoTLV
+ __ExtractAppInfoTLV
+ __NetTransportFinalize.12025
+ __NetTransportFinalize.12033
+ __NetTransportInitialize.12026
+ __NetTransportInitialize.12036
+ __NetTransportRead.12022
+ __NetTransportRead.12035
+ __NetTransportWriteV.12021
+ __NetTransportWriteV.12034
+ __OBJC_$_CLASS_METHODS_CUUserNotificationSession
+ __OBJC_$_CLASS_PROP_LIST_CUFile
+ ___29+[CUFile fileIODispatchQueue]_block_invoke
+ ___31-[CUNANPublisher scheduleRetry]_block_invoke
+ ___55+[CUUserNotificationSession reportAction:error:mockID:]_block_invoke
+ ___61-[CUNANPublisher sendMessageData:endpoint:completionHandler:]_block_invoke.52
+ ___61-[CUNANPublisher sendMessageData:endpoint:completionHandler:]_block_invoke.55
+ ___71+[CUFile resolveRelativePath:rootPath:dispatchQueue:completionHandler:]_block_invoke
+ ___AVFoundationLibrary_block_invoke.9478
+ ___AccountsLibrary_block_invoke.8217
+ ___AppleAccountLibrary_block_invoke.8220
+ ___AuthKitLibrary_block_invoke.8206
+ ___Block_byref_object_copy_.10464
+ ___Block_byref_object_copy_.10958
+ ___Block_byref_object_copy_.12584
+ ___Block_byref_object_copy_.2719
+ ___Block_byref_object_copy_.2972
+ ___Block_byref_object_copy_.4874
+ ___Block_byref_object_copy_.5228
+ ___Block_byref_object_copy_.5760
+ ___Block_byref_object_copy_.6085
+ ___Block_byref_object_copy_.8994
+ ___Block_byref_object_dispose_.10465
+ ___Block_byref_object_dispose_.10959
+ ___Block_byref_object_dispose_.12585
+ ___Block_byref_object_dispose_.2720
+ ___Block_byref_object_dispose_.2973
+ ___Block_byref_object_dispose_.4875
+ ___Block_byref_object_dispose_.5229
+ ___Block_byref_object_dispose_.5761
+ ___Block_byref_object_dispose_.6086
+ ___Block_byref_object_dispose_.8995
+ ___CULocalizedString_block_invoke
+ ___CoreAnalyticsLibrary_block_invoke.8686
+ ___CoreBluetoothLibrary_block_invoke.1149
+ ___CoreBluetoothLibrary_block_invoke.1327
+ ___CoreBluetoothLibrary_block_invoke.1538
+ ___CoreBluetoothLibrary_block_invoke.2078
+ ___CoreBluetoothLibrary_block_invoke.2332
+ ___CoreHAPLibrary_block_invoke.5801
+ ___MobileBluetoothLibrary_block_invoke.1947
+ ___MobileCoreServicesLibrary_block_invoke.13637
+ ___MobileCoreServicesLibrary_block_invoke.795
+ ___RapportLibrary_block_invoke.5817
+ ___WiFiPeerToPeerLibrary_block_invoke.4869
+ ___WiFiPeerToPeerLibrary_block_invoke.5203
+ ___WiFiPeerToPeerLibrary_block_invoke.9910
+ ___block_descriptor_tmp.14620
+ ___block_descriptor_tmp.3.14636
+ ___block_literal_global.1013
+ ___block_literal_global.10261
+ ___block_literal_global.10497
+ ___block_literal_global.10911
+ ___block_literal_global.1145
+ ___block_literal_global.11999
+ ___block_literal_global.12361
+ ___block_literal_global.1323
+ ___block_literal_global.13553
+ ___block_literal_global.141.8322
+ ___block_literal_global.14479
+ ___block_literal_global.14623
+ ___block_literal_global.1531
+ ___block_literal_global.155.8305
+ ___block_literal_global.1743
+ ___block_literal_global.1960
+ ___block_literal_global.2328
+ ___block_literal_global.260.10940
+ ___block_literal_global.280.8242
+ ___block_literal_global.2814
+ ___block_literal_global.282.9924
+ ___block_literal_global.283
+ ___block_literal_global.285.9921
+ ___block_literal_global.29.8353
+ ___block_literal_global.294.9916
+ ___block_literal_global.300.9912
+ ___block_literal_global.3001
+ ___block_literal_global.314.8195
+ ___block_literal_global.33.8354
+ ___block_literal_global.336
+ ___block_literal_global.3388
+ ___block_literal_global.339
+ ___block_literal_global.3590
+ ___block_literal_global.41.8355
+ ___block_literal_global.413.8148
+ ___block_literal_global.4564
+ ___block_literal_global.47.8357
+ ___block_literal_global.4888
+ ___block_literal_global.5115
+ ___block_literal_global.52.8359
+ ___block_literal_global.538.8120
+ ___block_literal_global.58.8360
+ ___block_literal_global.5814
+ ___block_literal_global.59
+ ___block_literal_global.6590
+ ___block_literal_global.7.14625
+ ___block_literal_global.7031
+ ___block_literal_global.7317
+ ___block_literal_global.7526
+ ___block_literal_global.7990
+ ___block_literal_global.832
+ ___block_literal_global.8352
+ ___block_literal_global.8650
+ ___block_literal_global.884
+ ___block_literal_global.9259
+ ___block_literal_global.9492
+ ___block_literal_global.9661
+ ___block_literal_global.9927
+ ___initValCBManagerIsPrivilegedDaemonKey_block_invoke.1349
+ ___initValCBManagerNeedsRestrictedStateOperation_block_invoke.1366
+ ___logger_block_invoke.12365
+ ___logger_block_invoke.14483
+ ___logger_block_invoke.14632
+ ___logger_block_invoke.4852
+ ___logger_block_invoke.5119
+ ___logger_block_invoke.7530
+ ___logger_block_invoke.8238
+ ___logger_block_invoke.9866
+ __btServiceEventHandler.2037
+ __btSessionEventCallback.2069
+ _classACAccountStore.8213
+ _classAKAccountManager.8202
+ _classAVAudioSession.9474
+ _classCBCentralManager.1371
+ _classCBCentralManager.2082
+ _classCBPeripheralManager.1533
+ _classCBPeripheralManager.2074
+ _classHAPSystemKeychainStore.5797
+ _classWiFiAwareInternetSharingConfiguration.4923
+ _classWiFiAwarePairingMetadata
+ _classWiFiAwarePairingMetadata.4913
+ _constantValCBManagerIsPrivilegedDaemonKey.1347
+ _constantValCBManagerNeedsRestrictedStateOperation.1364
+ _fileIODispatchQueue.onceToken
+ _fileIODispatchQueue.queue
+ _gCFArrayType.12287
+ _gCFBooleanType.12288
+ _gCFDataType.12289
+ _gCFDateType.12290
+ _gCFDictionaryType.12291
+ _gCFNumberType.12286
+ _gCFStringType.12292
+ _gLogCategory_HTTPMessage
+ _gLogCategory_HTTPUtils
+ _gMockLock
+ _gMockSessions
+ _getACAccountStoreClass.8209
+ _getAKAccountManagerClass.8190
+ _getAVAudioSessionClass.9460
+ _getCBCentralManagerClass.1352
+ _getCBCentralManagerClass.2043
+ _getCBManagerIsPrivilegedDaemonKey.1343
+ _getCBManagerNeedsRestrictedStateOperation.1353
+ _getCBPeripheralManagerClass.1525
+ _getCBPeripheralManagerClass.2045
+ _getHAPSystemKeychainStoreClass.5793
+ _getWiFiAwareInternetSharingConfigurationClass.4898
+ _getWiFiAwarePairingMetadataClass
+ _getWiFiAwarePairingMetadataClass.4904
+ _initACAccountStore.8211
+ _initAKAccountManager.8200
+ _initAVAudioSession.9471
+ _initAnalyticsSendEvent.8668
+ _initBTDeviceFromAddress.2007
+ _initBTDeviceFromIdentifier.2009
+ _initBTDeviceGetAddressString.1982
+ _initBTDeviceGetConnectedServices.1950
+ _initBTServiceAddCallbacks.2066
+ _initBTServiceRemoveCallbacks.2040
+ _initBTSessionAttachWithQueue.2068
+ _initBTSessionDetachWithQueue.2036
+ _initCBCentralManager.1370
+ _initCBCentralManager.2081
+ _initCBPeripheralManager.1529
+ _initCBPeripheralManager.2072
+ _initHAPSystemKeychainStore.5795
+ _initValCBManagerIsPrivilegedDaemonKey.1345
+ _initValCBManagerNeedsRestrictedStateOperation.1362
+ _initWiFiAwareInternetSharingConfiguration.4922
+ _initWiFiAwarePairingMetadata
+ _initWiFiAwarePairingMetadata.4911
+ _logger.12357
+ _logger.14400
+ _logger.4848
+ _logger.5112
+ _logger.7523
+ _logger.8233
+ _logger.9861
+ _objc_msgSend$_scheduleRetry
+ _objc_msgSend$actionHandler
+ _objc_msgSend$addMockSession:mockID:
+ _objc_msgSend$bundleWithIdentifier:
+ _objc_msgSend$initWithBundleID:selfPairingName:peerDeviceName:storageClass:lifetime:pairingClient:
+ _objc_msgSend$initWithContentsOfFile:
+ _objc_msgSend$localizations
+ _objc_msgSend$mockID
+ _objc_msgSend$pathForResource:ofType:inDirectory:forLocalization:
+ _objc_msgSend$preferredLocalizationsFromArray:forPreferences:
+ _objc_msgSend$removeMockSession:mockID:
+ _objc_msgSend$resolveRelativePath:rootPath:error:
+ _objc_msgSend$scheduleRetry
+ _objc_msgSend$setShouldDisplayActionsInline:
+ _sCUOSLogCreateOnce_logger.12360
+ _sCUOSLogCreateOnce_logger.14478
+ _sCUOSLogCreateOnce_logger.14624
+ _sCUOSLogCreateOnce_logger.4849
+ _sCUOSLogCreateOnce_logger.5114
+ _sCUOSLogCreateOnce_logger.7525
+ _sCUOSLogCreateOnce_logger.8235
+ _sCUOSLogCreateOnce_logger.9863
+ _sCUOSLogHandle_logger.12362
+ _sCUOSLogHandle_logger.14480
+ _sCUOSLogHandle_logger.14626
+ _sCUOSLogHandle_logger.4850
+ _sCUOSLogHandle_logger.5116
+ _sCUOSLogHandle_logger.7527
+ _sCUOSLogHandle_logger.8236
+ _sCUOSLogHandle_logger.9864
+ _softLinkAnalyticsSendEvent.8663
+ _softLinkBTDeviceFromAddress.2004
+ _softLinkBTDeviceFromIdentifier.2001
+ _softLinkBTDeviceGetAddressString.1961
+ _softLinkBTDeviceGetConnectedServices.1932
+ _softLinkBTServiceAddCallbacks.2051
+ _softLinkBTServiceRemoveCallbacks.2030
+ _softLinkBTSessionAttachWithQueue.2048
+ _softLinkBTSessionDetachWithQueue.2033
+ _softLinkOnceCBManagerIsPrivilegedDaemonKey.1346
+ _softLinkOnceCBManagerNeedsRestrictedStateOperation.1363
- GCC_except_table1010
- GCC_except_table1363
- GCC_except_table1398
- GCC_except_table1403
- GCC_except_table1407
- GCC_except_table1480
- GCC_except_table1481
- GCC_except_table1515
- GCC_except_table1521
- GCC_except_table1529
- GCC_except_table1577
- GCC_except_table1578
- GCC_except_table1615
- GCC_except_table1646
- GCC_except_table1669
- GCC_except_table1671
- GCC_except_table1675
- GCC_except_table1687
- GCC_except_table1689
- GCC_except_table1701
- GCC_except_table2335
- GCC_except_table2336
- GCC_except_table2356
- GCC_except_table2394
- GCC_except_table2469
- GCC_except_table2493
- GCC_except_table2530
- GCC_except_table2534
- GCC_except_table2597
- GCC_except_table2598
- GCC_except_table2600
- GCC_except_table2601
- GCC_except_table2603
- GCC_except_table2614
- GCC_except_table2617
- GCC_except_table2620
- GCC_except_table2627
- GCC_except_table2630
- GCC_except_table2699
- GCC_except_table3019
- GCC_except_table3020
- GCC_except_table3108
- GCC_except_table3130
- GCC_except_table3164
- GCC_except_table3168
- GCC_except_table3212
- GCC_except_table3215
- GCC_except_table3216
- GCC_except_table3218
- GCC_except_table3516
- GCC_except_table3937
- GCC_except_table4187
- GCC_except_table4242
- GCC_except_table4249
- GCC_except_table4257
- GCC_except_table4409
- GCC_except_table4413
- GCC_except_table4415
- GCC_except_table4417
- GCC_except_table4440
- GCC_except_table4516
- GCC_except_table4517
- GCC_except_table4518
- GCC_except_table4519
- GCC_except_table4521
- GCC_except_table4523
- GCC_except_table4525
- GCC_except_table4527
- GCC_except_table4552
- GCC_except_table4554
- GCC_except_table4555
- GCC_except_table4557
- GCC_except_table4558
- GCC_except_table4561
- GCC_except_table4562
- GCC_except_table4563
- GCC_except_table4564
- GCC_except_table4565
- GCC_except_table4579
- GCC_except_table4583
- GCC_except_table4584
- GCC_except_table4585
- GCC_except_table4587
- GCC_except_table4588
- GCC_except_table4590
- GCC_except_table4593
- GCC_except_table4594
- GCC_except_table4602
- GCC_except_table5216
- GCC_except_table5221
- GCC_except_table5225
- GCC_except_table5292
- GCC_except_table5302
- GCC_except_table5312
- GCC_except_table5321
- GCC_except_table5585
- GCC_except_table5586
- GCC_except_table5599
- GCC_except_table699
- GCC_except_table792
- GCC_except_table807
- GCC_except_table812
- _ACAccountStoreFunction.8218
- _AKAccountManagerFunction.8207
- _AVAudioSessionFunction.9464
- _AVFoundationLibrary.sLib.9468
- _AVFoundationLibrary.sOnce.9460
- _AccountsLibrary.sLib.8221
- _AccountsLibrary.sOnce.8215
- _AppleAccountLibrary.sLib.8224
- _AppleAccountLibrary.sOnce.8211
- _AuthKitLibrary.sLib.8210
- _AuthKitLibrary.sOnce.8204
- _BTServiceSpecificEventToString.2008
- _CBCentralManagerFunction.1397
- _CBCentralManagerFunction.2108
- _CBManagerIsPrivilegedDaemonKeyFunction.1375
- _CBManagerNeedsRestrictedStateOperationFunction.1392
- _CBPeripheralManagerFunction.1559
- _CBPeripheralManagerFunction.2100
- _CoreAnalyticsLibrary.sLib.8654
- _CoreAnalyticsLibrary.sOnce.8652
- _CoreBluetoothLibrary.sLib.1170
- _CoreBluetoothLibrary.sLib.1348
- _CoreBluetoothLibrary.sLib.1564
- _CoreBluetoothLibrary.sLib.2103
- _CoreBluetoothLibrary.sLib.2353
- _CoreBluetoothLibrary.sOnce.1168
- _CoreBluetoothLibrary.sOnce.1346
- _CoreBluetoothLibrary.sOnce.1554
- _CoreBluetoothLibrary.sOnce.2097
- _CoreBluetoothLibrary.sOnce.2351
- _CoreHAPLibrary.sLib.5807
- _CoreHAPLibrary.sOnce.5801
- _GetFairPlayHWInfo
- _GetFairPlayHWInfoEx
- _HAPSystemKeychainStoreFunction.5804
- _MobileBluetoothLibrary.sLib.1967
- _MobileBluetoothLibrary.sOnce.1966
- _MobileCoreServicesLibrary.sLib.13621
- _MobileCoreServicesLibrary.sLib.816
- _MobileCoreServicesLibrary.sOnce.13620
- _MobileCoreServicesLibrary.sOnce.815
- _OBJC_IVAR_$_CUNANPublisher._activateCompletion
- _RapportLibrary.sLib.5823
- _RapportLibrary.sOnce.5818
- _WiFiAwareInternetSharingConfigurationFunction.4932
- _WiFiPeerToPeerLibrary.sLib.4885
- _WiFiPeerToPeerLibrary.sLib.5211
- _WiFiPeerToPeerLibrary.sLib.9893
- _WiFiPeerToPeerLibrary.sOnce.4879
- _WiFiPeerToPeerLibrary.sOnce.5206
- _WiFiPeerToPeerLibrary.sOnce.9892
- __NetTransportFinalize.12011
- __NetTransportFinalize.12019
- __NetTransportInitialize.12012
- __NetTransportInitialize.12022
- __NetTransportRead.12008
- __NetTransportRead.12021
- __NetTransportWriteV.12007
- __NetTransportWriteV.12020
- __SHA3Final
- __SHA3Init
- __SHA3Update
- __SHA3_Block
- ___61-[CUNANPublisher sendMessageData:endpoint:completionHandler:]_block_invoke.46
- ___61-[CUNANPublisher sendMessageData:endpoint:completionHandler:]_block_invoke.49
- ___AVFoundationLibrary_block_invoke.9466
- ___AccountsLibrary_block_invoke.8220
- ___AppleAccountLibrary_block_invoke.8223
- ___AuthKitLibrary_block_invoke.8209
- ___Block_byref_object_copy_.10444
- ___Block_byref_object_copy_.10942
- ___Block_byref_object_copy_.12567
- ___Block_byref_object_copy_.2743
- ___Block_byref_object_copy_.2996
- ___Block_byref_object_copy_.4887
- ___Block_byref_object_copy_.5234
- ___Block_byref_object_copy_.5765
- ___Block_byref_object_copy_.6090
- ___Block_byref_object_copy_.8999
- ___Block_byref_object_dispose_.10445
- ___Block_byref_object_dispose_.10943
- ___Block_byref_object_dispose_.12568
- ___Block_byref_object_dispose_.2744
- ___Block_byref_object_dispose_.2997
- ___Block_byref_object_dispose_.4888
- ___Block_byref_object_dispose_.5235
- ___Block_byref_object_dispose_.5766
- ___Block_byref_object_dispose_.6091
- ___Block_byref_object_dispose_.9000
- ___CoreAnalyticsLibrary_block_invoke.8689
- ___CoreBluetoothLibrary_block_invoke.1173
- ___CoreBluetoothLibrary_block_invoke.1351
- ___CoreBluetoothLibrary_block_invoke.1562
- ___CoreBluetoothLibrary_block_invoke.2102
- ___CoreBluetoothLibrary_block_invoke.2356
- ___CoreHAPLibrary_block_invoke.5806
- ___MobileBluetoothLibrary_block_invoke.1971
- ___MobileCoreServicesLibrary_block_invoke.13624
- ___MobileCoreServicesLibrary_block_invoke.819
- ___RapportLibrary_block_invoke.5822
- ___WiFiPeerToPeerLibrary_block_invoke.4883
- ___WiFiPeerToPeerLibrary_block_invoke.5209
- ___WiFiPeerToPeerLibrary_block_invoke.9896
- ___block_descriptor_tmp.14607
- ___block_descriptor_tmp.3.14623
- ___block_literal_global.10243
- ___block_literal_global.1037
- ___block_literal_global.10477
- ___block_literal_global.1169
- ___block_literal_global.12347
- ___block_literal_global.1347
- ___block_literal_global.13540
- ___block_literal_global.141.8324
- ___block_literal_global.14466
- ___block_literal_global.14610
- ___block_literal_global.155.8307
- ___block_literal_global.1555
- ___block_literal_global.1767
- ___block_literal_global.1984
- ___block_literal_global.2352
- ___block_literal_global.260.10924
- ___block_literal_global.268
- ___block_literal_global.273
- ___block_literal_global.277.8244
- ___block_literal_global.282.9908
- ___block_literal_global.2838
- ___block_literal_global.29.8355
- ___block_literal_global.294.9902
- ___block_literal_global.300.9898
- ___block_literal_global.3025
- ___block_literal_global.314.8198
- ___block_literal_global.319
- ___block_literal_global.322
- ___block_literal_global.33.8356
- ___block_literal_global.3412
- ___block_literal_global.3614
- ___block_literal_global.41.8357
- ___block_literal_global.413.8151
- ___block_literal_global.4587
- ___block_literal_global.47.8359
- ___block_literal_global.4901
- ___block_literal_global.5121
- ___block_literal_global.52.8361
- ___block_literal_global.53
- ___block_literal_global.538.8123
- ___block_literal_global.58.8362
- ___block_literal_global.5819
- ___block_literal_global.6595
- ___block_literal_global.7.14612
- ___block_literal_global.7035
- ___block_literal_global.7319
- ___block_literal_global.7528
- ___block_literal_global.7994
- ___block_literal_global.8354
- ___block_literal_global.856
- ___block_literal_global.8653
- ___block_literal_global.908
- ___block_literal_global.9250
- ___block_literal_global.9480
- ___block_literal_global.9646
- ___block_literal_global.9911
- ___initValCBManagerIsPrivilegedDaemonKey_block_invoke.1373
- ___initValCBManagerNeedsRestrictedStateOperation_block_invoke.1390
- ___logger_block_invoke.12351
- ___logger_block_invoke.14470
- ___logger_block_invoke.14619
- ___logger_block_invoke.4862
- ___logger_block_invoke.5125
- ___logger_block_invoke.7532
- ___logger_block_invoke.8240
- ___logger_block_invoke.9852
- __btServiceEventHandler.2061
- __btSessionEventCallback.2093
- __kCryptoHashDescriptor_SHA3
- _classACAccountStore.8216
- _classAKAccountManager.8205
- _classAVAudioSession.9462
- _classCBCentralManager.1395
- _classCBCentralManager.2106
- _classCBPeripheralManager.1557
- _classCBPeripheralManager.2098
- _classHAPSystemKeychainStore.5802
- _classWiFiAwareInternetSharingConfiguration.4930
- _constantValCBManagerIsPrivilegedDaemonKey.1371
- _constantValCBManagerNeedsRestrictedStateOperation.1388
- _gCFArrayType.12273
- _gCFBooleanType.12274
- _gCFDataType.12275
- _gCFDateType.12276
- _gCFDictionaryType.12277
- _gCFNumberType.12272
- _gCFStringType.12278
- _getACAccountStoreClass.8212
- _getAKAccountManagerClass.8193
- _getAVAudioSessionClass.9448
- _getCBCentralManagerClass.1376
- _getCBCentralManagerClass.2067
- _getCBManagerIsPrivilegedDaemonKey.1367
- _getCBManagerNeedsRestrictedStateOperation.1377
- _getCBPeripheralManagerClass.1549
- _getCBPeripheralManagerClass.2069
- _getHAPSystemKeychainStoreClass.5798
- _getWiFiAwareInternetSharingConfigurationClass.4911
- _initACAccountStore.8214
- _initAKAccountManager.8203
- _initAVAudioSession.9459
- _initAnalyticsSendEvent.8671
- _initBTDeviceFromAddress.2031
- _initBTDeviceFromIdentifier.2033
- _initBTDeviceGetAddressString.2006
- _initBTDeviceGetConnectedServices.1974
- _initBTServiceAddCallbacks.2090
- _initBTServiceRemoveCallbacks.2064
- _initBTSessionAttachWithQueue.2092
- _initBTSessionDetachWithQueue.2060
- _initCBCentralManager.1394
- _initCBCentralManager.2105
- _initCBPeripheralManager.1553
- _initCBPeripheralManager.2096
- _initHAPSystemKeychainStore.5800
- _initValCBManagerIsPrivilegedDaemonKey.1369
- _initValCBManagerNeedsRestrictedStateOperation.1386
- _initWiFiAwareInternetSharingConfiguration.4928
- _kCryptoHashDescriptor_SHA3
- _kSHA3RoundConstants
- _logger.12343
- _logger.14387
- _logger.4858
- _logger.5118
- _logger.7525
- _logger.8235
- _logger.9847
- _sCUOSLogCreateOnce_logger.12346
- _sCUOSLogCreateOnce_logger.14465
- _sCUOSLogCreateOnce_logger.14611
- _sCUOSLogCreateOnce_logger.4859
- _sCUOSLogCreateOnce_logger.5120
- _sCUOSLogCreateOnce_logger.7527
- _sCUOSLogCreateOnce_logger.8237
- _sCUOSLogCreateOnce_logger.9849
- _sCUOSLogHandle_logger.12348
- _sCUOSLogHandle_logger.14467
- _sCUOSLogHandle_logger.14613
- _sCUOSLogHandle_logger.4860
- _sCUOSLogHandle_logger.5122
- _sCUOSLogHandle_logger.7529
- _sCUOSLogHandle_logger.8238
- _sCUOSLogHandle_logger.9850
- _softLinkAnalyticsSendEvent.8666
- _softLinkBTDeviceFromAddress.2028
- _softLinkBTDeviceFromIdentifier.2025
- _softLinkBTDeviceGetAddressString.1985
- _softLinkBTDeviceGetConnectedServices.1956
- _softLinkBTServiceAddCallbacks.2075
- _softLinkBTServiceRemoveCallbacks.2054
- _softLinkBTSessionAttachWithQueue.2072
- _softLinkBTSessionDetachWithQueue.2057
- _softLinkOnceCBManagerIsPrivilegedDaemonKey.1370
- _softLinkOnceCBManagerNeedsRestrictedStateOperation.1387
CStrings:
+ "### Bad binary length: %zu"
+ "### Bad chunk wrap: %zu vs %zu"
+ "### Bad content length: %llu vs %zu"
+ "### Bad extra data length: %zu vs %zu"
+ "@\"UNNotificationIcon\""
+ "Activate: bundleID=%@, category=%@, mockID=%@"
+ "AppleLanguages"
+ "CUFileIOQueue"
+ "Device"
+ "HTTPUtils"
+ "Localizable"
+ "OSStatus HTTPClientSendBinaryBytes(HTTPClientRef, HTTPMessageFlags, uint8_t, const void *, size_t, HTTPMessageBinaryCompletion_f, void *)"
+ "OSStatus HTTPMessageReadMessageEx(HTTPMessageRef, NetTransportRead_f, void *)"
+ "OSStatus HTTPReadLine(HTTPHeader *, NetTransportRead_f, void *, const char **, size_t *)"
+ "OSStatus _HTTPMessageProcessChunkHeader(HTTPMessageRef, uint64_t)"
+ "Path matches root"
+ "T@\"NSObject<OS_dispatch_queue>\",R"
+ "T@\"NSString\",C,N,V_pairingBundleID"
+ "T@\"NSString\",C,V_mockID"
+ "T@\"UNNotificationIcon\",C,N,V_icon"
+ "WFAPublisher retry"
+ "WiFiAwarePairingMetadata"
+ "_icon"
+ "_pairingBundleID"
+ "_retryPending"
+ "_scheduleRetry"
+ "addMockSession:mockID:"
+ "bundleWithIdentifier:"
+ "com.apple.Setup"
+ "fileIODispatchQueue"
+ "icon"
+ "initWithBundleID:selfPairingName:peerDeviceName:storageClass:lifetime:pairingClient:"
+ "initWithContentsOfFile:"
+ "localizations"
+ "pairingBundleID"
+ "pathForResource:ofType:inDirectory:forLocalization:"
+ "preferredLocalizationsFromArray:forPreferences:"
+ "realpath failed: path=%s"
+ "removeMockSession:mockID:"
+ "reportAction:error:mockID:"
+ "resolveRelativePath:rootPath:dispatchQueue:completionHandler:"
+ "resolveRelativePath:rootPath:error:"
+ "scheduleRetry"
+ "setPairingBundleID:"
+ "setShouldDisplayActionsInline:"
+ "strings"
+ "updateARP: no AF_LINK"
+ "v36@0:8i16@20@28"
+ "\xf1"
- "%2hhx"
- "Activate: BundleID %@, Category %@\n"
- "Publisher start failed"
- "WFAPublisher restarting after unexpected termination"
- "dataSession:confirmedForPeerDataAddress:serviceSpecificInfo:pairingKeyStoreID:"
- "realpath failed"
- "v48@0:8@\"WiFiAwareDataSession\"16@\"WiFiMACAddress\"24@\"WiFiAwarePublishDatapathServiceSpecificInfo\"32@\"NSUUID\"40"
- "\xe1"

```
