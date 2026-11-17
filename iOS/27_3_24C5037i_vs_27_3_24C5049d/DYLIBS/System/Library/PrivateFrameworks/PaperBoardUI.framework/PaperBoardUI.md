## PaperBoardUI

> `/System/Library/PrivateFrameworks/PaperBoardUI.framework/PaperBoardUI`

```diff

-355.3.7.0.0
-  __TEXT.__text: 0x83a70
-  __TEXT.__objc_methlist: 0xa2c4
+355.3.12.0.0
+  __TEXT.__text: 0x84c78
+  __TEXT.__objc_methlist: 0xa384
   __TEXT.__const: 0x8a8
-  __TEXT.__cstring: 0x8759
-  __TEXT.__gcc_except_tab: 0xe34
-  __TEXT.__oslogstring: 0x6de3
+  __TEXT.__cstring: 0x890e
+  __TEXT.__gcc_except_tab: 0xea0
+  __TEXT.__oslogstring: 0x714a
   __TEXT.__dlopen_cstrs: 0x1a6
-  __TEXT.__unwind_info: 0x37c8
+  __TEXT.__unwind_info: 0x3838
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x24b8
+  __DATA_CONST.__const: 0x24e0
   __DATA_CONST.__objc_classlist: 0x378
   __DATA_CONST.__objc_catlist: 0x68
   __DATA_CONST.__objc_protolist: 0x1f0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5788
+  __DATA_CONST.__objc_selrefs: 0x57e0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x310
   __DATA_CONST.__objc_arraydata: 0x1e0
   __DATA_CONST.__got: 0x8f0
   __AUTH_CONST.__const: 0x980
-  __AUTH_CONST.__cfstring: 0x6840
-  __AUTH_CONST.__objc_const: 0x1ac88
+  __AUTH_CONST.__cfstring: 0x6900
+  __AUTH_CONST.__objc_const: 0x1ad48
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH_CONST.__objc_dictobj: 0x1b8
   __AUTH_CONST.__objc_intobj: 0x120

   __AUTH_CONST.__auth_got: 0x870
   __AUTH.__objc_data: 0x2260
   __AUTH.__data: 0x8
-  __DATA.__objc_ivar: 0xb08
+  __DATA.__objc_ivar: 0xb20
   __DATA.__data: 0x1760
   __DATA_DIRTY.__objc_data: 0x50
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 4111
-  Symbols:   6609
-  CStrings:  1647
+  Functions: 4138
+  Symbols:   6643
+  CStrings:  1667
 
Symbols:
+ -[PBUIPosterViewController _checkTransferReadiness]
+ -[PBUIPosterViewController _computeIsReadyToTransfer]
+ -[PBUIPosterViewController _invalidateTransferReadinessPoll]
+ -[PBUIPosterViewController _pollUntilReadyToTransferWithCompletion:]
+ -[PBUIPosterViewController _transferReadinessDescription]
+ -[PBUIPosterViewController isReadyToTransfer]
+ -[PBUIPosterViewController notifyWhenDisplayTransferAcknowledgedWithCompletion:]
+ -[PBUIPosterViewController notifyWhenReadyToTransferWithCompletion:]
+ -[PBUIPosterWallpaperRemoteViewController isReadyToTransfer]
+ -[PBUIPosterWallpaperRemoteViewController notifyWhenDisplayTransferAcknowledgedWithCompletion:]
+ -[PBUIPosterWallpaperRemoteViewController notifyWhenReadyToTransferWithCompletion:]
+ -[PBUIPosterWallpaperRemoteViewController significantEventsCounter]
+ -[PBUIPosterWallpaperViewController isReadyToTransfer]
+ -[PBUIPosterWallpaperViewController notifyWhenDisplayTransferAcknowledgedWithCompletion:]
+ -[PBUIPosterWallpaperViewController notifyWhenReadyToTransferWithCompletion:]
+ -[PBUIPosterWallpaperViewController significantEventsCounter]
+ GCC_except_table118
+ GCC_except_table144
+ GCC_except_table148
+ GCC_except_table160
+ GCC_except_table164
+ GCC_except_table166
+ GCC_except_table170
+ GCC_except_table173
+ GCC_except_table176
+ GCC_except_table179
+ GCC_except_table182
+ GCC_except_table185
+ GCC_except_table191
+ GCC_except_table193
+ GCC_except_table195
+ GCC_except_table197
+ GCC_except_table199
+ GCC_except_table201
+ GCC_except_table89
+ _OBJC_IVAR_$_PBUIPosterViewController._latestDisplayTransferAcknowledgement
+ _OBJC_IVAR_$_PBUIPosterViewController._pendingTransferReadinessCompletion
+ _OBJC_IVAR_$_PBUIPosterViewController._transferReadinessAssertion
+ _OBJC_IVAR_$_PBUIPosterViewController._transferReadinessDisplayLink
+ _OBJC_IVAR_$_PBUIPosterViewController._transferReadinessExpectedScene
+ _OBJC_IVAR_$_PBUIPosterViewController._transferReadinessPollTickCount
+ ___68-[PBUIPosterViewController _pollUntilReadyToTransferWithCompletion:]_block_invoke
+ ___68-[PBUIPosterViewController _pollUntilReadyToTransferWithCompletion:]_block_invoke_2
+ ___72-[PBUIPosterViewController viewDidMoveToWindow:shouldAppearOrDisappear:]_block_invoke
+ ___80-[PBUIPosterViewController notifyWhenDisplayTransferAcknowledgedWithCompletion:]_block_invoke
+ ___block_descriptor_40_e8_32bs_e20_v24?08"NSError"16ls32l8
+ ___getNSStringFromPUIPosterArbitrationBlockingReasonSymbolLoc_block_invoke
+ ___getPFTFutureClass_block_invoke
+ _getNSStringFromPUIPosterArbitrationBlockingReasonSymbolLoc
+ _getNSStringFromPUIPosterArbitrationBlockingReasonSymbolLoc.ptr
+ _getPFTFutureClass
+ _getPFTFutureClass.softClass
+ _soft_NSStringFromPUIPosterArbitrationBlockingReason
- GCC_except_table125
- GCC_except_table143
- GCC_except_table145
- GCC_except_table147
- GCC_except_table152
- GCC_except_table156
- GCC_except_table159
- GCC_except_table161
- GCC_except_table165
- GCC_except_table171
- GCC_except_table174
- GCC_except_table180
- GCC_except_table183
- GCC_except_table186
- GCC_except_table190
- GCC_except_table192
- GCC_except_table194
- GCC_except_table196
- GCC_except_table86
CStrings:
+ "Class getPFTFutureClass(void)_block_invoke"
+ "Lock screen presented; flushing the poster scene update now"
+ "LockScreenPresented"
+ "NSString *soft_NSStringFromPUIPosterArbitrationBlockingReason(PUIPosterArbitrationBlockingReason)"
+ "NSStringFromPUIPosterArbitrationBlockingReason"
+ "PBUITransferAlwaysImmediate"
+ "PFTFuture"
+ "[TransferAcknowledgement] wallpaper acknowledged the scene update for the move to %{public}@ after %.3f seconds"
+ "[TransferReadiness] _checkTransferReadiness: applicable scene changed since this wait started (was %{public}@, now %{public}@) -- giving up"
+ "[TransferReadiness] _checkTransferReadiness: became ready after %lu ticks (activeVariant=%{public}@) -- firing completion"
+ "[TransferReadiness] _checkTransferReadiness: still NOT ready after %lu ticks (%{public}@)"
+ "[TransferReadiness] gave up waiting for readiness"
+ "[TransferReadiness] notifyWhenReadyToTransferWithCompletion: NOT ready (%{public}@) -- deferring, will poll"
+ "[TransferReadiness] notifyWhenReadyToTransferWithCompletion: already ready (%{public}@)"
+ "[TransferReadiness] notifyWhenReadyToTransferWithCompletion: superseding an already-outstanding wait"
+ "activeVariant=%@ checkedScene=%@ (ownScene=%@) isRotating=%@ luminanceIsFull=%@ arbitrationBlockingReasons=%@"
+ "nil, fell back to counterpart"
+ "self"
+ "transfer readiness wait"
+ "v24@?0@8@\"NSError\"16"
+ "\xf0\xc1\xf0\xf1"
- "\xf0\xf0\xf0q"
```
