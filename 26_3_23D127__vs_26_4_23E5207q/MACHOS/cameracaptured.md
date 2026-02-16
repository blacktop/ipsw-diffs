## cameracaptured

> `/usr/libexec/cameracaptured`

```diff

-665.80.10.0.0
-  __TEXT.__text: 0x530
-  __TEXT.__auth_stubs: 0x280
+665.100.6.0.0
+  __TEXT.__text: 0x618
+  __TEXT.__auth_stubs: 0x2b0
   __TEXT.__objc_stubs: 0x20
-  __TEXT.__const: 0x24
-  __TEXT.__gcc_except_tab: 0x50
-  __TEXT.__oslogstring: 0x106
-  __TEXT.__cstring: 0x71
+  __TEXT.__const: 0x2c
+  __TEXT.__gcc_except_tab: 0x64
+  __TEXT.__oslogstring: 0x1f7
+  __TEXT.__cstring: 0x76
   __TEXT.__objc_methname: 0x21
   __TEXT.__unwind_info: 0x78
-  __DATA_CONST.__auth_got: 0x150
+  __DATA_CONST.__auth_got: 0x168
   __DATA_CONST.__got: 0x38
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x50

   - /System/Library/PrivateFrameworks/MediaSafetyNet.framework/MediaSafetyNet
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1DFE3989-F1EC-36D0-BA3E-3A9A855B1F97
+  UUID: 77DC8D2C-534C-3844-B531-4F3D4E54BC0C
   Functions: 4
-  Symbols:   51
-  CStrings:  13
+  Symbols:   54
+  CStrings:  15
 
Symbols:
+ __os_log_send_and_compose_impl
+ _fig_log_call_emit_and_clean_up_after_send_and_compose
+ _fig_log_emitter_get_os_log_and_send_and_compose_flags_and_os_log_type
Functions:
~ sub_100000ad0 : 1100 -> 1332
CStrings:
+ "/Library/Caches/com.apple.xbs/36C787BD-51D4-404A-A076-0F05B7B0FA6C/TemporaryDirectory.qH7drh/Sources/CameraCapture/CMCapture/Sources/cameracaptured/Resources-Embedded/cameracaptured.m %s: cannot listen for language changed notification (%d)"
+ "main"

```
