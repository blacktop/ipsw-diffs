## BiometricKitUI

> `/System/Library/PrivateFrameworks/BiometricKitUI.framework/BiometricKitUI`

```diff

-684.100.0.0.0
-  __TEXT.__text: 0x6eabc
-  __TEXT.__objc_methlist: 0x72e0
+685.1.2.0.0
+  __TEXT.__text: 0x6ee28
+  __TEXT.__objc_methlist: 0x7300
   __TEXT.__const: 0xd44
   __TEXT.__gcc_except_tab: 0xde4
-  __TEXT.__cstring: 0x3026
-  __TEXT.__oslogstring: 0x6963
+  __TEXT.__cstring: 0x3036
+  __TEXT.__oslogstring: 0x6a83
   __TEXT.__dlopen_cstrs: 0x292
   __TEXT.__swift5_typeref: 0x2c2
   __TEXT.__swift5_capture: 0x114

   __TEXT.__swift5_proto: 0x20
   __TEXT.__swift5_types: 0x34
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x2140
+  __TEXT.__unwind_info: 0x2150
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_protolist: 0x160
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4918
+  __DATA_CONST.__objc_selrefs: 0x4928
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x198
   __DATA_CONST.__objc_arraydata: 0x188
   __DATA_CONST.__got: 0x880
   __AUTH_CONST.__const: 0xc50
-  __AUTH_CONST.__cfstring: 0x3400
+  __AUTH_CONST.__cfstring: 0x3440
   __AUTH_CONST.__objc_const: 0x10720
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_arrayobj: 0xc0

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2875
-  Symbols:   6386
-  CStrings:  1078
+  Functions: 2878
+  Symbols:   6392
+  CStrings:  1083
 
Symbols:
+ -[BKUIHostedDynamicallySizedJindoPresentable _sweepStalePresentablesFromBannerSource:]
+ -[BKUIPearlEnrollView _resetPreviewLayerBlur]
+ -[BKUIPearlJindoEnrollViewController endEnrollFlowWithError:]
+ GCC_except_table20
+ GCC_except_table34
+ GCC_except_table72
+ GCC_except_table96
+ _objc_msgSend$_resetPreviewLayerBlur
+ _objc_msgSend$_sweepStalePresentablesFromBannerSource:
+ _objc_msgSend$adjustedContentInset
+ _objc_msgSend$revokeAllPresentablesWithReason:userInfo:error:
+ _objc_msgSend$setAccessibilityLabel:
- GCC_except_table71
- GCC_except_table95
- ___61-[BKUIPearlJindoEnrollViewController nextStateButtonPressed:]_block_invoke_2
- _objc_msgSend$presentingViewController
- _objc_msgSend$statusBarFrame
- _objc_msgSend$statusBarManager
Functions:
+ -[BKUIPearlJindoEnrollViewController endEnrollFlowWithError:]
~ -[BKUIPearlJindoEnrollViewController _postBannerToDestinationWithInitialStateCollapsed:enrollViewStateConfiguration:] : 664 -> 708
~ -[BKUIPearlJindoEnrollViewController nextStateButtonPressed:] : 480 -> 524
~ ___61-[BKUIPearlJindoEnrollViewController nextStateButtonPressed:]_block_invoke : 116 -> 308
~ -[BKUIPearlMovieLoopView selfPortrait] : 272 -> 248
~ -[BKUIPearlEnrollViewController _updateLeftBarButtonItem] : 1060 -> 1108
~ -[BKUIPearlEnrollViewController returnToEnroll] : 64 -> 196
~ -[BKUIPearlEnrollView preEnrollActivate] : 40 -> 80
~ -[BKUIPearlEnrollView _endAndCleanupEnrollSessionIfNeeded] : 136 -> 144
+ -[BKUIPearlEnrollView _resetPreviewLayerBlur]
~ -[BKUIFingerPrintEnrollTutorialViewController _contentViewTopOffset] : 304 -> 64
~ -[BKUIHostedDynamicallySizedJindoPresentable revoke] : 300 -> 336
+ -[BKUIHostedDynamicallySizedJindoPresentable _sweepStalePresentablesFromBannerSource:]
CStrings:
+ "Error revoking presentables %{public}@"
+ "Pearl: skipping Jindo banner post as enrollment is no longer active"
+ "Resetting preview layer blur"
+ "Returning to enroll from partial capture, target state %i"
+ "Revoking current presentable"
+ "Swept %{public}lu orphaned presentable(s) after a stale request identifier"
+ "com.apple.biometrickitui.revoke"
+ "com.apple.biometrickitui.staleIdentifierSweep"
- "-[BKUIPearlMovieLoopView selfPortrait]"
- "BKUIPearlMovieLoopView.m"
- "false"
```
