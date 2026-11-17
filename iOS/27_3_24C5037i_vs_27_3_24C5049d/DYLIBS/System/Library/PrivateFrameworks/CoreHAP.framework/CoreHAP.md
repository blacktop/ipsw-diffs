## CoreHAP

> `/System/Library/PrivateFrameworks/CoreHAP.framework/CoreHAP`

```diff

-1535.0.0.0.2
-  __TEXT.__text: 0x30f7e8
-  __TEXT.__objc_methlist: 0x1d1a8
-  __TEXT.__const: 0x1aa8
+1535.3.8.0.0
+  __TEXT.__text: 0x318768
+  __TEXT.__objc_methlist: 0x1d550
+  __TEXT.__const: 0x1af0
   __TEXT.__dlopen_cstrs: 0x4e
-  __TEXT.__constg_swiftt: 0xd6c
-  __TEXT.__swift5_typeref: 0x567
-  __TEXT.__swift5_reflstr: 0x927
-  __TEXT.__swift5_fieldmd: 0x748
+  __TEXT.__constg_swiftt: 0xe0c
+  __TEXT.__swift5_typeref: 0x58d
   __TEXT.__swift5_builtin: 0xf0
+  __TEXT.__swift5_reflstr: 0x9a1
+  __TEXT.__swift5_fieldmd: 0x778
   __TEXT.__swift5_assocty: 0x198
   __TEXT.__swift5_proto: 0x8c
   __TEXT.__swift5_types: 0x64
-  __TEXT.__cstring: 0x19245
-  __TEXT.__oslogstring: 0x4cebb
-  __TEXT.__swift5_capture: 0x2c0
+  __TEXT.__cstring: 0x19382
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__gcc_except_tab: 0x71a0
-  __TEXT.__unwind_info: 0xa260
+  __TEXT.__oslogstring: 0x4ea5d
+  __TEXT.__swift5_capture: 0x350
+  __TEXT.__gcc_except_tab: 0x728c
+  __TEXT.__unwind_info: 0xa488
   __TEXT.__eh_frame: 0x10e8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x6868
-  __DATA_CONST.__objc_classlist: 0xdd8
+  __DATA_CONST.__const: 0x69e0
+  __DATA_CONST.__objc_classlist: 0xde8
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x3f0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9b30
+  __DATA_CONST.__objc_selrefs: 0x9d98
   __DATA_CONST.__objc_protorefs: 0x110
-  __DATA_CONST.__objc_superrefs: 0xc00
+  __DATA_CONST.__objc_superrefs: 0xc10
   __DATA_CONST.__objc_arraydata: 0x200
-  __DATA_CONST.__got: 0x1208
-  __AUTH_CONST.__const: 0x1b00
-  __AUTH_CONST.__cfstring: 0x11b60
-  __AUTH_CONST.__objc_const: 0x32ff0
+  __DATA_CONST.__got: 0x1218
+  __AUTH_CONST.__const: 0x1cf8
+  __AUTH_CONST.__cfstring: 0x11c20
+  __AUTH_CONST.__objc_const: 0x33618
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_intobj: 0x780
   __AUTH_CONST.__objc_floatobj: 0x20
   __AUTH_CONST.__objc_doubleobj: 0x40
   __AUTH_CONST.__objc_arrayobj: 0xc0
-  __AUTH_CONST.__auth_got: 0x14a0
-  __AUTH.__objc_data: 0x8830
-  __AUTH.__data: 0x138
+  __AUTH_CONST.__auth_got: 0x14d8
+  __AUTH.__objc_data: 0x8990
+  __AUTH.__data: 0x130
   __AUTH.__thread_vars: 0x30
   __AUTH.__thread_bss: 0x28
-  __DATA.__objc_ivar: 0x1e7c
-  __DATA.__data: 0x3250
+  __DATA.__objc_ivar: 0x1edc
+  __DATA.__data: 0x3268
   __DATA.__crash_info: 0x148
   __DATA.__common: 0x90
   __DATA_DIRTY.__objc_data: 0x1108

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 11695
-  Symbols:   19180
-  CStrings:  8059
+  Functions: 11854
+  Symbols:   19373
+  CStrings:  8156
 
Symbols:
+ +[HAP2CoAPIOThread libcoapLogLevel]
+ +[HAP2ThreadNetworkUtil _interfaceContainingIPv6Address:fromInterfaces:]
+ +[HAP2ThreadNetworkUtil isInfraIPv6Address:fromInterfaces:]
+ +[HAPNFCTagContents tagContentsWithNDEFMessage:tagIdentifier:technology:]
+ +[HAPNFCTagContents tagContentsWithNDEFMessageData:tagIdentifier:technology:]
+ -[HAP2AccessoryServerSecureTransportPairVerify _noteSessionStarted]
+ -[HAP2AccessoryServerSecureTransportPairVerify _reopenWaitMilliseconds]
+ -[HAP2AccessoryServerSecureTransportPairVerify _test_ageLastSessionStartByMilliseconds:]
+ -[HAP2AccessoryServerSecureTransportPairVerify _test_expireReopenWait]
+ -[HAP2AccessoryServerSecureTransportPairVerify didChangeStateWithError:]
+ -[HAP2CoAPClient _exchangeLocalCloseQoS:]
+ -[HAP2SerializedOperationQueue _highestUnfinishedQoSClass]
+ -[HAP2SerializedOperationQueue _releaseUnfinishedQoSLevel:]
+ -[HAP2SerializedOperationQueue _stampDiagnosticsOnOperation:enqueueTime:]
+ -[HAP2SerializedOperationQueue _trackUnfinishedOperation:qosClass:]
+ -[HAP2SerializedOperationQueue addConcurrentBlockWithQoS:block:]
+ -[HAP2SerializedOperationQueue highestUnfinishedQoSClass]
+ -[HAP2SerializedOperationQueue performBlockAtHighestUnfinishedQoS:]
+ -[HAPAccessoryServerBrowserNFC _beginDiscoveryEpisodePrewarming:]
+ -[HAPAccessoryServerBrowserNFC _isReadingDetectedTagContents]
+ -[HAPAccessoryServerBrowserNFC _scheduleRearmAfterDelay:]
+ -[HAPAccessoryServerBrowserNFC _startDiscoveringNFCAccessoryServerAsRetry:]
+ -[HAPAccessoryServerBrowserNFC _surfaceServerWithSetupPayload:tagContents:emulatedMFiToken:emulatedMFiTokenUUID:]
+ -[HAPAccessoryServerBrowserNFC busyRetryCount]
+ -[HAPAccessoryServerBrowserNFC commitAwaitingTagServer]
+ -[HAPAccessoryServerBrowserNFC nfcServerDidReleaseReaderAtM4:]
+ -[HAPAccessoryServerBrowserNFC nfcServerNeedsTagForCommit:]
+ -[HAPAccessoryServerBrowserNFC readsDetectedTagContents]
+ -[HAPAccessoryServerBrowserNFC rearmRetryGeneration]
+ -[HAPAccessoryServerBrowserNFC rearmRetryPending]
+ -[HAPAccessoryServerBrowserNFC setBusyRetryCount:]
+ -[HAPAccessoryServerBrowserNFC setCommitAwaitingTagServer:]
+ -[HAPAccessoryServerBrowserNFC setReadsDetectedTagContents:]
+ -[HAPAccessoryServerBrowserNFC setReadsTagContentsOnDetection:]
+ -[HAPAccessoryServerBrowserNFC setRearmRetryGeneration:]
+ -[HAPAccessoryServerBrowserNFC setRearmRetryPending:]
+ -[HAPAccessoryServerBrowserNFC setTagContentsReadSession:]
+ -[HAPAccessoryServerBrowserNFC tagContentsReadSession]
+ -[HAPAccessoryServerNFC _armReaderReleaseGraceTimer]
+ -[HAPAccessoryServerNFC _cancelReaderReleaseGrace]
+ -[HAPAccessoryServerNFC _failPairingWithAIDSelectionError:]
+ -[HAPAccessoryServerNFC _injectPrefetchedMFiTokenIntoPairSetupSession]
+ -[HAPAccessoryServerNFC _joinSharedCredentialFetchForKey:handler:]
+ -[HAPAccessoryServerNFC _makePairSetupSession]
+ -[HAPAccessoryServerNFC _mayReleaseReaderPastGracePeriod]
+ -[HAPAccessoryServerNFC _parkCommitUntilReadyForTag]
+ -[HAPAccessoryServerNFC _readerReleaseGracePeriodDidEndForGeneration:]
+ -[HAPAccessoryServerNFC _releaseReaderAtM4]
+ -[HAPAccessoryServerNFC _releaseReaderIfM5StillWaiting]
+ -[HAPAccessoryServerNFC _requestSharedNetworkCredentialsForKey:handler:fetch:]
+ -[HAPAccessoryServerNFC _runOnWorkQueue:]
+ -[HAPAccessoryServerNFC _startHAPPairSetupOnWorkQueue]
+ -[HAPAccessoryServerNFC abandonParkedCommit]
+ -[HAPAccessoryServerNFC awaitingTagForCommit]
+ -[HAPAccessoryServerNFC holdsTagThroughM6]
+ -[HAPAccessoryServerNFC pairSetupSession:lateMFiTokenForM4Hash:completionHandler:]
+ -[HAPAccessoryServerNFC prefetchedMFiTokenFromM4]
+ -[HAPAccessoryServerNFC readerReleaseGraceElapsed]
+ -[HAPAccessoryServerNFC readerReleaseGracePeriod]
+ -[HAPAccessoryServerNFC releasedReaderAtM4]
+ -[HAPAccessoryServerNFC setAwaitingTagForCommit:]
+ -[HAPAccessoryServerNFC setHoldsTagThroughM6:]
+ -[HAPAccessoryServerNFC setPrefetchedMFiTokenFromM4:]
+ -[HAPAccessoryServerNFC setReaderReleaseGraceElapsed:]
+ -[HAPAccessoryServerNFC setReaderReleaseGracePeriod:]
+ -[HAPAccessoryServerNFC setReleasedReaderAtM4:]
+ -[HAPAccessoryServerNFC setTagContents:]
+ -[HAPAccessoryServerNFC tagContents]
+ -[HAPNFCReaderSession readTagContentsWithCompletion:]
+ -[HAPNFCSharedCredentialFetch .cxx_destruct]
+ -[HAPNFCSharedCredentialFetch answer]
+ -[HAPNFCSharedCredentialFetch init]
+ -[HAPNFCSharedCredentialFetch setAnswer:]
+ -[HAPNFCSharedCredentialFetch waitingHandlers]
+ -[HAPNFCTagContents .cxx_destruct]
+ -[HAPNFCTagContents hapSetupPayloadURLString]
+ -[HAPNFCTagContents initWithSetupPayloadURLStrings:mfiToken:mfiTokenUUID:tagIdentifier:technology:]
+ -[HAPNFCTagContents mfiTokenUUID]
+ -[HAPNFCTagContents mfiToken]
+ -[HAPNFCTagContents setupPayloadURLStrings]
+ -[HAPNFCTagContents tagIdentifier]
+ -[HAPNFCTagContents technology]
+ GCC_except_table10129
+ GCC_except_table10167
+ GCC_except_table10204
+ GCC_except_table10332
+ GCC_except_table10334
+ GCC_except_table10336
+ GCC_except_table10338
+ GCC_except_table10342
+ GCC_except_table10352
+ GCC_except_table10355
+ GCC_except_table10359
+ GCC_except_table10366
+ GCC_except_table10372
+ GCC_except_table10377
+ GCC_except_table10380
+ GCC_except_table10385
+ GCC_except_table10390
+ GCC_except_table10393
+ GCC_except_table10396
+ GCC_except_table10422
+ GCC_except_table10425
+ GCC_except_table10426
+ GCC_except_table10470
+ GCC_except_table10471
+ GCC_except_table10472
+ GCC_except_table10474
+ GCC_except_table10475
+ GCC_except_table10477
+ GCC_except_table10478
+ GCC_except_table10479
+ GCC_except_table10481
+ GCC_except_table10482
+ GCC_except_table10484
+ GCC_except_table10488
+ GCC_except_table10489
+ GCC_except_table10495
+ GCC_except_table10547
+ GCC_except_table10554
+ GCC_except_table10665
+ GCC_except_table10667
+ GCC_except_table10669
+ GCC_except_table10672
+ GCC_except_table10674
+ GCC_except_table10676
+ GCC_except_table10678
+ GCC_except_table10679
+ GCC_except_table10686
+ GCC_except_table10688
+ GCC_except_table10689
+ GCC_except_table10737
+ GCC_except_table10739
+ GCC_except_table10741
+ GCC_except_table10743
+ GCC_except_table1102
+ GCC_except_table1660
+ GCC_except_table1665
+ GCC_except_table1667
+ GCC_except_table1681
+ GCC_except_table1693
+ GCC_except_table1695
+ GCC_except_table1697
+ GCC_except_table1699
+ GCC_except_table1829
+ GCC_except_table1833
+ GCC_except_table1835
+ GCC_except_table2063
+ GCC_except_table2283
+ GCC_except_table2285
+ GCC_except_table2290
+ GCC_except_table2296
+ GCC_except_table2298
+ GCC_except_table2304
+ GCC_except_table2306
+ GCC_except_table2310
+ GCC_except_table2318
+ GCC_except_table2322
+ GCC_except_table2328
+ GCC_except_table2330
+ GCC_except_table2332
+ GCC_except_table2334
+ GCC_except_table2340
+ GCC_except_table2344
+ GCC_except_table235
+ GCC_except_table2352
+ GCC_except_table2354
+ GCC_except_table236
+ GCC_except_table2367
+ GCC_except_table237
+ GCC_except_table2375
+ GCC_except_table2382
+ GCC_except_table2386
+ GCC_except_table2390
+ GCC_except_table2433
+ GCC_except_table244
+ GCC_except_table245
+ GCC_except_table252
+ GCC_except_table2549
+ GCC_except_table2553
+ GCC_except_table2554
+ GCC_except_table2556
+ GCC_except_table2558
+ GCC_except_table2570
+ GCC_except_table2575
+ GCC_except_table2579
+ GCC_except_table2582
+ GCC_except_table2584
+ GCC_except_table2587
+ GCC_except_table260
+ GCC_except_table2604
+ GCC_except_table2618
+ GCC_except_table262
+ GCC_except_table2623
+ GCC_except_table2626
+ GCC_except_table2631
+ GCC_except_table2634
+ GCC_except_table2638
+ GCC_except_table264
+ GCC_except_table2643
+ GCC_except_table265
+ GCC_except_table2654
+ GCC_except_table2666
+ GCC_except_table2677
+ GCC_except_table270
+ GCC_except_table2719
+ GCC_except_table2720
+ GCC_except_table2721
+ GCC_except_table2723
+ GCC_except_table2724
+ GCC_except_table2725
+ GCC_except_table2727
+ GCC_except_table2731
+ GCC_except_table2732
+ GCC_except_table2766
+ GCC_except_table2768
+ GCC_except_table2772
+ GCC_except_table2776
+ GCC_except_table279
+ GCC_except_table283
+ GCC_except_table287
+ GCC_except_table289
+ GCC_except_table29
+ GCC_except_table2940
+ GCC_except_table2951
+ GCC_except_table2955
+ GCC_except_table2969
+ GCC_except_table2975
+ GCC_except_table2977
+ GCC_except_table2980
+ GCC_except_table2981
+ GCC_except_table2983
+ GCC_except_table3084
+ GCC_except_table3092
+ GCC_except_table3093
+ GCC_except_table3094
+ GCC_except_table3095
+ GCC_except_table3096
+ GCC_except_table3097
+ GCC_except_table3112
+ GCC_except_table3126
+ GCC_except_table3206
+ GCC_except_table3218
+ GCC_except_table3425
+ GCC_except_table3434
+ GCC_except_table3451
+ GCC_except_table3485
+ GCC_except_table3501
+ GCC_except_table3503
+ GCC_except_table3515
+ GCC_except_table3522
+ GCC_except_table3544
+ GCC_except_table3558
+ GCC_except_table3559
+ GCC_except_table3560
+ GCC_except_table3563
+ GCC_except_table3569
+ GCC_except_table3576
+ GCC_except_table3579
+ GCC_except_table3584
+ GCC_except_table3589
+ GCC_except_table3594
+ GCC_except_table3634
+ GCC_except_table3651
+ GCC_except_table3654
+ GCC_except_table3659
+ GCC_except_table3661
+ GCC_except_table3677
+ GCC_except_table3692
+ GCC_except_table3694
+ GCC_except_table3698
+ GCC_except_table3706
+ GCC_except_table3714
+ GCC_except_table3778
+ GCC_except_table3785
+ GCC_except_table3787
+ GCC_except_table3788
+ GCC_except_table3811
+ GCC_except_table3831
+ GCC_except_table4060
+ GCC_except_table4135
+ GCC_except_table4142
+ GCC_except_table4146
+ GCC_except_table4148
+ GCC_except_table4150
+ GCC_except_table4152
+ GCC_except_table4156
+ GCC_except_table4159
+ GCC_except_table4165
+ GCC_except_table4176
+ GCC_except_table4178
+ GCC_except_table4179
+ GCC_except_table4181
+ GCC_except_table4184
+ GCC_except_table4186
+ GCC_except_table4187
+ GCC_except_table4189
+ GCC_except_table4190
+ GCC_except_table4192
+ GCC_except_table4199
+ GCC_except_table4209
+ GCC_except_table4212
+ GCC_except_table4223
+ GCC_except_table4224
+ GCC_except_table4226
+ GCC_except_table4228
+ GCC_except_table4231
+ GCC_except_table4235
+ GCC_except_table4237
+ GCC_except_table4240
+ GCC_except_table4243
+ GCC_except_table4255
+ GCC_except_table4257
+ GCC_except_table4261
+ GCC_except_table4265
+ GCC_except_table4269
+ GCC_except_table4274
+ GCC_except_table4287
+ GCC_except_table4306
+ GCC_except_table4329
+ GCC_except_table4335
+ GCC_except_table4339
+ GCC_except_table4343
+ GCC_except_table4345
+ GCC_except_table4348
+ GCC_except_table4350
+ GCC_except_table4352
+ GCC_except_table4359
+ GCC_except_table4360
+ GCC_except_table4361
+ GCC_except_table4362
+ GCC_except_table4363
+ GCC_except_table4364
+ GCC_except_table4365
+ GCC_except_table4367
+ GCC_except_table4368
+ GCC_except_table4369
+ GCC_except_table4370
+ GCC_except_table4429
+ GCC_except_table4437
+ GCC_except_table4470
+ GCC_except_table4478
+ GCC_except_table4486
+ GCC_except_table4488
+ GCC_except_table4499
+ GCC_except_table4547
+ GCC_except_table4554
+ GCC_except_table4556
+ GCC_except_table4558
+ GCC_except_table4559
+ GCC_except_table4564
+ GCC_except_table4581
+ GCC_except_table4583
+ GCC_except_table4589
+ GCC_except_table4590
+ GCC_except_table4595
+ GCC_except_table4596
+ GCC_except_table4602
+ GCC_except_table4608
+ GCC_except_table4609
+ GCC_except_table4610
+ GCC_except_table4613
+ GCC_except_table4617
+ GCC_except_table4618
+ GCC_except_table4621
+ GCC_except_table4627
+ GCC_except_table4631
+ GCC_except_table4632
+ GCC_except_table4640
+ GCC_except_table4677
+ GCC_except_table4678
+ GCC_except_table4680
+ GCC_except_table4681
+ GCC_except_table4684
+ GCC_except_table4685
+ GCC_except_table4700
+ GCC_except_table4703
+ GCC_except_table4710
+ GCC_except_table4713
+ GCC_except_table4728
+ GCC_except_table4738
+ GCC_except_table4740
+ GCC_except_table4818
+ GCC_except_table4819
+ GCC_except_table4820
+ GCC_except_table4821
+ GCC_except_table4822
+ GCC_except_table4823
+ GCC_except_table4824
+ GCC_except_table4825
+ GCC_except_table4826
+ GCC_except_table4827
+ GCC_except_table4828
+ GCC_except_table4829
+ GCC_except_table4830
+ GCC_except_table4831
+ GCC_except_table4832
+ GCC_except_table4871
+ GCC_except_table4898
+ GCC_except_table4989
+ GCC_except_table4991
+ GCC_except_table4993
+ GCC_except_table4995
+ GCC_except_table4997
+ GCC_except_table5088
+ GCC_except_table5092
+ GCC_except_table5093
+ GCC_except_table5095
+ GCC_except_table5097
+ GCC_except_table5100
+ GCC_except_table5103
+ GCC_except_table5106
+ GCC_except_table5109
+ GCC_except_table5112
+ GCC_except_table5115
+ GCC_except_table5118
+ GCC_except_table5126
+ GCC_except_table5139
+ GCC_except_table5144
+ GCC_except_table5148
+ GCC_except_table5150
+ GCC_except_table5153
+ GCC_except_table5167
+ GCC_except_table5175
+ GCC_except_table5179
+ GCC_except_table5185
+ GCC_except_table5190
+ GCC_except_table52
+ GCC_except_table5208
+ GCC_except_table5210
+ GCC_except_table5212
+ GCC_except_table5216
+ GCC_except_table5222
+ GCC_except_table5225
+ GCC_except_table5227
+ GCC_except_table5236
+ GCC_except_table5238
+ GCC_except_table5240
+ GCC_except_table5243
+ GCC_except_table5254
+ GCC_except_table5265
+ GCC_except_table5267
+ GCC_except_table5278
+ GCC_except_table5280
+ GCC_except_table5282
+ GCC_except_table5288
+ GCC_except_table557
+ GCC_except_table5570
+ GCC_except_table5576
+ GCC_except_table5593
+ GCC_except_table5597
+ GCC_except_table5615
+ GCC_except_table5621
+ GCC_except_table5635
+ GCC_except_table5649
+ GCC_except_table5653
+ GCC_except_table567
+ GCC_except_table5771
+ GCC_except_table589
+ GCC_except_table618
+ GCC_except_table6232
+ GCC_except_table6239
+ GCC_except_table624
+ GCC_except_table6249
+ GCC_except_table6250
+ GCC_except_table6261
+ GCC_except_table6306
+ GCC_except_table6307
+ GCC_except_table6308
+ GCC_except_table6309
+ GCC_except_table636
+ GCC_except_table637
+ GCC_except_table639
+ GCC_except_table642
+ GCC_except_table645
+ GCC_except_table6506
+ GCC_except_table6507
+ GCC_except_table6508
+ GCC_except_table6509
+ GCC_except_table6510
+ GCC_except_table6512
+ GCC_except_table6514
+ GCC_except_table6515
+ GCC_except_table6517
+ GCC_except_table6538
+ GCC_except_table6549
+ GCC_except_table655
+ GCC_except_table6551
+ GCC_except_table6556
+ GCC_except_table6559
+ GCC_except_table6562
+ GCC_except_table6566
+ GCC_except_table657
+ GCC_except_table6570
+ GCC_except_table661
+ GCC_except_table668
+ GCC_except_table671
+ GCC_except_table705
+ GCC_except_table715
+ GCC_except_table7163
+ GCC_except_table7164
+ GCC_except_table7183
+ GCC_except_table7193
+ GCC_except_table7196
+ GCC_except_table7201
+ GCC_except_table7204
+ GCC_except_table7209
+ GCC_except_table723
+ GCC_except_table7478
+ GCC_except_table7482
+ GCC_except_table750
+ GCC_except_table754
+ GCC_except_table7542
+ GCC_except_table7546
+ GCC_except_table7548
+ GCC_except_table7550
+ GCC_except_table757
+ GCC_except_table759
+ GCC_except_table765
+ GCC_except_table767
+ GCC_except_table7767
+ GCC_except_table7775
+ GCC_except_table7777
+ GCC_except_table7779
+ GCC_except_table7781
+ GCC_except_table7787
+ GCC_except_table780
+ GCC_except_table7800
+ GCC_except_table7819
+ GCC_except_table7830
+ GCC_except_table784
+ GCC_except_table7844
+ GCC_except_table7848
+ GCC_except_table7853
+ GCC_except_table7855
+ GCC_except_table7859
+ GCC_except_table7861
+ GCC_except_table788
+ GCC_except_table7937
+ GCC_except_table7944
+ GCC_except_table7948
+ GCC_except_table7949
+ GCC_except_table7950
+ GCC_except_table7951
+ GCC_except_table7960
+ GCC_except_table7976
+ GCC_except_table798
+ GCC_except_table799
+ GCC_except_table8011
+ GCC_except_table8012
+ GCC_except_table8013
+ GCC_except_table8033
+ GCC_except_table804
+ GCC_except_table8045
+ GCC_except_table8048
+ GCC_except_table8053
+ GCC_except_table8055
+ GCC_except_table8069
+ GCC_except_table807
+ GCC_except_table810
+ GCC_except_table815
+ GCC_except_table819
+ GCC_except_table825
+ GCC_except_table826
+ GCC_except_table8293
+ GCC_except_table8306
+ GCC_except_table831
+ GCC_except_table8311
+ GCC_except_table8314
+ GCC_except_table8315
+ GCC_except_table8318
+ GCC_except_table832
+ GCC_except_table8320
+ GCC_except_table8350
+ GCC_except_table8372
+ GCC_except_table8376
+ GCC_except_table8380
+ GCC_except_table8385
+ GCC_except_table8389
+ GCC_except_table8393
+ GCC_except_table8397
+ GCC_except_table8401
+ GCC_except_table8409
+ GCC_except_table8411
+ GCC_except_table8413
+ GCC_except_table8441
+ GCC_except_table8453
+ GCC_except_table860
+ GCC_except_table8618
+ GCC_except_table8622
+ GCC_except_table867
+ GCC_except_table8684
+ GCC_except_table8696
+ GCC_except_table875
+ GCC_except_table876
+ GCC_except_table8790
+ GCC_except_table8792
+ GCC_except_table8793
+ GCC_except_table8794
+ GCC_except_table8860
+ GCC_except_table8874
+ GCC_except_table8882
+ GCC_except_table8883
+ GCC_except_table8890
+ GCC_except_table8903
+ GCC_except_table8909
+ GCC_except_table8913
+ GCC_except_table8916
+ GCC_except_table8918
+ GCC_except_table8923
+ GCC_except_table8929
+ GCC_except_table8944
+ GCC_except_table8948
+ GCC_except_table8953
+ GCC_except_table8956
+ GCC_except_table8963
+ GCC_except_table8966
+ GCC_except_table8980
+ GCC_except_table8987
+ GCC_except_table8993
+ GCC_except_table9002
+ GCC_except_table9004
+ GCC_except_table9008
+ GCC_except_table9009
+ GCC_except_table9016
+ GCC_except_table904
+ GCC_except_table9040
+ GCC_except_table9041
+ GCC_except_table9046
+ GCC_except_table9050
+ GCC_except_table9051
+ GCC_except_table9054
+ GCC_except_table9060
+ GCC_except_table9064
+ GCC_except_table9068
+ GCC_except_table9070
+ GCC_except_table9072
+ GCC_except_table9076
+ GCC_except_table9230
+ GCC_except_table9267
+ GCC_except_table9328
+ GCC_except_table9335
+ GCC_except_table9341
+ GCC_except_table9348
+ GCC_except_table9349
+ GCC_except_table9365
+ GCC_except_table9371
+ GCC_except_table9425
+ GCC_except_table9428
+ GCC_except_table9455
+ GCC_except_table9456
+ GCC_except_table946
+ GCC_except_table9461
+ GCC_except_table9481
+ GCC_except_table9499
+ GCC_except_table9500
+ GCC_except_table9501
+ GCC_except_table9508
+ GCC_except_table9511
+ GCC_except_table9515
+ GCC_except_table9519
+ GCC_except_table9520
+ GCC_except_table9522
+ GCC_except_table9530
+ GCC_except_table9531
+ GCC_except_table9534
+ GCC_except_table9537
+ GCC_except_table9544
+ GCC_except_table9548
+ GCC_except_table9553
+ GCC_except_table9554
+ GCC_except_table9555
+ GCC_except_table9571
+ GCC_except_table9573
+ GCC_except_table9576
+ GCC_except_table9582
+ GCC_except_table9590
+ GCC_except_table9595
+ GCC_except_table9601
+ GCC_except_table9607
+ GCC_except_table9619
+ GCC_except_table9620
+ GCC_except_table9625
+ GCC_except_table9637
+ GCC_except_table9638
+ GCC_except_table9641
+ GCC_except_table9643
+ GCC_except_table9645
+ GCC_except_table9649
+ GCC_except_table9670
+ GCC_except_table9672
+ GCC_except_table9673
+ GCC_except_table9699
+ GCC_except_table974
+ GCC_except_table9864
+ GCC_except_table99
+ GCC_except_table9927
+ GCC_except_table993
+ GCC_except_table9959
+ GCC_except_table9962
+ _HAP2NextSharedWorkloop
+ _HAP2NextSharedWorkloop.nextIndex
+ _HAP2NextSharedWorkloop.onceToken
+ _HAP2NextSharedWorkloop.workloops
+ _HAP2ReopenBackoffMilliseconds
+ _HAPMFiTokenUUIDFromWireData
+ _HAPMFiTokenWireUUIDData
+ _HAPNFCURIScheme
+ _OBJC_CLASS_$_HAPNFCSharedCredentialFetch
+ _OBJC_CLASS_$_HAPNFCTagContents
+ _OBJC_CLASS_$_NFNdefMessage
+ _OBJC_IVAR_$_HAP2AccessoryServerSecureTransportPairVerify._lastSessionStartedAt
+ _OBJC_IVAR_$_HAP2AccessoryServerSecureTransportPairVerify._nextOpenAllowedAt
+ _OBJC_IVAR_$_HAP2AccessoryServerSecureTransportPairVerify._quickSessionCount
+ _OBJC_IVAR_$_HAP2CoAPClient._localCloseQoS
+ _OBJC_IVAR_$_HAP2SerializedOperationQueue._unfinishedCountByQoSLevel
+ _OBJC_IVAR_$_HAPAccessoryServerBrowserNFC._busyRetryCount
+ _OBJC_IVAR_$_HAPAccessoryServerBrowserNFC._commitAwaitingTagServer
+ _OBJC_IVAR_$_HAPAccessoryServerBrowserNFC._readsDetectedTagContents
+ _OBJC_IVAR_$_HAPAccessoryServerBrowserNFC._rearmRetryGeneration
+ _OBJC_IVAR_$_HAPAccessoryServerBrowserNFC._rearmRetryPending
+ _OBJC_IVAR_$_HAPAccessoryServerBrowserNFC._tagContentsReadSession
+ _OBJC_IVAR_$_HAPAccessoryServerNFC._awaitingTagForCommit
+ _OBJC_IVAR_$_HAPAccessoryServerNFC._holdsTagThroughM6
+ _OBJC_IVAR_$_HAPAccessoryServerNFC._prefetchedMFiTokenFromM4
+ _OBJC_IVAR_$_HAPAccessoryServerNFC._readerReleaseGraceElapsed
+ _OBJC_IVAR_$_HAPAccessoryServerNFC._readerReleaseGraceGeneration
+ _OBJC_IVAR_$_HAPAccessoryServerNFC._readerReleaseGracePeriod
+ _OBJC_IVAR_$_HAPAccessoryServerNFC._releasedReaderAtM4
+ _OBJC_IVAR_$_HAPAccessoryServerNFC._sharedCredentialFetches
+ _OBJC_IVAR_$_HAPAccessoryServerNFC._tagContents
+ _OBJC_IVAR_$_HAPNFCSharedCredentialFetch._answer
+ _OBJC_IVAR_$_HAPNFCSharedCredentialFetch._waitingHandlers
+ _OBJC_IVAR_$_HAPNFCTagContents._mfiToken
+ _OBJC_IVAR_$_HAPNFCTagContents._mfiTokenUUID
+ _OBJC_IVAR_$_HAPNFCTagContents._setupPayloadURLStrings
+ _OBJC_IVAR_$_HAPNFCTagContents._tagIdentifier
+ _OBJC_IVAR_$_HAPNFCTagContents._technology
+ _OBJC_METACLASS_$_HAPNFCSharedCredentialFetch
+ _OBJC_METACLASS_$_HAPNFCTagContents
+ __OBJC_$_CLASS_METHODS_HAPNFCTagContents
+ __OBJC_$_CLASS_PROP_LIST_HAP2CoAPIOThread
+ __OBJC_$_INSTANCE_METHODS_HAPNFCSharedCredentialFetch
+ __OBJC_$_INSTANCE_METHODS_HAPNFCTagContents
+ __OBJC_$_INSTANCE_VARIABLES_HAPNFCSharedCredentialFetch
+ __OBJC_$_INSTANCE_VARIABLES_HAPNFCTagContents
+ __OBJC_$_PROP_LIST_HAPNFCSharedCredentialFetch
+ __OBJC_$_PROP_LIST_HAPNFCTagContents
+ __OBJC_CLASS_RO_$_HAPNFCSharedCredentialFetch
+ __OBJC_CLASS_RO_$_HAPNFCTagContents
+ __OBJC_METACLASS_RO_$_HAPNFCSharedCredentialFetch
+ __OBJC_METACLASS_RO_$_HAPNFCTagContents
+ ___110-[HAPAccessoryServerNFC pairSetupSession:didReceiveThreadNetworkConfigurationTLVRequestWithCompletionHandler:]_block_invoke_3
+ ___139-[HAP2AccessoryServerTransportCoAP _executeRacingWithRequest:path:method:messageID:primaryClient:secondaryClient:failoverTimeout:rttStats:]_block_invoke_2
+ ___24-[HAP2CoAPIOThread main]_block_invoke
+ ___41-[HAP2CoAPClient _exchangeLocalCloseQoS:]_block_invoke
+ ___44-[HAPAccessoryServerNFC abandonParkedCommit]_block_invoke
+ ___45-[HAP2SerializedOperationQueue addOperation:]_block_invoke_4
+ ___52-[HAPAccessoryServerBrowserNFC _handleTagDetection:]_block_invoke
+ ___52-[HAPAccessoryServerBrowserNFC _handleTagDetection:]_block_invoke_2
+ ___52-[HAPAccessoryServerNFC _armReaderReleaseGraceTimer]_block_invoke
+ ___52-[HAPAccessoryServerNFC _parkCommitUntilReadyForTag]_block_invoke
+ ___52-[HAPAccessoryServerNFC _parkCommitUntilReadyForTag]_block_invoke_2
+ ___53-[HAPNFCReaderSession readTagContentsWithCompletion:]_block_invoke
+ ___54-[HAP2AccessoryServerControllerOperation _sendRequest]_block_invoke_3
+ ___54-[HAPAccessoryServerNFC _startHAPPairSetupOnWorkQueue]_block_invoke
+ ___55-[HAPAccessoryServerNFC _releaseReaderIfM5StillWaiting]_block_invoke
+ ___55-[HAPAccessoryServerNFC _releaseReaderIfM5StillWaiting]_block_invoke_2
+ ___56-[HAP2AccessoryServerController _scheduleRestartSession]_block_invoke_3
+ ___56-[HAP2AccessoryServerController _scheduleRestartSession]_block_invoke_4
+ ___57-[HAPAccessoryServerBrowserNFC _scheduleRearmAfterDelay:]_block_invoke
+ ___58-[HAP2SerializedOperationQueue _highestUnfinishedQoSClass]_block_invoke
+ ___59-[HAP2SerializedOperationQueue _releaseUnfinishedQoSLevel:]_block_invoke
+ ___59-[HAPAccessoryServerBrowserNFC nfcServerNeedsTagForCommit:]_block_invoke
+ ___59-[HAPAccessoryServerNFC _failPairingWithAIDSelectionError:]_block_invoke
+ ___60-[HAP2AccessoryServerController closeSessionWithCompletion:]_block_invoke_2
+ ___62-[HAPAccessoryServerBrowserNFC nfcServerDidReleaseReaderAtM4:]_block_invoke
+ ___63-[HAPAccessoryServerBrowserNFC setReadsTagContentsOnDetection:]_block_invoke
+ ___65-[HAP2AccessoryServerController sendProbeOnTransport:completion:]_block_invoke_2
+ ___67-[HAP2AccessoryServerSecureTransportPairVerify _noteSessionStarted]_block_invoke
+ ___67-[HAP2SerializedOperationQueue _trackUnfinishedOperation:qosClass:]_block_invoke
+ ___67-[HAP2SerializedOperationQueue _trackUnfinishedOperation:qosClass:]_block_invoke_2
+ ___68-[HAP2AccessoryServerController openTransportWithResume:completion:]_block_invoke_3
+ ___69-[HAP2AccessoryServerSecureTransportPairVerify doOpenWithCompletion:]_block_invoke
+ ___70-[HAP2AccessoryServerControllerOperation _closeSessionWithCompletion:]_block_invoke_3
+ ___70-[HAP2AccessoryServerSecureTransportPairVerify _test_expireReopenWait]_block_invoke
+ ___71-[HAP2AccessoryServerControllerTimedWriteOperation _sendExecuteRequest]_block_invoke_3
+ ___71-[HAP2AccessoryServerControllerTimedWriteOperation _sendPrepareRequest]_block_invoke_3
+ ___71-[HAP2AccessoryServerSecureTransportPairVerify _reopenWaitMilliseconds]_block_invoke
+ ___78-[HAPAccessoryServerNFC _requestSharedNetworkCredentialsForKey:handler:fetch:]_block_invoke
+ ___78-[HAPAccessoryServerNFC _requestSharedNetworkCredentialsForKey:handler:fetch:]_block_invoke_2
+ ___78-[HAPAccessoryServerNFC _requestSharedNetworkCredentialsForKey:handler:fetch:]_block_invoke_3
+ ___78-[HAPAccessoryServerNFC _requestSharedNetworkCredentialsForKey:handler:fetch:]_block_invoke_4
+ ___78-[HAPAccessoryServerNFC _requestSharedNetworkCredentialsForKey:handler:fetch:]_block_invoke_5
+ ___82-[HAPAccessoryServerNFC pairSetupSession:lateMFiTokenForM4Hash:completionHandler:]_block_invoke
+ ___88-[HAP2AccessoryServerSecureTransportPairVerify _test_ageLastSessionStartByMilliseconds:]_block_invoke
+ ___HAP2NextSharedWorkloop_block_invoke
+ ___block_descriptor_40_e8_32s_e68_v16?0?<v?"NSData""NSString""HAPAdditionalWifiData""NSError">8ls32l8
+ ___block_descriptor_48_e8_32s40s_e8_v12?0B8ls32l8s40l8
+ ___block_descriptor_48_e8_32w40w_e5_v8?0lw32l8w40l8
+ ___block_descriptor_52_e8_32s40r_e5_v8?0lr40l8s32l8
+ ___block_descriptor_52_e8_32s_e28_v32?0"NSOperation"8Q16^B24ls32l8
+ ___block_descriptor_53_e8_32bs40w_e17_v16?0"NSError"8lw40l8s32l8
+ ___block_descriptor_56_e8_32s40s48s_e39_v24?0"HAPNFCTagContents"8"NSError"16ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48s_e67_v40?0"NSData"8"NSString"16"HAPAdditionalWifiData"24"NSError"32ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40bs48r_e5_v8?0ls32l8s40l8r48l8
+ ___block_descriptor_64_e8_32s40s48bs56bs_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_descriptor_64_e8_32s40s48s56s_e68_v16?0?<v?"NSData""NSString""HAPAdditionalWifiData""NSError">8ls32l8s40l8s48l8s56l8
+ ___block_descriptor_88_e8_32s40s48s56s64s72s80s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8
+ ___swift_closure_destructor.253Tm
+ _dispatch_block_create_with_qos_class
+ _dispatch_get_specific
+ _dispatch_queue_attr_make_initially_inactive
+ _dispatch_queue_set_specific
+ _dispatch_set_qos_class_floor
+ _dispatch_workloop_create
+ _kHAPAccessoryServerNFCWorkQueueKey
+ _kHAPNFCThreadCredentialFetchKey_block_invoke._hmf_once_t0
+ _kHAPNFCThreadCredentialFetchKey_block_invoke._hmf_once_v1
+ _main.onceToken
+ _swift_retain_x1
+ _symbolic Ieg_
+ _symbolic IeyB_
+ _symbolic SbIegy_
+ _symbolic _____IeyBy_ 10ObjectiveC8ObjCBoolV
+ _symbolic yycSg
+ _type_layout_string So25HAPNetworkCredentialTypesV
- -[HAP2SerializedOperationQueue _applyCallerQoSToOperations:]
- -[HAP2SerializedOperationQueue _stampDiagnosticsOnOperations:]
- -[HAP2SerializedOperationQueue addConcurrentBlock:qos:]
- -[HAP2SerializedOperationQueue addConcurrentOperation:]
- -[HAPAccessoryServerBrowserNFC _scheduleBusyRearmAfterDelay]
- -[HAPAccessoryServerBrowserNFC busyRetryPending]
- -[HAPAccessoryServerBrowserNFC committedBusyRetryCount]
- -[HAPAccessoryServerBrowserNFC setBusyRetryPending:]
- -[HAPAccessoryServerBrowserNFC setCommittedBusyRetryCount:]
- GCC_except_table1001
- GCC_except_table1003
- GCC_except_table10036
- GCC_except_table1007
- GCC_except_table10073
- GCC_except_table1014
- GCC_except_table1017
- GCC_except_table10201
- GCC_except_table10203
- GCC_except_table10205
- GCC_except_table10207
- GCC_except_table10209
- GCC_except_table10211
- GCC_except_table10213
- GCC_except_table10219
- GCC_except_table10221
- GCC_except_table10224
- GCC_except_table10226
- GCC_except_table10228
- GCC_except_table10235
- GCC_except_table10241
- GCC_except_table10246
- GCC_except_table10249
- GCC_except_table10254
- GCC_except_table10259
- GCC_except_table10262
- GCC_except_table10265
- GCC_except_table10291
- GCC_except_table10294
- GCC_except_table10295
- GCC_except_table10339
- GCC_except_table10341
- GCC_except_table10343
- GCC_except_table10346
- GCC_except_table10347
- GCC_except_table10348
- GCC_except_table10351
- GCC_except_table10353
- GCC_except_table10358
- GCC_except_table10364
- GCC_except_table10416
- GCC_except_table10423
- GCC_except_table1051
- GCC_except_table10599
- GCC_except_table10601
- GCC_except_table10603
- GCC_except_table10606
- GCC_except_table10608
- GCC_except_table1061
- GCC_except_table10610
- GCC_except_table10612
- GCC_except_table10613
- GCC_except_table10620
- GCC_except_table10622
- GCC_except_table10623
- GCC_except_table1069
- GCC_except_table1096
- GCC_except_table1103
- GCC_except_table1105
- GCC_except_table1111
- GCC_except_table1113
- GCC_except_table1126
- GCC_except_table1130
- GCC_except_table1134
- GCC_except_table1144
- GCC_except_table1145
- GCC_except_table1150
- GCC_except_table1153
- GCC_except_table1156
- GCC_except_table1161
- GCC_except_table1165
- GCC_except_table1171
- GCC_except_table1172
- GCC_except_table1177
- GCC_except_table1178
- GCC_except_table1206
- GCC_except_table1213
- GCC_except_table1221
- GCC_except_table1222
- GCC_except_table1250
- GCC_except_table1273
- GCC_except_table1292
- GCC_except_table1316
- GCC_except_table1320
- GCC_except_table1334
- GCC_except_table1339
- GCC_except_table1444
- GCC_except_table1446
- GCC_except_table18
- GCC_except_table2004
- GCC_except_table2009
- GCC_except_table2011
- GCC_except_table2025
- GCC_except_table2037
- GCC_except_table2039
- GCC_except_table2041
- GCC_except_table2043
- GCC_except_table2173
- GCC_except_table2177
- GCC_except_table2179
- GCC_except_table224
- GCC_except_table225
- GCC_except_table226
- GCC_except_table233
- GCC_except_table234
- GCC_except_table2381
- GCC_except_table240
- GCC_except_table241
- GCC_except_table243
- GCC_except_table246
- GCC_except_table249
- GCC_except_table253
- GCC_except_table259
- GCC_except_table2601
- GCC_except_table2603
- GCC_except_table2608
- GCC_except_table2622
- GCC_except_table2624
- GCC_except_table2636
- GCC_except_table2652
- GCC_except_table2662
- GCC_except_table2670
- GCC_except_table2672
- GCC_except_table2685
- GCC_except_table2693
- GCC_except_table2700
- GCC_except_table2704
- GCC_except_table2708
- GCC_except_table272
- GCC_except_table2749
- GCC_except_table276
- GCC_except_table278
- GCC_except_table2865
- GCC_except_table2869
- GCC_except_table2870
- GCC_except_table2872
- GCC_except_table2874
- GCC_except_table2886
- GCC_except_table2891
- GCC_except_table2895
- GCC_except_table2898
- GCC_except_table2900
- GCC_except_table2903
- GCC_except_table2920
- GCC_except_table2930
- GCC_except_table2932
- GCC_except_table2934
- GCC_except_table2939
- GCC_except_table2942
- GCC_except_table2944
- GCC_except_table2950
- GCC_except_table2954
- GCC_except_table2956
- GCC_except_table2970
- GCC_except_table2974
- GCC_except_table2982
- GCC_except_table2993
- GCC_except_table3035
- GCC_except_table3036
- GCC_except_table3037
- GCC_except_table3039
- GCC_except_table3040
- GCC_except_table3041
- GCC_except_table3043
- GCC_except_table3047
- GCC_except_table3048
- GCC_except_table3074
- GCC_except_table3078
- GCC_except_table3082
- GCC_except_table3246
- GCC_except_table3253
- GCC_except_table3257
- GCC_except_table3261
- GCC_except_table3265
- GCC_except_table3268
- GCC_except_table3270
- GCC_except_table3272
- GCC_except_table3275
- GCC_except_table3281
- GCC_except_table3283
- GCC_except_table3286
- GCC_except_table3287
- GCC_except_table3289
- GCC_except_table333
- GCC_except_table3390
- GCC_except_table3398
- GCC_except_table3399
- GCC_except_table3400
- GCC_except_table3401
- GCC_except_table3402
- GCC_except_table3403
- GCC_except_table341
- GCC_except_table3418
- GCC_except_table3432
- GCC_except_table3512
- GCC_except_table352
- GCC_except_table3524
- GCC_except_table366
- GCC_except_table369
- GCC_except_table3731
- GCC_except_table374
- GCC_except_table3740
- GCC_except_table3757
- GCC_except_table3791
- GCC_except_table3807
- GCC_except_table3809
- GCC_except_table382
- GCC_except_table3821
- GCC_except_table3828
- GCC_except_table3850
- GCC_except_table3864
- GCC_except_table3865
- GCC_except_table3866
- GCC_except_table3869
- GCC_except_table3875
- GCC_except_table388
- GCC_except_table3882
- GCC_except_table3885
- GCC_except_table3890
- GCC_except_table3895
- GCC_except_table390
- GCC_except_table3900
- GCC_except_table392
- GCC_except_table3940
- GCC_except_table3957
- GCC_except_table3960
- GCC_except_table3965
- GCC_except_table3967
- GCC_except_table3983
- GCC_except_table3998
- GCC_except_table4000
- GCC_except_table4004
- GCC_except_table4012
- GCC_except_table4020
- GCC_except_table403
- GCC_except_table4084
- GCC_except_table4091
- GCC_except_table4093
- GCC_except_table4094
- GCC_except_table41
- GCC_except_table4117
- GCC_except_table4137
- GCC_except_table436
- GCC_except_table4366
- GCC_except_table4441
- GCC_except_table4452
- GCC_except_table4454
- GCC_except_table4456
- GCC_except_table4458
- GCC_except_table4471
- GCC_except_table4482
- GCC_except_table4485
- GCC_except_table4487
- GCC_except_table4490
- GCC_except_table4492
- GCC_except_table4493
- GCC_except_table4495
- GCC_except_table4496
- GCC_except_table4498
- GCC_except_table450
- GCC_except_table4505
- GCC_except_table451
- GCC_except_table4515
- GCC_except_table4518
- GCC_except_table4529
- GCC_except_table4530
- GCC_except_table4534
- GCC_except_table4537
- GCC_except_table4541
- GCC_except_table4543
- GCC_except_table4549
- GCC_except_table4561
- GCC_except_table4563
- GCC_except_table4567
- GCC_except_table4571
- GCC_except_table4575
- GCC_except_table458
- GCC_except_table4580
- GCC_except_table4593
- GCC_except_table460
- GCC_except_table462
- GCC_except_table463
- GCC_except_table4635
- GCC_except_table4641
- GCC_except_table4645
- GCC_except_table4649
- GCC_except_table4651
- GCC_except_table4654
- GCC_except_table4658
- GCC_except_table4665
- GCC_except_table4666
- GCC_except_table4667
- GCC_except_table4668
- GCC_except_table4669
- GCC_except_table4671
- GCC_except_table4672
- GCC_except_table4673
- GCC_except_table4674
- GCC_except_table468
- GCC_except_table4764
- GCC_except_table4765
- GCC_except_table4766
- GCC_except_table4767
- GCC_except_table4768
- GCC_except_table4769
- GCC_except_table4770
- GCC_except_table4771
- GCC_except_table4772
- GCC_except_table4773
- GCC_except_table4774
- GCC_except_table4775
- GCC_except_table4776
- GCC_except_table4777
- GCC_except_table4778
- GCC_except_table4817
- GCC_except_table4844
- GCC_except_table485
- GCC_except_table487
- GCC_except_table493
- GCC_except_table4935
- GCC_except_table4937
- GCC_except_table4939
- GCC_except_table494
- GCC_except_table4941
- GCC_except_table4943
- GCC_except_table4980
- GCC_except_table499
- GCC_except_table4992
- GCC_except_table500
- GCC_except_table5038
- GCC_except_table5039
- GCC_except_table5041
- GCC_except_table5043
- GCC_except_table5049
- GCC_except_table5052
- GCC_except_table5055
- GCC_except_table5058
- GCC_except_table506
- GCC_except_table5061
- GCC_except_table5064
- GCC_except_table5067
- GCC_except_table5072
- GCC_except_table5085
- GCC_except_table5090
- GCC_except_table5094
- GCC_except_table5096
- GCC_except_table5099
- GCC_except_table5113
- GCC_except_table5125
- GCC_except_table5131
- GCC_except_table5132
- GCC_except_table5135
- GCC_except_table5136
- GCC_except_table515
- GCC_except_table5154
- GCC_except_table5156
- GCC_except_table5158
- GCC_except_table5159
- GCC_except_table516
- GCC_except_table5162
- GCC_except_table5168
- GCC_except_table517
- GCC_except_table5171
- GCC_except_table5173
- GCC_except_table518
- GCC_except_table5182
- GCC_except_table5184
- GCC_except_table519
- GCC_except_table520
- GCC_except_table5200
- GCC_except_table521
- GCC_except_table5211
- GCC_except_table5224
- GCC_except_table5226
- GCC_except_table5228
- GCC_except_table5234
- GCC_except_table524
- GCC_except_table530
- GCC_except_table534
- GCC_except_table535
- GCC_except_table543
- GCC_except_table5516
- GCC_except_table5522
- GCC_except_table5539
- GCC_except_table5543
- GCC_except_table5561
- GCC_except_table5567
- GCC_except_table5581
- GCC_except_table559
- GCC_except_table5595
- GCC_except_table5599
- GCC_except_table5717
- GCC_except_table580
- GCC_except_table583
- GCC_except_table584
- GCC_except_table587
- GCC_except_table588
- GCC_except_table603
- GCC_except_table6040
- GCC_except_table6042
- GCC_except_table6044
- GCC_except_table6046
- GCC_except_table606
- GCC_except_table613
- GCC_except_table616
- GCC_except_table6245
- GCC_except_table6246
- GCC_except_table6256
- GCC_except_table6298
- GCC_except_table6301
- GCC_except_table6302
- GCC_except_table6304
- GCC_except_table631
- GCC_except_table641
- GCC_except_table643
- GCC_except_table6481
- GCC_except_table6482
- GCC_except_table6483
- GCC_except_table6484
- GCC_except_table6485
- GCC_except_table6486
- GCC_except_table6487
- GCC_except_table6488
- GCC_except_table6490
- GCC_except_table6522
- GCC_except_table6524
- GCC_except_table6529
- GCC_except_table6532
- GCC_except_table6535
- GCC_except_table6539
- GCC_except_table6543
- GCC_except_table7094
- GCC_except_table7095
- GCC_except_table7114
- GCC_except_table7124
- GCC_except_table7127
- GCC_except_table7132
- GCC_except_table7135
- GCC_except_table7140
- GCC_except_table7409
- GCC_except_table7413
- GCC_except_table7473
- GCC_except_table7477
- GCC_except_table7479
- GCC_except_table7481
- GCC_except_table7657
- GCC_except_table7665
- GCC_except_table7667
- GCC_except_table7669
- GCC_except_table7671
- GCC_except_table7677
- GCC_except_table7690
- GCC_except_table7709
- GCC_except_table7720
- GCC_except_table7734
- GCC_except_table7738
- GCC_except_table7743
- GCC_except_table7745
- GCC_except_table7749
- GCC_except_table7751
- GCC_except_table7827
- GCC_except_table7834
- GCC_except_table7838
- GCC_except_table7839
- GCC_except_table7840
- GCC_except_table7841
- GCC_except_table7850
- GCC_except_table7866
- GCC_except_table7901
- GCC_except_table7902
- GCC_except_table7903
- GCC_except_table7923
- GCC_except_table7935
- GCC_except_table7938
- GCC_except_table7943
- GCC_except_table7945
- GCC_except_table7959
- GCC_except_table8225
- GCC_except_table8238
- GCC_except_table8243
- GCC_except_table8246
- GCC_except_table8247
- GCC_except_table8249
- GCC_except_table8250
- GCC_except_table8252
- GCC_except_table8282
- GCC_except_table8304
- GCC_except_table8308
- GCC_except_table8312
- GCC_except_table8321
- GCC_except_table8325
- GCC_except_table8329
- GCC_except_table8333
- GCC_except_table8341
- GCC_except_table8343
- GCC_except_table8345
- GCC_except_table8371
- GCC_except_table8382
- GCC_except_table8529
- GCC_except_table8533
- GCC_except_table8569
- GCC_except_table8665
- GCC_except_table8666
- GCC_except_table8667
- GCC_except_table8668
- GCC_except_table8670
- GCC_except_table8671
- GCC_except_table8736
- GCC_except_table8750
- GCC_except_table8751
- GCC_except_table8756
- GCC_except_table8757
- GCC_except_table8764
- GCC_except_table8776
- GCC_except_table8782
- GCC_except_table8784
- GCC_except_table8786
- GCC_except_table88
- GCC_except_table8801
- GCC_except_table8815
- GCC_except_table8818
- GCC_except_table8819
- GCC_except_table8824
- GCC_except_table8827
- GCC_except_table8834
- GCC_except_table8837
- GCC_except_table8851
- GCC_except_table8858
- GCC_except_table8864
- GCC_except_table8873
- GCC_except_table8879
- GCC_except_table8880
- GCC_except_table8887
- GCC_except_table8912
- GCC_except_table8917
- GCC_except_table8921
- GCC_except_table8922
- GCC_except_table8925
- GCC_except_table8931
- GCC_except_table8935
- GCC_except_table8939
- GCC_except_table8941
- GCC_except_table8943
- GCC_except_table903
- GCC_except_table9101
- GCC_except_table913
- GCC_except_table9138
- GCC_except_table9196
- GCC_except_table9199
- GCC_except_table9206
- GCC_except_table9212
- GCC_except_table9219
- GCC_except_table9220
- GCC_except_table9236
- GCC_except_table9240
- GCC_except_table9241
- GCC_except_table9242
- GCC_except_table9291
- GCC_except_table9292
- GCC_except_table9294
- GCC_except_table9297
- GCC_except_table9324
- GCC_except_table9330
- GCC_except_table935
- GCC_except_table9350
- GCC_except_table9368
- GCC_except_table9375
- GCC_except_table9376
- GCC_except_table9377
- GCC_except_table9380
- GCC_except_table9383
- GCC_except_table9384
- GCC_except_table9388
- GCC_except_table9389
- GCC_except_table9391
- GCC_except_table9399
- GCC_except_table9400
- GCC_except_table9403
- GCC_except_table9406
- GCC_except_table9408
- GCC_except_table9410
- GCC_except_table9413
- GCC_except_table9417
- GCC_except_table9424
- GCC_except_table9440
- GCC_except_table9442
- GCC_except_table9445
- GCC_except_table9451
- GCC_except_table9459
- GCC_except_table9464
- GCC_except_table9470
- GCC_except_table9476
- GCC_except_table9488
- GCC_except_table9489
- GCC_except_table9494
- GCC_except_table9510
- GCC_except_table9512
- GCC_except_table9518
- GCC_except_table9542
- GCC_except_table9568
- GCC_except_table964
- GCC_except_table9733
- GCC_except_table9796
- GCC_except_table982
- GCC_except_table9828
- GCC_except_table983
- GCC_except_table9831
- GCC_except_table985
- GCC_except_table991
- GCC_except_table9998
- _OBJC_IVAR_$_HAP2AccessoryServerTransportCoAP._sendRequestQoS
- _OBJC_IVAR_$_HAPAccessoryServerBrowserNFC._busyRetryPending
- _OBJC_IVAR_$_HAPAccessoryServerBrowserNFC._committedBusyRetryCount
- ___108-[HAPAccessoryServerNFC pairSetupSession:didReceiveWiFiNetworkConfigurationTLVRequestWithCompletionHandler:]_block_invoke_2
- ___60-[HAP2SerializedOperationQueue _applyCallerQoSToOperations:]_block_invoke
- ___60-[HAPAccessoryServerBrowserNFC _scheduleBusyRearmAfterDelay]_block_invoke
- ___62-[HAP2SerializedOperationQueue _stampDiagnosticsOnOperations:]_block_invoke
- ___98-[HAPAccessoryServerNFC pairSetupSession:validateAndRollMFiTokenWithUUID:token:completionHandler:]_block_invoke_3
- ___block_descriptor_40_e28_v32?0"NSOperation"8Q16^B24l
- ___block_descriptor_48_e8_32s_e28_v32?0"NSOperation"8Q16^B24ls32l8
- ___block_descriptor_49_e8_32bs40w_e17_v16?0"NSError"8lw40l8s32l8
- ___swift_closure_destructor.242Tm
- _kHAPNFCAPDUStatusWordUserInfoKey_block_invoke._hmf_once_t0
- _kHAPNFCAPDUStatusWordUserInfoKey_block_invoke._hmf_once_v1
- _type_layout_string So29HAPCHMThreadConnectivityStateV
CStrings:
+ "%@ Secure Transport: Not opening a new session for another %llu ms"
+ "Abandoning the commit parked for its tag; the browser no longer holds this server"
+ "Answering the %{public}@ credential request with this pairing's earlier answer"
+ "Commit already waiting for the tag; keeping the session it readied"
+ "Commit on a released reader; readying M5 before asking for the tag again"
+ "Could not read NDEF from the connected tag (read supported: %{BOOL}d): %{public}@"
+ "Declining the uncertified prompt of a superseded SPAKE2+ session"
+ "Dropping tag contents read on a stale/replaced NFC reader session"
+ "Dropping the ready notice of a commit that is no longer waiting for its tag"
+ "Dropping the ready notice of a commit whose tag is already back"
+ "Failed to disconnect tag: %{public}@ %ld"
+ "Failed to read the NFC tag's NDEF message"
+ "Failed to select HAP AID: %{public}@ %ld"
+ "Failed to start reader session: %{public}@ %ld"
+ "Forwarding emulated tag's prefetched MFi software token to NFC server"
+ "Forwarding emulated tag's prefetched MFi software token to reused NFC server"
+ "HAPNFCReaderReleaseGracePeriod"
+ "Handing the prefetched MFi token to the session a commit readied"
+ "Ignoring a prefetched MFi token (%lu bytes): this pairing keeps the token M4 carried"
+ "Ignoring a reader release from an NFC server that is no longer current"
+ "Ignoring a tag request from an NFC server already pairing on its tag"
+ "Ignoring a tag request from an NFC server that is no longer current"
+ "Ignoring an AID selection failure: the pairing ended during AID selection (state %lu)"
+ "Ignoring pending-commit notice; the commit already resumed pair-setup"
+ "Ignoring setup code request from a pair-setup session that is no longer current"
+ "Joining the %{public}@ credential fetch already in flight for this pairing"
+ "Keeping the MFi token an earlier M4 carried; not replacing it with this one (%lu bytes)"
+ "Keeping the MFi token being rolled (%lu bytes) for any later pass over the tag"
+ "M4: 32-byte hash and no tap-time token; asking whether one arrived since pair-setup started"
+ "M4: a tap-time token (%ld bytes) arrived after pair-setup started; checking the hash"
+ "M4: no tap-time token arrived after pair-setup started"
+ "M4: pair-setup stopped during the late MFi token lookup"
+ "M5 still waiting on an MFi roll or network credentials %.1fs after M4; releasing the NFC reader until they arrive"
+ "MFi roll and network credentials settled; asking the browser for the tag"
+ "NFC discovery already searching; the commit's tag is detected on it"
+ "NFC reader already holds a detected tag; the commit pairs on it"
+ "NFC server released the tag after M4; ending the reader session"
+ "NLM: %@ IPv6 address matches no local interface network, unknown"
+ "NLM: %@ No CoAP client to send on; failing request"
+ "No NFC tag connected to read NDEF from"
+ "No consent %.1fs after the pre-warmed M4; releasing the NFC reader until the commit"
+ "Not starting pair-setup: the pairing ended during AID selection (state %lu)"
+ "Pair-setup: session wrapper released before %{public}s; not continuing"
+ "Pre-warm AID selection failed: %{public}@ %ld"
+ "Pre-warm NFC reader still refused as busy after %lu retries; stopping pre-warm"
+ "Pre-warmed tag left the field before consent; releasing the NFC reader until the commit is ready for a re-tap"
+ "Re-arming the NFC reader for a commit waiting for its tag"
+ "Read NDEF from the connected tag: %lu HomeKit URL(s), MFi token: %{BOOL}d"
+ "Reading a detected tag's contents; keeping its reader session for the committed pairing"
+ "Reading the detected tag's NDEF before pair-setup selects the HAP AID"
+ "Ready to commit: the MFi roll and network credentials M5 waits on have settled (credential budget spent: %{bool,public}d)"
+ "Releasing the NFC reader after M4; the commit re-runs pair-setup on the tag"
+ "Resolver: skipping unknown IPv6 address, accessory advertises IPv4, for deviceID=%{public}@"
+ "S"
+ "SPAKE2+ session asked at M4 for a tap-time MFi token; have one: %{BOOL}d"
+ "Secure Transport: Ignoring open of a stale security session"
+ "Starting the pair-setup session readied while the commit waited for its tag"
+ "Surfacing the NFC server without tag contents: %{public}@ %ld"
+ "T"
+ "[%{public}@] Abandoning the commit parked for its tag; the browser no longer holds this server"
+ "[%{public}@] Answering the %{public}@ credential request with this pairing's earlier answer"
+ "[%{public}@] Commit already waiting for the tag; keeping the session it readied"
+ "[%{public}@] Commit on a released reader; readying M5 before asking for the tag again"
+ "[%{public}@] Could not read NDEF from the connected tag (read supported: %{BOOL}d): %{public}@"
+ "[%{public}@] Declining the uncertified prompt of a superseded SPAKE2+ session"
+ "[%{public}@] Dropping tag contents read on a stale/replaced NFC reader session"
+ "[%{public}@] Dropping the ready notice of a commit that is no longer waiting for its tag"
+ "[%{public}@] Dropping the ready notice of a commit whose tag is already back"
+ "[%{public}@] Failed to disconnect tag: %{public}@ %ld"
+ "[%{public}@] Failed to select HAP AID: %{public}@ %ld"
+ "[%{public}@] Failed to start reader session: %{public}@ %ld"
+ "[%{public}@] Forwarding emulated tag's prefetched MFi software token to NFC server"
+ "[%{public}@] Forwarding emulated tag's prefetched MFi software token to reused NFC server"
+ "[%{public}@] Handing the prefetched MFi token to the session a commit readied"
+ "[%{public}@] Ignoring a prefetched MFi token (%lu bytes): this pairing keeps the token M4 carried"
+ "[%{public}@] Ignoring a reader release from an NFC server that is no longer current"
+ "[%{public}@] Ignoring a tag request from an NFC server already pairing on its tag"
+ "[%{public}@] Ignoring a tag request from an NFC server that is no longer current"
+ "[%{public}@] Ignoring an AID selection failure: the pairing ended during AID selection (state %lu)"
+ "[%{public}@] Ignoring pending-commit notice; the commit already resumed pair-setup"
+ "[%{public}@] Ignoring setup code request from a pair-setup session that is no longer current"
+ "[%{public}@] Joining the %{public}@ credential fetch already in flight for this pairing"
+ "[%{public}@] Keeping the MFi token an earlier M4 carried; not replacing it with this one (%lu bytes)"
+ "[%{public}@] Keeping the MFi token being rolled (%lu bytes) for any later pass over the tag"
+ "[%{public}@] M5 still waiting on an MFi roll or network credentials %.1fs after M4; releasing the NFC reader until they arrive"
+ "[%{public}@] MFi roll and network credentials settled; asking the browser for the tag"
+ "[%{public}@] NFC discovery already searching; the commit's tag is detected on it"
+ "[%{public}@] NFC reader already holds a detected tag; the commit pairs on it"
+ "[%{public}@] NFC server released the tag after M4; ending the reader session"
+ "[%{public}@] No NFC tag connected to read NDEF from"
+ "[%{public}@] No consent %.1fs after the pre-warmed M4; releasing the NFC reader until the commit"
+ "[%{public}@] Not starting pair-setup: the pairing ended during AID selection (state %lu)"
+ "[%{public}@] Pre-warm AID selection failed: %{public}@ %ld"
+ "[%{public}@] Pre-warm NFC reader still refused as busy after %lu retries; stopping pre-warm"
+ "[%{public}@] Pre-warmed tag left the field before consent; releasing the NFC reader until the commit is ready for a re-tap"
+ "[%{public}@] Re-arming the NFC reader for a commit waiting for its tag"
+ "[%{public}@] Read NDEF from the connected tag: %lu HomeKit URL(s), MFi token: %{BOOL}d"
+ "[%{public}@] Reading a detected tag's contents; keeping its reader session for the committed pairing"
+ "[%{public}@] Reading the detected tag's NDEF before pair-setup selects the HAP AID"
+ "[%{public}@] Releasing the NFC reader after M4; the commit re-runs pair-setup on the tag"
+ "[%{public}@] SPAKE2+ session asked at M4 for a tap-time MFi token; have one: %{BOOL}d"
+ "[%{public}@] Starting the pair-setup session readied while the commit waited for its tag"
+ "[%{public}@] Surfacing the NFC server without tag contents: %{public}@ %ld"
+ "[%{public}@] nfcd refused the NFC reader arm as busy again (attempt %lu of %lu)"
+ "[%{public}@] nfcd refused the NFC reader arm as busy; retrying every %.0fms, up to %lu times"
+ "apple.com:hap-mfi-token"
+ "ch"
+ "com.apple.CoreHAP.HAP2.workloop.0"
+ "com.apple.CoreHAP.HAP2.workloop.1"
+ "commitNeedsTag"
+ "mt"
+ "nfcd refused the NFC reader arm as busy again (attempt %lu of %lu)"
+ "nfcd refused the NFC reader arm as busy; retrying every %.0fms, up to %lu times"
+ "readerReleasedAtM4"
+ "v16@?0@?<v@?@\"NSData\"@\"NSString\"@\"HAPAdditionalWifiData\"@\"NSError\">8"
+ "v24@?0@\"HAPNFCTagContents\"8@\"NSError\"16"
+ "wifi"
+ "x-hm"
+ "\xf0!\xf0A"
- "!1"
- "Address %@ does not match any local interface, assuming Thread"
- "Failed to disconnect tag: %@"
- "Failed to select HAP AID: %@"
- "Failed to start reader session: %@"
- "Initialized HAPNFCReaderSession with delegate: %@"
- "NFC reader session started"
- "NLM: %@ isThreadIPv6Address: %{BOOL}d"
- "Pair-setup: session wrapper released before M5; not sending M5"
- "Pre-warm AID selection failed (non-fatal): %@"
- "Pre-warm NFC reader arm refused as busy; pacing the re-arm by %.0fms"
- "Secondary(Thread)"
- "[%{public}@] Failed to disconnect tag: %@"
- "[%{public}@] Failed to select HAP AID: %@"
- "[%{public}@] Failed to start reader session: %@"
- "[%{public}@] Initialized HAPNFCReaderSession with delegate: %@"
- "[%{public}@] NFC reader session started"
- "[%{public}@] Pre-warm AID selection failed (non-fatal): %@"
- "[%{public}@] Pre-warm NFC reader arm refused as busy; pacing the re-arm by %.0fms"
- "[%{public}@] nfcd refused the NFC reader arm as busy; retrying in %.0fms (attempt %lu of %lu)"
- "nfcd refused the NFC reader arm as busy; retrying in %.0fms (attempt %lu of %lu)"
- "\xf01\xf0A"
```
