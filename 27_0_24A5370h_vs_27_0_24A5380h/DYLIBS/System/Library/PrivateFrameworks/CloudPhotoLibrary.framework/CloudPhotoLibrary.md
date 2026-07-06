## CloudPhotoLibrary

> `/System/Library/PrivateFrameworks/CloudPhotoLibrary.framework/CloudPhotoLibrary`

```diff

-  __TEXT.__text: 0x1c9d34
-  __TEXT.__objc_methlist: 0x15cac
+  __TEXT.__text: 0x1ca868
+  __TEXT.__objc_methlist: 0x15c64
   __TEXT.__const: 0x328
-  __TEXT.__gcc_except_tab: 0x4d0c
-  __TEXT.__oslogstring: 0x16cf3
-  __TEXT.__cstring: 0x18083
-  __TEXT.__unwind_info: 0x6cc8
+  __TEXT.__gcc_except_tab: 0x4d78
+  __TEXT.__oslogstring: 0x16c06
+  __TEXT.__cstring: 0x180cb
+  __TEXT.__unwind_info: 0x6d10
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x6f38
-  __DATA_CONST.__objc_classlist: 0x9e0
+  __DATA_CONST.__const: 0x6f48
+  __DATA_CONST.__objc_classlist: 0x9e8
   __DATA_CONST.__objc_catlist: 0x90
-  __DATA_CONST.__objc_protolist: 0x198
+  __DATA_CONST.__objc_protolist: 0x1b8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9310
+  __DATA_CONST.__objc_selrefs: 0x92c8
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x940
   __DATA_CONST.__objc_arraydata: 0x1438
-  __DATA_CONST.__got: 0xb28
+  __DATA_CONST.__got: 0xb48
   __AUTH_CONST.__const: 0x2ca0
   __AUTH_CONST.__cfstring: 0x17be0
-  __AUTH_CONST.__objc_const: 0x23660
-  __AUTH_CONST.__objc_intobj: 0x780
+  __AUTH_CONST.__objc_const: 0x23890
+  __AUTH_CONST.__objc_intobj: 0x798
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_dictobj: 0x140
   __AUTH_CONST.__objc_floatobj: 0x50
-  __AUTH_CONST.__auth_got: 0x798
-  __AUTH.__objc_data: 0x960
+  __AUTH_CONST.__auth_got: 0x7a8
+  __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x1c08
-  __DATA.__data: 0x14f0
-  __DATA.__bss: 0xce8
+  __DATA.__data: 0x1670
+  __DATA.__bss: 0xc90
   __DATA.__common: 0x30
-  __DATA_DIRTY.__objc_data: 0x5960
-  __DATA_DIRTY.__bss: 0x320
+  __DATA_DIRTY.__objc_data: 0x62c0
+  __DATA_DIRTY.__bss: 0x390
   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcupolicy.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 9763
-  Symbols:   30003
-  CStrings:  8461
+  Functions: 9774
+  Symbols:   30023
+  CStrings:  8456
 
Sections:
~ __TEXT.__const : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH_CONST.__objc_floatobj : content changed
~ __DATA.__objc_ivar : content changed
Symbols:
+ -[CPLConfiguration delegate]
+ -[CPLConfiguration setDelegate:]
+ -[CPLConfigurationFetcher URLSession:task:didReceiveChallenge:completionHandler:]
+ -[CPLEngineLibrary configurationDidUpdate:]
+ -[CPLEngineLibrary iCloudLibraryClientNeedsToVerifyTerms]
+ -[CPLEngineLibrary setICloudLibraryClientNeedsToVerifyTerms:]
+ -[CPLEngineScheduler _forceRestartSyncSession]
+ -[CPLEngineScheduler setTurboMode:]
+ -[CPLEngineScheduler shouldBypassBackgroundScheduling]
+ -[CPLEngineSystemMonitor _startWatchingTurboSync]
+ -[CPLEngineSystemMonitor turboSyncObserverExpirationDateDidChange:]
+ -[CPLNetworkState isBadQuality]
+ -[CPLNetworkState isSufficentlyDifferentFromNetworkState:]
+ -[CPLNetworkState shouldTriggerRetryOfNetworkOperationsFromNetworkState:]
+ -[CPLPredictionFlagFormatter stringForObjectValue:]
+ -[CPLStatus iCloudLibraryClientNeedsToVerifyTerms]
+ -[CPLStatus setICloudLibraryClientNeedsToVerifyTerms:]
+ -[CPLSyncSession forcesBypassBackgroundScheduling]
+ -[CPLSyncSession isBlocked]
+ -[CPLSyncSession setBlocked:]
+ GCC_except_table1120
+ GCC_except_table1203
+ GCC_except_table1257
+ GCC_except_table1262
+ GCC_except_table1308
+ GCC_except_table1326
+ GCC_except_table1328
+ GCC_except_table1502
+ GCC_except_table1551
+ GCC_except_table1555
+ GCC_except_table1557
+ GCC_except_table1562
+ GCC_except_table1572
+ GCC_except_table1574
+ GCC_except_table1581
+ GCC_except_table1584
+ GCC_except_table1593
+ GCC_except_table1595
+ GCC_except_table1597
+ GCC_except_table1599
+ GCC_except_table1681
+ GCC_except_table1769
+ GCC_except_table2030
+ GCC_except_table2254
+ GCC_except_table2255
+ GCC_except_table2258
+ GCC_except_table2265
+ GCC_except_table2269
+ GCC_except_table2296
+ GCC_except_table2303
+ GCC_except_table2313
+ GCC_except_table2316
+ GCC_except_table240
+ GCC_except_table2505
+ GCC_except_table255
+ GCC_except_table2604
+ GCC_except_table261
+ GCC_except_table264
+ GCC_except_table266
+ GCC_except_table2678
+ GCC_except_table268
+ GCC_except_table2719
+ GCC_except_table2811
+ GCC_except_table2818
+ GCC_except_table2971
+ GCC_except_table298
+ GCC_except_table3060
+ GCC_except_table3350
+ GCC_except_table3352
+ GCC_except_table3456
+ GCC_except_table3467
+ GCC_except_table3522
+ GCC_except_table3524
+ GCC_except_table3635
+ GCC_except_table3659
+ GCC_except_table3741
+ GCC_except_table3745
+ GCC_except_table3747
+ GCC_except_table3749
+ GCC_except_table3753
+ GCC_except_table377
+ GCC_except_table3914
+ GCC_except_table3961
+ GCC_except_table4206
+ GCC_except_table427
+ GCC_except_table4282
+ GCC_except_table4286
+ GCC_except_table4288
+ GCC_except_table4297
+ GCC_except_table438
+ GCC_except_table4502
+ GCC_except_table4516
+ GCC_except_table4673
+ GCC_except_table4703
+ GCC_except_table4734
+ GCC_except_table4752
+ GCC_except_table4759
+ GCC_except_table4767
+ GCC_except_table4769
+ GCC_except_table4783
+ GCC_except_table4785
+ GCC_except_table4788
+ GCC_except_table511
+ GCC_except_table515
+ GCC_except_table5160
+ GCC_except_table5193
+ GCC_except_table5195
+ GCC_except_table5221
+ GCC_except_table531
+ GCC_except_table5355
+ GCC_except_table5365
+ GCC_except_table5422
+ GCC_except_table5425
+ GCC_except_table553
+ GCC_except_table5603
+ GCC_except_table5611
+ GCC_except_table5701
+ GCC_except_table5705
+ GCC_except_table571
+ GCC_except_table5711
+ GCC_except_table5718
+ GCC_except_table5734
+ GCC_except_table5740
+ GCC_except_table5786
+ GCC_except_table5792
+ GCC_except_table5796
+ GCC_except_table581
+ GCC_except_table5822
+ GCC_except_table5827
+ GCC_except_table5829
+ GCC_except_table5831
+ GCC_except_table5833
+ GCC_except_table5835
+ GCC_except_table5837
+ GCC_except_table5839
+ GCC_except_table5842
+ GCC_except_table5847
+ GCC_except_table5849
+ GCC_except_table5852
+ GCC_except_table5854
+ GCC_except_table5899
+ GCC_except_table5901
+ GCC_except_table5903
+ GCC_except_table5915
+ GCC_except_table599
+ GCC_except_table6064
+ GCC_except_table6106
+ GCC_except_table6117
+ GCC_except_table612
+ GCC_except_table6176
+ GCC_except_table6179
+ GCC_except_table6264
+ GCC_except_table6266
+ GCC_except_table6282
+ GCC_except_table6305
+ GCC_except_table6321
+ GCC_except_table6323
+ GCC_except_table6483
+ GCC_except_table6511
+ GCC_except_table6554
+ GCC_except_table6574
+ GCC_except_table6600
+ GCC_except_table6611
+ GCC_except_table6632
+ GCC_except_table6652
+ GCC_except_table6656
+ GCC_except_table6682
+ GCC_except_table6714
+ GCC_except_table6754
+ GCC_except_table6819
+ GCC_except_table6845
+ GCC_except_table6849
+ GCC_except_table6858
+ GCC_except_table6876
+ GCC_except_table6894
+ GCC_except_table6902
+ GCC_except_table6903
+ GCC_except_table6917
+ GCC_except_table6972
+ GCC_except_table7097
+ GCC_except_table7111
+ GCC_except_table7114
+ GCC_except_table722
+ GCC_except_table7241
+ GCC_except_table7243
+ GCC_except_table7245
+ GCC_except_table7249
+ GCC_except_table7252
+ GCC_except_table728
+ GCC_except_table7629
+ GCC_except_table763
+ GCC_except_table767
+ GCC_except_table7675
+ GCC_except_table7677
+ GCC_except_table7698
+ GCC_except_table770
+ GCC_except_table7712
+ GCC_except_table7716
+ GCC_except_table772
+ GCC_except_table7724
+ GCC_except_table7727
+ GCC_except_table7747
+ GCC_except_table775
+ GCC_except_table7754
+ GCC_except_table777
+ GCC_except_table7777
+ GCC_except_table781
+ GCC_except_table7812
+ GCC_except_table783
+ GCC_except_table7843
+ GCC_except_table7854
+ GCC_except_table7874
+ GCC_except_table7877
+ GCC_except_table7879
+ GCC_except_table7881
+ GCC_except_table7912
+ GCC_except_table792
+ GCC_except_table794
+ GCC_except_table796
+ GCC_except_table7962
+ GCC_except_table798
+ GCC_except_table800
+ GCC_except_table802
+ GCC_except_table804
+ GCC_except_table806
+ GCC_except_table808
+ GCC_except_table810
+ GCC_except_table8106
+ GCC_except_table812
+ GCC_except_table8132
+ GCC_except_table814
+ GCC_except_table8162
+ GCC_except_table822
+ GCC_except_table824
+ GCC_except_table826
+ GCC_except_table828
+ GCC_except_table830
+ GCC_except_table8317
+ GCC_except_table8319
+ GCC_except_table8349
+ GCC_except_table8358
+ GCC_except_table8363
+ GCC_except_table8379
+ GCC_except_table839
+ GCC_except_table8393
+ GCC_except_table8403
+ GCC_except_table8408
+ GCC_except_table841
+ GCC_except_table843
+ GCC_except_table845
+ GCC_except_table847
+ GCC_except_table849
+ GCC_except_table8492
+ GCC_except_table851
+ GCC_except_table853
+ GCC_except_table855
+ GCC_except_table857
+ GCC_except_table8579
+ GCC_except_table859
+ GCC_except_table8638
+ GCC_except_table8716
+ GCC_except_table8731
+ GCC_except_table8753
+ GCC_except_table8759
+ GCC_except_table8778
+ GCC_except_table8788
+ GCC_except_table879
+ GCC_except_table8830
+ GCC_except_table8833
+ GCC_except_table8837
+ GCC_except_table8841
+ GCC_except_table885
+ GCC_except_table8919
+ GCC_except_table894
+ GCC_except_table903
+ GCC_except_table915
+ _CFNotificationCenterGetDistributedCenter
+ _CPLRequestEngine
+ _CPLSetRequestEngineBlock
+ _CPLSyncSessionPredictionTypeTurboMode
+ _OBJC_CLASS_$_CPLPredictionFlagFormatter
+ _OBJC_IVAR_$_CPLConfiguration._delegate
+ _OBJC_IVAR_$_CPLEngineScheduler._turboMode
+ _OBJC_IVAR_$_CPLEngineSystemMonitor._lastNetworkState
+ _OBJC_IVAR_$_CPLEngineSystemMonitor._turboSyncObserver
+ _OBJC_IVAR_$_CPLSyncSession._blocked
+ _OBJC_IVAR_$_CPLSyncSession._forcesBypassBackgroundScheduling
+ _OBJC_IVAR_$_CPLTurboSyncObserver._lastNetworkState
+ _OBJC_METACLASS_$_CPLPredictionFlagFormatter
+ __CPLRequestEngineBlock
+ __CPLRequestEngineBlockLock
+ __CPLSetTurboModeExpirationDate
+ __OBJC_$_INSTANCE_METHODS_CPLPredictionFlagFormatter
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CPLConfigurationDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CPLTurboSyncObserverDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSURLSessionDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSURLSessionTaskDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CPLConfigurationDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CPLTurboSyncObserverDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSURLSessionDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSURLSessionTaskDelegate
+ __OBJC_$_PROTOCOL_REFS_CPLConfigurationDelegate
+ __OBJC_$_PROTOCOL_REFS_CPLTurboSyncObserverDelegate
+ __OBJC_$_PROTOCOL_REFS_NSURLSessionDelegate
+ __OBJC_$_PROTOCOL_REFS_NSURLSessionTaskDelegate
+ __OBJC_CLASS_PROTOCOLS_$_CPLConfigurationFetcher
+ __OBJC_CLASS_RO_$_CPLPredictionFlagFormatter
+ __OBJC_LABEL_PROTOCOL_$_CPLConfigurationDelegate
+ __OBJC_LABEL_PROTOCOL_$_CPLTurboSyncObserverDelegate
+ __OBJC_LABEL_PROTOCOL_$_NSURLSessionDelegate
+ __OBJC_LABEL_PROTOCOL_$_NSURLSessionTaskDelegate
+ __OBJC_METACLASS_RO_$_CPLPredictionFlagFormatter
+ __OBJC_PROTOCOL_$_CPLConfigurationDelegate
+ __OBJC_PROTOCOL_$_CPLTurboSyncObserverDelegate
+ __OBJC_PROTOCOL_$_NSURLSessionDelegate
+ __OBJC_PROTOCOL_$_NSURLSessionTaskDelegate
+ ___27-[CPLSyncSession isBlocked]_block_invoke
+ ___29-[CPLSyncSession setBlocked:]_block_invoke
+ ___35-[CPLEngineScheduler setTurboMode:]_block_invoke
+ ___43-[CPLEngineLibrary configurationDidUpdate:]_block_invoke
+ ___50-[CPLStatus iCloudLibraryClientNeedsToVerifyTerms]_block_invoke
+ ___51-[CPLConfiguration _updateConfigurationDictionary:]_block_invoke
+ ___54-[CPLStatus setICloudLibraryClientNeedsToVerifyTerms:]_block_invoke
+ ___67-[CPLEngineSystemMonitor turboSyncObserverExpirationDateDidChange:]_block_invoke
+ ___67-[CPLEngineSystemMonitor turboSyncObserverExpirationDateDidChange:]_block_invoke_2
+ ___CPLRequestEngine_block_invoke
+ ___CPLSetRequestEngineBlock_block_invoke
+ ___block_descriptor_41_e8_32s_e8_v16?0Q8ls32l8
+ _dispatch_get_global_queue
+ _objc_msgSend$configurationDidUpdate:
+ _objc_msgSend$expirationDate
+ _objc_msgSend$iCloudLibraryClientNeedsToVerifyTerms
+ _objc_msgSend$isBadQuality
+ _objc_msgSend$isSufficentlyDifferentFromNetworkState:
+ _objc_msgSend$setBlocked:
+ _objc_msgSend$setICloudLibraryClientNeedsToVerifyTerms:
+ _objc_msgSend$setTurboMode:
+ _objc_msgSend$shouldTriggerRetryOfNetworkOperationsFromNetworkState:
- -[CPLConfiguration _save]
- -[CPLEngineScheduler _allowsJustInCaseSessions]
- -[CPLEngineScheduler _enableSynchronizationWithReasonLocked:]
- -[CPLEngineScheduler _justInCaseSessionIsPossible]
- -[CPLEngineScheduler _noteSyncSessionNeededFromStateDontRewindImmediately:]
- -[CPLEngineScheduler _prepareFirstSession]
- -[CPLEngineScheduler _setRequiredFirstState:]
- -[CPLEngineScheduler _startSyncSession:withMinimalPhase:rewind:]
- -[CPLEngineScheduler _syncSessionIsPossible]
- -[CPLEngineScheduler _unscheduleNextSyncSession]
- -[CPLEngineScheduler _updateTurboModeOnQueue]
- -[CPLEngineScheduler setCanUseTurboMode:]
- -[CPLEngineScheduler shouldUseTurboMode]
- -[CPLEngineSystemMonitor _hasPermanentDataOverride]
- -[CPLEngineSystemMonitor _permanentDataOverrideHasChanged]
- -[CPLEngineSystemMonitor _startWatchingPermanentDataOverride]
- -[CPLEngineSystemMonitor _stopWatchingPermanentDataOverride]
- -[CPLEngineSystemMonitor _updateCanUseTurboModeOnScheduler]
- -[CPLSyncSession usesTurboMode]
- GCC_except_table1115
- GCC_except_table1195
- GCC_except_table1249
- GCC_except_table1254
- GCC_except_table1300
- GCC_except_table1318
- GCC_except_table1320
- GCC_except_table1494
- GCC_except_table1543
- GCC_except_table1547
- GCC_except_table1549
- GCC_except_table1554
- GCC_except_table1556
- GCC_except_table1566
- GCC_except_table1573
- GCC_except_table1576
- GCC_except_table1579
- GCC_except_table1585
- GCC_except_table1589
- GCC_except_table1591
- GCC_except_table1673
- GCC_except_table1761
- GCC_except_table2014
- GCC_except_table2246
- GCC_except_table2247
- GCC_except_table2250
- GCC_except_table2257
- GCC_except_table2261
- GCC_except_table2288
- GCC_except_table2295
- GCC_except_table2305
- GCC_except_table2308
- GCC_except_table239
- GCC_except_table2497
- GCC_except_table254
- GCC_except_table2596
- GCC_except_table260
- GCC_except_table263
- GCC_except_table265
- GCC_except_table2662
- GCC_except_table267
- GCC_except_table2711
- GCC_except_table2803
- GCC_except_table2810
- GCC_except_table2963
- GCC_except_table297
- GCC_except_table3052
- GCC_except_table3338
- GCC_except_table3340
- GCC_except_table3422
- GCC_except_table3426
- GCC_except_table3436
- GCC_except_table3446
- GCC_except_table3504
- GCC_except_table3506
- GCC_except_table3636
- GCC_except_table3660
- GCC_except_table3742
- GCC_except_table3746
- GCC_except_table3748
- GCC_except_table3750
- GCC_except_table3754
- GCC_except_table376
- GCC_except_table3915
- GCC_except_table3962
- GCC_except_table4207
- GCC_except_table426
- GCC_except_table4283
- GCC_except_table4287
- GCC_except_table4289
- GCC_except_table4298
- GCC_except_table437
- GCC_except_table4501
- GCC_except_table4515
- GCC_except_table4672
- GCC_except_table4702
- GCC_except_table4733
- GCC_except_table4751
- GCC_except_table4758
- GCC_except_table4766
- GCC_except_table4768
- GCC_except_table4782
- GCC_except_table4784
- GCC_except_table4787
- GCC_except_table510
- GCC_except_table514
- GCC_except_table5159
- GCC_except_table5192
- GCC_except_table5194
- GCC_except_table5220
- GCC_except_table530
- GCC_except_table5354
- GCC_except_table5364
- GCC_except_table5421
- GCC_except_table5424
- GCC_except_table552
- GCC_except_table5602
- GCC_except_table5610
- GCC_except_table569
- GCC_except_table5700
- GCC_except_table5704
- GCC_except_table5710
- GCC_except_table5717
- GCC_except_table5732
- GCC_except_table5739
- GCC_except_table5785
- GCC_except_table5791
- GCC_except_table5795
- GCC_except_table580
- GCC_except_table5821
- GCC_except_table5826
- GCC_except_table5828
- GCC_except_table5830
- GCC_except_table5832
- GCC_except_table5834
- GCC_except_table5836
- GCC_except_table5838
- GCC_except_table5841
- GCC_except_table5846
- GCC_except_table5848
- GCC_except_table5850
- GCC_except_table5853
- GCC_except_table5898
- GCC_except_table5900
- GCC_except_table5902
- GCC_except_table5914
- GCC_except_table598
- GCC_except_table6063
- GCC_except_table6105
- GCC_except_table611
- GCC_except_table6115
- GCC_except_table6175
- GCC_except_table6178
- GCC_except_table6263
- GCC_except_table6265
- GCC_except_table6281
- GCC_except_table6304
- GCC_except_table6320
- GCC_except_table6322
- GCC_except_table6482
- GCC_except_table6510
- GCC_except_table6551
- GCC_except_table6571
- GCC_except_table6597
- GCC_except_table6608
- GCC_except_table6629
- GCC_except_table6649
- GCC_except_table6653
- GCC_except_table6679
- GCC_except_table6711
- GCC_except_table6751
- GCC_except_table6814
- GCC_except_table6840
- GCC_except_table6844
- GCC_except_table6853
- GCC_except_table6871
- GCC_except_table6884
- GCC_except_table6897
- GCC_except_table6898
- GCC_except_table6912
- GCC_except_table6967
- GCC_except_table7092
- GCC_except_table7106
- GCC_except_table7109
- GCC_except_table721
- GCC_except_table7236
- GCC_except_table7238
- GCC_except_table7240
- GCC_except_table7244
- GCC_except_table7247
- GCC_except_table727
- GCC_except_table762
- GCC_except_table7623
- GCC_except_table766
- GCC_except_table7665
- GCC_except_table7669
- GCC_except_table7686
- GCC_except_table769
- GCC_except_table7700
- GCC_except_table771
- GCC_except_table7710
- GCC_except_table7718
- GCC_except_table7721
- GCC_except_table774
- GCC_except_table7741
- GCC_except_table7748
- GCC_except_table776
- GCC_except_table7771
- GCC_except_table780
- GCC_except_table7806
- GCC_except_table782
- GCC_except_table7837
- GCC_except_table7848
- GCC_except_table7868
- GCC_except_table7871
- GCC_except_table7873
- GCC_except_table7875
- GCC_except_table7906
- GCC_except_table791
- GCC_except_table793
- GCC_except_table795
- GCC_except_table7956
- GCC_except_table797
- GCC_except_table799
- GCC_except_table801
- GCC_except_table803
- GCC_except_table805
- GCC_except_table807
- GCC_except_table809
- GCC_except_table8105
- GCC_except_table811
- GCC_except_table8128
- GCC_except_table813
- GCC_except_table8158
- GCC_except_table821
- GCC_except_table823
- GCC_except_table825
- GCC_except_table827
- GCC_except_table829
- GCC_except_table8313
- GCC_except_table8315
- GCC_except_table8345
- GCC_except_table8354
- GCC_except_table8359
- GCC_except_table8375
- GCC_except_table838
- GCC_except_table8389
- GCC_except_table8399
- GCC_except_table840
- GCC_except_table8404
- GCC_except_table842
- GCC_except_table844
- GCC_except_table846
- GCC_except_table848
- GCC_except_table8488
- GCC_except_table850
- GCC_except_table852
- GCC_except_table854
- GCC_except_table8575
- GCC_except_table8634
- GCC_except_table8712
- GCC_except_table8727
- GCC_except_table874
- GCC_except_table8749
- GCC_except_table8755
- GCC_except_table8774
- GCC_except_table8784
- GCC_except_table880
- GCC_except_table8826
- GCC_except_table8828
- GCC_except_table889
- GCC_except_table8908
- GCC_except_table898
- GCC_except_table910
- _OBJC_IVAR_$_CPLEngineScheduler._canUseTurboMode
- _OBJC_IVAR_$_CPLEngineScheduler._isUsingTurboMode
- _OBJC_IVAR_$_CPLEngineScheduler._turboModeLock
- _OBJC_IVAR_$_CPLEngineScheduler._turboModeObserver
- _OBJC_IVAR_$_CPLEngineSystemMonitor._hasSetupBatteryMonitor
- _OBJC_IVAR_$_CPLEngineSystemMonitor._turboModeFlags
- _OBJC_IVAR_$_CPLSyncSession._usesTurboMode
- ___40-[CPLEngineScheduler shouldUseTurboMode]_block_invoke
- ___41-[CPLEngineScheduler setCanUseTurboMode:]_block_invoke
- ___45-[CPLEngineScheduler _updateTurboModeOnQueue]_block_invoke
- ___48-[CPLEngineScheduler openWithCompletionHandler:]_block_invoke_3
- ___50-[CPLEngineScheduler _turboModeSettingsHasChanged]_block_invoke
- ___57-[CPLEngineSystemMonitor getStatusWithCompletionHandler:]_block_invoke_4
- ___block_descriptor_40_e8_32s_e21_v20?0"NSString"8I16ls32l8
- _objc_msgSend$_allowsJustInCaseSessions
- _objc_msgSend$_backOff
- _objc_msgSend$_disableFastRelaunchProtection
- _objc_msgSend$_disableRetryAfterLocked
- _objc_msgSend$_disableSynchronizationBecauseContainerHasBeenWipedLocked
- _objc_msgSend$_disableSynchronizationWithReasonLocked:
- _objc_msgSend$_enableSynchronizationWithReasonLocked:
- _objc_msgSend$_handleResetAnchorWithError:completionHandler:
- _objc_msgSend$_handleResetClientCacheWithError:completionHandler:
- _objc_msgSend$_handleResetCloudCacheWithError:completionHandler:
- _objc_msgSend$_handleResetGlobalAnchorWithError:completionHandler:
- _objc_msgSend$_hasPermanentDataOverride
- _objc_msgSend$_justInCaseSessionIsPossible
- _objc_msgSend$_keepSessionInformation:
- _objc_msgSend$_noteServerIsUnavailableWithErrorLocked:reason:
- _objc_msgSend$_noteSignificantEvent
- _objc_msgSend$_noteSyncSession:failedDuringPhase:withError:
- _objc_msgSend$_noteSyncSessionNeededFromState:proposedScheduleDate:
- _objc_msgSend$_noteSyncSessionNeededFromStateDontRewindImmediately:
- _objc_msgSend$_permanentDataOverrideHasChanged
- _objc_msgSend$_prepareFirstSession
- _objc_msgSend$_reallyNoteServerHasChangesLocked
- _objc_msgSend$_reallyStartSyncSession:
- _objc_msgSend$_reallyUnscheduleSession
- _objc_msgSend$_scheduleNextSyncSession
- _objc_msgSend$_setRequiredFirstState:
- _objc_msgSend$_startOverridingBudget:reason:
- _objc_msgSend$_startRequiredSyncSession:
- _objc_msgSend$_startSyncSession:withMinimalPhase:rewind:
- _objc_msgSend$_startWatchingPermanentDataOverride
- _objc_msgSend$_stopOverridingBudget:reason:
- _objc_msgSend$_stopPreparingFirstSession
- _objc_msgSend$_stopWatchingPermanentDataOverride
- _objc_msgSend$_syncSessionIsPossible
- _objc_msgSend$_unscheduleNextSyncSession
- _objc_msgSend$_updateCanUseTurboModeOnScheduler
- _objc_msgSend$_updateConfigurationDictionary:
- _objc_msgSend$_updateLastSyncDateIfNecessaryLocked
- _objc_msgSend$_updateOverridingForeground
- _objc_msgSend$_withSystemBudgetOverride:
- _objc_msgSend$setCanUseTurboMode:
- _objc_msgSend$shouldUseTurboMode
CStrings:
+ "\nTurbo mode: expires %@"
+ " blocked"
+ "%@ is blocked at %@ and we need to rewind to %@ - restarting a sync session now"
+ "CPLEPPAutoEnable"
+ "CloudPhotoLibrary-910.27.103"
+ "com.apple.cpl.epp-auto-enable"
+ "com.apple.cpl.wantsdaemon.notification"
+ "iCloudLibraryClientNeedsToVerifyTerms"
+ "low power mode: enabled"
+ "turbo mode"
+ "turboMode"
+ "\xd1"
+ "\xf0\xf0Q"
- "\nTurbo mode%s: expires %@"
- " (blocked)"
- " turbo"
- "%@ (%i)"
- "%@ (unkn.)"
- "Can use turbo mode: %@"
- "Cancelling discretionary %@ because turbo mode has been enabled"
- "Cancelling non-discretionary %@ because turbo mode has been disabled"
- "CloudPhotoLibrary-910.21.101"
- "Rescheduling discretionary %@ because turbo mode has been enabled"
- "Rescheduling non-discretionary %@ because turbo mode has been disabled"
- "Updating turbo mode: %@"
- "enabled"
- "low data"
- "low power"
- "turbo mode flags: %@"
- "v20@?0@\"NSString\"8I16"
- "\xf0\xf0a"

```
