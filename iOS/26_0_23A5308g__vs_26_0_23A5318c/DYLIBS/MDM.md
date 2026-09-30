## MDM

> `/System/Library/PrivateFrameworks/MDM.framework/MDM`

```diff

-50.0.0.0.0
-  __TEXT.__text: 0x55d38
+52.0.0.0.0
+  __TEXT.__text: 0x55df4
   __TEXT.__auth_stubs: 0xf70
   __TEXT.__objc_methlist: 0x417c
   __TEXT.__const: 0x1a2
-  __TEXT.__gcc_except_tab: 0x1110
+  __TEXT.__gcc_except_tab: 0x1148
   __TEXT.__cstring: 0x5592
   __TEXT.__oslogstring: 0x6cfa
   __TEXT.__dlopen_cstrs: 0x55

   __TEXT.__swift5_capture: 0x68
   __TEXT.__swift_as_entry: 0xc
   __TEXT.__swift_as_ret: 0xc
-  __TEXT.__unwind_info: 0x1210
+  __TEXT.__unwind_info: 0x1218
   __TEXT.__eh_frame: 0x178
   __TEXT.__objc_classname: 0x6c4
-  __TEXT.__objc_methname: 0xeb2b
+  __TEXT.__objc_methname: 0xeb32
   __TEXT.__objc_methtype: 0x1b90
   __TEXT.__objc_stubs: 0xb9a0
   __DATA_CONST.__got: 0x11a8
-  __DATA_CONST.__const: 0x1f10
+  __DATA_CONST.__const: 0x1ee8
   __DATA_CONST.__objc_classlist: 0x190
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xb8

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: E9F6599F-98F2-3188-B1C8-7397073D1D99
+  UUID: 13491DBA-B347-32C3-ACC4-1E05BE84E29C
   Functions: 1647
   Symbols:   6659
   CStrings:  4263
Symbols:
+ GCC_except_table238
+ _objc_msgSend$waitForNetworkWithTimeout:strict:completionHandler:
- ___block_descriptor_40_e8_32s_e34_v16?0"DMCBackgroundTaskWrapper"8ls32l8
- _objc_msgSend$waitForNetworkWithCompletionHandler:timeout:
Functions:
~ -[MDMServerCore _syncBootstrapTokenToMDMWithToken:retryCount:completionHandler:] : 352 -> 368
~ -[MDMServerCore _memberQueueScheduleRRTSInactivityTaskWithInterval:] : 296 -> 380
~ ___68-[MDMServerCore _memberQueueScheduleRRTSInactivityTaskWithInterval:]_block_invoke : 12 -> 100
CStrings:
+ "waitForNetworkWithTimeout:strict:completionHandler:"
- "waitForNetworkWithCompletionHandler:timeout:"

```
