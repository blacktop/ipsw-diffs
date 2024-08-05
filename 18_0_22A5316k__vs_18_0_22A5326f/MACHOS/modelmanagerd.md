## modelmanagerd

> `/usr/libexec/modelmanagerd`

```diff

-121.0.0.0.0
-  __TEXT.__text: 0x110298
-  __TEXT.__auth_stubs: 0x2cd0
+122.0.0.0.0
+  __TEXT.__text: 0x110e14
+  __TEXT.__auth_stubs: 0x2c90
   __TEXT.__const: 0x2450
   __TEXT.__cstring: 0x26ac
-  __TEXT.__swift5_typeref: 0x18f0
-  __TEXT.__swift5_capture: 0xa3c
+  __TEXT.__swift5_typeref: 0x18da
+  __TEXT.__swift5_capture: 0xa5c
   __TEXT.__objc_methname: 0x418
-  __TEXT.__oslogstring: 0x5cd5
+  __TEXT.__oslogstring: 0x5d75
   __TEXT.__swift5_entry: 0x8
   __TEXT.__constg_swiftt: 0x1b90
   __TEXT.__swift5_builtin: 0x14

   __TEXT.__swift5_assocty: 0xd0
   __TEXT.__objc_classname: 0x5b
   __TEXT.__objc_methtype: 0x191
-  __TEXT.__unwind_info: 0x4a40
-  __TEXT.__eh_frame: 0xeedc
-  __DATA_CONST.__auth_got: 0x1668
-  __DATA_CONST.__got: 0xba8
-  __DATA_CONST.__auth_ptr: 0x920
-  __DATA_CONST.__const: 0x2780
+  __TEXT.__unwind_info: 0x4a90
+  __TEXT.__eh_frame: 0xf01c
+  __DATA_CONST.__auth_got: 0x1648
+  __DATA_CONST.__got: 0xbc8
+  __DATA_CONST.__auth_ptr: 0x8c8
+  __DATA_CONST.__const: 0x2810
   __DATA_CONST.__objc_classlist: 0xf8
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA.__objc_const: 0x2ab0
   __DATA.__objc_selrefs: 0x138
   __DATA.__objc_data: 0x4b0
-  __DATA.__data: 0x4be0
+  __DATA.__data: 0x4c48
   __DATA.__common: 0x4d8
   __DATA.__bss: 0x3548
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftSystem.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 5048
-  Symbols:   1230
-  CStrings:  744
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 5093
+  Symbols:   1238
+  CStrings:  746
 
Symbols:
+ _$s20ModelManagerServices14InferenceErrorO20assetVersionMismatchyA2CmFWC
+ _$sSSs16TextOutputStreamsWP
+ _$ss13withTaskGroup2of9returning9isolation4bodyq_xm_q_mScA_pSgYiq_ScGyxGzYaXEtYas8SendableRzr0_lF
+ _$ss13withTaskGroup2of9returning9isolation4bodyq_xm_q_mScA_pSgYiq_ScGyxGzYaXEtYas8SendableRzr0_lFTu
+ _$ss21withThrowingTaskGroup2of9returning9isolation4bodyq_xm_q_mScA_pSgYiq_Scgyxs5Error_pGzYaKXEtYaKs8SendableRzr0_lF
+ _$ss21withThrowingTaskGroup2of9returning9isolation4bodyq_xm_q_mScA_pSgYiq_Scgyxs5Error_pGzYaKXEtYaKs8SendableRzr0_lFTu
+ _$ss23withCheckedContinuation9isolation8function_xScA_pSgYi_SSyScCyxs5NeverOGXEtYalF
+ _$ss23withCheckedContinuation9isolation8function_xScA_pSgYi_SSyScCyxs5NeverOGXEtYalFTu
+ _$ss27withTaskCancellationHandler9operation8onCancel9isolationxxyYaKXE_yyYbXEScA_pSgYitYaKlF
+ _$ss27withTaskCancellationHandler9operation8onCancel9isolationxxyYaKXE_yyYbXEScA_pSgYitYaKlFTu
+ _$ss31withCheckedThrowingContinuation9isolation8function_xScA_pSgYi_SSyScCyxs5Error_pGXEtYaKlF
+ _$ss31withCheckedThrowingContinuation9isolation8function_xScA_pSgYi_SSyScCyxs5Error_pGXEtYaKlFTu
+ _$ss5print_9separator10terminator2toyypd_S2Sxzts16TextOutputStreamRzlF
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
- _$s19CollectionsInternal10OrderedSetV11descriptionSSvg
- _$sScC12continuation8functionScCyxq_GSccyxq_G_SStcfC
- _$sScG22awaitAllRemainingTasksyyYaF
- _$sScG22awaitAllRemainingTasksyyYaFTu
- _$sScg22awaitAllRemainingTasksyyYaF
- _$sScg22awaitAllRemainingTasksyyYaFTu
- _$sScg9cancelAllyyF
- _$ss27withTaskCancellationHandler9operation8onCancelxxyYaKXE_yyYbXEtYaKlF
- _$ss27withTaskCancellationHandler9operation8onCancelxxyYaKXE_yyYbXEtYaKlFTu
- _swift_continuation_await
- _swift_continuation_init
- _swift_taskGroup_destroy
- _swift_taskGroup_initialize
CStrings:
+ "All remaining assets that need transitioning have failed to unload or move to dynamic, %!s(MISSING)"
+ "All remaining inactive assets that need purging have failed to unload or move to dynamic, %!s(MISSING)"
+ "Responding to request: %!s(MISSING) with assetVersionMismatch"
+ "While unloading assets for pending version change: all remaining assets failed to unload, %!s(MISSING)"
+ "nextAssetToUnloadToMakeRoom found dynamicBlocker but couldn't get asset for it %!s(MISSING)"
- "Additional assets should be transitioned but attempts to unload or move to dynamic have failed"
- "Additional inactive assets need purging but attempts to unload or move to dynamic have failed"
- "While unloading assets for pending version change: remaining assets failed to unload"

```
