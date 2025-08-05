## CoreSpeechFoundation

> `/System/Library/PrivateFrameworks/CoreSpeechFoundation.framework/CoreSpeechFoundation`

```diff

-3500.115.2.0.0
-  __TEXT.__text: 0xc0f24
+3500.122.2.0.0
+  __TEXT.__text: 0xc16dc
   __TEXT.__auth_stubs: 0x1eb0
-  __TEXT.__objc_methlist: 0xc3d0
+  __TEXT.__objc_methlist: 0xc4b8
   __TEXT.__const: 0x7f8
   __TEXT.__dlopen_cstrs: 0x1ee
   __TEXT.__constg_swiftt: 0x240
   __TEXT.__swift5_typeref: 0x185
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_types: 0x1c
-  __TEXT.__cstring: 0x14fdc
+  __TEXT.__cstring: 0x151c5
   __TEXT.__swift5_fieldmd: 0x128
   __TEXT.__swift5_reflstr: 0x84
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_proto: 0x8
-  __TEXT.__gcc_except_tab: 0x4124
-  __TEXT.__oslogstring: 0xf750
-  __TEXT.__unwind_info: 0x35b8
+  __TEXT.__gcc_except_tab: 0x4138
+  __TEXT.__oslogstring: 0xf7f2
+  __TEXT.__unwind_info: 0x35f8
   __TEXT.__eh_frame: 0xe0
-  __TEXT.__objc_classname: 0x1b84
-  __TEXT.__objc_methname: 0x20948
-  __TEXT.__objc_methtype: 0x4335
-  __TEXT.__objc_stubs: 0x10d00
-  __DATA_CONST.__got: 0xf68
-  __DATA_CONST.__const: 0x2640
-  __DATA_CONST.__objc_classlist: 0x6b8
+  __TEXT.__objc_classname: 0x1bb8
+  __TEXT.__objc_methname: 0x20b95
+  __TEXT.__objc_methtype: 0x43cb
+  __TEXT.__objc_stubs: 0x10e00
+  __DATA_CONST.__got: 0xf80
+  __DATA_CONST.__const: 0x2670
+  __DATA_CONST.__objc_classlist: 0x6c0
   __DATA_CONST.__objc_catlist: 0x58
-  __DATA_CONST.__objc_protolist: 0x1a0
+  __DATA_CONST.__objc_protolist: 0x1a8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6ac8
+  __DATA_CONST.__objc_selrefs: 0x6b28
   __DATA_CONST.__objc_protorefs: 0x28
-  __DATA_CONST.__objc_superrefs: 0x500
+  __DATA_CONST.__objc_superrefs: 0x508
   __DATA_CONST.__objc_arraydata: 0x198
   __AUTH_CONST.__auth_got: 0xf70
   __AUTH_CONST.__const: 0x1630
-  __AUTH_CONST.__cfstring: 0x8da0
-  __AUTH_CONST.__objc_const: 0x12e68
+  __AUTH_CONST.__cfstring: 0x8de0
+  __AUTH_CONST.__objc_const: 0x13040
   __AUTH_CONST.__objc_dictobj: 0x1e0
   __AUTH_CONST.__objc_intobj: 0x378
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_floatobj: 0x1a0
-  __AUTH.__objc_data: 0x18e8
-  __DATA.__objc_ivar: 0xc98
-  __DATA.__data: 0x13b0
-  __DATA.__bss: 0x920
-  __DATA_DIRTY.__objc_data: 0x2b00
-  __DATA_DIRTY.__data: 0x2d0
-  __DATA_DIRTY.__bss: 0x3a0
+  __AUTH.__objc_data: 0x1898
+  __DATA.__objc_ivar: 0xca8
+  __DATA.__data: 0x1408
+  __DATA.__bss: 0x8b8
+  __DATA_DIRTY.__objc_data: 0x2ba0
+  __DATA_DIRTY.__data: 0x2d8
+  __DATA_DIRTY.__bss: 0x400
   __DATA_DIRTY.__common: 0x68
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
+  - /usr/lib/swift/libswiftCoreAudio_Private.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 0534F09B-BBA1-3574-9F47-67A629BB9005
-  Functions: 4724
-  Symbols:   16023
-  CStrings:  10079
+  UUID: 857DAFC1-7275-3F5F-854A-986C6E1335E7
+  Functions: 4745
+  Symbols:   16097
+  CStrings:  10117
 
Symbols:
+ +[CSUtils supportDropInCall]
+ -[CSFDropInCallStateNotifier .cxx_destruct]
+ -[CSFDropInCallStateNotifier _registerForDropInCallbacks]
+ -[CSFDropInCallStateNotifier conversationProviderManager]
+ -[CSFDropInCallStateNotifier csdConnectionObserver]
+ -[CSFDropInCallStateNotifier init]
+ -[CSFDropInCallStateNotifier notifyObserver:didReceiveNotificationWithToken:]
+ -[CSFDropInCallStateNotifier queue]
+ -[CSFDropInCallStateNotifier setConversationProviderManager:]
+ -[CSFDropInCallStateNotifier setCsdConnectionObserver:]
+ -[CSFDropInCallStateNotifier setQueue:]
+ -[CSFDropInCallStateNotifier start]
+ -[CSFDropInCallStateNotifier stop]
+ -[CSPhoneCallStateMonitor .cxx_destruct]
+ -[CSPhoneCallStateMonitor deregisterDropInCallNotification]
+ -[CSPhoneCallStateMonitor registerDropInCallNotificationIfNeeded]
+ GCC_except_table1237
+ GCC_except_table1266
+ GCC_except_table1347
+ GCC_except_table1348
+ GCC_except_table1349
+ GCC_except_table1350
+ GCC_except_table1356
+ GCC_except_table1359
+ GCC_except_table1365
+ GCC_except_table1366
+ GCC_except_table1368
+ GCC_except_table1371
+ GCC_except_table1383
+ GCC_except_table1782
+ GCC_except_table1783
+ GCC_except_table1784
+ GCC_except_table1793
+ GCC_except_table1796
+ GCC_except_table1802
+ GCC_except_table1809
+ GCC_except_table1811
+ GCC_except_table1812
+ GCC_except_table1826
+ GCC_except_table1832
+ GCC_except_table1922
+ GCC_except_table1927
+ GCC_except_table1979
+ GCC_except_table1989
+ GCC_except_table2030
+ GCC_except_table2032
+ GCC_except_table2033
+ GCC_except_table2039
+ GCC_except_table2048
+ GCC_except_table2055
+ GCC_except_table2098
+ GCC_except_table2171
+ GCC_except_table2281
+ GCC_except_table2316
+ GCC_except_table2462
+ GCC_except_table2533
+ GCC_except_table2544
+ GCC_except_table2546
+ GCC_except_table2551
+ GCC_except_table2553
+ GCC_except_table2566
+ GCC_except_table2573
+ GCC_except_table2575
+ GCC_except_table2593
+ GCC_except_table2614
+ GCC_except_table2652
+ GCC_except_table2709
+ GCC_except_table2711
+ GCC_except_table2712
+ GCC_except_table2853
+ GCC_except_table2990
+ GCC_except_table2998
+ GCC_except_table3006
+ GCC_except_table3017
+ GCC_except_table3019
+ GCC_except_table3020
+ GCC_except_table3043
+ GCC_except_table3103
+ GCC_except_table3158
+ GCC_except_table3181
+ GCC_except_table3212
+ GCC_except_table3213
+ GCC_except_table3214
+ GCC_except_table3215
+ GCC_except_table3238
+ GCC_except_table3251
+ GCC_except_table3410
+ GCC_except_table3470
+ GCC_except_table3484
+ GCC_except_table3526
+ GCC_except_table3527
+ GCC_except_table3556
+ GCC_except_table3557
+ GCC_except_table3562
+ GCC_except_table3563
+ GCC_except_table3564
+ GCC_except_table3587
+ GCC_except_table3595
+ GCC_except_table3596
+ GCC_except_table3598
+ GCC_except_table3611
+ GCC_except_table3637
+ GCC_except_table3663
+ GCC_except_table3664
+ GCC_except_table3665
+ GCC_except_table3666
+ GCC_except_table3676
+ GCC_except_table3762
+ GCC_except_table3772
+ GCC_except_table3776
+ GCC_except_table3777
+ GCC_except_table3780
+ GCC_except_table3785
+ GCC_except_table3788
+ GCC_except_table3791
+ GCC_except_table3792
+ GCC_except_table3795
+ GCC_except_table3796
+ GCC_except_table3807
+ GCC_except_table3814
+ GCC_except_table3815
+ GCC_except_table3818
+ GCC_except_table3819
+ GCC_except_table3820
+ GCC_except_table3822
+ GCC_except_table3823
+ GCC_except_table3824
+ GCC_except_table3826
+ GCC_except_table3827
+ GCC_except_table3829
+ GCC_except_table3830
+ GCC_except_table3831
+ GCC_except_table3832
+ GCC_except_table3857
+ GCC_except_table3905
+ GCC_except_table3909
+ GCC_except_table3959
+ GCC_except_table3960
+ GCC_except_table3967
+ GCC_except_table3968
+ GCC_except_table3969
+ GCC_except_table3970
+ GCC_except_table3972
+ GCC_except_table3994
+ GCC_except_table3996
+ GCC_except_table3998
+ GCC_except_table3999
+ GCC_except_table4000
+ GCC_except_table4001
+ GCC_except_table4002
+ GCC_except_table4003
+ GCC_except_table4004
+ GCC_except_table4005
+ GCC_except_table4028
+ GCC_except_table4030
+ GCC_except_table4032
+ GCC_except_table4036
+ GCC_except_table4037
+ GCC_except_table4038
+ GCC_except_table4039
+ GCC_except_table4040
+ GCC_except_table4044
+ GCC_except_table4047
+ GCC_except_table4048
+ GCC_except_table4050
+ GCC_except_table4052
+ GCC_except_table4078
+ GCC_except_table4079
+ GCC_except_table4081
+ GCC_except_table4083
+ GCC_except_table4084
+ GCC_except_table4085
+ GCC_except_table4090
+ GCC_except_table4092
+ GCC_except_table4096
+ GCC_except_table4097
+ GCC_except_table4127
+ GCC_except_table4131
+ GCC_except_table4231
+ GCC_except_table4238
+ GCC_except_table4284
+ GCC_except_table4339
+ GCC_except_table4351
+ GCC_except_table4434
+ GCC_except_table4446
+ GCC_except_table4451
+ GCC_except_table4492
+ GCC_except_table4558
+ GCC_except_table603
+ GCC_except_table604
+ GCC_except_table763
+ GCC_except_table770
+ GCC_except_table833
+ GCC_except_table834
+ GCC_except_table841
+ GCC_except_table856
+ GCC_except_table857
+ GCC_except_table858
+ GCC_except_table864
+ GCC_except_table868
+ GCC_except_table869
+ GCC_except_table873
+ GCC_except_table877
+ GCC_except_table878
+ GCC_except_table879
+ GCC_except_table893
+ _AudioConverterFillComplexBuffer_BlockInvoke.7167
+ _OBJC_CLASS_$_AFNotifyObserver
+ _OBJC_CLASS_$_CSFDropInCallStateNotifier
+ _OBJC_CLASS_$_TUConversationProviderManager
+ _OBJC_IVAR_$_CSFDropInCallStateNotifier._conversationProviderManager
+ _OBJC_IVAR_$_CSFDropInCallStateNotifier._csdConnectionObserver
+ _OBJC_IVAR_$_CSFDropInCallStateNotifier._queue
+ _OBJC_IVAR_$_CSPhoneCallStateMonitor._dropInCallNotifier
+ _OBJC_METACLASS_$_CSFDropInCallStateNotifier
+ __OBJC_$_INSTANCE_METHODS_CSFDropInCallStateNotifier
+ __OBJC_$_INSTANCE_VARIABLES_CSFDropInCallStateNotifier
+ __OBJC_$_INSTANCE_VARIABLES_CSPhoneCallStateMonitor
+ __OBJC_$_PROP_LIST_CSFDropInCallStateNotifier
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_AFNotifyObserverDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AFNotifyObserverDelegate
+ __OBJC_$_PROTOCOL_REFS_AFNotifyObserverDelegate
+ __OBJC_CLASS_PROTOCOLS_$_CSFDropInCallStateNotifier
+ __OBJC_CLASS_RO_$_CSFDropInCallStateNotifier
+ __OBJC_LABEL_PROTOCOL_$_AFNotifyObserverDelegate
+ __OBJC_METACLASS_RO_$_CSFDropInCallStateNotifier
+ __OBJC_PROTOCOL_$_AFNotifyObserverDelegate
+ ___34-[CSFDropInCallStateNotifier stop]_block_invoke
+ ___35-[CSFDropInCallStateNotifier start]_block_invoke
+ ___50-[CSUAFDownloadMonitor _startMonitoringWithQueue:]_block_invoke.284
+ ___57-[CSFDropInCallStateNotifier _registerForDropInCallbacks]_block_invoke
+ ___57-[CSFDropInCallStateNotifier _registerForDropInCallbacks]_block_invoke.32
+ ___64-[CSUAFAssetManagerBase _mapVoiceTriggerAsset:asset:completion:]_block_invoke.331
+ ___64-[CSUAFAssetManagerBase _mapVoiceTriggerAsset:asset:completion:]_block_invoke_2.332
+ ___77-[CSFDropInCallStateNotifier notifyObserver:didReceiveNotificationWithToken:]_block_invoke
+ ___Block_byref_object_copy_.12504
+ ___Block_byref_object_copy_.12902
+ ___Block_byref_object_copy_.13199
+ ___Block_byref_object_copy_.13446
+ ___Block_byref_object_copy_.13945
+ ___Block_byref_object_copy_.14511
+ ___Block_byref_object_copy_.14595
+ ___Block_byref_object_copy_.1541
+ ___Block_byref_object_copy_.15462
+ ___Block_byref_object_copy_.2084
+ ___Block_byref_object_copy_.2494
+ ___Block_byref_object_copy_.3256
+ ___Block_byref_object_copy_.4569
+ ___Block_byref_object_copy_.4789
+ ___Block_byref_object_copy_.5639
+ ___Block_byref_object_copy_.6050
+ ___Block_byref_object_copy_.7752
+ ___Block_byref_object_copy_.8026
+ ___Block_byref_object_copy_.8474
+ ___Block_byref_object_copy_.9232
+ ___Block_byref_object_dispose_.12505
+ ___Block_byref_object_dispose_.12903
+ ___Block_byref_object_dispose_.13200
+ ___Block_byref_object_dispose_.13447
+ ___Block_byref_object_dispose_.13946
+ ___Block_byref_object_dispose_.14512
+ ___Block_byref_object_dispose_.14596
+ ___Block_byref_object_dispose_.1542
+ ___Block_byref_object_dispose_.15463
+ ___Block_byref_object_dispose_.2085
+ ___Block_byref_object_dispose_.2495
+ ___Block_byref_object_dispose_.3257
+ ___Block_byref_object_dispose_.4570
+ ___Block_byref_object_dispose_.4790
+ ___Block_byref_object_dispose_.5640
+ ___Block_byref_object_dispose_.6051
+ ___Block_byref_object_dispose_.7753
+ ___Block_byref_object_dispose_.8027
+ ___Block_byref_object_dispose_.8475
+ ___Block_byref_object_dispose_.9233
+ ___block_descriptor_40_e8_32w_e17_v16?0"NSError"8lw32l8
+ ___block_literal_global.10109
+ ___block_literal_global.10206
+ ___block_literal_global.1105
+ ___block_literal_global.11079
+ ___block_literal_global.11284
+ ___block_literal_global.11439
+ ___block_literal_global.11656
+ ___block_literal_global.11693
+ ___block_literal_global.12550
+ ___block_literal_global.13015
+ ___block_literal_global.1311
+ ___block_literal_global.13299
+ ___block_literal_global.13545
+ ___block_literal_global.13851
+ ___block_literal_global.1398
+ ___block_literal_global.14234
+ ___block_literal_global.1426
+ ___block_literal_global.14336
+ ___block_literal_global.14392
+ ___block_literal_global.1453
+ ___block_literal_global.14537
+ ___block_literal_global.14738
+ ___block_literal_global.14831
+ ___block_literal_global.14920
+ ___block_literal_global.1497
+ ___block_literal_global.15249
+ ___block_literal_global.15487
+ ___block_literal_global.1568
+ ___block_literal_global.180.8152
+ ___block_literal_global.20.13000
+ ___block_literal_global.2101
+ ___block_literal_global.2194
+ ___block_literal_global.2250
+ ___block_literal_global.2435
+ ___block_literal_global.2510
+ ___block_literal_global.2619
+ ___block_literal_global.2668
+ ___block_literal_global.27.8269
+ ___block_literal_global.276.8094
+ ___block_literal_global.2985
+ ___block_literal_global.3168
+ ___block_literal_global.3276
+ ___block_literal_global.3580
+ ___block_literal_global.3733
+ ___block_literal_global.3998
+ ___block_literal_global.41.8256
+ ___block_literal_global.422
+ ___block_literal_global.4597
+ ___block_literal_global.4757
+ ___block_literal_global.4805
+ ___block_literal_global.5407
+ ___block_literal_global.5491
+ ___block_literal_global.6272
+ ___block_literal_global.6419
+ ___block_literal_global.6487
+ ___block_literal_global.6544
+ ___block_literal_global.6660
+ ___block_literal_global.6678
+ ___block_literal_global.6872
+ ___block_literal_global.6935
+ ___block_literal_global.6995
+ ___block_literal_global.7096
+ ___block_literal_global.7132
+ ___block_literal_global.7417
+ ___block_literal_global.8282
+ ___block_literal_global.8302
+ ___block_literal_global.8357
+ ___block_literal_global.864
+ ___block_literal_global.8758
+ ___block_literal_global.8820
+ ___block_literal_global.8967
+ ___block_literal_global.9024
+ ___block_literal_global.9259
+ ___block_literal_global.9566
+ ___block_literal_global.9697
+ ___block_literal_global.975
+ ___block_literal_global.9805
+ __swift_FORCE_LOAD_$_swiftCoreAudio_Private
+ __swift_FORCE_LOAD_$_swiftCoreAudio_Private_$_CoreSpeechFoundation
+ _objc_msgSend$_registerForDropInCallbacks
+ _objc_msgSend$deregisterDropInCallNotification
+ _objc_msgSend$initWithName:options:queue:delegate:
+ _objc_msgSend$registerDropInCallNotificationIfNeeded
+ _objc_msgSend$registerForCallbacksForProvider:completionHandler:
+ _objc_msgSend$setConversationProviderManager:
+ _objc_msgSend$stop
+ _objc_msgSend$supportDropInCall
+ _sharedHandler.onceToken.12549
+ _sharedHandler.sharedHandler.12551
+ _sharedInstance._sharedInstance.10207
+ _sharedInstance._sharedInstance.11080
+ _sharedInstance._sharedInstance.11694
+ _sharedInstance._sharedInstance.14337
+ _sharedInstance._sharedInstance.14393
+ _sharedInstance._sharedInstance.14832
+ _sharedInstance._sharedInstance.14921
+ _sharedInstance._sharedInstance.3999
+ _sharedInstance._sharedInstance.4758
+ _sharedInstance._sharedInstance.5408
+ _sharedInstance._sharedInstance.6273
+ _sharedInstance._sharedInstance.6873
+ _sharedInstance._sharedInstance.7097
+ _sharedInstance._sharedInstance.7418
+ _sharedInstance._sharedInstance.865
+ _sharedInstance._sharedInstance.976
+ _sharedInstance.onceToken.10205
+ _sharedInstance.onceToken.11078
+ _sharedInstance.onceToken.11283
+ _sharedInstance.onceToken.11692
+ _sharedInstance.onceToken.1310
+ _sharedInstance.onceToken.13298
+ _sharedInstance.onceToken.1425
+ _sharedInstance.onceToken.14335
+ _sharedInstance.onceToken.14391
+ _sharedInstance.onceToken.14737
+ _sharedInstance.onceToken.14830
+ _sharedInstance.onceToken.14919
+ _sharedInstance.onceToken.1496
+ _sharedInstance.onceToken.15248
+ _sharedInstance.onceToken.15486
+ _sharedInstance.onceToken.1567
+ _sharedInstance.onceToken.2193
+ _sharedInstance.onceToken.2249
+ _sharedInstance.onceToken.2509
+ _sharedInstance.onceToken.3275
+ _sharedInstance.onceToken.3732
+ _sharedInstance.onceToken.3997
+ _sharedInstance.onceToken.4596
+ _sharedInstance.onceToken.4756
+ _sharedInstance.onceToken.4804
+ _sharedInstance.onceToken.5406
+ _sharedInstance.onceToken.6271
+ _sharedInstance.onceToken.6418
+ _sharedInstance.onceToken.6659
+ _sharedInstance.onceToken.6871
+ _sharedInstance.onceToken.7095
+ _sharedInstance.onceToken.7416
+ _sharedInstance.onceToken.8301
+ _sharedInstance.onceToken.8356
+ _sharedInstance.onceToken.863
+ _sharedInstance.onceToken.8819
+ _sharedInstance.onceToken.9023
+ _sharedInstance.onceToken.9565
+ _sharedInstance.onceToken.9696
+ _sharedInstance.onceToken.974
+ _sharedInstance.onceToken.9804
+ _sharedInstance.sharedInstance.11285
+ _sharedInstance.sharedInstance.1312
+ _sharedInstance.sharedInstance.13300
+ _sharedInstance.sharedInstance.14739
+ _sharedInstance.sharedInstance.15250
+ _sharedInstance.sharedInstance.15488
+ _sharedInstance.sharedInstance.2195
+ _sharedInstance.sharedInstance.2251
+ _sharedInstance.sharedInstance.2511
+ _sharedInstance.sharedInstance.3277
+ _sharedInstance.sharedInstance.3734
+ _sharedInstance.sharedInstance.4806
+ _sharedInstance.sharedInstance.6420
+ _sharedInstance.sharedInstance.8303
+ _sharedInstance.sharedInstance.8821
+ _sharedInstance.sharedInstance.9025
+ _sharedInstance.sharedInstance.9698
+ _sharedInstance.sharedInstance.9806
+ _sharedInstance.sharedManager.6661
+ _sharedInstance.sharedManager.8358
+ _sharedLogger.onceToken.13850
+ _sharedLogger.onceToken.2618
+ _sharedLogger.onceToken.6486
+ _sharedLogger.onceToken.6677
+ _sharedLogger.shared.13852
+ _sharedManager.onceToken.14536
+ _sharedMonitor.onceToken.5490
+ _sharedMonitor.sharedMonitor.5492
+ _sharedPreferences.onceToken.8757
- GCC_except_table1233
- GCC_except_table1262
- GCC_except_table1335
- GCC_except_table1340
- GCC_except_table1341
- GCC_except_table1342
- GCC_except_table1352
- GCC_except_table1355
- GCC_except_table1357
- GCC_except_table1358
- GCC_except_table1360
- GCC_except_table1367
- GCC_except_table1379
- GCC_except_table1777
- GCC_except_table1778
- GCC_except_table1779
- GCC_except_table1780
- GCC_except_table1788
- GCC_except_table1798
- GCC_except_table1805
- GCC_except_table1807
- GCC_except_table1808
- GCC_except_table1822
- GCC_except_table1828
- GCC_except_table1918
- GCC_except_table1923
- GCC_except_table1975
- GCC_except_table1985
- GCC_except_table2025
- GCC_except_table2026
- GCC_except_table2028
- GCC_except_table2035
- GCC_except_table2044
- GCC_except_table2051
- GCC_except_table2094
- GCC_except_table2167
- GCC_except_table2277
- GCC_except_table2312
- GCC_except_table2454
- GCC_except_table2529
- GCC_except_table2540
- GCC_except_table2542
- GCC_except_table2547
- GCC_except_table2549
- GCC_except_table2562
- GCC_except_table2569
- GCC_except_table2571
- GCC_except_table2589
- GCC_except_table2610
- GCC_except_table2648
- GCC_except_table2705
- GCC_except_table2707
- GCC_except_table2708
- GCC_except_table2849
- GCC_except_table2986
- GCC_except_table2994
- GCC_except_table3002
- GCC_except_table3009
- GCC_except_table3015
- GCC_except_table3016
- GCC_except_table3039
- GCC_except_table3095
- GCC_except_table3154
- GCC_except_table3177
- GCC_except_table3208
- GCC_except_table3209
- GCC_except_table3210
- GCC_except_table3211
- GCC_except_table3234
- GCC_except_table3247
- GCC_except_table3406
- GCC_except_table3466
- GCC_except_table3480
- GCC_except_table3522
- GCC_except_table3523
- GCC_except_table3552
- GCC_except_table3553
- GCC_except_table3555
- GCC_except_table3558
- GCC_except_table3560
- GCC_except_table3583
- GCC_except_table3586
- GCC_except_table3591
- GCC_except_table3592
- GCC_except_table3607
- GCC_except_table3633
- GCC_except_table3657
- GCC_except_table3659
- GCC_except_table3660
- GCC_except_table3662
- GCC_except_table3741
- GCC_except_table3742
- GCC_except_table3751
- GCC_except_table3753
- GCC_except_table3754
- GCC_except_table3755
- GCC_except_table3756
- GCC_except_table3759
- GCC_except_table3760
- GCC_except_table3764
- GCC_except_table3765
- GCC_except_table3766
- GCC_except_table3767
- GCC_except_table3768
- GCC_except_table3769
- GCC_except_table3770
- GCC_except_table3771
- GCC_except_table3782
- GCC_except_table3793
- GCC_except_table3794
- GCC_except_table3797
- GCC_except_table3798
- GCC_except_table3799
- GCC_except_table3801
- GCC_except_table3806
- GCC_except_table3809
- GCC_except_table3836
- GCC_except_table3884
- GCC_except_table3888
- GCC_except_table3938
- GCC_except_table3939
- GCC_except_table3946
- GCC_except_table3947
- GCC_except_table3948
- GCC_except_table3949
- GCC_except_table3951
- GCC_except_table3952
- GCC_except_table3974
- GCC_except_table3975
- GCC_except_table3977
- GCC_except_table3978
- GCC_except_table3979
- GCC_except_table3980
- GCC_except_table3981
- GCC_except_table3982
- GCC_except_table3983
- GCC_except_table3984
- GCC_except_table4007
- GCC_except_table4008
- GCC_except_table4009
- GCC_except_table4010
- GCC_except_table4011
- GCC_except_table4012
- GCC_except_table4013
- GCC_except_table4015
- GCC_except_table4017
- GCC_except_table4018
- GCC_except_table4019
- GCC_except_table4020
- GCC_except_table4023
- GCC_except_table4026
- GCC_except_table4027
- GCC_except_table4057
- GCC_except_table4058
- GCC_except_table4060
- GCC_except_table4063
- GCC_except_table4064
- GCC_except_table4069
- GCC_except_table4071
- GCC_except_table4106
- GCC_except_table4110
- GCC_except_table4210
- GCC_except_table4217
- GCC_except_table4263
- GCC_except_table4318
- GCC_except_table4330
- GCC_except_table4413
- GCC_except_table4425
- GCC_except_table4430
- GCC_except_table4471
- GCC_except_table4537
- GCC_except_table594
- GCC_except_table601
- GCC_except_table760
- GCC_except_table767
- GCC_except_table830
- GCC_except_table831
- GCC_except_table838
- GCC_except_table853
- GCC_except_table854
- GCC_except_table855
- GCC_except_table859
- GCC_except_table860
- GCC_except_table861
- GCC_except_table867
- GCC_except_table871
- GCC_except_table872
- GCC_except_table876
- GCC_except_table890
- _AudioConverterFillComplexBuffer_BlockInvoke.7140
- ___50-[CSUAFDownloadMonitor _startMonitoringWithQueue:]_block_invoke.281
- ___64-[CSUAFAssetManagerBase _mapVoiceTriggerAsset:asset:completion:]_block_invoke.328
- ___64-[CSUAFAssetManagerBase _mapVoiceTriggerAsset:asset:completion:]_block_invoke_2.329
- ___Block_byref_object_copy_.12388
- ___Block_byref_object_copy_.12786
- ___Block_byref_object_copy_.13083
- ___Block_byref_object_copy_.13330
- ___Block_byref_object_copy_.13829
- ___Block_byref_object_copy_.14395
- ___Block_byref_object_copy_.14479
- ___Block_byref_object_copy_.15346
- ___Block_byref_object_copy_.1540
- ___Block_byref_object_copy_.2076
- ___Block_byref_object_copy_.2486
- ___Block_byref_object_copy_.3229
- ___Block_byref_object_copy_.4542
- ___Block_byref_object_copy_.4762
- ___Block_byref_object_copy_.5612
- ___Block_byref_object_copy_.6023
- ___Block_byref_object_copy_.7737
- ___Block_byref_object_copy_.8012
- ___Block_byref_object_copy_.8460
- ___Block_byref_object_copy_.9218
- ___Block_byref_object_dispose_.12389
- ___Block_byref_object_dispose_.12787
- ___Block_byref_object_dispose_.13084
- ___Block_byref_object_dispose_.13331
- ___Block_byref_object_dispose_.13830
- ___Block_byref_object_dispose_.14396
- ___Block_byref_object_dispose_.14480
- ___Block_byref_object_dispose_.15347
- ___Block_byref_object_dispose_.1541
- ___Block_byref_object_dispose_.2077
- ___Block_byref_object_dispose_.2487
- ___Block_byref_object_dispose_.3230
- ___Block_byref_object_dispose_.4543
- ___Block_byref_object_dispose_.4763
- ___Block_byref_object_dispose_.5613
- ___Block_byref_object_dispose_.6024
- ___Block_byref_object_dispose_.7738
- ___Block_byref_object_dispose_.8013
- ___Block_byref_object_dispose_.8461
- ___Block_byref_object_dispose_.9219
- ___block_literal_global.10095
- ___block_literal_global.10192
- ___block_literal_global.1104
- ___block_literal_global.11064
- ___block_literal_global.11269
- ___block_literal_global.11424
- ___block_literal_global.11540
- ___block_literal_global.11577
- ___block_literal_global.12434
- ___block_literal_global.12899
- ___block_literal_global.1310
- ___block_literal_global.13183
- ___block_literal_global.13429
- ___block_literal_global.13735
- ___block_literal_global.1397
- ___block_literal_global.14118
- ___block_literal_global.14220
- ___block_literal_global.1425
- ___block_literal_global.14276
- ___block_literal_global.14421
- ___block_literal_global.1452
- ___block_literal_global.14622
- ___block_literal_global.14715
- ___block_literal_global.14804
- ___block_literal_global.1496
- ___block_literal_global.15133
- ___block_literal_global.15371
- ___block_literal_global.1567
- ___block_literal_global.180.8138
- ___block_literal_global.20.12884
- ___block_literal_global.2093
- ___block_literal_global.2186
- ___block_literal_global.2242
- ___block_literal_global.2427
- ___block_literal_global.2502
- ___block_literal_global.2611
- ___block_literal_global.2660
- ___block_literal_global.27.8255
- ___block_literal_global.276.8080
- ___block_literal_global.2958
- ___block_literal_global.3141
- ___block_literal_global.3249
- ___block_literal_global.3553
- ___block_literal_global.3706
- ___block_literal_global.3971
- ___block_literal_global.41.8242
- ___block_literal_global.421.8017
- ___block_literal_global.4570
- ___block_literal_global.4730
- ___block_literal_global.4778
- ___block_literal_global.5380
- ___block_literal_global.5464
- ___block_literal_global.6245
- ___block_literal_global.6392
- ___block_literal_global.6460
- ___block_literal_global.6517
- ___block_literal_global.6633
- ___block_literal_global.6651
- ___block_literal_global.6845
- ___block_literal_global.6908
- ___block_literal_global.6968
- ___block_literal_global.7069
- ___block_literal_global.7105
- ___block_literal_global.7390
- ___block_literal_global.8268
- ___block_literal_global.8288
- ___block_literal_global.8343
- ___block_literal_global.863
- ___block_literal_global.8744
- ___block_literal_global.8806
- ___block_literal_global.8953
- ___block_literal_global.9010
- ___block_literal_global.9245
- ___block_literal_global.9552
- ___block_literal_global.9683
- ___block_literal_global.974
- ___block_literal_global.9791
- _sharedHandler.onceToken.12433
- _sharedHandler.sharedHandler.12435
- _sharedInstance._sharedInstance.10193
- _sharedInstance._sharedInstance.11065
- _sharedInstance._sharedInstance.11578
- _sharedInstance._sharedInstance.14221
- _sharedInstance._sharedInstance.14277
- _sharedInstance._sharedInstance.14716
- _sharedInstance._sharedInstance.14805
- _sharedInstance._sharedInstance.3972
- _sharedInstance._sharedInstance.4731
- _sharedInstance._sharedInstance.5381
- _sharedInstance._sharedInstance.6246
- _sharedInstance._sharedInstance.6846
- _sharedInstance._sharedInstance.7070
- _sharedInstance._sharedInstance.7391
- _sharedInstance._sharedInstance.864
- _sharedInstance._sharedInstance.975
- _sharedInstance.onceToken.10191
- _sharedInstance.onceToken.11063
- _sharedInstance.onceToken.11268
- _sharedInstance.onceToken.11576
- _sharedInstance.onceToken.1309
- _sharedInstance.onceToken.13182
- _sharedInstance.onceToken.14219
- _sharedInstance.onceToken.1424
- _sharedInstance.onceToken.14275
- _sharedInstance.onceToken.14621
- _sharedInstance.onceToken.14714
- _sharedInstance.onceToken.14803
- _sharedInstance.onceToken.1495
- _sharedInstance.onceToken.15132
- _sharedInstance.onceToken.15370
- _sharedInstance.onceToken.1566
- _sharedInstance.onceToken.2185
- _sharedInstance.onceToken.2241
- _sharedInstance.onceToken.2501
- _sharedInstance.onceToken.3248
- _sharedInstance.onceToken.3705
- _sharedInstance.onceToken.3970
- _sharedInstance.onceToken.4569
- _sharedInstance.onceToken.4729
- _sharedInstance.onceToken.4777
- _sharedInstance.onceToken.5379
- _sharedInstance.onceToken.6244
- _sharedInstance.onceToken.6391
- _sharedInstance.onceToken.6632
- _sharedInstance.onceToken.6844
- _sharedInstance.onceToken.7068
- _sharedInstance.onceToken.7389
- _sharedInstance.onceToken.8287
- _sharedInstance.onceToken.8342
- _sharedInstance.onceToken.862
- _sharedInstance.onceToken.8805
- _sharedInstance.onceToken.9009
- _sharedInstance.onceToken.9551
- _sharedInstance.onceToken.9682
- _sharedInstance.onceToken.973
- _sharedInstance.onceToken.9790
- _sharedInstance.sharedInstance.11270
- _sharedInstance.sharedInstance.1311
- _sharedInstance.sharedInstance.13184
- _sharedInstance.sharedInstance.14623
- _sharedInstance.sharedInstance.15134
- _sharedInstance.sharedInstance.15372
- _sharedInstance.sharedInstance.2187
- _sharedInstance.sharedInstance.2243
- _sharedInstance.sharedInstance.2503
- _sharedInstance.sharedInstance.3250
- _sharedInstance.sharedInstance.3707
- _sharedInstance.sharedInstance.4779
- _sharedInstance.sharedInstance.6393
- _sharedInstance.sharedInstance.8289
- _sharedInstance.sharedInstance.8807
- _sharedInstance.sharedInstance.9011
- _sharedInstance.sharedInstance.9684
- _sharedInstance.sharedInstance.9792
- _sharedInstance.sharedManager.6634
- _sharedInstance.sharedManager.8344
- _sharedLogger.onceToken.13734
- _sharedLogger.onceToken.2610
- _sharedLogger.onceToken.6459
- _sharedLogger.onceToken.6650
- _sharedLogger.shared.13736
- _sharedManager.onceToken.14420
- _sharedMonitor.onceToken.5463
- _sharedMonitor.sharedMonitor.5465
- _sharedPreferences.onceToken.8743
CStrings:
+ "%s Received CSD XPC connection notification. Re-registering for drop-in calls"
+ "%s Registered for drop-in calls"
+ "%s Unable to register for drop-in calls: %{public}@"
+ "-[CSFDropInCallStateNotifier _registerForDropInCallbacks]_block_invoke"
+ "-[CSFDropInCallStateNotifier _registerForDropInCallbacks]_block_invoke_2"
+ "-[CSFDropInCallStateNotifier notifyObserver:didReceiveNotificationWithToken:]_block_invoke"
+ "?"
+ "@\"<_TtP20CoreSpeechFoundation29CSEnhancedEndpointerModelType_>\""
+ "@\"AFNotifyObserver\""
+ "@\"CSFDropInCallStateNotifier\""
+ "@\"MLMultiArray\""
+ "@\"TUConversationProviderManager\""
+ "AFNotifyObserverDelegate"
+ "CSFDropInCallStateNotifier"
+ "CSFDropInCallStateNotifier queue"
+ "T@\"AFNotifyObserver\",&,N,V_csdConnectionObserver"
+ "T@\"TUConversationProviderManager\",&,N,V_conversationProviderManager"
+ "_conversationProviderManager"
+ "_csdConnectionObserver"
+ "_dropInCallNotifier"
+ "_registerForDropInCallbacks"
+ "com.apple.private.alloy.dropin.communication"
+ "com.apple.telephonyutilities.callservicesdaemon.connectionrequest"
+ "conversationProviderManager"
+ "csdConnectionObserver"
+ "deregisterDropInCallNotification"
+ "initWithName:options:queue:delegate:"
+ "notifyObserver:didChangeStateFrom:to:"
+ "notifyObserver:didReceiveNotificationWithToken:"
+ "registerDropInCallNotificationIfNeeded"
+ "registerForCallbacksForProvider:completionHandler:"
+ "setConversationProviderManager:"
+ "setCsdConnectionObserver:"
+ "supportDropInCall"
+ "v28@0:8@\"AFNotifyObserver\"16i24"
+ "v40@0:8@\"AFNotifyObserver\"16Q24Q32"

```
