## CoreUtils

> `/System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils`

```diff

-780.15.0.0.0
-  __TEXT.__text: 0x11abfc
-  __TEXT.__auth_stubs: 0x3010
-  __TEXT.__objc_methlist: 0x9c40
-  __TEXT.__cstring: 0x2284c
-  __TEXT.__const: 0x2308
-  __TEXT.__gcc_except_tab: 0x1d38
-  __TEXT.__oslogstring: 0xd69
-  __TEXT.__unwind_info: 0x3a10
+790.21.0.0.0
+  __TEXT.__text: 0x11e010
+  __TEXT.__auth_stubs: 0x3030
+  __TEXT.__objc_methlist: 0x9ce0
+  __TEXT.__cstring: 0x23038
+  __TEXT.__const: 0x2380
+  __TEXT.__gcc_except_tab: 0x1d64
+  __TEXT.__oslogstring: 0xd90
+  __TEXT.__unwind_info: 0x3a60
   __TEXT.__eh_frame: 0x50
-  __TEXT.__objc_classname: 0xcd1
-  __TEXT.__objc_methname: 0x15875
-  __TEXT.__objc_methtype: 0x42d2
-  __TEXT.__objc_stubs: 0xa2c0
-  __DATA_CONST.__got: 0x660
-  __DATA_CONST.__const: 0x29c0
+  __TEXT.__objc_classname: 0xcd4
+  __TEXT.__objc_methname: 0x15b3c
+  __TEXT.__objc_methtype: 0x4332
+  __TEXT.__objc_stubs: 0xa460
+  __DATA_CONST.__got: 0x690
+  __DATA_CONST.__const: 0x29e8
   __DATA_CONST.__objc_classlist: 0x360
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x148
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4c28
+  __DATA_CONST.__objc_selrefs: 0x4ca0
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x248
   __DATA_CONST.__objc_arraydata: 0x8
-  __AUTH_CONST.__auth_got: 0x1818
-  __AUTH_CONST.__const: 0x1ff0
-  __AUTH_CONST.__cfstring: 0x4400
-  __AUTH_CONST.__objc_const: 0x13c38
+  __AUTH_CONST.__auth_got: 0x1828
+  __AUTH_CONST.__const: 0x27f0
+  __AUTH_CONST.__cfstring: 0x4460
+  __AUTH_CONST.__objc_const: 0x13cf0
   __AUTH_CONST.__objc_intobj: 0x258
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x1f40
-  __AUTH.__data: 0xb18
-  __DATA.__objc_ivar: 0x1538
+  __AUTH.__data: 0xb28
+  __DATA.__objc_ivar: 0x1548
   __DATA.__data: 0x31b0
-  __DATA.__bss: 0x1110
+  __DATA.__bss: 0x1330
   __DATA.__common: 0x2a
   __DATA_DIRTY.__objc_data: 0x280
   __DATA_DIRTY.__data: 0x178

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: A9868D9F-6624-34DC-B0F3-398B26E71C32
-  Functions: 5755
-  Symbols:   16550
-  CStrings:  10122
+  UUID: 3791312E-3F0C-3426-A69F-0298317BEEA7
+  Functions: 5847
+  Symbols:   16890
+  CStrings:  10195
 
Symbols:
+ +[CUFile realPath:dispatchQueue:completionHandler:]
+ +[CUFile realPath:error:]
+ +[CUPairingManager copySystemPairingIdentifierWithFlags:error:]
+ -[CUFile _getLengthWithCompletionHandler:]
+ -[CUFile getLengthWithCompletionHandler:]
+ -[CUNANDataSession setWfaConnectionMode:]
+ -[CUNANDataSession setWfaServiceSpecificInfo:]
+ -[CUNANDataSession wfaConnectionMode]
+ -[CUNANDataSession wfaServiceSpecificInfo]
+ -[CUNANSubscriber setWfaDiscoveryMode:]
+ -[CUNANSubscriber wfaDiscoveryMode]
+ -[CUWiFiManager _wifiHandleEvent:]
+ -[CUWiFiManager _wifiJoinNotification:status:reason:]
+ GCC_except_table1039
+ GCC_except_table1392
+ GCC_except_table1427
+ GCC_except_table1432
+ GCC_except_table1433
+ GCC_except_table1436
+ GCC_except_table1509
+ GCC_except_table1510
+ GCC_except_table1541
+ GCC_except_table1544
+ GCC_except_table1550
+ GCC_except_table1555
+ GCC_except_table1558
+ GCC_except_table1607
+ GCC_except_table1608
+ GCC_except_table1645
+ GCC_except_table1676
+ GCC_except_table1699
+ GCC_except_table1705
+ GCC_except_table1717
+ GCC_except_table1719
+ GCC_except_table1731
+ GCC_except_table2361
+ GCC_except_table2362
+ GCC_except_table2382
+ GCC_except_table2420
+ GCC_except_table2495
+ GCC_except_table2519
+ GCC_except_table2553
+ GCC_except_table2557
+ GCC_except_table2620
+ GCC_except_table2621
+ GCC_except_table2623
+ GCC_except_table2624
+ GCC_except_table2626
+ GCC_except_table2631
+ GCC_except_table2634
+ GCC_except_table2637
+ GCC_except_table2640
+ GCC_except_table2643
+ GCC_except_table2650
+ GCC_except_table2653
+ GCC_except_table2722
+ GCC_except_table3040
+ GCC_except_table3041
+ GCC_except_table3129
+ GCC_except_table3151
+ GCC_except_table3185
+ GCC_except_table3189
+ GCC_except_table3233
+ GCC_except_table3236
+ GCC_except_table3237
+ GCC_except_table3239
+ GCC_except_table3536
+ GCC_except_table3952
+ GCC_except_table4202
+ GCC_except_table4257
+ GCC_except_table4264
+ GCC_except_table4272
+ GCC_except_table4424
+ GCC_except_table4428
+ GCC_except_table4430
+ GCC_except_table4432
+ GCC_except_table4455
+ GCC_except_table4541
+ GCC_except_table4548
+ GCC_except_table4550
+ GCC_except_table4554
+ GCC_except_table4556
+ GCC_except_table4568
+ GCC_except_table4575
+ GCC_except_table4577
+ GCC_except_table4578
+ GCC_except_table4580
+ GCC_except_table4581
+ GCC_except_table4582
+ GCC_except_table4584
+ GCC_except_table4585
+ GCC_except_table4586
+ GCC_except_table4587
+ GCC_except_table4588
+ GCC_except_table4589
+ GCC_except_table4596
+ GCC_except_table4598
+ GCC_except_table4599
+ GCC_except_table4602
+ GCC_except_table4603
+ GCC_except_table4604
+ GCC_except_table4605
+ GCC_except_table4606
+ GCC_except_table4607
+ GCC_except_table4608
+ GCC_except_table4610
+ GCC_except_table4611
+ GCC_except_table4612
+ GCC_except_table4613
+ GCC_except_table4614
+ GCC_except_table4615
+ GCC_except_table4616
+ GCC_except_table4617
+ GCC_except_table4618
+ GCC_except_table4619
+ GCC_except_table4620
+ GCC_except_table4621
+ GCC_except_table4622
+ GCC_except_table4624
+ GCC_except_table4625
+ GCC_except_table4626
+ GCC_except_table4628
+ GCC_except_table5265
+ GCC_except_table5270
+ GCC_except_table5274
+ GCC_except_table5341
+ GCC_except_table5351
+ GCC_except_table5361
+ GCC_except_table5370
+ GCC_except_table5691
+ GCC_except_table5692
+ GCC_except_table5705
+ GCC_except_table728
+ GCC_except_table821
+ GCC_except_table836
+ GCC_except_table838
+ GCC_except_table841
+ _ACAccountStoreFunction.8162
+ _AKAccountManagerFunction.8151
+ _AVAudioSessionFunction.9412
+ _AVFoundationLibrary.sLib.9416
+ _AVFoundationLibrary.sOnce.9408
+ _AWDLTrafficRegistrationServiceMacVirtualDisplayFunction
+ _AccountsLibrary.sLib.8165
+ _AccountsLibrary.sOnce.8159
+ _AppleAccountLibrary.sLib.8168
+ _AppleAccountLibrary.sOnce.8155
+ _AudioToolboxLibrary.sLib.628
+ _AudioToolboxLibrary.sOnce.627
+ _AuthKitLibrary.sLib.8154
+ _AuthKitLibrary.sOnce.8148
+ _BTServiceSpecificEventToString.2008
+ _CALayerFunction.13175
+ _CATransactionFunction.13192
+ _CBCentralManagerFunction.1398
+ _CBCentralManagerFunction.2108
+ _CBManagerNeedsRestrictedStateOperationFunction.1393
+ _CBPeripheralManagerFunction.1560
+ _CBPeripheralManagerFunction.2100
+ _CWFInterfaceFunction
+ _CoreAnalyticsLibrary.sLib.8600
+ _CoreAnalyticsLibrary.sOnce.8598
+ _CoreAudioLibrary.sLib.611
+ _CoreAudioLibrary.sOnce.609
+ _CoreBluetoothLibrary.sLib.1171
+ _CoreBluetoothLibrary.sLib.1349
+ _CoreBluetoothLibrary.sLib.1565
+ _CoreBluetoothLibrary.sLib.2103
+ _CoreBluetoothLibrary.sLib.2353
+ _CoreBluetoothLibrary.sOnce.1169
+ _CoreBluetoothLibrary.sOnce.1347
+ _CoreBluetoothLibrary.sOnce.1555
+ _CoreBluetoothLibrary.sOnce.2097
+ _CoreBluetoothLibrary.sOnce.2351
+ _CoreGraphicsLibrary.sLib.342
+ _CoreGraphicsLibrary.sOnce.340
+ _CoreHAPLibrary.sLib.5760
+ _CoreHAPLibrary.sOnce.5754
+ _CoreWiFiLibrary.sLib
+ _CoreWiFiLibrary.sOnce
+ _HAPSystemKeychainStoreFunction.5757
+ _HTTPClientSetClientContext
+ _IOSurfaceLibrary.sLib.398
+ _IOSurfaceLibrary.sOnce.397
+ _ImageIOLibrary.sLib.376
+ _ImageIOLibrary.sOnce.375
+ _MobileBluetoothLibrary.sLib.1967
+ _MobileBluetoothLibrary.sOnce.1966
+ _MobileCoreServicesLibrary.sLib.13582
+ _MobileCoreServicesLibrary.sLib.816
+ _MobileCoreServicesLibrary.sOnce.13581
+ _MobileCoreServicesLibrary.sOnce.815
+ _OBJC_IVAR_$_CUNANDataSession._wfaConnectionMode
+ _OBJC_IVAR_$_CUNANDataSession._wfaServiceSpecificInfo
+ _OBJC_IVAR_$_CUNANSubscriber._wfaDiscoveryMode
+ _OBJC_IVAR_$_CUWiFiManager._wifiInterface
+ _QuartzCoreLibrary.sLib.13140
+ _QuartzCoreLibrary.sOnce.13138
+ _RapportLibrary.sLib.5776
+ _RapportLibrary.sOnce.5771
+ _VideoToolboxLibrary.sLib.13147
+ _VideoToolboxLibrary.sOnce.13146
+ _WiFiAwareInternetSharingConfigurationFunction.4906
+ _WiFiDeviceClientRegisterBssidChangeCallback
+ _WiFiDeviceClientRegisterUserJoinNotificationCallback
+ _WiFiPeerToPeerLibrary.sLib.4860
+ _WiFiPeerToPeerLibrary.sLib.5179
+ _WiFiPeerToPeerLibrary.sLib.9844
+ _WiFiPeerToPeerLibrary.sOnce.4857
+ _WiFiPeerToPeerLibrary.sOnce.5174
+ _WiFiPeerToPeerLibrary.sOnce.9843
+ __NetTransportFinalize.11968
+ __NetTransportFinalize.11976
+ __NetTransportInitialize.11969
+ __NetTransportInitialize.11979
+ __NetTransportRead.11965
+ __NetTransportRead.11978
+ __NetTransportWriteV.11964
+ __NetTransportWriteV.11977
+ __OBJC_$_CLASS_METHODS_CUFile
+ __SetupClientAuthenticationFailed
+ __SetupServerAuthenticationFailed
+ ___35-[CUWiFiManager _wifiEnsureStarted]_block_invoke_2
+ ___41-[CUFile getLengthWithCompletionHandler:]_block_invoke
+ ___51+[CUFile realPath:dispatchQueue:completionHandler:]_block_invoke
+ ___AVFoundationLibrary_block_invoke.9414
+ ___AccountsLibrary_block_invoke.8164
+ ___AppleAccountLibrary_block_invoke.8167
+ ___AudioToolboxLibrary_block_invoke.631
+ ___AuthKitLibrary_block_invoke.8153
+ ___Block_byref_object_copy_.10392
+ ___Block_byref_object_copy_.10900
+ ___Block_byref_object_copy_.12534
+ ___Block_byref_object_copy_.2743
+ ___Block_byref_object_copy_.2995
+ ___Block_byref_object_copy_.4862
+ ___Block_byref_object_copy_.5202
+ ___Block_byref_object_copy_.5718
+ ___Block_byref_object_copy_.6043
+ ___Block_byref_object_copy_.8945
+ ___Block_byref_object_dispose_.10393
+ ___Block_byref_object_dispose_.10901
+ ___Block_byref_object_dispose_.12535
+ ___Block_byref_object_dispose_.2744
+ ___Block_byref_object_dispose_.2996
+ ___Block_byref_object_dispose_.4863
+ ___Block_byref_object_dispose_.5203
+ ___Block_byref_object_dispose_.5719
+ ___Block_byref_object_dispose_.6044
+ ___Block_byref_object_dispose_.8946
+ ___CoreAnalyticsLibrary_block_invoke.8634
+ ___CoreAudioLibrary_block_invoke.616
+ ___CoreBluetoothLibrary_block_invoke.1174
+ ___CoreBluetoothLibrary_block_invoke.1352
+ ___CoreBluetoothLibrary_block_invoke.1563
+ ___CoreBluetoothLibrary_block_invoke.2102
+ ___CoreBluetoothLibrary_block_invoke.2356
+ ___CoreGraphicsLibrary_block_invoke.348
+ ___CoreHAPLibrary_block_invoke.5759
+ ___CoreWiFiLibrary_block_invoke
+ ___IOSurfaceLibrary_block_invoke.401
+ ___ImageIOLibrary_block_invoke.379
+ ___MobileBluetoothLibrary_block_invoke.1971
+ ___MobileCoreServicesLibrary_block_invoke.13585
+ ___MobileCoreServicesLibrary_block_invoke.819
+ ___QuartzCoreLibrary_block_invoke.13144
+ ___RapportLibrary_block_invoke.5775
+ ___VideoToolboxLibrary_block_invoke.13150
+ ___WiFiPeerToPeerLibrary_block_invoke.4859
+ ___WiFiPeerToPeerLibrary_block_invoke.5177
+ ___WiFiPeerToPeerLibrary_block_invoke.9847
+ ____wifiBSSIDChangeNotification_block_invoke
+ ____wifiUserJoinNotification_block_invoke
+ ___block_descriptor_40_e8_32w_e18_v16?0"CWFEvent"8lw32l8
+ ___block_descriptor_tmp.11606
+ ___block_descriptor_tmp.11656
+ ___block_descriptor_tmp.14571
+ ___block_descriptor_tmp.3.14581
+ ___block_descriptor_tmp.346
+ ___block_descriptor_tmp.623
+ ___block_descriptor_tmp.7.14576
+ ___block_literal_global.100
+ ___block_literal_global.10191
+ ___block_literal_global.103
+ ___block_literal_global.1037
+ ___block_literal_global.10425
+ ___block_literal_global.107
+ ___block_literal_global.110
+ ___block_literal_global.11443
+ ___block_literal_global.11593
+ ___block_literal_global.11654
+ ___block_literal_global.1170
+ ___block_literal_global.1188
+ ___block_literal_global.1191
+ ___block_literal_global.1194
+ ___block_literal_global.1198
+ ___block_literal_global.120
+ ___block_literal_global.1202
+ ___block_literal_global.1207
+ ___block_literal_global.1218
+ ___block_literal_global.1226
+ ___block_literal_global.1229
+ ___block_literal_global.12306
+ ___block_literal_global.1232
+ ___block_literal_global.1235
+ ___block_literal_global.1240
+ ___block_literal_global.1255
+ ___block_literal_global.1259
+ ___block_literal_global.1263
+ ___block_literal_global.1277
+ ___block_literal_global.1281
+ ___block_literal_global.1307
+ ___block_literal_global.1310
+ ___block_literal_global.1313
+ ___block_literal_global.13139
+ ___block_literal_global.1316
+ ___block_literal_global.1319
+ ___block_literal_global.1322
+ ___block_literal_global.1325
+ ___block_literal_global.1328
+ ___block_literal_global.1331
+ ___block_literal_global.1334
+ ___block_literal_global.1337
+ ___block_literal_global.134
+ ___block_literal_global.1340
+ ___block_literal_global.1343
+ ___block_literal_global.1348
+ ___block_literal_global.13501
+ ___block_literal_global.141.8271
+ ___block_literal_global.14422
+ ___block_literal_global.14574
+ ___block_literal_global.155.8254
+ ___block_literal_global.1556
+ ___block_literal_global.174
+ ___block_literal_global.1767
+ ___block_literal_global.177
+ ___block_literal_global.181
+ ___block_literal_global.195
+ ___block_literal_global.196
+ ___block_literal_global.198
+ ___block_literal_global.1984
+ ___block_literal_global.199
+ ___block_literal_global.201
+ ___block_literal_global.2352
+ ___block_literal_global.257.8194
+ ___block_literal_global.259
+ ___block_literal_global.264.10879
+ ___block_literal_global.271.8189
+ ___block_literal_global.274
+ ___block_literal_global.276.8190
+ ___block_literal_global.279
+ ___block_literal_global.282
+ ___block_literal_global.2838
+ ___block_literal_global.285
+ ___block_literal_global.287
+ ___block_literal_global.288.9855
+ ___block_literal_global.29.8302
+ ___block_literal_global.291
+ ___block_literal_global.294
+ ___block_literal_global.297
+ ___block_literal_global.300
+ ___block_literal_global.300.9849
+ ___block_literal_global.3024
+ ___block_literal_global.303
+ ___block_literal_global.308.9821
+ ___block_literal_global.314
+ ___block_literal_global.317
+ ___block_literal_global.319
+ ___block_literal_global.321
+ ___block_literal_global.322
+ ___block_literal_global.326
+ ___block_literal_global.33.8303
+ ___block_literal_global.341
+ ___block_literal_global.3413
+ ___block_literal_global.3615
+ ___block_literal_global.375.8109
+ ___block_literal_global.387
+ ___block_literal_global.398
+ ___block_literal_global.4
+ ___block_literal_global.401
+ ___block_literal_global.404
+ ___block_literal_global.407.8090
+ ___block_literal_global.41.8304
+ ___block_literal_global.410
+ ___block_literal_global.413.8086
+ ___block_literal_global.416
+ ___block_literal_global.437
+ ___block_literal_global.441
+ ___block_literal_global.444
+ ___block_literal_global.457
+ ___block_literal_global.4577
+ ___block_literal_global.47.8306
+ ___block_literal_global.470
+ ___block_literal_global.473
+ ___block_literal_global.4876
+ ___block_literal_global.5094
+ ___block_literal_global.52.8308
+ ___block_literal_global.538
+ ___block_literal_global.541
+ ___block_literal_global.545
+ ___block_literal_global.5772
+ ___block_literal_global.58.8309
+ ___block_literal_global.610
+ ___block_literal_global.640
+ ___block_literal_global.6536
+ ___block_literal_global.6976
+ ___block_literal_global.7
+ ___block_literal_global.7259
+ ___block_literal_global.7468
+ ___block_literal_global.749
+ ___block_literal_global.765
+ ___block_literal_global.7934
+ ___block_literal_global.8301
+ ___block_literal_global.8599
+ ___block_literal_global.9197
+ ___block_literal_global.9428
+ ___block_literal_global.9594
+ ___block_literal_global.9859
+ ___initValAVAudioSessionCategoryAmbient_block_invoke
+ ___initValAVAudioSessionInterruptionNotification_block_invoke
+ ___initValAWDLTrafficRegistrationServiceAirPlay_block_invoke
+ ___initValAWDLTrafficRegistrationServiceDeviceToDeviceMigration_block_invoke
+ ___initValAWDLTrafficRegistrationServiceMPRemoteCamera_block_invoke
+ ___initValAWDLTrafficRegistrationServiceMacVirtualDisplay_block_invoke
+ ___initValAWDLTrafficRegistrationServiceRemoteCamera_block_invoke
+ ___initValAWDLTrafficRegistrationServiceRemoteScreen_block_invoke
+ ___initValAWDLTrafficRegistrationServiceSidecar_block_invoke
+ ___initValAWDLTrafficRegistrationServiceTVRemoteCamera_block_invoke
+ ___initValAWDLTrafficRegistrationServiceUniversalControl_block_invoke
+ ___initValCBAdvertisementDataAppleMfgData_block_invoke
+ ___initValCBAdvertisementDataDeviceAddress_block_invoke
+ ___initValCBAdvertisementDataIsConnectable_block_invoke
+ ___initValCBAdvertisementDataManufacturerDataKey_block_invoke
+ ___initValCBCentralManagerOptionShowPowerAlertKey_block_invoke
+ ___initValCBCentralManagerScanOptionActive_block_invoke
+ ___initValCBCentralManagerScanOptionAllowDuplicatesKey_block_invoke
+ ___initValCBCentralManagerScanOptionMatchingRuleKey_block_invoke
+ ___initValCBCentralManagerScanOptionMatchingRuleMaskKey_block_invoke
+ ___initValCBCentralManagerScanOptionMatchingRulePayloadKey_block_invoke
+ ___initValCBCentralManagerScanOptionMatchingRuleRSSIKey_block_invoke
+ ___initValCBCentralManagerScanOptionMatchingRuleTypeKey_block_invoke
+ ___initValCBCentralManagerScanOptionScanInterval_block_invoke
+ ___initValCBCentralManagerScanOptionScanWindow_block_invoke
+ ___initValCBConnectPeripheralOptionClientBundleID_block_invoke
+ ___initValCBConnectPeripheralOptionConnectionUseCase_block_invoke
+ ___initValCBManagerIsPrivilegedDaemonKey_block_invoke
+ ___initValCBManagerIsPrivilegedDaemonKey_block_invoke.1374
+ ___initValCBManagerNeedsRestrictedStateOperation_block_invoke
+ ___initValCBManagerNeedsRestrictedStateOperation_block_invoke.1391
+ ___initValCBPeripheralManagerOptionShowPowerAlertKey_block_invoke
+ ___initValCBScalablePipeOptionTransport_block_invoke
+ ___initValEasyConfigKey_DeviceID_block_invoke
+ ___initValEasyConfigKey_Flags_block_invoke
+ ___initValEasyConfigKey_ReasonError_block_invoke
+ ___initValFBSDisplayLayoutElementControlCenterIdentifier_block_invoke
+ ___initValFBSDisplayLayoutElementLockScreenIdentifier_block_invoke
+ ___initValFBSDisplayLayoutElementNotificationCenterIdentifier_block_invoke
+ ___initValFBSDisplayLayoutElementSiriIdentifier_block_invoke
+ ___initValFMFDevicesChangedNotification_block_invoke
+ ___initValFMFMeDeviceChangedNotification_block_invoke
+ ___initValNSFontAttributeName_block_invoke
+ ___initValRPOptionTimeoutSeconds_block_invoke
+ ___initValSBSDisplayLayoutElementAppSwitcherIdentifier_block_invoke
+ ___initValSBSDisplayLayoutElementCarPlayOEMIdentifier_block_invoke
+ ___initValSBSDisplayLayoutElementHomeScreenIdentifier_block_invoke
+ ___initValSBSDisplayLayoutElementLockScreenNavigationIdentifier_block_invoke
+ ___initValSBSDisplayLayoutElementLoginIdentifier_block_invoke
+ ___initValSBSDisplayLayoutElementNowPlayingIdentifier_block_invoke
+ ___initValSBSDisplayLayoutElementPasscodeIdentifier_block_invoke
+ ___initValSBSDisplayLayoutElementSpotlightIdentifier_block_invoke
+ ___initValSBSDisplayLayoutElementTodayViewIdentifier_block_invoke
+ ___initValTUCallCenterCallConnectedNotification_block_invoke
+ ___initValTUCallCenterCallStatusChangedNotification_block_invoke
+ ___initValTUCallCenterVideoCallStatusChangedNotification_block_invoke
+ ___initValUNNotificationDefaultActionIdentifier_block_invoke
+ ___initValUNNotificationDismissActionIdentifier_block_invoke
+ ___initValkCAContextDisplayName_block_invoke
+ ___initValkCAContextIgnoresHitTest_block_invoke
+ ___initValkCAMediaTimingFunctionEaseIn_block_invoke
+ ___initValkCAMediaTimingFunctionEaseOut_block_invoke
+ ___logger_block_invoke.12310
+ ___logger_block_invoke.14426
+ ___logger_block_invoke.4838
+ ___logger_block_invoke.5098
+ ___logger_block_invoke.7472
+ ___logger_block_invoke.8185
+ ___logger_block_invoke.9801
+ __btServiceEventHandler.2061
+ __btSessionEventCallback.2093
+ __wifiBSSIDChangeNotification
+ __wifiUserJoinNotification
+ _classACAccountStore.8160
+ _classAKAccountManager.8149
+ _classAVAudioSession.9410
+ _classCALayer.13173
+ _classCATransaction.13190
+ _classCBCentralManager.1396
+ _classCBCentralManager.2106
+ _classCBPeripheralManager.1558
+ _classCBPeripheralManager.2098
+ _classCWFInterface
+ _classHAPSystemKeychainStore.5755
+ _classWiFiAwareInternetSharingConfiguration.4904
+ _constantValAWDLTrafficRegistrationServiceMacVirtualDisplay
+ _constantValCBManagerIsPrivilegedDaemonKey.1372
+ _constantValCBManagerNeedsRestrictedStateOperation.1389
+ _gCFArrayType.12232
+ _gCFBooleanType.12233
+ _gCFDataType.12234
+ _gCFDateType.12235
+ _gCFDictionaryType.12236
+ _gCFNumberType.12231
+ _gCFStringType.12237
+ _getACAccountStoreClass.8156
+ _getAKAccountManagerClass.8139
+ _getAVAudioSessionClass.9396
+ _getAWDLTrafficRegistrationServiceMacVirtualDisplay
+ _getCALayerClass.13154
+ _getCATransactionClass.13180
+ _getCBCentralManagerClass.2067
+ _getCBManagerIsPrivilegedDaemonKey.1368
+ _getCBPeripheralManagerClass.1550
+ _getCBPeripheralManagerClass.2069
+ _getCWFInterfaceClass
+ _getHAPSystemKeychainStoreClass.5751
+ _getWiFiAwareInternetSharingConfigurationClass.4886
+ _initACAccountStore.8158
+ _initAKAccountManager.8147
+ _initAVAudioSession.9407
+ _initAnalyticsSendEvent.8616
+ _initAudioObjectGetPropertyData.608
+ _initAudioUnitGetParameter.634
+ _initAudioUnitSetParameter.626
+ _initBTDeviceFromAddress.2031
+ _initBTDeviceFromIdentifier.2033
+ _initBTDeviceGetAddressString.2006
+ _initBTDeviceGetConnectedServices.1974
+ _initBTServiceAddCallbacks.2090
+ _initBTServiceRemoveCallbacks.2064
+ _initBTSessionAttachWithQueue.2092
+ _initBTSessionDetachWithQueue.2060
+ _initCALayer.13171
+ _initCATransaction.13188
+ _initCBCentralManager.1395
+ _initCBCentralManager.2105
+ _initCBPeripheralManager.1554
+ _initCBPeripheralManager.2096
+ _initCGColorSpaceCreateDeviceRGB.358
+ _initCGImageDestinationAddImage.382
+ _initCGImageDestinationFinalize.374
+ _initCWFInterface
+ _initHAPSystemKeychainStore.5753
+ _initIOSurfaceGetBaseAddress.404
+ _initIOSurfaceLock.407
+ _initIOSurfaceUnlock.396
+ _initValAWDLTrafficRegistrationServiceMacVirtualDisplay
+ _initValCBManagerIsPrivilegedDaemonKey.1370
+ _initWiFiAwareInternetSharingConfiguration.4903
+ _kWiFiUserJoinNetworkKey
+ _kWiFiUserJoinStatusAssociating
+ _kWiFiUserJoinStatusKey
+ _logger.12302
+ _logger.14348
+ _logger.4834
+ _logger.5091
+ _logger.7465
+ _logger.8180
+ _logger.9796
+ _objc_msgSend$_getLengthWithCompletionHandler:
+ _objc_msgSend$_wifiHandleEvent:
+ _objc_msgSend$_wifiJoinNotification:status:reason:
+ _objc_msgSend$copySystemPairingIdentifierWithFlags:error:
+ _objc_msgSend$finishAndReturnError:
+ _objc_msgSend$finishWithM3:error:
+ _objc_msgSend$generateM1AndReturnError:
+ _objc_msgSend$generateM2WithM1:error:
+ _objc_msgSend$generateM3WithM2:error:
+ _objc_msgSend$initWithPasswordPtr:passwordLength:
+ _objc_msgSend$pairingIdentityWithPrivateKey:attemptToReadFromKeychain:completionHandler:
+ _objc_msgSend$realPath:error:
+ _objc_msgSend$setEventHandler:
+ _objc_msgSend$setTargetQueue:
+ _objc_msgSend$startMonitoringEventType:error:
+ _sCUOSLogCreateOnce_logger.12305
+ _sCUOSLogCreateOnce_logger.14421
+ _sCUOSLogCreateOnce_logger.4835
+ _sCUOSLogCreateOnce_logger.5093
+ _sCUOSLogCreateOnce_logger.7467
+ _sCUOSLogCreateOnce_logger.8182
+ _sCUOSLogCreateOnce_logger.9798
+ _sCUOSLogHandle_logger.12307
+ _sCUOSLogHandle_logger.14423
+ _sCUOSLogHandle_logger.4836
+ _sCUOSLogHandle_logger.5095
+ _sCUOSLogHandle_logger.7469
+ _sCUOSLogHandle_logger.8183
+ _sCUOSLogHandle_logger.9799
+ _softLinkAnalyticsSendEvent.8611
+ _softLinkAudioObjectGetPropertyData.606
+ _softLinkAudioUnitGetParameter.622
+ _softLinkAudioUnitSetParameter.624
+ _softLinkBTDeviceFromAddress.2028
+ _softLinkBTDeviceFromIdentifier.2025
+ _softLinkBTDeviceGetAddressString.1985
+ _softLinkBTDeviceGetConnectedServices.1956
+ _softLinkBTServiceAddCallbacks.2075
+ _softLinkBTServiceRemoveCallbacks.2054
+ _softLinkBTSessionAttachWithQueue.2072
+ _softLinkBTSessionDetachWithQueue.2057
+ _softLinkCGColorSpaceCreateDeviceRGB.356
+ _softLinkCGImageDestinationAddImage.371
+ _softLinkCGImageDestinationFinalize.372
+ _softLinkIOSurfaceGetBaseAddress.389
+ _softLinkIOSurfaceLock.388
+ _softLinkIOSurfaceUnlock.390
+ _softLinkOnceAVAudioSessionCategoryAmbient
+ _softLinkOnceAVAudioSessionInterruptionNotification
+ _softLinkOnceAWDLTrafficRegistrationServiceAirPlay
+ _softLinkOnceAWDLTrafficRegistrationServiceDeviceToDeviceMigration
+ _softLinkOnceAWDLTrafficRegistrationServiceMPRemoteCamera
+ _softLinkOnceAWDLTrafficRegistrationServiceMacVirtualDisplay
+ _softLinkOnceAWDLTrafficRegistrationServiceRemoteCamera
+ _softLinkOnceAWDLTrafficRegistrationServiceRemoteScreen
+ _softLinkOnceAWDLTrafficRegistrationServiceSidecar
+ _softLinkOnceAWDLTrafficRegistrationServiceTVRemoteCamera
+ _softLinkOnceAWDLTrafficRegistrationServiceUniversalControl
+ _softLinkOnceCBAdvertisementDataAppleMfgData
+ _softLinkOnceCBAdvertisementDataDeviceAddress
+ _softLinkOnceCBAdvertisementDataIsConnectable
+ _softLinkOnceCBAdvertisementDataManufacturerDataKey
+ _softLinkOnceCBCentralManagerOptionShowPowerAlertKey
+ _softLinkOnceCBCentralManagerScanOptionActive
+ _softLinkOnceCBCentralManagerScanOptionAllowDuplicatesKey
+ _softLinkOnceCBCentralManagerScanOptionMatchingRuleKey
+ _softLinkOnceCBCentralManagerScanOptionMatchingRuleMaskKey
+ _softLinkOnceCBCentralManagerScanOptionMatchingRulePayloadKey
+ _softLinkOnceCBCentralManagerScanOptionMatchingRuleRSSIKey
+ _softLinkOnceCBCentralManagerScanOptionMatchingRuleTypeKey
+ _softLinkOnceCBCentralManagerScanOptionScanInterval
+ _softLinkOnceCBCentralManagerScanOptionScanWindow
+ _softLinkOnceCBConnectPeripheralOptionClientBundleID
+ _softLinkOnceCBConnectPeripheralOptionConnectionUseCase
+ _softLinkOnceCBManagerIsPrivilegedDaemonKey
+ _softLinkOnceCBManagerIsPrivilegedDaemonKey.1371
+ _softLinkOnceCBManagerNeedsRestrictedStateOperation
+ _softLinkOnceCBManagerNeedsRestrictedStateOperation.1388
+ _softLinkOnceCBPeripheralManagerOptionShowPowerAlertKey
+ _softLinkOnceCBScalablePipeOptionTransport
+ _softLinkOnceEasyConfigKey_DeviceID
+ _softLinkOnceEasyConfigKey_Flags
+ _softLinkOnceEasyConfigKey_ReasonError
+ _softLinkOnceFBSDisplayLayoutElementControlCenterIdentifier
+ _softLinkOnceFBSDisplayLayoutElementLockScreenIdentifier
+ _softLinkOnceFBSDisplayLayoutElementNotificationCenterIdentifier
+ _softLinkOnceFBSDisplayLayoutElementSiriIdentifier
+ _softLinkOnceFMFDevicesChangedNotification
+ _softLinkOnceFMFMeDeviceChangedNotification
+ _softLinkOnceNSFontAttributeName
+ _softLinkOnceRPOptionTimeoutSeconds
+ _softLinkOnceSBSDisplayLayoutElementAppSwitcherIdentifier
+ _softLinkOnceSBSDisplayLayoutElementCarPlayOEMIdentifier
+ _softLinkOnceSBSDisplayLayoutElementHomeScreenIdentifier
+ _softLinkOnceSBSDisplayLayoutElementLockScreenNavigationIdentifier
+ _softLinkOnceSBSDisplayLayoutElementLoginIdentifier
+ _softLinkOnceSBSDisplayLayoutElementNowPlayingIdentifier
+ _softLinkOnceSBSDisplayLayoutElementPasscodeIdentifier
+ _softLinkOnceSBSDisplayLayoutElementSpotlightIdentifier
+ _softLinkOnceSBSDisplayLayoutElementTodayViewIdentifier
+ _softLinkOnceTUCallCenterCallConnectedNotification
+ _softLinkOnceTUCallCenterCallStatusChangedNotification
+ _softLinkOnceTUCallCenterVideoCallStatusChangedNotification
+ _softLinkOnceUNNotificationDefaultActionIdentifier
+ _softLinkOnceUNNotificationDismissActionIdentifier
+ _softLinkOncekCAContextDisplayName
+ _softLinkOncekCAContextIgnoresHitTest
+ _softLinkOncekCAMediaTimingFunctionEaseIn
+ _softLinkOncekCAMediaTimingFunctionEaseOut
- -[CUWiFiManager _wifiAutoJoinNotification:]
- GCC_except_table1013
- GCC_except_table1364
- GCC_except_table1398
- GCC_except_table1403
- GCC_except_table1404
- GCC_except_table1407
- GCC_except_table1480
- GCC_except_table1481
- GCC_except_table1512
- GCC_except_table1515
- GCC_except_table1521
- GCC_except_table1526
- GCC_except_table1529
- GCC_except_table1578
- GCC_except_table1579
- GCC_except_table1616
- GCC_except_table1646
- GCC_except_table1669
- GCC_except_table1671
- GCC_except_table1675
- GCC_except_table1687
- GCC_except_table1689
- GCC_except_table2327
- GCC_except_table2328
- GCC_except_table2348
- GCC_except_table2386
- GCC_except_table2459
- GCC_except_table2483
- GCC_except_table2517
- GCC_except_table2521
- GCC_except_table2584
- GCC_except_table2585
- GCC_except_table2587
- GCC_except_table2588
- GCC_except_table2590
- GCC_except_table2595
- GCC_except_table2598
- GCC_except_table2601
- GCC_except_table2604
- GCC_except_table2607
- GCC_except_table2614
- GCC_except_table2617
- GCC_except_table2686
- GCC_except_table3003
- GCC_except_table3004
- GCC_except_table3092
- GCC_except_table3114
- GCC_except_table3148
- GCC_except_table3152
- GCC_except_table3196
- GCC_except_table3199
- GCC_except_table3200
- GCC_except_table3202
- GCC_except_table3484
- GCC_except_table3897
- GCC_except_table4175
- GCC_except_table4182
- GCC_except_table4190
- GCC_except_table4342
- GCC_except_table4346
- GCC_except_table4348
- GCC_except_table4350
- GCC_except_table4373
- GCC_except_table4457
- GCC_except_table4458
- GCC_except_table4459
- GCC_except_table4460
- GCC_except_table4462
- GCC_except_table4464
- GCC_except_table4466
- GCC_except_table4468
- GCC_except_table4472
- GCC_except_table4474
- GCC_except_table4486
- GCC_except_table4493
- GCC_except_table4495
- GCC_except_table4496
- GCC_except_table4498
- GCC_except_table4499
- GCC_except_table4500
- GCC_except_table4502
- GCC_except_table4503
- GCC_except_table4504
- GCC_except_table4505
- GCC_except_table4506
- GCC_except_table4507
- GCC_except_table4514
- GCC_except_table4516
- GCC_except_table4517
- GCC_except_table4520
- GCC_except_table4521
- GCC_except_table4522
- GCC_except_table4523
- GCC_except_table4524
- GCC_except_table4525
- GCC_except_table4526
- GCC_except_table4528
- GCC_except_table4529
- GCC_except_table4530
- GCC_except_table4531
- GCC_except_table4532
- GCC_except_table4533
- GCC_except_table4534
- GCC_except_table4535
- GCC_except_table4536
- GCC_except_table4537
- GCC_except_table4538
- GCC_except_table4543
- GCC_except_table5176
- GCC_except_table5181
- GCC_except_table5185
- GCC_except_table5252
- GCC_except_table5262
- GCC_except_table5271
- GCC_except_table5279
- GCC_except_table5600
- GCC_except_table5601
- GCC_except_table5614
- GCC_except_table723
- GCC_except_table812
- GCC_except_table826
- GCC_except_table828
- GCC_except_table831
- _ACAccountStoreFunction.8136
- _AKAccountManagerFunction.8125
- _AVAudioSessionFunction.9389
- _AVFoundationLibrary.sLib.9393
- _AVFoundationLibrary.sOnce.9385
- _AccountsLibrary.sLib.8139
- _AccountsLibrary.sOnce.8133
- _AppleAccountLibrary.sLib.8142
- _AppleAccountLibrary.sOnce.8129
- _AudioToolboxLibrary.sLib.627
- _AudioToolboxLibrary.sOnce.626
- _AuthKitLibrary.sLib.8128
- _AuthKitLibrary.sOnce.8122
- _BTServiceSpecificEventToString.2011
- _CALayerFunction.13077
- _CATransactionFunction.13094
- _CBCentralManagerFunction.1395
- _CBCentralManagerFunction.2111
- _CBManagerNeedsRestrictedStateOperationFunction.1390
- _CBPeripheralManagerFunction.1556
- _CBPeripheralManagerFunction.2103
- _CoreAnalyticsLibrary.sLib.8576
- _CoreAnalyticsLibrary.sOnce.8574
- _CoreAudioLibrary.sLib.610
- _CoreAudioLibrary.sOnce.608
- _CoreBluetoothLibrary.sLib.1172
- _CoreBluetoothLibrary.sLib.1350
- _CoreBluetoothLibrary.sLib.1561
- _CoreBluetoothLibrary.sLib.2106
- _CoreBluetoothLibrary.sLib.2356
- _CoreBluetoothLibrary.sOnce.1170
- _CoreBluetoothLibrary.sOnce.1348
- _CoreBluetoothLibrary.sOnce.1551
- _CoreBluetoothLibrary.sOnce.2100
- _CoreBluetoothLibrary.sOnce.2354
- _CoreGraphicsLibrary.sLib.343
- _CoreGraphicsLibrary.sOnce.341
- _CoreHAPLibrary.sLib.5731
- _CoreHAPLibrary.sOnce.5725
- _HAPSystemKeychainStoreFunction.5728
- _IOSurfaceLibrary.sLib.399
- _IOSurfaceLibrary.sOnce.398
- _ImageIOLibrary.sLib.377
- _ImageIOLibrary.sOnce.376
- _MobileBluetoothLibrary.sLib.1962
- _MobileBluetoothLibrary.sOnce.1961
- _MobileCoreServicesLibrary.sLib.13486
- _MobileCoreServicesLibrary.sLib.815
- _MobileCoreServicesLibrary.sOnce.13485
- _MobileCoreServicesLibrary.sOnce.814
- _QuartzCoreLibrary.sLib.13042
- _QuartzCoreLibrary.sOnce.13040
- _RapportLibrary.sLib.5747
- _RapportLibrary.sOnce.5742
- _VideoToolboxLibrary.sLib.13049
- _VideoToolboxLibrary.sOnce.13048
- _WiFiAwareInternetSharingConfigurationFunction.4885
- _WiFiPeerToPeerLibrary.sLib.4839
- _WiFiPeerToPeerLibrary.sLib.5155
- _WiFiPeerToPeerLibrary.sLib.9798
- _WiFiPeerToPeerLibrary.sOnce.4835
- _WiFiPeerToPeerLibrary.sOnce.5150
- _WiFiPeerToPeerLibrary.sOnce.9796
- __NetTransportFinalize.11901
- __NetTransportFinalize.11909
- __NetTransportInitialize.11902
- __NetTransportInitialize.11912
- __NetTransportRead.11898
- __NetTransportRead.11911
- __NetTransportWriteV.11897
- __NetTransportWriteV.11910
- ___AVFoundationLibrary_block_invoke.9391
- ___AccountsLibrary_block_invoke.8138
- ___AppleAccountLibrary_block_invoke.8141
- ___AudioToolboxLibrary_block_invoke.630
- ___AuthKitLibrary_block_invoke.8127
- ___Block_byref_object_copy_.10336
- ___Block_byref_object_copy_.10844
- ___Block_byref_object_copy_.12460
- ___Block_byref_object_copy_.2745
- ___Block_byref_object_copy_.2999
- ___Block_byref_object_copy_.4841
- ___Block_byref_object_copy_.5178
- ___Block_byref_object_copy_.5689
- ___Block_byref_object_copy_.6014
- ___Block_byref_object_copy_.8921
- ___Block_byref_object_dispose_.10337
- ___Block_byref_object_dispose_.10845
- ___Block_byref_object_dispose_.12461
- ___Block_byref_object_dispose_.2746
- ___Block_byref_object_dispose_.3000
- ___Block_byref_object_dispose_.4842
- ___Block_byref_object_dispose_.5179
- ___Block_byref_object_dispose_.5690
- ___Block_byref_object_dispose_.6015
- ___Block_byref_object_dispose_.8922
- ___CoreAnalyticsLibrary_block_invoke.8610
- ___CoreAudioLibrary_block_invoke.615
- ___CoreBluetoothLibrary_block_invoke.1175
- ___CoreBluetoothLibrary_block_invoke.1353
- ___CoreBluetoothLibrary_block_invoke.1559
- ___CoreBluetoothLibrary_block_invoke.2105
- ___CoreBluetoothLibrary_block_invoke.2359
- ___CoreGraphicsLibrary_block_invoke.349
- ___CoreHAPLibrary_block_invoke.5730
- ___IOSurfaceLibrary_block_invoke.402
- ___ImageIOLibrary_block_invoke.380
- ___MobileBluetoothLibrary_block_invoke.1965
- ___MobileCoreServicesLibrary_block_invoke.13489
- ___MobileCoreServicesLibrary_block_invoke.818
- ___QuartzCoreLibrary_block_invoke.13046
- ___RapportLibrary_block_invoke.5746
- ___VideoToolboxLibrary_block_invoke.13052
- ___WiFiPeerToPeerLibrary_block_invoke.4837
- ___WiFiPeerToPeerLibrary_block_invoke.5153
- ___WiFiPeerToPeerLibrary_block_invoke.9802
- ___block_descriptor_tmp.11550
- ___block_descriptor_tmp.11600
- ___block_descriptor_tmp.14471
- ___block_descriptor_tmp.3.14481
- ___block_descriptor_tmp.347
- ___block_descriptor_tmp.622
- ___block_descriptor_tmp.7.14476
- ___block_literal_global.10135
- ___block_literal_global.1036
- ___block_literal_global.10369
- ___block_literal_global.112.3405
- ___block_literal_global.11387
- ___block_literal_global.11537
- ___block_literal_global.11598
- ___block_literal_global.1171
- ___block_literal_global.1192
- ___block_literal_global.1196
- ___block_literal_global.1201
- ___block_literal_global.1212
- ___block_literal_global.1220
- ___block_literal_global.12239
- ___block_literal_global.1224
- ___block_literal_global.1230
- ___block_literal_global.1243
- ___block_literal_global.1245
- ___block_literal_global.1249
- ___block_literal_global.1257
- ___block_literal_global.126
- ___block_literal_global.1261
- ___block_literal_global.13041
- ___block_literal_global.133
- ___block_literal_global.13405
- ___block_literal_global.1349
- ___block_literal_global.14328
- ___block_literal_global.14474
- ___block_literal_global.155.8228
- ___block_literal_global.1552
- ___block_literal_global.1763
- ___block_literal_global.1977
- ___block_literal_global.2355
- ___block_literal_global.248
- ___block_literal_global.257.8169
- ___block_literal_global.264.10822
- ___block_literal_global.268.8163
- ___block_literal_global.271
- ___block_literal_global.274.8164
- ___block_literal_global.2840
- ___block_literal_global.29.8274
- ___block_literal_global.3013
- ___block_literal_global.33.8275
- ___block_literal_global.3404
- ___block_literal_global.342
- ___block_literal_global.3607
- ___block_literal_global.375.8082
- ___block_literal_global.41.8276
- ___block_literal_global.4557
- ___block_literal_global.458
- ___block_literal_global.47.8278
- ___block_literal_global.4855
- ___block_literal_global.5.11604
- ___block_literal_global.5065
- ___block_literal_global.52.8280
- ___block_literal_global.539
- ___block_literal_global.5743
- ___block_literal_global.58.8281
- ___block_literal_global.609
- ___block_literal_global.636
- ___block_literal_global.6504
- ___block_literal_global.6949
- ___block_literal_global.7232
- ___block_literal_global.7442
- ___block_literal_global.751
- ___block_literal_global.767
- ___block_literal_global.7908
- ___block_literal_global.8273
- ___block_literal_global.8575
- ___block_literal_global.9174
- ___block_literal_global.9405
- ___block_literal_global.9550
- ___block_literal_global.9797
- ___logger_block_invoke.12243
- ___logger_block_invoke.14332
- ___logger_block_invoke.4816
- ___logger_block_invoke.5069
- ___logger_block_invoke.7446
- ___logger_block_invoke.8159
- __btServiceEventHandler.2064
- __btSessionEventCallback.2096
- _classACAccountStore.8134
- _classAKAccountManager.8123
- _classAVAudioSession.9387
- _classCALayer.13075
- _classCATransaction.13092
- _classCBCentralManager.1393
- _classCBCentralManager.2109
- _classCBPeripheralManager.1554
- _classCBPeripheralManager.2101
- _classHAPSystemKeychainStore.5726
- _classWiFiAwareInternetSharingConfiguration.4883
- _constantValCBManagerIsPrivilegedDaemonKey.1374
- _constantValCBManagerNeedsRestrictedStateOperation.1388
- _gCFArrayType.12165
- _gCFBooleanType.12166
- _gCFDataType.12167
- _gCFDateType.12168
- _gCFDictionaryType.12169
- _gCFNumberType.12164
- _gCFStringType.12170
- _getACAccountStoreClass.8130
- _getAKAccountManagerClass.8113
- _getAVAudioSessionClass.9373
- _getCALayerClass.13056
- _getCATransactionClass.13082
- _getCBCentralManagerClass.2070
- _getCBManagerIsPrivilegedDaemonKey.1371
- _getCBPeripheralManagerClass.1546
- _getCBPeripheralManagerClass.2072
- _getHAPSystemKeychainStoreClass.5722
- _getWiFiAwareInternetSharingConfigurationClass.4865
- _initACAccountStore.8132
- _initAKAccountManager.8121
- _initAVAudioSession.9384
- _initAnalyticsSendEvent.8592
- _initAudioObjectGetPropertyData.607
- _initAudioUnitGetParameter.633
- _initAudioUnitSetParameter.625
- _initBTDeviceFromAddress.2034
- _initBTDeviceFromIdentifier.2036
- _initBTDeviceGetAddressString.2009
- _initBTDeviceGetConnectedServices.1967
- _initBTServiceAddCallbacks.2093
- _initBTServiceRemoveCallbacks.2067
- _initBTSessionAttachWithQueue.2095
- _initBTSessionDetachWithQueue.2063
- _initCALayer.13073
- _initCATransaction.13090
- _initCBCentralManager.1392
- _initCBCentralManager.2108
- _initCBPeripheralManager.1550
- _initCBPeripheralManager.2099
- _initCGColorSpaceCreateDeviceRGB.359
- _initCGImageDestinationAddImage.383
- _initCGImageDestinationFinalize.375
- _initHAPSystemKeychainStore.5724
- _initIOSurfaceGetBaseAddress.405
- _initIOSurfaceLock.408
- _initIOSurfaceUnlock.397
- _initValCBManagerIsPrivilegedDaemonKey.1373
- _initWiFiAwareInternetSharingConfiguration.4882
- _logger.12235
- _logger.14252
- _logger.4812
- _logger.5062
- _logger.7439
- _logger.8154
- _objc_msgSend$_wifiAutoJoinNotification:
- _objc_msgSend$pairingIdentityWithPrivateKey:completionHandler:
- _sCUOSLogCreateOnce_logger.12238
- _sCUOSLogCreateOnce_logger.14327
- _sCUOSLogCreateOnce_logger.4813
- _sCUOSLogCreateOnce_logger.5064
- _sCUOSLogCreateOnce_logger.7441
- _sCUOSLogCreateOnce_logger.8156
- _sCUOSLogHandle_logger.12240
- _sCUOSLogHandle_logger.14329
- _sCUOSLogHandle_logger.4814
- _sCUOSLogHandle_logger.5066
- _sCUOSLogHandle_logger.7443
- _sCUOSLogHandle_logger.8157
- _softLinkAnalyticsSendEvent.8587
- _softLinkAudioObjectGetPropertyData.605
- _softLinkAudioUnitGetParameter.621
- _softLinkAudioUnitSetParameter.623
- _softLinkBTDeviceFromAddress.2031
- _softLinkBTDeviceFromIdentifier.2028
- _softLinkBTDeviceGetAddressString.1978
- _softLinkBTDeviceGetConnectedServices.1951
- _softLinkBTServiceAddCallbacks.2078
- _softLinkBTServiceRemoveCallbacks.2057
- _softLinkBTSessionAttachWithQueue.2075
- _softLinkBTSessionDetachWithQueue.2060
- _softLinkCGColorSpaceCreateDeviceRGB.357
- _softLinkCGImageDestinationAddImage.372
- _softLinkCGImageDestinationFinalize.373
- _softLinkIOSurfaceGetBaseAddress.390
- _softLinkIOSurfaceLock.389
- _softLinkIOSurfaceUnlock.391
CStrings:
+ "### PairSetup SPAKE2 get M1 SharePData failed: %d"
+ "### PairSetup SPAKE2 get M2 ConfirmVData failed: %d"
+ "### PairSetup SPAKE2 get M2 ShareVData failed: %d"
+ "### PairSetup SPAKE2 get M3 failed: %d"
+ "### PairSetup client M2 bad status: 0x%X, %#m\n"
+ "### PairSetup client M4 bad status: 0x%X, %#m\n"
+ "### PairSetup client M6 bad status: 0x%X, %#m\n"
+ "### PairSetup client SPAKE2 add M1 SharePData TLV failed: %d"
+ "### PairSetup client SPAKE2 add M3 ConfirmPData TLV failed: %d"
+ "### PairSetup client SPAKE2 finish failed: %@"
+ "### PairSetup client SPAKE2 generate M1 failed: %@"
+ "### PairSetup client SPAKE2 generate M3 failed: %@"
+ "### PairSetup client SPAKE2 malloc secret failed"
+ "### PairSetup client SPAKE2 start failed: no password"
+ "### PairSetup client SPAKE2 verify failed: no prover"
+ "### PairSetup client bad state: %d\n"
+ "### PairSetup client state %d failed: %#m\n%?{end}%1{tlv8}\n"
+ "### PairSetup client wrong setup code"
+ "### PairSetup client: server not allowed: %#m\n"
+ "### PairSetup server SPAKE2 add M2 ConfirmVData TLV failed: %d"
+ "### PairSetup server SPAKE2 add M2 RetryDelay TLV failed: %d"
+ "### PairSetup server SPAKE2 add M2 ShareVData TLV failed: %d"
+ "### PairSetup server SPAKE2 finish failed: %@"
+ "### PairSetup server SPAKE2 generate M2 failed: %@"
+ "### PairSetup server SPAKE2 malloc secret failed"
+ "### PairSetup server SPAKE2 start failed: no password"
+ "### PairSetup server SPAKE2 verify failed: %@"
+ "### PairSetup server SPAKE2 verify failed: no verifier"
+ "### PairSetup server bad signature: %#m\n"
+ "### PairSetup server bad state: %d\n"
+ "### PairSetup server disabled after too many attempts\n"
+ "### PairSetup server save peer failed: %#m\n"
+ "### PairSetup server state %d failed: %#m\n%?{end}%1{tlv8}\n"
+ "### PairSetup server unsupported method: %u\n"
+ "### PairSetup server wrong setup code"
+ "### PairSetup server: client not allowed: %#m\n"
+ "### PairVerify client -- server lacks ACL: %@\n"
+ "### PairVerify client M2 failed: find peer failed, %#m\n"
+ "### PairVerify client M2 failed: get PK, %#m\n"
+ "### PairVerify client M2 failed: get encrypted data, %#m\n"
+ "### PairVerify client M2 failed: get identifier failed, %#m\n"
+ "### PairVerify client M2 failed: get signature failed, %#m\n"
+ "### PairVerify client M2 verify signature failed: %#m\n"
+ "### PairVerify client M3 sign failed: %#m\n"
+ "### PairVerify client M4 bad status: 0x%X, %#m\n"
+ "### PairVerify client bad state: %d\n"
+ "### PairVerify client state %d failed: %#m\n%?{end}%1{tlv8}\n"
+ "### PairVerify server -- client lacks ACL: %@\n"
+ "### PairVerify server M2 failed: copy identity, %#m\n"
+ "### PairVerify server M2 sign failed: %#m\n"
+ "### PairVerify server M3 bad status: 0x%X, %#m\n"
+ "### PairVerify server M3 verify signature failed: %#m\n"
+ "### PairVerify server M5 requested ACL not allowed: %#m, %@\n"
+ "### PairVerify server bad auth tag\n"
+ "### PairVerify server bad signature: %#m\n"
+ "### PairVerify server bad state: %d\n"
+ "### PairVerify server state %d failed: %#m\n%?{end}%1{tlv8}\n"
+ "### PairVerify server unknown peer: %.*s\n"
+ "### PairVerify server unsupported method: %u\n"
+ "+[CUPairingManager copySystemPairingIdentifierWithFlags:error:]"
+ "-[CUWiFiManager _wifiHandleEvent:]"
+ "-[CUWiFiManager _wifiJoinNotification:status:reason:]"
+ "/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi"
+ "@\"CWFInterface\""
+ "@\"WiFiAwarePublishDatapathServiceSpecificInfo\""
+ "AWDLTrafficRegistrationServiceMacVirtualDisplay"
+ "AutoJoin"
+ "BonjourDevice_GetDNSName failed: %#m"
+ "CWFInterface"
+ "Create path string failed"
+ "MacVirtualDisplay"
+ "No UTF8 path"
+ "OSStatus BonjourDevice_GetDNSName(CFDictionaryRef, uint64_t, char *, size_t)"
+ "OSStatus _SetupClientAuthenticationFailed(PairingSessionRef, const uint8_t *, const uint8_t *const)"
+ "OSStatus _SetupClientSPAKE2Start(PairingSessionRef, TLV8Buffer *)"
+ "OSStatus _SetupClientSPAKE2Verify(PairingSessionRef, const uint8_t *, const uint8_t *const, TLV8Buffer *)"
+ "OSStatus _SetupServerAuthenticationFailed(PairingSessionRef, uint8_t, TLV8Buffer *, uint8_t **, size_t *)"
+ "OSStatus _SetupServerSPAKE2Start(PairingSessionRef, const uint8_t *, const uint8_t *const, TLV8Buffer *)"
+ "OSStatus _SetupServerSPAKE2Verify(PairingSessionRef, const uint8_t *, const uint8_t *const)"
+ "Pair-resume client M2 for ID %llu failed %#m...doing PairVerify\n"
+ "Pair-resume server M1 for ID %llu failed %#m...doing PairVerify\n"
+ "PairSetup  client M3 -- verify request\n%?{end}%1{tlv8}\n"
+ "PairSetup client M1 -- start request\n%?{end}%1{tlv8}\n"
+ "PairSetup client M2 -- start response\n%?{end}%1{tlv8}\n"
+ "PairSetup client M4 -- verify response\n%?{end}%1{tlv8}\n"
+ "PairSetup client M5 -- exchange request\n%?{end}%1{tlv8}\n"
+ "PairSetup client M6 -- exchange response\n%?{end}%1{tlv8}\n"
+ "PairSetup client SPAKE2 start"
+ "PairSetup client done -- server authenticated\n"
+ "PairSetup server M1 -- start request\n%?{end}%1{tlv8}\n"
+ "PairSetup server M2 -- start response\n%?{end}%1{tlv8}\n"
+ "PairSetup server M3 -- verify request\n%?{end}%1{tlv8}\n"
+ "PairSetup server M4 -- verify response\n%?{end}%1{tlv8}\n"
+ "PairSetup server M5 -- exchange request\n%?{end}%1{tlv8}\n"
+ "PairSetup server M6 -- exchange response\n%?{end}%1{tlv8}\n"
+ "PairSetup server SPAKE2 start"
+ "PairSetup server done -- client authenticated\n"
+ "PairSetup server throttling for %d second(s)\n"
+ "PairSetup transient client done -- server authenticated\n"
+ "PairSetup transient server done -- client authenticated\n"
+ "PairVerify client M1 -- start request\n%?{end}%1{tlv8}\n"
+ "PairVerify client M2 -- start response\n%?{end}%1{tlv8}\n"
+ "PairVerify client M3 -- finish request\n%?{end}%1{tlv8}\n"
+ "PairVerify client M4 -- finish response\n%?{end}%1{tlv8}\n"
+ "PairVerify client done\n"
+ "PairVerify server M1 -- start request\n%?{end}%1{tlv8}\n"
+ "PairVerify server M2 -- start response\n%?{end}%1{tlv8}\n"
+ "PairVerify server M3 -- finish request\n%?{end}%1{tlv8}\n"
+ "PairVerify server M4 -- finish response\n%?{end}%1{tlv8}\n"
+ "PairVerify server done\n"
+ "T@\"NSObject<OS_dispatch_queue>\",&,V_dispatchQueue"
+ "T@\"WiFiAwarePublishDatapathServiceSpecificInfo\",&,N,V_wfaServiceSpecificInfo"
+ "T@?,C,V_invalidationHandler"
+ "Tq,N,V_wfaConnectionMode"
+ "Tq,N,V_wfaDiscoveryMode"
+ "UserJoin"
+ "WiFi Join notification: status=%@, state=%s, flags=%@, reason=%@"
+ "WiFi event:type=%ld"
+ "WiFi state changed: %s -> %s, flags=%@"
+ "WiFi state unchanged: %s, flags=%@"
+ "_getLengthWithCompletionHandler:"
+ "_wfaConnectionMode"
+ "_wfaDiscoveryMode"
+ "_wfaServiceSpecificInfo"
+ "_wifiHandleEvent:"
+ "_wifiInterface"
+ "_wifiJoinNotification:status:reason:"
+ "accessory:didUpdateHH1EOLEnabled:"
+ "copySystemPairingIdentifierWithFlags:error:"
+ "getLengthWithCompletionHandler:"
+ "pairingIdentityWithPrivateKey:attemptToReadFromKeychain:completionHandler:"
+ "realPath:dispatchQueue:completionHandler:"
+ "realPath:error:"
+ "realpath failed"
+ "setTargetQueue:"
+ "setWfaConnectionMode:"
+ "setWfaDiscoveryMode:"
+ "setWfaServiceSpecificInfo:"
+ "startMonitoringEventType:error:"
+ "stat failed"
+ "v16@?0@\"CWFEvent\"8"
+ "v40@0:8^{__WiFiNetwork=}16@24@32"
+ "wfaConnectionMode"
+ "wfaDiscoveryMode"
+ "wfaServiceSpecificInfo"
+ "\xe1"
- "### Pair-setup client M2 bad status: 0x%X, %#m\n"
- "### Pair-setup client M4 bad status: 0x%X, %#m\n"
- "### Pair-setup client M6 bad status: 0x%X, %#m\n"
- "### Pair-setup client bad state: %d\n"
- "### Pair-setup client state %d failed: %#m\n%?{end}%1{tlv8}\n"
- "### Pair-setup client wrong setup code\n"
- "### Pair-setup client: server not allowed: %#m\n"
- "### Pair-setup server bad signature: %#m\n"
- "### Pair-setup server bad state: %d\n"
- "### Pair-setup server disabled after too many attempts\n"
- "### Pair-setup server save peer failed: %#m\n"
- "### Pair-setup server state %d failed: %#m\n%?{end}%1{tlv8}\n"
- "### Pair-setup server unsupported method: %u\n"
- "### Pair-setup server wrong setup code\n"
- "### Pair-setup server: client not allowed: %#m\n"
- "### Pair-verify client -- server lacks ACL: %@\n"
- "### Pair-verify client M2 failed: find peer failed, %#m\n"
- "### Pair-verify client M2 failed: get PK, %#m\n"
- "### Pair-verify client M2 failed: get encrypted data, %#m\n"
- "### Pair-verify client M2 failed: get identifier failed, %#m\n"
- "### Pair-verify client M2 failed: get signature failed, %#m\n"
- "### Pair-verify client M2 verify signature failed: %#m\n"
- "### Pair-verify client M3 sign failed: %#m\n"
- "### Pair-verify client M4 bad status: 0x%X, %#m\n"
- "### Pair-verify client bad state: %d\n"
- "### Pair-verify client state %d failed: %#m\n%?{end}%1{tlv8}\n"
- "### Pair-verify server -- client lacks ACL: %@\n"
- "### Pair-verify server M2 failed: copy identity, %#m\n"
- "### Pair-verify server M2 sign failed: %#m\n"
- "### Pair-verify server M3 bad status: 0x%X, %#m\n"
- "### Pair-verify server M3 verify signature failed: %#m\n"
- "### Pair-verify server M5 requested ACL not allowed: %#m, %@\n"
- "### Pair-verify server bad auth tag\n"
- "### Pair-verify server bad signature: %#m\n"
- "### Pair-verify server bad state: %d\n"
- "### Pair-verify server state %d failed: %#m\n%?{end}%1{tlv8}\n"
- "### Pair-verify server unknown peer: %.*s\n"
- "### Pair-verify server unsupported method: %u\n"
- "+[CUPairingManager copySystemPairingIdentifierAndReturnError:]"
- "-[CUWiFiManager _wifiAutoJoinNotification:]"
- "No HomeKit Self Accessory Identity SPI"
- "Pair-resume client M2 for ID %llu failed %#m...doing pair-verify\n"
- "Pair-resume server M1 for ID %llu failed %#m...doing pair-verify\n"
- "Pair-setup  client M3 -- verify request\n%?{end}%1{tlv8}\n"
- "Pair-setup client M1 -- start request\n%?{end}%1{tlv8}\n"
- "Pair-setup client M2 -- start response\n%?{end}%1{tlv8}\n"
- "Pair-setup client M4 -- verify response\n%?{end}%1{tlv8}\n"
- "Pair-setup client M5 -- exchange request\n%?{end}%1{tlv8}\n"
- "Pair-setup client M6 -- exchange response\n%?{end}%1{tlv8}\n"
- "Pair-setup client done -- server authenticated\n"
- "Pair-setup server M1 -- start request\n%?{end}%1{tlv8}\n"
- "Pair-setup server M2 -- start response\n%?{end}%1{tlv8}\n"
- "Pair-setup server M3 -- verify request\n%?{end}%1{tlv8}\n"
- "Pair-setup server M4 -- verify response\n%?{end}%1{tlv8}\n"
- "Pair-setup server M5 -- exchange request\n%?{end}%1{tlv8}\n"
- "Pair-setup server M6 -- exchange response\n%?{end}%1{tlv8}\n"
- "Pair-setup server done -- client authenticated\n"
- "Pair-setup server throttling for %d second(s)\n"
- "Pair-setup transient client done -- server authenticated\n"
- "Pair-setup transient server done -- client authenticated\n"
- "Pair-verify client M1 -- start request\n%?{end}%1{tlv8}\n"
- "Pair-verify client M2 -- start response\n%?{end}%1{tlv8}\n"
- "Pair-verify client M3 -- finish request\n%?{end}%1{tlv8}\n"
- "Pair-verify client M4 -- finish response\n%?{end}%1{tlv8}\n"
- "Pair-verify client done\n"
- "Pair-verify server M1 -- start request\n%?{end}%1{tlv8}\n"
- "Pair-verify server M2 -- start response\n%?{end}%1{tlv8}\n"
- "Pair-verify server M3 -- finish request\n%?{end}%1{tlv8}\n"
- "Pair-verify server M4 -- finish response\n%?{end}%1{tlv8}\n"
- "Pair-verify server done\n"
- "WiFi AutoJoin notification: %@, %s, %#{flags}\n"
- "WiFi state changed: %s -> %s, %#{flags} %?''@\n"
- "WiFi state changed: %s, %#{flags}\n"
- "_wifiAutoJoinNotification:"
- "pairingIdentityWithPrivateKey:completionHandler:"
- "\xd1"

```
