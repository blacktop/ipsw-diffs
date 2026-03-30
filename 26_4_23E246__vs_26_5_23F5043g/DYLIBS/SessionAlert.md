## SessionAlert

> `/System/Library/PrivateFrameworks/SessionAlert.framework/SessionAlert`

```diff

-268.4.11.100.0
-  __TEXT.__text: 0x1c414
-  __TEXT.__auth_stubs: 0xb10
-  __TEXT.__const: 0x1bb2
-  __TEXT.__constg_swiftt: 0x5e4
-  __TEXT.__swift5_typeref: 0x6e2
-  __TEXT.__swift5_reflstr: 0x1e8
-  __TEXT.__swift5_fieldmd: 0x518
-  __TEXT.__swift5_builtin: 0x28
-  __TEXT.__swift5_types: 0x78
-  __TEXT.__cstring: 0x203
-  __TEXT.__swift5_protos: 0x14
-  __TEXT.__swift5_proto: 0x1b0
-  __TEXT.__swift5_capture: 0x20c
-  __TEXT.__oslogstring: 0x870
-  __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x6d8
-  __TEXT.__eh_frame: 0x488
+268.5.7.0.0
+  __TEXT.__text: 0x216cc
+  __TEXT.__auth_stubs: 0xbb0
+  __TEXT.__const: 0x1d12
+  __TEXT.__constg_swiftt: 0x6a0
+  __TEXT.__swift5_typeref: 0x74c
+  __TEXT.__swift5_reflstr: 0x268
+  __TEXT.__swift5_fieldmd: 0x568
+  __TEXT.__swift5_builtin: 0x3c
+  __TEXT.__swift5_types: 0x7c
+  __TEXT.__cstring: 0x243
+  __TEXT.__swift5_protos: 0x18
+  __TEXT.__swift5_proto: 0x1b4
+  __TEXT.__swift5_capture: 0x23c
+  __TEXT.__oslogstring: 0xa30
+  __TEXT.__swift5_mpenum: 0x18
+  __TEXT.__swift_as_entry: 0xc
+  __TEXT.__swift_as_ret: 0xc
+  __TEXT.__unwind_info: 0x7c8
+  __TEXT.__eh_frame: 0x7a8
   __TEXT.__objc_classname: 0x40
-  __TEXT.__objc_methname: 0xc2
+  __TEXT.__objc_methname: 0x102
   __TEXT.__objc_methtype: 0x7
-  __DATA_CONST.__got: 0x100
+  __DATA_CONST.__got: 0x120
   __DATA_CONST.__const: 0x68
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __AUTH_CONST.__auth_got: 0x588
-  __AUTH_CONST.__const: 0xfe0
-  __AUTH_CONST.__objc_const: 0x250
+  __AUTH_CONST.__auth_got: 0x5d8
+  __AUTH_CONST.__const: 0x1148
+  __AUTH_CONST.__objc_const: 0x290
   __AUTH.__data: 0xa0
-  __DATA.__data: 0x468
-  __DATA.__bss: 0x3280
-  __DATA_DIRTY.__data: 0x350
+  __DATA.__data: 0x490
+  __DATA.__bss: 0x3300
+  __DATA_DIRTY.__data: 0x3a8
   __DATA_DIRTY.__bss: 0x200
   - /System/Library/Frameworks/ActivityKit.framework/ActivityKit
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 9805711F-DDA2-39FB-A2BE-DFC0EB3E29F2
-  Functions: 643
-  Symbols:   367
-  CStrings:  57
+  UUID: 32416D4F-9B61-3308-9F59-0C687869196F
+  Functions: 713
+  Symbols:   399
+  CStrings:  65
 
Symbols:
+ ___swift_async_entry_functlets
+ ___swift_async_ret_functlets
+ ___swift_memcpy17_8
+ _block_copy_helper.120
+ _block_copy_helper.48
+ _block_copy_helper.60
+ _block_copy_helper.66
+ _block_descriptor.122
+ _block_descriptor.50
+ _block_descriptor.62
+ _block_descriptor.68
+ _block_destroy_helper.121
+ _block_destroy_helper.49
+ _block_destroy_helper.61
+ _block_destroy_helper.67
+ _get_enum_tag_for_layout_string 12SessionAlert12RemoteDeviceO
+ _objc_retain_x20
+ _objectdestroy.101Tm
+ _objectdestroy.131Tm
+ _objectdestroy.39Tm
+ _objectdestroy.55Tm
+ _swift_cvw_enumFn_getEnumTag
+ _swift_task_alloc
+ _swift_task_create
+ _swift_task_dealloc
+ _swift_task_switch
+ _swift_unknownObjectRelease_n
+ _symbolic $s12SessionAlert0B17ClientIdentifyingP
+ _symbolic Say_____G 12SessionAlert12RemoteDeviceO
+ _symbolic Say______pG 12SessionAlert0B17ClientIdentifyingP
+ _symbolic ScA_pSg
+ _symbolic ScPSg
+ _symbolic _____ 12SessionAlert12RemoteDeviceO
+ _symbolic ______p 12SessionAlert0B17ClientIdentifyingP
+ _symbolic _____ySnySiGG s23_ContiguousArrayStorageC
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 12SessionAlert12RemoteDeviceO
+ _symbolic _____y______pG s23_ContiguousArrayStorageC 12SessionAlert0E17ClientIdentifyingP
+ _symbolic ytIeAgHr_
+ _type_layout_string 12SessionAlert12RemoteDeviceO
- _block_copy_helper.92
- _block_descriptor.94
- _block_destroy_helper.93
- _objc_retain_x22
- _objc_retain_x26
- _objectdestroy.102Tm
- _objectdestroy.29Tm
- _objectdestroy.78Tm
- _swift_release_n
- _swift_weakDestroy
- _swift_weakInit
- _swift_weakLoadStrong
- _symbolic _____ 11ActivityKit8WatchdogC
- _symbolic _____Sg 12SessionAlert0B0V13FailureReasonO
- _symbolic _____SgXw 12SessionAlert0B6CenterC
- _symbolic _____SgXwz_Xx 12SessionAlert0B6CenterC
CStrings:
+ "(%{private}s): Client %{public}s did not present interrupting alert on local device: %{public}s"
+ "(%{private}s): Client %{public}s successfully presented interrupting alert on local device: %{public}s"
+ "(%{private}s): Local optional alert failed; retrying for additional remote device: %{public}s"
+ "(%{private}s): Remote device failed to show optional alert on device %{public}s; retrying as optional alert on remote device %{public}s: %{public}s"
+ "Attempting to present alert on %s clients: %s for alert: %{public}s"
+ "Client removed: %{public}s"
+ "New client added: %{public}s"
+ "Presenting alert to clients: "
+ "_queue_alertClients"
+ "_queue_sequencedRemotePresentationDevices"
+ "com.apple.liveactivities.additionalRemoteDevice."
- "(%{private}s): Attempting to present alert on local device: %{public}s"
- "(%{private}s): Sending failed optional alert to remote device: %{public}s"
- "Presenting alert"

```
