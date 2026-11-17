## MediaPlaybackCore

> `/System/Library/PrivateFrameworks/MediaPlaybackCore.framework/MediaPlaybackCore`

```diff

-26300.26.43.301.0
-  __TEXT.__text: 0x4a527c
-  __TEXT.__objc_methlist: 0x180b0
+26300.26.46.101.0
+  __TEXT.__text: 0x4aa074
+  __TEXT.__objc_methlist: 0x182b0
   __TEXT.__dlopen_cstrs: 0x114
   __TEXT.__const: 0x11200
-  __TEXT.__oslogstring: 0x4e408
-  __TEXT.__cstring: 0x263a6
+  __TEXT.__oslogstring: 0x4ebe2
+  __TEXT.__cstring: 0x263da
   __TEXT.__swift5_typeref: 0x5702
-  __TEXT.__swift5_capture: 0xb29c
-  __TEXT.__constg_swiftt: 0x7ea4
-  __TEXT.__swift5_reflstr: 0x5d12
-  __TEXT.__swift5_fieldmd: 0x59c4
+  __TEXT.__swift5_capture: 0xb330
+  __TEXT.__constg_swiftt: 0x7eec
+  __TEXT.__swift5_reflstr: 0x5d62
+  __TEXT.__swift5_fieldmd: 0x59e8
   __TEXT.__swift5_builtin: 0x708
   __TEXT.__swift5_mpenum: 0x130
   __TEXT.__swift5_assocty: 0xc08

   __TEXT.__swift_as_cont: 0xf10
   __TEXT.__swift5_protos: 0xe8
   __TEXT.__swift5_types2: 0x4
-  __TEXT.__gcc_except_tab: 0x5ab4
+  __TEXT.__gcc_except_tab: 0x5b28
   __TEXT.__ustring: 0x4dc
-  __TEXT.__unwind_info: 0x11350
-  __TEXT.__eh_frame: 0x11500
+  __TEXT.__unwind_info: 0x10fe0
+  __TEXT.__eh_frame: 0x11510
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x95e0
-  __DATA_CONST.__objc_classlist: 0xd48
+  __DATA_CONST.__const: 0x9600
+  __DATA_CONST.__objc_classlist: 0xd58
   __DATA_CONST.__objc_catlist: 0x298
-  __DATA_CONST.__objc_protolist: 0x7f0
+  __DATA_CONST.__objc_protolist: 0x7f8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xccf0
+  __DATA_CONST.__objc_selrefs: 0xcd88
   __DATA_CONST.__objc_protorefs: 0x3a0
-  __DATA_CONST.__objc_superrefs: 0x6d8
+  __DATA_CONST.__objc_superrefs: 0x6e8
   __DATA_CONST.__objc_arraydata: 0x288
-  __DATA_CONST.__got: 0x3510
-  __AUTH_CONST.__const: 0x24430
-  __AUTH_CONST.__cfstring: 0x1f060
-  __AUTH_CONST.__objc_const: 0x35168
+  __DATA_CONST.__got: 0x3518
+  __AUTH_CONST.__const: 0x245f0
+  __AUTH_CONST.__cfstring: 0x1f0c0
+  __AUTH_CONST.__objc_const: 0x35640
   __AUTH_CONST.__objc_intobj: 0x8b8
   __AUTH_CONST.__objc_arrayobj: 0x258
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__objc_doubleobj: 0x60
-  __AUTH_CONST.__auth_got: 0x3570
-  __AUTH.__objc_data: 0x5b98
-  __AUTH.__data: 0x4360
-  __DATA.__objc_ivar: 0x1b00
-  __DATA.__data: 0x7580
+  __AUTH_CONST.__auth_got: 0x3580
+  __AUTH.__objc_data: 0x5c38
+  __AUTH.__data: 0x4390
+  __DATA.__objc_ivar: 0x1b40
+  __DATA.__data: 0x75e0
   __DATA.__common: 0x280
-  __DATA_DIRTY.__objc_data: 0x35d8
-  __DATA_DIRTY.__data: 0x45c8
+  __DATA_DIRTY.__objc_data: 0x35f0
+  __DATA_DIRTY.__data: 0x45e8
   __DATA_DIRTY.__bss: 0x1328
   __DATA_DIRTY.__common: 0xc8
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 25224
-  Symbols:   18855
-  CStrings:  8386
+  Functions: 25328
+  Symbols:   18943
+  CStrings:  8410
 
Symbols:
+ -[MPCAssistantPlaybackQueue privateListeningOverride]
+ -[MPCAssistantPlaybackQueue setPrivateListeningOverride:]
+ -[MPCModelGenericAVItem _applyTimedMetadataResponse:metadataChangeTime:]
+ -[MPCModelGenericAVItem _prepareLeaseWithShouldRequireLeaseAcquisition:completesWhenRequestSent:completionHandler:]
+ -[MPCModelGenericAVItemTimedMetadataRequest lastFinalResponse]
+ -[MPCModelGenericAVItemTimedMetadataRequest setLastFinalResponse:]
+ -[MPCPlaybackAccount _isUnknownAccount]
+ -[MPCPlaybackEngine isSelfieSingSessionActive]
+ -[MPCPlaybackEngine selfieSingSessionController]
+ -[MPCPlaybackEngine takeSelfieSingSessionAssertion]
+ -[MPCSelfieSingSessionController .cxx_destruct]
+ -[MPCSelfieSingSessionController _assertionDidInvalidateWithIdentifier:released:]
+ -[MPCSelfieSingSessionController _scheduleActiveStateUpdate]
+ -[MPCSelfieSingSessionController _updateActiveState]
+ -[MPCSelfieSingSessionController initWithEngineID:activeStateHandler:]
+ -[MPCSelfieSingSessionController isActive]
+ -[MPCSelfieSingSessionController takeAssertion]
+ -[MPCWhiskyController engineDidBeginSelfieSingSession:]
+ -[MPCWhiskyController engineDidEndSelfieSingSession:]
+ -[_MPCPlaybackEnginePlayer engineDidBeginSelfieSingSession:]
+ -[_MPCPlaybackEnginePlayer engineDidEndSelfieSingSession:]
+ -[_MPCSelfieSingSessionAssertion .cxx_destruct]
+ -[_MPCSelfieSingSessionAssertion _invalidateReleased:]
+ -[_MPCSelfieSingSessionAssertion _invalidateReplaced]
+ -[_MPCSelfieSingSessionAssertion dealloc]
+ -[_MPCSelfieSingSessionAssertion description]
+ -[_MPCSelfieSingSessionAssertion identifier]
+ -[_MPCSelfieSingSessionAssertion initWithController:]
+ -[_MPCSelfieSingSessionAssertion invalidate]
+ -[_MPCSelfieSingSessionAssertion isInvalidated]
+ GCC_except_table1003
+ GCC_except_table1013
+ GCC_except_table1208
+ GCC_except_table1210
+ GCC_except_table1380
+ GCC_except_table1382
+ GCC_except_table1429
+ GCC_except_table1440
+ GCC_except_table1447
+ GCC_except_table1454
+ GCC_except_table1491
+ GCC_except_table1503
+ GCC_except_table1512
+ GCC_except_table1555
+ GCC_except_table1728
+ GCC_except_table1730
+ GCC_except_table1748
+ GCC_except_table1818
+ GCC_except_table1904
+ GCC_except_table1905
+ GCC_except_table196
+ GCC_except_table2016
+ GCC_except_table2036
+ GCC_except_table2038
+ GCC_except_table2067
+ GCC_except_table2076
+ GCC_except_table2081
+ GCC_except_table2083
+ GCC_except_table2086
+ GCC_except_table2097
+ GCC_except_table2107
+ GCC_except_table2222
+ GCC_except_table2273
+ GCC_except_table2277
+ GCC_except_table2280
+ GCC_except_table2306
+ GCC_except_table2330
+ GCC_except_table2362
+ GCC_except_table2442
+ GCC_except_table2629
+ GCC_except_table2657
+ GCC_except_table2686
+ GCC_except_table2831
+ GCC_except_table2859
+ GCC_except_table2860
+ GCC_except_table2885
+ GCC_except_table2887
+ GCC_except_table2896
+ GCC_except_table2898
+ GCC_except_table2900
+ GCC_except_table2902
+ GCC_except_table2905
+ GCC_except_table2931
+ GCC_except_table2940
+ GCC_except_table2945
+ GCC_except_table2947
+ GCC_except_table2951
+ GCC_except_table2956
+ GCC_except_table2962
+ GCC_except_table2965
+ GCC_except_table2968
+ GCC_except_table2996
+ GCC_except_table3039
+ GCC_except_table3129
+ GCC_except_table3133
+ GCC_except_table3144
+ GCC_except_table3145
+ GCC_except_table3177
+ GCC_except_table3221
+ GCC_except_table3222
+ GCC_except_table3238
+ GCC_except_table3295
+ GCC_except_table3315
+ GCC_except_table3316
+ GCC_except_table3326
+ GCC_except_table3368
+ GCC_except_table3370
+ GCC_except_table3377
+ GCC_except_table3388
+ GCC_except_table3392
+ GCC_except_table3434
+ GCC_except_table3479
+ GCC_except_table3484
+ GCC_except_table359
+ GCC_except_table3616
+ GCC_except_table3637
+ GCC_except_table3644
+ GCC_except_table3669
+ GCC_except_table3673
+ GCC_except_table3683
+ GCC_except_table3740
+ GCC_except_table3745
+ GCC_except_table3749
+ GCC_except_table3819
+ GCC_except_table3918
+ GCC_except_table3922
+ GCC_except_table3933
+ GCC_except_table3949
+ GCC_except_table3955
+ GCC_except_table3964
+ GCC_except_table405
+ GCC_except_table4092
+ GCC_except_table413
+ GCC_except_table4137
+ GCC_except_table4138
+ GCC_except_table4139
+ GCC_except_table4158
+ GCC_except_table4167
+ GCC_except_table4186
+ GCC_except_table4191
+ GCC_except_table4193
+ GCC_except_table4207
+ GCC_except_table421
+ GCC_except_table4230
+ GCC_except_table4241
+ GCC_except_table430
+ GCC_except_table4330
+ GCC_except_table4362
+ GCC_except_table4373
+ GCC_except_table4404
+ GCC_except_table4575
+ GCC_except_table4576
+ GCC_except_table4754
+ GCC_except_table4789
+ GCC_except_table4791
+ GCC_except_table4799
+ GCC_except_table4807
+ GCC_except_table4822
+ GCC_except_table4830
+ GCC_except_table4838
+ GCC_except_table4848
+ GCC_except_table4863
+ GCC_except_table4907
+ GCC_except_table4921
+ GCC_except_table4937
+ GCC_except_table4940
+ GCC_except_table4946
+ GCC_except_table4998
+ GCC_except_table5036
+ GCC_except_table5124
+ GCC_except_table514
+ GCC_except_table5225
+ GCC_except_table531
+ GCC_except_table5470
+ GCC_except_table5471
+ GCC_except_table548
+ GCC_except_table5551
+ GCC_except_table5632
+ GCC_except_table5647
+ GCC_except_table5670
+ GCC_except_table5672
+ GCC_except_table5823
+ GCC_except_table5848
+ GCC_except_table5965
+ GCC_except_table6046
+ GCC_except_table6054
+ GCC_except_table6055
+ GCC_except_table6119
+ GCC_except_table6179
+ GCC_except_table6182
+ GCC_except_table6185
+ GCC_except_table6271
+ GCC_except_table6488
+ GCC_except_table6505
+ GCC_except_table6553
+ GCC_except_table6566
+ GCC_except_table7082
+ GCC_except_table7416
+ GCC_except_table7431
+ GCC_except_table7525
+ GCC_except_table7534
+ GCC_except_table7623
+ GCC_except_table7630
+ GCC_except_table7648
+ GCC_except_table7699
+ GCC_except_table7700
+ GCC_except_table7703
+ GCC_except_table7708
+ GCC_except_table7724
+ GCC_except_table799
+ GCC_except_table857
+ GCC_except_table937
+ GCC_except_table971
+ GCC_except_table973
+ GCC_except_table978
+ GCC_except_table980
+ GCC_except_table993
+ GCC_except_table997
+ _CGRectGetHeight
+ _CGRectGetWidth
+ _MPCPlaybackEngineEventTypeSelfieSingSessionBegin
+ _MPCPlaybackEngineEventTypeSelfieSingSessionEnd
+ _OBJC_CLASS_$_MPCSelfieSingSessionController
+ _OBJC_CLASS_$_UIScreen
+ _OBJC_CLASS_$__MPCSelfieSingSessionAssertion
+ _OBJC_IVAR_$_MPCAssistantPlaybackQueue._privateListeningOverride
+ _OBJC_IVAR_$_MPCModelGenericAVItem._lastFinalTimedMetadataResponse
+ _OBJC_IVAR_$_MPCModelGenericAVItem._timedMetadataStationFallbackGeneration
+ _OBJC_IVAR_$_MPCModelGenericAVItemTimedMetadataRequest._lastFinalResponse
+ _OBJC_IVAR_$_MPCModelRadioQueueFeeder._stationArtworkCacheRequestInFlight
+ _OBJC_IVAR_$_MPCPlaybackEngine._selfieSingSessionController
+ _OBJC_IVAR_$_MPCQueueController._liveItemBeginQueueItemID
+ _OBJC_IVAR_$_MPCQueueController._liveItemBeginQueueSectionID
+ _OBJC_IVAR_$_MPCSelfieSingSessionController._active
+ _OBJC_IVAR_$_MPCSelfieSingSessionController._activeStateHandler
+ _OBJC_IVAR_$_MPCSelfieSingSessionController._engineID
+ _OBJC_IVAR_$_MPCSelfieSingSessionController._holder
+ _OBJC_IVAR_$_MPCSelfieSingSessionController._holderIdentifier
+ _OBJC_IVAR_$_MPCSelfieSingSessionController._lock
+ _OBJC_IVAR_$__MPCSelfieSingSessionAssertion._controller
+ _OBJC_IVAR_$__MPCSelfieSingSessionAssertion._identifier
+ _OBJC_IVAR_$__MPCSelfieSingSessionAssertion._invalidated
+ _OBJC_IVAR_$__MPCSelfieSingSessionAssertion._lock
+ _OBJC_METACLASS_$_MPCSelfieSingSessionController
+ _OBJC_METACLASS_$__MPCSelfieSingSessionAssertion
+ _OUTLINED_FUNCTION_512
+ _OUTLINED_FUNCTION_513
+ _OUTLINED_FUNCTION_647
+ _OUTLINED_FUNCTION_648
+ __OBJC_$_INSTANCE_METHODS_MPCSelfieSingSessionController
+ __OBJC_$_INSTANCE_METHODS__MPCSelfieSingSessionAssertion
+ __OBJC_$_INSTANCE_VARIABLES_MPCSelfieSingSessionController
+ __OBJC_$_INSTANCE_VARIABLES__MPCSelfieSingSessionAssertion
+ __OBJC_$_PROP_LIST_MPCSelfieSingSessionAssertion
+ __OBJC_$_PROP_LIST_MPCSelfieSingSessionController
+ __OBJC_$_PROP_LIST__MPCSelfieSingSessionAssertion
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MPCSelfieSingSessionAssertion
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MPCSelfieSingSessionAssertion
+ __OBJC_$_PROTOCOL_REFS_MPCSelfieSingSessionAssertion
+ __OBJC_CLASS_PROTOCOLS_$__MPCSelfieSingSessionAssertion
+ __OBJC_CLASS_RO_$_MPCSelfieSingSessionController
+ __OBJC_CLASS_RO_$__MPCSelfieSingSessionAssertion
+ __OBJC_LABEL_PROTOCOL_$_MPCSelfieSingSessionAssertion
+ __OBJC_METACLASS_RO_$_MPCSelfieSingSessionController
+ __OBJC_METACLASS_RO_$__MPCSelfieSingSessionAssertion
+ __OBJC_PROTOCOL_$_MPCSelfieSingSessionAssertion
+ ___115-[MPCModelGenericAVItem _prepareLeaseWithShouldRequireLeaseAcquisition:completesWhenRequestSent:completionHandler:]_block_invoke
+ ___115-[MPCModelGenericAVItem _prepareLeaseWithShouldRequireLeaseAcquisition:completesWhenRequestSent:completionHandler:]_block_invoke_2
+ ___40-[MPCPlaybackEngine initWithParameters:]_block_invoke
+ ___42-[MPCSelfieSingSessionController isActive]_block_invoke
+ ___47-[MPCSelfieSingSessionController takeAssertion]_block_invoke
+ ___47-[_MPCSelfieSingSessionAssertion isInvalidated]_block_invoke
+ ___52-[MPCModelGenericAVItem _reloadTimedMetadataRequest]_block_invoke_3
+ ___52-[MPCSelfieSingSessionController _updateActiveState]_block_invoke
+ ___53-[_MPCSelfieSingSessionAssertion _invalidateReplaced]_block_invoke
+ ___54-[_MPCSelfieSingSessionAssertion _invalidateReleased:]_block_invoke
+ ___60-[MPCSelfieSingSessionController _scheduleActiveStateUpdate]_block_invoke
+ ___78-[MPCModelGenericAVItem _finishDeferredLeaseAcquisitionWithCompletionHandler:]_block_invoke_3
+ ___78-[MPCModelGenericAVItem _finishDeferredLeaseAcquisitionWithCompletionHandler:]_block_invoke_4
+ ___81-[MPCSelfieSingSessionController _assertionDidInvalidateWithIdentifier:released:]_block_invoke
+ ____MPCQCBMSessionTypeAccounts_block_invoke
+ ___block_descriptor_49_e8_32s40bs_e64_v24?0"MPCModelGenericAVItemTimedMetadataResponse"8"NSError"16ls40l8s32l8
+ ___block_descriptor_50_e8_32s40bs_e97_v32?0"ICMusicSubscriptionLeaseSession"8"MPSubscriptionStatusPlaybackInformation"16"NSError"24ls32l8s40l8
+ ___block_descriptor_58_e8_32s40s48bs_e5_v8?0ls32l8s48l8s40l8
+ ___block_descriptor_73_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
+ ___swift_closure_destructor.227Tm
+ ___swift_closure_destructor.500Tm
+ ___swift_closure_destructor.609Tm
- -[MPCPlaybackAccountManager guestAccount]
- -[MPCPlaybackAccountManager unknownAccount]
- GCC_except_table1000
- GCC_except_table1004
- GCC_except_table1198
- GCC_except_table1205
- GCC_except_table1375
- GCC_except_table1377
- GCC_except_table1424
- GCC_except_table1435
- GCC_except_table1442
- GCC_except_table1449
- GCC_except_table1486
- GCC_except_table1498
- GCC_except_table1507
- GCC_except_table1550
- GCC_except_table1723
- GCC_except_table1725
- GCC_except_table1738
- GCC_except_table1813
- GCC_except_table1899
- GCC_except_table1900
- GCC_except_table194
- GCC_except_table2011
- GCC_except_table2031
- GCC_except_table2033
- GCC_except_table2061
- GCC_except_table2070
- GCC_except_table2075
- GCC_except_table2077
- GCC_except_table2080
- GCC_except_table2091
- GCC_except_table2101
- GCC_except_table2216
- GCC_except_table2267
- GCC_except_table2271
- GCC_except_table2274
- GCC_except_table2300
- GCC_except_table2324
- GCC_except_table2356
- GCC_except_table2436
- GCC_except_table2623
- GCC_except_table2651
- GCC_except_table2678
- GCC_except_table2823
- GCC_except_table2844
- GCC_except_table2851
- GCC_except_table2877
- GCC_except_table2879
- GCC_except_table2884
- GCC_except_table2888
- GCC_except_table2890
- GCC_except_table2894
- GCC_except_table2897
- GCC_except_table2923
- GCC_except_table2932
- GCC_except_table2937
- GCC_except_table2939
- GCC_except_table2943
- GCC_except_table2948
- GCC_except_table2949
- GCC_except_table2954
- GCC_except_table2960
- GCC_except_table2980
- GCC_except_table3031
- GCC_except_table3121
- GCC_except_table3125
- GCC_except_table3136
- GCC_except_table3137
- GCC_except_table3161
- GCC_except_table3211
- GCC_except_table3212
- GCC_except_table3228
- GCC_except_table3285
- GCC_except_table3302
- GCC_except_table3303
- GCC_except_table3313
- GCC_except_table3355
- GCC_except_table3357
- GCC_except_table3364
- GCC_except_table3375
- GCC_except_table3379
- GCC_except_table3423
- GCC_except_table3468
- GCC_except_table3473
- GCC_except_table355
- GCC_except_table3605
- GCC_except_table3626
- GCC_except_table3633
- GCC_except_table3658
- GCC_except_table3662
- GCC_except_table3672
- GCC_except_table3729
- GCC_except_table3734
- GCC_except_table3738
- GCC_except_table3808
- GCC_except_table3905
- GCC_except_table3909
- GCC_except_table3920
- GCC_except_table3936
- GCC_except_table3942
- GCC_except_table3951
- GCC_except_table403
- GCC_except_table4079
- GCC_except_table411
- GCC_except_table4124
- GCC_except_table4125
- GCC_except_table4126
- GCC_except_table4145
- GCC_except_table4154
- GCC_except_table4173
- GCC_except_table4178
- GCC_except_table4180
- GCC_except_table419
- GCC_except_table4194
- GCC_except_table4217
- GCC_except_table4228
- GCC_except_table428
- GCC_except_table4317
- GCC_except_table4336
- GCC_except_table4360
- GCC_except_table4391
- GCC_except_table4562
- GCC_except_table4563
- GCC_except_table4741
- GCC_except_table4776
- GCC_except_table4778
- GCC_except_table4786
- GCC_except_table4794
- GCC_except_table4809
- GCC_except_table4817
- GCC_except_table4825
- GCC_except_table4835
- GCC_except_table4850
- GCC_except_table4894
- GCC_except_table4908
- GCC_except_table4924
- GCC_except_table4927
- GCC_except_table4933
- GCC_except_table4985
- GCC_except_table5023
- GCC_except_table5111
- GCC_except_table513
- GCC_except_table5212
- GCC_except_table529
- GCC_except_table5457
- GCC_except_table5458
- GCC_except_table546
- GCC_except_table5537
- GCC_except_table5630
- GCC_except_table5782
- GCC_except_table5807
- GCC_except_table5924
- GCC_except_table6005
- GCC_except_table6013
- GCC_except_table6014
- GCC_except_table6078
- GCC_except_table6103
- GCC_except_table6138
- GCC_except_table6141
- GCC_except_table6230
- GCC_except_table6447
- GCC_except_table6464
- GCC_except_table6512
- GCC_except_table6525
- GCC_except_table7041
- GCC_except_table7375
- GCC_except_table7390
- GCC_except_table7484
- GCC_except_table7493
- GCC_except_table7582
- GCC_except_table7589
- GCC_except_table7607
- GCC_except_table7658
- GCC_except_table7659
- GCC_except_table7662
- GCC_except_table7667
- GCC_except_table7683
- GCC_except_table798
- GCC_except_table854
- GCC_except_table934
- GCC_except_table965
- GCC_except_table970
- GCC_except_table975
- GCC_except_table977
- GCC_except_table990
- GCC_except_table994
- _OBJC_IVAR_$_MPCPlaybackAccountManager._guestAccount
- _OBJC_IVAR_$_MPCPlaybackAccountManager._unknownAccount
- _OUTLINED_FUNCTION_514
- _OUTLINED_FUNCTION_515
- ___90-[MPCModelGenericAVItem _prepareLeaseWithShouldRequireLeaseAcquisition:completionHandler:]_block_invoke
- ___90-[MPCModelGenericAVItem _prepareLeaseWithShouldRequireLeaseAcquisition:completionHandler:]_block_invoke_2
- ___block_descriptor_48_e8_32s40bs_e64_v24?0"MPCModelGenericAVItemTimedMetadataResponse"8"NSError"16ls40l8s32l8
- ___block_descriptor_49_e8_32s40bs_e97_v32?0"ICMusicSubscriptionLeaseSession"8"MPSubscriptionStatusPlaybackInformation"16"NSError"24ls32l8s40l8
- ___block_descriptor_57_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
- ___block_descriptor_89_e8_32s40s48s56s64bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
- ___swift_closure_destructor.226Tm
- ___swift_closure_destructor.499Tm
- ___swift_closure_destructor.608Tm
CStrings:
+ "<%@: %p id=%@ invalidated=%d>"
+ "Atmos: %@"
+ "Object is a video"
+ "Surround: %@"
+ "[%{public}@]-[LeaseRatePreparation] - %{public}@: Completing without waiting for lease acquisition response [online keys already available]"
+ "[AC] Failed to download %{public}s to asset cache: %{public}s"
+ "[AC] Not downloading %{public}s to asset cache [asset cache unavailable]"
+ "[AC] Not downloading %{public}s to asset cache [cache item is not downloadable]"
+ "[AC] Not downloading %{public}s to asset cache [item already has a download task]"
+ "[AC] Not downloading %{public}s to asset cache [item was released]"
+ "[AC] Not downloading %{public}s to asset cache [no cache item]"
+ "[AP] - %{public}@ - Applying restriction deferred during the Selfie Sing session"
+ "[AP] - %{public}@ - Deferring restriction until the Selfie Sing session ends [%{public}@]"
+ "[AP] - %{public}@ - Not arming the pause timeout [Selfie Sing session active]"
+ "[ENG:%{public}@] SelfieSingSession | invalidating assertion [] id=%{public}@"
+ "[ENG:%{public}@] SelfieSingSession | invalidating assertion [released without invalidate] id=%{public}@"
+ "[ENG:%{public}@] SelfieSingSession | session began []"
+ "[ENG:%{public}@] SelfieSingSession | session ended []"
+ "[ENG:%{public}@] SelfieSingSession | taking assertion [] id=%{public}@"
+ "[ENG:%{public}@] SelfieSingSession | taking assertion [already held] heldID=%{public}@"
+ "[PL:%{public}s] PLAYER CONTROLLER: Dropping the held itemDidBecomeCurrent of the incoming item the queue already considers current - item:%{public}s"
+ "[PL:%{public}s] PLAYER PROCESSING: InternalPlayerController - pausesAtItemEnd:%{bool,public}d - current item: %{public}s"
+ "[PL:%{public}s] STATE MACHINE: Applying target start time %{public}fs parked while changing queue - identifier:%{public}s in state: %{public}s"
+ "[PL:%{public}s] STATE MACHINE: Discarding target start time %{public}fs superseded by jump to %{public}fs - identifier:%{public}s"
+ "a\xf0\xa1"
+ "paused at item end"
+ "selfie-sing-session-begin"
+ "selfie-sing-session-end"
+ "\xf0\xf0\xf0\xe1"
- "DownloadToAssetCache"
- "Object is a video without traits"
- "Unexpected item type for loaded enhanced audio"
- "a\xf0\x91"
- "\xf0\xf0\xf0\xc1"
```
