## libchannel.dylib

> `/usr/lib/libchannel.dylib`

```diff

 50.0.4.0.0
-  __TEXT.__text: 0x32e8
-  __TEXT.__auth_stubs: 0x420
+  __TEXT.__text: 0x31f8
+  __TEXT.__auth_stubs: 0x400
   __TEXT.__objc_methlist: 0x74
   __TEXT.__const: 0x28
-  __TEXT.__gcc_except_tab: 0x2a0
+  __TEXT.__gcc_except_tab: 0x200
   __TEXT.__oslogstring: 0x1c7
-  __TEXT.__cstring: 0x157
-  __TEXT.__unwind_info: 0x290
+  __TEXT.__cstring: 0xdd
+  __TEXT.__unwind_info: 0x268
   __TEXT.__objc_classname: 0x42
   __TEXT.__objc_methname: 0x1e
   __TEXT.__objc_methtype: 0x11

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x218
+  __AUTH_CONST.__auth_got: 0x208
   __AUTH_CONST.__const: 0xc0
   __AUTH_CONST.__objc_const: 0x240
   __AUTH.__objc_data: 0x140

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/librealtime_safety.dylib
   Functions: 139
-  Symbols:   227
-  CStrings:  28
+  Symbols:   225
+  CStrings:  25
 
Symbols:
- _realtime_runtime_check_pop_authorization
- _realtime_runtime_check_push_authorization
CStrings:
- "mach_msg with timeout=0 is RT safe"
- "mach_port_mod_refs is RT safe here"
- "os_crash is not realtime_safe, but crashing is okay"

```
