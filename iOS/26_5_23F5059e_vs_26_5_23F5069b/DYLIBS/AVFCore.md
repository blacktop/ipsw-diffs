## AVFCore

> `/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`

```diff

-2420.6.1.0.0
-  __TEXT.__text: 0x1b19d0
+2420.7.1.0.0
+  __TEXT.__text: 0x1b1b10
   __TEXT.__auth_stubs: 0x3d10
-  __TEXT.__objc_methlist: 0x1b3ec
+  __TEXT.__objc_methlist: 0x1b3f4
   __TEXT.__cstring: 0x2460b
   __TEXT.__const: 0x1e58
   __TEXT.__gcc_except_tab: 0x6aec

   __TEXT.__swift5_capture: 0x60
   __TEXT.__unwind_info: 0x9788
   __TEXT.__objc_classname: 0x60a6
-  __TEXT.__objc_methname: 0x36db3
-  __TEXT.__objc_methtype: 0x9f57
-  __TEXT.__objc_stubs: 0x21220
+  __TEXT.__objc_methname: 0x36e0b
+  __TEXT.__objc_methtype: 0x9f67
+  __TEXT.__objc_stubs: 0x21240
   __DATA_CONST.__got: 0x46f8
   __DATA_CONST.__const: 0x57d0
   __DATA_CONST.__objc_classlist: 0x11b8
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x1e0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xadd0
+  __DATA_CONST.__objc_selrefs: 0xadd8
   __DATA_CONST.__objc_protorefs: 0x50
   __DATA_CONST.__objc_superrefs: 0xd08
   __DATA_CONST.__objc_arraydata: 0x308
   __AUTH_CONST.__auth_got: 0x1e98
   __AUTH_CONST.__const: 0x10f8
   __AUTH_CONST.__cfstring: 0x19400
-  __AUTH_CONST.__objc_const: 0x31110
+  __AUTH_CONST.__objc_const: 0x31150
   __AUTH_CONST.__objc_intobj: 0x2a0
   __AUTH_CONST.__objc_arrayobj: 0x348
   __AUTH_CONST.__objc_doubleobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0x7b50
   __AUTH.__data: 0x1e8
-  __DATA.__objc_ivar: 0x2624
+  __DATA.__objc_ivar: 0x262c
   __DATA.__data: 0x1810
   __DATA.__crash_info: 0x148
   __DATA.__common: 0x160

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 7776EC6C-87FC-3D5F-BA2D-77096813A412
-  Functions: 11586
-  Symbols:   39566
-  CStrings:  16966
+  UUID: 5E4BC0AE-E64D-350D-9345-7E6C33FE8B52
+  Functions: 11588
+  Symbols:   39573
+  CStrings:  16970
 
Symbols:
+ -[AVPlayer(AVPlayerMultitaskSupport) _invalidateBackgroundAssertionOnQueue]
+ GCC_except_table542
+ GCC_except_table550
+ GCC_except_table554
+ GCC_except_table561
+ GCC_except_table570
+ GCC_except_table575
+ GCC_except_table580
+ GCC_except_table594
+ GCC_except_table597
+ GCC_except_table612
+ GCC_except_table620
+ GCC_except_table624
+ GCC_except_table630
+ GCC_except_table638
+ GCC_except_table650
+ GCC_except_table654
+ GCC_except_table660
+ GCC_except_table667
+ GCC_except_table672
+ GCC_except_table679
+ GCC_except_table690
+ GCC_except_table695
+ GCC_except_table704
+ GCC_except_table711
+ GCC_except_table718
+ GCC_except_table719
+ GCC_except_table723
+ GCC_except_table733
+ GCC_except_table737
+ GCC_except_table745
+ GCC_except_table748
+ GCC_except_table752
+ GCC_except_table762
+ GCC_except_table774
+ GCC_except_table781
+ GCC_except_table791
+ GCC_except_table796
+ GCC_except_table806
+ GCC_except_table830
+ GCC_except_table835
+ GCC_except_table847
+ GCC_except_table859
+ _OBJC_IVAR_$_AVPlayerInternal.backgroundAssertion
+ _OBJC_IVAR_$_AVPlayerInternal.backgroundAssertionGeneration
+ ___109-[AVPlayer _runOnIvarAccessQueueOperationThatMayChangeCurrentItemWithPreflightBlock:modificationBlock:error:]_block_invoke.464
+ ___109-[AVPlayer _runOnIvarAccessQueueOperationThatMayChangeCurrentItemWithPreflightBlock:modificationBlock:error:]_block_invoke.465
+ ___109-[AVPlayer _runOnIvarAccessQueueOperationThatMayChangeCurrentItemWithPreflightBlock:modificationBlock:error:]_block_invoke_2.466
+ ___58-[AVPlayer(AVPlayerMultitaskSupport) _didEnterBackground:]_block_invoke_4
+ ___62-[AVPlayer _setRate:rateChangeReason:figPlayerSetRateHandler:]_block_invoke.529
+ ___67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke.489
+ ___67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke_2.493
+ ___67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke_3.501
+ ___67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke_4.502
+ ___67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke_5.509
+ ___67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke_6.510
+ ___67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke_7.512
+ ___67-[AVPlayer(AVPlayerPIPSupport) _setSilencesOtherPlaybackDuringPIP:]_block_invoke.1166
+ ___90-[AVPlayer(AVPlayerPIPSupport) setPrefersPlayingSilentlyWhenConflictingWithOtherPlayback:]_block_invoke.1163
+ ___91-[AVPlayer(AVPlayerRoutingPlaybackArbitrationSupport) _setNonMixableAudioPriorityInternal:]_block_invoke.1259
+ ___avplayer_fpNotificationCallback_block_invoke.1431
+ ___avplayer_fpNotificationCallback_block_invoke_2.1432
+ ___block_literal_global.1409
+ ___block_literal_global.1447
+ ___block_literal_global.1473
+ ___block_literal_global.601
+ ___block_literal_global.616
+ ___block_literal_global.969
+ _objc_msgSend$_invalidateBackgroundAssertionOnQueue
- GCC_except_table540
- GCC_except_table552
- GCC_except_table563
- GCC_except_table568
- GCC_except_table578
- GCC_except_table581
- GCC_except_table586
- GCC_except_table610
- GCC_except_table618
- GCC_except_table622
- GCC_except_table626
- GCC_except_table632
- GCC_except_table646
- GCC_except_table652
- GCC_except_table658
- GCC_except_table663
- GCC_except_table675
- GCC_except_table682
- GCC_except_table693
- GCC_except_table698
- GCC_except_table709
- GCC_except_table717
- GCC_except_table721
- GCC_except_table729
- GCC_except_table735
- GCC_except_table743
- GCC_except_table750
- GCC_except_table756
- GCC_except_table770
- GCC_except_table787
- GCC_except_table794
- GCC_except_table804
- GCC_except_table833
- GCC_except_table838
- GCC_except_table843
- GCC_except_table857
- ___109-[AVPlayer _runOnIvarAccessQueueOperationThatMayChangeCurrentItemWithPreflightBlock:modificationBlock:error:]_block_invoke.461
- ___109-[AVPlayer _runOnIvarAccessQueueOperationThatMayChangeCurrentItemWithPreflightBlock:modificationBlock:error:]_block_invoke.462
- ___109-[AVPlayer _runOnIvarAccessQueueOperationThatMayChangeCurrentItemWithPreflightBlock:modificationBlock:error:]_block_invoke_2.463
- ___62-[AVPlayer _setRate:rateChangeReason:figPlayerSetRateHandler:]_block_invoke.526
- ___67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke.486
- ___67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke_2.490
- ___67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke_3.498
- ___67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke_4.499
- ___67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke_5.506
- ___67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke_6.507
- ___67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke_7.509
- ___67-[AVPlayer(AVPlayerPIPSupport) _setSilencesOtherPlaybackDuringPIP:]_block_invoke.1162
- ___90-[AVPlayer(AVPlayerPIPSupport) setPrefersPlayingSilentlyWhenConflictingWithOtherPlayback:]_block_invoke.1159
- ___91-[AVPlayer(AVPlayerRoutingPlaybackArbitrationSupport) _setNonMixableAudioPriorityInternal:]_block_invoke.1255
- ___avplayer_fpNotificationCallback_block_invoke.1427
- ___avplayer_fpNotificationCallback_block_invoke_2.1428
- ___block_literal_global.1405
- ___block_literal_global.1443
- ___block_literal_global.1469
- ___block_literal_global.595
- ___block_literal_global.613
- ___block_literal_global.966
Functions:
~ -[AVPlayer dealloc] : 1692 -> 1724
+ -[AVPlayer(AVPlayerMultitaskSupport) _invalidateBackgroundAssertionOnQueue]
~ ___58-[AVPlayer(AVPlayerMultitaskSupport) _didEnterBackground:]_block_invoke : 196 -> 236
~ ___58-[AVPlayer(AVPlayerMultitaskSupport) _didEnterBackground:]_block_invoke_2 : 196 -> 220
~ ___58-[AVPlayer(AVPlayerMultitaskSupport) _didEnterBackground:]_block_invoke_3 : 8 -> 128
+ ___58-[AVPlayer(AVPlayerMultitaskSupport) _didEnterBackground:]_block_invoke_4
~ ___59-[AVPlayer(AVPlayerMultitaskSupport) _willEnterForeground:]_block_invoke : 84 -> 92
CStrings:
+ "@\"RBSAssertion\""
+ "_invalidateBackgroundAssertionOnQueue"
+ "backgroundAssertion"
+ "backgroundAssertionGeneration"

```
