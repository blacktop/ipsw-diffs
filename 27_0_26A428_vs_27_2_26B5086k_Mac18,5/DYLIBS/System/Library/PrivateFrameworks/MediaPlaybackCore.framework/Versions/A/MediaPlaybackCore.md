## MediaPlaybackCore

> `/System/Library/PrivateFrameworks/MediaPlaybackCore.framework/Versions/A/MediaPlaybackCore`

```diff

-26140.26.31.301.0
-  __TEXT.__text: 0x3b5fc0
-  __TEXT.__objc_methlist: 0x164e0
+26200.26.36.301.0
+  __TEXT.__text: 0x3b784c
+  __TEXT.__objc_methlist: 0x16558
   __TEXT.__dlopen_cstrs: 0xbe
   __TEXT.__const: 0xd880
-  __TEXT.__cstring: 0x230c7
+  __TEXT.__cstring: 0x232f0
   __TEXT.__constg_swiftt: 0x65f8
-  __TEXT.__swift5_typeref: 0x462a
+  __TEXT.__swift5_typeref: 0x461a
   __TEXT.__swift5_builtin: 0x578
-  __TEXT.__swift5_reflstr: 0x4972
-  __TEXT.__swift5_fieldmd: 0x4824
+  __TEXT.__swift5_reflstr: 0x49a2
+  __TEXT.__swift5_fieldmd: 0x4830
   __TEXT.__swift5_assocty: 0xa20
-  __TEXT.__oslogstring: 0x41d88
+  __TEXT.__oslogstring: 0x42221
   __TEXT.__swift5_proto: 0x7a8
   __TEXT.__swift5_types: 0x44c
-  __TEXT.__swift5_capture: 0x6514
+  __TEXT.__swift5_capture: 0x6528
   __TEXT.__swift_as_entry: 0x2c0
   __TEXT.__swift_as_ret: 0x320
   __TEXT.__swift_as_cont: 0x8ac
   __TEXT.__swift5_mpenum: 0xb8
   __TEXT.__swift5_protos: 0xc4
   __TEXT.__swift5_types2: 0x4
-  __TEXT.__gcc_except_tab: 0x560c
+  __TEXT.__gcc_except_tab: 0x56c0
   __TEXT.__ustring: 0x4d4
-  __TEXT.__unwind_info: 0xd378
-  __TEXT.__eh_frame: 0x9d98
+  __TEXT.__unwind_info: 0xd3a8
+  __TEXT.__eh_frame: 0x9d28
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x280
   __DATA_CONST.__objc_protolist: 0x6c8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xbf40
+  __DATA_CONST.__objc_selrefs: 0xbf90
   __DATA_CONST.__objc_protorefs: 0x2c8
-  __DATA_CONST.__objc_superrefs: 0x6b0
-  __DATA_CONST.__objc_arraydata: 0x290
-  __DATA_CONST.__got: 0x2a68
-  __AUTH_CONST.__const: 0x1e4a0
-  __AUTH_CONST.__cfstring: 0x1dea0
-  __AUTH_CONST.__objc_const: 0x30b40
+  __DATA_CONST.__objc_superrefs: 0x6b8
+  __DATA_CONST.__objc_arraydata: 0x298
+  __DATA_CONST.__got: 0x2a70
+  __AUTH_CONST.__const: 0x1e588
+  __AUTH_CONST.__cfstring: 0x1e000
+  __AUTH_CONST.__objc_const: 0x30c50
   __AUTH_CONST.__objc_intobj: 0x888
   __AUTH_CONST.__objc_arrayobj: 0x288
   __AUTH_CONST.__objc_dictobj: 0xc8

   __AUTH_CONST.__auth_got: 0x26f8
   __AUTH.__objc_data: 0x4808
   __AUTH.__data: 0x1ef0
-  __DATA.__objc_ivar: 0x1a34
+  __DATA.__objc_ivar: 0x1a48
   __DATA.__data: 0x56d0
   __DATA.__common: 0xe8
   __DATA_DIRTY.__objc_data: 0x3100
-  __DATA_DIRTY.__data: 0x5ba8
+  __DATA_DIRTY.__data: 0x5bc8
   __DATA_DIRTY.__bss: 0x1b30
   __DATA_DIRTY.__common: 0xb0
   - /System/Library/Frameworks/AVFAudio.framework/Versions/A/AVFAudio

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 19132
-  Symbols:   22781
-  CStrings:  7558
+  Functions: 19149
+  Symbols:   22808
+  CStrings:  7580
 
Symbols:
+ -[MPCFuture _removeInvalidHandler:]
+ -[MPCFuture invalidHandlers]
+ -[MPCFutureInvalidationToken dealloc]
+ -[MPCFutureInvalidationToken handler]
+ -[MPCFutureInvalidationToken setHandler:]
+ -[MPCModelStorePlaybackItemsRequest setVersionHashesByStoreID:]
+ -[MPCModelStorePlaybackItemsRequest versionHashesByStoreID]
+ -[MPCModelStorePlaybackItemsRequestAccumulation initWithProgressiveResults:properties:personalizationProperties:serverObjectDatabase:libraryObjectDatabase:performanceMetrics:]
+ -[_MPCModelStorePlaybackItemsRequestAccumulator_Legacy initWithRequest:serverObjectDatabase:account:]
+ -[_MPCModelStorePlaybackItemsRequestAccumulator_Modern initWithRequest:serverObjectDatabase:account:]
+ -[_MPCVideoLayerOutput customControlItems]
+ -[_MPCVideoLayerOutput setCustomControlItems:]
+ GCC_except_table1007
+ GCC_except_table1010
+ GCC_except_table1012
+ GCC_except_table1019
+ GCC_except_table1021
+ GCC_except_table1038
+ GCC_except_table1044
+ GCC_except_table1050
+ GCC_except_table1053
+ GCC_except_table1056
+ GCC_except_table1249
+ GCC_except_table1251
+ GCC_except_table1423
+ GCC_except_table1467
+ GCC_except_table1478
+ GCC_except_table1485
+ GCC_except_table1492
+ GCC_except_table1529
+ GCC_except_table1541
+ GCC_except_table1550
+ GCC_except_table1593
+ GCC_except_table1766
+ GCC_except_table1768
+ GCC_except_table1781
+ GCC_except_table1786
+ GCC_except_table1856
+ GCC_except_table1941
+ GCC_except_table1942
+ GCC_except_table2056
+ GCC_except_table2076
+ GCC_except_table2078
+ GCC_except_table2106
+ GCC_except_table2117
+ GCC_except_table2123
+ GCC_except_table2125
+ GCC_except_table2128
+ GCC_except_table2139
+ GCC_except_table2149
+ GCC_except_table2265
+ GCC_except_table2320
+ GCC_except_table2323
+ GCC_except_table2351
+ GCC_except_table2375
+ GCC_except_table2408
+ GCC_except_table2649
+ GCC_except_table2677
+ GCC_except_table2704
+ GCC_except_table2849
+ GCC_except_table2870
+ GCC_except_table2877
+ GCC_except_table2878
+ GCC_except_table2903
+ GCC_except_table2905
+ GCC_except_table2916
+ GCC_except_table2918
+ GCC_except_table2920
+ GCC_except_table2923
+ GCC_except_table2951
+ GCC_except_table2960
+ GCC_except_table2965
+ GCC_except_table2967
+ GCC_except_table2971
+ GCC_except_table2976
+ GCC_except_table2982
+ GCC_except_table2985
+ GCC_except_table2988
+ GCC_except_table3008
+ GCC_except_table3058
+ GCC_except_table3144
+ GCC_except_table3148
+ GCC_except_table3159
+ GCC_except_table3160
+ GCC_except_table3184
+ GCC_except_table3196
+ GCC_except_table3242
+ GCC_except_table3243
+ GCC_except_table3252
+ GCC_except_table3309
+ GCC_except_table3327
+ GCC_except_table3334
+ GCC_except_table3375
+ GCC_except_table3379
+ GCC_except_table3389
+ GCC_except_table3400
+ GCC_except_table3404
+ GCC_except_table3448
+ GCC_except_table3493
+ GCC_except_table3498
+ GCC_except_table3614
+ GCC_except_table3635
+ GCC_except_table3642
+ GCC_except_table3669
+ GCC_except_table3673
+ GCC_except_table3683
+ GCC_except_table3740
+ GCC_except_table3747
+ GCC_except_table3751
+ GCC_except_table3822
+ GCC_except_table390
+ GCC_except_table392
+ GCC_except_table3925
+ GCC_except_table3929
+ GCC_except_table3941
+ GCC_except_table3957
+ GCC_except_table3964
+ GCC_except_table3974
+ GCC_except_table4102
+ GCC_except_table4147
+ GCC_except_table4148
+ GCC_except_table4149
+ GCC_except_table4169
+ GCC_except_table4180
+ GCC_except_table4198
+ GCC_except_table4203
+ GCC_except_table4205
+ GCC_except_table4241
+ GCC_except_table4253
+ GCC_except_table4342
+ GCC_except_table4361
+ GCC_except_table4376
+ GCC_except_table4385
+ GCC_except_table4416
+ GCC_except_table445
+ GCC_except_table453
+ GCC_except_table4587
+ GCC_except_table4588
+ GCC_except_table463
+ GCC_except_table474
+ GCC_except_table4767
+ GCC_except_table4802
+ GCC_except_table4820
+ GCC_except_table4836
+ GCC_except_table4848
+ GCC_except_table4858
+ GCC_except_table4869
+ GCC_except_table4882
+ GCC_except_table4929
+ GCC_except_table4944
+ GCC_except_table4961
+ GCC_except_table4966
+ GCC_except_table4972
+ GCC_except_table5017
+ GCC_except_table5052
+ GCC_except_table5135
+ GCC_except_table5492
+ GCC_except_table558
+ GCC_except_table5594
+ GCC_except_table574
+ GCC_except_table5744
+ GCC_except_table575
+ GCC_except_table5769
+ GCC_except_table591
+ GCC_except_table592
+ GCC_except_table5941
+ GCC_except_table6007
+ GCC_except_table6032
+ GCC_except_table6067
+ GCC_except_table6070
+ GCC_except_table6073
+ GCC_except_table6159
+ GCC_except_table6376
+ GCC_except_table6393
+ GCC_except_table6844
+ GCC_except_table7188
+ GCC_except_table7198
+ GCC_except_table7288
+ GCC_except_table7297
+ GCC_except_table7386
+ GCC_except_table7393
+ GCC_except_table7411
+ GCC_except_table7462
+ GCC_except_table7463
+ GCC_except_table7466
+ GCC_except_table7487
+ GCC_except_table843
+ GCC_except_table899
+ GCC_except_table975
+ OBJC_IVAR_$_MPCFuture._invalidHandlers
+ OBJC_IVAR_$_MPCFutureInvalidationToken._handler
+ OBJC_IVAR_$_MPCModelStorePlaybackItemsRequest._versionHashesByStoreID
+ OBJC_IVAR_$_MPCPlaybackAccountManager._accountsUpdateQueue
+ OBJC_IVAR_$__MPCModelStorePlaybackItemsRequestAccumulator_Legacy._hasHandledStoreResponse
+ OBJC_IVAR_$__MPCVideoLayerOutput.customControlItems
+ _OBJC_CLASS_$_NSPointerArray
+ __101-[_MPCModelStorePlaybackItemsRequestAccumulator_Legacy initWithRequest:serverObjectDatabase:account:]_block_invoke
+ __101-[_MPCModelStorePlaybackItemsRequestAccumulator_Legacy initWithRequest:serverObjectDatabase:account:]_block_invoke_2
+ __101-[_MPCModelStorePlaybackItemsRequestAccumulator_Modern initWithRequest:serverObjectDatabase:account:]_block_invoke
+ __101-[_MPCModelStorePlaybackItemsRequestAccumulator_Modern initWithRequest:serverObjectDatabase:account:]_block_invoke_2
+ __119-[MPCAssistantRemoteControlDestination resolveWithRouteIdentifiers:allowedPlaybackTargets:audioRoutingInfo:completion:]_block_invoke
+ ___101-[_MPCModelStorePlaybackItemsRequestAccumulator_Legacy initWithRequest:serverObjectDatabase:account:]_block_invoke
+ ___101-[_MPCModelStorePlaybackItemsRequestAccumulator_Legacy initWithRequest:serverObjectDatabase:account:]_block_invoke_2
+ ___101-[_MPCModelStorePlaybackItemsRequestAccumulator_Legacy initWithRequest:serverObjectDatabase:account:]_block_invoke_3
+ ___101-[_MPCModelStorePlaybackItemsRequestAccumulator_Modern _locked_progressiveSectionWithoutVersionHash:]_block_invoke
+ ___101-[_MPCModelStorePlaybackItemsRequestAccumulator_Modern initWithRequest:serverObjectDatabase:account:]_block_invoke
+ ___101-[_MPCModelStorePlaybackItemsRequestAccumulator_Modern initWithRequest:serverObjectDatabase:account:]_block_invoke_2
+ ___101-[_MPCModelStorePlaybackItemsRequestAccumulator_Modern initWithRequest:serverObjectDatabase:account:]_block_invoke_3
+ ___107-[_MPCModelStorePlaybackItemsRequestAccumulator_Modern _locked_detectVersionHashMismatchIfNeeded:childKey:]_block_invoke
+ ___175-[MPCModelStorePlaybackItemsRequestAccumulation initWithProgressiveResults:properties:personalizationProperties:serverObjectDatabase:libraryObjectDatabase:performanceMetrics:]_block_invoke
+ ___175-[MPCModelStorePlaybackItemsRequestAccumulation initWithProgressiveResults:properties:personalizationProperties:serverObjectDatabase:libraryObjectDatabase:performanceMetrics:]_block_invoke_2
+ ___175-[MPCModelStorePlaybackItemsRequestAccumulation initWithProgressiveResults:properties:personalizationProperties:serverObjectDatabase:libraryObjectDatabase:performanceMetrics:]_block_invoke_3
+ ___175-[MPCModelStorePlaybackItemsRequestAccumulation initWithProgressiveResults:properties:personalizationProperties:serverObjectDatabase:libraryObjectDatabase:performanceMetrics:]_block_invoke_4
+ ___175-[MPCModelStorePlaybackItemsRequestAccumulation initWithProgressiveResults:properties:personalizationProperties:serverObjectDatabase:libraryObjectDatabase:performanceMetrics:]_block_invoke_5
+ ___175-[MPCModelStorePlaybackItemsRequestAccumulation initWithProgressiveResults:properties:personalizationProperties:serverObjectDatabase:libraryObjectDatabase:performanceMetrics:]_block_invoke_6
+ ___35-[MPCFuture _removeInvalidHandler:]_block_invoke
+ ___36+[MPCPlaybackEngine preheatPlayback]_block_invoke_2
+ ___57-[MPCPlaybackAccountManager performAfterLoadingAccounts:]_block_invoke
+ ___block_descriptor_40_e8_32r_e14_v24?0{?=qiI}8l
+ ___block_descriptor_48_e8_32s40bs_e9_v16?0^v8l
+ ___block_descriptor_49_e8_32s40s_e18_16?0"NSString"8l
+ ___block_descriptor_61_e8_32s40s48s_e49_v16?0"MPIdentifierSet<MPMutableIdentifierSet>"8l
+ _objc_msgSend$_removeInvalidHandler:
+ _objc_msgSend$addPointer:
+ _objc_msgSend$initWithProgressiveResults:properties:personalizationProperties:serverObjectDatabase:libraryObjectDatabase:performanceMetrics:
+ _objc_msgSend$initWithRequest:serverObjectDatabase:account:
+ _objc_msgSend$pointerAtIndex:
+ _objc_msgSend$replacePointerAtIndex:withPointer:
+ _objc_msgSend$setHandler:
+ _objc_msgSend$strongObjectsPointerArray
+ _objc_msgSend$tokenForDatabase:
+ _objc_msgSend$versionHashesByStoreID
- -[MPCFuture invalidBlocks]
- -[MPCModelStorePlaybackItemsRequestAccumulation initWithProgressiveResults:properties:personalizationProperties:libraryObjectDatabase:performanceMetrics:]
- -[_MPCModelStorePlaybackItemsRequestAccumulator_Legacy initWithRequest:serverObjectDatabase:]
- -[_MPCModelStorePlaybackItemsRequestAccumulator_Modern initWithRequest:serverObjectDatabase:]
- GCC_except_table1003
- GCC_except_table1006
- GCC_except_table1008
- GCC_except_table1015
- GCC_except_table1017
- GCC_except_table1030
- GCC_except_table1040
- GCC_except_table1046
- GCC_except_table1049
- GCC_except_table1052
- GCC_except_table1241
- GCC_except_table1247
- GCC_except_table1415
- GCC_except_table1463
- GCC_except_table1474
- GCC_except_table1481
- GCC_except_table1488
- GCC_except_table1525
- GCC_except_table1537
- GCC_except_table1546
- GCC_except_table1589
- GCC_except_table1762
- GCC_except_table1764
- GCC_except_table1777
- GCC_except_table1782
- GCC_except_table1852
- GCC_except_table1937
- GCC_except_table1938
- GCC_except_table2052
- GCC_except_table2072
- GCC_except_table2074
- GCC_except_table2102
- GCC_except_table2113
- GCC_except_table2119
- GCC_except_table2121
- GCC_except_table2124
- GCC_except_table2135
- GCC_except_table2145
- GCC_except_table2261
- GCC_except_table2312
- GCC_except_table2319
- GCC_except_table2347
- GCC_except_table2371
- GCC_except_table2404
- GCC_except_table2645
- GCC_except_table2673
- GCC_except_table2700
- GCC_except_table2843
- GCC_except_table2864
- GCC_except_table2871
- GCC_except_table2872
- GCC_except_table2897
- GCC_except_table2899
- GCC_except_table2904
- GCC_except_table2908
- GCC_except_table2912
- GCC_except_table2917
- GCC_except_table2945
- GCC_except_table2952
- GCC_except_table2957
- GCC_except_table2959
- GCC_except_table2963
- GCC_except_table2968
- GCC_except_table2969
- GCC_except_table2974
- GCC_except_table2980
- GCC_except_table3000
- GCC_except_table3050
- GCC_except_table3136
- GCC_except_table3140
- GCC_except_table3151
- GCC_except_table3152
- GCC_except_table3176
- GCC_except_table3188
- GCC_except_table3234
- GCC_except_table3235
- GCC_except_table3244
- GCC_except_table3301
- GCC_except_table3319
- GCC_except_table3326
- GCC_except_table3367
- GCC_except_table3371
- GCC_except_table3381
- GCC_except_table3392
- GCC_except_table3396
- GCC_except_table3440
- GCC_except_table3485
- GCC_except_table3490
- GCC_except_table3606
- GCC_except_table3627
- GCC_except_table3634
- GCC_except_table3661
- GCC_except_table3665
- GCC_except_table3675
- GCC_except_table3732
- GCC_except_table3739
- GCC_except_table3743
- GCC_except_table3814
- GCC_except_table387
- GCC_except_table389
- GCC_except_table3917
- GCC_except_table3921
- GCC_except_table3933
- GCC_except_table3949
- GCC_except_table3956
- GCC_except_table3966
- GCC_except_table4094
- GCC_except_table4139
- GCC_except_table4140
- GCC_except_table4141
- GCC_except_table4161
- GCC_except_table4172
- GCC_except_table4190
- GCC_except_table4195
- GCC_except_table4197
- GCC_except_table4233
- GCC_except_table4245
- GCC_except_table4334
- GCC_except_table4353
- GCC_except_table4368
- GCC_except_table4377
- GCC_except_table4408
- GCC_except_table442
- GCC_except_table450
- GCC_except_table4579
- GCC_except_table4580
- GCC_except_table460
- GCC_except_table471
- GCC_except_table4759
- GCC_except_table4794
- GCC_except_table4796
- GCC_except_table4828
- GCC_except_table4840
- GCC_except_table4850
- GCC_except_table4861
- GCC_except_table4874
- GCC_except_table4921
- GCC_except_table4936
- GCC_except_table4953
- GCC_except_table4958
- GCC_except_table4964
- GCC_except_table5009
- GCC_except_table5044
- GCC_except_table5127
- GCC_except_table5482
- GCC_except_table554
- GCC_except_table5583
- GCC_except_table570
- GCC_except_table571
- GCC_except_table5733
- GCC_except_table5758
- GCC_except_table587
- GCC_except_table588
- GCC_except_table5930
- GCC_except_table5996
- GCC_except_table6021
- GCC_except_table6056
- GCC_except_table6059
- GCC_except_table6062
- GCC_except_table6148
- GCC_except_table6365
- GCC_except_table6382
- GCC_except_table6833
- GCC_except_table7177
- GCC_except_table7187
- GCC_except_table7277
- GCC_except_table7286
- GCC_except_table7370
- GCC_except_table7377
- GCC_except_table7395
- GCC_except_table7446
- GCC_except_table7447
- GCC_except_table7450
- GCC_except_table7455
- GCC_except_table839
- GCC_except_table895
- GCC_except_table971
- OBJC_IVAR_$_MPCFuture._invalidBlocks
- __114-[_MPCModelStorePlaybackItemsRequestAccumulator_Legacy _locked_resolveContentDescriptorsUsingServerObjectDatabase]_block_invoke_2
- __93-[_MPCModelStorePlaybackItemsRequestAccumulator_Legacy initWithRequest:serverObjectDatabase:]_block_invoke
- __93-[_MPCModelStorePlaybackItemsRequestAccumulator_Legacy initWithRequest:serverObjectDatabase:]_block_invoke_2
- __93-[_MPCModelStorePlaybackItemsRequestAccumulator_Modern initWithRequest:serverObjectDatabase:]_block_invoke
- __93-[_MPCModelStorePlaybackItemsRequestAccumulator_Modern initWithRequest:serverObjectDatabase:]_block_invoke_2
- ___154-[MPCModelStorePlaybackItemsRequestAccumulation initWithProgressiveResults:properties:personalizationProperties:libraryObjectDatabase:performanceMetrics:]_block_invoke
- ___154-[MPCModelStorePlaybackItemsRequestAccumulation initWithProgressiveResults:properties:personalizationProperties:libraryObjectDatabase:performanceMetrics:]_block_invoke_2
- ___154-[MPCModelStorePlaybackItemsRequestAccumulation initWithProgressiveResults:properties:personalizationProperties:libraryObjectDatabase:performanceMetrics:]_block_invoke_3
- ___154-[MPCModelStorePlaybackItemsRequestAccumulation initWithProgressiveResults:properties:personalizationProperties:libraryObjectDatabase:performanceMetrics:]_block_invoke_4
- ___154-[MPCModelStorePlaybackItemsRequestAccumulation initWithProgressiveResults:properties:personalizationProperties:libraryObjectDatabase:performanceMetrics:]_block_invoke_5
- ___154-[MPCModelStorePlaybackItemsRequestAccumulation initWithProgressiveResults:properties:personalizationProperties:libraryObjectDatabase:performanceMetrics:]_block_invoke_6
- ___93-[_MPCModelStorePlaybackItemsRequestAccumulator_Legacy initWithRequest:serverObjectDatabase:]_block_invoke
- ___93-[_MPCModelStorePlaybackItemsRequestAccumulator_Legacy initWithRequest:serverObjectDatabase:]_block_invoke_2
- ___93-[_MPCModelStorePlaybackItemsRequestAccumulator_Legacy initWithRequest:serverObjectDatabase:]_block_invoke_3
- ___93-[_MPCModelStorePlaybackItemsRequestAccumulator_Modern initWithRequest:serverObjectDatabase:]_block_invoke
- ___93-[_MPCModelStorePlaybackItemsRequestAccumulator_Modern initWithRequest:serverObjectDatabase:]_block_invoke_2
- ___93-[_MPCModelStorePlaybackItemsRequestAccumulator_Modern initWithRequest:serverObjectDatabase:]_block_invoke_3
- ___block_descriptor_41_e8_32s_e18_16?0"NSString"8l
- ___block_descriptor_53_e8_32s40s_e49_v16?0"MPIdentifierSet<MPMutableIdentifierSet>"8l
- _objc_msgSend$initWithProgressiveResults:properties:personalizationProperties:libraryObjectDatabase:performanceMetrics:
- _objc_msgSend$initWithRequest:serverObjectDatabase:
- _objc_msgSend$weakToStrongObjectsMapTable
- _symbolic yt______pIgrzo_ s5ErrorP
CStrings:
+ " versionHashesByStoreID=%@"
+ "AccumulationSectionPromotionUnsupported"
+ "AccumulationVersionHashUnavailable"
+ "Cannot promote items to sections for a request using sectionedModelObjects: %@"
+ "Future has accumulated %lu invalidation handlers: %{public}@"
+ "MPCModelStorePlaybackItemsRequestVersionHashesByStoreID"
+ "PreheatPlayback"
+ "SEED"
+ "Store did not provide versionHash '%@' for container %@"
+ "Update: %{public}@<%{public}@> Falling back to watch due to error=%@. Connect Device Dialog Imminent"
+ "XL-Accumulator-VersionHashLess"
+ "[%{public}@]-MPCPlayerItemConfigurator %p - [AP] - Deferring Alchemy configuration [start item, transitions disabled, audio accessory]: %{public}@"
+ "[BMUS:%{public}@:%{public}@] _addPlaybackContext: | disabling auto play [%{public}@]"
+ "[PIA] %p container has no children with any versionHash [empty, not a versionHash mismatch] identifier=%{public}@ versionHash=%{public}@"
+ "[PIA] %p failing request [requested versionHash unavailable after load] identifier=%{public}@ versionHash=%{public}@"
+ "[PIA] %p failing request [section promotion unsupported for sectionedModelObjects] indexPaths=%{public}@"
+ "[PL:%{public}s] TRANSITION: Skipping transition setup - a seek/jump is in flight [caller: %{public}s] - will re-evaluate on seek completion"
+ "[SPIR:%{sonic:fourCC}u] execute | finished with placeholders [prioritized batch reported complete]"
+ "[SPIR:%{sonic:fourCC}u] execute | finished with placeholders [prioritized batch reported complete] unpersonalizedContentDescriptors=%{public}@"
+ "[SPIR:%{sonic:fourCC}u] execute | loadPage [firstPage]"
+ "[SPIR:%{sonic:fourCC}u] populateSection:sectionIndex: | container has no children with any versionHash [treating as empty, not a versionHash mismatch] progressiveSection=%{public}@"
+ "[SPIR:%{sonic:fourCC}u] populateSection:sectionIndex: | failing request [store cannot provide requested versionHash] progressiveSection=%{public}@ versionHash=%{public}@"
+ "assetQueueDidChange(state:)"
+ "com.apple.mediaplaybackcore.accountmanager.update"
+ "data source unsupported"
+ "guest account unsupported"
+ "restoreCurrentTransitionIfNeeded()"
+ "sendOverlappedPlaybackDidEndForOngoingTransition()"
+ "setupNextPlayerItemTransition(_:caller:)"
- "\nc"
- "MPC_LIVE_LINK_UNABLE_TO_SHAREPLAY_ALERT_ACTION"
- "MPC_LIVE_LINK_UNABLE_TO_SHAREPLAY_ALERT_TITLE"
- "[BMUS:%{public}@:%{public}@] _addPlaybackContext: | disabling auto play [data source unsupported]"
- "[SPIR%{sonic:fourCC}u] execute | loadPage [firstPage]"
- "[SPIR:%{sonic:fourCC}u] execute | finished with placeholders [prioritized IDs loaded]"
- "[SPIR:%{sonic:fourCC}u] execute | finished with placeholders [prioritized IDs loaded] unpersonalizedContentDescriptors=%{public}@"
```
