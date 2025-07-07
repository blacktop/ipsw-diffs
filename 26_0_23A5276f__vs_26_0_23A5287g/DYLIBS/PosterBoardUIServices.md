## PosterBoardUIServices

> `/System/Library/PrivateFrameworks/PosterBoardUIServices.framework/PosterBoardUIServices`

```diff

-280.101.0.0.0
-  __TEXT.__text: 0x8cd30
-  __TEXT.__auth_stubs: 0x1f40
-  __TEXT.__objc_methlist: 0x6780
-  __TEXT.__const: 0x2518
-  __TEXT.__cstring: 0x524f
-  __TEXT.__gcc_except_tab: 0xe84
-  __TEXT.__oslogstring: 0x3b1f
+283.101.0.0.0
+  __TEXT.__text: 0x8d590
+  __TEXT.__auth_stubs: 0x1f80
+  __TEXT.__objc_methlist: 0x67f8
+  __TEXT.__const: 0x2528
+  __TEXT.__cstring: 0x522f
+  __TEXT.__gcc_except_tab: 0xf08
+  __TEXT.__oslogstring: 0x3c6f
   __TEXT.__swift5_typeref: 0x58ef
   __TEXT.__constg_swiftt: 0xbcc
   __TEXT.__swift5_reflstr: 0x903

   __TEXT.__swift5_assocty: 0x288
   __TEXT.__swift5_proto: 0x10c
   __TEXT.__swift5_types: 0x84
-  __TEXT.__swift5_capture: 0x264
+  __TEXT.__swift5_capture: 0x274
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift_as_entry: 0x3c
   __TEXT.__swift_as_ret: 0x48
-  __TEXT.__unwind_info: 0x24a8
+  __TEXT.__unwind_info: 0x24b0
   __TEXT.__eh_frame: 0x1478
-  __TEXT.__objc_classname: 0x144d
-  __TEXT.__objc_methname: 0x1315f
-  __TEXT.__objc_methtype: 0x31d1
-  __TEXT.__objc_stubs: 0xb6e0
-  __DATA_CONST.__got: 0xce8
-  __DATA_CONST.__const: 0x1fb8
+  __TEXT.__objc_classname: 0x1451
+  __TEXT.__objc_methname: 0x1340e
+  __TEXT.__objc_methtype: 0x3257
+  __TEXT.__objc_stubs: 0xb820
+  __DATA_CONST.__got: 0xce0
+  __DATA_CONST.__const: 0x1ec0
   __DATA_CONST.__objc_classlist: 0x328
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x268
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3c20
+  __DATA_CONST.__objc_selrefs: 0x3c88
   __DATA_CONST.__objc_protorefs: 0x90
   __DATA_CONST.__objc_superrefs: 0x218
-  __AUTH_CONST.__auth_got: 0xfb0
-  __AUTH_CONST.__const: 0x15f8
-  __AUTH_CONST.__cfstring: 0x32e0
-  __AUTH_CONST.__objc_const: 0x140a8
+  __AUTH_CONST.__auth_got: 0xfd0
+  __AUTH_CONST.__const: 0x1640
+  __AUTH_CONST.__cfstring: 0x3300
+  __AUTH_CONST.__objc_const: 0x14120
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH.__objc_data: 0x1738
   __AUTH.__data: 0x5d0
-  __DATA.__objc_ivar: 0x77c
+  __DATA.__objc_ivar: 0x788
   __DATA.__data: 0x2770
   __DATA.__bss: 0x2420
   __DATA.__common: 0x98

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 67BF07E7-1DE1-3CFF-B863-983D09C0F81A
-  Functions: 3385
-  Symbols:   9282
-  CStrings:  4619
+  UUID: 69408F9F-0381-3482-A69D-FDC145577AF0
+  Functions: 3394
+  Symbols:   9306
+  CStrings:  4646
 
Symbols:
+ +[PRUISPosterChannelSnapshotDefinition galleryDefinitionForChannelIdentifier:]
+ -[PRUISDeviceMotionProvider _activeOrientationChangedDate]
+ -[PRUISDeviceMotionProvider _previousAttitudeQuaternion]
+ -[PRUISDeviceMotionProvider _previousOrientation]
+ -[PRUISDeviceMotionProvider _queue_processDeviceMotion:].cold.3
+ -[PRUISDeviceMotionProvider _setPreviousAttitudeQuaternion:]
+ -[PRUISPosterChannelViewController _fetchInitialStateSnapshotBundleForPoster:]
+ -[PRUISPosterChannelViewController delegate]
+ -[PRUISPosterChannelViewController initWithChannel:purpose:context:delegate:initialRenderingOptions:]
+ -[PRUISPosterChannelViewController initWithChannel:purpose:context:delegate:initialRenderingOptions:].cold.1
+ -[PRUISPosterChannelViewController initWithChannel:purpose:context:delegate:initialRenderingOptions:].cold.2
+ -[PRUISPosterChannelViewController initWithChannel:purpose:context:delegate:initialRenderingOptions:].cold.3
+ -[PRUISPosterChannelViewController setDelegate:]
+ -[PRUISPosterRenderingViewController _updateBackgroundSceneToSize:orientation:withAnimationSettings:]
+ -[PRUISPosterRenderingViewController _updateBackgroundSceneToSize:orientation:withAnimationSettings:].cold.1
+ -[PRUISPosterSnapshotSQLiteCache discardSnapshotsForPostersMatchingPredicate:].cold.1
+ GCC_except_table148
+ GCC_except_table159
+ GCC_except_table28
+ GCC_except_table56
+ GCC_except_table66
+ GCC_except_table82
+ _OBJC_IVAR_$_PRUISDeviceMotionProvider._lock_activeOrientationChangedDate
+ _OBJC_IVAR_$_PRUISDeviceMotionProvider._lock_previousAttitudeQuaternion
+ _OBJC_IVAR_$_PRUISDeviceMotionProvider._lock_previousOrientation
+ _OBJC_IVAR_$_PRUISPosterChannelViewController._delegate
+ _OBJC_IVAR_$_PRUISPosterChannelViewController._initialStateWaitingForLiveRenderingSnapshotBundle
+ __ZL20_simd_slerp_internal10simd_quatdS_d
+ ___101-[PRUISPosterChannelViewController initWithChannel:purpose:context:delegate:initialRenderingOptions:]_block_invoke
+ ___101-[PRUISPosterRenderingViewController _updateBackgroundSceneToSize:orientation:withAnimationSettings:]_block_invoke
+ ___101-[PRUISPosterRenderingViewController _updateBackgroundSceneToSize:orientation:withAnimationSettings:]_block_invoke_2
+ ___110-[_PRUISPosterSnapshotControllerImpl _snapshotRequestDidFinishWithResult:snapshotterError:request:completion:]_block_invoke.129
+ ___110-[_PRUISPosterSnapshotControllerImpl _snapshotRequestDidFinishWithResult:snapshotterError:request:completion:]_block_invoke.129.cold.1
+ ___110-[_PRUISPosterSnapshotControllerImpl _snapshotRequestDidFinishWithResult:snapshotterError:request:completion:]_block_invoke.132
+ ___62-[_PRUISPosterChannelUpdateDescriptorsTask _executeWithState:]_block_invoke.177
+ ___69-[_PRUISPosterChannelUpdateDescriptorsTask channel:didUpdateContext:]_block_invoke
+ ___71-[PRUISPosterChannelViewController _snapshotCurrentPosterConfiguration]_block_invoke.90
+ ___71-[PRUISPosterChannelViewController _snapshotCurrentPosterConfiguration]_block_invoke.90.cold.1
+ ___72-[_PRUISPosterSnapshotControllerImpl executeSnapshotRequest:completion:]_block_invoke.119
+ ___89-[PRUISPosterRenderingViewController viewWillTransitionToSize:withTransitionCoordinator:]_block_invoke
+ ___89-[PRUISPosterRenderingViewController viewWillTransitionToSize:withTransitionCoordinator:]_block_invoke_2
+ ___block_descriptor_139_e8_32s40s_e63_v24?0"FBSMutableSceneSettings"8"FBSSceneTransitionContext"16ls32l8s40l8
+ ___block_descriptor_32_e56_v16?0"<UIViewControllerTransitionCoordinatorContext>"8l
+ ___block_descriptor_48_e8_32s40w_e33_v16?0"PUIPosterSnapshotBundle"8lw40l8s32l8
+ ___block_descriptor_72_e8_32s40s_e56_v16?0"<UIViewControllerTransitionCoordinatorContext>"8ls32l8s40l8
+ ___block_literal_global.135
+ ___block_literal_global.141
+ ___block_literal_global.147
+ ___block_literal_global.170
+ ___block_literal_global.175
+ _atan2
+ _block_copy_helper.178
+ _block_copy_helper.181
+ _block_copy_helper.191
+ _block_copy_helper.194
+ _block_copy_helper.198
+ _block_copy_helper.274
+ _block_descriptor.180
+ _block_descriptor.183
+ _block_descriptor.193
+ _block_descriptor.196
+ _block_descriptor.200
+ _block_descriptor.276
+ _block_destroy_helper.179
+ _block_destroy_helper.182
+ _block_destroy_helper.192
+ _block_destroy_helper.195
+ _block_destroy_helper.199
+ _block_destroy_helper.275
+ _objc_msgSend$SQLitePredicate
+ _objc_msgSend$_activeOrientationChangedDate
+ _objc_msgSend$_fetchInitialStateSnapshotBundleForPoster:
+ _objc_msgSend$_previousAttitudeQuaternion
+ _objc_msgSend$_previousOrientation
+ _objc_msgSend$_setPreviousAttitudeQuaternion:
+ _objc_msgSend$_updateBackgroundSceneToSize:orientation:withAnimationSettings:
+ _objc_msgSend$animateAlongsideTransition:completion:
+ _objc_msgSend$cleanupWithError:
+ _objc_msgSend$discardSnapshotBundlesMatchingSQLPredicate:outError:
+ _objc_msgSend$initWithChannel:purpose:context:delegate:initialRenderingOptions:
+ _objc_msgSend$initialStateSnapshotDescriptorForPosterConfiguration:
+ _objc_msgSend$latestSnapshotBundleMatchingPredicate:outError:
+ _objc_msgSend$orPredicate:
+ _objc_msgSend$removeObjectAtIndex:
+ _objc_msgSend$snapshotBundlesMatchingPredicate:outError:
+ _objc_msgSend$timeIntervalSinceNow
+ _objc_terminate
+ _objectdestroy.263Tm
+ _sin
- -[PRUISPosterChannelViewController initWithChannel:purpose:context:].cold.1
- -[PRUISPosterChannelViewController initWithChannel:purpose:context:].cold.2
- -[PRUISPosterChannelViewController initWithChannel:purpose:context:].cold.3
- -[PRUISPosterEditingViewController updateMotionWithRotation:].cold.1
- -[PRUISPosterRenderingViewController _updateBackgroundSceneToSize:orientation:withAnimationSettings:fence:]
- -[PRUISPosterRenderingViewController _updateBackgroundSceneToSize:orientation:withAnimationSettings:fence:].cold.1
- -[PRUISPosterRenderingViewController updateMotionWithRotation:].cold.1
- GCC_except_table14
- GCC_except_table146
- GCC_except_table29
- GCC_except_table32
- GCC_except_table48
- GCC_except_table54
- GCC_except_table70
- GCC_except_table75
- GCC_except_table80
- _OBJC_CLASS_$_PFDefer
- _OBJC_IVAR_$_PRUISPosterRenderingViewController._isAnimatingTransitionToSize
- _OBJC_IVAR_$_PRUISPosterRenderingViewController._needsLayoutWhileInAnimationBlock
- ___107-[PRUISPosterRenderingViewController _updateBackgroundSceneToSize:orientation:withAnimationSettings:fence:]_block_invoke
- ___107-[PRUISPosterRenderingViewController _updateBackgroundSceneToSize:orientation:withAnimationSettings:fence:]_block_invoke_2
- ___110-[_PRUISPosterSnapshotControllerImpl _snapshotRequestDidFinishWithResult:snapshotterError:request:completion:]_block_invoke.128
- ___110-[_PRUISPosterSnapshotControllerImpl _snapshotRequestDidFinishWithResult:snapshotterError:request:completion:]_block_invoke.128.cold.1
- ___110-[_PRUISPosterSnapshotControllerImpl _snapshotRequestDidFinishWithResult:snapshotterError:request:completion:]_block_invoke.131
- ___60-[PRUISPosterChannelViewController channel:didUpdatePoster:]_block_invoke_7
- ___62-[_PRUISPosterChannelUpdateDescriptorsTask _executeWithState:]_block_invoke.178
- ___67-[PRUISPosterChannelViewController _createViewControllerForPoster:]_block_invoke
- ___67-[PRUISPosterChannelViewController _createViewControllerForPoster:]_block_invoke.110
- ___67-[PRUISPosterChannelViewController _createViewControllerForPoster:]_block_invoke.114
- ___67-[PRUISPosterChannelViewController _createViewControllerForPoster:]_block_invoke_2
- ___67-[PRUISPosterChannelViewController _createViewControllerForPoster:]_block_invoke_2.113
- ___68-[PRUISPosterChannelViewController initWithChannel:purpose:context:]_block_invoke
- ___68-[PRUISPosterChannelViewController initWithChannel:purpose:context:]_block_invoke_2
- ___71-[PRUISPosterChannelViewController _snapshotCurrentPosterConfiguration]_block_invoke.91
- ___71-[PRUISPosterChannelViewController _snapshotCurrentPosterConfiguration]_block_invoke.91.cold.1
- ___72-[_PRUISPosterSnapshotControllerImpl executeSnapshotRequest:completion:]_block_invoke.118
- ___78-[PRUISPosterSnapshotSQLiteCache discardSnapshotsForPostersMatchingPredicate:]_block_invoke
- ___block_descriptor_105_e8_32s40s48s56s_e63_v24?0"FBSMutableSceneSettings"8"FBSSceneTransitionContext"16ls32l8s40l8s48l8s56l8
- ___block_descriptor_40_e8_32bs_e9_16?0^8ls32l8
- ___block_descriptor_40_e8_32w_e44_v16?0"PRUISPosterRenderingViewController"8lw32l8
- ___block_descriptor_48_e8_32bs40w_e30_"<PFTFuture>"16?0"NSError"8lw40l8s32l8
- ___block_descriptor_48_e8_32bs40w_e46_"<PFTFuture>"16?0"PUIPosterSnapshotBundle"8lw40l8s32l8
- ___block_descriptor_48_e8_32s40bs_e9_16?0^8ls40l8s32l8
- ___block_descriptor_48_e8_32s40s_e30_"<PFTFuture>"16?0"NSArray"8ls32l8s40l8
- ___block_descriptor_56_e8_32s40s48s_e69_"PRUISPosterRenderingViewController"16?0"PUIPosterSnapshotBundle"8ls32l8s40l8s48l8
- ___block_descriptor_56_e8_32s40s48w_e33_v16?0"PUIPosterSnapshotBundle"8lw48l8s32l8s40l8
- ___block_descriptor_64_e8_32s40s48bs56w_e44_v16?0"PRUISPosterRenderingViewController"8lw56l8s32l8s40l8s48l8
- ___block_literal_global.144
- ___block_literal_global.167
- ___block_literal_global.172
- _block_copy_helper.173
- _block_copy_helper.176
- _block_copy_helper.186
- _block_copy_helper.189
- _block_copy_helper.193
- _block_copy_helper.269
- _block_descriptor.175
- _block_descriptor.178
- _block_descriptor.188
- _block_descriptor.191
- _block_descriptor.195
- _block_descriptor.271
- _block_destroy_helper.174
- _block_destroy_helper.177
- _block_destroy_helper.187
- _block_destroy_helper.190
- _block_destroy_helper.194
- _block_destroy_helper.270
- _objc_msgSend$_latestSnapshotBundleForConfiguration:
- _objc_msgSend$_purgeSnapshotBundleFuture:
- _objc_msgSend$_updateBackgroundSceneToSize:orientation:withAnimationSettings:fence:
- _objc_msgSend$block:
- _objc_msgSend$chain:
- _objc_msgSend$discardSnapshotBundlesMatchingPredicate:
- _objc_msgSend$isSceneContentReady
- _objectdestroy.258Tm
CStrings:
+ "%@_%@"
+ "%s reaping snapshots matching predicate: %@"
+ "%{public}@ adding new view controller: %{public}@"
+ "%{public}@ fetching initial state snapshot bundle for predicate (host-provided? %{public}@): %{public}@"
+ "<%{public}@:%{public}p> error discarding snapshot bundles using predicate: %{public}@, error: %{public}@"
+ "<%{public}@:%{public}p>error fetching snapshotBundles matching predicate, cannot discard: %{public}@"
+ "@\"<PRUISPosterChannelViewControllerDelegate>\""
+ "Smooth out device motion events for a recent interface orientation change using the previous attitude: x: %f, y: %f, z: %f, w: %f"
+ "T@\"<PRUISPosterChannelViewControllerDelegate>\",W,N,V_delegate"
+ "_activeOrientationChangedDate"
+ "_fetchInitialStateSnapshotBundleForPoster:"
+ "_initialStateWaitingForLiveRenderingSnapshotBundle"
+ "_lock_activeOrientationChangedDate"
+ "_lock_previousAttitudeQuaternion"
+ "_lock_previousOrientation"
+ "_previousAttitudeQuaternion"
+ "_previousOrientation"
+ "_setPreviousAttitudeQuaternion:"
+ "_updateBackgroundSceneToSize:orientation:withAnimationSettings:"
+ "animateAlongsideTransition:completion:"
+ "checkCacheIsReachableAsync"
+ "cleanupWithError:"
+ "discardSnapshotBundlesMatchingSQLPredicate:outError:"
+ "galleryDefinitionForChannelIdentifier:"
+ "initWithChannel:purpose:context:delegate:initialRenderingOptions:"
+ "initialStateSnapshotDescriptorForPosterConfiguration:"
+ "latestSnapshotBundleMatchingPredicate:outError:"
+ "removeObjectAtIndex:"
+ "snapshotBundlesMatchingPredicate:outError:"
+ "timeIntervalSinceNow"
+ "v16@?0@\"<UIViewControllerTransitionCoordinatorContext>\"8"
+ "v48@0:8{?=}16"
+ "v48@0:8{CGSize=dd}16q32@40"
+ "{?=\"vector\"}"
+ "{?=}16@0:8"
+ "\xa1"
+ "\xf01"
+ "\xf0\xf0B"
- "%s Reaping snapshots matching predicate: %@"
- "(%{public}@:%p) Ignoring motion update because scene content is not ready"
- "@\"<PFTFuture>\"16@?0@\"NSArray\"8"
- "@\"PRUISPosterRenderingViewController\"16@?0@\"PUIPosterSnapshotBundle\"8"
- "SceneViewController-%p: ignoring motion update because scene content is not ready"
- "_isAnimatingTransitionToSize"
- "_needsLayoutWhileInAnimationBlock"
- "_updateBackgroundSceneToSize:orientation:withAnimationSettings:fence:"
- "block:"
- "chain:"
- "isSceneContentReady"
- "\xb1"
- "\xf0\xf0R"

```
