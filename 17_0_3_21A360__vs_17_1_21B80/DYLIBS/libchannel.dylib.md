## libchannel.dylib

> `/usr/lib/libchannel.dylib`

```diff

-42.0.0.0.0
-  __TEXT.__text: 0x32f0
-  __TEXT.__auth_stubs: 0x420
+43.0.0.0.0
+  __TEXT.__text: 0x321c
+  __TEXT.__auth_stubs: 0x400
   __TEXT.__objc_methlist: 0x74
   __TEXT.__oslogstring: 0x1c7
   __TEXT.__const: 0x10
-  __TEXT.__gcc_except_tab: 0x254
-  __TEXT.__cstring: 0x157
-  __TEXT.__unwind_info: 0x254
+  __TEXT.__gcc_except_tab: 0x1c0
+  __TEXT.__cstring: 0xdd
+  __TEXT.__unwind_info: 0x230
   __TEXT.__eh_frame: 0x74
   __TEXT.__objc_classname: 0x42
   __TEXT.__objc_methname: 0x1e

   __DATA_CONST.__objc_selrefs: 0x18
   __AUTH_CONST.__objc_const: 0x120
   __AUTH_CONST.__const: 0xc0
-  __AUTH_CONST.__auth_got: 0x218
+  __AUTH_CONST.__auth_got: 0x208
   __AUTH.__objc_data: 0x140
   __DATA.__objc_classrefs: 0x20
   __DATA.__objc_superrefs: 0x20

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/librealtime_safety.dylib
   Functions: 149
-  Symbols:   386
-  CStrings:  28
+  Symbols:   380
+  CStrings:  25
 
Symbols:
- GCC_except_table1
- GCC_except_table12
- GCC_except_table15
- GCC_except_table16
- _realtime_runtime_check_pop_authorization
- _realtime_runtime_check_push_authorization
CStrings:
- "mach_msg with timeout=0 is RT safe"
- "mach_port_mod_refs is RT safe here"
- "os_crash is not realtime_safe, but crashing is okay"

```
