## libswift_Concurrency.dylib

> `/usr/lib/swift/libswift_Concurrency.dylib`

```diff

-6.0.3.1.6
-  __TEXT.__text: 0x6c538
-  __TEXT.__auth_stubs: 0xf50
+6.1.0.105.6
+  __TEXT.__text: 0x69cc4
+  __TEXT.__auth_stubs: 0xf60
   __TEXT.__init_offsets: 0xc
   __TEXT.__const: 0x2481
-  __TEXT.__cstring: 0x1b00
-  __TEXT.__swift5_typeref: 0xafc
+  __TEXT.__cstring: 0x1c4d
+  __TEXT.__swift5_typeref: 0xade
   __TEXT.__swift5_capture: 0x208
   __TEXT.__swift5_reflstr: 0x249
   __TEXT.__swift5_assocty: 0x6d8

   __TEXT.__swift5_mpenum: 0x10
   __TEXT.__swift5_protos: 0x20
   __TEXT.__swift5_proto: 0x1a4
-  __TEXT.__swift5_types: 0x150
+  __TEXT.__swift5_types: 0x14c
   __TEXT.__swift5_types2: 0x8
+  __TEXT.__swift_as_entry: 0x27c
+  __TEXT.__swift_as_ret: 0x328
   __TEXT.__oslogstring: 0x494
-  __TEXT.__unwind_info: 0x25f8
-  __TEXT.__eh_frame: 0x62e8
+  __TEXT.__unwind_info: 0x25b0
+  __TEXT.__eh_frame: 0x6250
   __DATA_CONST.__got: 0x218
   __DATA_CONST.__const: 0x1b8
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __AUTH_CONST.__auth_got: 0x7a8
-  __AUTH_CONST.__auth_ptr: 0x4a0
-  __AUTH_CONST.__const: 0x22c0
+  __AUTH_CONST.__auth_got: 0x7b0
+  __AUTH_CONST.__auth_ptr: 0x498
+  __AUTH_CONST.__const: 0x2220
   __AUTH_CONST.__objc_const: 0x370
   __AUTH.__data: 0x888
-  __DATA.__data: 0x668
-  __DATA.__bss: 0x4018
-  __DATA.__common: 0x40
+  __DATA.__data: 0x660
+  __DATA.__bss: 0x3e50
+  __DATA.__common: 0x58
   __DATA_DIRTY.__data: 0x170
-  __DATA_DIRTY.__common: 0x89
-  __DATA_DIRTY.__bss: 0x1840
+  __DATA_DIRTY.__bss: 0x1a88
+  __DATA_DIRTY.__common: 0x39
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
-  Functions: 2634
-  Symbols:   3830
-  CStrings:  192
+  Functions: 2670
+  Symbols:   3899
+  CStrings:  190
 
Symbols:
+ _$sSa15_checkSubscript_20wasNativeTypeCheckeds16_DependenceTokenVSi_SbtF
+ _$sSa29_hoistableIsNativeTypeCheckedSbyF
+ _$sSa8endIndexSivg
+ _$sSa9removeAll15keepingCapacityySb_tF
+ _$sScIsE4next7ElementQzSgyYa7FailureQzYKF
+ _$sScIsE4next7ElementQzSgyYa7FailureQzYKFTu
+ _$sScM21sharedUnownedExecutorScevpZMV
+ _$sScM6sharedScMvpZMV
+ _$sScP10backgroundScPvpZMV
+ _$sScP11unspecifiedScPvpZMV
+ _$sScP13userInitiatedScPvpZMV
+ _$sScP15userInteractiveScPvpZMV
+ _$sScP3lowScPvpZMV
+ _$sScP4highScPvpZMV
+ _$sScP6mediumScPvpZMV
+ _$sScP7defaultScPvpZMV
+ _$sScP7utilityScPvpZMV
+ _$sScTss5NeverORszABRs_rlE11isCancelledSbvpZMV
+ _$sScTss5NeverORszABRs_rlE12basePriorityScPSgvpZMV
+ _$sScTss5NeverORszABRs_rlE15currentPriorityScPvpZMV
+ _$ss12_ArrayBufferV19_getElementSlowPathyyXlSiF
+ _$ss15ContinuousClockV3nowAB7InstantVvpZMV
+ _$ss15ContinuousClockV7InstantV3nowADvpZMV
+ _$ss15SuspendingClockV3nowAB7InstantVvpZMV
+ _$ss15SuspendingClockV7InstantV3nowADvpZMV
+ _$ss9TaskLocalC18_enclosingInstance7wrapped7storagexs5NeverO_s24ReferenceWritableKeyPathCyAGxGAIyAgByxGGtcipZMV
+ __swift_concurrency_debug_internal_layout_version
+ _os_apt_msg_async_task_running_4swift
+ _os_apt_msg_async_task_waiting_on_4swift
+ _swift_retainCount
+ _swift_taskGroup_initializeWithOptions
+ _swift_task_deinitOnExecutor
+ _swift_task_donateThreadToGlobalExecutorUntil
+ _swift_task_donateThreadToGlobalExecutorUntil_hook
+ _swift_task_getMainExecutor_hook
+ _swift_task_invokeSwiftCheckIsolated
+ _swift_task_isCurrentExecutorWithFlags
+ _swift_task_isMainExecutor
+ _swift_task_isMainExecutor_hook
- _$sSS21_builtinStringLiteral17utf8CodeUnitCount7isASCIISSBp_BwBi1_tcfC
- _$sSlsE5first7ElementQzSgvg
- _$sSqMn
- __ZdlPvSt19__type_descriptor_t
- __ZnwmSt19__type_descriptor_t
- _concurrencyEnableJobDispatchIntegration
- _dispatch_async_f
- _swift_arrayDestroy
- _swift_unknownObjectRetain
CStrings:
+ " leaked its continuation without resuming it. This may cause tasks waiting on it to remain suspended forever.\n"
+ "<unknown>"
+ "Illegal attempt to set a TaskLocal value, use `withValue(...) { ... }` instead."
+ "Initializing continuation for task %p that was already initialized.\n"
+ "Not supported for Dispatch executor"
+ "Object %p of class %s deallocated with non-zero retain count %zd. This object's deinit, or something called from it, may have created a strong reference to self which outlived deinit, resulting in a dangling reference.\n"
+ "Resuming continuation for task %p that is not awaited (may have already been resumed).\n"
+ "__s61async_hook"
- " leaked its continuation!\n"
- " value, use `withValue(...) { ... }` instead."
- ")"
- ", "
- ", startSlot: "
- "@"
- "Illegal attempt to set a "
- "Initializing continuation context %p that was already initialized.\n"
- "Resuming continuation context %p that was not awaited (may have already been resumed).\n"
- "__s60async_hook"

```
