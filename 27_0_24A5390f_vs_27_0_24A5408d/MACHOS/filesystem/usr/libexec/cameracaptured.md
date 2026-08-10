## cameracaptured

> `/usr/libexec/cameracaptured`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_selrefs`

```diff

-761.0.0.0.3
-  __TEXT.__text: 0x700
-  __TEXT.__auth_stubs: 0x2d0
+764.22.5.122.2
+  __TEXT.__text: 0x628
+  __TEXT.__auth_stubs: 0x2a0
   __TEXT.__objc_stubs: 0xa0
-  __TEXT.__const: 0x34
-  __TEXT.__gcc_except_tab: 0x74
-  __TEXT.__oslogstring: 0x254
-  __TEXT.__cstring: 0x76
+  __TEXT.__const: 0x2c
+  __TEXT.__gcc_except_tab: 0x60
+  __TEXT.__oslogstring: 0x163
+  __TEXT.__cstring: 0x71
   __TEXT.__objc_methname: 0x7d
   __TEXT.__unwind_info: 0x80
   __DATA_CONST.__const: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0x178
+  __DATA_CONST.__auth_got: 0x160
   __DATA_CONST.__got: 0x50
   __DATA_CONST.__auth_ptr: 0x8
   __DATA.__objc_selrefs: 0x28

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 6
-  Symbols:   59
-  CStrings:  20
+  Symbols:   56
+  CStrings:  18
 
Symbols:
- __os_log_send_and_compose_impl
- _fig_log_call_emit_and_clean_up_after_send_and_compose
- _fig_log_emitter_get_os_log_and_send_and_compose_flags_and_os_log_type
Functions:
~ sub_100000ad0 : 1480 -> 1264
CStrings:
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CameraCapture/CMCapture/Sources/cameracaptured/Resources-Embedded/cameracaptured.m %s: cannot listen for language changed notification (%d)"
- "main"
```
