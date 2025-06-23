## CoreUtils

> `/System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils`

```diff

-790.18.0.0.0
-  __TEXT.__text: 0x11dba4
-  __TEXT.__auth_stubs: 0x3040
-  __TEXT.__objc_methlist: 0x9ce0
-  __TEXT.__cstring: 0x23017
+800.4.0.0.0
+  __TEXT.__text: 0x11e158
+  __TEXT.__auth_stubs: 0x3050
+  __TEXT.__objc_methlist: 0x9d80
+  __TEXT.__cstring: 0x23049
   __TEXT.__const: 0x2380
   __TEXT.__gcc_except_tab: 0x1d68
-  __TEXT.__oslogstring: 0xd99
-  __TEXT.__unwind_info: 0x3a28
+  __TEXT.__oslogstring: 0xd90
+  __TEXT.__unwind_info: 0x3a40
   __TEXT.__eh_frame: 0x50
-  __TEXT.__objc_classname: 0xcd1
-  __TEXT.__objc_methname: 0x15cc5
-  __TEXT.__objc_methtype: 0x467a
-  __TEXT.__objc_stubs: 0xa400
-  __DATA_CONST.__got: 0x688
-  __DATA_CONST.__const: 0x29e8
+  __TEXT.__objc_classname: 0xcd4
+  __TEXT.__objc_methname: 0x15f54
+  __TEXT.__objc_methtype: 0x46c5
+  __TEXT.__objc_stubs: 0xa4c0
+  __DATA_CONST.__got: 0x690
+  __DATA_CONST.__const: 0x2a28
   __DATA_CONST.__objc_classlist: 0x360
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x148
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4ca0
+  __DATA_CONST.__objc_selrefs: 0x4d20
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x248
   __DATA_CONST.__objc_arraydata: 0x8
-  __AUTH_CONST.__auth_got: 0x1830
-  __AUTH_CONST.__const: 0x27f0
+  __AUTH_CONST.__auth_got: 0x1838
+  __AUTH_CONST.__const: 0x2830
   __AUTH_CONST.__cfstring: 0x4480
-  __AUTH_CONST.__objc_const: 0x13cb8
+  __AUTH_CONST.__objc_const: 0x13d78
   __AUTH_CONST.__objc_intobj: 0x258
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x1f40
   __AUTH.__data: 0xb28
-  __DATA.__objc_ivar: 0x153c
+  __DATA.__objc_ivar: 0x154c
   __DATA.__data: 0x31b0
-  __DATA.__bss: 0x1330
+  __DATA.__bss: 0x1350
   __DATA.__common: 0x2a
   __DATA_DIRTY.__objc_data: 0x280
   __DATA_DIRTY.__data: 0x178

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: D9F77508-67B1-3679-AC22-F24DB7909F57
-  Functions: 5834
-  Symbols:   16858
-  CStrings:  10198
+  UUID: 30E3F8F3-24B7-3BBB-ABE0-F175A0FE9F39
+  Functions: 5853
+  Symbols:   16914
+  CStrings:  10228
 
Symbols:
+ +[CUFile realPath:dispatchQueue:completionHandler:]
+ +[CUFile realPath:error:]
+ +[CUPairingManager copySystemPairingIdentifierWithFlags:error:]
+ -[CUFile _getLengthWithCompletionHandler:]
+ -[CUFile getLengthWithCompletionHandler:]
+ -[CUNANDataSession setWfaConnectionMode:]
+ -[CUNANDataSession setWfaPairingMetadata:]
+ -[CUNANDataSession setWfaServiceSpecificInfo:]
+ -[CUNANDataSession wfaConnectionMode]
+ -[CUNANDataSession wfaPairingMetadata]
+ -[CUNANDataSession wfaServiceSpecificInfo]
+ -[CUNANSubscriber setWfaDiscoveryMode:]
+ -[CUNANSubscriber wfaDiscoveryMode]
+ GCC_except_table2363
+ GCC_except_table2364
+ GCC_except_table2384
+ GCC_except_table2422
+ GCC_except_table2497
+ GCC_except_table2521
+ GCC_except_table2555
+ GCC_except_table2559
+ GCC_except_table2622
+ GCC_except_table2623
+ GCC_except_table2626
+ GCC_except_table2633
+ GCC_except_table2636
+ GCC_except_table2639
+ GCC_except_table2642
+ GCC_except_table2645
+ GCC_except_table2652
+ GCC_except_table2655
+ GCC_except_table2724
+ GCC_except_table3042
+ GCC_except_table3043
+ GCC_except_table3131
+ GCC_except_table3153
+ GCC_except_table3187
+ GCC_except_table3191
+ GCC_except_table3235
+ GCC_except_table3238
+ GCC_except_table3239
+ GCC_except_table3241
+ GCC_except_table3538
+ GCC_except_table3954
+ GCC_except_table4204
+ GCC_except_table4259
+ GCC_except_table4266
+ GCC_except_table4274
+ GCC_except_table4426
+ GCC_except_table4430
+ GCC_except_table4432
+ GCC_except_table4434
+ GCC_except_table4457
+ GCC_except_table4542
+ GCC_except_table4544
+ GCC_except_table4546
+ GCC_except_table4548
+ GCC_except_table4550
+ GCC_except_table4552
+ GCC_except_table4556
+ GCC_except_table4558
+ GCC_except_table4583
+ GCC_except_table4584
+ GCC_except_table4586
+ GCC_except_table4587
+ GCC_except_table4588
+ GCC_except_table4590
+ GCC_except_table4616
+ GCC_except_table4620
+ GCC_except_table4622
+ GCC_except_table4623
+ GCC_except_table4624
+ GCC_except_table4626
+ GCC_except_table4627
+ GCC_except_table4628
+ GCC_except_table4630
+ GCC_except_table5271
+ GCC_except_table5276
+ GCC_except_table5280
+ GCC_except_table5347
+ GCC_except_table5367
+ GCC_except_table5376
+ GCC_except_table5697
+ GCC_except_table5698
+ GCC_except_table5711
+ _ACAccountStoreFunction.8200
+ _AKAccountManagerFunction.8189
+ _AVAudioSessionFunction.9457
+ _AVFoundationLibrary.sLib.9461
+ _AVFoundationLibrary.sOnce.9453
+ _AccountsLibrary.sLib.8203
+ _AccountsLibrary.sOnce.8197
+ _AppleAccountLibrary.sLib.8206
+ _AppleAccountLibrary.sOnce.8193
+ _AuthKitLibrary.sLib.8192
+ _AuthKitLibrary.sOnce.8186
+ _CALayerFunction.13213
+ _CATransactionFunction.13230
+ _CUNextIDDecimal32
+ _CUNextIDDecimal32.sNextID
+ _CUNextIDDecimal32.sOnce
+ _CUNextIDDecimal64
+ _CUNextIDDecimal64.sNextID
+ _CUNextIDDecimal64.sOnce
+ _CoreAnalyticsLibrary.sLib.8646
+ _CoreAnalyticsLibrary.sOnce.8644
+ _CoreHAPLibrary.sLib.5787
+ _CoreHAPLibrary.sOnce.5781
+ _HAPSystemKeychainStoreFunction.5784
+ _MobileCoreServicesLibrary.sLib.13620
+ _MobileCoreServicesLibrary.sOnce.13619
+ _OBJC_IVAR_$_CUNANDataSession._wfaConnectionMode
+ _OBJC_IVAR_$_CUNANDataSession._wfaPairingMetadata
+ _OBJC_IVAR_$_CUNANDataSession._wfaServiceSpecificInfo
+ _OBJC_IVAR_$_CUNANSubscriber._wfaDiscoveryMode
+ _QuartzCoreLibrary.sLib.13178
+ _QuartzCoreLibrary.sOnce.13176
+ _RapportLibrary.sLib.5803
+ _RapportLibrary.sOnce.5798
+ _VideoToolboxLibrary.sLib.13185
+ _VideoToolboxLibrary.sOnce.13184
+ _WiFiAwareInternetSharingConfigurationFunction.4931
+ _WiFiPeerToPeerLibrary.sLib.4884
+ _WiFiPeerToPeerLibrary.sLib.5206
+ _WiFiPeerToPeerLibrary.sLib.9889
+ _WiFiPeerToPeerLibrary.sOnce.4878
+ _WiFiPeerToPeerLibrary.sOnce.5201
+ _WiFiPeerToPeerLibrary.sOnce.9888
+ __NetTransportFinalize.12004
+ __NetTransportFinalize.12012
+ __NetTransportInitialize.12005
+ __NetTransportInitialize.12015
+ __NetTransportRead.12001
+ __NetTransportRead.12014
+ __NetTransportWriteV.12000
+ __NetTransportWriteV.12013
+ __OBJC_$_CLASS_METHODS_CUFile
+ ___41-[CUFile getLengthWithCompletionHandler:]_block_invoke
+ ___51+[CUFile realPath:dispatchQueue:completionHandler:]_block_invoke
+ ___AVFoundationLibrary_block_invoke.9459
+ ___AccountsLibrary_block_invoke.8202
+ ___AppleAccountLibrary_block_invoke.8205
+ ___AuthKitLibrary_block_invoke.8191
+ ___Block_byref_object_copy_.10438
+ ___Block_byref_object_copy_.10944
+ ___Block_byref_object_copy_.12568
+ ___Block_byref_object_copy_.4886
+ ___Block_byref_object_copy_.5229
+ ___Block_byref_object_copy_.5745
+ ___Block_byref_object_copy_.6070
+ ___Block_byref_object_copy_.8991
+ ___Block_byref_object_dispose_.10439
+ ___Block_byref_object_dispose_.10945
+ ___Block_byref_object_dispose_.12569
+ ___Block_byref_object_dispose_.4887
+ ___Block_byref_object_dispose_.5230
+ ___Block_byref_object_dispose_.5746
+ ___Block_byref_object_dispose_.6071
+ ___Block_byref_object_dispose_.8992
+ ___CUNextIDDecimal32_block_invoke
+ ___CUNextIDDecimal64_block_invoke
+ ___CoreAnalyticsLibrary_block_invoke.8680
+ ___CoreHAPLibrary_block_invoke.5786
+ ___MobileCoreServicesLibrary_block_invoke.13623
+ ___QuartzCoreLibrary_block_invoke.13182
+ ___RapportLibrary_block_invoke.5802
+ ___VideoToolboxLibrary_block_invoke.13188
+ ___WiFiPeerToPeerLibrary_block_invoke.4882
+ ___WiFiPeerToPeerLibrary_block_invoke.5204
+ ___WiFiPeerToPeerLibrary_block_invoke.9892
+ ___block_descriptor_tmp.11650
+ ___block_descriptor_tmp.11700
+ ___block_descriptor_tmp.14608
+ ___block_descriptor_tmp.22
+ ___block_descriptor_tmp.3.14618
+ ___block_descriptor_tmp.6
+ ___block_descriptor_tmp.7.14613
+ ___block_descriptor_tmp.9
+ ___block_literal_global.10237
+ ___block_literal_global.10471
+ ___block_literal_global.11
+ ___block_literal_global.11487
+ ___block_literal_global.11637
+ ___block_literal_global.11698
+ ___block_literal_global.12340
+ ___block_literal_global.13177
+ ___block_literal_global.13539
+ ___block_literal_global.141.8310
+ ___block_literal_global.14463
+ ___block_literal_global.14611
+ ___block_literal_global.155.8293
+ ___block_literal_global.24
+ ___block_literal_global.264.10924
+ ___block_literal_global.268.8227
+ ___block_literal_global.271.4606
+ ___block_literal_global.271.8228
+ ___block_literal_global.276.8229
+ ___block_literal_global.288.9900
+ ___block_literal_global.29.8341
+ ___block_literal_global.300.9894
+ ___block_literal_global.308.9866
+ ___block_literal_global.33.8342
+ ___block_literal_global.375.8147
+ ___block_literal_global.407.8128
+ ___block_literal_global.41.8343
+ ___block_literal_global.413.8124
+ ___block_literal_global.4584
+ ___block_literal_global.47.8345
+ ___block_literal_global.4900
+ ___block_literal_global.5120
+ ___block_literal_global.52.8347
+ ___block_literal_global.5799
+ ___block_literal_global.58.8348
+ ___block_literal_global.6564
+ ___block_literal_global.7002
+ ___block_literal_global.7286
+ ___block_literal_global.7495
+ ___block_literal_global.7961
+ ___block_literal_global.8
+ ___block_literal_global.8340
+ ___block_literal_global.8645
+ ___block_literal_global.9242
+ ___block_literal_global.9473
+ ___block_literal_global.9639
+ ___block_literal_global.9905
+ ___logger_block_invoke.12344
+ ___logger_block_invoke.14467
+ ___logger_block_invoke.4860
+ ___logger_block_invoke.5124
+ ___logger_block_invoke.7499
+ ___logger_block_invoke.8223
+ ___logger_block_invoke.9846
+ _arc4random_uniform
+ _classACAccountStore.8198
+ _classAKAccountManager.8187
+ _classAVAudioSession.9455
+ _classCALayer.13211
+ _classCATransaction.13228
+ _classHAPSystemKeychainStore.5782
+ _classWiFiAwareInternetSharingConfiguration.4929
+ _gCFArrayType.12266
+ _gCFBooleanType.12267
+ _gCFDataType.12268
+ _gCFDateType.12269
+ _gCFDictionaryType.12270
+ _gCFNumberType.12265
+ _gCFStringType.12271
+ _getACAccountStoreClass.8194
+ _getAKAccountManagerClass.8177
+ _getAVAudioSessionClass.9441
+ _getCALayerClass.13192
+ _getCATransactionClass.13218
+ _getHAPSystemKeychainStoreClass.5778
+ _getWiFiAwareInternetSharingConfigurationClass.4910
+ _initACAccountStore.8196
+ _initAKAccountManager.8185
+ _initAVAudioSession.9452
+ _initAnalyticsSendEvent.8662
+ _initCALayer.13209
+ _initCATransaction.13226
+ _initHAPSystemKeychainStore.5780
+ _initWiFiAwareInternetSharingConfiguration.4927
+ _logger.12336
+ _logger.14386
+ _logger.4856
+ _logger.5117
+ _logger.7492
+ _logger.8218
+ _logger.9841
+ _objc_msgSend$_getLengthWithCompletionHandler:
+ _objc_msgSend$copySystemPairingIdentifierWithFlags:error:
+ _objc_msgSend$realPath:error:
+ _objc_msgSend$setConnectionMode:
+ _objc_msgSend$setDiscoveryMode:
+ _objc_msgSend$setPairingMetadata:
+ _sCUOSLogCreateOnce_logger.12339
+ _sCUOSLogCreateOnce_logger.14462
+ _sCUOSLogCreateOnce_logger.4857
+ _sCUOSLogCreateOnce_logger.5119
+ _sCUOSLogCreateOnce_logger.7494
+ _sCUOSLogCreateOnce_logger.8220
+ _sCUOSLogCreateOnce_logger.9843
+ _sCUOSLogHandle_logger.12341
+ _sCUOSLogHandle_logger.14464
+ _sCUOSLogHandle_logger.4858
+ _sCUOSLogHandle_logger.5121
+ _sCUOSLogHandle_logger.7496
+ _sCUOSLogHandle_logger.8221
+ _sCUOSLogHandle_logger.9844
+ _softLinkAnalyticsSendEvent.8657
- GCC_except_table2357
- GCC_except_table2358
- GCC_except_table2378
- GCC_except_table2416
- GCC_except_table2489
- GCC_except_table2513
- GCC_except_table2547
- GCC_except_table2551
- GCC_except_table2614
- GCC_except_table2615
- GCC_except_table2617
- GCC_except_table2618
- GCC_except_table2620
- GCC_except_table2631
- GCC_except_table2634
- GCC_except_table2637
- GCC_except_table2644
- GCC_except_table2647
- GCC_except_table2716
- GCC_except_table3033
- GCC_except_table3034
- GCC_except_table3122
- GCC_except_table3144
- GCC_except_table3178
- GCC_except_table3182
- GCC_except_table3226
- GCC_except_table3229
- GCC_except_table3230
- GCC_except_table3232
- GCC_except_table3529
- GCC_except_table3945
- GCC_except_table4195
- GCC_except_table4250
- GCC_except_table4257
- GCC_except_table4265
- GCC_except_table4417
- GCC_except_table4421
- GCC_except_table4423
- GCC_except_table4425
- GCC_except_table4448
- GCC_except_table4532
- GCC_except_table4533
- GCC_except_table4534
- GCC_except_table4535
- GCC_except_table4537
- GCC_except_table4539
- GCC_except_table4547
- GCC_except_table4549
- GCC_except_table4561
- GCC_except_table4568
- GCC_except_table4571
- GCC_except_table4573
- GCC_except_table4574
- GCC_except_table4575
- GCC_except_table4578
- GCC_except_table4581
- GCC_except_table4592
- GCC_except_table4595
- GCC_except_table4596
- GCC_except_table4597
- GCC_except_table4599
- GCC_except_table4603
- GCC_except_table4611
- GCC_except_table5252
- GCC_except_table5257
- GCC_except_table5261
- GCC_except_table5328
- GCC_except_table5338
- GCC_except_table5348
- GCC_except_table5678
- GCC_except_table5679
- GCC_except_table5692
- _ACAccountStoreFunction.8170
- _AKAccountManagerFunction.8159
- _AVAudioSessionFunction.9427
- _AVFoundationLibrary.sLib.9431
- _AVFoundationLibrary.sOnce.9423
- _AccountsLibrary.sLib.8173
- _AccountsLibrary.sOnce.8167
- _AppleAccountLibrary.sLib.8176
- _AppleAccountLibrary.sOnce.8163
- _AuthKitLibrary.sLib.8162
- _AuthKitLibrary.sOnce.8156
- _CALayerFunction.13176
- _CATransactionFunction.13193
- _CoreAnalyticsLibrary.sLib.8615
- _CoreAnalyticsLibrary.sOnce.8613
- _CoreHAPLibrary.sLib.5764
- _CoreHAPLibrary.sOnce.5758
- _HAPSystemKeychainStoreFunction.5761
- _MobileCoreServicesLibrary.sLib.13583
- _MobileCoreServicesLibrary.sOnce.13582
- _QuartzCoreLibrary.sLib.13141
- _QuartzCoreLibrary.sOnce.13139
- _RapportLibrary.sLib.5780
- _RapportLibrary.sOnce.5775
- _VideoToolboxLibrary.sLib.13148
- _VideoToolboxLibrary.sOnce.13147
- _WiFiAwareInternetSharingConfigurationFunction.4913
- _WiFiPeerToPeerLibrary.sLib.4866
- _WiFiPeerToPeerLibrary.sLib.5184
- _WiFiPeerToPeerLibrary.sLib.9859
- _WiFiPeerToPeerLibrary.sOnce.4860
- _WiFiPeerToPeerLibrary.sOnce.5177
- _WiFiPeerToPeerLibrary.sOnce.9858
- __NetTransportFinalize.11970
- __NetTransportFinalize.11978
- __NetTransportInitialize.11971
- __NetTransportInitialize.11981
- __NetTransportRead.11967
- __NetTransportRead.11980
- __NetTransportWriteV.11966
- __NetTransportWriteV.11979
- ___AVFoundationLibrary_block_invoke.9429
- ___AccountsLibrary_block_invoke.8172
- ___AppleAccountLibrary_block_invoke.8175
- ___AuthKitLibrary_block_invoke.8161
- ___Block_byref_object_copy_.10408
- ___Block_byref_object_copy_.10915
- ___Block_byref_object_copy_.12535
- ___Block_byref_object_copy_.4868
- ___Block_byref_object_copy_.5207
- ___Block_byref_object_copy_.5722
- ___Block_byref_object_copy_.6049
- ___Block_byref_object_copy_.8960
- ___Block_byref_object_dispose_.10409
- ___Block_byref_object_dispose_.10916
- ___Block_byref_object_dispose_.12536
- ___Block_byref_object_dispose_.4869
- ___Block_byref_object_dispose_.5208
- ___Block_byref_object_dispose_.5723
- ___Block_byref_object_dispose_.6050
- ___Block_byref_object_dispose_.8961
- ___CoreAnalyticsLibrary_block_invoke.8649
- ___CoreHAPLibrary_block_invoke.5763
- ___MobileCoreServicesLibrary_block_invoke.13586
- ___QuartzCoreLibrary_block_invoke.13145
- ___RapportLibrary_block_invoke.5779
- ___VideoToolboxLibrary_block_invoke.13151
- ___WiFiPeerToPeerLibrary_block_invoke.4864
- ___WiFiPeerToPeerLibrary_block_invoke.5182
- ___WiFiPeerToPeerLibrary_block_invoke.9862
- ___block_descriptor_tmp.11621
- ___block_descriptor_tmp.11671
- ___block_descriptor_tmp.14577
- ___block_descriptor_tmp.16
- ___block_descriptor_tmp.3.14587
- ___block_descriptor_tmp.7.14582
- ___block_literal_global.10207
- ___block_literal_global.10441
- ___block_literal_global.11458
- ___block_literal_global.11608
- ___block_literal_global.11669
- ___block_literal_global.12308
- ___block_literal_global.13140
- ___block_literal_global.13502
- ___block_literal_global.141.8279
- ___block_literal_global.14428
- ___block_literal_global.14580
- ___block_literal_global.155.8262
- ___block_literal_global.18
- ___block_literal_global.254.8202
- ___block_literal_global.264.10894
- ___block_literal_global.268.5178
- ___block_literal_global.268.8197
- ___block_literal_global.271.8198
- ___block_literal_global.288.9870
- ___block_literal_global.29.8310
- ___block_literal_global.300.9864
- ___block_literal_global.308.9836
- ___block_literal_global.33.8311
- ___block_literal_global.375.8117
- ___block_literal_global.407.8098
- ___block_literal_global.41.8312
- ___block_literal_global.413.8094
- ___block_literal_global.4568
- ___block_literal_global.47.8314
- ___block_literal_global.4882
- ___block_literal_global.5094
- ___block_literal_global.52.8316
- ___block_literal_global.5776
- ___block_literal_global.58.8317
- ___block_literal_global.6538
- ___block_literal_global.6975
- ___block_literal_global.7257
- ___block_literal_global.7465
- ___block_literal_global.7931
- ___block_literal_global.8309
- ___block_literal_global.8614
- ___block_literal_global.9212
- ___block_literal_global.9443
- ___block_literal_global.9609
- ___block_literal_global.9875
- ___logger_block_invoke.12312
- ___logger_block_invoke.14432
- ___logger_block_invoke.4842
- ___logger_block_invoke.5098
- ___logger_block_invoke.7469
- ___logger_block_invoke.8193
- ___logger_block_invoke.9816
- _classACAccountStore.8168
- _classAKAccountManager.8157
- _classAVAudioSession.9425
- _classCALayer.13174
- _classCATransaction.13191
- _classHAPSystemKeychainStore.5759
- _classWiFiAwareInternetSharingConfiguration.4911
- _gCFArrayType.12234
- _gCFBooleanType.12235
- _gCFDataType.12236
- _gCFDateType.12237
- _gCFDictionaryType.12238
- _gCFNumberType.12233
- _gCFStringType.12239
- _getACAccountStoreClass.8164
- _getAKAccountManagerClass.8147
- _getAVAudioSessionClass.9411
- _getCALayerClass.13155
- _getCATransactionClass.13181
- _getHAPSystemKeychainStoreClass.5755
- _getWiFiAwareInternetSharingConfigurationClass.4892
- _initACAccountStore.8166
- _initAKAccountManager.8155
- _initAVAudioSession.9422
- _initAnalyticsSendEvent.8631
- _initCALayer.13172
- _initCATransaction.13189
- _initHAPSystemKeychainStore.5757
- _initWiFiAwareInternetSharingConfiguration.4909
- _logger.12304
- _logger.14349
- _logger.4838
- _logger.5091
- _logger.7462
- _logger.8188
- _logger.9811
- _sCUOSLogCreateOnce_logger.12307
- _sCUOSLogCreateOnce_logger.14427
- _sCUOSLogCreateOnce_logger.4839
- _sCUOSLogCreateOnce_logger.5093
- _sCUOSLogCreateOnce_logger.7464
- _sCUOSLogCreateOnce_logger.8190
- _sCUOSLogCreateOnce_logger.9813
- _sCUOSLogHandle_logger.12309
- _sCUOSLogHandle_logger.14429
- _sCUOSLogHandle_logger.4840
- _sCUOSLogHandle_logger.5095
- _sCUOSLogHandle_logger.7466
- _sCUOSLogHandle_logger.8191
- _sCUOSLogHandle_logger.9814
- _softLinkAnalyticsSendEvent.8626
CStrings:
+ "+[CUPairingManager copySystemPairingIdentifierWithFlags:error:]"
+ "@\"WiFiAwarePairingMetadata\""
+ "@\"WiFiAwarePublishDatapathServiceSpecificInfo\""
+ "Create path string failed"
+ "No UTF8 path"
+ "T@\"WiFiAwarePairingMetadata\",&,N,V_wfaPairingMetadata"
+ "T@\"WiFiAwarePublishDatapathServiceSpecificInfo\",&,N,V_wfaServiceSpecificInfo"
+ "Tq,N,V_wfaConnectionMode"
+ "Tq,N,V_wfaDiscoveryMode"
+ "WiFi Join notification: status=%@, state=%s, flags=%@, reason=%@"
+ "WiFi state changed: %s -> %s, flags=%@"
+ "WiFi state unchanged: %s, flags=%@"
+ "_getLengthWithCompletionHandler:"
+ "_wfaConnectionMode"
+ "_wfaDiscoveryMode"
+ "_wfaPairingMetadata"
+ "_wfaServiceSpecificInfo"
+ "copySystemPairingIdentifierWithFlags:error:"
+ "getLengthWithCompletionHandler:"
+ "realPath:dispatchQueue:completionHandler:"
+ "realPath:error:"
+ "realpath failed"
+ "setConnectionMode:"
+ "setDiscoveryMode:"
+ "setPairingMetadata:"
+ "setWfaConnectionMode:"
+ "setWfaDiscoveryMode:"
+ "setWfaPairingMetadata:"
+ "setWfaServiceSpecificInfo:"
+ "stat failed"
+ "wfaConnectionMode"
+ "wfaDiscoveryMode"
+ "wfaPairingMetadata"
+ "wfaServiceSpecificInfo"
+ "\xe1"
- "+[CUPairingManager copySystemPairingIdentifierAndReturnError:]"
- "WiFi Join notification: ssid=%@, status=%@, state=%s, flags=%@, reason=%@"
- "WiFi state changed: %s -> %s, flags=%@, ssid=%@"
- "WiFi state unchanged: %s, flags=%@, ssid=%@"
- "\xd1"

```
