## cameracaptured

> `/usr/libexec/cameracaptured`

```diff

-587.122.6.0.2
-  __TEXT.__text: 0x530
-  __TEXT.__auth_stubs: 0x280
+587.140.7.122.2
+  __TEXT.__text: 0x650
+  __TEXT.__auth_stubs: 0x2c0
   __TEXT.__objc_stubs: 0x20
-  __TEXT.__const: 0x24
-  __TEXT.__gcc_except_tab: 0x50
-  __TEXT.__oslogstring: 0x106
-  __TEXT.__cstring: 0x71
+  __TEXT.__const: 0x2c
+  __TEXT.__gcc_except_tab: 0x6c
+  __TEXT.__oslogstring: 0x1b8
+  __TEXT.__cstring: 0x76
   __TEXT.__objc_methname: 0x21
   __TEXT.__unwind_info: 0x78
-  __DATA_CONST.__auth_got: 0x150
-  __DATA_CONST.__got: 0x38
+  __DATA_CONST.__auth_got: 0x170
+  __DATA_CONST.__got: 0x40
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8

   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6FA167CB-F5A7-351F-81B5-7ED7E59D711D
+  UUID: AD794CA2-CD38-3EA1-B2C0-28CE2D3EF660
   Functions: 4
-  Symbols:   51
-  CStrings:  13
+  Symbols:   56
+  CStrings:  15
 
Symbols:
+ ___stack_chk_fail
+ ___stack_chk_guard
+ __os_log_send_and_compose_impl
+ _fig_log_call_emit_and_clean_up_after_send_and_compose
+ _fig_log_emitter_get_os_log_and_send_and_compose_flags_and_os_log_type
Functions:
~ sub_100000ba0 : 1100 -> 1388
CStrings:
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/cameracaptured/Resources-Embedded/cameracaptured.m %s: cannot listen for language changed notification (%d)"
+ "main"

```
