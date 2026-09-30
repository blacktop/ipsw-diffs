## CoreUtils

> `/System/Library/PrivateFrameworks/CoreUtils.framework/Versions/A/CoreUtils`

```diff

-770.26.0.0.0
-  __TEXT.__text: 0x118094
-  __TEXT.__auth_stubs: 0x29f0
-  __TEXT.__objc_methlist: 0x9988
-  __TEXT.__cstring: 0x2237d
-  __TEXT.__const: 0x2310
-  __TEXT.__gcc_except_tab: 0x1c44
-  __TEXT.__oslogstring: 0x620
-  __TEXT.__unwind_info: 0x3830
+780.12.0.0.0
+  __TEXT.__text: 0x11cef0
+  __TEXT.__auth_stubs: 0x2af0
+  __TEXT.__objc_methlist: 0x9e60
+  __TEXT.__cstring: 0x21774
+  __TEXT.__const: 0x2340
+  __TEXT.__gcc_except_tab: 0x1d28
+  __TEXT.__oslogstring: 0xdef
+  __TEXT.__unwind_info: 0x3950
   __TEXT.__eh_frame: 0x50
-  __TEXT.__objc_classname: 0xbf2
-  __TEXT.__objc_methname: 0x158b1
-  __TEXT.__objc_methtype: 0x4314
-  __TEXT.__objc_stubs: 0xa080
-  __DATA_CONST.__got: 0x610
-  __DATA_CONST.__const: 0x1470
-  __DATA_CONST.__objc_classlist: 0x308
+  __TEXT.__objc_classname: 0xcde
+  __TEXT.__objc_methname: 0x162b7
+  __TEXT.__objc_methtype: 0x44e3
+  __TEXT.__objc_stubs: 0xa400
+  __DATA_CONST.__got: 0x640
+  __DATA_CONST.__const: 0x1490
+  __DATA_CONST.__objc_classlist: 0x360
   __DATA_CONST.__objc_catlist: 0x48
-  __DATA_CONST.__objc_protolist: 0x140
+  __DATA_CONST.__objc_protolist: 0x150
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4c70
+  __DATA_CONST.__objc_selrefs: 0x4e68
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x208
-  __AUTH_CONST.__auth_got: 0x1508
+  __DATA_CONST.__objc_superrefs: 0x248
+  __DATA_CONST.__objc_arraydata: 0x8
+  __AUTH_CONST.__auth_got: 0x1588
   __AUTH_CONST.__auth_ptr: 0x20
-  __AUTH_CONST.__const: 0x3870
-  __AUTH_CONST.__cfstring: 0x3f20
-  __AUTH_CONST.__objc_const: 0x12f48
-  __AUTH_CONST.__objc_intobj: 0x168
-  __AUTH.__objc_data: 0x280
-  __AUTH.__data: 0x1e0
-  __DATA.__objc_ivar: 0x1484
-  __DATA.__data: 0x31c0
-  __DATA.__bss: 0xf30
+  __AUTH_CONST.__const: 0x38f0
+  __AUTH_CONST.__cfstring: 0x3fa0
+  __AUTH_CONST.__objc_const: 0x13ad0
+  __AUTH_CONST.__objc_intobj: 0x180
+  __AUTH_CONST.__objc_arrayobj: 0x18
+  __AUTH.__objc_data: 0x5f0
+  __AUTH.__data: 0x1f0
+  __DATA.__objc_ivar: 0x14e8
+  __DATA.__data: 0x3130
+  __DATA.__bss: 0xf70
   __DATA.__common: 0x2a
   __DATA_DIRTY.__objc_data: 0x1bd0
   __DATA_DIRTY.__data: 0xa38

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 5612
-  Symbols:   11426
-  CStrings:  9423
+  Functions: 5718
+  Symbols:   11698
+  CStrings:  9563
 
Symbols:
+ +[CUSPAKECommon scryptWithPasswordData:outputPtr:outputLen:error:]
+ -[CUFile .cxx_destruct]
+ -[CUFile _completeReadRequest:data:error:]
+ -[CUFile _completeWriteRequest:error:]
+ -[CUFile _openForReadingAndReturnError:]
+ -[CUFile _openForWritingAndReturnError:]
+ -[CUFile _processRead:]
+ -[CUFile _processReads]
+ -[CUFile _processWrite:]
+ -[CUFile _processWrites]
+ -[CUFile _readRequest:]
+ -[CUFile _writeRequest:]
+ -[CUFile closeWithCompletionHandler:]
+ -[CUFile dealloc]
+ -[CUFile initForReadingFromURL:dispatchQueue:]
+ -[CUFile initForWritingToURL:dispatchQueue:]
+ -[CUFile initForWritingToURL:totalLength:dispatchQueue:]
+ -[CUFile openWithCompletionHandler:]
+ -[CUFile readLength:completionHandler:]
+ -[CUFile readLength:offset:completionHandler:]
+ -[CUFile writeData:completionHandler:]
+ -[CUFile writeData:offset:completionHandler:]
+ -[CUFileReadRequest .cxx_destruct]
+ -[CUFileReadRequest completionHandler]
+ -[CUFileReadRequest length]
+ -[CUFileReadRequest offset]
+ -[CUFileReadRequest setCompletionHandler:]
+ -[CUFileReadRequest setLength:]
+ -[CUFileReadRequest setOffset:]
+ -[CUFileWriteRequest .cxx_destruct]
+ -[CUFileWriteRequest completionHandler]
+ -[CUFileWriteRequest data]
+ -[CUFileWriteRequest offset]
+ -[CUFileWriteRequest setCompletionHandler:]
+ -[CUFileWriteRequest setData:]
+ -[CUFileWriteRequest setOffset:]
+ -[CUNANDataSession _pairingRequestStartedForDataSession:pinCodeInputCompletionHandler:]
+ -[CUNANDataSession pairingPromptHandler]
+ -[CUNANDataSession pairingRequestStartedForDataSession:pinCodeInputCompletionHandler:]
+ -[CUNANDataSession setPairingPromptHandler:]
+ -[CUNANDataSession setWfaPairingCacheEnabled:]
+ -[CUNANDataSession setWfaPairingMethod:]
+ -[CUNANDataSession tryPairingPassword:]
+ -[CUNANDataSession wfaPairingCacheEnabled]
+ -[CUNANDataSession wfaPairingMethod]
+ -[CUNANPairingPromptInfo .cxx_destruct]
+ -[CUNANPairingPromptInfo description]
+ -[CUNANPairingPromptInfo initWithDataSession:]
+ -[CUNANPairingPromptInfo name]
+ -[CUNANPairingPromptInfo textInfo]
+ -[CUNANPairingShowInfo .cxx_destruct]
+ -[CUNANPairingShowInfo description]
+ -[CUNANPairingShowInfo initWithSubscriberInfo:pinCode:]
+ -[CUNANPairingShowInfo name]
+ -[CUNANPairingShowInfo pinCode]
+ -[CUNANPairingShowInfo textInfo]
+ -[CUNANPublisher pairingRequestIndicatedForPublisher:bySubscriber:usingPINCode:]
+ -[CUNANPublisher pairingShowHandler]
+ -[CUNANPublisher setPairingShowHandler:]
+ -[CUSPAKEM1 .cxx_destruct]
+ -[CUSPAKEM1 dictionaryRepresentation]
+ -[CUSPAKEM1 initWithDictionary:error:]
+ -[CUSPAKEM1 setSharePData:]
+ -[CUSPAKEM1 sharePData]
+ -[CUSPAKEM2 .cxx_destruct]
+ -[CUSPAKEM2 confirmVData]
+ -[CUSPAKEM2 dictionaryRepresentation]
+ -[CUSPAKEM2 initWithDictionary:error:]
+ -[CUSPAKEM2 setConfirmVData:]
+ -[CUSPAKEM2 setShareVData:]
+ -[CUSPAKEM2 shareVData]
+ -[CUSPAKEM3 .cxx_destruct]
+ -[CUSPAKEM3 confirmPData]
+ -[CUSPAKEM3 dictionaryRepresentation]
+ -[CUSPAKEM3 initWithDictionary:error:]
+ -[CUSPAKEM3 setConfirmPData:]
+ -[CUSPAKEProver .cxx_destruct]
+ -[CUSPAKEProver dealloc]
+ -[CUSPAKEProver finishAndReturnError:]
+ -[CUSPAKEProver generateM1AndReturnError:]
+ -[CUSPAKEProver generateM3WithM2:error:]
+ -[CUSPAKEProver initWithPasswordCString:]
+ -[CUSPAKEProver initWithPasswordPtr:passwordLength:]
+ -[CUSPAKEProver initWithPasswordString:]
+ -[CUSPAKEVerifier .cxx_destruct]
+ -[CUSPAKEVerifier dealloc]
+ -[CUSPAKEVerifier finishWithM3:error:]
+ -[CUSPAKEVerifier generateM2WithM1:error:]
+ -[CUSPAKEVerifier initWithPasswordCString:]
+ -[CUSPAKEVerifier initWithPasswordPtr:passwordLength:]
+ -[CUSPAKEVerifier initWithPasswordString:]
+ ACAccountStoreFunction.7885
+ AKAccountManagerFunction.7874
+ AccountsLibrary.sLib.7888
+ AccountsLibrary.sOnce.7882
+ AppleAccountLibrary.sLib.7891
+ AppleAccountLibrary.sOnce.7878
+ AudioUnitLibrary.sLib.559
+ AudioUnitLibrary.sOnce.558
+ AuthKitLibrary.sLib.7877
+ AuthKitLibrary.sOnce.7871
+ CALayerFunction.12872
+ CATransactionFunction.12889
+ CBCentralManagerFunction.1314
+ CBCentralManagerFunction.1889
+ CBManagerIsPrivilegedDaemonKeyFunction.1294
+ CBManagerNeedsRestrictedStateOperationFunction.1309
+ CBPeripheralManagerFunction.1471
+ CBPeripheralManagerFunction.1881
+ CWWiFiClientFunction.14092
+ CoreAnalyticsLibrary.sLib.8329
+ CoreAnalyticsLibrary.sOnce.8327
+ CoreAudioLibrary.sLib.542
+ CoreAudioLibrary.sOnce.540
+ CoreBluetoothLibrary.sLib.1105
+ CoreBluetoothLibrary.sLib.1270
+ CoreBluetoothLibrary.sLib.1476
+ CoreBluetoothLibrary.sLib.1884
+ CoreBluetoothLibrary.sOnce.1103
+ CoreBluetoothLibrary.sOnce.1268
+ CoreBluetoothLibrary.sOnce.1466
+ CoreBluetoothLibrary.sOnce.1878
+ CoreHAPLibrary.sLib.5625
+ CoreHAPLibrary.sOnce.5617
+ CoreServicesLibrary.sLib.13301
+ CoreServicesLibrary.sLib.749
+ CoreServicesLibrary.sLib.7977
+ CoreServicesLibrary.sOnce.13300
+ CoreServicesLibrary.sOnce.747
+ CoreServicesLibrary.sOnce.7976
+ CoreWLANLibrary.sLib.14097
+ CoreWLANLibrary.sOnce.14087
+ GCC_except_table2306
+ GCC_except_table2307
+ GCC_except_table2326
+ GCC_except_table2361
+ GCC_except_table2434
+ GCC_except_table2458
+ GCC_except_table2492
+ GCC_except_table2496
+ GCC_except_table2559
+ GCC_except_table2563
+ GCC_except_table2565
+ GCC_except_table2570
+ GCC_except_table2573
+ GCC_except_table2576
+ GCC_except_table2579
+ GCC_except_table2582
+ GCC_except_table2589
+ GCC_except_table2591
+ GCC_except_table2659
+ GCC_except_table2974
+ GCC_except_table2975
+ GCC_except_table3034
+ GCC_except_table3105
+ GCC_except_table3109
+ GCC_except_table3153
+ GCC_except_table3156
+ GCC_except_table3157
+ GCC_except_table3159
+ GCC_except_table3433
+ GCC_except_table3861
+ GCC_except_table4128
+ GCC_except_table4136
+ GCC_except_table4144
+ GCC_except_table4296
+ GCC_except_table4300
+ GCC_except_table4302
+ GCC_except_table4304
+ GCC_except_table4327
+ GCC_except_table4412
+ GCC_except_table4413
+ GCC_except_table4414
+ GCC_except_table4416
+ GCC_except_table4422
+ GCC_except_table4426
+ GCC_except_table4447
+ GCC_except_table4469
+ GCC_except_table4475
+ GCC_except_table4478
+ GCC_except_table4479
+ GCC_except_table4480
+ GCC_except_table4481
+ GCC_except_table4482
+ GCC_except_table4483
+ GCC_except_table4485
+ GCC_except_table4486
+ GCC_except_table4487
+ GCC_except_table4488
+ GCC_except_table4489
+ GCC_except_table4490
+ GCC_except_table4491
+ GCC_except_table4492
+ GCC_except_table4493
+ GCC_except_table4494
+ GCC_except_table4495
+ GCC_except_table4496
+ GCC_except_table4497
+ GCC_except_table4499
+ GCC_except_table4500
+ GCC_except_table4501
+ GCC_except_table4503
+ GCC_except_table5137
+ GCC_except_table5142
+ GCC_except_table5146
+ GCC_except_table5212
+ GCC_except_table5222
+ GCC_except_table5231
+ GCC_except_table5239
+ GCC_except_table5563
+ GCC_except_table5564
+ GCC_except_table5577
+ HAPSystemKeychainStoreFunction.5621
+ IOBluetoothDeviceFunction.1838
+ IOBluetoothLibrary.sLib.13224
+ IOBluetoothLibrary.sLib.1841
+ IOBluetoothLibrary.sOnce.13219
+ IOBluetoothLibrary.sOnce.1835
+ MobileDeviceLibrary.sLib.4155
+ MobileDeviceLibrary.sOnce.4153
+ OBJC_IVAR_$_CUFile._dispatchQueue
+ OBJC_IVAR_$_CUFile._fd
+ OBJC_IVAR_$_CUFile._readQueue
+ OBJC_IVAR_$_CUFile._totalLength
+ OBJC_IVAR_$_CUFile._url
+ OBJC_IVAR_$_CUFile._writeQueue
+ OBJC_IVAR_$_CUFileReadRequest._completionHandler
+ OBJC_IVAR_$_CUFileReadRequest._length
+ OBJC_IVAR_$_CUFileReadRequest._offset
+ OBJC_IVAR_$_CUFileWriteRequest._completionHandler
+ OBJC_IVAR_$_CUFileWriteRequest._data
+ OBJC_IVAR_$_CUFileWriteRequest._offset
+ OBJC_IVAR_$_CUNANDataSession._pairingPromptHandler
+ OBJC_IVAR_$_CUNANDataSession._pinCodeInputCompletionHandler
+ OBJC_IVAR_$_CUNANDataSession._wfaPairingCacheEnabled
+ OBJC_IVAR_$_CUNANDataSession._wfaPairingMethod
+ OBJC_IVAR_$_CUNANPairingPromptInfo._name
+ OBJC_IVAR_$_CUNANPairingPromptInfo._textInfo
+ OBJC_IVAR_$_CUNANPairingShowInfo._name
+ OBJC_IVAR_$_CUNANPairingShowInfo._pinCode
+ OBJC_IVAR_$_CUNANPairingShowInfo._textInfo
+ OBJC_IVAR_$_CUNANPublisher._pairingShowHandler
+ OBJC_IVAR_$_CUSPAKEM1._sharePData
+ OBJC_IVAR_$_CUSPAKEM2._confirmVData
+ OBJC_IVAR_$_CUSPAKEM2._shareVData
+ OBJC_IVAR_$_CUSPAKEM3._confirmPData
+ OBJC_IVAR_$_CUSPAKEProver._passwordData
+ OBJC_IVAR_$_CUSPAKEProver._sessionKey
+ OBJC_IVAR_$_CUSPAKEProver._spakeContext
+ OBJC_IVAR_$_CUSPAKEVerifier._passwordData
+ OBJC_IVAR_$_CUSPAKEVerifier._spakeContext
+ QuartzCoreLibrary.sLib.12839
+ QuartzCoreLibrary.sOnce.12837
+ RapportLibrary.sLib.5640
+ RapportLibrary.sOnce.5635
+ WiFiAwareInternetSharingConfigurationFunction.4789
+ WiFiPeerToPeerLibrary.sLib.4741
+ WiFiPeerToPeerLibrary.sLib.5048
+ WiFiPeerToPeerLibrary.sLib.9587
+ WiFiPeerToPeerLibrary.sOnce.4736
+ WiFiPeerToPeerLibrary.sOnce.5043
+ WiFiPeerToPeerLibrary.sOnce.9586
+ _CUPrintNSDataHexDump
+ _CUPrintTXTRecordNSData
+ _HTTPClientSetConnectionProgressHandler
+ _NetTransportFinalize.11690
+ _NetTransportFinalize.11698
+ _NetTransportInitialize.11691
+ _NetTransportInitialize.11701
+ _NetTransportRead.11687
+ _NetTransportRead.11700
+ _NetTransportWriteV.11686
+ _NetTransportWriteV.11699
+ _OBJC_CLASS_$_CUFile
+ _OBJC_CLASS_$_CUFileReadRequest
+ _OBJC_CLASS_$_CUFileWriteRequest
+ _OBJC_CLASS_$_CUNANPairingPromptInfo
+ _OBJC_CLASS_$_CUNANPairingShowInfo
+ _OBJC_CLASS_$_CUSPAKECommon
+ _OBJC_CLASS_$_CUSPAKEM1
+ _OBJC_CLASS_$_CUSPAKEM2
+ _OBJC_CLASS_$_CUSPAKEM3
+ _OBJC_CLASS_$_CUSPAKEProver
+ _OBJC_CLASS_$_CUSPAKEVerifier
+ _OBJC_CLASS_$_NSConstantArray
+ _OBJC_CLASS_$_NSFileManager
+ _OBJC_METACLASS_$_CUFile
+ _OBJC_METACLASS_$_CUFileReadRequest
+ _OBJC_METACLASS_$_CUFileWriteRequest
+ _OBJC_METACLASS_$_CUNANPairingPromptInfo
+ _OBJC_METACLASS_$_CUNANPairingShowInfo
+ _OBJC_METACLASS_$_CUSPAKECommon
+ _OBJC_METACLASS_$_CUSPAKEM1
+ _OBJC_METACLASS_$_CUSPAKEM2
+ _OBJC_METACLASS_$_CUSPAKEM3
+ _OBJC_METACLASS_$_CUSPAKEProver
+ _OBJC_METACLASS_$_CUSPAKEVerifier
+ _WiFiAwarePairingConfigurationFunction
+ _WiFiAwarePublishDatapathSecurityConfigurationFunction
+ __61-[CUNANPublisher sendMessageData:endpoint:completionHandler:]_block_invoke.47
+ __61-[CUNANPublisher sendMessageData:endpoint:completionHandler:]_block_invoke.50
+ __62-[CUNANSubscriber sendMessageData:endpoint:completionHandler:]_block_invoke.18
+ __62-[CUNANSubscriber sendMessageData:endpoint:completionHandler:]_block_invoke_2.19
+ __AccountsLibrary_block_invoke.7887
+ __AppleAccountLibrary_block_invoke.7890
+ __AudioUnitLibrary_block_invoke.562
+ __AuthKitLibrary_block_invoke.7876
+ __Block_byref_object_copy_.10117
+ __Block_byref_object_copy_.10620
+ __Block_byref_object_copy_.12257
+ __Block_byref_object_copy_.1890
+ __Block_byref_object_copy_.2482
+ __Block_byref_object_copy_.2736
+ __Block_byref_object_copy_.4016
+ __Block_byref_object_copy_.4120
+ __Block_byref_object_copy_.4742
+ __Block_byref_object_copy_.5071
+ __Block_byref_object_copy_.5573
+ __Block_byref_object_copy_.5903
+ __Block_byref_object_copy_.8674
+ __Block_byref_object_dispose_.10118
+ __Block_byref_object_dispose_.10621
+ __Block_byref_object_dispose_.12258
+ __Block_byref_object_dispose_.1891
+ __Block_byref_object_dispose_.2483
+ __Block_byref_object_dispose_.2737
+ __Block_byref_object_dispose_.4017
+ __Block_byref_object_dispose_.4121
+ __Block_byref_object_dispose_.4743
+ __Block_byref_object_dispose_.5072
+ __Block_byref_object_dispose_.5574
+ __Block_byref_object_dispose_.5904
+ __Block_byref_object_dispose_.8675
+ __CoreAnalyticsLibrary_block_invoke.8362
+ __CoreAudioLibrary_block_invoke.547
+ __CoreBluetoothLibrary_block_invoke.1108
+ __CoreBluetoothLibrary_block_invoke.1273
+ __CoreBluetoothLibrary_block_invoke.1474
+ __CoreBluetoothLibrary_block_invoke.1883
+ __CoreHAPLibrary_block_invoke.5623
+ __CoreServicesLibrary_block_invoke.13304
+ __CoreServicesLibrary_block_invoke.752
+ __CoreServicesLibrary_block_invoke.7979
+ __CoreWLANLibrary_block_invoke.14095
+ __IOBluetoothLibrary_block_invoke.13222
+ __IOBluetoothLibrary_block_invoke.1840
+ __MobileDeviceLibrary_block_invoke.4159
+ __OBJC_$_CLASS_METHODS_CUSPAKECommon
+ __OBJC_$_INSTANCE_METHODS_CUFile
+ __OBJC_$_INSTANCE_METHODS_CUFileReadRequest
+ __OBJC_$_INSTANCE_METHODS_CUFileWriteRequest
+ __OBJC_$_INSTANCE_METHODS_CUNANPairingPromptInfo
+ __OBJC_$_INSTANCE_METHODS_CUNANPairingShowInfo
+ __OBJC_$_INSTANCE_METHODS_CUSPAKEM1
+ __OBJC_$_INSTANCE_METHODS_CUSPAKEM2
+ __OBJC_$_INSTANCE_METHODS_CUSPAKEM3
+ __OBJC_$_INSTANCE_METHODS_CUSPAKEProver
+ __OBJC_$_INSTANCE_METHODS_CUSPAKEVerifier
+ __OBJC_$_INSTANCE_VARIABLES_CUFile
+ __OBJC_$_INSTANCE_VARIABLES_CUFileReadRequest
+ __OBJC_$_INSTANCE_VARIABLES_CUFileWriteRequest
+ __OBJC_$_INSTANCE_VARIABLES_CUNANPairingPromptInfo
+ __OBJC_$_INSTANCE_VARIABLES_CUNANPairingShowInfo
+ __OBJC_$_INSTANCE_VARIABLES_CUSPAKEM1
+ __OBJC_$_INSTANCE_VARIABLES_CUSPAKEM2
+ __OBJC_$_INSTANCE_VARIABLES_CUSPAKEM3
+ __OBJC_$_INSTANCE_VARIABLES_CUSPAKEProver
+ __OBJC_$_INSTANCE_VARIABLES_CUSPAKEVerifier
+ __OBJC_$_PROP_LIST_CUFileReadRequest
+ __OBJC_$_PROP_LIST_CUFileWriteRequest
+ __OBJC_$_PROP_LIST_CUNANPairingPromptInfo
+ __OBJC_$_PROP_LIST_CUNANPairingShowInfo
+ __OBJC_$_PROP_LIST_CUSPAKEM1
+ __OBJC_$_PROP_LIST_CUSPAKEM2
+ __OBJC_$_PROP_LIST_CUSPAKEM3
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_WiFiAwareDataSessionPairingDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_WiFiAwarePublisherPairingDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_WiFiAwareDataSessionPairingDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_WiFiAwarePublisherPairingDelegate
+ __OBJC_$_PROTOCOL_REFS_WiFiAwareDataSessionPairingDelegate
+ __OBJC_$_PROTOCOL_REFS_WiFiAwarePublisherPairingDelegate
+ __OBJC_CLASS_RO_$_CUFile
+ __OBJC_CLASS_RO_$_CUFileReadRequest
+ __OBJC_CLASS_RO_$_CUFileWriteRequest
+ __OBJC_CLASS_RO_$_CUNANPairingPromptInfo
+ __OBJC_CLASS_RO_$_CUNANPairingShowInfo
+ __OBJC_CLASS_RO_$_CUSPAKECommon
+ __OBJC_CLASS_RO_$_CUSPAKEM1
+ __OBJC_CLASS_RO_$_CUSPAKEM2
+ __OBJC_CLASS_RO_$_CUSPAKEM3
+ __OBJC_CLASS_RO_$_CUSPAKEProver
+ __OBJC_CLASS_RO_$_CUSPAKEVerifier
+ __OBJC_LABEL_PROTOCOL_$_WiFiAwareDataSessionPairingDelegate
+ __OBJC_LABEL_PROTOCOL_$_WiFiAwarePublisherPairingDelegate
+ __OBJC_METACLASS_RO_$_CUFile
+ __OBJC_METACLASS_RO_$_CUFileReadRequest
+ __OBJC_METACLASS_RO_$_CUFileWriteRequest
+ __OBJC_METACLASS_RO_$_CUNANPairingPromptInfo
+ __OBJC_METACLASS_RO_$_CUNANPairingShowInfo
+ __OBJC_METACLASS_RO_$_CUSPAKECommon
+ __OBJC_METACLASS_RO_$_CUSPAKEM1
+ __OBJC_METACLASS_RO_$_CUSPAKEM2
+ __OBJC_METACLASS_RO_$_CUSPAKEM3
+ __OBJC_METACLASS_RO_$_CUSPAKEProver
+ __OBJC_METACLASS_RO_$_CUSPAKEVerifier
+ __OBJC_PROTOCOL_$_WiFiAwareDataSessionPairingDelegate
+ __OBJC_PROTOCOL_$_WiFiAwarePublisherPairingDelegate
+ __QuartzCoreLibrary_block_invoke.12843
+ __RapportLibrary_block_invoke.5639
+ __WiFiPeerToPeerLibrary_block_invoke.4739
+ __WiFiPeerToPeerLibrary_block_invoke.5046
+ __WiFiPeerToPeerLibrary_block_invoke.9590
+ ___17-[CUFile dealloc]_block_invoke
+ ___36-[CUFile openWithCompletionHandler:]_block_invoke
+ ___37-[CUFile closeWithCompletionHandler:]_block_invoke
+ ___38-[CUFile writeData:completionHandler:]_block_invoke
+ ___39-[CUFile readLength:completionHandler:]_block_invoke
+ ___39-[CUNANDataSession tryPairingPassword:]_block_invoke
+ ___45-[CUFile writeData:offset:completionHandler:]_block_invoke
+ ___46-[CUFile readLength:offset:completionHandler:]_block_invoke
+ ___80-[CUNANPublisher pairingRequestIndicatedForPublisher:bySubscriber:usingPINCode:]_block_invoke
+ ___86-[CUNANDataSession pairingRequestStartedForDataSession:pinCodeInputCompletionHandler:]_block_invoke
+ ___block_descriptor_32_e8_v16?0q8l
+ __block_descriptor_tmp.11336
+ __block_descriptor_tmp.11385
+ __block_descriptor_tmp.14199
+ __block_descriptor_tmp.328
+ __block_descriptor_tmp.42.11332
+ __block_descriptor_tmp.554
+ __block_descriptor_tmp.7.11391
+ __block_literal_global.10152
+ __block_literal_global.10203
+ __block_literal_global.1104
+ __block_literal_global.11168
+ __block_literal_global.11320
+ __block_literal_global.11397
+ __block_literal_global.12036
+ __block_literal_global.1269
+ __block_literal_global.12838
+ __block_literal_global.14088
+ __block_literal_global.14202
+ __block_literal_global.1467
+ __block_literal_global.1625
+ __block_literal_global.163.748
+ __block_literal_global.1818
+ __block_literal_global.251
+ __block_literal_global.256.10603
+ __block_literal_global.2581
+ __block_literal_global.268
+ __block_literal_global.273
+ __block_literal_global.2752
+ __block_literal_global.278
+ __block_literal_global.3078
+ __block_literal_global.325
+ __block_literal_global.3278
+ __block_literal_global.34.12845
+ __block_literal_global.375
+ __block_literal_global.385.7854
+ __block_literal_global.3904
+ __block_literal_global.396
+ __block_literal_global.40.12897
+ __block_literal_global.4154
+ __block_literal_global.44.11327
+ __block_literal_global.44.8038
+ __block_literal_global.4466
+ __block_literal_global.4758
+ __block_literal_global.4965
+ __block_literal_global.541
+ __block_literal_global.56
+ __block_literal_global.5636
+ __block_literal_global.6415
+ __block_literal_global.6804
+ __block_literal_global.7212
+ __block_literal_global.7663
+ __block_literal_global.789
+ __block_literal_global.8036
+ __block_literal_global.8328
+ __block_literal_global.844
+ __block_literal_global.8921
+ __block_literal_global.9238
+ __block_literal_global.9550
+ __block_literal_global.972
+ __block_literal_global.9910
+ __logger_block_invoke.12040
+ __logger_block_invoke.4716
+ __logger_block_invoke.4969
+ __logger_block_invoke.7216
+ __logger_block_invoke.7907
+ _cc_clear
+ _ccscrypt
+ _ccscrypt_storage_size
+ _ccspake_cp_256_rfc
+ _ccspake_generate_L
+ _ccspake_kex_generate
+ _ccspake_kex_process
+ _ccspake_mac_compute
+ _ccspake_mac_hkdf_hmac_sha256
+ _ccspake_mac_verify_and_get_session_key
+ _ccspake_prover_initialize
+ _ccspake_reduce_w
+ _ccspake_sizeof_ctx
+ _ccspake_sizeof_point
+ _ccspake_sizeof_w
+ _ccspake_verifier_initialize
+ _classWiFiAwarePairingConfiguration
+ _classWiFiAwarePublishDatapathSecurityConfiguration
+ _getWiFiAwarePairingConfigurationClass
+ _getWiFiAwarePublishDatapathSecurityConfigurationClass
+ _initWiFiAwarePairingConfiguration
+ _initWiFiAwarePublishDatapathSecurityConfiguration
+ _objc_msgSend$URLByDeletingLastPathComponent
+ _objc_msgSend$_completeReadRequest:data:error:
+ _objc_msgSend$_newZeroingDataWithBytes:length:
+ _objc_msgSend$_openForReadingAndReturnError:
+ _objc_msgSend$_openForWritingAndReturnError:
+ _objc_msgSend$_pairingRequestStartedForDataSession:pinCodeInputCompletionHandler:
+ _objc_msgSend$_processRead:
+ _objc_msgSend$_processWrite:
+ _objc_msgSend$_readRequest:
+ _objc_msgSend$_writeRequest:
+ _objc_msgSend$confirmPData
+ _objc_msgSend$confirmVData
+ _objc_msgSend$createDirectoryAtURL:withIntermediateDirectories:attributes:error:
+ _objc_msgSend$initWithDataSession:
+ _objc_msgSend$initWithPairingConfiguration:usingPairingDelegate:
+ _objc_msgSend$initWithSubscriberInfo:pinCode:
+ _objc_msgSend$initWithSupportedPairSetupMethods:pairingCachingEnabled:
+ _objc_msgSend$offset
+ _objc_msgSend$scryptWithPasswordData:outputPtr:outputLen:error:
+ _objc_msgSend$setConfirmPData:
+ _objc_msgSend$setConfirmVData:
+ _objc_msgSend$setOffset:
+ _objc_msgSend$setPairingCachingEnabled:
+ _objc_msgSend$setPairingMethod:
+ _objc_msgSend$setSharePData:
+ _objc_msgSend$setShareVData:
+ _objc_msgSend$sharePData
+ _objc_msgSend$shareVData
+ classACAccountStore.7883
+ classAKAccountManager.7872
+ classCALayer.12870
+ classCATransaction.12887
+ classCBCentralManager.1312
+ classCBCentralManager.1887
+ classCBPeripheralManager.1469
+ classCBPeripheralManager.1879
+ classCWWiFiClient.14090
+ classHAPSystemKeychainStore.5619
+ classIOBluetoothDevice.1836
+ classWiFiAwareInternetSharingConfiguration.4787
+ constantValCBManagerIsPrivilegedDaemonKey.1292
+ constantValCBManagerNeedsRestrictedStateOperation.1307
+ gCFArrayType.11960
+ gCFBooleanType.11961
+ gCFDataType.11962
+ gCFDateType.11963
+ gCFDictionaryType.11964
+ gCFNumberType.11959
+ gCFStringType.11965
+ getACAccountStoreClass.7879
+ getAKAccountManagerClass.7862
+ getCALayerClass.12851
+ getCATransactionClass.12877
+ getCBCentralManagerClass.1295
+ getCBCentralManagerClass.1869
+ getCBManagerIsPrivilegedDaemonKey.1289
+ getCBManagerNeedsRestrictedStateOperation.1296
+ getCBPeripheralManagerClass.1461
+ getCBPeripheralManagerClass.1871
+ getCWWiFiClientClass.14072
+ getHAPSystemKeychainStoreClass.5614
+ getIOBluetoothDeviceClass.1817
+ getWiFiAwareInternetSharingConfigurationClass.4768
+ initACAccountStore.7881
+ initAKAccountManager.7870
+ initAMDeviceConnect.4176
+ initAMDeviceCopyValue.4168
+ initAMDeviceCreateCopy.4267
+ initAMDeviceDisconnect.4152
+ initAMDeviceStartSession.4173
+ initAMDeviceStopSession.4162
+ initAnalyticsSendEvent.8343
+ initAudioObjectGetPropertyData.539
+ initAudioUnitGetParameter.565
+ initAudioUnitSetParameter.557
+ initCALayer.12868
+ initCATransaction.12885
+ initCBCentralManager.1311
+ initCBCentralManager.1886
+ initCBPeripheralManager.1465
+ initCBPeripheralManager.1877
+ initCWWiFiClient.14086
+ initHAPSystemKeychainStore.5616
+ initIOBluetoothDevice.1834
+ initIOBluetoothRegisterForNotifications.1875
+ initIOBluetoothRemoveRegistrationForNotifications.1866
+ initValCBManagerIsPrivilegedDaemonKey.1291
+ initValCBManagerNeedsRestrictedStateOperation.1306
+ initWiFiAwareInternetSharingConfiguration.4785
+ logger.12032
+ logger.4712
+ logger.4962
+ logger.7209
+ logger.7902
+ sCUOSLogCreateOnce_logger.12035
+ sCUOSLogCreateOnce_logger.4713
+ sCUOSLogCreateOnce_logger.4964
+ sCUOSLogCreateOnce_logger.7211
+ sCUOSLogCreateOnce_logger.7904
+ sCUOSLogHandle_logger.12037
+ sCUOSLogHandle_logger.4714
+ sCUOSLogHandle_logger.4966
+ sCUOSLogHandle_logger.7213
+ sCUOSLogHandle_logger.7905
+ softLinkAMDeviceConnect.4134
+ softLinkAMDeviceCopyValue.4143
+ softLinkAMDeviceCreateCopy.4247
+ softLinkAMDeviceDisconnect.4148
+ softLinkAMDeviceStartSession.4136
+ softLinkAMDeviceStopSession.4147
+ softLinkAnalyticsSendEvent.8340
+ softLinkAudioObjectGetPropertyData.537
+ softLinkAudioUnitGetParameter.553
+ softLinkAudioUnitSetParameter.555
+ softLinkIOBluetoothRegisterForNotifications.1873
+ softLinkIOBluetoothRemoveRegistrationForNotifications.1852
- -[CUNANDataSession dealloc]
- -[CUNANDataSession label]
- -[CUNANDataSession setLabel:]
- -[CUNANPublisher label]
- -[CUNANPublisher setLabel:]
- -[CUNANSubscriber label]
- -[CUNANSubscriber setLabel:]
- ACAccountStoreFunction.7828
- AKAccountManagerFunction.7817
- AccountsLibrary.sLib.7831
- AccountsLibrary.sOnce.7825
- AppleAccountLibrary.sLib.7834
- AppleAccountLibrary.sOnce.7821
- AudioUnitLibrary.sLib.561
- AudioUnitLibrary.sOnce.560
- AuthKitLibrary.sLib.7820
- AuthKitLibrary.sOnce.7814
- CALayerFunction.12585
- CATransactionFunction.12602
- CBCentralManagerFunction.1315
- CBCentralManagerFunction.1890
- CBManagerIsPrivilegedDaemonKeyFunction.1295
- CBManagerNeedsRestrictedStateOperationFunction.1310
- CBPeripheralManagerFunction.1473
- CBPeripheralManagerFunction.1882
- CWWiFiClientFunction.13806
- CoreAnalyticsLibrary.sLib.8272
- CoreAnalyticsLibrary.sOnce.8270
- CoreAudioLibrary.sLib.544
- CoreAudioLibrary.sOnce.542
- CoreBluetoothLibrary.sLib.1108
- CoreBluetoothLibrary.sLib.1273
- CoreBluetoothLibrary.sLib.1478
- CoreBluetoothLibrary.sLib.1885
- CoreBluetoothLibrary.sOnce.1106
- CoreBluetoothLibrary.sOnce.1271
- CoreBluetoothLibrary.sOnce.1468
- CoreBluetoothLibrary.sOnce.1879
- CoreHAPLibrary.sLib.5589
- CoreHAPLibrary.sOnce.5582
- CoreServicesLibrary.sLib.13014
- CoreServicesLibrary.sLib.751
- CoreServicesLibrary.sLib.7919
- CoreServicesLibrary.sOnce.13013
- CoreServicesLibrary.sOnce.750
- CoreServicesLibrary.sOnce.7918
- CoreWLANLibrary.sLib.13811
- CoreWLANLibrary.sOnce.13801
- GCC_except_table2280
- GCC_except_table2281
- GCC_except_table2300
- GCC_except_table2332
- GCC_except_table2404
- GCC_except_table2429
- GCC_except_table2463
- GCC_except_table2467
- GCC_except_table2530
- GCC_except_table2531
- GCC_except_table2533
- GCC_except_table2534
- GCC_except_table2536
- GCC_except_table2541
- GCC_except_table2544
- GCC_except_table2547
- GCC_except_table2550
- GCC_except_table2553
- GCC_except_table2630
- GCC_except_table2945
- GCC_except_table2946
- GCC_except_table3005
- GCC_except_table3076
- GCC_except_table3080
- GCC_except_table3124
- GCC_except_table3127
- GCC_except_table3128
- GCC_except_table3130
- GCC_except_table3404
- GCC_except_table3832
- GCC_except_table4099
- GCC_except_table4107
- GCC_except_table4115
- GCC_except_table4267
- GCC_except_table4271
- GCC_except_table4273
- GCC_except_table4275
- GCC_except_table4298
- GCC_except_table4382
- GCC_except_table4383
- GCC_except_table4384
- GCC_except_table4385
- GCC_except_table4387
- GCC_except_table4389
- GCC_except_table4391
- GCC_except_table4393
- GCC_except_table4397
- GCC_except_table4399
- GCC_except_table4421
- GCC_except_table4423
- GCC_except_table4424
- GCC_except_table4425
- GCC_except_table4427
- GCC_except_table4429
- GCC_except_table4430
- GCC_except_table4431
- GCC_except_table4432
- GCC_except_table4442
- GCC_except_table4443
- GCC_except_table4446
- GCC_except_table4451
- GCC_except_table4462
- GCC_except_table4463
- GCC_except_table4464
- GCC_except_table4465
- GCC_except_table4466
- GCC_except_table4467
- GCC_except_table4468
- GCC_except_table4470
- GCC_except_table4474
- GCC_except_table5032
- GCC_except_table5037
- GCC_except_table5041
- GCC_except_table5107
- GCC_except_table5117
- GCC_except_table5126
- GCC_except_table5134
- GCC_except_table5456
- GCC_except_table5457
- GCC_except_table5470
- HAPSystemKeychainStoreFunction.5585
- IOBluetoothDeviceFunction.1839
- IOBluetoothLibrary.sLib.12937
- IOBluetoothLibrary.sLib.1842
- IOBluetoothLibrary.sOnce.12932
- IOBluetoothLibrary.sOnce.1836
- MobileDeviceLibrary.sLib.4160
- MobileDeviceLibrary.sOnce.4158
- OBJC_IVAR_$_CUNANDataSession._label
- OBJC_IVAR_$_CUNANDataSession._ucat
- OBJC_IVAR_$_CUNANPublisher._label
- OBJC_IVAR_$_CUNANPublisher._ucat
- OBJC_IVAR_$_CUNANSubscriber._label
- OBJC_IVAR_$_CUNANSubscriber._ucat
- QuartzCoreLibrary.sLib.12552
- QuartzCoreLibrary.sOnce.12550
- RapportLibrary.sLib.5605
- RapportLibrary.sOnce.5600
- WiFiAwareInternetSharingConfigurationFunction.4749
- WiFiPeerToPeerLibrary.sLib.4710
- WiFiPeerToPeerLibrary.sLib.5009
- WiFiPeerToPeerLibrary.sLib.9529
- WiFiPeerToPeerLibrary.sOnce.4705
- WiFiPeerToPeerLibrary.sOnce.5002
- WiFiPeerToPeerLibrary.sOnce.9528
- _NetTransportFinalize.11415
- _NetTransportFinalize.11423
- _NetTransportInitialize.11416
- _NetTransportInitialize.11426
- _NetTransportRead.11412
- _NetTransportRead.11425
- _NetTransportWriteV.11411
- _NetTransportWriteV.11424
- __61-[CUNANPublisher sendMessageData:endpoint:completionHandler:]_block_invoke.26
- __62-[CUNANSubscriber sendMessageData:endpoint:completionHandler:]_block_invoke_2.29
- __AccountsLibrary_block_invoke.7830
- __AppleAccountLibrary_block_invoke.7833
- __AudioUnitLibrary_block_invoke.564
- __AuthKitLibrary_block_invoke.7819
- __Block_byref_object_copy_.10057
- __Block_byref_object_copy_.10562
- __Block_byref_object_copy_.11974
- __Block_byref_object_copy_.1891
- __Block_byref_object_copy_.2484
- __Block_byref_object_copy_.2738
- __Block_byref_object_copy_.4019
- __Block_byref_object_copy_.4125
- __Block_byref_object_copy_.4711
- __Block_byref_object_copy_.5030
- __Block_byref_object_copy_.5539
- __Block_byref_object_copy_.5868
- __Block_byref_object_copy_.8618
- __Block_byref_object_dispose_.10058
- __Block_byref_object_dispose_.10563
- __Block_byref_object_dispose_.11975
- __Block_byref_object_dispose_.1892
- __Block_byref_object_dispose_.2485
- __Block_byref_object_dispose_.2739
- __Block_byref_object_dispose_.4020
- __Block_byref_object_dispose_.4126
- __Block_byref_object_dispose_.4712
- __Block_byref_object_dispose_.5031
- __Block_byref_object_dispose_.5540
- __Block_byref_object_dispose_.5869
- __Block_byref_object_dispose_.8619
- __CoreAnalyticsLibrary_block_invoke.8305
- __CoreAudioLibrary_block_invoke.549
- __CoreBluetoothLibrary_block_invoke.1111
- __CoreBluetoothLibrary_block_invoke.1276
- __CoreBluetoothLibrary_block_invoke.1476
- __CoreBluetoothLibrary_block_invoke.1884
- __CoreHAPLibrary_block_invoke.5587
- __CoreServicesLibrary_block_invoke.13017
- __CoreServicesLibrary_block_invoke.754
- __CoreServicesLibrary_block_invoke.7922
- __CoreWLANLibrary_block_invoke.13809
- __IOBluetoothLibrary_block_invoke.12935
- __IOBluetoothLibrary_block_invoke.1841
- __MobileDeviceLibrary_block_invoke.4164
- __QuartzCoreLibrary_block_invoke.12556
- __RapportLibrary_block_invoke.5604
- __WiFiPeerToPeerLibrary_block_invoke.4708
- __WiFiPeerToPeerLibrary_block_invoke.5007
- __WiFiPeerToPeerLibrary_block_invoke.9532
- ___61-[CUNANPublisher sendMessageData:endpoint:completionHandler:]_block_invoke_3
- ___62-[CUNANSubscriber sendMessageData:endpoint:completionHandler:]_block_invoke_3
- __block_descriptor_tmp.11170
- __block_descriptor_tmp.11219
- __block_descriptor_tmp.13913
- __block_descriptor_tmp.330
- __block_descriptor_tmp.42.11166
- __block_descriptor_tmp.556
- __block_descriptor_tmp.7.11224
- __block_literal_global.10092
- __block_literal_global.10143
- __block_literal_global.11002
- __block_literal_global.1107
- __block_literal_global.11154
- __block_literal_global.11229
- __block_literal_global.11757
- __block_literal_global.12551
- __block_literal_global.1272
- __block_literal_global.13802
- __block_literal_global.13916
- __block_literal_global.1469
- __block_literal_global.1627
- __block_literal_global.166
- __block_literal_global.1820
- __block_literal_global.256
- __block_literal_global.2583
- __block_literal_global.269
- __block_literal_global.2754
- __block_literal_global.3081
- __block_literal_global.327.7852
- __block_literal_global.3281
- __block_literal_global.34.12558
- __block_literal_global.377
- __block_literal_global.385.7797
- __block_literal_global.3907
- __block_literal_global.398
- __block_literal_global.40.12610
- __block_literal_global.4159
- __block_literal_global.44.11161
- __block_literal_global.44.7981
- __block_literal_global.4454
- __block_literal_global.4726
- __block_literal_global.5003
- __block_literal_global.543
- __block_literal_global.5601
- __block_literal_global.6376
- __block_literal_global.6761
- __block_literal_global.7166
- __block_literal_global.7608
- __block_literal_global.791
- __block_literal_global.7979
- __block_literal_global.8271
- __block_literal_global.846
- __block_literal_global.8866
- __block_literal_global.9181
- __block_literal_global.9493
- __block_literal_global.975
- __block_literal_global.9851
- __logger_block_invoke.11761
- __logger_block_invoke.7849
- _gLogCategory_CUNANDataSession
- _gLogCategory_CUNANPublisher
- _gLogCategory_CUNANSubscriber
- classACAccountStore.7826
- classAKAccountManager.7815
- classCALayer.12583
- classCATransaction.12600
- classCBCentralManager.1313
- classCBCentralManager.1888
- classCBPeripheralManager.1471
- classCBPeripheralManager.1880
- classCWWiFiClient.13804
- classHAPSystemKeychainStore.5583
- classIOBluetoothDevice.1837
- classWiFiAwareInternetSharingConfiguration.4747
- constantValCBManagerIsPrivilegedDaemonKey.1293
- constantValCBManagerNeedsRestrictedStateOperation.1308
- gCFArrayType.11683
- gCFBooleanType.11684
- gCFDataType.11685
- gCFDateType.11686
- gCFDictionaryType.11687
- gCFNumberType.11682
- gCFStringType.11688
- getACAccountStoreClass.7822
- getAKAccountManagerClass.7805
- getCALayerClass.12564
- getCATransactionClass.12590
- getCBCentralManagerClass.1296
- getCBCentralManagerClass.1870
- getCBManagerIsPrivilegedDaemonKey.1290
- getCBManagerNeedsRestrictedStateOperation.1297
- getCBPeripheralManagerClass.1463
- getCBPeripheralManagerClass.1872
- getCWWiFiClientClass.13786
- getHAPSystemKeychainStoreClass.5579
- getIOBluetoothDeviceClass.1819
- getWiFiAwareInternetSharingConfigurationClass.4735
- initACAccountStore.7824
- initAKAccountManager.7813
- initAMDeviceConnect.4181
- initAMDeviceCopyValue.4173
- initAMDeviceCreateCopy.4272
- initAMDeviceDisconnect.4157
- initAMDeviceStartSession.4178
- initAMDeviceStopSession.4167
- initAnalyticsSendEvent.8286
- initAudioObjectGetPropertyData.541
- initAudioUnitGetParameter.567
- initAudioUnitSetParameter.559
- initCALayer.12581
- initCATransaction.12598
- initCBCentralManager.1312
- initCBCentralManager.1887
- initCBPeripheralManager.1467
- initCBPeripheralManager.1878
- initCWWiFiClient.13800
- initHAPSystemKeychainStore.5581
- initIOBluetoothDevice.1835
- initIOBluetoothRegisterForNotifications.1876
- initIOBluetoothRemoveRegistrationForNotifications.1867
- initValCBManagerIsPrivilegedDaemonKey.1292
- initValCBManagerNeedsRestrictedStateOperation.1307
- initWiFiAwareInternetSharingConfiguration.4745
- logger.11754
- logger.7845
- sCUOSLogCreateOnce_logger.11756
- sCUOSLogCreateOnce_logger.7846
- sCUOSLogHandle_logger.11758
- sCUOSLogHandle_logger.7847
- softLinkAMDeviceConnect.4139
- softLinkAMDeviceCopyValue.4148
- softLinkAMDeviceCreateCopy.4252
- softLinkAMDeviceDisconnect.4153
- softLinkAMDeviceStartSession.4141
- softLinkAMDeviceStopSession.4152
- softLinkAnalyticsSendEvent.8283
- softLinkAudioObjectGetPropertyData.539
- softLinkAudioUnitGetParameter.555
- softLinkAudioUnitSetParameter.557
- softLinkIOBluetoothRegisterForNotifications.1874
- softLinkIOBluetoothRemoveRegistrationForNotifications.1853
CStrings:
+ "\x01\x11(\""
+ "\x01\x12\x11"
+ "\x01\x12."
+ "\x01\xa2\x19"
+ "### SendMessage failed: %@"
+ "### SendMessage failed: EP %@, Data %@, %@"
+ "### WFA DataSession confirmed for existing session: %@"
+ "### WFA DataSession confirmed missing identifier"
+ "### WFA DataSession start failed: %@, %@"
+ "### WFA DataSession terminated missing identifier: %@"
+ "### WFA DataSession terminated untracked: '%@', %@, %@"
+ "### WFA discovery result missing identifier"
+ "### WFA lost result missing identifier"
+ "### WFAPublisher start failed: '%@', %@"
+ "### WFASubscriber start failed: '%@', %@"
+ "### tryPairingPassword with no input handler"
+ "%##{txt}"
+ "%.1H"
+ "%{txt}"
+ "(no handler)"
+ ", IP %@"
+ "/AppleInternal/Library/BuildRoots/fa4539c7-059d-11f0-b0c1-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/CoreUtils/CoreUtils/TestUtils.c"
+ "@24@0:8r*16"
+ "@32@0:8r^v16Q24"
+ "@40@0:8@16Q24@32"
+ "Activate '%@', %@"
+ "Activate: endpoint=%@, controlFlags=%@, trafficFlags=%@, pair=%s"
+ "Activate: serviceType=%@, name='%@', port=%d, trafficFlags=%@, customData=%@, textInfo=%@, pair=%s"
+ "B48@0:8@16*24Q32^@40"
+ "CID 0x%08X"
+ "CUFile"
+ "CUFile closed"
+ "CUFile deleted"
+ "CUFileReadRequest"
+ "CUFileWriteRequest"
+ "CUNANPairingPromptInfo"
+ "CUNANPairingShowInfo"
+ "CUSPAKECommon"
+ "CUSPAKEM1"
+ "CUSPAKEM2"
+ "CUSPAKEM3"
+ "CUSPAKEProver"
+ "CUSPAKEVerifier"
+ "Create parent failed"
+ "DataSession ended: %@"
+ "DataSession started: %@"
+ "Endpoint changed: %@, %@"
+ "Endpoint found: %@"
+ "Endpoint lost: %@"
+ "F_NOCACHE failed"
+ "F_PREALLOCATE failed"
+ "F_RDAHEAD failed"
+ "F_SINGLE_WRITER failed"
+ "Get parent URL failed"
+ "No path"
+ "PairSetup-SPAKE2-Context"
+ "PairSetup-SPAKE2-ProverID"
+ "PairSetup-SPAKE2-Salt"
+ "PairSetup-SPAKE2-VerifierID"
+ "PairingPrompt: %@ %s"
+ "PairingShow: %@"
+ "SendMessage completed: EP %@, Data %@"
+ "SendMessage start: EP %@, Data %@"
+ "T@\"NSData\",C,N,V_confirmPData"
+ "T@\"NSData\",C,N,V_confirmVData"
+ "T@\"NSData\",C,N,V_sharePData"
+ "T@\"NSData\",C,N,V_shareVData"
+ "T@\"NSDictionary\",R,C,N,V_textInfo"
+ "T@\"NSString\",R,C,N,V_pinCode"
+ "T@?,C,N,V_pairingPromptHandler"
+ "T@?,C,N,V_pairingShowHandler"
+ "TB,N,V_wfaPairingCacheEnabled"
+ "TQ,N,V_length"
+ "TQ,N,V_offset"
+ "Tq,N,V_wfaPairingMethod"
+ "URLByDeletingLastPathComponent"
+ "WFA DataSession indicated: '%@', %@"
+ "WFA DataSession request started: %@"
+ "WFA DataSession terminate completed: %@"
+ "WFA DataSession terminate start"
+ "WFA DataSession terminated: %@, %@"
+ "WFA DataSession terminated: '%@', %@, %@"
+ "WFA discovery result: PA <%@>, PI %u, SV '%@', SI <%@>"
+ "WFA lost result missing not found: %@"
+ "WFA lost result: PA <%@>, PI %u"
+ "WFAPublisher restarting after unexpected termination"
+ "WFAPublisher started: '%@'"
+ "WFAPublisher terminated: '%@', %s"
+ "WFASubscriber restarting after unexpected termination"
+ "WFASubscriber started: '%@'"
+ "WFASubscriber terminated: '%@', %s"
+ "WiFiAwareDataSessionPairingDelegate"
+ "WiFiAwarePairingConfiguration"
+ "WiFiAwarePublishDatapathSecurityConfiguration"
+ "WiFiAwarePublisherPairingDelegate"
+ "^{ccspake_ctx=^{ccspake_cp}^{ccspake_mac}^{ccrng_state}BQ[20C]C[26{ccdigest_ctx=[1C]}][64C][0Q]}"
+ "_completeReadRequest:data:error:"
+ "_confirmPData"
+ "_confirmVData"
+ "_newZeroingDataWithBytes:length:"
+ "_openForReadingAndReturnError:"
+ "_openForWritingAndReturnError:"
+ "_pairingPromptHandler"
+ "_pairingRequestStartedForDataSession:pinCodeInputCompletionHandler:"
+ "_pairingShowHandler"
+ "_passwordData"
+ "_pinCode"
+ "_pinCodeInputCompletionHandler"
+ "_processRead:"
+ "_processWrite:"
+ "_readQueue"
+ "_readRequest:"
+ "_sessionKey"
+ "_sharePData"
+ "_shareVData"
+ "_spakeContext"
+ "_totalLength"
+ "_url"
+ "_wfaPairingCacheEnabled"
+ "_wfaPairingMethod"
+ "_writeQueue"
+ "_writeRequest:"
+ "bad scrypt storage size: %lld bytes"
+ "ccscrypt failed: %d"
+ "ccspake verify failed: %d"
+ "ccspake_ctx malloc failed"
+ "ccspake_generate_L"
+ "ccspake_kex_generate failed: %d"
+ "ccspake_kex_process failed: %d"
+ "ccspake_mac_compute failed: %d"
+ "ccspake_prover_initialize failed: %d"
+ "ccspake_reduce_w failed w0: %d"
+ "ccspake_reduce_w failed w1: %d"
+ "closeWithCompletionHandler:"
+ "confirmP"
+ "confirmPData"
+ "confirmV"
+ "confirmVData"
+ "createDirectoryAtURL:withIntermediateDirectories:attributes:error:"
+ "dictionaryRepresentation"
+ "finishWithM3:error:"
+ "generate session key failed"
+ "generateM1AndReturnError:"
+ "generateM2WithM1:error:"
+ "generateM3WithM2:error:"
+ "get confirmP failed: %d"
+ "get confirmV failed: %d"
+ "get sharePData failed: %d"
+ "get shareV failed: %d"
+ "i24@0:8^@16"
+ "initForReadingFromURL:dispatchQueue:"
+ "initForWritingToURL:dispatchQueue:"
+ "initForWritingToURL:totalLength:dispatchQueue:"
+ "initWithDataSession:"
+ "initWithPairingConfiguration:usingPairingDelegate:"
+ "initWithPasswordCString:"
+ "initWithPasswordPtr:passwordLength:"
+ "initWithPasswordString:"
+ "initWithSubscriberInfo:pinCode:"
+ "initWithSupportedPairSetupMethods:pairingCachingEnabled:"
+ "lseek failed"
+ "malloc failed: %zu bytes"
+ "name=%@"
+ "no session key"
+ "no spake context"
+ "not prepared for reading"
+ "not prepared for writing"
+ "offset"
+ "open failed"
+ "openWithCompletionHandler:"
+ "pairingPromptHandler"
+ "pairingRequestIndicatedForPublisher:bySubscriber:usingNFCTag:"
+ "pairingRequestIndicatedForPublisher:bySubscriber:usingPINCode:"
+ "pairingRequestIndicatedForPublisher:bySubscriber:usingPassphrase:"
+ "pairingRequestIndicatedForPublisher:bySubscriber:usingQRCodeInformation:"
+ "pairingRequestStartedForDataSession:nfcTagScannedCompletionHandler:"
+ "pairingRequestStartedForDataSession:passphraseInputCompletionHandler:"
+ "pairingRequestStartedForDataSession:pinCodeInputCompletionHandler:"
+ "pairingRequestStartedForDataSession:qrCodeScannedCompletionHandler:"
+ "pairingShowHandler"
+ "pinCode"
+ "pinCode=%@"
+ "re-open after close not allowed"
+ "read failed"
+ "readLength:completionHandler:"
+ "readLength:offset:completionHandler:"
+ "scrypt storage malloc failed: %lld bytes"
+ "scryptWithPasswordData:outputPtr:outputLen:error:"
+ "setConfirmPData:"
+ "setConfirmVData:"
+ "setOffset:"
+ "setPairingCachingEnabled:"
+ "setPairingMethod:"
+ "setPairingPromptHandler:"
+ "setPairingShowHandler:"
+ "setSharePData:"
+ "setShareVData:"
+ "setWfaPairingCacheEnabled:"
+ "setWfaPairingMethod:"
+ "shareP"
+ "sharePData"
+ "shareV"
+ "shareVData"
+ "super init failed"
+ "textInfo=%@"
+ "tryPairingPassword:"
+ "tryPairingPassword: length=%d"
+ "v32@0:8@\"WiFiAwareDataSession\"16@?<v@?@\"NSData\">24"
+ "v32@0:8@\"WiFiAwareDataSession\"16@?<v@?@\"NSString\">24"
+ "v40@0:8@\"WiFiAwarePublisher\"16@\"WiFiAwarePublishServiceSpecificInfo\"24@\"NSData\"32"
+ "v40@0:8@\"WiFiAwarePublisher\"16@\"WiFiAwarePublishServiceSpecificInfo\"24@\"NSString\"32"
+ "v40@0:8Q16Q24@?32"
+ "wfaPairingCacheEnabled"
+ "wfaPairingMethod"
+ "write failed"
+ "writeData:completionHandler:"
+ "writeData:offset:completionHandler:"
- "\x01\x11\x11."
- "\x01H\x12"
- "\x01\xb2\x1a"
- "### SendMessage failed: %{error}"
- "### SendMessage failed: EP %@, Data %.12@, %{error}"
- "### WFA DataSession confirmed for existing session: %@\n"
- "### WFA DataSession confirmed missing identifier\n"
- "### WFA DataSession start failed: %@, %#m\n"
- "### WFA DataSession terminated missing identifier: %#m\n"
- "### WFA DataSession terminated untracked: '%@', %@, %#m\n"
- "### WFA discovery result missing identifier\n"
- "### WFA lost result missing identifier\n"
- "### WFAPublisher start failed: '%@', %#m\n"
- "### WFASubscriber start failed: '%@', %#m\n"
- ", IP %##a"
- "-[CUNANDataSession _activateWithCompletion:]"
- "-[CUNANDataSession _invalidate]"
- "-[CUNANDataSession _invalidated]"
- "-[CUNANDataSession _terminateServerDataSession]"
- "-[CUNANDataSession _terminateServerDataSession]_block_invoke_2"
- "-[CUNANDataSession dataSession:confirmedForPeerDataAddress:serviceSpecificInfo:]_block_invoke"
- "-[CUNANDataSession dataSession:failedToStartWithError:]_block_invoke"
- "-[CUNANDataSession dataSession:terminatedWithReason:]_block_invoke"
- "-[CUNANDataSession dataSessionRequestStarted:]_block_invoke"
- "-[CUNANDataSession reportIssue:]_block_invoke"
- "-[CUNANPublisher _activateWithCompletion:]"
- "-[CUNANPublisher _invalidate]"
- "-[CUNANPublisher _invalidated]"
- "-[CUNANPublisher _publisher:dataConfirmedForHandle:localInterfaceIndex:serviceSpecificInfo:]"
- "-[CUNANPublisher _updateServiceSpecificInfo]"
- "-[CUNANPublisher _updateServiceSpecificInfo]_block_invoke"
- "-[CUNANPublisher publisher:dataIndicatedForHandle:serviceSpecificInfo:]"
- "-[CUNANPublisher publisher:dataTerminatedForHandle:reason:]_block_invoke"
- "-[CUNANPublisher publisher:failedToStartWithError:]_block_invoke"
- "-[CUNANPublisher publisher:receivedMessage:fromSubscriberID:subscriberAddress:]_block_invoke"
- "-[CUNANPublisher publisher:terminatedWithReason:]_block_invoke"
- "-[CUNANPublisher publisherStarted:]_block_invoke"
- "-[CUNANPublisher sendMessageData:endpoint:completionHandler:]_block_invoke"
- "-[CUNANPublisher sendMessageData:endpoint:completionHandler:]_block_invoke_3"
- "-[CUNANSubscriber _activateWithCompletion:]"
- "-[CUNANSubscriber _invalidate]"
- "-[CUNANSubscriber _invalidated]"
- "-[CUNANSubscriber _lostAllEndpoints]_block_invoke"
- "-[CUNANSubscriber _subscriber:lostDiscoveryResultForPublishID:address:]"
- "-[CUNANSubscriber _subscriber:receivedDiscoveryResult:]"
- "-[CUNANSubscriber reportMockEndpointFound:]_block_invoke"
- "-[CUNANSubscriber reportMockEndpointLost:]_block_invoke"
- "-[CUNANSubscriber sendMessageData:endpoint:completionHandler:]_block_invoke"
- "-[CUNANSubscriber sendMessageData:endpoint:completionHandler:]_block_invoke_2"
- "-[CUNANSubscriber sendMessageData:endpoint:completionHandler:]_block_invoke_3"
- "-[CUNANSubscriber subscriber:failedToStartWithError:]_block_invoke"
- "-[CUNANSubscriber subscriber:receivedMessage:fromPublishID:address:]_block_invoke"
- "-[CUNANSubscriber subscriber:terminatedWithReason:]_block_invoke"
- "-[CUNANSubscriber subscriberStarted:]_block_invoke"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CoreUtils/CoreUtils/TestUtils.c"
- "Activate '%@', %#{flags}\n"
- "Activate: endpoint=%@, controlFlags=%@, trafficFlags=%@"
- "Activate: serviceType=%@, name='%@', port=%d, trafficFlags=%@, customData=%@, textInfo=%@"
- "DataSession ended: %@\n"
- "DataSession started: %@\n"
- "Endpoint changed: %@, %#{flags}\n"
- "Endpoint found: %@\n"
- "Endpoint lost: %@\n"
- "SendMessage completed: EP %@, Data %.12@"
- "SendMessage start: EP %@, Data %.12@"
- "WFA DataSession indicated: '%@', %@\n"
- "WFA DataSession request started: %@\n"
- "WFA DataSession terminate completed: %#m\n"
- "WFA DataSession terminate start\n"
- "WFA DataSession terminated: %@, %#m\n"
- "WFA DataSession terminated: '%@', %@, %#m\n"
- "WFA discovery result: PA <%@>, PI %u, SV '%@', SI <%@>\n"
- "WFA lost result missing not found: %@\n"
- "WFA lost result: PA <%@>, PI %u\n"
- "WFAPublisher restarting after unexpected termination\n"
- "WFAPublisher started: '%@'\n"
- "WFAPublisher terminated: '%@', %s\n"
- "WFASubscriber restarting after unexpected termination\n"
- "WFASubscriber started: '%@'\n"
- "WFASubscriber terminated: '%@', %s\n"

```
