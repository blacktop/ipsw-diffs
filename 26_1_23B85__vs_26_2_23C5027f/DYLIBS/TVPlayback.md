## TVPlayback

> `/System/Library/PrivateFrameworks/TVPlayback.framework/TVPlayback`

```diff

-598.10.2.0.0
-  __TEXT.__text: 0x675c4
-  __TEXT.__auth_stubs: 0x820
-  __TEXT.__objc_methlist: 0x5e90
+598.20.2.0.0
+  __TEXT.__text: 0x68284
+  __TEXT.__auth_stubs: 0x840
+  __TEXT.__objc_methlist: 0x5f58
   __TEXT.__const: 0x270
-  __TEXT.__cstring: 0x6878
-  __TEXT.__oslogstring: 0x65b2
+  __TEXT.__cstring: 0x68a2
+  __TEXT.__oslogstring: 0x6716
   __TEXT.__gcc_except_tab: 0x2730
-  __TEXT.__unwind_info: 0x16b8
-  __TEXT.__objc_classname: 0x843
-  __TEXT.__objc_methname: 0x12e5d
-  __TEXT.__objc_methtype: 0x2507
-  __TEXT.__objc_stubs: 0xb420
-  __DATA_CONST.__got: 0x8a0
+  __TEXT.__unwind_info: 0x16f0
+  __TEXT.__objc_classname: 0x856
+  __TEXT.__objc_methname: 0x130f6
+  __TEXT.__objc_methtype: 0x2512
+  __TEXT.__objc_stubs: 0xb5c0
+  __DATA_CONST.__got: 0x8a8
   __DATA_CONST.__const: 0x2498
-  __DATA_CONST.__objc_classlist: 0x1f8
+  __DATA_CONST.__objc_classlist: 0x200
   __DATA_CONST.__objc_catlist: 0x80
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3cc8
+  __DATA_CONST.__objc_selrefs: 0x3d40
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x170
+  __DATA_CONST.__objc_superrefs: 0x178
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__auth_got: 0x420
+  __AUTH_CONST.__auth_got: 0x430
   __AUTH_CONST.__const: 0x680
-  __AUTH_CONST.__cfstring: 0x6a20
-  __AUTH_CONST.__objc_const: 0x98d8
+  __AUTH_CONST.__cfstring: 0x6a40
+  __AUTH_CONST.__objc_const: 0x9a28
   __AUTH_CONST.__objc_intobj: 0x480
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH.__objc_data: 0x8c0
-  __DATA.__objc_ivar: 0x7a8
-  __DATA.__data: 0xac0
-  __DATA.__bss: 0xa8
+  __AUTH.__objc_data: 0x910
+  __DATA.__objc_ivar: 0x7b4
+  __DATA.__data: 0xac8
+  __DATA.__bss: 0xb0
   __DATA_DIRTY.__objc_data: 0xaf0
-  __DATA_DIRTY.__bss: 0x208
+  __DATA_DIRTY.__bss: 0x220
   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/AVKit.framework/AVKit
+  - /System/Library/Frameworks/AVRouting.framework/AVRouting
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E51F476D-CDA4-306A-8531-6C03A8EFA519
-  Functions: 2244
-  Symbols:   8270
-  CStrings:  5501
+  UUID: 1B09526F-047E-3005-AAAC-AAC05E572408
+  Functions: 2259
+  Symbols:   8332
+  CStrings:  5534
 
Symbols:
+ +[TVPRoutingManager sharedInstance]
+ -[TVPPlayer _avResourcePriority:]
+ -[TVPPlayer _tvpResourcePriority:]
+ -[TVPPlayer _updateSynchronizationForAVQueuePlayer:synchronizationIdentifier:]
+ -[TVPPlayer _updateSynchronizationForAVQueuePlayer:synchronizationIdentifier:].cold.1
+ -[TVPPlayer networkResourcePriority]
+ -[TVPPlayer setNetworkResourcePriority:]
+ -[TVPPlayer setSynchronizationIdentifier:]
+ -[TVPPlayer synchronizationIdentifier]
+ -[TVPRoutingManager .cxx_destruct]
+ -[TVPRoutingManager _updatePlaybackArbiterWithPlayer:]
+ -[TVPRoutingManager observeValueForKeyPath:ofObject:change:context:]
+ -[TVPRoutingManager preferredPlayer]
+ -[TVPRoutingManager setPreferredPlayer:]
+ GCC_except_table121
+ GCC_except_table127
+ GCC_except_table225
+ GCC_except_table231
+ GCC_except_table236
+ GCC_except_table241
+ GCC_except_table242
+ GCC_except_table244
+ GCC_except_table291
+ GCC_except_table321
+ GCC_except_table331
+ GCC_except_table353
+ GCC_except_table357
+ GCC_except_table366
+ GCC_except_table379
+ GCC_except_table406
+ GCC_except_table409
+ GCC_except_table412
+ GCC_except_table414
+ GCC_except_table415
+ GCC_except_table417
+ GCC_except_table418
+ GCC_except_table426
+ GCC_except_table430
+ GCC_except_table434
+ GCC_except_table444
+ GCC_except_table446
+ GCC_except_table448
+ GCC_except_table473
+ GCC_except_table475
+ GCC_except_table478
+ GCC_except_table491
+ GCC_except_table495
+ GCC_except_table500
+ GCC_except_table504
+ GCC_except_table510
+ GCC_except_table518
+ GCC_except_table521
+ GCC_except_table533
+ GCC_except_table538
+ GCC_except_table542
+ GCC_except_table701
+ _OBJC_CLASS_$_AVPlaybackCoordinationMedium
+ _OBJC_CLASS_$_AVRoutingPlaybackArbiter
+ _OBJC_CLASS_$_TVPRoutingManager
+ _OBJC_IVAR_$_TVPPlayer._networkResourcePriority
+ _OBJC_IVAR_$_TVPPlayer._synchronizationIdentifier
+ _OBJC_IVAR_$_TVPRoutingManager._preferredPlayer
+ _OBJC_METACLASS_$_TVPRoutingManager
+ _PlayerKVOContext
+ __OBJC_$_CLASS_METHODS_TVPRoutingManager
+ __OBJC_$_INSTANCE_METHODS_TVPRoutingManager
+ __OBJC_$_INSTANCE_VARIABLES_TVPRoutingManager
+ __OBJC_$_PROP_LIST_TVPRoutingManager
+ __OBJC_CLASS_RO_$_TVPRoutingManager
+ __OBJC_METACLASS_RO_$_TVPRoutingManager
+ ___23-[TVPPlayer invalidate]_block_invoke.396
+ ___35+[TVPRoutingManager sharedInstance]_block_invoke
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.749
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.760
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.774
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.776
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.776.cold.1
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.782
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.783
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.787
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.791
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.792
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.796
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.800
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.804
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.806
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.808
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.827
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.837
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.842
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.850
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.855
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.857
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.859
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.867
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.871
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.872
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.876
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.878
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.890
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.892
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.901
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.906
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.907
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.908
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.920
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.921
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.922
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.929
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.930
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.939
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.954
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.963
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.973
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.977
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_10.887
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_10.948
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_11.949
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_12.950
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_13.951
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_14.952
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_15.953
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.751
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.761
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.779
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.784
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.810
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.838
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.844
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.849
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.851
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.856
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.858
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.860
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.868
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.873
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.877
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.879
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.891
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.904
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.909
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.919
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.923
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.927
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.931
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.940
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.955
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.978
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.753
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.762
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.780
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.786
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.812
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.839
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.845
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.852
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.863
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.874
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.880
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.912
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.924
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.928
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.932
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.941
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.956
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.981
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.755
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.781
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.819
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.841
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.853
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.864
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.875
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.881
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.925
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.933
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.942
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.957
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.982
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_5.820
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_5.854
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_5.865
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_5.882
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_5.934
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_5.943
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_5.958
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_5.983
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_6.821
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_6.866
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_6.883
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_6.935
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_6.944
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_6.959
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_7.823
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_7.884
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_7.936
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_7.945
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_7.962
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_7.962.cold.1
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_7.962.cold.2
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_7.962.cold.3
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_7.962.cold.4
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_7.962.cold.5
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_8.824
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_8.885
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_8.937
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_8.946
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_9.825
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_9.886
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_9.938
+ ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_9.947
+ ___43-[TVPPlayer _currentPlayerItemDidChangeTo:]_block_invoke.592
+ ___51-[TVPPlayer _integratedTimelineSnapshotsOutOfSync:]_block_invoke.599
+ ___56-[TVPPlayer changeToMediaAtIndex:reason:ignoreDelegate:]_block_invoke.422
+ ___58-[TVPPlayer changeMediaInDirection:reason:ignoreDelegate:]_block_invoke.413
+ ___58-[TVPPlayer changeMediaInDirection:reason:ignoreDelegate:]_block_invoke.420
+ ___60-[TVPPlayer observeValueForKeyPath:ofObject:change:context:]_block_invoke.407
+ ___block_literal_global.228
+ ___block_literal_global.364
+ ___block_literal_global.366
+ ___block_literal_global.428
+ ___block_literal_global.431
+ ___block_literal_global.602
+ ___block_literal_global.618
+ ___block_literal_global.620
+ ___block_literal_global.622
+ ___block_literal_global.862
+ ___block_literal_global.961
+ __updateSynchronizationForAVQueuePlayer:synchronizationIdentifier:.coordinatorMediums
+ _dispatch_queue_attr_make_with_autorelease_frequency
+ _dispatch_queue_attr_make_with_qos_class
+ _objc_msgSend$_avResourcePriority:
+ _objc_msgSend$_tvpResourcePriority:
+ _objc_msgSend$_updatePlaybackArbiterWithPlayer:
+ _objc_msgSend$_updateSynchronizationForAVQueuePlayer:synchronizationIdentifier:
+ _objc_msgSend$connectedPlaybackCoordinators
+ _objc_msgSend$coordinateUsingCoordinationMedium:error:
+ _objc_msgSend$networkResourcePriority
+ _objc_msgSend$playbackCoordinationMedium
+ _objc_msgSend$preferredPlayer
+ _objc_msgSend$setNetworkResourcePriority:
+ _objc_msgSend$setPreferredParticipantForExternalPlayback:
+ _objc_msgSend$setPreferredParticipantForNonMixableAudioRoutes:
+ _objc_msgSend$sharedRoutingPlaybackArbiter
+ _objc_msgSend$synchronizationIdentifier
- GCC_except_table114
- GCC_except_table120
- GCC_except_table218
- GCC_except_table221
- GCC_except_table222
- GCC_except_table224
- GCC_except_table234
- GCC_except_table237
- GCC_except_table284
- GCC_except_table314
- GCC_except_table324
- GCC_except_table346
- GCC_except_table350
- GCC_except_table359
- GCC_except_table372
- GCC_except_table391
- GCC_except_table399
- GCC_except_table401
- GCC_except_table402
- GCC_except_table404
- GCC_except_table407
- GCC_except_table410
- GCC_except_table416
- GCC_except_table419
- GCC_except_table427
- GCC_except_table432
- GCC_except_table437
- GCC_except_table441
- GCC_except_table466
- GCC_except_table468
- GCC_except_table471
- GCC_except_table477
- GCC_except_table486
- GCC_except_table488
- GCC_except_table497
- GCC_except_table503
- GCC_except_table511
- GCC_except_table514
- GCC_except_table526
- GCC_except_table528
- GCC_except_table531
- GCC_except_table693
- _OBJC_CLASS_$_AVPlayer
- ___23-[TVPPlayer invalidate]_block_invoke.397
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.746
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.754
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.771
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.773
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.773.cold.1
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.779
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.780
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.784
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.785
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.789
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.790
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.794
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.795
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.799
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.803
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.824
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.834
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.839
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.844
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.852
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.854
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.856
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.864
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.866
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.868
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.873
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.875
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.886
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.887
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.898
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.899
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.900
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.904
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.915
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.917
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.919
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.923
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.927
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.936
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.951
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.960
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.970
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.974
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_10.884
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_10.945
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_11.946
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_12.947
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_13.948
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_14.949
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_15.950
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.748
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.758
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.776
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.781
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.807
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.835
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.841
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.846
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.848
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.853
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.855
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.857
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.865
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.867
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.874
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.876
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.888
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.901
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.906
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.916
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.920
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.924
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.928
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.937
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.952
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.975
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.750
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.759
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.777
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.783
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.809
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.836
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.842
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.849
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.860
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.871
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.877
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.909
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.921
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.925
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.929
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.938
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.953
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.978
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.752
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.778
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.816
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.838
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.850
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.861
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.872
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.878
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.922
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.930
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.939
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.954
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.979
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_5.817
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_5.851
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_5.862
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_5.879
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_5.931
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_5.940
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_5.955
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_5.980
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_6.818
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_6.863
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_6.880
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_6.932
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_6.941
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_6.956
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_7.820
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_7.881
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_7.933
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_7.942
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_7.959
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_7.959.cold.1
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_7.959.cold.2
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_7.959.cold.3
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_7.959.cold.4
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_7.959.cold.5
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_8.821
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_8.882
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_8.934
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_8.943
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_9.822
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_9.883
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_9.935
- ___42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_9.944
- ___43-[TVPPlayer _currentPlayerItemDidChangeTo:]_block_invoke.589
- ___51-[TVPPlayer _integratedTimelineSnapshotsOutOfSync:]_block_invoke.596
- ___56-[TVPPlayer changeToMediaAtIndex:reason:ignoreDelegate:]_block_invoke.424
- ___58-[TVPPlayer changeMediaInDirection:reason:ignoreDelegate:]_block_invoke.414
- ___58-[TVPPlayer changeMediaInDirection:reason:ignoreDelegate:]_block_invoke.421
- ___60-[TVPPlayer observeValueForKeyPath:ofObject:change:context:]_block_invoke.408
- ___block_literal_global.229
- ___block_literal_global.365
- ___block_literal_global.367
- ___block_literal_global.429
- ___block_literal_global.432
- ___block_literal_global.599
- ___block_literal_global.615
- ___block_literal_global.617
- ___block_literal_global.619
- ___block_literal_global.859
- ___block_literal_global.958
- _objc_msgSend$setSupportsSharedNetworkCoordination:
CStrings:
+ "AVPlayer (%@) did change for %@"
+ "Failed to sync with coordinator medium using identifier %@, error %@"
+ "Ignoring set of %@ because it is the same as the previous value"
+ "Removing player observer for %@"
+ "Setting player %@ to routing playback arbiter"
+ "Setting player observer for %@"
+ "Successfully synced player %@, using medium %@, with synchronizationIdentifier %@"
+ "T@\"NSObject<TVPAVFPlayback>\",W,N,V_preferredPlayer"
+ "T@\"NSString\",&,N,V_synchronizationIdentifier"
+ "TVPRoutingManager"
+ "Tq,N,V_networkResourcePriority"
+ "_avResourcePriority:"
+ "_networkResourcePriority"
+ "_preferredPlayer"
+ "_synchronizationIdentifier"
+ "_tvpResourcePriority:"
+ "_updatePlaybackArbiterWithPlayer:"
+ "_updateSynchronizationForAVQueuePlayer:synchronizationIdentifier:"
+ "connectedPlaybackCoordinators"
+ "coordinateUsingCoordinationMedium:error:"
+ "networkResourcePriority"
+ "playbackCoordinationMedium"
+ "preferredPlayer"
+ "q24@0:8q16"
+ "setNetworkResourcePriority:"
+ "setPreferredParticipantForExternalPlayback:"
+ "setPreferredParticipantForNonMixableAudioRoutes:"
+ "setPreferredPlayer:"
+ "setSynchronizationIdentifier:"
+ "sharedRoutingPlaybackArbiter"
+ "synchronizationIdentifier"
- "setSupportsSharedNetworkCoordination:"

```
