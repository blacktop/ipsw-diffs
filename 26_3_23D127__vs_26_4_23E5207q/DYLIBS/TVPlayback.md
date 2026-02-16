## TVPlayback

> `/System/Library/PrivateFrameworks/TVPlayback.framework/TVPlayback`

```diff

-598.30.2.0.0
-  __TEXT.__text: 0x684bc
-  __TEXT.__auth_stubs: 0x840
-  __TEXT.__objc_methlist: 0x5f58
-  __TEXT.__const: 0x270
-  __TEXT.__cstring: 0x68a2
-  __TEXT.__oslogstring: 0x67c5
-  __TEXT.__gcc_except_tab: 0x2734
-  __TEXT.__unwind_info: 0x16f0
-  __TEXT.__objc_classname: 0x856
-  __TEXT.__objc_methname: 0x130f6
-  __TEXT.__objc_methtype: 0x2512
-  __TEXT.__objc_stubs: 0xb5c0
-  __DATA_CONST.__got: 0x8a8
-  __DATA_CONST.__const: 0x2498
-  __DATA_CONST.__objc_classlist: 0x200
+598.40.15.0.0
+  __TEXT.__text: 0x6d75c
+  __TEXT.__auth_stubs: 0x7f0
+  __TEXT.__objc_methlist: 0x5ef0
+  __TEXT.__const: 0x260
+  __TEXT.__cstring: 0x6877
+  __TEXT.__oslogstring: 0x69e1
+  __TEXT.__gcc_except_tab: 0x21f4
+  __TEXT.__unwind_info: 0x1be8
+  __TEXT.__objc_classname: 0x84b
+  __TEXT.__objc_methname: 0x1319a
+  __TEXT.__objc_methtype: 0x2501
+  __TEXT.__objc_stubs: 0xb640
+  __DATA_CONST.__got: 0x8b0
+  __DATA_CONST.__const: 0x2478
+  __DATA_CONST.__objc_classlist: 0x1f8
   __DATA_CONST.__objc_catlist: 0x80
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3d40
+  __DATA_CONST.__objc_selrefs: 0x3d58
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x178
+  __DATA_CONST.__objc_superrefs: 0x170
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__auth_got: 0x430
+  __AUTH_CONST.__auth_got: 0x408
   __AUTH_CONST.__const: 0x680
-  __AUTH_CONST.__cfstring: 0x6a40
-  __AUTH_CONST.__objc_const: 0x9a28
+  __AUTH_CONST.__cfstring: 0x6ae0
+  __AUTH_CONST.__objc_const: 0x9958
   __AUTH_CONST.__objc_intobj: 0x480
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH.__objc_data: 0x910
-  __DATA.__objc_ivar: 0x7b4
+  __AUTH.__objc_data: 0x8c0
+  __DATA.__objc_ivar: 0x7b0
   __DATA.__data: 0xac8
-  __DATA.__bss: 0xb0
+  __DATA.__bss: 0xa8
   __DATA_DIRTY.__objc_data: 0xaf0
-  __DATA_DIRTY.__bss: 0x220
+  __DATA_DIRTY.__bss: 0x228
   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: DDEA0E74-E00C-3D02-A500-468599F21C3F
-  Functions: 2259
+  UUID: 08345932-6EE7-30E8-918C-A2597B32002A
+  Functions: 2256
   Symbols:   8333
-  CStrings:  5536
+  CStrings:  5551
 
Symbols:
+ +[TVPMediaItemLoader loaderForPlayerItem:]
+ -[TVPBoundaryTimeObserverInfo description]
+ -[TVPBoundaryTimeObserverInfo isForPrimaryPlayer]
+ -[TVPBoundaryTimeObserverInfo segmentRelativeTimes]
+ -[TVPBoundaryTimeObserverInfo setIsForPrimaryPlayer:]
+ -[TVPBoundaryTimeObserverInfo setSegmentRelativeTimes:]
+ -[TVPMediaItemLoader posterProxy]
+ -[TVPMediaItemLoader setPosterProxy:]
+ -[TVPMediaItemLoader setWeakPlayerItemsHashTable:]
+ -[TVPMediaItemLoader weakPlayerItemsHashTable]
+ -[TVPPlayer _addCustomTimelineBoundaryTimeObserversWithSnapshot:]
+ -[TVPPlayer _removeCustomTimelineBoundaryTimeObservers]
+ -[TVPPlayer _updateCustomTimelineBoundaryObserversDueToCurrentSegmentChange:]
+ -[TVPPlayer _useCustomTimelineBoundaryTimeObserver]
+ -[TVPPlayer boundaryTimeObserverInfoArray]
+ -[TVPPlayer currentPlayerItemPreviousStatus]
+ -[TVPPlayer setBoundaryTimeObserverInfoArray:]
+ -[TVPPlayer setCurrentPlayerItemPreviousStatus:]
+ GCC_except_table126
+ GCC_except_table132
+ GCC_except_table230
+ GCC_except_table233
+ GCC_except_table237
+ GCC_except_table240
+ GCC_except_table243
+ GCC_except_table26
+ GCC_except_table35
+ GCC_except_table377
+ GCC_except_table396
+ GCC_except_table403
+ GCC_except_table404
+ GCC_except_table407
+ GCC_except_table410
+ GCC_except_table413
+ GCC_except_table416
+ GCC_except_table421
+ GCC_except_table424
+ GCC_except_table428
+ GCC_except_table432
+ GCC_except_table437
+ GCC_except_table442
+ GCC_except_table47
+ GCC_except_table471
+ GCC_except_table476
+ GCC_except_table482
+ GCC_except_table489
+ GCC_except_table498
+ GCC_except_table502
+ GCC_except_table508
+ GCC_except_table516
+ GCC_except_table519
+ GCC_except_table531
+ GCC_except_table536
+ GCC_except_table540
+ GCC_except_table56
+ GCC_except_table59
+ GCC_except_table703
+ GCC_except_table81
+ GCC_except_table88
+ GCC_except_table93
+ GCC_except_table95
+ _AVPlayerIntegratedTimelineSnapshotsOutOfSyncReasonCurrentSegmentChanged
+ _OBJC_IVAR_$_TVPBoundaryTimeObserverInfo._isForPrimaryPlayer
+ _OBJC_IVAR_$_TVPBoundaryTimeObserverInfo._segmentRelativeTimes
+ _OBJC_IVAR_$_TVPMediaItemLoader._posterProxy
+ _OBJC_IVAR_$_TVPMediaItemLoader._weakPlayerItemsHashTable
+ _OBJC_IVAR_$_TVPPlayer._boundaryTimeObserverInfoArray
+ _OBJC_IVAR_$_TVPPlayer._currentPlayerItemPreviousStatus
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ ___23-[TVPPlayer invalidate]_block_invoke.422
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.1000
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.1004
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.785
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.799
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.801.cold.1
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.807
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.812
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.813
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.816
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.817
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.818
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.821
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.822
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.823
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.825
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.826
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.829
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.830
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.831
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.833
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.852
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.862
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.874
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.877
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.882
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.884
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.886
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.894
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.896
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.898
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.899
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.916
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.917
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.919
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.928
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.932
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.933
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.934
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.935
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.945
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.947
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.948
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.949
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.953
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.956
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.957
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.966
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.981
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.990
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_10.914
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_10.975
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_11.976
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_12.977
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_13.978
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_14.979
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_15.980
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.1005
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.776
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.786
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.804
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.809
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.835
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.863
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.869
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.876
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.878
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.883
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.885
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.887
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.895
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.897
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.900
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.906
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.918
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.936
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.946
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.950
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.954
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.958
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.967
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.982
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.1008
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.778
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.787
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.805
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.811
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.837
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.864
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.870
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.879
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.890
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.901
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.907
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.939
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.951
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.955
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.959
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.968
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.983
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.1009
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.780
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.806
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.844
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.866
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.880
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.891
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.902
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.908
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.952
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.960
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.969
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.984
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_5.1010
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_5.845
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_5.881
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_5.892
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_5.909
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_5.961
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_5.970
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_5.985
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_6.846
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_6.893
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_6.910
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_6.962
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_6.971
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_6.986
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_7.848
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_7.911
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_7.963
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_7.972
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_7.989
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_7.989.cold.1
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_7.989.cold.2
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_7.989.cold.3
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_7.989.cold.4
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_7.989.cold.5
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_8.849
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_8.912
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_8.964
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_8.973
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_9.850
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_9.913
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_9.965
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_9.974
+ ___43-[TVPPlayer _currentPlayerItemDidChangeTo:]_block_invoke.620
+ ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke.216
+ ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke.217
+ ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke.217.cold.1
+ ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke.220
+ ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke.230
+ ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke.231
+ ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke_2.221
+ ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke_2.232
+ ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke_3.222
+ ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke_4.223
+ ___51-[TVPPlayer _integratedTimelineSnapshotsOutOfSync:]_block_invoke.627
+ ___51-[TVPPlayer _integratedTimelineSnapshotsOutOfSync:]_block_invoke_2
+ ___56-[TVPPlayer changeToMediaAtIndex:reason:ignoreDelegate:]_block_invoke.448
+ ___56-[TVPPlayer changeToMediaAtIndex:reason:ignoreDelegate:]_block_invoke.449
+ ___58-[TVPPlayer changeMediaInDirection:reason:ignoreDelegate:]_block_invoke.439
+ ___58-[TVPPlayer changeMediaInDirection:reason:ignoreDelegate:]_block_invoke.446
+ ___60-[TVPPlayer observeValueForKeyPath:ofObject:change:context:]_block_invoke.433
+ ___65-[TVPPlayer _addCustomTimelineBoundaryTimeObserversWithSnapshot:]_block_invoke
+ ___65-[TVPPlayer _addCustomTimelineBoundaryTimeObserversWithSnapshot:]_block_invoke_2
+ ___77-[TVPPlayer _updateCustomTimelineBoundaryObserversDueToCurrentSegmentChange:]_block_invoke
+ ___block_descriptor_56_e8_32s40w_e5_v8?0ls32l8w40l8
+ ___block_literal_global.255
+ ___block_literal_global.391
+ ___block_literal_global.393
+ ___block_literal_global.454
+ ___block_literal_global.457
+ ___block_literal_global.630
+ ___block_literal_global.646
+ ___block_literal_global.648
+ ___block_literal_global.650
+ ___block_literal_global.889
+ ___block_literal_global.988
+ _objc_msgSend$_addCustomTimelineBoundaryTimeObserversWithSnapshot:
+ _objc_msgSend$_removeCustomTimelineBoundaryTimeObservers
+ _objc_msgSend$_updateCustomTimelineBoundaryObserversDueToCurrentSegmentChange:
+ _objc_msgSend$_useCustomTimelineBoundaryTimeObserver
+ _objc_msgSend$appendString:
+ _objc_msgSend$boundaryTimeObserverInfoArray
+ _objc_msgSend$currentPlayerItemPreviousStatus
+ _objc_msgSend$initWithString:
+ _objc_msgSend$isForPrimaryPlayer
+ _objc_msgSend$loaderForPlayerItem:
+ _objc_msgSend$posterProxy
+ _objc_msgSend$segmentRelativeTimes
+ _objc_msgSend$setCurrentPlayerItemPreviousStatus:
+ _objc_msgSend$setIsForPrimaryPlayer:
+ _objc_msgSend$setSegmentRelativeTimes:
+ _objc_msgSend$timeMapping
+ _objc_msgSend$weakPlayerItemsHashTable
- -[TVPPlayer _activePlayerItem]
- -[TVPPlayer _activePlayerTimeControlStatus]
- -[TVPPlayer _addBoundaryTimeObserversToAVQueuePlayer:]
- -[TVPPlayer _addPeriodicTimeObserverToAVQueuePlayer:]
- -[TVPPlayer _integratedTimelineEnabled]
- -[TVPPlayer _removeBoundaryTimeObserversFromAVQueuePlayer:]
- -[TVPPlayer _removePeriodicTimeObserverFromAVQueuePlayer:]
- -[TVPPlayerItem .cxx_destruct]
- -[TVPPlayerItem audioSelectionIsAutomatic]
- -[TVPPlayerItem dealloc]
- -[TVPPlayerItem initWithAsset:]
- -[TVPPlayerItem mediaItemLoader]
- -[TVPPlayerItem muted]
- -[TVPPlayerItem posterProxy]
- -[TVPPlayerItem previousStatus]
- -[TVPPlayerItem savedManualAudioSelection]
- -[TVPPlayerItem scrubImageLoader]
- -[TVPPlayerItem selectMediaOption:inMediaSelectionGroup:]
- -[TVPPlayerItem selectMediaOptionAutomaticallyInMediaSelectionGroup:]
- -[TVPPlayerItem setAudioSelectionIsAutomatic:]
- -[TVPPlayerItem setMediaItemLoader:]
- -[TVPPlayerItem setMuted:]
- -[TVPPlayerItem setPosterProxy:]
- -[TVPPlayerItem setPreviousStatus:]
- -[TVPPlayerItem setSavedManualAudioSelection:]
- -[TVPPlayerItem setScrubImageLoader:]
- GCC_except_table121
- GCC_except_table127
- GCC_except_table13
- GCC_except_table225
- GCC_except_table228
- GCC_except_table229
- GCC_except_table235
- GCC_except_table241
- GCC_except_table242
- GCC_except_table244
- GCC_except_table25
- GCC_except_table33
- GCC_except_table37
- GCC_except_table379
- GCC_except_table398
- GCC_except_table405
- GCC_except_table408
- GCC_except_table411
- GCC_except_table414
- GCC_except_table417
- GCC_except_table418
- GCC_except_table423
- GCC_except_table426
- GCC_except_table430
- GCC_except_table434
- GCC_except_table439
- GCC_except_table448
- GCC_except_table475
- GCC_except_table478
- GCC_except_table484
- GCC_except_table49
- GCC_except_table495
- GCC_except_table500
- GCC_except_table504
- GCC_except_table510
- GCC_except_table518
- GCC_except_table521
- GCC_except_table535
- GCC_except_table538
- GCC_except_table542
- GCC_except_table55
- GCC_except_table701
- GCC_except_table80
- GCC_except_table87
- GCC_except_table92
- GCC_except_table94
- _OBJC_CLASS_$_TVPPlayerItem
- _OBJC_IVAR_$_TVPPlayerItem._audioSelectionIsAutomatic
- _OBJC_IVAR_$_TVPPlayerItem._mediaItemLoader
- _OBJC_IVAR_$_TVPPlayerItem._muted
- _OBJC_IVAR_$_TVPPlayerItem._posterProxy
- _OBJC_IVAR_$_TVPPlayerItem._previousStatus
- _OBJC_IVAR_$_TVPPlayerItem._savedManualAudioSelection
- _OBJC_IVAR_$_TVPPlayerItem._scrubImageLoader
- _OBJC_METACLASS_$_AVPlayerItem
- _OBJC_METACLASS_$_TVPPlayerItem
- __OBJC_$_INSTANCE_METHODS_TVPPlayerItem
- __OBJC_$_INSTANCE_VARIABLES_TVPPlayerItem
- __OBJC_$_PROP_LIST_TVPPlayerItem
- __OBJC_CLASS_RO_$_TVPPlayerItem
- __OBJC_METACLASS_RO_$_TVPPlayerItem
- ___23-[TVPPlayer invalidate]_block_invoke.396
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.749
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.757
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.760
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.776
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.776.cold.1
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.783
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.787
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.788
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.791
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.792
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.793
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.796
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.797
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.798
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.800
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.802
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.804
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.805
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.806
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.837
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.842
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.847
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.850
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.855
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.857
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.859
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.869
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.871
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.872
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.876
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.878
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.889
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.890
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.892
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.901
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.902
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.906
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.907
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.908
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.918
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.920
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.921
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.922
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.926
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.939
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.954
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.963
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.973
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.977
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_10.887
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_10.948
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_11.949
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_12.950
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_13.951
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_14.952
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_15.953
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.751
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.761
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.779
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.784
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.810
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.838
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.844
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.849
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.851
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.856
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.858
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.860
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.868
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.870
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.873
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.877
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.879
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.891
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.909
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.919
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.923
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.927
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.940
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.955
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.978
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.753
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.762
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.780
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.786
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.812
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.839
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.845
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.852
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.863
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.874
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.880
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.912
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.924
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.928
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.932
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.941
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.956
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.981
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.755
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.781
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.819
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.841
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.853
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.864
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.875
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.881
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.925
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.933
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.942
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.957
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.982
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_5.820
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_5.854
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_5.865
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_5.882
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_5.934
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_5.943
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_5.958
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_5.983
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_6.821
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_6.866
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_6.883
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_6.935
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_6.944
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_6.959
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_7.823
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_7.884
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_7.936
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_7.945
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_7.962
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_7.962.cold.1
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_7.962.cold.2
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_7.962.cold.3
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_7.962.cold.4
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_7.962.cold.5
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_8.824
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_8.885
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_8.937
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_8.946
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_9.825
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_9.886
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_9.938
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_9.947
- ___43-[TVPPlayer _currentPlayerItemDidChangeTo:]_block_invoke.592
- ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke.222
- ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke.223
- ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke.223.cold.1
- ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke.232
- ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke.236
- ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke.237
- ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke_2.233
- ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke_2.238
- ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke_3.234
- ___44-[TVPDownload _registerStateMachineHandlers]_block_invoke_4.235
- ___51-[TVPPlayer _integratedTimelineSnapshotsOutOfSync:]_block_invoke.599
- ___53-[TVPPlayer _addHighFrequencyTimeObserverIfNecessary]_block_invoke_3
- ___53-[TVPPlayer _addPeriodicTimeObserverToAVQueuePlayer:]_block_invoke
- ___53-[TVPPlayer _addPeriodicTimeObserverToAVQueuePlayer:]_block_invoke_2
- ___54-[TVPPlayer _addBoundaryTimeObserversToAVQueuePlayer:]_block_invoke
- ___54-[TVPPlayer _addBoundaryTimeObserversToAVQueuePlayer:]_block_invoke_2
- ___54-[TVPPlayer _addBoundaryTimeObserversToAVQueuePlayer:]_block_invoke_3
- ___56-[TVPPlayer changeToMediaAtIndex:reason:ignoreDelegate:]_block_invoke.422
- ___56-[TVPPlayer changeToMediaAtIndex:reason:ignoreDelegate:]_block_invoke.423
- ___58-[TVPPlayer changeMediaInDirection:reason:ignoreDelegate:]_block_invoke.413
- ___58-[TVPPlayer changeMediaInDirection:reason:ignoreDelegate:]_block_invoke.420
- ___59-[TVPPlayer _removeBoundaryTimeObserversFromAVQueuePlayer:]_block_invoke
- ___60-[TVPPlayer observeValueForKeyPath:ofObject:change:context:]_block_invoke.407
- ___70-[TVPPlayer _notifyOfBoundaryCrossingBetweenPreviousTime:updatedTime:]_block_invoke
- ___block_descriptor_40_e8_32s_e52_v32?0"NSUUID"8"TVPBoundaryTimeObserverInfo"16^B24ls32l8
- ___block_descriptor_80_e52_v32?0"NSUUID"8"TVPBoundaryTimeObserverInfo"16^B24l
- ___block_literal_global.228
- ___block_literal_global.231
- ___block_literal_global.364
- ___block_literal_global.366
- ___block_literal_global.428
- ___block_literal_global.431
- ___block_literal_global.602
- ___block_literal_global.618
- ___block_literal_global.620
- ___block_literal_global.622
- ___block_literal_global.862
- ___block_literal_global.961
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$_activePlayerItem
- _objc_msgSend$_activePlayerTimeControlStatus
- _objc_msgSend$_addBoundaryTimeObserversToAVQueuePlayer:
- _objc_msgSend$_addPeriodicTimeObserverToAVQueuePlayer:
- _objc_msgSend$_integratedTimelineEnabled
- _objc_msgSend$_removeBoundaryTimeObserversFromAVQueuePlayer:
- _objc_msgSend$_removePeriodicTimeObserverFromAVQueuePlayer:
- _objc_msgSend$audioSelectionIsAutomatic
- _objc_msgSend$previousStatus
- _objc_msgSend$savedManualAudioSelection
- _objc_msgSend$setAudioSelectionIsAutomatic:
- _objc_msgSend$setPreviousStatus:
- _objc_msgSend$setSavedManualAudioSelection:
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x9
CStrings:
+ "%.3f"
+ ", "
+ "Adding boundary observer to %@ player %@ for the following times [segment relative/overall]: %@"
+ "Boundary observer fired for one of these requested times: %@"
+ "DisableCustomTimelineBoundaryObserver"
+ "Firing boundary observer manually after delay: %@"
+ "Firing boundary observer manually since one or more times are in last %.1f seconds: %@"
+ "Not firing boundary observer manually after delay because elapsed time %.3f isn't past the requested time %.3f"
+ "Removed %lu boundary observer times from %@ player by removing 1 time observer"
+ "Removed %lu boundary observer times from interstitial player by removing %lu time observer(s)"
+ "Removed %lu boundary observer times from primary player by removing %lu time observer(s)"
+ "Requested boundary time %.3f is in the next %.1f seconds. Will fire info manually in %.3f seconds: %@"
+ "T@\"AVPlayerItem\",&,N,V_currentPlayerItem"
+ "T@\"AVPlayerItem\",&,N,V_playerItemFromCacheManager"
+ "T@\"NSArray\",C,N,V_segmentRelativeTimes"
+ "T@\"NSHashTable\",&,N,V_weakPlayerItemsHashTable"
+ "T@\"NSMutableArray\",&,N,V_boundaryTimeObserverInfoArray"
+ "TB,N,V_isForPrimaryPlayer"
+ "Tq,N,V_currentPlayerItemPreviousStatus"
+ "Updating boundary time observers at time %f due to current segment change: %@"
+ "["
+ "[%.3f, %.3f]"
+ "]"
+ "_addCustomTimelineBoundaryTimeObserversWithSnapshot:"
+ "_boundaryTimeObserverInfoArray"
+ "_currentPlayerItemPreviousStatus"
+ "_isForPrimaryPlayer"
+ "_removeCustomTimelineBoundaryTimeObservers"
+ "_segmentRelativeTimes"
+ "_updateCustomTimelineBoundaryObserversDueToCurrentSegmentChange:"
+ "_useCustomTimelineBoundaryTimeObserver"
+ "_weakPlayerItemsHashTable"
+ "appendString:"
+ "boundaryTimeObserverInfoArray"
+ "currentPlayerItemPreviousStatus"
+ "initWithString:"
+ "isForPrimaryPlayer"
+ "loaderForPlayerItem:"
+ "primary"
+ "segmentRelativeTimes"
+ "setBoundaryTimeObserverInfoArray:"
+ "setCurrentPlayerItemPreviousStatus:"
+ "setIsForPrimaryPlayer:"
+ "setSegmentRelativeTimes:"
+ "setWeakPlayerItemsHashTable:"
+ "timeMapping"
+ "weakPlayerItemsHashTable"
- "@\"TVPPlayerItem\""
- "Current player item media selection did change"
- "Current player item time did jump"
- "DisableIntegratedTimeline"
- "DisableInterstitials"
- "In _setElapsedTimeOrDateOnCurrentPlayerItem, calling seekToDate on current player item"
- "In _setElapsedTimeOrDateOnCurrentPlayerItem, calling seekToTime on current player item"
- "Prior to enqueueing item, seeking player item to %@"
- "T@\"AVMediaSelectionOption\",&,N,V_savedManualAudioSelection"
- "T@\"TVPMediaItemLoader\",W,N,V_mediaItemLoader"
- "T@\"TVPPlayerItem\",&,N,V_currentPlayerItem"
- "T@\"TVPPlayerItem\",&,N,V_playerItemFromCacheManager"
- "T@,&,N,V_scrubImageLoader"
- "TB,N,V_audioSelectionIsAutomatic"
- "TVPPlayerItem"
- "Tq,N,V_previousStatus"
- "_activePlayerItem"
- "_activePlayerTimeControlStatus"
- "_addBoundaryTimeObserversToAVQueuePlayer:"
- "_addPeriodicTimeObserverToAVQueuePlayer:"
- "_audioSelectionIsAutomatic"
- "_integratedTimelineEnabled"
- "_previousStatus"
- "_removeBoundaryTimeObserversFromAVQueuePlayer:"
- "_removePeriodicTimeObserverFromAVQueuePlayer:"
- "_savedManualAudioSelection"
- "_scrubImageLoader"
- "audioSelectionIsAutomatic"
- "previousStatus"
- "savedManualAudioSelection"
- "scrubImageLoader"
- "setAudioSelectionIsAutomatic:"
- "setPreviousStatus:"
- "setSavedManualAudioSelection:"
- "setScrubImageLoader:"
- "v32@?0@\"NSUUID\"8@\"TVPBoundaryTimeObserverInfo\"16^B24"

```
