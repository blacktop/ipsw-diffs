## CloudPhotoLibrary

> `/System/Library/PrivateFrameworks/CloudPhotoLibrary.framework/Versions/A/CloudPhotoLibrary`

```diff

-  __TEXT.__text: 0x1e45b0
-  __TEXT.__objc_methlist: 0x15c6c
+  __TEXT.__text: 0x1e51e4
+  __TEXT.__objc_methlist: 0x15c54
   __TEXT.__const: 0x328
-  __TEXT.__gcc_except_tab: 0x4d14
-  __TEXT.__oslogstring: 0x16bbf
-  __TEXT.__cstring: 0x18c0f
-  __TEXT.__unwind_info: 0x6d10
+  __TEXT.__gcc_except_tab: 0x4d80
+  __TEXT.__oslogstring: 0x16ad2
+  __TEXT.__cstring: 0x18c54
+  __TEXT.__unwind_info: 0x6d70
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1120
-  __DATA_CONST.__objc_classlist: 0x9e0
+  __DATA_CONST.__const: 0x1138
+  __DATA_CONST.__objc_classlist: 0x9e8
   __DATA_CONST.__objc_catlist: 0x90
-  __DATA_CONST.__objc_protolist: 0x190
+  __DATA_CONST.__objc_protolist: 0x1b0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x92a8
+  __DATA_CONST.__objc_selrefs: 0x9280
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x948
   __DATA_CONST.__objc_arraydata: 0x1438
-  __DATA_CONST.__got: 0xb20
+  __DATA_CONST.__got: 0xb40
   __AUTH_CONST.__const: 0x9820
   __AUTH_CONST.__cfstring: 0x17960
-  __AUTH_CONST.__objc_const: 0x23680
-  __AUTH_CONST.__objc_intobj: 0x750
+  __AUTH_CONST.__objc_const: 0x238b0
+  __AUTH_CONST.__objc_intobj: 0x768
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_dictobj: 0x140
   __AUTH_CONST.__objc_floatobj: 0x50
-  __AUTH_CONST.__auth_got: 0x5c8
-  __AUTH.__objc_data: 0x960
+  __AUTH_CONST.__auth_got: 0x5d8
+  __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x1c08
-  __DATA.__data: 0x1480
-  __DATA.__bss: 0xb78
+  __DATA.__data: 0x1600
+  __DATA.__bss: 0xb48
   __DATA.__common: 0x28
-  __DATA_DIRTY.__objc_data: 0x5960
-  __DATA_DIRTY.__bss: 0x3f0
+  __DATA_DIRTY.__objc_data: 0x62c0
+  __DATA_DIRTY.__bss: 0x430
   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/Versions/A/ProtocolBuffer
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 9878
-  Symbols:   20294
-  CStrings:  8404
+  Functions: 9893
+  Symbols:   20314
+  CStrings:  8398
 
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
+ GCC_except_table1156
+ GCC_except_table1232
+ GCC_except_table1286
+ GCC_except_table1291
+ GCC_except_table1330
+ GCC_except_table1350
+ GCC_except_table1352
+ GCC_except_table1526
+ GCC_except_table1575
+ GCC_except_table1579
+ GCC_except_table1581
+ GCC_except_table1586
+ GCC_except_table1596
+ GCC_except_table1598
+ GCC_except_table1605
+ GCC_except_table1608
+ GCC_except_table1617
+ GCC_except_table1619
+ GCC_except_table1621
+ GCC_except_table1623
+ GCC_except_table1705
+ GCC_except_table1793
+ GCC_except_table2046
+ GCC_except_table2056
+ GCC_except_table2282
+ GCC_except_table2283
+ GCC_except_table2286
+ GCC_except_table2293
+ GCC_except_table2297
+ GCC_except_table2324
+ GCC_except_table2331
+ GCC_except_table2341
+ GCC_except_table2344
+ GCC_except_table2533
+ GCC_except_table259
+ GCC_except_table2634
+ GCC_except_table2708
+ GCC_except_table274
+ GCC_except_table2749
+ GCC_except_table280
+ GCC_except_table283
+ GCC_except_table2841
+ GCC_except_table2848
+ GCC_except_table285
+ GCC_except_table287
+ GCC_except_table3001
+ GCC_except_table3090
+ GCC_except_table317
+ GCC_except_table3380
+ GCC_except_table3382
+ GCC_except_table3486
+ GCC_except_table3497
+ GCC_except_table3552
+ GCC_except_table3554
+ GCC_except_table3665
+ GCC_except_table3689
+ GCC_except_table3783
+ GCC_except_table3787
+ GCC_except_table3789
+ GCC_except_table3791
+ GCC_except_table3795
+ GCC_except_table3956
+ GCC_except_table4005
+ GCC_except_table402
+ GCC_except_table4250
+ GCC_except_table4335
+ GCC_except_table4339
+ GCC_except_table4341
+ GCC_except_table4350
+ GCC_except_table452
+ GCC_except_table4555
+ GCC_except_table4569
+ GCC_except_table467
+ GCC_except_table4729
+ GCC_except_table4759
+ GCC_except_table4796
+ GCC_except_table4814
+ GCC_except_table4827
+ GCC_except_table4835
+ GCC_except_table4837
+ GCC_except_table4851
+ GCC_except_table4853
+ GCC_except_table4856
+ GCC_except_table5228
+ GCC_except_table5261
+ GCC_except_table5263
+ GCC_except_table5289
+ GCC_except_table540
+ GCC_except_table5423
+ GCC_except_table5433
+ GCC_except_table544
+ GCC_except_table5491
+ GCC_except_table5494
+ GCC_except_table560
+ GCC_except_table5672
+ GCC_except_table5682
+ GCC_except_table5774
+ GCC_except_table5778
+ GCC_except_table5784
+ GCC_except_table5792
+ GCC_except_table5808
+ GCC_except_table5814
+ GCC_except_table582
+ GCC_except_table5861
+ GCC_except_table5868
+ GCC_except_table5872
+ GCC_except_table5898
+ GCC_except_table5903
+ GCC_except_table5905
+ GCC_except_table5907
+ GCC_except_table5909
+ GCC_except_table5911
+ GCC_except_table5913
+ GCC_except_table5915
+ GCC_except_table5918
+ GCC_except_table5925
+ GCC_except_table5927
+ GCC_except_table5930
+ GCC_except_table5932
+ GCC_except_table5977
+ GCC_except_table5979
+ GCC_except_table5981
+ GCC_except_table5993
+ GCC_except_table601
+ GCC_except_table611
+ GCC_except_table6144
+ GCC_except_table6186
+ GCC_except_table6197
+ GCC_except_table6256
+ GCC_except_table6259
+ GCC_except_table629
+ GCC_except_table6344
+ GCC_except_table6346
+ GCC_except_table6362
+ GCC_except_table6385
+ GCC_except_table6401
+ GCC_except_table6403
+ GCC_except_table642
+ GCC_except_table6563
+ GCC_except_table6591
+ GCC_except_table6634
+ GCC_except_table6656
+ GCC_except_table6690
+ GCC_except_table6702
+ GCC_except_table6731
+ GCC_except_table6758
+ GCC_except_table6762
+ GCC_except_table6788
+ GCC_except_table6820
+ GCC_except_table6861
+ GCC_except_table6926
+ GCC_except_table6952
+ GCC_except_table6956
+ GCC_except_table6965
+ GCC_except_table6983
+ GCC_except_table7001
+ GCC_except_table7010
+ GCC_except_table7011
+ GCC_except_table7025
+ GCC_except_table7083
+ GCC_except_table7209
+ GCC_except_table7223
+ GCC_except_table7226
+ GCC_except_table7353
+ GCC_except_table7355
+ GCC_except_table7357
+ GCC_except_table7361
+ GCC_except_table7364
+ GCC_except_table757
+ GCC_except_table7738
+ GCC_except_table7784
+ GCC_except_table7786
+ GCC_except_table7807
+ GCC_except_table7821
+ GCC_except_table7825
+ GCC_except_table7833
+ GCC_except_table7836
+ GCC_except_table7856
+ GCC_except_table7863
+ GCC_except_table7886
+ GCC_except_table791
+ GCC_except_table7921
+ GCC_except_table795
+ GCC_except_table7952
+ GCC_except_table7963
+ GCC_except_table798
+ GCC_except_table7985
+ GCC_except_table7988
+ GCC_except_table7990
+ GCC_except_table7992
+ GCC_except_table800
+ GCC_except_table8023
+ GCC_except_table803
+ GCC_except_table805
+ GCC_except_table8073
+ GCC_except_table809
+ GCC_except_table811
+ GCC_except_table820
+ GCC_except_table8217
+ GCC_except_table822
+ GCC_except_table824
+ GCC_except_table8240
+ GCC_except_table826
+ GCC_except_table8270
+ GCC_except_table828
+ GCC_except_table830
+ GCC_except_table832
+ GCC_except_table834
+ GCC_except_table836
+ GCC_except_table838
+ GCC_except_table840
+ GCC_except_table8418
+ GCC_except_table842
+ GCC_except_table8420
+ GCC_except_table8450
+ GCC_except_table8459
+ GCC_except_table8464
+ GCC_except_table8480
+ GCC_except_table8495
+ GCC_except_table850
+ GCC_except_table8507
+ GCC_except_table8512
+ GCC_except_table852
+ GCC_except_table854
+ GCC_except_table856
+ GCC_except_table858
+ GCC_except_table8596
+ GCC_except_table867
+ GCC_except_table8685
+ GCC_except_table869
+ GCC_except_table871
+ GCC_except_table873
+ GCC_except_table8744
+ GCC_except_table875
+ GCC_except_table877
+ GCC_except_table879
+ GCC_except_table881
+ GCC_except_table8822
+ GCC_except_table883
+ GCC_except_table8837
+ GCC_except_table885
+ GCC_except_table8859
+ GCC_except_table8865
+ GCC_except_table887
+ GCC_except_table8884
+ GCC_except_table8894
+ GCC_except_table8936
+ GCC_except_table8939
+ GCC_except_table8943
+ GCC_except_table8947
+ GCC_except_table9029
+ GCC_except_table907
+ GCC_except_table913
+ GCC_except_table922
+ GCC_except_table933
+ GCC_except_table949
+ OBJC_IVAR_$_CPLConfiguration._delegate
+ OBJC_IVAR_$_CPLEngineScheduler._turboMode
+ OBJC_IVAR_$_CPLEngineSystemMonitor._lastNetworkState
+ OBJC_IVAR_$_CPLEngineSystemMonitor._turboSyncObserver
+ OBJC_IVAR_$_CPLSyncSession._blocked
+ OBJC_IVAR_$_CPLSyncSession._forcesBypassBackgroundScheduling
+ OBJC_IVAR_$_CPLTurboSyncObserver._lastNetworkState
+ _CFNotificationCenterGetDistributedCenter
+ _CPLRequestEngine
+ _CPLSetRequestEngineBlock
+ _CPLSyncSessionPredictionTypeTurboMode
+ _OBJC_CLASS_$_CPLPredictionFlagFormatter
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
+ ___block_descriptor_41_e8_32s_e8_v16?0Q8l
+ _dispatch_get_global_queue
+ _objc_msgSend$configurationDidUpdate:
+ _objc_msgSend$expirationDate
+ _objc_msgSend$iCloudLibraryClientNeedsToVerifyTerms
+ _objc_msgSend$isBadQuality
+ _objc_msgSend$isSufficentlyDifferentFromNetworkState:
+ _objc_msgSend$keywords
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
- -[CPLEngineSystemMonitor _updateCanUseTurboModeOnScheduler]
- -[CPLSyncSession usesTurboMode]
- GCC_except_table1151
- GCC_except_table1224
- GCC_except_table1278
- GCC_except_table1283
- GCC_except_table1322
- GCC_except_table1342
- GCC_except_table1344
- GCC_except_table1518
- GCC_except_table1567
- GCC_except_table1571
- GCC_except_table1573
- GCC_except_table1578
- GCC_except_table1580
- GCC_except_table1590
- GCC_except_table1597
- GCC_except_table1600
- GCC_except_table1603
- GCC_except_table1609
- GCC_except_table1613
- GCC_except_table1615
- GCC_except_table1697
- GCC_except_table1785
- GCC_except_table2038
- GCC_except_table2048
- GCC_except_table2274
- GCC_except_table2275
- GCC_except_table2278
- GCC_except_table2285
- GCC_except_table2289
- GCC_except_table2316
- GCC_except_table2323
- GCC_except_table2333
- GCC_except_table2336
- GCC_except_table2525
- GCC_except_table258
- GCC_except_table2626
- GCC_except_table2692
- GCC_except_table273
- GCC_except_table2741
- GCC_except_table279
- GCC_except_table282
- GCC_except_table2833
- GCC_except_table284
- GCC_except_table2840
- GCC_except_table286
- GCC_except_table2993
- GCC_except_table3082
- GCC_except_table316
- GCC_except_table3368
- GCC_except_table3370
- GCC_except_table3452
- GCC_except_table3456
- GCC_except_table3466
- GCC_except_table3476
- GCC_except_table3534
- GCC_except_table3536
- GCC_except_table3666
- GCC_except_table3690
- GCC_except_table3784
- GCC_except_table3788
- GCC_except_table3790
- GCC_except_table3792
- GCC_except_table3796
- GCC_except_table3957
- GCC_except_table4006
- GCC_except_table401
- GCC_except_table4251
- GCC_except_table4336
- GCC_except_table4340
- GCC_except_table4342
- GCC_except_table4351
- GCC_except_table451
- GCC_except_table4554
- GCC_except_table4568
- GCC_except_table466
- GCC_except_table4728
- GCC_except_table4758
- GCC_except_table4795
- GCC_except_table4813
- GCC_except_table4826
- GCC_except_table4834
- GCC_except_table4836
- GCC_except_table4850
- GCC_except_table4852
- GCC_except_table4855
- GCC_except_table5227
- GCC_except_table5260
- GCC_except_table5262
- GCC_except_table5288
- GCC_except_table539
- GCC_except_table5422
- GCC_except_table543
- GCC_except_table5432
- GCC_except_table5490
- GCC_except_table5493
- GCC_except_table559
- GCC_except_table5671
- GCC_except_table5681
- GCC_except_table5773
- GCC_except_table5777
- GCC_except_table5783
- GCC_except_table5791
- GCC_except_table5806
- GCC_except_table581
- GCC_except_table5813
- GCC_except_table5860
- GCC_except_table5867
- GCC_except_table5871
- GCC_except_table5897
- GCC_except_table5902
- GCC_except_table5904
- GCC_except_table5906
- GCC_except_table5908
- GCC_except_table5910
- GCC_except_table5912
- GCC_except_table5914
- GCC_except_table5917
- GCC_except_table5924
- GCC_except_table5926
- GCC_except_table5928
- GCC_except_table5931
- GCC_except_table5976
- GCC_except_table5978
- GCC_except_table5980
- GCC_except_table599
- GCC_except_table5992
- GCC_except_table610
- GCC_except_table6143
- GCC_except_table6185
- GCC_except_table6195
- GCC_except_table6255
- GCC_except_table6258
- GCC_except_table628
- GCC_except_table6343
- GCC_except_table6345
- GCC_except_table6361
- GCC_except_table6384
- GCC_except_table6400
- GCC_except_table6402
- GCC_except_table641
- GCC_except_table6562
- GCC_except_table6590
- GCC_except_table6631
- GCC_except_table6653
- GCC_except_table6687
- GCC_except_table6699
- GCC_except_table6728
- GCC_except_table6755
- GCC_except_table6759
- GCC_except_table6785
- GCC_except_table6817
- GCC_except_table6858
- GCC_except_table6921
- GCC_except_table6947
- GCC_except_table6951
- GCC_except_table6960
- GCC_except_table6978
- GCC_except_table6991
- GCC_except_table7005
- GCC_except_table7006
- GCC_except_table7020
- GCC_except_table7078
- GCC_except_table7204
- GCC_except_table7218
- GCC_except_table7221
- GCC_except_table7348
- GCC_except_table7350
- GCC_except_table7352
- GCC_except_table7356
- GCC_except_table7359
- GCC_except_table756
- GCC_except_table7732
- GCC_except_table7774
- GCC_except_table7778
- GCC_except_table7795
- GCC_except_table7809
- GCC_except_table7819
- GCC_except_table7827
- GCC_except_table7830
- GCC_except_table7850
- GCC_except_table7857
- GCC_except_table7880
- GCC_except_table790
- GCC_except_table7915
- GCC_except_table794
- GCC_except_table7946
- GCC_except_table7957
- GCC_except_table797
- GCC_except_table7979
- GCC_except_table7982
- GCC_except_table7984
- GCC_except_table7986
- GCC_except_table799
- GCC_except_table8017
- GCC_except_table802
- GCC_except_table804
- GCC_except_table8067
- GCC_except_table808
- GCC_except_table810
- GCC_except_table819
- GCC_except_table8209
- GCC_except_table821
- GCC_except_table823
- GCC_except_table8232
- GCC_except_table825
- GCC_except_table8262
- GCC_except_table827
- GCC_except_table829
- GCC_except_table831
- GCC_except_table833
- GCC_except_table835
- GCC_except_table837
- GCC_except_table839
- GCC_except_table841
- GCC_except_table8410
- GCC_except_table8412
- GCC_except_table8442
- GCC_except_table8451
- GCC_except_table8456
- GCC_except_table8472
- GCC_except_table8487
- GCC_except_table849
- GCC_except_table8499
- GCC_except_table8504
- GCC_except_table851
- GCC_except_table853
- GCC_except_table855
- GCC_except_table857
- GCC_except_table8588
- GCC_except_table866
- GCC_except_table8677
- GCC_except_table868
- GCC_except_table870
- GCC_except_table872
- GCC_except_table8736
- GCC_except_table874
- GCC_except_table876
- GCC_except_table878
- GCC_except_table880
- GCC_except_table8814
- GCC_except_table882
- GCC_except_table8829
- GCC_except_table8851
- GCC_except_table8857
- GCC_except_table8876
- GCC_except_table8886
- GCC_except_table8928
- GCC_except_table8930
- GCC_except_table9014
- GCC_except_table902
- GCC_except_table908
- GCC_except_table917
- GCC_except_table928
- GCC_except_table944
- OBJC_IVAR_$_CPLEngineScheduler._canUseTurboMode
- OBJC_IVAR_$_CPLEngineScheduler._isUsingTurboMode
- OBJC_IVAR_$_CPLEngineScheduler._turboModeLock
- OBJC_IVAR_$_CPLEngineScheduler._turboModeObserver
- OBJC_IVAR_$_CPLEngineSystemMonitor._hasSetupBatteryMonitor
- OBJC_IVAR_$_CPLEngineSystemMonitor._turboModeFlags
- OBJC_IVAR_$_CPLSyncSession._usesTurboMode
- ___40-[CPLEngineScheduler shouldUseTurboMode]_block_invoke
- ___41-[CPLEngineScheduler setCanUseTurboMode:]_block_invoke
- ___45-[CPLEngineScheduler _updateTurboModeOnQueue]_block_invoke
- ___48-[CPLEngineScheduler openWithCompletionHandler:]_block_invoke_3
- ___50-[CPLEngineScheduler _turboModeSettingsHasChanged]_block_invoke
- ___block_descriptor_40_e8_32s_e21_v20?0"NSString"8I16l
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
- _objc_msgSend$_justInCaseSessionIsPossible
- _objc_msgSend$_keepSessionInformation:
- _objc_msgSend$_noteServerIsUnavailableWithErrorLocked:reason:
- _objc_msgSend$_noteSignificantEvent
- _objc_msgSend$_noteSyncSession:failedDuringPhase:withError:
- _objc_msgSend$_noteSyncSessionNeededFromState:proposedScheduleDate:
- _objc_msgSend$_noteSyncSessionNeededFromStateDontRewindImmediately:
- _objc_msgSend$_prepareFirstSession
- _objc_msgSend$_reallyNoteServerHasChangesLocked
- _objc_msgSend$_reallyStartSyncSession:
- _objc_msgSend$_reallyUnscheduleSession
- _objc_msgSend$_scheduleNextSyncSession
- _objc_msgSend$_setRequiredFirstState:
- _objc_msgSend$_startOverridingBudget:reason:
- _objc_msgSend$_startRequiredSyncSession:
- _objc_msgSend$_startSyncSession:withMinimalPhase:rewind:
- _objc_msgSend$_stopOverridingBudget:reason:
- _objc_msgSend$_stopPreparingFirstSession
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
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLBackgroundActivity.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLBeforeUploadCheckItems.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLCallObserver.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLDirectUploadTask.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLEngineDerivativesCache.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLEngineForceSyncTask.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLEngineLibrary.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLEngineScheduler.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLEngineSyncManager.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLEngineSyncTask.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLEngineSystemMonitor.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLEngineTransport.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLEngineUIObservationCenter.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLFileWatcher.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLGenerateDerivativesSubtask.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLMingleChangesTask.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLMingleUtility.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLNetworkWatcher.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLPowerAssertion.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLProcessStagedScopesTask.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLPullFromTransportTask.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLPushToTransportTask.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLScopeUpdateTask.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLSyncSession.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLSyncStep.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLTransaction.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLTransportScopeMapping.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLUIObservedSource.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLUIRecordObservedSource.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLUIScopeObservedSource.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLUISyncActivityObservedSource.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLUIUploadProgressHub.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLUploadComputeStatesAccumulator.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLUploadComputeStatesTask.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLUploadPushedChangesTask.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/cloudphotolibrary/Engine/Feedback/CPLEngineFeedbackManager.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/cloudphotolibrary/Engine/Feedback/CPLFeedbackMessage.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/cloudphotolibrary/Engine/Storage/CPLBatchExtractionStep.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/cloudphotolibrary/Engine/Storage/CPLBatchExtractionStrategy.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/cloudphotolibrary/Engine/Storage/CPLChangeBatchChangeStorage.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/cloudphotolibrary/Engine/Storage/CPLChangeSessionUpdate.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/cloudphotolibrary/Engine/Storage/CPLChangedRecordStorageView.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/cloudphotolibrary/Engine/Storage/CPLClientCacheView_Extensions.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/cloudphotolibrary/Engine/Storage/CPLEngineCloudCache.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/cloudphotolibrary/Engine/Storage/CPLEngineFileStorage.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/cloudphotolibrary/Engine/Storage/CPLEngineIDMapping.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/cloudphotolibrary/Engine/Storage/CPLEngineOutgoingResources.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/cloudphotolibrary/Engine/Storage/CPLEnginePushRepository.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/cloudphotolibrary/Engine/Storage/CPLEngineResourceDownloadQueue.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/cloudphotolibrary/Engine/Storage/CPLEngineResourceStorage.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/cloudphotolibrary/Engine/Storage/CPLEngineScope.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/cloudphotolibrary/Engine/Storage/CPLEngineScopeStorage.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/cloudphotolibrary/Engine/Storage/CPLEngineStorage.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/cloudphotolibrary/Engine/Storage/CPLEngineStorageViews.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/cloudphotolibrary/Engine/Storage/CPLEngineStore.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/cloudphotolibrary/Engine/Storage/CPLEngineTransientRepository.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/cloudphotolibrary/Engine/Storage/CPLEngineTransientRepositoryBatchStorage.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/cloudphotolibrary/Engine/Storage/CPLExtractedBatch.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/cloudphotolibrary/Engine/Storage/CPLFeature.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/cloudphotolibrary/Engine/Storage/CPLRecordStorageView.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/cloudphotolibrary/Engine/Storage/CPLSharedBatchStorage.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLAlbumChange.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLAssetChange.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLBase.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLChangeBatch.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLChangeSession.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLCommentChange.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLConfiguration.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLConfigurationDictionary.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLContainerChange.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLErrors.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLFaceAnalysisReference.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLFaceCropChange.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLFingerprintContext.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLFingerprintScheme.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLForceSyncTask.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLItemChange.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLLibraryManager.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLLibraryParameters.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLMasterChange.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLPersonChange.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLPlatform.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLPullChangeSession.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLPushChangeSession.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLPushSessionTracker.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLRecordChange.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLRecordTarget.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLResource.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLResourceIdentity.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLResourceTransferTask.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLSchemaFilter.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLScopeChange.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLScopedIdentifier.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLSocialGroupChange.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLStatus.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLTransportContainerConfiguration.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLTurboSyncObserver.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLUIObserver.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLUIRecordObserver.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLUIScopeObserver.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/NSObject+CPLCodingProxy.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/cloudphotolibrary/Implementations/Daemon/CPLProxyLibraryManager.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/cloudphotolibrary/Implementations/Daemon/CPLProxySession.m"
+ "CPLEPPAutoEnable"
+ "CloudPhotoLibrary-910.28.103"
+ "com.apple.cpl.epp-auto-enable"
+ "com.apple.cpl.wantsdaemon.notification"
+ "iCloudLibraryClientNeedsToVerifyTerms"
+ "low power mode: enabled"
+ "turbo mode"
+ "turboMode"
+ "\xf0\xf0Q"
- "\nTurbo mode%s: expires %@"
- " (blocked)"
- " turbo"
- "%@ (%i)"
- "%@ (unkn.)"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLBackgroundActivity.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLBeforeUploadCheckItems.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLCallObserver.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLDirectUploadTask.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLEngineDerivativesCache.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLEngineForceSyncTask.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLEngineLibrary.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLEngineScheduler.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLEngineSyncManager.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLEngineSyncTask.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLEngineSystemMonitor.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLEngineTransport.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLEngineUIObservationCenter.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLFileWatcher.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLGenerateDerivativesSubtask.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLMingleChangesTask.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLMingleUtility.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLNetworkWatcher.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLPowerAssertion.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLProcessStagedScopesTask.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLPullFromTransportTask.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLPushToTransportTask.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLScopeUpdateTask.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLSyncSession.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLSyncStep.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLTransaction.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLTransportScopeMapping.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLUIObservedSource.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLUIRecordObservedSource.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLUIScopeObservedSource.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLUISyncActivityObservedSource.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLUIUploadProgressHub.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLUploadComputeStatesAccumulator.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLUploadComputeStatesTask.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/workspaces/cloudphotolibrary/Engine/CPLUploadPushedChangesTask.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/workspaces/cloudphotolibrary/Engine/Feedback/CPLEngineFeedbackManager.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/workspaces/cloudphotolibrary/Engine/Feedback/CPLFeedbackMessage.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/workspaces/cloudphotolibrary/Engine/Storage/CPLBatchExtractionStep.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/workspaces/cloudphotolibrary/Engine/Storage/CPLBatchExtractionStrategy.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/workspaces/cloudphotolibrary/Engine/Storage/CPLChangeBatchChangeStorage.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/workspaces/cloudphotolibrary/Engine/Storage/CPLChangeSessionUpdate.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/workspaces/cloudphotolibrary/Engine/Storage/CPLChangedRecordStorageView.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/workspaces/cloudphotolibrary/Engine/Storage/CPLClientCacheView_Extensions.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/workspaces/cloudphotolibrary/Engine/Storage/CPLEngineCloudCache.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/workspaces/cloudphotolibrary/Engine/Storage/CPLEngineFileStorage.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/workspaces/cloudphotolibrary/Engine/Storage/CPLEngineIDMapping.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/workspaces/cloudphotolibrary/Engine/Storage/CPLEngineOutgoingResources.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/workspaces/cloudphotolibrary/Engine/Storage/CPLEnginePushRepository.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/workspaces/cloudphotolibrary/Engine/Storage/CPLEngineResourceDownloadQueue.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/workspaces/cloudphotolibrary/Engine/Storage/CPLEngineResourceStorage.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/workspaces/cloudphotolibrary/Engine/Storage/CPLEngineScope.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/workspaces/cloudphotolibrary/Engine/Storage/CPLEngineScopeStorage.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/workspaces/cloudphotolibrary/Engine/Storage/CPLEngineStorage.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/workspaces/cloudphotolibrary/Engine/Storage/CPLEngineStorageViews.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/workspaces/cloudphotolibrary/Engine/Storage/CPLEngineStore.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/workspaces/cloudphotolibrary/Engine/Storage/CPLEngineTransientRepository.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/workspaces/cloudphotolibrary/Engine/Storage/CPLEngineTransientRepositoryBatchStorage.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/workspaces/cloudphotolibrary/Engine/Storage/CPLExtractedBatch.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/workspaces/cloudphotolibrary/Engine/Storage/CPLFeature.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/workspaces/cloudphotolibrary/Engine/Storage/CPLRecordStorageView.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/workspaces/cloudphotolibrary/Engine/Storage/CPLSharedBatchStorage.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLAlbumChange.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLAssetChange.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLBase.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLChangeBatch.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLChangeSession.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLCommentChange.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLConfiguration.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLConfigurationDictionary.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLContainerChange.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLErrors.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLFaceAnalysisReference.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLFaceCropChange.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLFingerprintContext.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLFingerprintScheme.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLForceSyncTask.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLItemChange.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLLibraryManager.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLLibraryParameters.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLMasterChange.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLPersonChange.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLPlatform.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLPullChangeSession.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLPushChangeSession.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLPushSessionTracker.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLRecordChange.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLRecordTarget.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLResource.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLResourceIdentity.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLResourceTransferTask.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLSchemaFilter.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLScopeChange.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLScopedIdentifier.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLSocialGroupChange.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLStatus.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLTransportContainerConfiguration.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLTurboSyncObserver.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLUIObserver.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLUIRecordObserver.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/CPLUIScopeObserver.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/workspaces/cloudphotolibrary/Framework/Sources/NSObject+CPLCodingProxy.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/workspaces/cloudphotolibrary/Implementations/Daemon/CPLProxyLibraryManager.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/workspaces/cloudphotolibrary/Implementations/Daemon/CPLProxySession.m"
- "Can use turbo mode: %@"
- "Cancelling discretionary %@ because turbo mode has been enabled"
- "Cancelling non-discretionary %@ because turbo mode has been disabled"
- "CloudPhotoLibrary-910.22.101"
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
