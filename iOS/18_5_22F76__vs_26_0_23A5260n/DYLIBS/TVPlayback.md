## TVPlayback

> `/System/Library/PrivateFrameworks/TVPlayback.framework/TVPlayback`

```diff

-563.50.5.0.0
-  __TEXT.__text: 0x66128
-  __TEXT.__auth_stubs: 0x810
-  __TEXT.__objc_methlist: 0x5e28
+590.0.0.0.0
+  __TEXT.__text: 0x669cc
+  __TEXT.__auth_stubs: 0x820
+  __TEXT.__objc_methlist: 0x5e30
   __TEXT.__const: 0x260
-  __TEXT.__cstring: 0x6705
-  __TEXT.__oslogstring: 0x625c
-  __TEXT.__gcc_except_tab: 0x262c
-  __TEXT.__unwind_info: 0x1680
-  __TEXT.__objc_classname: 0x837
-  __TEXT.__objc_methname: 0x12dd2
-  __TEXT.__objc_methtype: 0x244a
+  __TEXT.__cstring: 0x6784
+  __TEXT.__oslogstring: 0x63eb
+  __TEXT.__gcc_except_tab: 0x26dc
+  __TEXT.__unwind_info: 0x16a8
+  __TEXT.__objc_classname: 0x843
+  __TEXT.__objc_methname: 0x12d44
+  __TEXT.__objc_methtype: 0x2507
   __TEXT.__objc_stubs: 0xb3a0
-  __DATA_CONST.__got: 0x880
-  __DATA_CONST.__const: 0x2440
-  __DATA_CONST.__objc_classlist: 0x1f0
+  __DATA_CONST.__got: 0x898
+  __DATA_CONST.__const: 0x2438
+  __DATA_CONST.__objc_classlist: 0x1f8
   __DATA_CONST.__objc_catlist: 0x80
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x170
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__auth_got: 0x418
+  __AUTH_CONST.__auth_got: 0x420
   __AUTH_CONST.__const: 0x640
-  __AUTH_CONST.__cfstring: 0x6900
-  __AUTH_CONST.__objc_const: 0x9860
+  __AUTH_CONST.__cfstring: 0x6980
+  __AUTH_CONST.__objc_const: 0x98a0
   __AUTH_CONST.__objc_intobj: 0x480
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH.__objc_data: 0x8c0
-  __DATA.__objc_ivar: 0x7ac
+  __DATA.__objc_ivar: 0x7a4
   __DATA.__data: 0xac0
   __DATA.__bss: 0xa8
-  __DATA_DIRTY.__objc_data: 0xaa0
+  __DATA_DIRTY.__objc_data: 0xaf0
   __DATA_DIRTY.__bss: 0x1f8
   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices
   - /System/Library/PrivateFrameworks/RTCReporting.framework/RTCReporting
   - /System/Library/PrivateFrameworks/StoreServices.framework/StoreServices
+  - /System/Library/PrivateFrameworks/TVAppServices.framework/TVAppServices
   - /System/Library/PrivateFrameworks/TVMLKit.framework/TVMLKit
   - /System/Library/PrivateFrameworks/iTunesStore.framework/iTunesStore
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F3533AEE-59BB-3DC3-A05A-64DAE2CA1B4A
-  Functions: 2229
-  Symbols:   8225
-  CStrings:  5463
+  UUID: 27DD90B1-721A-3FA8-9176-57313DB22939
+  Functions: 2231
+  Symbols:   8229
+  CStrings:  5474
 
Symbols:
+ +[TVPHeicUtil isHeicFormatAllowed]
+ +[TVPHeicUtil isTVApp]
+ -[TVPDownload _variantQualifiersForCurrentSettingsUsingMultichannelAudio:]
+ GCC_except_table45
+ GCC_except_table485
+ GCC_except_table487
+ GCC_except_table496
+ GCC_except_table502
+ GCC_except_table510
+ GCC_except_table513
+ GCC_except_table525
+ GCC_except_table527
+ GCC_except_table534
+ GCC_except_table692
+ _OBJC_CLASS_$_AVPlayer
+ _OBJC_CLASS_$_TVAppAccountStoreObjC
+ _OBJC_CLASS_$_TVPHeicUtil
+ _OBJC_METACLASS_$_TVPHeicUtil
+ _TVPMediaItemMetadataPlaybackReportingEventCollection
+ _UIImageHEICRepresentation
+ _UTTypeHEIC
+ _VUIUtilitiesTvAppBundleIdIos
+ _VUIUtilitiesTvAppBundleIdOsx
+ _VUIUtilitiesTvAppBundleIdTvos
+ __OBJC_$_CLASS_METHODS_TVPHeicUtil
+ __OBJC_CLASS_RO_$_TVPHeicUtil
+ __OBJC_METACLASS_RO_$_TVPHeicUtil
+ ___23-[TVPPlayer invalidate]_block_invoke.397
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.751
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.754
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.770
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.770.cold.1
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.776
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.781
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.785
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.795
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.796
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.798
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.799
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.800
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.802
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.821
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.831
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.844
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.849
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.851
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.861
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.863
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.865
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.866
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.870
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.872
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.883
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.884
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.886
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.895
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.896
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.897
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.899
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.901
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.914
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.915
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.916
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.920
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.923
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.924
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.933
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.948
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.957
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.967
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.971
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_10.881
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_10.942
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_11.943
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_12.944
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_13.945
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_14.946
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_15.947
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.745
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.755
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.773
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.778
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.804
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.832
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.838
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.843
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.845
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.850
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.852
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.862
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.864
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.867
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.871
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.873
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.885
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.898
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.903
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.917
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.921
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.925
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.934
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.949
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.972
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.747
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.756
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.774
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.780
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.806
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.833
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.839
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.846
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.857
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.868
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.874
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.918
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.922
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.926
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.935
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.950
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.975
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.749
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.775
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.813
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.835
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.847
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.858
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.869
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.875
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.919
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.927
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.936
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.951
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.976
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_5.814
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_5.848
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_5.859
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_5.876
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_5.928
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_5.937
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_5.952
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_5.977
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_6.815
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_6.860
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_6.877
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_6.929
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_6.938
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_6.953
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_7.817
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_7.878
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_7.930
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_7.939
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_7.956
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_7.956.cold.1
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_7.956.cold.2
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_7.956.cold.3
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_7.956.cold.4
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_7.956.cold.5
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_8.818
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_8.879
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_8.931
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_8.940
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_9.819
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_9.880
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_9.932
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_9.941
+ ___43-[TVPPlayer _currentPlayerItemDidChangeTo:]_block_invoke.586
+ ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke.115
+ ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke.123
+ ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke.123.cold.1
+ ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke.123.cold.2
+ ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke.123.cold.3
+ ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke.129
+ ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke.135
+ ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke.192
+ ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke.222
+ ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke.223
+ ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke.223.cold.1
+ ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke.232
+ ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke.237
+ ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke_2.127
+ ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke_2.127.cold.1
+ ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke_2.130
+ ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke_2.136
+ ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke_2.139
+ ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke_2.193
+ ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke_2.195.cold.1
+ ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke_2.195.cold.2
+ ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke_2.227
+ ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke_2.233
+ ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke_2.238
+ ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke_3.228
+ ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke_3.234
+ ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke_4.229
+ ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke_4.235
+ ___51-[TVPPlayer _integratedTimelineSnapshotsOutOfSync:]_block_invoke.593
+ ___56-[TVPPlayer changeToMediaAtIndex:reason:ignoreDelegate:]_block_invoke.423
+ ___56-[TVPPlayer changeToMediaAtIndex:reason:ignoreDelegate:]_block_invoke.424
+ ___58-[TVPPlayer changeMediaInDirection:reason:ignoreDelegate:]_block_invoke.414
+ ___58-[TVPPlayer changeMediaInDirection:reason:ignoreDelegate:]_block_invoke.421
+ ___60-[TVPPlayer observeValueForKeyPath:ofObject:change:context:]_block_invoke.408
+ ___65-[TVPDownload URLSession:assetDownloadTask:willDownloadVariants:]_block_invoke
+ ___block_literal_global.231
+ ___block_literal_global.365
+ ___block_literal_global.367
+ ___block_literal_global.429
+ ___block_literal_global.432
+ ___block_literal_global.596
+ ___block_literal_global.614
+ ___block_literal_global.616
+ ___block_literal_global.856
+ ___block_literal_global.955
+ _objc_msgSend$_variantQualifiersForCurrentSettingsUsingMultichannelAudio:
+ _objc_msgSend$accountWithDSID:
+ _objc_msgSend$isHeicFormatAllowed
+ _objc_msgSend$isTVApp
+ _objc_msgSend$predicateForChannelCount:operatorType:
+ _objc_msgSend$setSupportsSharedNetworkCoordination:
- -[TVPDownload _variantQualifiersForCurrentSettingsAndAudioOption:useMultichannelAudio:]
- -[TVPDownload allowMultichannelAudio]
- -[TVPDownload limitMultichannelAudioToSingleLanguage]
- -[TVPDownload setAllowMultichannelAudio:]
- -[TVPDownload setLimitMultichannelAudioToSingleLanguage:]
- GCC_except_table43
- GCC_except_table481
- GCC_except_table488
- GCC_except_table498
- GCC_except_table506
- GCC_except_table509
- GCC_except_table521
- GCC_except_table523
- GCC_except_table526
- GCC_except_table688
- _OBJC_CLASS_$_ACAccountStore
- _OBJC_IVAR_$_TVPDownload._allowMultichannelAudio
- _OBJC_IVAR_$_TVPDownload._limitMultichannelAudioToSingleLanguage
- ___23-[TVPPlayer invalidate]_block_invoke.393
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.735
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.746
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.760
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.762
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.762.cold.1
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.769
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.773
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.774
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.778
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.779
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.783
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.784
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.788
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.813
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.823
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.828
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.833
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.843
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.845
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.855
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.857
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.858
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.862
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.864
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.875
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.876
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.878
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.887
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.888
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.889
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.891
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.903
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.904
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.908
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.911
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.921
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.936
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.945
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.955
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.959
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_10.873
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_10.930
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_11.931
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_12.932
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_13.933
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_14.934
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_15.935
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.737
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.747
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.765
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.770
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.796
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.824
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.830
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.835
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.837
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.842
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.844
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.846
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.856
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.859
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.863
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.865
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.877
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.890
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.894
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.901
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.905
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.909
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.922
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.937
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.960
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.739
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.748
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.766
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.772
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.798
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.825
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.831
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.838
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.849
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.860
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.866
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.910
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.914
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.923
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.938
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.963
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.741
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.767
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.805
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.827
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.839
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.850
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.861
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.867
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.907
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.915
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.924
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.939
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.964
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_5.806
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_5.840
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_5.851
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_5.868
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_5.916
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_5.925
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_5.940
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_5.965
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_6.807
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_6.852
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_6.869
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_6.917
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_6.926
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_6.941
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_7.809
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_7.870
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_7.918
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_7.927
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_7.944
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_7.944.cold.1
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_7.944.cold.2
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_7.944.cold.3
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_7.944.cold.4
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_7.944.cold.5
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_8.810
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_8.871
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_8.919
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_8.928
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_9.811
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_9.872
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_9.920
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_9.929
- ___43-[TVPPlayer _currentPlayerItemDidChangeTo:]_block_invoke.582
- ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke.117
- ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke.125
- ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke.125.cold.1
- ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke.125.cold.2
- ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke.125.cold.3
- ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke.131
- ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke.139
- ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke.198
- ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke.220
- ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke.227
- ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke.227.cold.1
- ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke.230
- ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke.240
- ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke.241
- ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke_2.129
- ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke_2.129.cold.1
- ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke_2.132
- ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke_2.138
- ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke_2.141
- ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke_2.197
- ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke_2.197.cold.1
- ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke_2.197.cold.2
- ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke_2.231
- ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke_2.237
- ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke_2.242
- ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke_3.232
- ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke_3.238
- ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke_4.233
- ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke_4.239
- ___51-[TVPPlayer _integratedTimelineSnapshotsOutOfSync:]_block_invoke.589
- ___56-[TVPPlayer changeToMediaAtIndex:reason:ignoreDelegate:]_block_invoke.419
- ___56-[TVPPlayer changeToMediaAtIndex:reason:ignoreDelegate:]_block_invoke.420
- ___58-[TVPPlayer changeMediaInDirection:reason:ignoreDelegate:]_block_invoke.410
- ___58-[TVPPlayer changeMediaInDirection:reason:ignoreDelegate:]_block_invoke.417
- ___60-[TVPPlayer observeValueForKeyPath:ofObject:change:context:]_block_invoke.404
- ___block_descriptor_64_e8_32s40s48s56s_e33_v32?0"AVMediaSelection"8Q16^B24ls32l8s40l8s48l8s56l8
- ___block_literal_global.235
- ___block_literal_global.361
- ___block_literal_global.363
- ___block_literal_global.425
- ___block_literal_global.428
- ___block_literal_global.592
- ___block_literal_global.608
- ___block_literal_global.610
- ___block_literal_global.848
- ___block_literal_global.943
- _objc_msgSend$_variantQualifiersForCurrentSettingsAndAudioOption:useMultichannelAudio:
- _objc_msgSend$allowMultichannelAudio
- _objc_msgSend$ams_iTunesAccountWithDSID:
- _objc_msgSend$ams_sharedAccountStore
- _objc_msgSend$limitMultichannelAudioToSingleLanguage
- _objc_msgSend$predicateForChannelCount:mediaSelectionOption:operatorType:
CStrings:
+ "Active player %@ has timeControlStatus of AVPlayerTimeControlStatusPlaying, but active player item %@ status isn't AVPlayerItemStatusReadyToPlay.  Waiting until it becomes ready to play."
+ "TVPHeicUtil"
+ "URLSession:assetDownloadTask:didReceiveMetricEvent:"
+ "Waiting for initial AVPlayerItem status to become ready to play"
+ "Waiting for non-initial AVPlayerItem status to become ready to play"
+ "_variantQualifiersForCurrentSettingsUsingMultichannelAudio:"
+ "accountWithDSID:"
+ "com.apple.TV"
+ "com.apple.TVWatchList"
+ "com.apple.tv"
+ "com.apple.tv AVAssetVariant logging queue"
+ "heic"
+ "integratedTimeline:didRequestSeekToTime:seekID:toleranceBefore:toleranceAfter:"
+ "isHeicFormatAllowed"
+ "isTVApp"
+ "menkaure"
+ "predicateForChannelCount:operatorType:"
+ "setSupportsSharedNetworkCoordination:"
+ "timeControlStatus is AVPlayerTimeControlStatusPlaying for %@ and player item status is AVPlayerItemStatusReadyToPlay for active item %@, but we're still waiting.  Posting player item status change to ReadyToPlay"
+ "v100@0:8@\"AVPlayerItemIntegratedTimeline\"16{?=qiIq}24i48{?=qiIq}52{?=qiIq}76"
+ "v100@0:8@16{?=qiIq}24i48{?=qiIq}52{?=qiIq}76"
+ "v40@0:8@\"NSURLSession\"16@\"AVAssetDownloadTask\"24@\"AVMetricEvent\"32"
- "TB,N,V_allowMultichannelAudio"
- "TB,N,V_limitMultichannelAudioToSingleLanguage"
- "Waiting for AVPlayerItem status to become ready to play"
- "_allowMultichannelAudio"
- "_limitMultichannelAudioToSingleLanguage"
- "_variantQualifiersForCurrentSettingsAndAudioOption:useMultichannelAudio:"
- "allowMultichannelAudio"
- "ams_iTunesAccountWithDSID:"
- "ams_sharedAccountStore"
- "averageBitRate > 0"
- "limitMultichannelAudioToSingleLanguage"
- "predicateForChannelCount:mediaSelectionOption:operatorType:"
- "setAllowMultichannelAudio:"
- "setLimitMultichannelAudioToSingleLanguage:"
- "v32@?0@\"AVMediaSelection\"8Q16^B24"

```
