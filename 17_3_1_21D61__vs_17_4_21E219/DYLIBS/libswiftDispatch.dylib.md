## libswiftDispatch.dylib

> `/usr/lib/swift/libswiftDispatch.dylib`

```diff

-34.80.1.0.0
-  __TEXT.__text: 0x11fec
-  __TEXT.__auth_stubs: 0xac0
-  __TEXT.__const: 0x2420
+41.0.0.0.0
+  __TEXT.__text: 0x10960
+  __TEXT.__auth_stubs: 0xab0
+  __TEXT.__const: 0x23f0
   __TEXT.__cstring: 0x1a3
   __TEXT.__swift5_typeref: 0x6ce
   __TEXT.__swift5_capture: 0x29c

   __TEXT.__swift5_types: 0x80
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x9f8
+  __TEXT.__unwind_info: 0x8fc
   __TEXT.__eh_frame: 0x320
-  __DATA_CONST.__got: 0x178
+  __DATA_CONST.__got: 0x180
   __DATA_CONST.__const: 0x98
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0xe0
+  __DATA_CONST.__objc_classrefs: 0x18
   __AUTH_CONST.__const: 0x1ec8
   __AUTH_CONST.__auth_ptr: 0x10
-  __AUTH_CONST.__auth_got: 0x560
-  __DATA.__objc_classrefs: 0x18
-  __DATA.__data: 0x11e8
-  __DATA.__bss: 0x2100
+  __AUTH_CONST.__auth_got: 0x558
+  __DATA.__data: 0x11f8
+  __DATA.__bss: 0x2000
   __DATA.__common: 0x1
-  __DATA_DIRTY.__data: 0x2f8
+  __DATA_DIRTY.__data: 0x268
   __DATA_DIRTY.__bss: 0x780
   - /System/Library/Frameworks/Combine.framework/Combine
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  Functions: 1423
-  Symbols:   3573
+  Functions: 1411
+  Symbols:   3533
   CStrings:  15
 
Symbols:
+ _$s8Dispatch0A4DataV11DeallocatorOwCPTm
+ _$sIg_Ieg_TRTA.45
+ _$sIg_Ieg_TRTA.52
+ _$sIg_Ieg_TRTA.59
+ _$sIg_Ieg_TRTA.82
+ _$sScFsE7enqueueyyScJF
+ _$sScJyScJs11ExecutorJobVncfC
+ _$sSo17OS_dispatch_queueC8DispatchE23_asyncAfterUnsafeHelper33_F417D752D2C4E9330E1C700411CE0C6ALL8deadline3qos5flags7executeyAC0D4TimeV_AC0D3QoSVAC0D13WorkItemFlagsVyyXBtFTm
+ _$sSo18OS_dispatch_sourceC8DispatchE30makeExclavesNotificationSource10identifier9eventMask5queueSo0a1_b1_C22_exclaves_notification_pSu_s6UInt32VSo0a1_b1_L0CSgtFZ
+ _$sSo18OS_dispatch_sourceP8DispatchE15setEventHandler3qos5flags7handleryAC0D3QoSV_AC0D13WorkItemFlagsVyyXBSgtFTm
+ _$sSo33OS_dispatch_queue_serial_executorC8DispatchE7enqueueyys11ExecutorJobVnF
+ _$sSo33OS_dispatch_queue_serial_executorCScf8DispatchScf7enqueueyys11ExecutorJobVnFTWTm
+ _$sxs5Error_pIgrzo_xsAA_pIegrzo_lTRTA.78
+ __dispatch_source_type_exclaves_notification
+ _block_copy_helper.39
+ _block_copy_helper.46
+ _block_copy_helper.53
+ _block_copy_helper.60
+ _block_copy_helper.72
+ _block_copy_helper.83
+ _block_descriptor.41
+ _block_descriptor.48
+ _block_descriptor.55
+ _block_descriptor.62
+ _block_descriptor.74
+ _block_descriptor.85
+ _block_destroy_helper.40
+ _block_destroy_helper.47
+ _block_destroy_helper.54
+ _block_destroy_helper.61
+ _block_destroy_helper.73
+ _block_destroy_helper.84
+ _dispatch_concurrent_queue_create_with_target_4swift
- _$s8Dispatch0A3QoSV10backgroundACvpZ
- _$s8Dispatch0A3QoSV10background_WZ
- _$s8Dispatch0A3QoSV10background_Wz
- _$s8Dispatch0A3QoSV11unspecifiedACvgZTm
- _$s8Dispatch0A3QoSV11unspecifiedACvpZ
- _$s8Dispatch0A3QoSV11unspecified_WZ
- _$s8Dispatch0A3QoSV11unspecified_Wz
- _$s8Dispatch0A3QoSV13userInitiatedACvpZ
- _$s8Dispatch0A3QoSV13userInitiated_WZ
- _$s8Dispatch0A3QoSV13userInitiated_Wz
- _$s8Dispatch0A3QoSV15userInteractiveACvpZ
- _$s8Dispatch0A3QoSV15userInteractive_WZ
- _$s8Dispatch0A3QoSV15userInteractive_Wz
- _$s8Dispatch0A3QoSV7defaultACvpZ
- _$s8Dispatch0A3QoSV7default_WZ
- _$s8Dispatch0A3QoSV7default_Wz
- _$s8Dispatch0A3QoSV7utilityACvpZ
- _$s8Dispatch0A3QoSV7utility_WZ
- _$s8Dispatch0A3QoSV7utility_Wz
- _$s8Dispatch0A8WorkItemC4wait7timeoutAA0A13TimeoutResultOAA0A4TimeV_tFTm
- _$sIg_Ieg_TRTA.46
- _$sIg_Ieg_TRTA.53
- _$sIg_Ieg_TRTA.60
- _$sIg_Ieg_TRTA.83
- _$sScFsE7enqueueyys11ExecutorJobVnF
- _$sSo17OS_dispatch_queueC8DispatchE10asyncAfter8deadline7executeyAC0D4TimeV_AC0D8WorkItemCtFTm
- _$sSo17OS_dispatch_queueC8DispatchE23_asyncAfterUnsafeHelper33_F417D752D2C4E9330E1C700411CE0C6ALL12wallDeadline3qos5flags7executeyAC0D8WallTimeV_AC0D3QoSVAC0D13WorkItemFlagsVyyXBtF
- _$sSo18OS_dispatch_sourceC8DispatchE12ProcessEventV3all_WZTv_
- _$sSo18OS_dispatch_sourceC8DispatchE15FileSystemEventV3all_WZTv_
- _$sSo18OS_dispatch_sourceC8DispatchE19MemoryPressureEventV3all_WZTv_
- _$sSo33OS_dispatch_queue_serial_executorC8DispatchE7enqueueyyScJF
- _$sSo33OS_dispatch_queue_serial_executorCScf8DispatchScf7enqueueyyScJFTWTm
- _$ss10SetAlgebraPs7ElementQz012ArrayLiteralC0RtzrlE05arrayE0xAFd_tcfCSo14OS_dispatch_ioC8DispatchE10CloseFlagsV_Tg5
- _$ss10SetAlgebraPs7ElementQz012ArrayLiteralC0RtzrlE05arrayE0xAFd_tcfCSo14OS_dispatch_ioC8DispatchE13IntervalFlagsV_Tg5
- _$sxs5Error_pIgrzo_xsAA_pIegrzo_lTRTA.79
- _block_copy_helper.40
- _block_copy_helper.47
- _block_copy_helper.61
- _block_copy_helper.73
- _block_copy_helper.84
- _block_descriptor.42
- _block_descriptor.49
- _block_descriptor.63
- _block_descriptor.75
- _block_descriptor.86
- _block_destroy_helper.41
- _block_destroy_helper.48
- _block_destroy_helper.62
- _block_destroy_helper.74
- _block_destroy_helper.85
- _dispatch_serial_queue_create_with_target_4swiftTm
- _objc_retain_x22
- _swift_setDeallocating

```
