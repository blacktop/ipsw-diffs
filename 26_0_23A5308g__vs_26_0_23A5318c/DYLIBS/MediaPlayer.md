## MediaPlayer

> `/System/Library/Frameworks/MediaPlayer.framework/MediaPlayer`

```diff

-4025.100.128.0.0
-  __TEXT.__text: 0x36ccd0
+4025.110.1.0.0
+  __TEXT.__text: 0x36d714
   __TEXT.__auth_stubs: 0x53a0
-  __TEXT.__objc_methlist: 0x281f4
+  __TEXT.__objc_methlist: 0x281c4
   __TEXT.__dlopen_cstrs: 0x4bd
-  __TEXT.__const: 0x17178
+  __TEXT.__const: 0x17180
   __TEXT.__swift5_typeref: 0x14e
   __TEXT.__swift5_capture: 0xe8
-  __TEXT.__cstring: 0x30bca
+  __TEXT.__cstring: 0x30c5f
   __TEXT.__constg_swiftt: 0xac
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_reflstr: 0x19

   __TEXT.__swift_as_entry: 0x1c
   __TEXT.__swift_as_ret: 0x1c
   __TEXT.__swift5_proto: 0x14
-  __TEXT.__gcc_except_tab: 0x1cb98
-  __TEXT.__oslogstring: 0x1917b
+  __TEXT.__gcc_except_tab: 0x1cbe4
+  __TEXT.__oslogstring: 0x19373
   __TEXT.__ustring: 0x1ca
   __TEXT.__unwind_info: 0xcda0
   __TEXT.__eh_frame: 0x460
   __TEXT.__objc_classname: 0x6322
-  __TEXT.__objc_methname: 0x62f7b
-  __TEXT.__objc_methtype: 0xde9b
-  __TEXT.__objc_stubs: 0x32b40
-  __DATA_CONST.__got: 0x2f30
-  __DATA_CONST.__const: 0xd610
+  __TEXT.__objc_methname: 0x62f31
+  __TEXT.__objc_methtype: 0xde65
+  __TEXT.__objc_stubs: 0x32a80
+  __DATA_CONST.__got: 0x2f38
+  __DATA_CONST.__const: 0xd670
   __DATA_CONST.__objc_classlist: 0x14f0
   __DATA_CONST.__objc_catlist: 0x108
   __DATA_CONST.__objc_protolist: 0x420
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x133e0
+  __DATA_CONST.__objc_selrefs: 0x133d0
   __DATA_CONST.__objc_protorefs: 0xe0
   __DATA_CONST.__objc_superrefs: 0xda8
   __DATA_CONST.__objc_arraydata: 0x890
   __AUTH_CONST.__auth_got: 0x29e8
   __AUTH_CONST.__const: 0xf3f8
-  __AUTH_CONST.__cfstring: 0x26c60
-  __AUTH_CONST.__objc_const: 0x45138
+  __AUTH_CONST.__cfstring: 0x26de0
+  __AUTH_CONST.__objc_const: 0x451d8
   __AUTH_CONST.__objc_intobj: 0x870
   __AUTH_CONST.__objc_arrayobj: 0xf30
   __AUTH_CONST.__objc_doubleobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH.__objc_data: 0xa780
   __AUTH.__data: 0xd8
-  __DATA.__objc_ivar: 0x2cf8
+  __DATA.__objc_ivar: 0x2d04
   __DATA.__data: 0x3608
   __DATA.__bss: 0xd30
   __DATA.__common: 0xa29

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: C885ECB3-0BA9-31AE-A6E1-9B72EC9568CB
-  Functions: 16864
-  Symbols:   56538
-  CStrings:  28685
+  UUID: 893DFDA3-1EE5-30DA-BC25-F807BCCE0B66
+  Functions: 16873
+  Symbols:   56554
+  CStrings:  28715
 
Symbols:
+ +[MPNowPlayingInfoCenter defaultExpectedQueueSize]
+ -[MPAVItem isInSmartTransition]
+ -[MPAVItem isInTransition]
+ -[MPAVItem setInSmartTransition:]
+ -[MPMediaControlsConfiguration setSurface:]
+ -[MPMediaControlsConfiguration surface]
+ -[MPNowPlayingInfoCenter _invalidatePlaybackQueueBoundaryWithExpectedQueueSize:]
+ -[MPNowPlayingInfoCenter _onQueue_ensureContentItemStorageInitialized]
+ -[MPNowPlayingInfoCenter _updateBloomFilterWithContentItemID:]
+ GCC_except_table13525
+ GCC_except_table13526
+ GCC_except_table13532
+ GCC_except_table13538
+ GCC_except_table13671
+ GCC_except_table13673
+ GCC_except_table13702
+ GCC_except_table13832
+ GCC_except_table13858
+ GCC_except_table13862
+ GCC_except_table13981
+ GCC_except_table13998
+ GCC_except_table14040
+ GCC_except_table14062
+ GCC_except_table14301
+ GCC_except_table14330
+ GCC_except_table14337
+ GCC_except_table14363
+ GCC_except_table14365
+ GCC_except_table14378
+ GCC_except_table14415
+ GCC_except_table14525
+ GCC_except_table14565
+ GCC_except_table14576
+ GCC_except_table14581
+ GCC_except_table14818
+ GCC_except_table14884
+ GCC_except_table14886
+ GCC_except_table14908
+ GCC_except_table14913
+ GCC_except_table14915
+ GCC_except_table15323
+ GCC_except_table15328
+ GCC_except_table15334
+ GCC_except_table15356
+ GCC_except_table15364
+ GCC_except_table15366
+ GCC_except_table15368
+ GCC_except_table15377
+ GCC_except_table15383
+ GCC_except_table15386
+ GCC_except_table15391
+ GCC_except_table15394
+ GCC_except_table15399
+ GCC_except_table15401
+ GCC_except_table15404
+ GCC_except_table15464
+ GCC_except_table15473
+ GCC_except_table15475
+ GCC_except_table15481
+ GCC_except_table15595
+ GCC_except_table15771
+ GCC_except_table15774
+ GCC_except_table15833
+ GCC_except_table15846
+ GCC_except_table15850
+ GCC_except_table15854
+ GCC_except_table15855
+ GCC_except_table15856
+ GCC_except_table15860
+ GCC_except_table16443
+ GCC_except_table16521
+ GCC_except_table16618
+ _CarKitLibraryCore.frameworkLibrary.49680
+ _MSVFastHexStringFromBytes.hexCharacters.55962
+ _OBJC_CLASS_$_MSVBloomFilter
+ _OBJC_IVAR_$_MPAVItem._inSmartTransition
+ _OBJC_IVAR_$_MPMediaControlsConfiguration._surface
+ _OBJC_IVAR_$_MPNowPlayingInfoCenter._contentItemBloomFilter
+ __MSV_XXH_XXH32_update.52647
+ __MSV_XXH_XXH64_update.52648
+ ___57-[MPNowPlayingInfoCenter _onQueue_pushContentItemsUpdate]_block_invoke.237
+ ___57-[MPNowPlayingInfoCenter _onQueue_pushContentItemsUpdate]_block_invoke.244
+ ___58-[MPNowPlayingInfoCenter _contentItemChangedNotification:]_block_invoke.235
+ ___76-[MPNowPlayingInfoCenter _invalidatePlaybackQueueImmediatelyWithCompletion:]_block_invoke.102
+ ___76-[MPNowPlayingInfoCenter _onQueue_registerPlaybackQueueDataSourceCallbacks:]_block_invoke.143
+ ___76-[MPNowPlayingInfoCenter _onQueue_registerPlaybackQueueDataSourceCallbacks:]_block_invoke_10.168
+ ___76-[MPNowPlayingInfoCenter _onQueue_registerPlaybackQueueDataSourceCallbacks:]_block_invoke_11.169
+ ___76-[MPNowPlayingInfoCenter _onQueue_registerPlaybackQueueDataSourceCallbacks:]_block_invoke_12.170
+ ___76-[MPNowPlayingInfoCenter _onQueue_registerPlaybackQueueDataSourceCallbacks:]_block_invoke_13.171
+ ___76-[MPNowPlayingInfoCenter _onQueue_registerPlaybackQueueDataSourceCallbacks:]_block_invoke_14.175
+ ___76-[MPNowPlayingInfoCenter _onQueue_registerPlaybackQueueDataSourceCallbacks:]_block_invoke_15.176
+ ___76-[MPNowPlayingInfoCenter _onQueue_registerPlaybackQueueDataSourceCallbacks:]_block_invoke_16.177
+ ___76-[MPNowPlayingInfoCenter _onQueue_registerPlaybackQueueDataSourceCallbacks:]_block_invoke_17.178
+ ___76-[MPNowPlayingInfoCenter _onQueue_registerPlaybackQueueDataSourceCallbacks:]_block_invoke_18.184
+ ___76-[MPNowPlayingInfoCenter _onQueue_registerPlaybackQueueDataSourceCallbacks:]_block_invoke_19.185
+ ___76-[MPNowPlayingInfoCenter _onQueue_registerPlaybackQueueDataSourceCallbacks:]_block_invoke_2.145
+ ___76-[MPNowPlayingInfoCenter _onQueue_registerPlaybackQueueDataSourceCallbacks:]_block_invoke_20.186
+ ___76-[MPNowPlayingInfoCenter _onQueue_registerPlaybackQueueDataSourceCallbacks:]_block_invoke_21.187
+ ___76-[MPNowPlayingInfoCenter _onQueue_registerPlaybackQueueDataSourceCallbacks:]_block_invoke_22.188
+ ___76-[MPNowPlayingInfoCenter _onQueue_registerPlaybackQueueDataSourceCallbacks:]_block_invoke_23.189
+ ___76-[MPNowPlayingInfoCenter _onQueue_registerPlaybackQueueDataSourceCallbacks:]_block_invoke_3.146
+ ___76-[MPNowPlayingInfoCenter _onQueue_registerPlaybackQueueDataSourceCallbacks:]_block_invoke_4.154
+ ___76-[MPNowPlayingInfoCenter _onQueue_registerPlaybackQueueDataSourceCallbacks:]_block_invoke_5.155
+ ___76-[MPNowPlayingInfoCenter _onQueue_registerPlaybackQueueDataSourceCallbacks:]_block_invoke_6.161
+ ___76-[MPNowPlayingInfoCenter _onQueue_registerPlaybackQueueDataSourceCallbacks:]_block_invoke_7.162
+ ___76-[MPNowPlayingInfoCenter _onQueue_registerPlaybackQueueDataSourceCallbacks:]_block_invoke_8.163
+ ___76-[MPNowPlayingInfoCenter _onQueue_registerPlaybackQueueDataSourceCallbacks:]_block_invoke_9.164
+ ___77-[MPNowPlayingInfoCenter _contentItemForIdentifier:alreadyOnDataSourceQueue:]_block_invoke.70
+ ___80-[MPNowPlayingInfoCenter _invalidatePlaybackQueueBoundaryWithExpectedQueueSize:]_block_invoke
+ ___80-[MPNowPlayingInfoCenter _invalidatePlaybackQueueBoundaryWithExpectedQueueSize:]_block_invoke.233
+ ___80-[MPNowPlayingInfoCenter _invalidatePlaybackQueueBoundaryWithExpectedQueueSize:]_block_invoke_2
+ ___81-[MPNowPlayingInfoCenter _onDataSourceQueue_getContentItemIDsInRange:completion:]_block_invoke.111
+ ___Block_byref_object_copy_.48369
+ ___Block_byref_object_copy_.49043
+ ___Block_byref_object_copy_.49129
+ ___Block_byref_object_copy_.49696
+ ___Block_byref_object_copy_.49926
+ ___Block_byref_object_copy_.51125
+ ___Block_byref_object_copy_.51747
+ ___Block_byref_object_copy_.54661
+ ___Block_byref_object_copy_.55283
+ ___Block_byref_object_copy_.58731
+ ___Block_byref_object_dispose_.48370
+ ___Block_byref_object_dispose_.49044
+ ___Block_byref_object_dispose_.49130
+ ___Block_byref_object_dispose_.49697
+ ___Block_byref_object_dispose_.49927
+ ___Block_byref_object_dispose_.51126
+ ___Block_byref_object_dispose_.51748
+ ___Block_byref_object_dispose_.54662
+ ___Block_byref_object_dispose_.55284
+ ___Block_byref_object_dispose_.58732
+ ___CarKitLibraryCore_block_invoke.49681
+ ___block_descriptor_56_e8_32s40s48r_e5_v8?0ls32l8r48l8s40l8
+ ___block_descriptor_72_e8_32s40r48r56r64r_e5_v8?0ls32l8r40l8r48l8r56l8r64l8
+ ___block_literal_global.104.56427
+ ___block_literal_global.109.51768
+ ___block_literal_global.110.54665
+ ___block_literal_global.112.56394
+ ___block_literal_global.113.51758
+ ___block_literal_global.119.51741
+ ___block_literal_global.121.51730
+ ___block_literal_global.127.51709
+ ___block_literal_global.132.51693
+ ___block_literal_global.134.51687
+ ___block_literal_global.136.51681
+ ___block_literal_global.140
+ ___block_literal_global.144.51659
+ ___block_literal_global.144.56377
+ ___block_literal_global.152.51652
+ ___block_literal_global.156.51646
+ ___block_literal_global.158.51648
+ ___block_literal_global.163.51640
+ ___block_literal_global.217.53569
+ ___block_literal_global.227.55280
+ ___block_literal_global.25.55250
+ ___block_literal_global.27.49786
+ ___block_literal_global.35.54873
+ ___block_literal_global.38.54865
+ ___block_literal_global.39.55287
+ ___block_literal_global.39.56514
+ ___block_literal_global.45.54789
+ ___block_literal_global.47
+ ___block_literal_global.48423
+ ___block_literal_global.49053
+ ___block_literal_global.49142
+ ___block_literal_global.49791
+ ___block_literal_global.49923
+ ___block_literal_global.50697
+ ___block_literal_global.51135
+ ___block_literal_global.51868
+ ___block_literal_global.52475
+ ___block_literal_global.53232
+ ___block_literal_global.53592
+ ___block_literal_global.54918
+ ___block_literal_global.55285
+ ___block_literal_global.56.51862
+ ___block_literal_global.56.53585
+ ___block_literal_global.56546
+ ___block_literal_global.56996
+ ___block_literal_global.57417
+ ___block_literal_global.57542
+ ___block_literal_global.58763
+ ___block_literal_global.58828
+ ___block_literal_global.6.54915
+ ___block_literal_global.68.53203
+ ___block_literal_global.72.56453
+ ___block_literal_global.75.56455
+ ___block_literal_global.93.51811
+ ___block_literal_global.96.51799
+ ___getCARSessionStatusClass_block_invoke.49776
+ _audit_stringCarKit.49684
+ _getCARSessionStatusClass.softClass.49775
+ _initWithPlayerPath:.onceToken.56523
+ _objc_msgSend$initWithCapacity:falsePositiveTolerance:
+ _objc_msgSend$isInSmartTransition
+ _objc_msgSend$setInTransition:
+ _objc_msgSend$setSurface:
+ _objc_msgSend$surface
- -[MPNowPlayingInfoCenter _contentItemIDsInRange:itemsRange:]
- -[MPNowPlayingInfoCenter _createPlaybackQueueForRequest:]
- -[MPNowPlayingInfoCenter _onDataSourceQueue_artworkCatalogForContentItem:]
- -[MPNowPlayingInfoCenter _onQueue_registerLyricsDelegateCallbacks:]
- -[MPNowPlayingInfoCenter _onQueue_registerPlaybackQueueDataSourceCallbacks:]
- GCC_except_table13522
- GCC_except_table13523
- GCC_except_table13528
- GCC_except_table13536
- GCC_except_table13668
- GCC_except_table13670
- GCC_except_table13699
- GCC_except_table13829
- GCC_except_table13855
- GCC_except_table13859
- GCC_except_table13978
- GCC_except_table13995
- GCC_except_table14037
- GCC_except_table14059
- GCC_except_table14298
- GCC_except_table14327
- GCC_except_table14331
- GCC_except_table14360
- GCC_except_table14362
- GCC_except_table14375
- GCC_except_table14412
- GCC_except_table14522
- GCC_except_table14562
- GCC_except_table14573
- GCC_except_table14578
- GCC_except_table14815
- GCC_except_table14875
- GCC_except_table14883
- GCC_except_table14905
- GCC_except_table14910
- GCC_except_table14912
- GCC_except_table15316
- GCC_except_table15322
- GCC_except_table15324
- GCC_except_table15325
- GCC_except_table15371
- GCC_except_table15378
- GCC_except_table15384
- GCC_except_table15407
- GCC_except_table15413
- GCC_except_table15424
- GCC_except_table15426
- GCC_except_table15428
- GCC_except_table15437
- GCC_except_table15443
- GCC_except_table15447
- GCC_except_table15458
- GCC_except_table15463
- GCC_except_table15467
- GCC_except_table15468
- GCC_except_table15588
- GCC_except_table15764
- GCC_except_table15767
- GCC_except_table15826
- GCC_except_table15839
- GCC_except_table15841
- GCC_except_table15843
- GCC_except_table15847
- GCC_except_table15849
- GCC_except_table15853
- GCC_except_table16436
- GCC_except_table16514
- GCC_except_table16609
- _CarKitLibraryCore.frameworkLibrary.49674
- _MSVFastHexStringFromBytes.hexCharacters.55952
- __MSV_XXH_XXH32_update.52641
- __MSV_XXH_XXH64_update.52642
- ___57-[MPNowPlayingInfoCenter _onQueue_pushContentItemsUpdate]_block_invoke.226
- ___57-[MPNowPlayingInfoCenter _onQueue_pushContentItemsUpdate]_block_invoke.233
- ___58-[MPNowPlayingInfoCenter _contentItemChangedNotification:]_block_invoke.224
- ___76-[MPNowPlayingInfoCenter _invalidatePlaybackQueueImmediatelyWithCompletion:]_block_invoke.97
- ___76-[MPNowPlayingInfoCenter _onQueue_registerPlaybackQueueDataSourceCallbacks:]_block_invoke.138
- ___76-[MPNowPlayingInfoCenter _onQueue_registerPlaybackQueueDataSourceCallbacks:]_block_invoke_10.163
- ___76-[MPNowPlayingInfoCenter _onQueue_registerPlaybackQueueDataSourceCallbacks:]_block_invoke_11.164
- ___76-[MPNowPlayingInfoCenter _onQueue_registerPlaybackQueueDataSourceCallbacks:]_block_invoke_12.165
- ___76-[MPNowPlayingInfoCenter _onQueue_registerPlaybackQueueDataSourceCallbacks:]_block_invoke_13.166
- ___76-[MPNowPlayingInfoCenter _onQueue_registerPlaybackQueueDataSourceCallbacks:]_block_invoke_14.170
- ___76-[MPNowPlayingInfoCenter _onQueue_registerPlaybackQueueDataSourceCallbacks:]_block_invoke_15.171
- ___76-[MPNowPlayingInfoCenter _onQueue_registerPlaybackQueueDataSourceCallbacks:]_block_invoke_16.172
- ___76-[MPNowPlayingInfoCenter _onQueue_registerPlaybackQueueDataSourceCallbacks:]_block_invoke_17.173
- ___76-[MPNowPlayingInfoCenter _onQueue_registerPlaybackQueueDataSourceCallbacks:]_block_invoke_18.179
- ___76-[MPNowPlayingInfoCenter _onQueue_registerPlaybackQueueDataSourceCallbacks:]_block_invoke_19.180
- ___76-[MPNowPlayingInfoCenter _onQueue_registerPlaybackQueueDataSourceCallbacks:]_block_invoke_2.140
- ___76-[MPNowPlayingInfoCenter _onQueue_registerPlaybackQueueDataSourceCallbacks:]_block_invoke_20.181
- ___76-[MPNowPlayingInfoCenter _onQueue_registerPlaybackQueueDataSourceCallbacks:]_block_invoke_21.182
- ___76-[MPNowPlayingInfoCenter _onQueue_registerPlaybackQueueDataSourceCallbacks:]_block_invoke_3.141
- ___76-[MPNowPlayingInfoCenter _onQueue_registerPlaybackQueueDataSourceCallbacks:]_block_invoke_4.149
- ___76-[MPNowPlayingInfoCenter _onQueue_registerPlaybackQueueDataSourceCallbacks:]_block_invoke_5.150
- ___76-[MPNowPlayingInfoCenter _onQueue_registerPlaybackQueueDataSourceCallbacks:]_block_invoke_6.156
- ___76-[MPNowPlayingInfoCenter _onQueue_registerPlaybackQueueDataSourceCallbacks:]_block_invoke_7.157
- ___76-[MPNowPlayingInfoCenter _onQueue_registerPlaybackQueueDataSourceCallbacks:]_block_invoke_8.158
- ___76-[MPNowPlayingInfoCenter _onQueue_registerPlaybackQueueDataSourceCallbacks:]_block_invoke_9.159
- ___77-[MPNowPlayingInfoCenter _contentItemForIdentifier:alreadyOnDataSourceQueue:]_block_invoke.67
- ___81-[MPNowPlayingInfoCenter _onDataSourceQueue_getContentItemIDsInRange:completion:]_block_invoke.106
- ___Block_byref_object_copy_.48362
- ___Block_byref_object_copy_.49037
- ___Block_byref_object_copy_.49123
- ___Block_byref_object_copy_.49690
- ___Block_byref_object_copy_.49920
- ___Block_byref_object_copy_.51119
- ___Block_byref_object_copy_.51741
- ___Block_byref_object_copy_.54705
- ___Block_byref_object_copy_.55274
- ___Block_byref_object_copy_.58721
- ___Block_byref_object_dispose_.48363
- ___Block_byref_object_dispose_.49038
- ___Block_byref_object_dispose_.49124
- ___Block_byref_object_dispose_.49691
- ___Block_byref_object_dispose_.49921
- ___Block_byref_object_dispose_.51120
- ___Block_byref_object_dispose_.51742
- ___Block_byref_object_dispose_.54706
- ___Block_byref_object_dispose_.55275
- ___Block_byref_object_dispose_.58722
- ___CarKitLibraryCore_block_invoke.49675
- ___block_descriptor_56_e8_32s40s48r_e5_v8?0ls32l8s40l8r48l8
- ___block_descriptor_72_e8_32s40r48r56r64r_e5_v8?0lr40l8s32l8r48l8r56l8r64l8
- ___block_literal_global.104.56417
- ___block_literal_global.105
- ___block_literal_global.109.51762
- ___block_literal_global.112.56384
- ___block_literal_global.113.51752
- ___block_literal_global.119.51735
- ___block_literal_global.121.51724
- ___block_literal_global.127.51703
- ___block_literal_global.132.51687
- ___block_literal_global.134.51681
- ___block_literal_global.135.54731
- ___block_literal_global.136.51675
- ___block_literal_global.144.51653
- ___block_literal_global.144.56367
- ___block_literal_global.152.51646
- ___block_literal_global.156.51640
- ___block_literal_global.158.51642
- ___block_literal_global.163.51634
- ___block_literal_global.217.53563
- ___block_literal_global.227.55271
- ___block_literal_global.25.55241
- ___block_literal_global.27.49780
- ___block_literal_global.38.54866
- ___block_literal_global.39.55278
- ___block_literal_global.39.56504
- ___block_literal_global.41.54858
- ___block_literal_global.48
- ___block_literal_global.48417
- ___block_literal_global.49047
- ___block_literal_global.49136
- ___block_literal_global.49785
- ___block_literal_global.49917
- ___block_literal_global.50
- ___block_literal_global.50691
- ___block_literal_global.51129
- ___block_literal_global.51862
- ___block_literal_global.52469
- ___block_literal_global.53226
- ___block_literal_global.53586
- ___block_literal_global.54909
- ___block_literal_global.55276
- ___block_literal_global.56.51856
- ___block_literal_global.56.53579
- ___block_literal_global.56536
- ___block_literal_global.56986
- ___block_literal_global.57407
- ___block_literal_global.57532
- ___block_literal_global.58753
- ___block_literal_global.58818
- ___block_literal_global.6.54906
- ___block_literal_global.68.53197
- ___block_literal_global.72.56443
- ___block_literal_global.75.56445
- ___block_literal_global.93.51805
- ___block_literal_global.96.51793
- ___getCARSessionStatusClass_block_invoke.49770
- _audit_stringCarKit.49678
- _getCARSessionStatusClass.softClass.49769
- _initWithPlayerPath:.onceToken.56513
- _objc_msgSend$_contentItemForIdentifier:
- _objc_msgSend$_contentItemForIdentifier:alreadyOnDataSourceQueue:
- _objc_msgSend$_contentItemIDsInRange:itemsRange:
- _objc_msgSend$_createPlaybackQueueForRequest:
- _objc_msgSend$_invalidatePlaybackQueueImmediatelyWithCompletion:
- _objc_msgSend$_onDataSourceQueue_artworkCatalogForContentItem:
- _objc_msgSend$_onDataSourceQueue_getContentItemIDsInRange:completion:
- _objc_msgSend$_onQueue_clearPlaybackQueueDataSourceCallbacks
- _objc_msgSend$_onQueue_pushContentItemsUpdate
- _objc_msgSend$_onQueue_registerLyricsDelegateCallbacks:
- _objc_msgSend$_onQueue_registerPlaybackQueueDataSourceCallbacks:
CStrings:
+ "<%@:%p routingContextUID=%@, style=%@, presentingAppBundleID=%@, sourcRect=%@, preferredWidth=%f, userInterfaceStyle=%@ surface=%@>"
+ "@\"MSVBloomFilter\""
+ "ActivityBanner"
+ "Ambient"
+ "App"
+ "BluePill"
+ "ControlCenter"
+ "CoverSheet"
+ "DynamicIsland"
+ "HomeTile"
+ "ProximityCard"
+ "RouteRecommendation"
+ "TB,N,GisInSmartTransition,V_inSmartTransition"
+ "Tq,N,V_surface"
+ "[InfoCenter] <%@: %p (%@)> Content item mutated | dropped [not in bloom filter] contentItemID=%{public}@"
+ "[InfoCenter] <%@: %p (%@)> Content item mutated | merged [already enqueued for update] contentItemID=%{public}@"
+ "[InfoCenter] <%@: %p (%@)> Content item mutated | pushed [metadata] contentItemID=%{public}@"
+ "[InfoCenter] <%@: %p (%@)> Content item mutated | pushed [request] contentItemID=%{public}@ request=%{public}@"
+ "[InfoCenter] <%@: %p (%@)> Content item mutated | queued [new] contentItemID=%{public}@"
+ "[InfoCenter] <%@: %p (%@)> invalidatePlaybackQueueBoundaryWithExpectedQueueSize:%ld [] adaptiveCapacity=%ld"
+ "[InfoCenter] <%@: %p (%@)> invalidatePlaybackQueueBoundaryWithExpectedQueueSize:%ld [] didChange=%{BOOL}u"
+ "_contentItemBloomFilter"
+ "_inSmartTransition"
+ "_invalidatePlaybackQueueBoundaryWithExpectedQueueSize:"
+ "_surface"
+ "becomeActivePlayer: %{public}@ error=%{public}@"
+ "bloomFilter"
+ "defaultExpectedQueueSize"
+ "inSmartTransition"
+ "initWithCapacity:falsePositiveTolerance:"
+ "isInSmartTransition"
+ "setInSmartTransition:"
+ "setSurface:"
+ "surface"
+ "\xf0r\xd1"
- "<%@:%p routingContextUID=%@, style=%@, presentingAppBundleID=%@, sourcRect=%@, preferredWidth=%f, userInterfaceStyle=%@>"
- "@40@0:8{?=qq}16^{?=qq}32"
- "[InfoCenter] <%@: %p (%@)> Content item mutated [already enqueued for update]: %{public}@"
- "[InfoCenter] <%@: %p (%@)> Content item mutated: %{public}@"
- "[InfoCenter] <%@: %p (%@)> sending content item changed: %{public}@"
- "^v24@0:8^v16"
- "_contentItemForIdentifier:"
- "_contentItemForIdentifier:alreadyOnDataSourceQueue:"
- "_createPlaybackQueueForRequest:"
- "_onDataSourceQueue_artworkCatalogForContentItem:"
- "_onDataSourceQueue_getContentItemIDsInRange:completion:"
- "_onQueue_clearPlaybackQueueDataSourceCallbacks"
- "_onQueue_pushContentItemsUpdate"
- "_onQueue_registerLyricsDelegateCallbacks:"
- "_onQueue_registerPlaybackQueueDataSourceCallbacks:"
- "becomeActivePlayer: %{public}@ failed %{public}@"
- "v40@0:8{_MSVSignedRange=qq}16@?32"
- "\xf0b\xd1"

```
