## cameracaptured

> `/usr/libexec/cameracaptured`

```diff

-  __TEXT.__text: 0x618
-  __TEXT.__auth_stubs: 0x2b0
+  __TEXT.__text: 0x530
+  __TEXT.__auth_stubs: 0x280
   __TEXT.__objc_stubs: 0x20
-  __TEXT.__const: 0x2c
-  __TEXT.__gcc_except_tab: 0x64
-  __TEXT.__oslogstring: 0x1f7
-  __TEXT.__cstring: 0x76
+  __TEXT.__const: 0x24
+  __TEXT.__gcc_except_tab: 0x50
+  __TEXT.__oslogstring: 0x106
+  __TEXT.__cstring: 0x71
   __TEXT.__objc_methname: 0x21
   __TEXT.__unwind_info: 0x78
-  __DATA_CONST.__auth_got: 0x168
+  __DATA_CONST.__auth_got: 0x150
   __DATA_CONST.__got: 0x38
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x50

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 4
-  Symbols:   54
-  CStrings:  15
+  Symbols:   51
+  CStrings:  13
 
Sections:
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__got : content changed
~ __DATA_CONST.__auth_ptr : content changed
~ __DATA_CONST.__const : content changed
~ __DATA.__objc_selrefs : content changed
Symbols:
- __os_log_send_and_compose_impl
- _fig_log_call_emit_and_clean_up_after_send_and_compose
- _fig_log_emitter_get_os_log_and_send_and_compose_flags_and_os_log_type
Functions:
~ sub_100000ad0 : 1332 -> 1100
CStrings:
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CameraCapture/CMCapture/Sources/cameracaptured/Resources-Embedded/cameracaptured.m %s: cannot listen for language changed notification (%d)"
- "main"

```
