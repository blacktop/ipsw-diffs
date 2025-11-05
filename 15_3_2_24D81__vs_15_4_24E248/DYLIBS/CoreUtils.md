## CoreUtils

> `/System/Library/PrivateFrameworks/CoreUtils.framework/Versions/A/CoreUtils`

```diff

-760.36.2.0.0
-  __TEXT.__text: 0x1163e0
-  __TEXT.__auth_stubs: 0x2970
-  __TEXT.__objc_methlist: 0x8378
-  __TEXT.__const: 0x2188
-  __TEXT.__gcc_except_tab: 0x1af0
-  __TEXT.__cstring: 0x2231c
-  __TEXT.__oslogstring: 0x35b
-  __TEXT.__unwind_info: 0x3890
+770.26.0.0.0
+  __TEXT.__text: 0x118094
+  __TEXT.__auth_stubs: 0x29f0
+  __TEXT.__objc_methlist: 0x9988
+  __TEXT.__cstring: 0x2237d
+  __TEXT.__const: 0x2310
+  __TEXT.__gcc_except_tab: 0x1c44
+  __TEXT.__oslogstring: 0x620
+  __TEXT.__unwind_info: 0x3830
   __TEXT.__eh_frame: 0x50
-  __TEXT.__objc_classname: 0xbf9
-  __TEXT.__objc_methname: 0x15727
-  __TEXT.__objc_methtype: 0x422e
-  __TEXT.__objc_stubs: 0x9f40
-  __DATA_CONST.__got: 0x618
-  __DATA_CONST.__const: 0x1428
-  __DATA_CONST.__objc_classlist: 0x300
+  __TEXT.__objc_classname: 0xbf2
+  __TEXT.__objc_methname: 0x158b1
+  __TEXT.__objc_methtype: 0x4314
+  __TEXT.__objc_stubs: 0xa080
+  __DATA_CONST.__got: 0x610
+  __DATA_CONST.__const: 0x1470
+  __DATA_CONST.__objc_classlist: 0x308
   __DATA_CONST.__objc_catlist: 0x48
-  __DATA_CONST.__objc_protolist: 0x150
+  __DATA_CONST.__objc_protolist: 0x140
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4200
+  __DATA_CONST.__objc_selrefs: 0x4c70
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x208
-  __AUTH_CONST.__auth_got: 0x14c8
-  __AUTH_CONST.__const: 0x3840
-  __AUTH_CONST.__cfstring: 0x3ea0
-  __AUTH_CONST.__objc_const: 0x158f8
+  __AUTH_CONST.__auth_got: 0x1508
+  __AUTH_CONST.__const: 0x3870
+  __AUTH_CONST.__cfstring: 0x3f20
+  __AUTH_CONST.__objc_const: 0x12f48
   __AUTH_CONST.__objc_intobj: 0x168
-  __AUTH.__objc_data: 0x1e0
+  __AUTH.__objc_data: 0x280
   __AUTH.__data: 0x1e0
   __DATA.__objc_ivar: 0x1484
-  __DATA.__data: 0x32f0
-  __DATA.__bss: 0xf40
+  __DATA.__data: 0x31c0
+  __DATA.__bss: 0xf30
   __DATA.__common: 0x2a
-  __DATA_DIRTY.__objc_data: 0x1c20
-  __DATA_DIRTY.__data: 0xa58
+  __DATA_DIRTY.__objc_data: 0x1bd0
+  __DATA_DIRTY.__data: 0xa38
   __DATA_DIRTY.__bss: 0x228
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: F4778D3D-6AF1-315F-A741-8C963B1307EF
-  Functions: 5666
-  Symbols:   11380
-  CStrings:  9821
+  UUID: AE3F561F-B576-3365-BBE4-63160741009A
+  Functions: 5612
+  Symbols:   11426
+  CStrings:  9861
 
Symbols:
+ -[CUNANDataSession setWfaPairingDelegate:]
+ -[CUNANDataSession wfaPairingDelegate]
+ -[CUSerialPort .cxx_destruct]
+ -[CUSerialPort _cleanup]
+ -[CUSerialPort _ensureSetUpAndReturnError:]
+ -[CUSerialPort _readLineWithFlags:completionHandler:]
+ -[CUSerialPort _writeLine:completionHandler:]
+ -[CUSerialPort dealloc]
+ -[CUSerialPort initWithConfiguration:dispatchQueue:]
+ -[CUSerialPort invalidate]
+ -[CUSerialPort readLineWithFlags:completionHandler:]
+ -[CUSerialPort writeLine:completionHandler:]
+ -[CUSerialPortConfiguration .cxx_destruct]
+ -[CUSerialPortConfiguration baudRate]
+ -[CUSerialPortConfiguration devicePath]
+ -[CUSerialPortConfiguration flags]
+ -[CUSerialPortConfiguration flowControl]
+ -[CUSerialPortConfiguration setBaudRate:]
+ -[CUSerialPortConfiguration setDevicePath:]
+ -[CUSerialPortConfiguration setFlags:]
+ -[CUSerialPortConfiguration setFlowControl:]
+ -[CUSystemMonitorImp _meDeviceOverride]
+ ACAccountStoreFunction.7828
+ AKAccountManagerFunction.7817
+ AccountsLibrary.sLib.7831
+ AccountsLibrary.sOnce.7825
+ AppleAccountLibrary.sLib.7834
+ AppleAccountLibrary.sOnce.7821
+ AudioUnitLibrary.sLib.561
+ AudioUnitLibrary.sOnce.560
+ AuthKitLibrary.sLib.7820
+ AuthKitLibrary.sOnce.7814
+ CALayerFunction.12585
+ CATransactionFunction.12602
+ CBCentralManagerFunction.1315
+ CBCentralManagerFunction.1890
+ CBManagerIsPrivilegedDaemonKeyFunction.1295
+ CBManagerNeedsRestrictedStateOperationFunction.1310
+ CBPeripheralManagerFunction.1473
+ CBPeripheralManagerFunction.1882
+ CWWiFiClientFunction.13806
+ CoreAnalyticsLibrary.sLib.8272
+ CoreAnalyticsLibrary.sOnce.8270
+ CoreAudioLibrary.sLib.544
+ CoreAudioLibrary.sOnce.542
+ CoreBluetoothLibrary.sLib.1108
+ CoreBluetoothLibrary.sLib.1273
+ CoreBluetoothLibrary.sLib.1478
+ CoreBluetoothLibrary.sLib.1885
+ CoreBluetoothLibrary.sOnce.1106
+ CoreBluetoothLibrary.sOnce.1271
+ CoreBluetoothLibrary.sOnce.1468
+ CoreBluetoothLibrary.sOnce.1879
+ CoreHAPLibrary.sLib.5589
+ CoreHAPLibrary.sOnce.5582
+ CoreServicesLibrary.sLib.13014
+ CoreServicesLibrary.sLib.751
+ CoreServicesLibrary.sLib.7919
+ CoreServicesLibrary.sOnce.13013
+ CoreServicesLibrary.sOnce.750
+ CoreServicesLibrary.sOnce.7918
+ CoreWLANLibrary.sLib.13811
+ CoreWLANLibrary.sOnce.13801
+ GCC_except_table1210
+ GCC_except_table1291
+ GCC_except_table1297
+ GCC_except_table1298
+ GCC_except_table1301
+ GCC_except_table1374
+ GCC_except_table1406
+ GCC_except_table1409
+ GCC_except_table1415
+ GCC_except_table1420
+ GCC_except_table1423
+ GCC_except_table1474
+ GCC_except_table1475
+ GCC_except_table1512
+ GCC_except_table1542
+ GCC_except_table1565
+ GCC_except_table1572
+ GCC_except_table1584
+ GCC_except_table1586
+ GCC_except_table1598
+ GCC_except_table2085
+ GCC_except_table2125
+ GCC_except_table2155
+ GCC_except_table2280
+ GCC_except_table2281
+ GCC_except_table2300
+ GCC_except_table2332
+ GCC_except_table2404
+ GCC_except_table2429
+ GCC_except_table2463
+ GCC_except_table2467
+ GCC_except_table2530
+ GCC_except_table2531
+ GCC_except_table2533
+ GCC_except_table2534
+ GCC_except_table2536
+ GCC_except_table2547
+ GCC_except_table2550
+ GCC_except_table2560
+ GCC_except_table2562
+ GCC_except_table2630
+ GCC_except_table2945
+ GCC_except_table2946
+ GCC_except_table3005
+ GCC_except_table3076
+ GCC_except_table3080
+ GCC_except_table3124
+ GCC_except_table3127
+ GCC_except_table3128
+ GCC_except_table3130
+ GCC_except_table3404
+ GCC_except_table3832
+ GCC_except_table4099
+ GCC_except_table4107
+ GCC_except_table4115
+ GCC_except_table4271
+ GCC_except_table4273
+ GCC_except_table4275
+ GCC_except_table4298
+ GCC_except_table4382
+ GCC_except_table4383
+ GCC_except_table4384
+ GCC_except_table4389
+ GCC_except_table4391
+ GCC_except_table4393
+ GCC_except_table4397
+ GCC_except_table4421
+ GCC_except_table4423
+ GCC_except_table4424
+ GCC_except_table4425
+ GCC_except_table4427
+ GCC_except_table4428
+ GCC_except_table4431
+ GCC_except_table4432
+ GCC_except_table4442
+ GCC_except_table4456
+ GCC_except_table4460
+ GCC_except_table4462
+ GCC_except_table4463
+ GCC_except_table4464
+ GCC_except_table4465
+ GCC_except_table4466
+ GCC_except_table4467
+ GCC_except_table4468
+ GCC_except_table4470
+ GCC_except_table4471
+ GCC_except_table4472
+ GCC_except_table4474
+ GCC_except_table5032
+ GCC_except_table5037
+ GCC_except_table5041
+ GCC_except_table5107
+ GCC_except_table5117
+ GCC_except_table5126
+ GCC_except_table5134
+ GCC_except_table5456
+ GCC_except_table5457
+ GCC_except_table5470
+ GCC_except_table686
+ GCC_except_table771
+ GCC_except_table787
+ GCC_except_table790
+ GCC_except_table973
+ HAPSystemKeychainStoreFunction.5585
+ IOBluetoothDeviceFunction.1839
+ IOBluetoothLibrary.sLib.12937
+ IOBluetoothLibrary.sLib.1842
+ IOBluetoothLibrary.sOnce.12932
+ IOBluetoothLibrary.sOnce.1836
+ MobileDeviceLibrary.sLib.4160
+ MobileDeviceLibrary.sOnce.4158
+ OBJC_IVAR_$_CUNANDataSession._wfaPairingDelegate
+ OBJC_IVAR_$_CUSerialPort._configuration
+ OBJC_IVAR_$_CUSerialPort._dispatchQueue
+ OBJC_IVAR_$_CUSerialPort._serialStream
+ OBJC_IVAR_$_CUSerialPortConfiguration._baudRate
+ OBJC_IVAR_$_CUSerialPortConfiguration._devicePath
+ OBJC_IVAR_$_CUSerialPortConfiguration._flags
+ OBJC_IVAR_$_CUSerialPortConfiguration._flowControl
+ OBJC_IVAR_$_CUSystemMonitorImp._meDeviceOverride
+ QuartzCoreLibrary.sLib.12552
+ QuartzCoreLibrary.sOnce.12550
+ RapportLibrary.sLib.5605
+ RapportLibrary.sOnce.5600
+ WiFiAwareInternetSharingConfigurationFunction.4749
+ WiFiPeerToPeerLibrary.sLib.4710
+ WiFiPeerToPeerLibrary.sLib.5009
+ WiFiPeerToPeerLibrary.sLib.9529
+ WiFiPeerToPeerLibrary.sOnce.4705
+ WiFiPeerToPeerLibrary.sOnce.5002
+ WiFiPeerToPeerLibrary.sOnce.9528
+ _AES_CBCFrame_Update2
+ _AES_ECB_Final
+ _AES_ECB_Init
+ _AES_ECB_Update
+ _Base64DecodedSize
+ _Base64EncodeLinesEx
+ _Base64EncodedLinesMaxSize
+ _CFPreferencesCopyValue
+ _CUEnterSandbox
+ _CUNumericSuffixRemoved
+ _DMAPContentBlock_AddCodeInfo
+ _DMAPContentBlock_AddInt16
+ _DMAPContentBlock_AddUTF8
+ _DataBuffer_AppendAppleGeneralIE
+ _DataBuffer_AppendVendorIE
+ _HTTPMessageSetClientMessageType
+ _IECopyCoalescedVendorSpecific
+ _IPCAgent_Perform
+ _IPCAgent_SetMessageHandler
+ _IPCAgent_Start
+ _NetTransportFinalize.11415
+ _NetTransportFinalize.11423
+ _NetTransportInitialize.11416
+ _NetTransportInitialize.11426
+ _NetTransportRead.11412
+ _NetTransportRead.11425
+ _NetTransportWriteV.11411
+ _NetTransportWriteV.11424
+ _OBJC_CLASS_$_CUSerialPort
+ _OBJC_CLASS_$_CUSerialPortConfiguration
+ _OBJC_CLASS_$_NSRegularExpression
+ _OBJC_METACLASS_$_CUSerialPort
+ _OBJC_METACLASS_$_CUSerialPortConfiguration
+ _SDPFindMediaSectionEx
+ _SDPScanFAttribute
+ _TextToNumVersion
+ __43-[CUSystemMonitorImp _meDeviceMonitorStart]_block_invoke.252
+ __43-[CUSystemMonitorImp _meDeviceMonitorStart]_block_invoke.257
+ __43-[CUSystemMonitorImp _meDeviceMonitorStart]_block_invoke_2.260
+ __43-[CUSystemMonitorImp _systemUIMonitorStart]_block_invoke.575
+ __47-[CUSystemMonitorImp _netInterfaceMonitorStart]_block_invoke.303
+ __47-[CUSystemMonitorImp _netInterfaceMonitorStart]_block_invoke.308
+ __47-[CUSystemMonitorImp _netInterfaceMonitorStart]_block_invoke.315
+ __47-[CUSystemMonitorImp _netInterfaceMonitorStart]_block_invoke.322
+ __47-[CUSystemMonitorImp _netInterfaceMonitorStart]_block_invoke_2.311
+ __47-[CUSystemMonitorImp _netInterfaceMonitorStart]_block_invoke_2.318
+ __47-[CUSystemMonitorImp _netInterfaceMonitorStart]_block_invoke_2.325
+ __47-[CUSystemMonitorImp _netInterfaceMonitorStart]_block_invoke_3.314
+ __47-[CUSystemMonitorImp _netInterfaceMonitorStart]_block_invoke_3.321
+ __47-[CUSystemMonitorImp _netInterfaceMonitorStart]_block_invoke_3.328
+ __AccountsLibrary_block_invoke.7830
+ __AppleAccountLibrary_block_invoke.7833
+ __AudioUnitLibrary_block_invoke.564
+ __AuthKitLibrary_block_invoke.7819
+ __Block_byref_object_copy_.10057
+ __Block_byref_object_copy_.10562
+ __Block_byref_object_copy_.11974
+ __Block_byref_object_copy_.1891
+ __Block_byref_object_copy_.2484
+ __Block_byref_object_copy_.2738
+ __Block_byref_object_copy_.4019
+ __Block_byref_object_copy_.4125
+ __Block_byref_object_copy_.4711
+ __Block_byref_object_copy_.5030
+ __Block_byref_object_copy_.5539
+ __Block_byref_object_copy_.5868
+ __Block_byref_object_copy_.8618
+ __Block_byref_object_dispose_.10058
+ __Block_byref_object_dispose_.10563
+ __Block_byref_object_dispose_.11975
+ __Block_byref_object_dispose_.1892
+ __Block_byref_object_dispose_.2485
+ __Block_byref_object_dispose_.2739
+ __Block_byref_object_dispose_.4020
+ __Block_byref_object_dispose_.4126
+ __Block_byref_object_dispose_.4712
+ __Block_byref_object_dispose_.5031
+ __Block_byref_object_dispose_.5540
+ __Block_byref_object_dispose_.5869
+ __Block_byref_object_dispose_.8619
+ __CUEnterSandbox_block_invoke.4
+ __CUEnterSandbox_block_invoke.6
+ __CoreAnalyticsLibrary_block_invoke.8305
+ __CoreAudioLibrary_block_invoke.549
+ __CoreBluetoothLibrary_block_invoke.1111
+ __CoreBluetoothLibrary_block_invoke.1276
+ __CoreBluetoothLibrary_block_invoke.1476
+ __CoreBluetoothLibrary_block_invoke.1884
+ __CoreHAPLibrary_block_invoke.5587
+ __CoreServicesLibrary_block_invoke.13017
+ __CoreServicesLibrary_block_invoke.754
+ __CoreServicesLibrary_block_invoke.7922
+ __CoreWLANLibrary_block_invoke.13809
+ __IOBluetoothLibrary_block_invoke.12935
+ __IOBluetoothLibrary_block_invoke.1841
+ __MobileDeviceLibrary_block_invoke.4164
+ __OBJC_$_INSTANCE_METHODS_CUSerialPort
+ __OBJC_$_INSTANCE_METHODS_CUSerialPortConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_CUSerialPort
+ __OBJC_$_INSTANCE_VARIABLES_CUSerialPortConfiguration
+ __OBJC_$_PROP_LIST_CUSerialPortConfiguration
+ __OBJC_CLASS_RO_$_CUSerialPort
+ __OBJC_CLASS_RO_$_CUSerialPortConfiguration
+ __OBJC_METACLASS_RO_$_CUSerialPort
+ __OBJC_METACLASS_RO_$_CUSerialPortConfiguration
+ __QuartzCoreLibrary_block_invoke.12556
+ __RapportLibrary_block_invoke.5604
+ __WiFiPeerToPeerLibrary_block_invoke.4708
+ __WiFiPeerToPeerLibrary_block_invoke.5007
+ __WiFiPeerToPeerLibrary_block_invoke.9532
+ ___26-[CUSerialPort invalidate]_block_invoke
+ ___43-[CUSerialPort _ensureSetUpAndReturnError:]_block_invoke
+ ___44-[CUSerialPort writeLine:completionHandler:]_block_invoke
+ ___52-[CUSerialPort readLineWithFlags:completionHandler:]_block_invoke
+ ___CUEnterSandbox_block_invoke
+ ____readLineCompletion_block_invoke
+ ____writeLineCompletion_block_invoke
+ ___block_descriptor_40_e8_32r_e5_v8?0l
+ __block_descriptor_tmp.11
+ __block_descriptor_tmp.11170
+ __block_descriptor_tmp.11219
+ __block_descriptor_tmp.12
+ __block_descriptor_tmp.13913
+ __block_descriptor_tmp.24
+ __block_descriptor_tmp.330
+ __block_descriptor_tmp.42.11166
+ __block_descriptor_tmp.5
+ __block_descriptor_tmp.556
+ __block_descriptor_tmp.7.11224
+ __block_literal_global.10092
+ __block_literal_global.10143
+ __block_literal_global.11002
+ __block_literal_global.1107
+ __block_literal_global.11154
+ __block_literal_global.11229
+ __block_literal_global.11757
+ __block_literal_global.12551
+ __block_literal_global.1263
+ __block_literal_global.1270
+ __block_literal_global.1272
+ __block_literal_global.1275
+ __block_literal_global.1283
+ __block_literal_global.1294
+ __block_literal_global.1302
+ __block_literal_global.1306
+ __block_literal_global.1312
+ __block_literal_global.1318
+ __block_literal_global.1320
+ __block_literal_global.1324
+ __block_literal_global.1328
+ __block_literal_global.1332
+ __block_literal_global.1336
+ __block_literal_global.134
+ __block_literal_global.1342
+ __block_literal_global.1350
+ __block_literal_global.1358
+ __block_literal_global.136
+ __block_literal_global.13802
+ __block_literal_global.13916
+ __block_literal_global.14
+ __block_literal_global.1469
+ __block_literal_global.154
+ __block_literal_global.156
+ __block_literal_global.1627
+ __block_literal_global.166
+ __block_literal_global.174
+ __block_literal_global.176
+ __block_literal_global.1820
+ __block_literal_global.197
+ __block_literal_global.199
+ __block_literal_global.207
+ __block_literal_global.209
+ __block_literal_global.232
+ __block_literal_global.239
+ __block_literal_global.246
+ __block_literal_global.2583
+ __block_literal_global.26
+ __block_literal_global.260
+ __block_literal_global.269
+ __block_literal_global.2754
+ __block_literal_global.286
+ __block_literal_global.288
+ __block_literal_global.300
+ __block_literal_global.305
+ __block_literal_global.307
+ __block_literal_global.3081
+ __block_literal_global.310
+ __block_literal_global.313
+ __block_literal_global.317
+ __block_literal_global.320
+ __block_literal_global.324
+ __block_literal_global.327.7852
+ __block_literal_global.3281
+ __block_literal_global.330
+ __block_literal_global.332
+ __block_literal_global.334
+ __block_literal_global.336
+ __block_literal_global.34.12558
+ __block_literal_global.342
+ __block_literal_global.344
+ __block_literal_global.362
+ __block_literal_global.364
+ __block_literal_global.377
+ __block_literal_global.385.7797
+ __block_literal_global.3907
+ __block_literal_global.392
+ __block_literal_global.394
+ __block_literal_global.398
+ __block_literal_global.40.12610
+ __block_literal_global.411
+ __block_literal_global.4159
+ __block_literal_global.422
+ __block_literal_global.424
+ __block_literal_global.44.11161
+ __block_literal_global.44.7981
+ __block_literal_global.4454
+ __block_literal_global.454
+ __block_literal_global.456
+ __block_literal_global.4726
+ __block_literal_global.473
+ __block_literal_global.475
+ __block_literal_global.493
+ __block_literal_global.499
+ __block_literal_global.5003
+ __block_literal_global.501
+ __block_literal_global.505
+ __block_literal_global.507
+ __block_literal_global.515
+ __block_literal_global.517
+ __block_literal_global.543
+ __block_literal_global.5601
+ __block_literal_global.580
+ __block_literal_global.582
+ __block_literal_global.592
+ __block_literal_global.594
+ __block_literal_global.609
+ __block_literal_global.611
+ __block_literal_global.6376
+ __block_literal_global.6761
+ __block_literal_global.7166
+ __block_literal_global.7608
+ __block_literal_global.778
+ __block_literal_global.791
+ __block_literal_global.794
+ __block_literal_global.7979
+ __block_literal_global.8271
+ __block_literal_global.846
+ __block_literal_global.8866
+ __block_literal_global.9181
+ __block_literal_global.9493
+ __block_literal_global.975
+ __block_literal_global.9851
+ __logger_block_invoke.11761
+ __logger_block_invoke.7849
+ __os_log_error_impl
+ __readLineCompletion
+ __set_user_dir_suffix
+ __writeLineCompletion
+ _cchkdf
+ _ccsha256_di
+ _chacha20_init_96x32
+ _confstr
+ _getpwuid
+ _kCFPreferencesAnyApplication
+ _objc_msgSend$_ensureSetUpAndReturnError:
+ _objc_msgSend$_meDeviceOverride
+ _objc_msgSend$_readLineWithFlags:completionHandler:
+ _objc_msgSend$_writeLine:completionHandler:
+ _objc_msgSend$baudRate
+ _objc_msgSend$currentAudioAndVideoCallCount
+ _objc_msgSend$devicePath
+ _objc_msgSend$firstMatchInString:options:range:
+ _objc_msgSend$flowControl
+ _objc_msgSend$initWithPattern:options:error:
+ _objc_msgSend$numberOfRanges
+ _objc_msgSend$rangeAtIndex:
+ _objc_msgSend$setPairingDelegate:
+ _objc_msgSend$substringWithRange:
+ _objc_storeWeak
+ _sandbox_init_with_parameters
+ classACAccountStore.7826
+ classAKAccountManager.7815
+ classCALayer.12583
+ classCATransaction.12600
+ classCBCentralManager.1313
+ classCBCentralManager.1888
+ classCBPeripheralManager.1471
+ classCBPeripheralManager.1880
+ classCWWiFiClient.13804
+ classHAPSystemKeychainStore.5583
+ classIOBluetoothDevice.1837
+ classWiFiAwareInternetSharingConfiguration.4747
+ constantValCBManagerIsPrivilegedDaemonKey.1293
+ constantValCBManagerNeedsRestrictedStateOperation.1308
+ gCFArrayType.11683
+ gCFBooleanType.11684
+ gCFDataType.11685
+ gCFDateType.11686
+ gCFDictionaryType.11687
+ gCFNumberType.11682
+ gCFStringType.11688
+ getACAccountStoreClass.7822
+ getAKAccountManagerClass.7805
+ getCALayerClass.12564
+ getCATransactionClass.12590
+ getCBCentralManagerClass.1296
+ getCBCentralManagerClass.1870
+ getCBManagerIsPrivilegedDaemonKey.1290
+ getCBManagerNeedsRestrictedStateOperation.1297
+ getCBPeripheralManagerClass.1463
+ getCBPeripheralManagerClass.1872
+ getCWWiFiClientClass.13786
+ getHAPSystemKeychainStoreClass.5579
+ getIOBluetoothDeviceClass.1819
+ getWiFiAwareInternetSharingConfigurationClass.4735
+ initACAccountStore.7824
+ initAKAccountManager.7813
+ initAMDeviceConnect.4181
+ initAMDeviceCopyValue.4173
+ initAMDeviceCreateCopy.4272
+ initAMDeviceDisconnect.4157
+ initAMDeviceStartSession.4178
+ initAMDeviceStopSession.4167
+ initAnalyticsSendEvent.8286
+ initAudioObjectGetPropertyData.541
+ initAudioUnitGetParameter.567
+ initAudioUnitSetParameter.559
+ initCALayer.12581
+ initCATransaction.12598
+ initCBCentralManager.1312
+ initCBCentralManager.1887
+ initCBPeripheralManager.1467
+ initCBPeripheralManager.1878
+ initCWWiFiClient.13800
+ initHAPSystemKeychainStore.5581
+ initIOBluetoothDevice.1835
+ initIOBluetoothRegisterForNotifications.1876
+ initIOBluetoothRemoveRegistrationForNotifications.1867
+ initValCBManagerIsPrivilegedDaemonKey.1292
+ initValCBManagerNeedsRestrictedStateOperation.1307
+ initWiFiAwareInternetSharingConfiguration.4745
+ logger.11754
+ logger.7845
+ sCUOSLogCreateOnce_logger.11756
+ sCUOSLogCreateOnce_logger.7846
+ sCUOSLogHandle_logger.11758
+ sCUOSLogHandle_logger.7847
+ softLinkAMDeviceConnect.4139
+ softLinkAMDeviceCopyValue.4148
+ softLinkAMDeviceCreateCopy.4252
+ softLinkAMDeviceDisconnect.4153
+ softLinkAMDeviceStartSession.4141
+ softLinkAMDeviceStopSession.4152
+ softLinkAnalyticsSendEvent.8283
+ softLinkAudioObjectGetPropertyData.539
+ softLinkAudioUnitGetParameter.555
+ softLinkAudioUnitSetParameter.557
+ softLinkIOBluetoothRegisterForNotifications.1874
+ softLinkIOBluetoothRemoveRegistrationForNotifications.1853
- -[CULiveAction .cxx_destruct]
- -[CULiveAction activateWithCompletion:]
- -[CULiveAction alertType]
- -[CULiveAction destinationIDs]
- -[CULiveAction direct]
- -[CULiveAction dispatchQueue]
- -[CULiveAction encodeWithXPCObject:]
- -[CULiveAction initWithXPCObject:error:]
- -[CULiveAction init]
- -[CULiveAction invalidate]
- -[CULiveAction invalidationHandler]
- -[CULiveAction originatingHomeKitAccessoryID]
- -[CULiveAction setAlertType:]
- -[CULiveAction setDestinationIDs:]
- -[CULiveAction setDirect:]
- -[CULiveAction setDispatchQueue:]
- -[CULiveAction setInvalidationHandler:]
- -[CULiveAction setOriginatingHomeKitAccessoryID:]
- -[CULiveAction setSoundFileURL:]
- -[CULiveAction setSpeakText:]
- -[CULiveAction soundFileURL]
- -[CULiveAction speakText]
- -[CUSystemMonitorImp callObserver:callChanged:]
- ACAccountStoreFunction.7970
- AKAccountManagerFunction.7959
- AccountsLibrary.sLib.7973
- AccountsLibrary.sOnce.7967
- AppleAccountLibrary.sLib.7976
- AppleAccountLibrary.sOnce.7963
- AudioUnitLibrary.sLib.658
- AudioUnitLibrary.sOnce.657
- AuthKitLibrary.sLib.7962
- AuthKitLibrary.sOnce.7956
- CALayerFunction.12834
- CATransactionFunction.12851
- CBCentralManagerFunction.1402
- CBCentralManagerFunction.1976
- CBManagerIsPrivilegedDaemonKeyFunction.1382
- CBManagerNeedsRestrictedStateOperationFunction.1397
- CBPeripheralManagerFunction.1559
- CBPeripheralManagerFunction.1968
- CWWiFiClientFunction.14203
- CallKitLibrary.sLib
- CallKitLibrary.sOnce
- CoreAnalyticsLibrary.sLib.8405
- CoreAnalyticsLibrary.sOnce.8403
- CoreAudioLibrary.sLib.641
- CoreAudioLibrary.sOnce.639
- CoreBluetoothLibrary.sLib.1188
- CoreBluetoothLibrary.sLib.1353
- CoreBluetoothLibrary.sLib.1564
- CoreBluetoothLibrary.sLib.1971
- CoreBluetoothLibrary.sOnce.1186
- CoreBluetoothLibrary.sOnce.1351
- CoreBluetoothLibrary.sOnce.1554
- CoreBluetoothLibrary.sOnce.1965
- CoreHAPLibrary.sLib.5739
- CoreHAPLibrary.sOnce.5732
- CoreServicesLibrary.sLib.13407
- CoreServicesLibrary.sLib.8048
- CoreServicesLibrary.sLib.836
- CoreServicesLibrary.sOnce.13406
- CoreServicesLibrary.sOnce.8047
- CoreServicesLibrary.sOnce.835
- CoreWLANLibrary.sLib.14208
- CoreWLANLibrary.sOnce.14198
- GCC_except_table1205
- GCC_except_table1286
- GCC_except_table1292
- GCC_except_table1293
- GCC_except_table1296
- GCC_except_table1343
- GCC_except_table1344
- GCC_except_table1378
- GCC_except_table1384
- GCC_except_table1389
- GCC_except_table1392
- GCC_except_table1443
- GCC_except_table1444
- GCC_except_table1481
- GCC_except_table1511
- GCC_except_table1534
- GCC_except_table1536
- GCC_except_table1541
- GCC_except_table1553
- GCC_except_table1555
- GCC_except_table2078
- GCC_except_table2118
- GCC_except_table2148
- GCC_except_table2271
- GCC_except_table2272
- GCC_except_table2291
- GCC_except_table2323
- GCC_except_table2395
- GCC_except_table2420
- GCC_except_table2454
- GCC_except_table2458
- GCC_except_table2521
- GCC_except_table2522
- GCC_except_table2524
- GCC_except_table2525
- GCC_except_table2527
- GCC_except_table2532
- GCC_except_table2535
- GCC_except_table2538
- GCC_except_table2551
- GCC_except_table2621
- GCC_except_table2936
- GCC_except_table2937
- GCC_except_table2996
- GCC_except_table3067
- GCC_except_table3071
- GCC_except_table3115
- GCC_except_table3118
- GCC_except_table3119
- GCC_except_table3121
- GCC_except_table3395
- GCC_except_table3826
- GCC_except_table4093
- GCC_except_table4101
- GCC_except_table4109
- GCC_except_table4261
- GCC_except_table4265
- GCC_except_table4269
- GCC_except_table4292
- GCC_except_table4370
- GCC_except_table4371
- GCC_except_table4372
- GCC_except_table4373
- GCC_except_table4375
- GCC_except_table4377
- GCC_except_table4379
- GCC_except_table4381
- GCC_except_table4406
- GCC_except_table4408
- GCC_except_table4409
- GCC_except_table4412
- GCC_except_table4413
- GCC_except_table4415
- GCC_except_table4416
- GCC_except_table4417
- GCC_except_table4419
- GCC_except_table4433
- GCC_except_table4436
- GCC_except_table4437
- GCC_except_table4438
- GCC_except_table4439
- GCC_except_table4441
- GCC_except_table4444
- GCC_except_table4445
- GCC_except_table4447
- GCC_except_table4448
- GCC_except_table4455
- GCC_except_table5057
- GCC_except_table5067
- GCC_except_table5076
- GCC_except_table5084
- GCC_except_table5429
- GCC_except_table5430
- GCC_except_table5443
- GCC_except_table681
- GCC_except_table766
- GCC_except_table780
- GCC_except_table782
- GCC_except_table968
- HAPSystemKeychainStoreFunction.5735
- IOBluetoothDeviceFunction.1925
- IOBluetoothLibrary.sLib.13330
- IOBluetoothLibrary.sLib.1928
- IOBluetoothLibrary.sOnce.13325
- IOBluetoothLibrary.sOnce.1922
- MobileDeviceLibrary.sLib.4322
- MobileDeviceLibrary.sOnce.4320
- OBJC_IVAR_$_CULiveAction._alertType
- OBJC_IVAR_$_CULiveAction._destinationIDs
- OBJC_IVAR_$_CULiveAction._direct
- OBJC_IVAR_$_CULiveAction._dispatchQueue
- OBJC_IVAR_$_CULiveAction._invalidationHandler
- OBJC_IVAR_$_CULiveAction._originatingHomeKitAccessoryID
- OBJC_IVAR_$_CULiveAction._soundFileURL
- OBJC_IVAR_$_CULiveAction._speakText
- OBJC_IVAR_$_CUSystemMonitorImp._callObserver
- QuartzCoreLibrary.sLib.12801
- QuartzCoreLibrary.sOnce.12799
- RapportLibrary.sLib.5754
- RapportLibrary.sOnce.5749
- WiFiAwareInternetSharingConfigurationFunction.4904
- WiFiPeerToPeerLibrary.sLib.4865
- WiFiPeerToPeerLibrary.sLib.5163
- WiFiPeerToPeerLibrary.sLib.9666
- WiFiPeerToPeerLibrary.sOnce.4861
- WiFiPeerToPeerLibrary.sOnce.5156
- WiFiPeerToPeerLibrary.sOnce.9664
- _CXCallObserverFunction
- _Cfree
- _Cmalloc
- _NetTransportFinalize.11755
- _NetTransportFinalize.11763
- _NetTransportInitialize.11756
- _NetTransportInitialize.11766
- _NetTransportRead.11752
- _NetTransportRead.11765
- _NetTransportWriteV.11751
- _NetTransportWriteV.11764
- _OBJC_CLASS_$_CULiveAction
- _OBJC_METACLASS_$_CULiveAction
- __43-[CUSystemMonitorImp _meDeviceMonitorStart]_block_invoke.243
- __43-[CUSystemMonitorImp _meDeviceMonitorStart]_block_invoke.248
- __43-[CUSystemMonitorImp _meDeviceMonitorStart]_block_invoke_2.251
- __43-[CUSystemMonitorImp _systemUIMonitorStart]_block_invoke.566
- __47-[CUSystemMonitorImp _netInterfaceMonitorStart]_block_invoke.294
- __47-[CUSystemMonitorImp _netInterfaceMonitorStart]_block_invoke.299
- __47-[CUSystemMonitorImp _netInterfaceMonitorStart]_block_invoke.306
- __47-[CUSystemMonitorImp _netInterfaceMonitorStart]_block_invoke.313
- __47-[CUSystemMonitorImp _netInterfaceMonitorStart]_block_invoke_2.302
- __47-[CUSystemMonitorImp _netInterfaceMonitorStart]_block_invoke_2.309
- __47-[CUSystemMonitorImp _netInterfaceMonitorStart]_block_invoke_2.316
- __47-[CUSystemMonitorImp _netInterfaceMonitorStart]_block_invoke_3.305
- __47-[CUSystemMonitorImp _netInterfaceMonitorStart]_block_invoke_3.312
- __47-[CUSystemMonitorImp _netInterfaceMonitorStart]_block_invoke_3.319
- __AccountsLibrary_block_invoke.7972
- __AppleAccountLibrary_block_invoke.7975
- __AudioUnitLibrary_block_invoke.661
- __AuthKitLibrary_block_invoke.7961
- __Block_byref_object_copy_.10194
- __Block_byref_object_copy_.10739
- __Block_byref_object_copy_.12223
- __Block_byref_object_copy_.1977
- __Block_byref_object_copy_.2556
- __Block_byref_object_copy_.2810
- __Block_byref_object_copy_.4183
- __Block_byref_object_copy_.4287
- __Block_byref_object_copy_.4866
- __Block_byref_object_copy_.5184
- __Block_byref_object_copy_.5689
- __Block_byref_object_copy_.6016
- __Block_byref_object_copy_.8751
- __Block_byref_object_dispose_.10195
- __Block_byref_object_dispose_.10740
- __Block_byref_object_dispose_.12224
- __Block_byref_object_dispose_.1978
- __Block_byref_object_dispose_.2557
- __Block_byref_object_dispose_.2811
- __Block_byref_object_dispose_.4184
- __Block_byref_object_dispose_.4288
- __Block_byref_object_dispose_.4867
- __Block_byref_object_dispose_.5185
- __Block_byref_object_dispose_.5690
- __Block_byref_object_dispose_.6017
- __Block_byref_object_dispose_.8752
- __CoreAnalyticsLibrary_block_invoke.8438
- __CoreAudioLibrary_block_invoke.646
- __CoreBluetoothLibrary_block_invoke.1191
- __CoreBluetoothLibrary_block_invoke.1356
- __CoreBluetoothLibrary_block_invoke.1562
- __CoreBluetoothLibrary_block_invoke.1970
- __CoreHAPLibrary_block_invoke.5737
- __CoreServicesLibrary_block_invoke.13410
- __CoreServicesLibrary_block_invoke.8050
- __CoreServicesLibrary_block_invoke.839
- __CoreWLANLibrary_block_invoke.14206
- __IOBluetoothLibrary_block_invoke.13328
- __IOBluetoothLibrary_block_invoke.1927
- __MobileDeviceLibrary_block_invoke.4326
- __OBJC_$_INSTANCE_METHODS_CULiveAction
- __OBJC_$_INSTANCE_VARIABLES_CULiveAction
- __OBJC_$_PROP_LIST_CULiveAction
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CUXPCCodable
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CXCallObserverDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_CUXPCCodable
- __OBJC_$_PROTOCOL_METHOD_TYPES_CXCallObserverDelegate
- __OBJC_$_PROTOCOL_REFS_CXCallObserverDelegate
- __OBJC_CLASS_PROTOCOLS_$_CULiveAction
- __OBJC_CLASS_RO_$_CULiveAction
- __OBJC_LABEL_PROTOCOL_$_CUXPCCodable
- __OBJC_LABEL_PROTOCOL_$_CXCallObserverDelegate
- __OBJC_METACLASS_RO_$_CULiveAction
- __OBJC_PROTOCOL_$_CUXPCCodable
- __OBJC_PROTOCOL_$_CXCallObserverDelegate
- __QuartzCoreLibrary_block_invoke.12805
- __RapportLibrary_block_invoke.5753
- __WiFiPeerToPeerLibrary_block_invoke.4864
- __WiFiPeerToPeerLibrary_block_invoke.5161
- __WiFiPeerToPeerLibrary_block_invoke.9669
- ___26-[CULiveAction invalidate]_block_invoke
- ___39-[CULiveAction activateWithCompletion:]_block_invoke
- ___CallKitLibrary_block_invoke
- __block_descriptor_tmp.11461
- __block_descriptor_tmp.11509
- __block_descriptor_tmp.14310
- __block_descriptor_tmp.16
- __block_descriptor_tmp.3.14319
- __block_descriptor_tmp.384
- __block_descriptor_tmp.42.11457
- __block_descriptor_tmp.653
- __block_literal_global.10229
- __block_literal_global.10321
- __block_literal_global.1057
- __block_literal_global.11290
- __block_literal_global.11445
- __block_literal_global.11507
- __block_literal_global.1187
- __block_literal_global.1258
- __block_literal_global.1265
- __block_literal_global.1269
- __block_literal_global.1274
- __block_literal_global.12800
- __block_literal_global.1282
- __block_literal_global.1293
- __block_literal_global.1301
- __block_literal_global.1305
- __block_literal_global.1311
- __block_literal_global.1317
- __block_literal_global.1319
- __block_literal_global.1323
- __block_literal_global.1327
- __block_literal_global.1331
- __block_literal_global.1335
- __block_literal_global.1341
- __block_literal_global.1349
- __block_literal_global.135
- __block_literal_global.1352
- __block_literal_global.1357
- __block_literal_global.137
- __block_literal_global.14199
- __block_literal_global.14313
- __block_literal_global.155.8080
- __block_literal_global.1555
- __block_literal_global.157
- __block_literal_global.1713
- __block_literal_global.175
- __block_literal_global.177
- __block_literal_global.18
- __block_literal_global.1907
- __block_literal_global.198
- __block_literal_global.200
- __block_literal_global.208
- __block_literal_global.210
- __block_literal_global.220
- __block_literal_global.223
- __block_literal_global.228
- __block_literal_global.230
- __block_literal_global.252
- __block_literal_global.264
- __block_literal_global.2655
- __block_literal_global.268
- __block_literal_global.270
- __block_literal_global.2826
- __block_literal_global.289
- __block_literal_global.291
- __block_literal_global.296
- __block_literal_global.301
- __block_literal_global.304
- __block_literal_global.308
- __block_literal_global.311
- __block_literal_global.315
- __block_literal_global.3154
- __block_literal_global.318
- __block_literal_global.321
- __block_literal_global.323
- __block_literal_global.325
- __block_literal_global.333
- __block_literal_global.335
- __block_literal_global.3354
- __block_literal_global.34.12807
- __block_literal_global.353
- __block_literal_global.355
- __block_literal_global.374
- __block_literal_global.376
- __block_literal_global.381.9665
- __block_literal_global.385.7933
- __block_literal_global.40.12859
- __block_literal_global.402
- __block_literal_global.404
- __block_literal_global.4071
- __block_literal_global.415
- __block_literal_global.4321
- __block_literal_global.44.11452
- __block_literal_global.44.8113
- __block_literal_global.445
- __block_literal_global.447
- __block_literal_global.4611
- __block_literal_global.464
- __block_literal_global.466
- __block_literal_global.474
- __block_literal_global.484
- __block_literal_global.486
- __block_literal_global.4881
- __block_literal_global.490
- __block_literal_global.492.7883
- __block_literal_global.496.7879
- __block_literal_global.498
- __block_literal_global.5.11513
- __block_literal_global.506
- __block_literal_global.508
- __block_literal_global.5157
- __block_literal_global.571
- __block_literal_global.573
- __block_literal_global.5750
- __block_literal_global.583
- __block_literal_global.585
- __block_literal_global.600
- __block_literal_global.602
- __block_literal_global.640
- __block_literal_global.6520
- __block_literal_global.6907
- __block_literal_global.7312
- __block_literal_global.7755
- __block_literal_global.776
- __block_literal_global.792
- __block_literal_global.8111
- __block_literal_global.8404
- __block_literal_global.876
- __block_literal_global.8998
- __block_literal_global.931
- __block_literal_global.9315
- __block_literal_global.9628
- __block_literal_global.9988
- __logger_block_invoke.7989
- _classCXCallObserver
- _cstr_new
- _default_alloc
- _fmod
- _gLogCategory_CULiveAction
- _getCXCallObserverClass
- _initCXCallObserver
- _malloc_allocator
- _objc_msgSend$calls
- _objc_msgSend$hasConnected
- _objc_msgSend$hasEnded
- _objc_msgSend$setDelegate:queue:
- classACAccountStore.7968
- classAKAccountManager.7957
- classCALayer.12832
- classCATransaction.12849
- classCBCentralManager.1400
- classCBCentralManager.1974
- classCBPeripheralManager.1557
- classCBPeripheralManager.1966
- classCWWiFiClient.14201
- classHAPSystemKeychainStore.5733
- classIOBluetoothDevice.1923
- classWiFiAwareInternetSharingConfiguration.4902
- constantValCBManagerIsPrivilegedDaemonKey.1380
- constantValCBManagerNeedsRestrictedStateOperation.1395
- gCFArrayType.12023
- gCFBooleanType.12024
- gCFDataType.12025
- gCFDateType.12026
- gCFDictionaryType.12027
- gCFNumberType.12022
- gCFStringType.12028
- getACAccountStoreClass.7964
- getAKAccountManagerClass.7947
- getCALayerClass.12813
- getCATransactionClass.12839
- getCBCentralManagerClass.1383
- getCBCentralManagerClass.1956
- getCBManagerIsPrivilegedDaemonKey.1377
- getCBManagerNeedsRestrictedStateOperation.1384
- getCBPeripheralManagerClass.1549
- getCBPeripheralManagerClass.1958
- getCWWiFiClientClass.14183
- getHAPSystemKeychainStoreClass.5729
- getIOBluetoothDeviceClass.1906
- getWiFiAwareInternetSharingConfigurationClass.4890
- initACAccountStore.7966
- initAKAccountManager.7955
- initAMDeviceConnect.4343
- initAMDeviceCopyValue.4333
- initAMDeviceCreateCopy.4434
- initAMDeviceDisconnect.4319
- initAMDeviceStartSession.4340
- initAMDeviceStopSession.4329
- initAnalyticsSendEvent.8418
- initAudioObjectGetPropertyData.638
- initAudioUnitGetParameter.664
- initAudioUnitSetParameter.656
- initCALayer.12830
- initCATransaction.12847
- initCBCentralManager.1399
- initCBCentralManager.1973
- initCBPeripheralManager.1553
- initCBPeripheralManager.1964
- initCWWiFiClient.14197
- initHAPSystemKeychainStore.5731
- initIOBluetoothDevice.1921
- initIOBluetoothRegisterForNotifications.1962
- initIOBluetoothRemoveRegistrationForNotifications.1953
- initValCBManagerIsPrivilegedDaemonKey.1379
- initValCBManagerNeedsRestrictedStateOperation.1394
- initWiFiAwareInternetSharingConfiguration.4900
- logger.7985
- sCUOSLogCreateOnce_logger.7986
- sCUOSLogHandle_logger.7987
- softLinkAMDeviceConnect.4301
- softLinkAMDeviceCopyValue.4310
- softLinkAMDeviceCreateCopy.4414
- softLinkAMDeviceDisconnect.4315
- softLinkAMDeviceStartSession.4303
- softLinkAMDeviceStopSession.4314
- softLinkAnalyticsSendEvent.8416
- softLinkAudioObjectGetPropertyData.636
- softLinkAudioUnitGetParameter.652
- softLinkAudioUnitSetParameter.654
- softLinkIOBluetoothRegisterForNotifications.1960
- softLinkIOBluetoothRemoveRegistrationForNotifications.1939
CStrings:
+ "### Get home dir failed: %{darwin.errno}d"
+ "### _set_user_dir_suffix failed: %{darwin.errno}d"
+ "### confstr cache dir failed: %{darwin.errno}d"
+ "### confstr temp dir failed: %{darwin.errno}d"
+ "### read line failed: bad UTF-8"
+ "### read line failed: err=%d"
+ "### read line start failed: err=%d"
+ "### realpath cache dir failed: '%s', %{darwin.errno}d"
+ "### realpath home dir failed: path='%s', errno=%{darwin.errno}d"
+ "### realpath temp dir failed: '%s', %{darwin.errno}d"
+ "### sandbox init failed: %d, %s"
+ "### write line failed: err=%d"
+ "### write line start failed: err=%d"
+ "(.*)\\s+\\(\\d+\\)$"
+ "-[CUSystemMonitorImp _meDeviceOverride]"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CoreUtils/CoreUtils/TestUtils.c"
+ "@\"<WiFiAwareDataSessionPairingDelegate>\""
+ "@\"CUSerialPortConfiguration\""
+ "CUSerialPort"
+ "CUSerialPortConfiguration"
+ "FakeFMF"
+ "MeDevice override: IDS %@"
+ "Read line failed"
+ "Read line failed: bad UTF-8"
+ "Read line start failed"
+ "Request written: CID 0x%08X, Header %zu bytes, Body %zu bytes%?{end}, Type %'s\n"
+ "Skipping duplicate connection: %##a"
+ "T@\"<WiFiAwareDataSessionPairingDelegate>\",W,N,V_wfaPairingDelegate"
+ "T@\"NSString\",C,N,V_devicePath"
+ "TQ,N,V_flags"
+ "This Device"
+ "Tq,N,V_baudRate"
+ "Tq,N,V_flowControl"
+ "Write line start failed"
+ "^{SerialStreamPrivate=}"
+ "_DARWIN_USER_CACHE"
+ "_DARWIN_USER_TEMP"
+ "_HOME"
+ "_baudRate"
+ "_devicePath"
+ "_ensureSetUpAndReturnError:"
+ "_flowControl"
+ "_meDeviceOverride"
+ "_readLineWithFlags:completionHandler:"
+ "_serialStream"
+ "_wfaPairingDelegate"
+ "_writeLine:completionHandler:"
+ "baudRate"
+ "currentAudioAndVideoCallCount"
+ "devicePath"
+ "firstMatchInString:options:range:"
+ "flowControl"
+ "home:didUpdateActionSet:isExecuting:"
+ "initWithConfiguration:dispatchQueue:"
+ "initWithPattern:options:error:"
+ "numberOfRanges"
+ "publisher:detectedMulticastError:fromMulticastReceiver:"
+ "publisher:receivedDataBlobForMulticastSession:fromPeer:"
+ "rangeAtIndex:"
+ "read line start"
+ "read line success: line='%@'"
+ "readLineWithFlags:completionHandler:"
+ "serial stream configure failed"
+ "serial stream create failed"
+ "serial stream end: path=%@"
+ "serial stream start: path=%@"
+ "setBaudRate:"
+ "setDevicePath:"
+ "setFlowControl:"
+ "setPairingDelegate:"
+ "setWfaPairingDelegate:"
+ "subscriber:detectedMulticastError:fromMulticastSender:"
+ "subscriber:receivedDataBlobForMulticastSession:fromPeer:"
+ "substringWithRange:"
+ "v36@0:8@\"HMHome\"16@\"HMActionSet\"24B32"
+ "v40@0:8@\"WiFiAwarePublisher\"16@\"NSData\"24@\"WiFiMACAddress\"32"
+ "v40@0:8@\"WiFiAwarePublisher\"16q24@\"WiFiMACAddress\"32"
+ "v40@0:8@\"WiFiAwareSubscriber\"16@\"NSData\"24@\"WiFiMACAddress\"32"
+ "v40@0:8@\"WiFiAwareSubscriber\"16q24@\"WiFiMACAddress\"32"
+ "wfaPairingDelegate"
+ "write line failed"
+ "write line start: line='%@'"
+ "write line success"
+ "writeLine:completionHandler:"
+ "\xd1"
- "-1"
- "-[CULiveAction activateWithCompletion:]_block_invoke"
- "-[CULiveAction invalidate]_block_invoke"
- "-[CUSystemMonitorImp callObserver:callChanged:]"
- ".."
- "/AppleInternal/Library/BuildRoots/74a3b953-bbbb-11ef-9ee5-7675e0905095/Library/Caches/com.apple.xbs/Sources/CoreUtils/CoreUtils/TestUtils.c"
- "/System/Library/PrivateFrameworks/CallKit.framework/CallKit"
- "@\"CXCallObserver\""
- "@32@0:8@\"NSObject<OS_xpc_object>\"16^@24"
- "CF"
- "CULiveAction"
- "CUXPCCodable"
- "CXCallObserver"
- "CXCallObserverDelegate"
- "CallKit changed\n"
- "Not supported, use HomeKit instead"
- "Request written: CID 0x%08X, Header %zu bytes, Body %zu bytes\n"
- "T@\"NSArray\",C,N,V_destinationIDs"
- "T@\"NSString\",C,N,V_originatingHomeKitAccessoryID"
- "T@\"NSString\",C,N,V_speakText"
- "T@\"NSURL\",C,N,V_soundFileURL"
- "TB,N,V_direct"
- "Ti,N,V_alertType"
- "XPC non-dict"
- "_alertType"
- "_callObserver"
- "_destinationIDs"
- "_direct"
- "_originatingHomeKitAccessoryID"
- "_soundFileURL"
- "_speakText"
- "alertType"
- "callObserver:callChanged:"
- "calls"
- "destinationIDs"
- "direct"
- "hasConnected"
- "hasEnded"
- "originatingHomeKitAccessoryID"
- "setAlertType:"
- "setDelegate:queue:"
- "setDestinationIDs:"
- "setDirect:"
- "setOriginatingHomeKitAccessoryID:"
- "setSoundFileURL:"
- "setSpeakText:"
- "soundFileURL"
- "speakText"
- "user:didUpdatePersonManagerSettings:"
- "v24@0:8@\"NSObject<OS_xpc_object>\"16"
- "v32@0:8@\"CXCallObserver\"16@\"CXCall\"24"

```
