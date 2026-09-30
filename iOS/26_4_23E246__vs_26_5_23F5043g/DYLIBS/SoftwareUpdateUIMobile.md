## SoftwareUpdateUIMobile

> `/System/Library/PrivateFrameworks/SoftwareUpdateUIMobile.framework/SoftwareUpdateUIMobile`

```diff

-508.100.174.0.0
-  __TEXT.__text: 0x786e4
+508.120.10.0.0
+  __TEXT.__text: 0x78b1c
   __TEXT.__auth_stubs: 0xcd0
   __TEXT.__objc_methlist: 0x259c
-  __TEXT.__cstring: 0x4027
-  __TEXT.__oslogstring: 0x7a8c
+  __TEXT.__cstring: 0x4087
+  __TEXT.__oslogstring: 0x7aec
   __TEXT.__gcc_except_tab: 0x4054
   __TEXT.__const: 0x3c0
   __TEXT.__constg_swiftt: 0xf0

   __TEXT.__swift5_capture: 0x240
   __TEXT.__swift_as_entry: 0x10
   __TEXT.__swift_as_ret: 0x8
-  __TEXT.__unwind_info: 0xd08
+  __TEXT.__unwind_info: 0xd10
   __TEXT.__eh_frame: 0x310
   __TEXT.__objc_classname: 0x681
   __TEXT.__objc_methname: 0x6fdb

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 1B5923C5-D90A-3709-ABA3-44826A7FE50C
-  Functions: 997
-  Symbols:   7121
-  CStrings:  2092
+  UUID: DC439CEB-1964-3C8A-B709-2CA5A3F87819
+  Functions: 999
+  Symbols:   7125
+  CStrings:  2094
 
Symbols:
+ GCC_except_table44
+ GCC_except_table81
+ ___83-[SUUIMobileStatefulUIManager client:downloadWasInvalidatedForNewUpdatesAvailable:]_block_invoke
+ ___os_log_helper_16_0_1_8_0
- GCC_except_table57
- GCC_except_table60
- GCC_except_table67
- GCC_except_table80
Functions:
~ -[SUUIMobileDownloadProgress isValidTimeRemaining:] : 192 -> 440
+ ___os_log_helper_16_0_1_8_0
~ -[SUUIMobileStatefulUIManager client:downloadWasInvalidatedForNewUpdatesAvailable:] : 2928 -> 3136
+ ___83-[SUUIMobileStatefulUIManager client:downloadWasInvalidatedForNewUpdatesAvailable:]_block_invoke
CStrings:
+ "-[SUUIMobileStatefulUIManager client:downloadWasInvalidatedForNewUpdatesAvailable:]_block_invoke"
+ "Time remaining is sub-second: %f seconds (will be clamped to 1.0 in UI), still considered as valid"

```
